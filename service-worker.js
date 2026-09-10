// Offline-Cache für ColorGrade.
// Bei jeder Veröffentlichung die Versionsnummer erhöhen, damit Nutzer
// automatisch die neue Version bekommen.
const CACHE = 'colorgrade-v36';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
  );
  self.clients.claim();
});

// Strategie:
//  • Die App-Seite (HTML/Navigation) = NETWORK-FIRST: online immer die neueste
//    Fassung holen und in den Cache legen, offline aus dem Cache fallen lassen.
//    So schlägt ein neues Deployment sofort beim nächsten Öffnen durch – der
//    alte Trick „Cache erst, nie aktualisieren" entfällt.
//  • Alle anderen Dateien (Icons, Manifest) = CACHE-FIRST, mit Netz-Nachladen.
self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const isHTML = req.mode === 'navigate' ||
    (req.headers.get('accept') || '').includes('text/html');

  if (isHTML) {
    event.respondWith(
      fetch(req).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put('./index.html', copy)).catch(() => {});
        return res;
      }).catch(() =>
        caches.match(req).then(hit => hit || caches.match('./index.html')).then(hit => hit || caches.match('./'))
      )
    );
    return;
  }

  event.respondWith(
    caches.match(req).then(hit =>
      hit || fetch(req).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy)).catch(() => {});
        return res;
      }).catch(() => hit)
    )
  );
});
