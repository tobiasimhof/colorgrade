# ColorGrade

Portfolio von **Tobias Imhof**: Sportfotografie, Videografie und eigene Apps. Die
Seite ist der Link im Lebenslauf für die Bewerbung um eine **Ausbildung zum
Mediengestalter Bild und Ton**, ein Wechsel aus dem jetzigen Beruf heraus. Die
Startseite zeigt seit v56 nur noch den Namen, einen Satz aus Fakten und die drei
Kacheln: Fotografie, Videografie und Apps. Die Kachel **Apps** führt ohne
Zwischenseite direkt in die ColorGrade App unter `app/`.

**Über mich und Kontakt stehen bewusst nicht mehr auf der Seite.** Wer den Link
anklickt, hat den Lebenslauf offen, dort stehen Werdegang und E-Mail bereits. Ein
zweites Mal wirkt es wie Füllmaterial, und die Startseite soll in zwei Sekunden
sagen, was es zu sehen gibt.

**Jede Seite hat denselben Kopf**, die App eingeschlossen: links die Marke
ColorGrade, die zur Startseite führt, rechts die Navigation Fotografie ·
Videografie · Apps. Wer eine Seite ergänzt, baut diesen Kopf mit ein.

**Was über den Nutzer bekannt ist** (für Texte auf der Seite): Schwerpunkt
Sportfotografie, ehrenamtlich für das Sportportal **FuPa**, liefert dort an
Spieltagen Bilder. Videografie ist neu und wird gerade erarbeitet. Nachname
**Imhof**, seit v56 steht er auf der Startseite. Noch offen und nicht erfinden:
jetziger Beruf und die Ausrüstung über „Nikon D3400, Telezoom" hinaus. Eine
E-Mail-Adresse braucht die Seite nicht mehr.

Unter `app/` liegt zusätzlich **ColorGrade**, das Lerntagebuch zu Bild, Video und
Farbe als installierbare Web-App (PWA, offline, alle Daten lokal auf dem Gerät).
Es ist kein Produkt für andere, sondern das Nachschlagewerk, das beim Einarbeiten
in Fotografie und Videografie entstanden ist.

> **Für Claude / neue Chats:** Diese README ist der aktuelle Projektstand **und**
> die Arbeitsanleitung. Lies sie zuerst. Vier Regeln sind Pflicht:
> **(1)** `service-worker.js` die Cache-Version um eins hochzählen, **(2)** unten im
> **Änderungsverlauf** eine Zeile ergänzen, **(3)** keine Gedankenstriche im Text,
> **(4)** **keine privaten Daten auf die Seite**: Vor- und Nachname genügen, keine
> Anschrift, keine Telefonnummer, keine E-Mail. Das Repo ist öffentlich, alles darin ist lesbar.

## Offene Aufgaben für den nächsten Chat

> Stand nach **v57**: Die Startseite ist auf Name, einen Satz und die drei Kacheln
> eingedampft, das Portfolio läuft in einer eigenen, schmal gestellten Schrift
> (Archivo, als Datei im Repo). Fotografie-Galerie steht mit sechs Bildern und Lightbox, die
> Videografie-Texte stehen, die App ist entschlackt.
>
> **Offen ist ein einziges Paket, und es kommt am Stück:** das Mannschaftsfoto
> (entsteht unter Flutlicht) und die zwei Video-Dateien (in Canva geschnitten, beide
> unter 30 Sekunden, einer davon 22). Der Nutzer lädt beides zusammen hoch, weil er
> die Videos bis dahin noch feinschleift. Nicht einzeln nachfragen, das ist so
> verabredet.
>
> **Reihenfolge ist seit v56 umgedreht: Optik vor Inhalt.** Die fehlenden Inhalte
> hängen an einem Drehtermin, die Optik nicht. Was am Erscheinungsbild noch offen
> ist, steht unter „Erscheinungsbild".

**Leitlinie des Nutzers für alle Texte:** Ein Personaler klickt sich durch, er liest
nicht. Also kurz halten, keine Absätze, die nach Werbung oder nach KI klingen. Im
Zweifel weglassen statt ausformulieren.

**Und keine Motivation auf der Seite.** Das Warum steht im Anschreiben, doppelt
klingt es nach „ich will das unbedingt". Auf der Seite stehen Fakten: was gemacht
wurde, womit, für wen. Die einzige Ausnahme ist der eine Satz am Kontakt, dass eine
Ausbildung zum Mediengestalter Bild und Ton gesucht wird.

**Schritt 2 · Fotografie** (Galerie steht seit v52, sechs Bilder seit v55)
Sechs Bilder liegen in `assets/img/`. Ganz oben steht seit v53 das **Querformat als
Aufmacher** ohne Überschrift, darunter drei Abschnitte: **Der Moment** (Schuss,
Zweikampf), **Die Menschen** (Torwart, Trainer) und **Das Porträt** (Spielerporträt
allein, `.shots.solo`). Lightbox mit Pfeiltasten und Escape ist gebaut. Offen ist nur
noch das **Mannschaftsfoto**, es gehört in den Abschnitt „Das Porträt" und macht
daraus eine saubere Zweierreihe.

Regeln, die der Nutzer selbst erarbeitet hat und die für Nachschub gelten:
Hochformate **durchgehend 4:5**, Querformate **16:9**, Schwarzpunkt unter 12,
Weißpunkt über 245, **kein Farbkanal über 2 Prozent am Anschlag** (das sieht man im
Helligkeits-Histogramm nicht, kostet aber unwiederbringlich Zeichnung) und bei
Menschen im Bild **Hautton R minus G zwischen 35 und 40**. Bearbeitet wird in Snapseed, ein Look wird über
Kopieren/Einfügen auf alle Bilder übertragen, damit die Galerie eine Handschrift
hat. Der Firmenlauf ist nach Absprache raus.

Neue Bilder kommen über `scripts/make_photos.py` herein: Quelldatei in die
`BILDER`-Tabelle eintragen, Skript mit dem Quellordner aufrufen, fertig. Es legt je
Bild eine 1600er Fassung für die Lightbox und eine 800er Kachel an. Breite Bilder
(`breit = True`) bekommen nur die 1600er, weil sie die volle Satzbreite von 860 px
füllen und eine 800er Kachel dort hochskaliert würde.

**Das Mannschaftsfoto** entsteht bei **Flutlicht**, weil der Verein keinen anderen
Termin gefunden hat. Das ist die schwierigste Aufnahmesituation des Projekts, deshalb
steht der Brief hier fest:

- **RAW aufnehmen.** Alle bisherigen Dateien sind Kamera-JPEGs. Unter Flutlicht ist
  der Weißabgleich nicht vorhersagbar (Halogenmetalldampf zieht grün, LED je nach
  Hersteller anders). Aus RAW ist der Farbstich verlustfrei zu korrigieren, aus JPEG
  nicht. Snapseed kann RAW entwickeln.
- **Zeit 1/100 oder 1/50 Sekunde.** Netzfrequenz 50 Hertz, Flutlicht pulsiert also
  mit 100 Hertz. Bei 1/125, 1/160 oder 1/200 schwankt die Helligkeit von Bild zu Bild
  und es entstehen Farbstreifen. Eine stehende Mannschaft braucht keine kurze Zeit.
- **Stativ**, **Blende f/5,6** (Schärfentiefe für zwei Reihen), **ISO so niedrig wie
  möglich** (D3400 gut bis 1600, brauchbar bis 3200; sonst lieber auf 1/50 runter).
- **Lichtrichtung beachten:** Flutlicht steht hoch und wirft harte Schatten in die
  Augenhöhlen. Nicht direkt unter den hellsten Mast stellen. Masten und Lampen aus
  dem Bild halten, die brennen aus.
- **15 bis 20 Auslösungen**, einer blinzelt immer.

Danach wie alle anderen: Beschnitt **4:5**, Schwarzpunkt unter 12, Weißpunkt über 245,
kein Kanal über 2 Prozent am Anschlag, Hautton R minus G zwischen 35 und 40. Es gehört
in den Abschnitt „Das Porträt" und macht daraus eine Zweierreihe.

**Schritt 3 · Videografie** (Texte stehen seit v48)
Die zwei Übungen sind beschrieben: „Atmosphäre auf den Beat" (Schnitt auf den Takt,
Zeitlupe) und „Match Cut im Wohnzimmer" (Anschlüsse, allein gedreht). Offen sind nur
noch die Dateien: nach `assets/video/`, längere über einen Hoster. Grenze bei
GitHub: 100 MB je Datei. Länge und Dateigröße sind beim Nutzer erfragt.

**Schritt 4 · Apps** (erledigt in v47)
Die Kachel führt direkt in die App, eine eigene Apps-Seite gibt es nicht mehr. Das
Warenwirtschaftssystem für einen Winzer ist auf Wunsch des Nutzers wieder raus, der
Bereich gehört allein ColorGrade.

**Schritt 5 · Feinschliff**
Über mich und Kontakt sind seit v56 von der Startseite verschwunden, E-Mail und
Werdegang stehen im Lebenslauf. Offen: Vorschaubild für geteilte Links (Open Graph),
eigenes Favicon, 404-Seite.

**Erscheinungsbild** (analysiert in v55, Punkt 1 erledigt in v56)
Der Nutzer findet, dass Schrift, Aufmachung und Bedienelemente „nach KI" aussehen. Die
Analyse hat sechs konkrete Ursachen ergeben, damit der nächste Chat sie nicht neu
herleiten muss:

1. **Der System-Font-Stack**, **erledigt in v56.** Er war der größte Verräter, weil
   jede generierte Seite genau den benutzt. Das Portfolio läuft jetzt auf **Archivo**,
   seit v57 in schmaler Breite.
   **Achtung, die App unter `app/` hat ihn noch:** Dort hängen 165 SVG-Texte an den
   Schriftmaßen, ein Tausch braucht einen eigenen Durchgang mit Screenshots, sonst
   rutscht Text aus den handgezeichneten Kästen.
2. **Der Regenbogen-Punkt** als Marke (`.dot`, conic-gradient). Generisch und für
   Sportfotografie ohne Bedeutung.
3. **16 px runde Ecken an allem**, auch an den Fotos. Runde Bildecken lesen sich als
   App-Oberfläche, nicht als Fotografie.
4. **Jeder Block ist eine umrandete Karte** (1 px Rahmen, runde Ecken, hellerer
   Hintergrund). Standard-Optik von Dashboard-Templates.
5. **Graue Versalien-Überschriften** (`.sec-h`). Gleiche Herkunft.
6. **Strich-Icons** auf den Startseiten-Kacheln (Lucide-Look).

**Gemeinsamer Nenner:** Die Oberfläche macht zu viel Lärm um die Fotos herum. Ein
Fotoportfolio wird professionell, wenn die Bedienelemente fast verschwinden und die
Bilder die einzige Farbe im Layout sind.

**Messung:** Die kräftigen Farben in den sechs Bildern sind Blau (220 Grad, 26 %,
das Vereinstrikot), Grün (80 Grad, 7 %, der Rasen) und Rot (10 Grad, 4 %). Der
Akzent der Seite ist Orange `#ff9f45` und kommt in keinem Bild vor. **Trotzdem nicht
gegen Blau tauschen**, sondern den Akzent überhaupt zurücknehmen.

**Die Schrift ist seit v56 gesetzt: Archivo** (Omnibus-Type, SIL Open Font License),
eine Groteske aus der Zeitungsecke, hohe x-Höhe, schmale Formen, keine Verzierungen.
Seit v57 liegt die Fassung mit **zwei Achsen** im Repo, Gewicht 400 bis 700 und Breite
62 bis 125 Prozent, zusammen 90 KB unter `assets/fonts/`, vorgeladen in jeder Seite.
Kein Google Fonts: Die Regel „keine externen Schriften" zielt auf den Datenschutz, eine
Datei auf derselben Domain verletzt sie nicht.

**Die Breite ist die Stellschraube für „edel":** Sie hängt an zwei Variablen oben in
`assets/style.css`, `--w-head` (Überschriften und Bedienelemente, steht auf 86 %) und
`--w-text` (Fließtext, 96 %). Eine Zahl ändern und die ganze Seite wird schmaler oder
breiter, ohne dass ein Layout nachgezogen werden muss. Unter etwa 80 % kippt es vom
Edlen ins Plakathafte, das war die Abwägung. **Pflicht:** Die Spanne
`font-stretch: 62% 125%` muss im `@font-face`-Block stehen, sonst greift `font-stretch`
an den Elementen nicht.

**Material, das der Nutzer beisteuern könnte:** seine Unterschrift auf weißem Papier
abfotografiert. Im Fuß der Seite wäre sie der stärkste Beleg dafür, dass hier ein
Mensch gebaut hat.

**Laufend:** SVG-Feinschliff in der App (siehe „SVG-Grafiken prüfen").
## Die App unter `app/` (ColorGrade Lerntagebuch)

> Hinweis: Der folgende Abschnitt beschreibt den Grundaufbau. Was seit v25 dazukam
> (Ziel-Ebene im Berater, Farbrad neu, Rezepte-Kopf, Emoji-/KI-Handschrift-Entschlackung,
> Video-Berater mit Grundlagen/Situationen …), steht vollständig im
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
  Video wie Bild **vier Bereiche A bis D** und dient zugleich als kompakte Zusammenfassung.

Damit sind **Video A bis D** inhaltlich gefüllt.

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

- **Zwei Teile:** Das **Portfolio** sind mehrere kleine Seiten im Wurzelverzeichnis
  mit einem gemeinsamen `assets/style.css`. Die **App** steckt komplett in
  `app/index.html` (HTML + CSS + JS in einer Datei). Keine Build-Tools, kein Framework.
- **Live gehen:** GitHub Pages veröffentlicht von **`main`**. Jede fertige Änderung
  auf dem zugewiesenen Feature-Branch committen, dann per **Fast-Forward in `main`**
  mergen und `main` pushen; den Feature-Branch nachziehen.
- **Schreibweise (Nutzer-Vorgabe):** **keine Gedankenstriche** im Text. Statt eines
  Strichs mitten im Satz ein Komma, einen Doppelpunkt oder einen neuen Satz setzen.
  Gilt für Seitentexte, App-Texte, Commit-Nachrichten und diese README. Zahlenbereiche
  als „18 bis 55 mm". Werbliche KI-Sätze vermeiden.
- **Privatsphäre:** Keine Anschrift, keine Telefonnummer, keine Tracker, keine externen
  Schriften. Alle Seiten tragen `<meta name="robots" content="noindex" />`. Das ist eine
  bewusste Entscheidung, damit die Seite nur über den Link im Lebenslauf erreicht wird.
- **Zwischenspeicher, zwei Ebenen:** GitHub Pages liefert mit `Cache-Control: max-age=600`
  aus. Der Browser darf eine Seite also zehn Minuten lang aus seinem eigenen Speicher
  bedienen, auch wenn der Service-Worker „erst das Netz fragen" sagt. Deshalb holt der
  Service-Worker Seiten seit v48 ausdrücklich frisch (`cache: 'reload'`). Seit v49
  lädt eine neue Fassung offene Fenster zusätzlich einmal selbst neu. Merke: Ein
  manuelles Neuladen umgeht den Browser-Cache ohnehin, ein normaler Klick auf einen
  Link nicht. Deshalb blieb die App hängen, während die Startseite frisch war.
  Wer sofort nach dem Push nachsieht, prüft am besten in einem privaten Fenster.
- **Cache-Version:** Nach **jeder** inhaltlichen Änderung die Konstante `CACHE` in
  `service-worker.js` um eins hochzählen (`colorgrade-vNN`), sonst laden installierte
  Geräte die alte Fassung. Neue Dateien zusätzlich in die `ASSETS`-Liste eintragen.
- **Änderungsverlauf:** Bei **jeder** Version unten eine Zeile ergänzen.
- **Testen vor dem Push:** Chromium ist vorinstalliert, Playwright global unter
  `/opt/node22/lib/node_modules`. Lokal `python3 -m http.server 8099` starten, dann jede
  Seite in 1280 und in 390 Pixel Breite laden und prüfen auf: HTTP 200, keine
  Konsolenfehler, kein horizontales Scrollen
  (`document.documentElement.scrollWidth > window.innerWidth`). Der Überlauf-Test ist
  nicht optional, genau daran ist die Galerie beim ersten Anlauf gescheitert.
  Fallstrick in der App: In JS-Strings **typografische** Anführungszeichen „…" benutzen,
  keine geraden, die beenden den String und brechen das Script.
- **SVG-Grafiken prüfen:** Die ~65 Grafiken in der App sind handgezeichnete SVGs
  (Koordinaten im Code), da rutscht schnell Text aus einer Box oder ein Pfeil endet
  neben dem Ziel. Zum Sichten alle `<figure>` mit SVG in eine Audit-Seite mit der
  App-CSS extrahieren und einzeln screenshotten, statt im Code zu raten. Merke:
  `text-anchor` plus x-Koordinate bestimmen, ob Text in der Box bleibt. Bei Platznot
  lieber die `viewBox`-Höhe erhöhen als Text überlappen lassen.
- **Nach dem Live-Gehen** dem Nutzer sagen: 1 bis 2 Min auf den Pages-Build warten, dann
  die installierte App einmal schließen & neu öffnen (oder im privaten Fenster prüfen),
  damit der neue Service-Worker greift.
## Änderungsverlauf

> **Regel:** Jede Änderung zählt die Cache-Version (`service-worker.js`) um eins hoch
> und bekommt hier genau eine Zeile. Neueste oben.

| Version | Was |
|---------|-----|
| **v57** | **Die Schrift läuft schmaler**, auf Wunsch des Nutzers: schmal wirkt ruhiger und teurer. Dafür liegt jetzt die Archivo-Fassung mit **zwei Achsen** im Repo (Gewicht 400 bis 700 **und** Breite 62 bis 125 Prozent, 90 KB statt 35 KB). Gesteuert wird es über zwei neue Variablen, `--w-head` für Überschriften und Bedienelemente (86 Prozent) und `--w-text` für den Fließtext (96 Prozent). Der Name rendert damit 12 Prozent schmaler. **Zwei Fallstricke, beide geprüft:** **(1)** `font-stretch` an den Elementen bleibt wirkungslos, wenn im `@font-face`-Block die Spanne `font-stretch: 62% 125%` fehlt, der Browser weiß sonst nichts von der Achse. **(2)** Die Datei heißt bewusst neu (`archivo-wdth-latin.woff2` statt `archivo-var-latin.woff2`). Unter dem alten Namen hätte der Browser-Cache bis zu zehn Minuten die alte Datei ohne Breiten-Achse geliefert, und die Seite hätte unverändert ausgesehen, ohne dass ein Fehler sichtbar wird. **Abwägung:** Unter etwa 80 Prozent kippt das Schriftbild vom Edlen ins Plakathafte, deshalb 86. |
| **v56** | **Eigene Schrift und eine leere Startseite.** Zwei Dinge, die zusammen gehören, weil beide dasselbe Ziel haben: Die Seite soll nicht nach Vorlage aussehen. **(1)** Der System-Font-Stack ist raus, das Portfolio läuft auf **Archivo** (Groteske aus der Zeitungsecke, SIL Open Font License). Eine variable Datei für alle Gewichte von 400 bis 700, 35 KB, als Latin-Subset unter `assets/fonts/`, kein Google Fonts. Jede Seite lädt sie per `rel="preload"` vor, sonst findet der Browser sie erst nach dem CSS und der erste Eindruck steht kurz in der Ersatzschrift. Überschriften stehen enger (`-.03em` beim Namen, `-.025em` bei den Seitentiteln), weil Archivo mehr Zug verträgt als der System-Stack. **Merke:** Das Gewicht 650, das an mehreren Stellen steht, gibt es jetzt wirklich; vorher hat der Browser es auf 700 gerundet oder künstlich fett gerechnet. **(2)** Die Startseite zeigt nur noch **Tobias Imhof**, einen Satz aus Fakten und die drei Kacheln. Über mich, Kontakt und der Notizkasten sind raus: Wer den Link anklickt, kommt aus dem Lebenslauf und hat Werdegang und E-Mail schon gelesen. Der Name ist entsprechend größer (38 px, ab 720 px 54 px), der Inhalt sitzt mittig. Die toten Regeln `.hero .kicker`, `.hero-more` und `.ft-in .sp` sind mit raus, ebenso die Kontakt-Links im Fuß der Unterseiten, die ins Leere gezeigt hätten. **Die App unter `app/` behält vorerst den alten Stack**, dort hängen 165 SVG-Texte an den Schriftmaßen. |
| **v55** | **Spielerporträt eingebunden**, die Galerie hat damit sechs Bilder. Es bekommt einen **eigenen Abschnitt „Das Porträt"** statt als drittes Bild zu den Menschen zu wandern: Ein Porträt ist geplante Arbeit und keine Reportage, und drei Bilder hätten in der zweispaltigen Reihe eine Lücke gelassen. `.shots.solo` deckelt die Breite auf 420 px, damit es so groß wirkt wie eine Kachel der anderen Reihen. **Lehrstück aus der Bearbeitung:** Der globale Sättigungsregler trifft Motiv und Hintergrund gleich stark. Ein Minus von 25, das dem lauten Grün galt, nahm der Haut ihre Farbe (R minus G fiel von 39 auf 31, die Haut wirkte milchig). Die Lösung war ein milderes globales Minus plus ein **Kontrollpunkt auf dem Gesicht** in „Selektiv". Ergebnis: Haut wieder bei R minus G = 38, dazu Schwarzpunkt 7, Weißpunkt 251, Kontrast 59,9 und kein Kanal über 1,6 Prozent. Die Gesamtsättigung liegt bei 129 statt der Zielspanne 85 bis 95, das ist hier bewusst: Der Wert kommt fast nur vom großen grünen Hintergrund, und weiter zu senken hätte erneut die Haut gekostet. **Merke: Bei Porträts schlägt ein gesunder Hautton jede Zielzahl für die Gesamtsättigung.** |
| **v54** | **Trainerbild getauscht** gegen die vom Nutzer neu bearbeitete Fassung. Entscheidend war ein Kanal-Clipping, das man im Histogramm der Helligkeit nicht sieht: Der Blaukanal stand in bis zu 5,32 Prozent der Pixel auf 255, dadurch hatte die Regenjacke in den hellen Partien keine Stoffzeichnung mehr, und der Rotkanal lag in 5,28 Prozent auf null, wodurch die Schatten ins Blaue kippten. Beide Werte liegen jetzt bei 0,01 und 0,07 Prozent. Dazu Weißpunkt von 222 auf 242 und Schwarzpunkt von 16 auf 13. **Merke für künftige Bilder:** Ein kräftig blaues Trikot oder sattes Grün ist oft schon ab Werk nah am Anschlag (hier 2,46 Prozent direkt aus der Kamera). Bei solchen Motiven gehört der Sättigungsregler nach unten, nicht nach oben, sonst ist die Zeichnung unwiederbringlich weg. |
| **v53** | Das Querformat („Lauf in den freien Raum") steht jetzt als **Aufmacher ganz oben**, direkt unter dem Einleitungssatz und bewusst ohne Überschrift (Nutzer-Wunsch: es zieht den Blick am besten). Darunter folgen zwei ruhige Zweierreihen im Hochformat. Das Aufmacherbild lädt nicht mehr verzögert, sondern mit `fetchpriority="high"`, weil es über der Falz liegt. Die Reihenfolge in der Lightbox folgt der neuen Anordnung. |
| **v52** | **Fotografie-Galerie gebaut**, der Bereich ist damit inhaltlich gefüllt. Fünf Bilder in zwei Abschnitten: „Der Moment" (Schuss, Zweikampf, Konter) und „Die Menschen" (Torwart, Trainer). Je Bild eine kurze Unterschrift mit Brennweite und Belichtungszeit aus den EXIF-Daten. Neue **Lightbox** (`.lb`) mit Blättern per Pfeiltasten, Schließen per Escape oder Klick auf den Hintergrund, Fokus bleibt im Overlay und kehrt beim Schließen auf die angeklickte Kachel zurück. Bilder als WebP in zwei Größen, 1600 px für die Lightbox und 800 px für die Kachel, erzeugt von `scripts/make_photos.py`; das Raster lädt so nur 280 KB. Zwei Dinge beim Testen gefunden und behoben: **(1)** Die Kachel des Querformats wurde von 800 auf 860 px hochskaliert, breite Bilder nehmen jetzt die 1600er Fassung. **(2)** Der Lightbox-Hintergrund war mit 94 Prozent halbtransparent, dadurch schienen Kopfzeile und Bildunterschriften durch und hellten die Tiefen des Fotos auf; jetzt deckend. Dazu sitzt die Unterschrift nicht mehr am unteren Bildschirmrand, sondern direkt unter dem Foto (`max-height` statt `flex: 1`). |
| **v51** | Texte auf der Startseite gekürzt (Nutzer-Wunsch): Die Kopfzeile ist ein Satz aus Fakten statt einer Absichtserklärung („Sportfotografie für das Portal FuPa, erste eigene Videoarbeiten, eine selbst gebaute App"). Über mich von vier Karten auf drei, je höchstens zwei kurze Sätze; die Karte „Mein Ziel" ist aufgelöst, ihr Kern steht jetzt als **ein** Satz beim Kontakt. Hintergrund: Das Warum steht im Anschreiben, auf der Seite klang es doppelt und zu sehr nach Wollen. Das Quellenverzeichnis aus v43 bleibt entfernt, das ist entschieden. |
| **v50** | App entschlackt (Nutzer-Wunsch): Der Block **„Über ColorGrade"** am Ende der Wissen-Startseite ist komplett raus, er war zu lang und klang zu sehr nach KI. **Achtung:** Das ausklappbare Quellen- und Literaturverzeichnis lag in diesem Block und ist damit ebenfalls weg (v43, sieben Publikationen). Wer es zurückholen will, findet es in der Historie. Dafür sagt die Kopfzeile jetzt sofort, worum es geht: „Mein Lerntagebuch zur Bildbearbeitung" steht in Akzentgelb und halbfett statt klein und grau. Das tote `.about`- und `.about-src`-CSS ist mit raus. |
| **v49** | Navigation vereinheitlicht (Nutzer-Wunsch): **Jede** Seite hat jetzt denselben Kopf, die App eingeschlossen, mit Marke links (führt zur Startseite) und Fotografie · Videografie · Apps rechts. Die eigene Über-mich-Seite ist aufgelöst, ihr Inhalt und der Kontakt stehen auf der Startseite. Dabei zwei echte Fehler gefunden und behoben. **(1)** Die App stylte `nav` als Element, also erbte der neue Kopf-`nav` die feste Positionierung der unteren Leiste und lag auf dem Untertitel; Regeln auf `body > nav` eingegrenzt. **(2)** Der Selbstheiler im Service-Worker (offene Fenster nach einer neuen Fassung neu laden) verklemmte sich: `activate` wartete per `await` auf `client.navigate()`, und ein Service-Worker liefert keine `fetch`-Ereignisse aus, solange `activate` läuft. Jetzt wird nicht mehr abgewartet, und die Fenster werden **vor** `claim()` eingesammelt, damit ein erster Besuch nicht mitten im Laden neu geladen wird. Mit einem Testaufbau geprüft, der GitHub Pages samt `max-age=600` nachstellt. |
| **v48** | Zwei Dinge. **(1)** Videografie-Seite mit den zwei echten Übungen gefüllt: „Atmosphäre auf den Beat" (Schnitt auf den Takt, leichte Zeitlupe) und „Match Cut im Wohnzimmer" (Anschlüsse, allein gedreht), je mit „Worum es ging" und „Was ich geübt habe". Kein Showreel, zwei Clips sind dafür zu wenig. **(2)** Fehler behoben, den der Nutzer gemeldet hat: Nach dem Live-Gehen stand in der App weiter der alte Text mit Umfrage. Ursache war nicht der Service-Worker-Cache, sondern der **Browser-Cache**: Pages liefert mit `max-age=600`, also bediente der Browser das `fetch` des Service-Workers bis zu zehn Minuten lang selbst. Seiten werden jetzt mit `cache: 'reload'` geholt, im Betrieb und beim Vorladen. |
| **v47** | Apps-Bereich auf ColorGrade zugespitzt (Nutzer-Wunsch): Die Kachel führt jetzt **direkt** in die App unter `app/`, die Zwischenseite `apps.html` ist gelöscht, das Winzer-Warenwirtschaftssystem wieder raus. In der App selbst alles entfernt, was für eine Bewerbung nichts beiträgt: Tally-Umfrage, Forschungsabsatz zur Bachelorarbeit und der Plattform-Text. Der Über-Text beschreibt die App jetzt als Lerntagebuch, die Untertitel im Kopf ebenso, und der frühere Feedback-Link oben rechts ist der Rückweg ins Portfolio. Quellenverzeichnis bleibt. Toter Code raus: `openAbout` und die `.about-fb`-Regeln. |
| **v46** | Startseite nach Nutzer-Wunsch umgebaut: oben ein kurzes Über mich, darunter **drei** Kacheln (Fotografie, Videografie, PWA und Apps) statt vier. Die dritte Kachel nimmt am Handy die volle Breite und stellt Symbol und Text nebeneinander, damit keine Lücke entsteht. Die Über-mich-Seite ist mit echten Angaben gefüllt: Schwerpunkt Sportfotografie, ehrenamtlich für FuPa, Einstieg in die Videografie, Ziel Ausbildung Mediengestalter Bild und Ton. Offen bleiben E-Mail, jetziger Beruf und Ausrüstung, die sind bewusst als Platzhalter markiert. |
| **v45** | **Umbau zum Portfolio.** Die Startseite ist jetzt ein Portfolio mit vier Kacheln (Fotografie, Videografie, PWA und Apps, Über mich), dazu je eine Unterseite und ein gemeinsames `assets/style.css`. Die bisherige Lern-App ist unverändert nach `app/` gezogen und hat ein eigenes Manifest, die Pfade für Icon und Service-Worker sind nachgezogen. Der Service-Worker bleibt im Wurzelverzeichnis, cacht jetzt Portfolio und App und legt jede Seite unter ihrer eigenen Adresse ab statt alles unter `index.html`. Alle Seiten stehen auf `noindex`, Inhalte sind noch Platzhalter. Gefunden und behoben beim Testen: `aspect-ratio` in einem Grid ohne `align-items: start` streckte die Galerie-Kacheln und sprengte die Seitenbreite. |
| **v44** | Den erklärenden Schlusssatz unter dem Quellen-Verzeichnis entfernt (Nutzer-Feedback); die Liste steht jetzt für sich. Ungenutzte `.src-note`-CSS-Regel mit raus. |
| **v43** | Ausklappbares **„Quellen & Literatur“** im Über-Bereich (`.about-src`, `<details>` unter dem „Alle Fakten…“-Satz). Sieben echte, verifizierte Publikationen in drei Gruppen: Kunst & Wahrnehmung (Prette, *Kunst verstehen*), Fotografie & Bild (Itten *Kunst der Farbe*, Freeman *The Photographer’s Eye*, Peterson *Understanding Exposure*), Videografie & Film (Brown *Cinematography*, Murch *In the Blink of an Eye*, Van Hurkman *Color Correction Handbook*). Alle Angaben per Websuche geprüft, keine erfundenen Quellen. |
| **v42** | Kopf-Link „Über & Feedback“ heißt jetzt nur noch **„Feedback“** (klarer, dass es zum Feedback führt; der Über-Text ist Zusatz). Der Klick scrollt jetzt mittig auf den **Feedback-Button** (`.about-fb`) statt an den Anfang des langen Über-Textes. |
| **v41** | SVG-Feinschliff, zweiter Durchlauf (Nutzer-Feedback). **(1)** Kamerabewegung (Video A9): der Schwenk-Bogen lief von oben nach unten und der Pfeil zeigte zurück; jetzt ein Bogen, der klar von links nach rechts sweept, mit Pfeil in Schwenk-Richtung. **(2)** J/L-Cut (Video A11, Ton & Schnitt): die Beschriftung „Ton läuft über den Bildschnitt (L-Cut)“ klebte auf der Ton-Spur (`viewBox` zu niedrig); `viewBox`-Höhe erhöht und Text mit Abstand darunter gesetzt. |
| **v40** | SVG-Feinschliff, erster Durchlauf: alle ~65 Grafiken einzeln gerendert und gesichtet, fünf mit fehlplatziertem Text korrigiert. **(1)** Farbkreis (Farblehre L2): „Blau“/„Grün“ liefen am Rand aus der `viewBox`, jetzt zentriert und in Bounds. **(2)** Kurven-Diagramm (Wissen L4): „heller ↑ Lichter“ lag auf der Kurve/Diagonale, jetzt frei über dem Plot. **(3)** Auswahl (Wissen L10): Beschriftung überlappte die Figur, jetzt oben. **(4)** Seitenverhältnis (Video A5): „hoch · Reel“ stand neben dem 9:16-Kasten (plus ein leeres `<text>`-Element), jetzt mittig im Kasten. **(5)** Vlog „in die Linse“ (Video B): „nicht aufs Bild schauen“ überlappte die Figur, `viewBox` erhöht und Text darunter gesetzt. Bereich D als Zusammenfassung abgehakt. |
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

Das betrifft die App unter `app/`, nicht das Portfolio.

1. **Veröffentlichen** über GitHub Pages: Repo-Einstellungen → *Pages* → Source
   `Deploy from a branch`, Branch `main`, Ordner `/ (root)`. Nach ein bis zwei
   Minuten liegt das Portfolio unter `https://<benutzername>.github.io/colorgrade/`
   und die App unter `.../colorgrade/app/`.
   Hinweis: Bei einem **privaten** Repo braucht GitHub Pages einen Bezahlplan.
2. Die Adresse `.../colorgrade/app/` am Tablet im Browser öffnen.
3. **Zum Startbildschirm hinzufügen**, fertig: eigenes Icon, Vollbild, offline nutzbar.

> Wer die App schon vor v45 installiert hatte, muss sie einmal neu hinzufügen: Die
> alte Verknüpfung zeigt auf die Wurzel und öffnet jetzt das Portfolio. Der
> gespeicherte Fortschritt bleibt erhalten, er liegt unter derselben Domain.
## Dateien

| Datei | Zweck |
|-------|-------|
| `index.html` | Portfolio-Startseite: Name, ein Satz, drei Kacheln |
| `fotografie.html` · `video.html` | die Unterseiten (Apps hat keine, die Kachel führt in die App) |
| `assets/style.css` | gemeinsames Design aller Portfolio-Seiten |
| `assets/img/` · `assets/video/` | Bilder und Clips fürs Portfolio |
| `assets/fonts/` | Archivo als variable WebFont-Datei (Gewicht und Breite) plus OFL-Lizenz |
| `app/index.html` | die komplette Lern-App (HTML, CSS, JS in einer Datei) |
| `app/manifest.webmanifest` | Installation der App (eigener Scope `app/`) |
| `manifest.webmanifest` | Manifest des Portfolios |
| `service-worker.js` | Offline-Cache für Portfolio **und** App (Version hier hochzählen) |
| `icons/` | Icons (aus `scripts/make_icons.py` erzeugt) |
| `scripts/make_icons.py` | erzeugt die Icons neu (reines Python) |
| `scripts/make_photos.py` | macht aus den Originalfotos die WebP-Dateien der Galerie |
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
