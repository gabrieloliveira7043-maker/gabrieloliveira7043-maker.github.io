/* Worker "caderno-admin": faz pelo servidor o que o navegador não pode no Firebase do Caderno de Prática.
   - POST /set-password      { uid, password }  troca a senha de um aluno (só a professora, logada)
   - POST /delete-user       { uid }            apaga o login de um aluno (só a professora, logada)
   - POST /reset-professor   { password }       troca a senha da conta de professora (só com o ADMIN_TOKEN)
   - GET  /health                               teste rápido
   Segredos (wrangler secret put): SA_JSON (arquivo da conta de serviço do Firebase) e ADMIN_TOKEN.
   Variáveis (wrangler.toml): PROJECT_ID e ALLOWED_ORIGINS. */

const enc = new TextEncoder();

function b64url(bytes) {
  let s = "";
  for (const b of new Uint8Array(bytes)) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function b64urlDecode(str) {
  const s = str.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((str.length + 3) % 4);
  return Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
}
function json(body, status, cors) {
  return new Response(JSON.stringify(body), { status: status || 200, headers: { "Content-Type": "application/json", ...cors } });
}

/* ---------- token de acesso do Google a partir da conta de serviço ---------- */
let cachedToken = null;
async function googleToken(env) {
  if (cachedToken && cachedToken.exp > Date.now() / 1000 + 60) return cachedToken.value;
  const sa = JSON.parse(env.SA_JSON);
  const now = Math.floor(Date.now() / 1000);
  const head = b64url(enc.encode(JSON.stringify({ alg: "RS256", typ: "JWT" })));
  const claim = b64url(enc.encode(JSON.stringify({
    iss: sa.client_email, scope: "https://www.googleapis.com/auth/cloud-platform",
    aud: "https://oauth2.googleapis.com/token", iat: now, exp: now + 3600,
  })));
  const pem = sa.private_key.replace(/-----[^-]+-----/g, "").replace(/\s+/g, "");
  const key = await crypto.subtle.importKey("pkcs8", b64urlDecode(pem.replace(/\+/g, "-").replace(/\//g, "_")),
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", key, enc.encode(head + "." + claim));
  const res = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: "grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=" + head + "." + claim + "." + b64url(sig),
  });
  const data = await res.json();
  if (!data.access_token) throw new Error("token do Google: " + JSON.stringify(data));
  cachedToken = { value: data.access_token, exp: now + (data.expires_in || 3600) };
  return cachedToken.value;
}

/* ---------- confere o login (ID token do Firebase) de quem chamou ---------- */
let jwks = null;
async function verifyIdToken(token, projectId) {
  const [h, p, s] = String(token || "").split(".");
  if (!s) throw new Error("sem token");
  const header = JSON.parse(new TextDecoder().decode(b64urlDecode(h)));
  const payload = JSON.parse(new TextDecoder().decode(b64urlDecode(p)));
  const now = Math.floor(Date.now() / 1000);
  if (payload.aud !== projectId || payload.iss !== "https://securetoken.google.com/" + projectId) throw new Error("token de outro projeto");
  if (payload.exp < now || payload.iat > now + 300 || !payload.sub) throw new Error("token vencido");
  if (!jwks || !jwks.keys.some((k) => k.kid === header.kid)) {
    jwks = await (await fetch("https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com")).json();
  }
  const jwk = jwks.keys.find((k) => k.kid === header.kid);
  if (!jwk) throw new Error("chave desconhecida");
  const key = await crypto.subtle.importKey("jwk", jwk, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]);
  const ok = await crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, b64urlDecode(s), enc.encode(h + "." + p));
  if (!ok) throw new Error("assinatura inválida");
  return payload.sub;
}

/* ---------- Firestore e Firebase Auth (API REST com a conta de serviço) ---------- */
async function readDoc(env, path) {
  const tok = await googleToken(env);
  const res = await fetch(`https://firestore.googleapis.com/v1/projects/${env.PROJECT_ID}/databases/(default)/documents/${path}`,
    { headers: { Authorization: "Bearer " + tok } });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error("firestore " + res.status);
  return (await res.json()).fields || {};
}
async function authAdmin(env, action, body) {
  const tok = await googleToken(env);
  const res = await fetch(`https://identitytoolkit.googleapis.com/v1/projects/${env.PROJECT_ID}/accounts:${action}`, {
    method: "POST", headers: { Authorization: "Bearer " + tok, "Content-Type": "application/json" }, body: JSON.stringify(body),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error((data.error && data.error.message) || "auth " + res.status);
  return data;
}
async function professorUid(env) {
  const f = await readDoc(env, "config/professor");
  return f && f.uid ? f.uid.stringValue : null;
}

export default {
  async fetch(req, env) {
    const origin = req.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((o) => o.trim()).filter(Boolean);
    const cors = allowed.includes(origin)
      ? { "Access-Control-Allow-Origin": origin, "Access-Control-Allow-Headers": "Authorization, Content-Type", "Access-Control-Allow-Methods": "POST, GET, OPTIONS", Vary: "Origin" }
      : {};
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    const path = new URL(req.url).pathname;
    try {
      if (path === "/health") return json({ ok: true }, 200, cors);
      if (req.method !== "POST") return json({ error: "método não permitido" }, 405, cors);
      const body = await req.json().catch(() => ({}));

      if (path === "/reset-professor") {
        if (!env.ADMIN_TOKEN || req.headers.get("Authorization") !== "Bearer " + env.ADMIN_TOKEN) return json({ error: "não autorizado" }, 401, cors);
        if (String(body.password || "").length < 6) return json({ error: "senha com menos de 6 caracteres" }, 400, cors);
        const uid = await professorUid(env);
        if (!uid) return json({ error: "a conta de professora ainda não existe" }, 404, cors);
        await authAdmin(env, "update", { localId: uid, password: body.password });
        return json({ ok: true }, 200, cors);
      }

      // as outras rotas: só a professora logada no caderno
      const caller = await verifyIdToken((req.headers.get("Authorization") || "").replace(/^Bearer /, ""), env.PROJECT_ID)
        .catch(() => null);
      if (!caller || caller !== (await professorUid(env))) return json({ error: "não autorizado" }, 403, cors);
      const uid = String(body.uid || "");
      if (!uid || uid === caller) return json({ error: "aluno inválido" }, 400, cors);
      if (!(await readDoc(env, "students/" + uid))) return json({ error: "aluno não encontrado" }, 404, cors);

      if (path === "/set-password") {
        if (String(body.password || "").length < 6) return json({ error: "senha com menos de 6 caracteres" }, 400, cors);
        await authAdmin(env, "update", { localId: uid, password: body.password });
        return json({ ok: true }, 200, cors);
      }
      if (path === "/delete-user") {
        await authAdmin(env, "delete", { localId: uid });
        return json({ ok: true }, 200, cors);
      }
      return json({ error: "rota não encontrada" }, 404, cors);
    } catch (e) {
      return json({ error: String(e.message || e) }, 500, cors);
    }
  },
};
