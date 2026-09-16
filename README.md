# allgemein

Code auf dem Tablet.

## 🎨 ColorGrade (PWA)

Ein Lern- und Nachschlagewerkzeug für **Bild- und Videobearbeitung** fürs Tablet, 
installierbar als App (PWA), funktioniert offline, speichert alle Daten lokal auf
dem Gerät. Die App ist als **Lernsystem für Einsteiger** aufgebaut: Sie nimmt einen
kompletten Neuling an die Hand und führt ihn Schritt für Schritt durch Aufnahme,
Bearbeitung, Farbe und den eigenen Stil.

> **Für Claude / neue Chats:** Diese README ist der aktuelle Projektstand **und**
> die Arbeitsanleitung. Lies sie zuerst, dann weißt du, was ColorGrade ist, wie
> wir arbeiten und wo wir stehen. Zwei Regeln sind Pflicht bei jeder Änderung:
> **(1)** `service-worker.js` die Cache-Version um eins hochzählen, **(2)** unten im
> **Änderungsverlauf** eine Zeile ergänzen. So bleibt der Stand über Chats hinweg
> nachvollziehbar.

---

## Offene Aufgaben für den nächsten Chat

> Die drei Punkte aus dem letzten Chat (Über-Text, Video-Gruppen umhängen,
> Lead-Texte) sind mit **v39** erledigt. Offen sind noch:

**1. Video-Bereich D zur „Zusammenfassung“ ausbauen**

Bereich D enthält bisher nur die Video-Rezepte. Geplant ist zusätzlich eine
kompakte Zusammenfassung der Bereiche A bis C auf einen Blick.

**2. Feinschliff**

Einige SVG-Grafiken sauberer machen, dazu Kleinigkeiten, die beim Durchklicken
auffallen.

---

## Aktueller Stand (Cache `v39`, Details im Änderungsverlauf unten)

> Hinweis: Der folgende Abschnitt beschreibt den Grundaufbau. Was seit v25 dazukam
> (Ziel-Ebene im Berater, Farbrad neu, Rezepte-Kopf, Emoji-/KI-Handschrift-Entschlackung,
> Feedback & „Über", Video-Berater mit Grundlagen/Situationen …), steht vollständig im
> **Änderungsverlauf** ab v26.

Ganz oben schaltet ein **Kopf-Umschalter** zwischen zwei Welten: **📷 Bildbearbeitung**
und **🎬 Videobearbeitung**. Die untere Navigation zeigt je Modus die passenden Bereiche;
der zuletzt gewählte Modus wird lokal gemerkt.

**Fertig (Bild):**
- 📖 **Wissen**: Startseite, zwei Ebenen (Lernen + Nachschlagen), **13 Lektionen**.
- 📷 **Berater**: 10 Motive, **vier Ebenen** je Motiv (Ziel · Aufnehmen · Verstehen · Anwenden).
- 🎨 **Farbe** mit zwei Ebenen: **Farblehre** (8 Lektionen) + **Farbrad**.
- 🧪 **Rezepte**: **nur Bild-Looks** (17 Stück), eigene Rezepte speicherbar.
  (Die Video-Rezepte sind in den Video-Bereich D umgezogen.)

**Fertig (Video):**
- 🎬 **Bereich A · Grundlagen**, **12 geführte Lektionen** in drei Phasen: *Das bewegte
  Bild* (fps, 180°-Regel, Belichten, Auflösung/Codec, scharf & farbstabil), *Erzählen mit
  Bildern* (Einstellungsgrößen, Bildaufbau, Kamerabewegung, die Sequenz) und *Ton & Schnitt*.
  Gleiches Lektions-Muster wie im Bild-Wissen, mit modusübergreifendem Sprung zu Foto-Lektionen.
  Dazu ein Umschalter **Lernen / Nachschlagen** wie im Bild-Wissen: Unter *Nachschlagen*
  liegt der Video-Spickzettel (Bildrate wählen, Kamera-Grundeinstellungen), eigene
  Einträge inklusive.

- 🧭 **Bereich B · Berater**, Situations-Gitter mit **10 Dreh-Situationen**, jede nach
  gleichem Template: Steckbrief, *Technik & Bild*, *Einstellungen & Winkel* (mit Grafik),
  *Geschichte erzählen*, *Worauf-achten*-Checkliste und ein **Übungs-Dreh** zum Nachdrehen,
  plus Sprünge in die passenden Grundlagen-Lektionen. Die 10:
  Interview & Podcast · Reise & Orte (B-Roll) · Event & Feier · Produkt & Unboxing ·
  Tutorial & How-to · Vlog & zur Kamera · Reel & Short · Reportage & Doku-Vlog ·
  Day-in-the-Life / GRWM · Sketch & POV.

- 🎨 **Bereich C · Farbe / Color Grading**, **8 geführte Lektionen** (gleiches Muster wie
  A): Korrektur vs. Grading · Reihenfolge · Räder &amp; Kurven · Scopes lesen · Log &amp; LUT ·
  Hauttöne &amp; Teal/Orange · Clips angleichen (Shot Matching) · ein Look über das ganze
  Video. Fokus rein auf Farbe/Grading, mit Sprüngen in die Grundlagen.

- 🧪 **Bereich D · Rezepte**, errichtet und mit den **Video-Rezepten** (Setup, Story-5-Shots,
  B-Roll, Reel) aus dem Bild-Bereich befüllt; eigene Video-Rezepte speicherbar. Damit hat
  Video wie Bild **vier Bereiche A bis D**. *(Geplant: hier zusätzlich eine kompakte
  Zusammenfassung von A bis C.)*

Damit sind **Video A bis D** inhaltlich gefüllt.

**Als Nächstes / offen:**
- 📋 **Bereich D zur „Zusammenfassung" ausbauen**: A bis C kurz & knapp auf einen Blick.
- 🔧 **Feinschliff:** einige SVG-Grafiken sauberer machen und Kleinigkeiten, die auffallen.

---

## Aufbau: die vier Bereiche

Untere Navigation in dieser Reihenfolge (= die Lernreise): **Wissen → Berater → Farbe → Rezepte**.

- 📖 **Wissen**: der Einstieg, zwei Ebenen über einen Umschalter.
  - **Lernen:** geführter Pfad aus **13 Grundlagen-Lektionen** (Drill-in, Fortschritt
    wird lokal abgehakt): Was ist Bildbearbeitung? · Die drei Zonen · Licht steuern ·
    Die Kurve verstehen · Weißabgleich · Farbe & Sättigung · Stimmung machen ·
    Details & Finish · Ebenen & Masken · Auswählen & Freistellen · Retuschieren ·
    Bildaufbau · Die Reihenfolge (fester Ablauf + harte Regeln: RAW, Dosierung,
    Licht, Rand-Check). Jede Lektion: Hook → Grafik → einfache Erklärung → „Merke" →
    „Probier's" → ausklappbare Vertiefung „für Fortgeschrittene".
  - **Nachschlagen:** der durchsuchbare Spickzettel in **17 Bild-Gruppen**.
    Eigene Einträge und Gruppen ergänzbar, Vorlagen ausblendbar. (Die zwei
    Video-Gruppen liegen seit v39 im Video-Bereich A.)

- 📷 **Berater**: Motiv antippen (Wald, Meer, Regennacht, Sonnenuntergang, Porträt,
  Berge, Stadt, Blumen, Food, Schnee), **vier Ebenen** je Motiv:
  - **🎯 Ziel:** der 0. Schritt vor dem ersten Regler: die drei Zielfragen (Wohin
    zuerst das Auge? · Warm oder kühl? · Was lenkt ab?), *eine* klare Empfehlung mit
    kurzer Begründung und die drei Trennungs-Achsen (Helligkeit, Sättigung,
    Farbtemperatur), mit denen sich das Motiv vom Hintergrund löst.
  - **📸 Aufnehmen:** wie du dieses Motiv am besten fotografierst (Licht, Perspektive,
    Bildaufbau, Technik), mit Sprung zur Lektion „Bildaufbau".
  - **🧩 Verstehen:** das Bearbeitungs-Konzept aufgeschlüsselt: Kernidee, eine Grafik
    (wo auf der Tonachse es greift), „So spielt es zusammen" Phase für Phase mit
    Sprüngen in die passenden Wissens-Lektionen, und ein Fazit.
  - **📋 Anwenden:** der fertige Ablauf in vier Phasen (Basis → Kurven → lokal →
    Finish) plus Color Grading auf Spannung oder Harmonie, mit konkreten Kurvengriffen.

- 🎨 **Farbe**: zwei Ebenen wie im Wissen.
  - **Farblehre:** 8 Lektionen zur Farbtheorie (Was ist Farbe? · Der Farbkreis · Die
    drei Eigenschaften · Warm & Kühl · Farbharmonien · Kontrast & Kontext · Was Farben
    ausdrücken · Farbe im Bild einsetzen), mit Sprüngen ins Farbrad und ins Wissen.
    Ausgerichtet auf das **Licht-/RGB-Modell** (Gegenfarbe von Blau = Gelb), passend
    zum Grading; der Malkasten (RYB) nur als Fortgeschrittenen-Randnotiz.
  - **Farbrad:** ein **Farb-Finder** in drei Bereichen. ① Hauptfarbe des Bildes auf dem
    Rad wählen + eine **Harmonie-Regel** (Monochrom · Analog · Komplementär · Split ·
    Triade) → daraus eine **5-Farben-Palette** („welche Farben passen zu meinem Bild").
    ② **Klassische Look-Kombis** (Teal & Orange, 70er, Blaue Stunde, Golden Hour, Wald,
    Beere) setzen Hauptfarbe + Regel. ③ **Die 3 Looks nachbauen** (Cinematic · Märchenhaft ·
    Nordisch) mit Grading-Anleitung als kanal-gruppierte S-Kurven (¼-/¾-Punkt, nicht die
    Ecken). Rad-Zeichnung/Palette: `harmonyPalette` + `renderPalette`.

- 🧪 **Rezepte**: **17 Bild-Looks** mit Kurvenarbeit, Begründung je Schritt und Merksatz;
  eigene Rezepte speicherbar. Oben ein aufklappbarer **Look-Modell-Kopf** („Jeder Look = 3
  Achsen": Farbverhältnis/Kontrast/Sättigung, mit Namen→Werte-Beispielen); jeder Bild-Look
  zeigt beim Aufklappen ein **3-Achsen-Diagramm** mit Formel. Gedacht als „Rezeptbuch", in dem
  man das Gelernte als eigenen Stil speichert. (Die früheren **Video-Rezepte** liegen jetzt im
  Video-Bereich unter **D**.)

**Alles ist löschbar** und wiederherstellbar (Wissen → Vorlagen verwalten). Eigene
Inhalte liegen lokal auf dem Gerät. Die Werkzeugnamen orientieren sich an gängigen
Foto-Apps; das Prinzip dahinter gilt in jedem Bearbeitungsprogramm.

---

## Das Lern-Prinzip

Die App ist eine **Reise vom Nichts zum eigenen Stil**, in vier Schritten:

1. **Wissen**, die Basis: was jedes Werkzeug tut (global Licht & Farbe, dann lokal
   & strukturell), plus Bildaufbau.
2. **Berater**, der Zusammenhang: wie die Werkzeuge pro Motiv zusammenwirken, und
   wie man das Motiv überhaupt aufnimmt.
3. **Farbe**, die Farblehre verstehen und am Farbrad aufs eigene Bild anwenden.
4. **Rezepte**, das Gelernte als eigene Rezepte speichern = der eigene Stil.

**Symmetrie:** Allgemeines Wissen lebt im **Wissen/Farbe** (Lektionen), motiv-spezifische
Anwendung im **Berater** (pro Kachel). Die Bereiche sind über **Lektions-Sprünge**
verzahnt (Berater/Farbe → passende Wissens-Lektion und umgekehrt), sodass man vom
Konzept jederzeit zur Grundlage springen kann.

---

## Arbeitsweise (wichtig für neue Chats)

- **Eine Datei:** Die ganze App steckt in `index.html` (HTML + CSS + JS zusammen).
  PWA, offline-fähig, Zustand in `localStorage`. Keine Build-Tools, kein Framework.
- **Live gehen:** GitHub Pages veröffentlicht von **`main`**. Deshalb wird jede fertige
  Änderung **direkt live** gebracht: auf dem zugewiesenen Feature-Branch committen,
  dann per **Fast-Forward in `main`** mergen und `main` pushen; den Feature-Branch
  nachziehen. (So kann der Nutzer sofort in der App testen.)
- **Schreibweise (Nutzer-Vorgabe):** **keine Gedankenstriche** im Text. Statt eines Strichs
  mitten im Satz ein Komma, einen Doppelpunkt oder einen neuen Satz setzen. Gilt für
  App-Texte, Commit-Nachrichten und diese README. Zahlenbereiche als „18 bis 55 mm“.
  Werbliche KI-Sätze vermeiden: Kapitel-Leads sind schlichte Beschreibungen.
- **Cache-Version:** Nach **jeder** inhaltlichen Änderung an der App die Konstante
  `CACHE` in `service-worker.js` um eins hochzählen (`colorgrade-vNN`), sonst laden
  installierte Geräte die alte Fassung.
- **Änderungsverlauf:** Bei **jeder** Version unten eine Zeile ergänzen (siehe Regel dort).
- **Testen vor dem Push:** Chromium ist vorinstalliert (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`),
  Playwright global unter `/opt/node22/lib/node_modules`. Vor dem Push die App laden,
  auf Konsolen-/Seitenfehler prüfen und die geänderten Stellen durchklicken.
  Fallstrick: In JS-Strings **typografische** Anführungszeichen `„…"` benutzen, keine
  geraden `"` (die beenden den String und brechen das Script).
- **Nach dem Live-Gehen** dem Nutzer sagen: 1 bis 2 Min auf den Pages-Build warten, dann
  die installierte App einmal schließen & neu öffnen (oder im privaten Fenster prüfen),
  damit der neue Service-Worker greift.

---

## Änderungsverlauf

> **Regel:** Jede Änderung zählt die Cache-Version (`service-worker.js`) um eins hoch
> und bekommt hier genau eine Zeile. Neueste oben.

| Version | Was |
|---------|-----|
| **v39** | Drei Punkte aus dem Textfeinschliff: **(1)** Der „Über ColorGrade“-Text ist neu und persönlich (Tobias, Digital Marketing, Forschung/Bachelorarbeit, kostenlos für immer, Bitte um Feedback, Quellenhinweis auf wissenschaftliche Veröffentlichungen wie „Kunst verstehen“ von Maria Carla Prette). **(2)** Die zwei Video-Gruppen sind aus dem Bild-Nachschlagen heraus; Video-Bereich A hat jetzt einen eigenen Umschalter **Lernen / Nachschlagen** mit Video-Spickzettel (`WISSEN`-Gruppen mit `v: true`, `buildGroups(video)`, eigener Eintrag merkt sich die Welt). **(3)** Alle Kapitel-Leads sind schlichte Beschreibungen statt Werbesätze. Dazu app-weit: **alle 705 Gedankenstriche entfernt** (Komma, Doppelpunkt oder neuer Satz; Zahlenbereiche als „bis“). |
| **v38** | Video-Berater bekommt zwei Modi (Umschalter oben): **Grundlagen** (neu, Standard) und **Situationen** (die 10 wie bisher). Der Grundlagen-Berater setzt Punkt B bis E des Video-Leitfadens um: Coverage & Fluss (Beats, 3 Größen, 6 Fluss-Prinzipien als **abhakbare Checkliste**, lokal gespeichert), die 3 Schnittregeln (180°/30°/Match-Cut), Story-Gerüst & Rhythmus (5-Shot), Reihenfolge im Schnitt (Ton vor Farbe). |
| **v37** | Feedback-Button im „Über"-Bereich rechtsbündig statt links. |
| **v36** | **Feedback & „Über die App"**: neue „Über ColorGrade"-Ecke am Ende der Wissen-Startseite (was es ist, warum kostenlos, kein Tracking) mit Button „Feedback geben" (Tally-Formular, öffnet extern). Dazu ein dezenter „Über & Feedback"-Link im Kopf, von jedem Bereich erreichbar. |
| **v35** | Weitere Politur: **Lektions- und Kachel-Icons entfernt** (Nutzer-Feedback). Ohne Icon jetzt: alle Lektionslisten (Wissen, Farblehre, Video-Grundlagen, Video-Farbe) und die Motiv-/Situations-Kacheln (Berater, Video-Berater) inkl. Motiv-Überschrift. Behalten: untere Navigation + Modus-Umschalter. |
| **v34** | Auftritt entschlackt vor dem Launch: dekorative Emojis aus Fließtext, Labels, Überschriften und Buttons entfernt (kontext-genau). **Funktional bleiben:** untere Navigation, Modus-Umschalter, Motiv-Kacheln, Lektions-Icons sowie Häkchen (✓) und Schließen-Kreuze (✕). Außerdem meta-/TODO-Notizen raus („Video-Rezepte jetzt drüben …", „hier kommt später …", „Prototyp …"). |
| **v33** | Rezepte-Kopf „3 Achsen" mit rotem Faden (Nutzer-Feedback): jede Achse sagt jetzt, **was sie steuert** (Grundstimmung/Härte/Lautstärke), und die 3 Looks (Cinematic/Märchenhaft/Nordisch) werden **direkt auf denselben 3 Reglern** gezeigt (`LOOK_MODEL`/`renderLookModel`), Achsen und Look-Namen sind damit verbunden statt zwei getrennte Listen. |
| **v32** | **Farbrad neu gedacht** als Farb-Finder (Nutzer-Feedback), drei Bereiche: ① Hauptfarbe wählen + Harmonie-Regel (Monochrom/Analog/Komplementär/Split/Triade) → abgeleitete **Palette** (Adobe-Logik, ein Basispunkt + Regeln); ② klassische Look-Kombis (Teal&Orange, 70er, Blaue Stunde …) setzen Hauptfarbe + Regel; ③ die 3 Looks mit Grading-Anleitung (kanal-gruppierte S-Kurven). Entfernt: „Bedeutung der Farben", langer Social-Media-Palettentext, generischer „So setzt du um"-Block. |
| **v31** | Kurven-Moves jetzt **nach Kanal gruppiert** (Nutzer-Feedback): pro Kanal beide Punkte zusammen (¼ Schatten + ¾ Lichter = kleine S-Kurve), Reihenfolge Blau → Rot → Grün, statt zwischen den Kanälen zu springen. Gilt im Farbrad (Looks) und im Berater-Grading (`movesByChannel`). |
| **v30** | Grading klarer & weniger überladen (Nutzer-Feedback): Kurven-Sprache app-weit auf **¼-Punkt (Schatten) / ¾-Punkt (Lichter)** statt „linkes/rechtes Ende (Ecke)" umgestellt, die auto-generierten Moves (`moveSentence`/`movesHtml`) **und** die Farbkanal-Tönungs-Schritte in allen Motiven & Rezepten; RGB-Fades/Weißpunkt bleiben bewusst „Ecke/Ende". Neu eine „Wo anfassen?"-Legende am Kurven-Hinweis. Farbrad-„Wohin diese Farben führen" von 6 auf **3 Looks** (Cinematic · Märchenhaft · Nordisch, gleiche Namen wie im Rezepte-Kopf); Farbrad-Umsetzung zeigt nur noch den **Hauptkanal**, Nebenkanäle einklappbar; Berater → Anwenden zeigt **eine** empfohlene Richtung (Spannung), Harmonie einklappbar. |
| **v29** | Service-Worker: App-Seite jetzt **network-first** (online immer die neueste Fassung, offline weiter aus dem Cache) statt cache-first, behebt, dass neue Deployments auf installierten Geräten hängen blieben. Icons/Manifest bleiben cache-first. |
| **v28** | Wissen (Bild-Leitfaden, Etappe 3): neue Lektion 13 „Die Reihenfolge" (fester Ablauf global→Look→lokal→Feinschliff als Grafik, „lokal vor global" + die harten Regeln: RAW statt JPEG, Dosierung, Licht beim Fotografieren, Rand-Check) + die Regel „Gesicht ≠ Rest der Person" (keine Struktur auf Haut, zweite engere Maske) in Lektion 11. |
| **v27** | Look-Modell (Bild-Leitfaden, Etappe 2): Rezepte-Kopf „Jeder Look = 3 Achsen" (Farbverhältnis/Kontrast/Sättigung) mit Namen→Werte-Beispielen (Cinematic/Märchenhaft/Nordisch) + je Bild-Look ein 3-Achsen-Diagramm mit Formel; in der Farblehre (FL5) der Hinweis „warm/kühl ≠ Harmonie/Spannung" (zwei getrennte Achsen). |
| **v26** | Berater bekommt den 0. Schritt: neue erste Ebene „🎯 Ziel" je Motiv, 3 Zielfragen (Wohin das Auge? · Warm/kühl? · Was lenkt ab?) + eine klare Empfehlung + die 3 Trennungs-Achsen (Helligkeit/Sättigung/Farbtemperatur), aus dem Bild-Leitfaden. |
| **v25** | Video-Bereich C „Farbe/Color Grading" (8 Lektionen) + Bereich D „Rezepte"; Video-Rezepte aus dem Bild-Bereich nach D verschoben (Bild-Rezepte jetzt nur Bild). Video hat damit A bis D. |
| **v24** | Video-Berater komplett (10 Situationen): + Reportage & Doku-Vlog, Day-in-the-Life/GRWM, Sketch & POV. |
| **v23** | Video-Berater: Situationen Tutorial & How-to, Vlog & zur Kamera, Reel & Short. |
| **v22** | Video-Berater: Situationen Reise & Orte, Event & Feier, Produkt & Unboxing. |
| **v21** | Video-Bereich B „Berater": Situations-Gitter + erste Situation „Interview & Podcast" (Steckbrief, Technik, Ton, Einstellungen, Story, Checkliste, Übungs-Dreh) mit Sprüngen in die Grundlagen-Lektionen. |
| **v20** | Video als eigene Welt: Bild/Video-Umschalter im Kopf + eigene Bottom-Nav je Modus; **Bereich A „Grundlagen"** mit 12 geführten Lektionen (bewegtes Bild · Erzählen · Ton & Schnitt), inkl. modusübergreifendem Sprung zu Foto-Lektionen. |
| **v19** | Fotografie: Wissen-Lektion 12 „Bildaufbau" (Drittelregel, 9 Felder, Bildtiefe) + Berater-Ansicht „📸 Aufnehmen" je Motiv (Aufnahme-Tipps). |
| **v18** | Wissen: drei Lektionen zum lokalen/strukturellen Bearbeiten, Ebenen & Masken, Auswählen & Freistellen, Retuschieren (→ 11 Lektionen). |
| **v17** | Farbe-Tab: Farblehre (8 Lektionen) + Farbrad-Umschalter; Navigation neu geordnet zu Wissen → Berater → Farbe → Rezepte. |
| **v16** | Berater: Konzept-Aufschlüsselung „Verstehen/Anwenden" für alle 10 Motive. |
| **v15** | Berater: Aufschlüsselung „Verstehen/Anwenden" (Prototyp am Motiv Wald). |
| **v14** | Wissens-Tab zu „Lernen + Nachschlagen" umgebaut; 8 Grundlagen-Lektionen mit Grafiken; Wissen wird Startseite. |
| **v13** | Ausgangsstand vor dem Lern-Umbau: Berater, Rezepte, Farbrad, Wissen als reines Glossar. |

---

## Auf dem Tablet als App installieren

1. **Veröffentlichen** über GitHub Pages: Repo-Einstellungen → *Pages* → Source
   `Deploy from a branch`, Branch `main`, Ordner `/ (root)`. Nach ein bis zwei
   Minuten liegt die App unter `https://<benutzername>.github.io/allgemein/`.
   Hinweis: Bei einem **privaten** Repo braucht GitHub Pages einen Bezahlplan, 
   bei einem kostenlosen Konto das Repo dafür auf öffentlich stellen oder einen
   anderen Static-Host (Netlify, Cloudflare Pages) verwenden.
2. Die Adresse am Tablet im Browser öffnen.
3. **Zum Startbildschirm hinzufügen**, fertig, eigenes App-Icon (Farbrad),
   Vollbild ohne Browserleiste, funktioniert offline.

---

## Dateien

| Datei | Zweck |
|-------|-------|
| `index.html` | die komplette App (HTML, CSS, JS in einer Datei) |
| `manifest.webmanifest` | App-Name, Icon, Standalone-Anzeige |
| `service-worker.js` | Offline-Cache (Cache-Version hier hochzählen) |
| `icons/` | App-Icons (aus `scripts/make_icons.py` erzeugt) |
| `scripts/make_icons.py` | erzeugt die Icons neu (reines Python) |

---

## Technische Notizen (Orientierung im Code)

- **Lektionen (Wissen):** `<article class="lk-lesson" data-lek="N">` in `#lernLesson`;
  Steuerung `renderLkList` / `openLesson` / `closeLesson`; Fortschritt in `localStorage`.
- **Lektionen (Farblehre):** paralleler Aufbau mit `data-fl="N"` in `#flLesson` und
  eigenem Controller (`renderFlList` / `openFl` / …). Gleiche Optik über die `.lk-*`-Klassen.
- **Berater:** `ADVISOR`-Array; je Motiv `{ basis, kurven, lokal, finish, tension,
  harmony, learn, shoot, looks }`. Drei Ansichten rendern `shootView` / `learnView` /
  `adviceApply`; Umschalten via `switchBView`.
- **Cross-Links:** `data-lek-jump="N"` springt über `goLesson()` in eine Wissens-Lektion;
  `data-goto-rad` schaltet zum Farbrad; `data-goto-anwenden` zur Anwenden-Ansicht.
- **CSS-Präfixe:** `.lk-*` = Lektions-Chrome, `.s-*` = SVG-Grafiken, `.bv-*` =
  Berater-Aufschlüsselung, `.fl-*` = Farblehre-Grafiken. Umschalter überall `.seg`/`.segbtn`.
- **Speicher:** gelesene Lektionen, eigenes Wissen, eigene Rezepte und ausgeblendete
  Vorlagen liegen in `localStorage` (Schlüssel mit Präfix `fw_`).

> Werte in den Rezepten und Beratungen sind **Startpunkte**, je nach Bild anpassen.
