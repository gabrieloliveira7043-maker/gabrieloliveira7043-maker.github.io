/* Service worker do Caderno de Prática: só mostra as notificações que o servidor manda e abre a tarefa ao tocar. */
self.addEventListener("install", function () { self.skipWaiting(); });
self.addEventListener("activate", function (e) { e.waitUntil(self.clients.claim()); });

self.addEventListener("push", function (e) {
  var d = {};
  try { d = e.data ? e.data.json() : {}; } catch (err) { d = { body: e.data ? e.data.text() : "" }; }
  e.waitUntil(self.registration.showNotification(d.title || "Caderno de Prática", {
    body: d.body || "",
    icon: "icone-192.png",
    badge: "icone-192.png",
    tag: d.tag || undefined,
    renotify: !!d.tag,
    data: { url: d.url || "./" },
  }));
});

self.addEventListener("notificationclick", function (e) {
  e.notification.close();
  var url = (e.notification.data && e.notification.data.url) || "./";
  var tarefa = null;
  try { tarefa = new URL(url, self.location.href).searchParams.get("tarefa"); } catch (err) {}
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then(function (abertas) {
    var minha = abertas.filter(function (c) { return c.url.indexOf(self.registration.scope) === 0; })[0];
    if (minha) { minha.postMessage({ tarefa: tarefa }); return minha.focus(); }   // caderno já aberto: só mostra a tarefa
    return self.clients.openWindow(url);
  }));
});
