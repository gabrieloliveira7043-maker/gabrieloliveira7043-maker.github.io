/* Worker "caderno-admin": faz pelo servidor o que o navegador não pode no Firebase do Caderno de Prática.
   Senhas
   - POST /create-user        { login, password } cria o login de um aluno            (professora logada)
   - POST /set-password       { uid, password }  troca a senha de um aluno            (professora logada)
   - POST /delete-user        { uid }            apaga o login e os anexos de um aluno (professora logada)
   - POST /reset-professor    { password }       troca a senha da professora          (só com o ADMIN_TOKEN)
   Anexos das tarefas (vídeo e foto, guardados no R2)
   - POST /upload?task=ID     corpo = arquivo    envia um anexo        (aluno dono da tarefa ou professora)
   - POST /file-urls          { task }           links temporários     (aluno dono da tarefa ou professora)
   - GET  /file?k=&e=&s=                         abre o arquivo pelo link temporário (aceita Range, para vídeo)
   - POST /delete-file        { task, key }      apaga um anexo        (aluno dono, antes de revisada, ou professora)
   - POST /delete-task-files  { task }           apaga todos os anexos de uma tarefa (professora)
   - GET  /health
   Segredos (wrangler secret put): SA_JSON, ADMIN_TOKEN, FILE_SECRET.
   Variáveis e R2 (wrangler.toml): PROJECT_ID, ALLOWED_ORIGINS e o bucket ANEXOS. */

const enc = new TextEncoder();
const MB = 1024 * 1024;
const LIMITE = { video: 90 * MB, image: 15 * MB, porTarefa: 3, total: 9 * 1024 * MB };
// só estes formatos entram (SVG e HTML ficam de fora: poderiam levar código junto)
const TIPOS = {
  "image/jpeg": "image", "image/png": "image", "image/webp": "image", "image/heic": "image", "image/heif": "image", "image/gif": "image",
  "video/mp4": "video", "video/quicktime": "video", "video/webm": "video", "video/3gpp": "video", "video/x-m4v": "video",
};
const UID_OK = /^[A-Za-z0-9]{1,128}$/;

// compara sem vazar pelo tempo de resposta quantos caracteres batem
function igual(a, b) {
  a = String(a); b = String(b);
  let d = a.length ^ b.length;
  for (let i = 0; i < Math.max(a.length, b.length); i++) d |= (a.charCodeAt(i) | 0) ^ (b.charCodeAt(i) | 0);
  return d === 0;
}

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
class Erro extends Error { constructor(status, msg) { super(msg); this.status = status; } }

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

/* ---------- Firestore (API REST com a conta de serviço; ignora as regras de segurança) ---------- */
function fromFs(v) {
  if (!v) return null;
  if ("stringValue" in v) return v.stringValue;
  if ("integerValue" in v) return Number(v.integerValue);
  if ("doubleValue" in v) return v.doubleValue;
  if ("booleanValue" in v) return v.booleanValue;
  if ("nullValue" in v) return null;
  if ("arrayValue" in v) return (v.arrayValue.values || []).map(fromFs);
  if ("mapValue" in v) { const o = {}; for (const [k, x] of Object.entries(v.mapValue.fields || {})) o[k] = fromFs(x); return o; }
  return null;
}
function toFs(x) {
  if (x === null || x === undefined) return { nullValue: null };
  if (typeof x === "string") return { stringValue: x };
  if (typeof x === "boolean") return { booleanValue: x };
  if (typeof x === "number") return Number.isInteger(x) ? { integerValue: String(x) } : { doubleValue: x };
  if (Array.isArray(x)) return { arrayValue: { values: x.map(toFs) } };
  const fields = {}; for (const [k, v] of Object.entries(x)) fields[k] = toFs(v);
  return { mapValue: { fields } };
}
function docUrl(env, path) { return `https://firestore.googleapis.com/v1/projects/${env.PROJECT_ID}/databases/(default)/documents/${path}`; }
async function readDoc(env, path) {
  const res = await fetch(docUrl(env, path), { headers: { Authorization: "Bearer " + await googleToken(env) } });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error("firestore " + res.status);
  const out = {};
  for (const [k, v] of Object.entries((await res.json()).fields || {})) out[k] = fromFs(v);
  return out;
}
async function patchDoc(env, path, data) {
  const mask = Object.keys(data).map((k) => "updateMask.fieldPaths=" + encodeURIComponent(k)).join("&");
  const fields = {}; for (const [k, v] of Object.entries(data)) fields[k] = toFs(v);
  const res = await fetch(docUrl(env, path) + "?" + mask, {
    method: "PATCH", headers: { Authorization: "Bearer " + await googleToken(env), "Content-Type": "application/json" },
    body: JSON.stringify({ fields }),
  });
  if (!res.ok) throw new Error("firestore " + res.status);
}
async function authAdmin(env, action, body) {
  const res = await fetch(`https://identitytoolkit.googleapis.com/v1/projects/${env.PROJECT_ID}/accounts:${action}`, {
    method: "POST", headers: { Authorization: "Bearer " + await googleToken(env), "Content-Type": "application/json" }, body: JSON.stringify(body),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error((data.error && data.error.message) || "auth " + res.status);
  return data;
}
// cria o login com a conta de serviço: funciona mesmo com o cadastro público do Firebase desligado
async function criarLogin(env, email, password) {
  const res = await fetch("https://identitytoolkit.googleapis.com/v1/accounts:signUp", {
    method: "POST", headers: { Authorization: "Bearer " + await googleToken(env), "Content-Type": "application/json" },
    body: JSON.stringify({ targetProjectId: env.PROJECT_ID, email, password }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok || !data.localId) throw new Error((data.error && data.error.message) || "auth " + res.status);
  return data;
}
async function professorUid(env) { const f = await readDoc(env, "config/professor"); return f ? f.uid : null; }

/* espaço usado no R2, guardado em config/storage para não precisar listar o bucket a cada envio */
async function addUsage(env, delta) {
  const cur = (await readDoc(env, "config/storage")) || {};
  await patchDoc(env, "config/storage", { bytes: Math.max(0, (cur.bytes || 0) + delta), updatedAt: Date.now() });
}

/* ---------- links temporários para abrir os arquivos ---------- */
async function hmac(env, msg) {
  const key = await crypto.subtle.importKey("raw", enc.encode(env.FILE_SECRET), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return b64url(await crypto.subtle.sign("HMAC", key, enc.encode(msg)));
}
async function signedUrl(env, base, key) {
  const exp = Math.floor(Date.now() / 1000) + 3600;
  return `${base}/file?k=${encodeURIComponent(key)}&e=${exp}&s=${await hmac(env, key + ":" + exp)}`;
}
async function serveFile(env, req, url) {
  const key = url.searchParams.get("k") || "", exp = Number(url.searchParams.get("e") || 0), sig = url.searchParams.get("s") || "";
  if (!key || exp < Date.now() / 1000 || !igual(sig, await hmac(env, key + ":" + exp))) return new Response("link inválido ou vencido", { status: 403 });
  const obj = await env.ANEXOS.get(key, { range: req.headers });
  if (!obj) return new Response("não encontrado", { status: 404 });
  const h = new Headers();
  obj.writeHttpMetadata(h);
  h.set("ETag", obj.httpEtag); h.set("Accept-Ranges", "bytes"); h.set("Cache-Control", "private, max-age=3600");
  // o arquivo é só mídia: o navegador não adivinha outro tipo nem roda código vindo dele
  if (!TIPOS[(h.get("Content-Type") || "").toLowerCase()]) h.set("Content-Type", "application/octet-stream");
  h.set("X-Content-Type-Options", "nosniff");
  h.set("Content-Security-Policy", "default-src 'none'; img-src 'self'; media-src 'self'; style-src 'unsafe-inline'; sandbox");
  h.set("Referrer-Policy", "no-referrer");
  let status = 200;
  if (obj.range && req.headers.get("Range")) {
    const off = obj.range.offset !== undefined ? obj.range.offset : obj.size - obj.range.suffix;
    const len = obj.range.length !== undefined ? obj.range.length : obj.size - off;
    h.set("Content-Range", `bytes ${off}-${off + len - 1}/${obj.size}`); h.set("Content-Length", String(len));
    status = 206;
  }
  return new Response(obj.body, { status, headers: h });
}

/* ---------- regras de quem pode mexer nos anexos de uma tarefa ---------- */
async function taskFor(env, caller, taskId, paraApagar) {
  if (!/^[\w-]{1,128}$/.test(taskId)) throw new Erro(400, "tarefa inválida");
  const task = await readDoc(env, "tasks/" + taskId);
  if (!task) throw new Erro(404, "tarefa não encontrada");
  const prof = await professorUid(env);
  const isProf = caller === prof;
  if (!isProf && caller !== task.uid) throw new Erro(403, "não autorizado");
  if (!isProf && paraApagar && task.status === "reviewed") throw new Erro(403, "tarefa já revisada");
  return { task, isProf };
}
async function deleteFiles(env, items) {
  if (!items.length) return 0;
  await env.ANEXOS.delete(items.map((a) => a.key));
  return items.reduce((s, a) => s + (a.size || 0), 0);
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url), path = url.pathname, base = url.origin;
    const origin = req.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((o) => o.trim()).filter(Boolean);
    const cors = allowed.includes(origin)
      ? { "Access-Control-Allow-Origin": origin, "Access-Control-Allow-Headers": "Authorization, Content-Type, X-File-Name", "Access-Control-Allow-Methods": "POST, GET, OPTIONS", Vary: "Origin" }
      : {};
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    try {
      if (path === "/health") return json({ ok: true }, 200, cors);
      if (path === "/file" && req.method === "GET") return await serveFile(env, req, url);
      if (req.method !== "POST") return json({ error: "método não permitido" }, 405, cors);

      if (path === "/reset-professor") {
        const body = await req.json().catch(() => ({}));
        if (!env.ADMIN_TOKEN || !igual(req.headers.get("Authorization") || "", "Bearer " + env.ADMIN_TOKEN)) return json({ error: "não autorizado" }, 401, cors);
        if (String(body.password || "").length < 6) return json({ error: "senha com menos de 6 caracteres" }, 400, cors);
        const uid = await professorUid(env);
        if (!uid) return json({ error: "a conta de professora ainda não existe" }, 404, cors);
        await authAdmin(env, "update", { localId: uid, password: body.password });
        return json({ ok: true }, 200, cors);
      }

      // daqui para baixo: precisa estar logado no caderno
      const caller = await verifyIdToken((req.headers.get("Authorization") || "").replace(/^Bearer /, ""), env.PROJECT_ID).catch(() => null);
      if (!caller) return json({ error: "não autorizado" }, 403, cors);

      if (path === "/upload") {
        const taskId = url.searchParams.get("task") || "";
        const { task } = await taskFor(env, caller, taskId, true);
        const type = (req.headers.get("Content-Type") || "").split(";")[0].trim().toLowerCase();
        const size = Number(req.headers.get("Content-Length") || 0);
        const kind = TIPOS[type] || null;
        if (!kind) return json({ error: "envie só vídeo (MP4, MOV) ou foto (JPG, PNG, HEIC)" }, 400, cors);
        if (!size) return json({ error: "arquivo vazio" }, 400, cors);
        if (size > LIMITE[kind]) return json({ error: kind === "video" ? "vídeo maior que 90 MB" : "foto maior que 15 MB" }, 413, cors);
        const atts = task.attachments || [];
        if (atts.length >= LIMITE.porTarefa) return json({ error: "no máximo 3 anexos por tarefa" }, 400, cors);
        const usage = (await readDoc(env, "config/storage")) || {};
        if ((usage.bytes || 0) + size > LIMITE.total) return json({ error: "espaço de anexos cheio; fale com o professor" }, 507, cors);
        const name = decodeURIComponent(req.headers.get("X-File-Name") || "anexo").slice(0, 120);
        const ext = (name.match(/\.([a-z0-9]{1,5})$/i) || [, kind === "video" ? "mp4" : "jpg"])[1].toLowerCase();
        const key = `anexos/${task.uid}/${taskId}/${Date.now()}-${crypto.randomUUID().slice(0, 8)}.${ext}`;
        const salvo = await env.ANEXOS.put(key, req.body, { httpMetadata: { contentType: type } });
        // confere o tamanho que realmente chegou, não só o que o navegador declarou
        if (!salvo || salvo.size > LIMITE[kind]) { await env.ANEXOS.delete(key); return json({ error: "arquivo maior que o permitido" }, 413, cors); }
        const item = { key, name, type, size: salvo.size, at: Date.now(), by: caller };
        await patchDoc(env, "tasks/" + taskId, { attachments: atts.concat([item]) });
        await addUsage(env, salvo.size);
        return json({ ok: true, item }, 200, cors);
      }

      const body = await req.json().catch(() => ({}));

      if (path === "/file-urls") {
        const { task } = await taskFor(env, caller, String(body.task || ""), false);
        const urls = {};
        for (const a of task.attachments || []) urls[a.key] = await signedUrl(env, base, a.key);
        return json({ ok: true, urls }, 200, cors);
      }
      if (path === "/delete-file") {
        const taskId = String(body.task || "");
        const { task } = await taskFor(env, caller, taskId, true);
        const atts = task.attachments || [], alvo = atts.filter((a) => a.key === body.key);
        if (!alvo.length) return json({ error: "anexo não encontrado" }, 404, cors);
        const freed = await deleteFiles(env, alvo);
        await patchDoc(env, "tasks/" + taskId, { attachments: atts.filter((a) => a.key !== body.key) });
        await addUsage(env, -freed);
        return json({ ok: true }, 200, cors);
      }

      // daqui para baixo: só a professora
      if (caller !== (await professorUid(env))) return json({ error: "não autorizado" }, 403, cors);

      if (path === "/delete-task-files") {
        const taskId = String(body.task || "");
        const { task } = await taskFor(env, caller, taskId, true);
        const freed = await deleteFiles(env, task.attachments || []);
        await patchDoc(env, "tasks/" + taskId, { attachments: [] });
        await addUsage(env, -freed);
        return json({ ok: true }, 200, cors);
      }

      if (path === "/create-user") {
        // o cadastro aberto do Firebase fica desligado; só a professora cria logins, por aqui
        const login = String(body.login || "").toLowerCase();
        if (!/^[a-z0-9._-]{3,30}$/.test(login)) return json({ error: "usuário inválido" }, 400, cors);
        if (String(body.password || "").length < 6) return json({ error: "senha com menos de 6 caracteres" }, 400, cors);
        try {
          const novo = await criarLogin(env, login + "@aluno.caderno", String(body.password));
          return json({ ok: true, uid: novo.localId }, 200, cors);
        } catch (e) {
          if (/EMAIL_EXISTS/.test(e.message)) return json({ error: "Esse usuário já existe.", code: "email-already-in-use" }, 409, cors);
          throw e;
        }
      }

      const uid = String(body.uid || "");
      if (!UID_OK.test(uid) || uid === caller) return json({ error: "aluno inválido" }, 400, cors);
      if (!(await readDoc(env, "students/" + uid))) return json({ error: "aluno não encontrado" }, 404, cors);

      if (path === "/set-password") {
        if (String(body.password || "").length < 6) return json({ error: "senha com menos de 6 caracteres" }, 400, cors);
        await authAdmin(env, "update", { localId: uid, password: body.password });
        return json({ ok: true }, 200, cors);
      }
      if (path === "/delete-user") {
        let freed = 0, cursor;
        do {
          const list = await env.ANEXOS.list({ prefix: `anexos/${uid}/`, cursor });
          if (list.objects.length) { await env.ANEXOS.delete(list.objects.map((o) => o.key)); freed += list.objects.reduce((s, o) => s + o.size, 0); }
          cursor = list.truncated ? list.cursor : undefined;
        } while (cursor);
        if (freed) await addUsage(env, -freed);
        await authAdmin(env, "delete", { localId: uid }).catch((e) => { if (!/USER_NOT_FOUND/.test(e.message)) throw e; });
        return json({ ok: true }, 200, cors);
      }
      return json({ error: "rota não encontrada" }, 404, cors);
    } catch (e) {
      // erros esperados (Erro) explicam o motivo; os internos não expõem detalhes do servidor
      if (e instanceof Erro) return json({ error: e.message }, e.status, cors);
      console.error(e);
      return json({ error: "Falha no servidor. Tente de novo." }, 500, cors);
    }
  },
};
