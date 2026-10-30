# Worker `caderno-admin` — passo a passo

Worker do Cloudflare que faz pelo servidor o que o navegador não pode no Firebase do **Caderno de Prática**
(projeto Firebase `caderno-de-pratica`, separado do Firebase do CRM). É o mesmo esquema do `huven-crm-admin`
com a rota `/set-password`.

| Rota | Quem pode | O que faz |
|---|---|---|
| `GET /health` | qualquer um | teste rápido |
| `POST /set-password` `{ uid, password }` | só a professora logada no caderno | troca a senha de um aluno |
| `POST /delete-user` `{ uid }` | só a professora logada no caderno | apaga o login de um aluno |
| `POST /reset-professor` `{ password }` | só com o `ADMIN_TOKEN` | troca a senha da conta de professora |

A professora é reconhecida pelo token de login do Firebase (`Authorization: Bearer <idToken>`), conferido contra
o documento `config/professor` do Firestore. O código já foi testado contra o projeto real, menos as chamadas
com a conta de serviço verdadeira (que só existe depois do passo 2).

## 1. Acesso necessário

- Conta do Cloudflare (a mesma do CRM).
- Acesso ao projeto Firebase `caderno-de-pratica`: o Gabriel adiciona você em
  **Configurações do projeto → Usuários e permissões → Adicionar membro** (papel **Proprietário**).
- Node.js 18 ou mais novo e este repositório clonado.

## 2. Chave da conta de serviço do Firebase

1. Console do Firebase → projeto `caderno-de-pratica` → engrenagem → **Configurações do projeto → Contas de serviço**.
2. **Gerar nova chave privada** → baixa um `.json`.
3. **Não** coloque esse arquivo no repositório. Ele dá acesso total ao projeto.

## 3. Publicar o Worker

```bash
cd caderno-de-pratica/worker
npx wrangler login
npx wrangler secret put SA_JSON < caminho/para/chave-baixada.json
npx wrangler secret put ADMIN_TOKEN
npx wrangler deploy
```

- Em `ADMIN_TOKEN`, cole uma senha longa e aleatória (ex.: gerada por um gerenciador de senhas). Guarde-a num
  lugar seguro: ela é a única forma de redefinir a senha da professora.
- O `deploy` mostra a URL, algo como `https://caderno-admin.<sua-conta>.workers.dev`.
- Depois de publicar, **apague o `.json` do computador**. A chave fica guardada só como segredo do Worker.

## 4. Testar

```bash
curl https://caderno-admin.<sua-conta>.workers.dev/health
```

Deve responder `{"ok":true}`.

Redefinir a senha da professora (quando ela esquecer):

```bash
curl -X POST https://caderno-admin.<sua-conta>.workers.dev/reset-professor \
  -H "Authorization: Bearer <ADMIN_TOKEN>" -H "Content-Type: application/json" \
  -d "{\"password\":\"NovaSenha123\"}"
```

Deve responder `{"ok":true}`. Depois disso, a professora entra com o usuário `rachelprofi` e a senha nova.

## 5. Ligar no caderno

Mande a URL do Worker para o Gabriel. Com ela, o caderno passa a usar `/set-password` e `/delete-user` na janela
**Acesso do aluno**, para trocar a senha de qualquer aluno sem precisar saber a antiga.

## Observações

- `ALLOWED_ORIGINS` em `wrangler.toml` lista os sites que podem chamar o Worker pelo navegador. Se o caderno mudar de
  endereço, acrescente o novo e rode `npx wrangler deploy` de novo.
- O plano gratuito do Workers (100 mil requisições por dia, por conta) é compartilhado com os Workers do CRM; o
  caderno usa muito pouco.
- Para trocar a chave no futuro: gere outra no Firebase, rode `npx wrangler secret put SA_JSON` com o arquivo novo e
  apague a chave antiga em **Contas de serviço → Gerenciar permissões da conta de serviço**.
