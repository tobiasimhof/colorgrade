#!/usr/bin/env python3
"""Bereitet Portfolio-Fotos fuer die Galerie auf.

Aus jedem Quellbild entstehen zwei WebP-Dateien:
  NAME.webp    1600 px lange Kante, fuer die Lightbox
  NAME-t.webp   800 px lange Kante, fuer die Kachel im Raster

Aufruf:  python3 scripts/make_photos.py QUELLORDNER
Die Zuordnung Quelldatei zu Zielname steht in BILDER.
"""
import sys, os
from PIL import Image, ImageOps

# Quelldateiname (im Quellordner)  ->  (Zielname ohne Endung, breit?, Qualitaet)
# breit = das Bild nimmt in der Galerie die volle Satzbreite ein (860 px).
# Eine 800er Kachel wuerde dort hochskaliert, deshalb bekommen breite Bilder
# nur die grosse Fassung und benutzen sie auch als Kachel.
# Qualitaet = None nimmt den Normalwert 82 fuer die 1600er Fassung. Ein
# eigener Wert ist nur noetig, wenn ein Bild stark rauscht: Korn laesst sich
# schlecht komprimieren und blaeht die Datei auf.
BILDER = {
    '29314e94-image.jpg': ('torwart-jubel', False, None),
    '13079f7a-image.jpg': ('trainer', False, None),
    'f43e3bc3-image.jpg': ('spielerportraet', False, None),
    'b4b04be7-image.jpg': ('spieltag-schuss', False, None),
    'f168ccee-image.jpg': ('spieltag-zweikampf', False, None),
    '912d98e8-image.jpg': ('spieltag-konter', True, None),
    # Flutlicht mit ISO 6400: mit Qualitaet 82 waere die Datei 448 KB gross,
    # mit 74 sind es 325 KB. Der Unterschied liegt im Gesichtsband bei im
    # Mittel 3,9 Helligkeitsstufen, faellt also aufs Korn und nicht auf die
    # Gesichter.
    'b6bba7ce-image.jpg': ('mannschaft', True, 74),
}

ZIEL = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')


def auf_kante(im, kante):
    w, h = im.size
    f = kante / max(w, h)
    if f >= 1:
        return im.copy()
    return im.resize((round(w * f), round(h * f)), Image.LANCZOS)


def main():
    quelle = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(ZIEL, exist_ok=True)
    for datei, (name, breit, qual) in BILDER.items():
        pfad = os.path.join(quelle, datei)
        if not os.path.exists(pfad):
            print('fehlt: %s' % pfad)
            continue
        # exif_transpose dreht das Bild gemaess Orientation-Tag und
        # entfernt den Tag, damit WebP nicht doppelt dreht.
        im = ImageOps.exif_transpose(Image.open(pfad)).convert('RGB')
        groessen = [(1600, '.webp', qual or 82)]
        if not breit:
            groessen.append((800, '-t.webp', 78))
        for kante, endung, q in groessen:
            out = os.path.join(ZIEL, name + endung)
            auf_kante(im, kante).save(out, 'WEBP', quality=q, method=6)
            k = os.path.getsize(out) // 1024
            print('%-28s %4d KB' % (name + endung, k))


if __name__ == '__main__':
    main()
