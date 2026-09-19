// Offline-Cache für ColorGrade (Portfolio + App).
// Bei jeder Veröffentlichung die Versionsnummer erhöhen, damit Geräte
// automatisch die neue Fassung bekommen.
const CACHE = 'colorgrade-v46';
const ASSETS = [
  './',
  './index.html',
  './fotografie.html',
  './video.html',
  './apps.html',
  './ueber.html',
  './assets/style.css',
  './manifest.webmanifest',
  './app/index.html',
  './app/manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png'
];

self.addEventListener('install', event => {
  // Einzeln legen statt addAll: eine fehlende Datei soll nicht die
  // ganze Installation scheitern lassen.
  event.waitUntil(caches.open(CACHE).then(c =>
    Promise.all(ASSETS.map(u => c.add(u).catch(() => {})))
  ));
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
//  • Seiten (HTML) = NETWORK-FIRST: online immer die neueste Fassung holen und
//    unter ihrer eigenen Adresse ablegen, offline aus dem Cache fallen lassen.
//    So schlägt ein neues Deployment sofort beim nächsten Öffnen durch.
//  • Alle anderen Dateien (CSS, Bilder, Manifest) = CACHE-FIRST mit Netz-Nachladen.
self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  if (new URL(req.url).origin !== self.location.origin) return;

  const isHTML = req.mode === 'navigate' ||
    (req.headers.get('accept') || '').includes('text/html');

  if (isHTML) {
    event.respondWith(
      fetch(req).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy)).catch(() => {});
        return res;
      }).catch(() =>
        caches.match(req).then(hit => hit || caches.match('./index.html'))
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
