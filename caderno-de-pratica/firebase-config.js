/* Configuração do projeto Firebase do Caderno de Prática.
   Copie do console do Firebase: Configurações do projeto → Seus apps → app da Web → firebaseConfig.
   Esses valores não são segredo: quem protege os dados são as regras em firestore.rules. */
window.CADERNO_FIREBASE = {
  apiKey: "AIzaSyDDMohG0HyTiy9ktnspSopOk1r4Hbdze9o",
  authDomain: "caderno-de-pratica.firebaseapp.com",
  projectId: "caderno-de-pratica",
  storageBucket: "caderno-de-pratica.firebasestorage.app",
  messagingSenderId: "9589711251",
  appId: "1:9589711251:web:1b8d37e0abc1c7c9958866"
};

/* Endereço do Worker "caderno-admin" no Cloudflare (pasta worker/), ex.: "https://caderno-admin.conta.workers.dev".
   Vazio: o caderno funciona sem anexos e sem trocar senha de aluno pelo servidor. */
window.CADERNO_WORKER = "";
