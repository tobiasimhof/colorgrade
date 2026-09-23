#!/usr/bin/env python3
"""Erzeugt Favicon und App-Icons: die Initialen "TI" weiss auf Schwarz.

Die Buchstaben kommen als Umrisse direkt aus der Seitenschrift Archivo
(assets/fonts/archivo-wdth-latin.woff2), damit das Icon genau so aussieht wie
der Name auf der Startseite. Gezeichnet wird ohne Bildbibliothek: Die Umrisse
werden in Linien zerlegt und zeilenweise gefuellt (Regel "nonzero"), mit
vierfacher Abtastung je Richtung fuer glatte Kanten.

Braucht nur fontTools und brotli (fuer woff2):
    pip install fonttools brotli
    python3 scripts/make_icons.py
"""
import os
import struct
import zlib

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.basePen import BasePen

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(BASE, "assets", "fonts", "archivo-wdth-latin.woff2")

TEXT = "TI"
BG = (19, 19, 21)        # --bg der Seite
FG = (242, 242, 244)     # --text der Seite
WEIGHT = 700             # so fett wie der Name auf der Startseite
WIDTH = 86               # --w-head: dieselbe Breite wie die Ueberschriften
TRACK = -0.02            # Zeichenabstand in em, wie beim Namen leicht enger
SS = 4                   # Abtastung je Richtung (4 x 4 = 16 Proben je Pixel)


class FlatPen(BasePen):
    """Zerlegt Kurven in kurze Geraden und sammelt geschlossene Polygone."""

    def __init__(self, glyphset, dx=0.0):
        super().__init__(glyphset)
        self.polys, self.cur, self.dx = [], [], dx

    def _moveTo(self, p):
        self.cur = [(p[0] + self.dx, p[1])]

    def _lineTo(self, p):
        self.cur.append((p[0] + self.dx, p[1]))

    def _curveToOne(self, p1, p2, p3):
        (x0, y0) = self.cur[-1]
        x0 -= self.dx
        for i in range(1, 17):
            t = i / 16
            mt = 1 - t
            x = mt**3 * x0 + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t**3 * p3[0]
            y = mt**3 * y0 + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t**3 * p3[1]
            self.cur.append((x + self.dx, y))

    def _qCurveToOne(self, p1, p2):
        (x0, y0) = self.cur[-1]
        x0 -= self.dx
        for i in range(1, 17):
            t = i / 16
            mt = 1 - t
            x = mt * mt * x0 + 2 * mt * t * p1[0] + t * t * p2[0]
            y = mt * mt * y0 + 2 * mt * t * p1[1] + t * t * p2[1]
            self.cur.append((x + self.dx, y))

    def _closePath(self):
        if len(self.cur) > 2:
            self.polys.append(self.cur)
        self.cur = []

    _endPath = _closePath


def glyph_polys():
    """Umrisse von TEXT in Schrifteinheiten, plus Begrenzungsrahmen."""
    font = TTFont(FONT)
    font = instantiateVariableFont(font, {"wght": WEIGHT, "wdth": WIDTH})
    upm = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    polys, x = [], 0.0
    for ch in TEXT:
        name = cmap[ord(ch)]
        pen = FlatPen(gs, dx=x)
        gs[name].draw(pen)
        polys += pen.polys
        x += hmtx[name][0] + TRACK * upm
    xs = [p[0] for poly in polys for p in poly]
    ys = [p[1] for poly in polys for p in poly]
    return polys, (min(xs), min(ys), max(xs), max(ys))


def coverage(polys, size, scale, ox, oy):
    """Deckung 0..1 je Pixel. Font-y zeigt nach oben, Bild-y nach unten."""
    edges = []
    for poly in polys:
        for i in range(len(poly)):
            (x0, y0), (x1, y1) = poly[i], poly[(i + 1) % len(poly)]
            X0, Y0 = ox + x0 * scale, oy - y0 * scale
            X1, Y1 = ox + x1 * scale, oy - y1 * scale
            if Y0 != Y1:
                edges.append((X0, Y0, X1, Y1))
    cov = [[0.0] * size for _ in range(size)]
    w = 1.0 / (SS * SS)
    for sy in range(size * SS):
        y = (sy + 0.5) / SS
        hits = []
        for X0, Y0, X1, Y1 in edges:
            if (Y0 <= y < Y1) or (Y1 <= y < Y0):
                x = X0 + (y - Y0) * (X1 - X0) / (Y1 - Y0)
                hits.append((x, 1 if Y1 > Y0 else -1))
        hits.sort()
        wind, row = 0, cov[sy // SS]
        for i, (x, d) in enumerate(hits):
            was = wind
            wind += d
            if was == 0 and wind != 0:
                start = x
            elif was != 0 and wind == 0:
                # Proben zwischen start und x liegen innen
                a = max(0, int(start * SS + 0.5))
                b = min(size * SS, int(x * SS + 0.5))
                for sx in range(a, b):
                    row[sx // SS] += w
    return cov


def png(size, pad_ratio, corner_ratio):
    polys, (x0, y0, x1, y1) = glyph_polys()
    avail = size * (1 - 2 * pad_ratio)
    scale = avail / max(x1 - x0, y1 - y0)
    # Die Buchstaben optisch mittig: Rahmen der Umrisse in die Bildmitte.
    ox = (size - (x1 - x0) * scale) / 2 - x0 * scale
    oy = (size + (y1 - y0) * scale) / 2 + y0 * scale
    cov = coverage(polys, size, scale, ox, oy)
    corner = size * corner_ratio
    px = bytearray()
    for y in range(size):
        px.append(0)
        for x in range(size):
            a = 255
            if corner > 0:
                dxc, dyc = min(x + .5, size - x - .5), min(y + .5, size - y - .5)
                if dxc < corner and dyc < corner:
                    d = ((corner - dxc) ** 2 + (corner - dyc) ** 2) ** .5 - corner
                    a = int(255 * max(0.0, min(1.0, 0.5 - d)))
            c = min(1.0, cov[y][x])
            px.extend(tuple(int(BG[i] + (FG[i] - BG[i]) * c) for i in range(3)) + (a,))

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
            + chunk(b"IDAT", zlib.compress(bytes(px), 9)) + chunk(b"IEND", b""))


def svg():
    """Favicon als Vektor: scharf in jeder Groesse, ein paar hundert Byte."""
    polys, (x0, y0, x1, y1) = glyph_polys()
    size, pad = 64, 0.2
    scale = size * (1 - 2 * pad) / max(x1 - x0, y1 - y0)
    ox = (size - (x1 - x0) * scale) / 2 - x0 * scale
    oy = (size + (y1 - y0) * scale) / 2 + y0 * scale
    d = " ".join("M" + " L".join(f"{ox + x * scale:.1f} {oy - y * scale:.1f}" for x, y in poly) + "Z"
                 for poly in polys)
    bg = "#%02x%02x%02x" % BG
    fg = "#%02x%02x%02x" % FG
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">'
            f'<rect width="{size}" height="{size}" rx="12" fill="{bg}"/>'
            f'<path d="{d}" fill="{fg}"/></svg>\n')


# (Datei, Groesse, Rand, Eckenrundung). Maskable und Apple ohne eigene Ecken:
# Das System schneidet selbst zu, bei maskable nur den inneren Kreis, deshalb
# dort mehr Rand.
TARGETS = [
    ("icons/icon-192.png", 192, 0.22, 0.22),
    ("icons/icon-512.png", 512, 0.22, 0.22),
    ("icons/icon-maskable-512.png", 512, 0.30, 0.0),
    ("icons/apple-touch-icon.png", 180, 0.24, 0.0),
    ("icons/favicon-32.png", 32, 0.16, 0.18),
]

if __name__ == "__main__":
    os.makedirs(os.path.join(BASE, "icons"), exist_ok=True)
    for path, size, pad, corner in TARGETS:
        data = png(size, pad, corner)
        with open(os.path.join(BASE, path), "wb") as f:
            f.write(data)
        print(f"geschrieben: {path} ({size}x{size}, {len(data)} bytes)")
    with open(os.path.join(BASE, "icons", "favicon.svg"), "w") as f:
        f.write(svg())
    print("geschrieben: icons/favicon.svg")
