# Worker `caderno-admin` — passo a passo

Worker do Cloudflare que faz pelo servidor o que o navegador não pode no Firebase do **Caderno de Prática**
(projeto Firebase `caderno-de-pratica`, separado do CRM). Faz duas coisas:

1. **Senhas** — o mesmo esquema do `huven-crm-admin` (`/set-password`): a professora troca a senha de qualquer
   aluno sem saber a antiga, e dá para redefinir a senha da própria professora.
2. **Anexos** — o aluno envia vídeo e foto da prática na tarefa; os arquivos ficam no **R2**.

| Rota | Quem pode | O que faz |
|---|---|---|
| `GET /health` | qualquer um | teste rápido |
| `POST /set-password` `{ uid, password }` | professora | troca a senha de um aluno |
| `POST /delete-user` `{ uid }` | professora | apaga o login e os anexos de um aluno |
| `POST /reset-professor` `{ password }` | só com `ADMIN_TOKEN` | troca a senha da professora |
| `POST /upload?task=ID` (corpo = arquivo) | aluno dono da tarefa ou professora | envia um anexo |
| `POST /file-urls` `{ task }` | aluno dono da tarefa ou professora | links temporários (1 h) dos anexos |
| `GET /file?k=&e=&s=` | quem tem o link temporário | abre o arquivo (aceita Range, para vídeo) |
| `POST /delete-file` `{ task, key }` | aluno dono (antes de revisada) ou professora | apaga um anexo |
| `POST /delete-task-files` `{ task }` | professora | apaga todos os anexos da tarefa |

Limites dos anexos: vídeo até 90 MB (o plano gratuito do Workers aceita até 100 MB por envio), foto até 15 MB,
3 por tarefa, e o Worker para de aceitar envios quando o total chega a 9 GB (a faixa gratuita do R2 é 10 GB).
O espaço usado fica no documento `config/storage` do Firestore.

O login de quem chama é o token do Firebase (`Authorization: Bearer <idToken>`); a professora é reconhecida pelo
documento `config/professor`. O código foi testado em Node com Google, Firestore e R2 simulados (25 de 25) e
com tokens reais do projeto; ainda não rodou no Cloudflare com a chave verdadeira.

## 1. Acesso necessário

- A conta do Cloudflare **onde o R2 foi criado**. O Worker precisa ficar na mesma conta do bucket.
- Acesso ao projeto Firebase `caderno-de-pratica`: o Gabriel adiciona você em
  **Configurações do projeto → Usuários e permissões → Adicionar membro** (papel **Proprietário**).
- Node.js 18 ou mais novo e este repositório clonado.

## 2. Bucket do R2

No Cloudflare (conta do R2) → **R2 Object Storage** → confira o nome do bucket dos anexos (ou crie um, por exemplo
`caderno-de-pratica-anexos`, sem acesso público). Coloque o nome exato em `wrangler.toml`, no campo `bucket_name`.

## 3. Chave da conta de serviço do Firebase

1. Console do Firebase → projeto `caderno-de-pratica` → engrenagem → **Configurações do projeto → Contas de serviço**.
2. **Gerar nova chave privada** → baixa um `.json`.
3. **Não** coloque esse arquivo no repositório. Ele dá acesso total ao projeto.

## 4. Publicar o Worker

```bash
cd caderno-de-pratica/worker
npx wrangler login
npx wrangler secret put SA_JSON < caminho/para/chave-baixada.json
npx wrangler secret put ADMIN_TOKEN
npx wrangler secret put FILE_SECRET
npx wrangler deploy
```

- `wrangler login` abre o navegador: entre com a conta do Cloudflare **do R2**.
- `ADMIN_TOKEN` e `FILE_SECRET`: cole duas senhas longas e aleatórias, diferentes (ex.: de um gerenciador de senhas).
  Guarde o `ADMIN_TOKEN` num lugar seguro: é ele que redefine a senha da professora. O `FILE_SECRET` assina os links
  temporários dos anexos.
- O `deploy` mostra a URL, algo como `https://caderno-admin.<sua-conta>.workers.dev`.
- Depois de publicar, **apague o `.json` do computador**. A chave fica guardada só como segredo do Worker.

## 5. Testar

```bash
curl https://caderno-admin.<sua-conta>.workers.dev/health
```

Deve responder `{"ok":true}`.

Redefinir a senha da professora (usuário `rachelprofi`):

```bash
curl -X POST https://caderno-admin.<sua-conta>.workers.dev/reset-professor \
  -H "Authorization: Bearer <ADMIN_TOKEN>" -H "Content-Type: application/json" \
  -d "{\"password\":\"NovaSenha123\"}"
```

Deve responder `{"ok":true}`.

## 6. Ligar no caderno

Mande a URL do Worker para o Gabriel. Ela vai em `caderno-de-pratica/firebase-config.js`, em
`window.CADERNO_WORKER`. A partir daí aparecem no caderno:

- **Anexar vídeo ou foto** na tarefa (aluno) e os anexos para a professora ver;
- **Definir senha nova** na janela **Acesso do aluno**, mesmo para alunos sem senha guardada;
- **Remover acesso** apagando também o login e os anexos.

## Observações

- `ALLOWED_ORIGINS` em `wrangler.toml` lista os sites que podem chamar o Worker pelo navegador. Se o caderno mudar de
  endereço, acrescente o novo e rode `npx wrangler deploy` de novo.
- Os arquivos ficam em `anexos/<uid do aluno>/<id da tarefa>/...` no bucket. O bucket não precisa (e não deve) ser
  público: os arquivos só abrem pelos links temporários do Worker.
- Para trocar a chave no futuro: gere outra no Firebase, rode `npx wrangler secret put SA_JSON` com o arquivo novo e
  apague a chave antiga em **Contas de serviço → Gerenciar permissões da conta de serviço**.
