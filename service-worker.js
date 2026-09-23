// Offline-Cache für ColorGrade (Portfolio + App).
// Bei jeder Veröffentlichung die Versionsnummer erhöhen, damit Geräte
// automatisch die neue Fassung bekommen.
const CACHE = 'colorgrade-v69';
const ASSETS = [
  './',
  './index.html',
  './fotografie.html',
  './video.html',
  './assets/style.css',
  './assets/fonts/archivo-wdth-latin.woff2',
  './manifest.webmanifest',
  './app/index.html',
  './app/manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon.svg',
  './icons/favicon-32.png',
  './assets/img/spieltag-schuss-t.webp',
  './assets/img/spieltag-zweikampf-t.webp',
  './assets/img/torwart-jubel-t.webp',
  './assets/img/trainer-t.webp',
  './assets/img/spielerportraet-t.webp',
  './assets/img/spieltag-schuss.webp',
  './assets/img/spieltag-zweikampf.webp',
  './assets/img/spieltag-konter.webp',
  './assets/img/torwart-jubel.webp',
  './assets/img/trainer.webp',
  './assets/img/spielerportraet.webp',
  './assets/img/mannschaft.webp',
  './assets/img/match-cut-poster.webp',
  './assets/img/beat-poster.webp',
  './assets/img/rheinhessen-trauben.webp'
];

// GitHub Pages liefert mit `Cache-Control: max-age=600` aus. Der Browser darf
// eine Seite also zehn Minuten lang aus seinem eigenen Zwischenspeicher bedienen,
// auch wenn wir hier „erst das Netz fragen" sagen: Wir fragen das Netz, und das
// Netz antwortet aus dem Browser-Cache. Deshalb holen wir Seiten ausdruecklich
// frisch (`cache: 'reload'`), sonst haengt eine neue Fassung bis zu zehn Minuten.
function frisch(req) {
  try {
    return fetch(new Request(req.url, { cache: 'reload', credentials: 'same-origin' }));
  } catch (e) {
    return fetch(req);
  }
}

self.addEventListener('install', event => {
  // Einzeln legen statt addAll: eine fehlende Datei soll nicht die
  // ganze Installation scheitern lassen.
  event.waitUntil(caches.open(CACHE).then(c =>
    Promise.all(ASSETS.map(u =>
      fetch(new Request(u, { cache: 'reload' }))
        .then(res => res.ok ? c.put(u, res) : null)
        .catch(() => {})
    ))
  ));
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    // Reihenfolge ist wichtig: erst die Fenster einsammeln, dann uebernehmen.
    // VOR `claim()` liefert matchAll nur Fenster, die der ALTE Service-Worker
    // bedient hat. Genau die zeigen moeglicherweise noch eine Fassung aus dem
    // Browser-Cache und werden unten einmal neu geladen, diesmal ueber frisch()
    // am Browser-Cache vorbei. Ein erster Besuch ist noch unkontrolliert, steht
    // also nicht in der Liste und wird nicht mitten im Laden gestoert.
    const alteFenster = await self.clients.matchAll({ type: 'window' });
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
    // Bewusst NICHT abwarten: `navigate()` loest eine Navigation aus, und die
    // kann dieser Service-Worker erst bedienen, wenn `activate` durch ist.
    // Wer hier `await` schreibt, baut eine Verklemmung: activate wartet auf die
    // Navigation, die Navigation wartet auf activate.
    for (const f of alteFenster) {
      f.navigate(f.url).catch(() => {});
    }
  })());
});

// Strategie:
//  • Seiten (HTML) = NETWORK-FIRST: online immer die neueste Fassung holen und
//    unter ihrer eigenen Adresse ablegen, offline aus dem Cache fallen lassen.
//    So schlägt ein neues Deployment sofort beim nächsten Öffnen durch.
//  • Alle anderen Dateien (CSS, Bilder, Manifest) = CACHE-FIRST mit Netz-Nachladen.
self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  // Videos laufen am Service-Worker vorbei. Der Browser holt sie in Stuecken
  // (Range-Anfragen, Antwort 206), und eine Antwort aus dem Cache waere die
  // ganze Datei: Safari spielt das Video dann gar nicht ab. Vorgeladen werden
  // sie auch nicht, fuenf MB pro Clip gehoeren nicht in den Offline-Speicher.
  if (/\.(mp4|webm|mov)$/i.test(url.pathname)) return;

  const isHTML = req.mode === 'navigate' ||
    (req.headers.get('accept') || '').includes('text/html');

  if (isHTML) {
    event.respondWith(
      frisch(req).then(res => {
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
