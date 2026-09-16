#!/usr/bin/env python3
"""Erzeugt die App-Icons (Farbrad auf dunklem Grund) ohne externe Bibliotheken.

Reines Python (nur zlib/struct aus der Standardbibliothek), damit es in jeder
Umgebung laeuft. Rendert ein HSV-Farbrad, passend zum Thema Farb-Grading.
"""
import math
import struct
import zlib

BG = (28, 28, 30)       # dunkles Anthrazit als Hintergrund
HUB = (28, 28, 30)      # Nabe in der Mitte (gleich wie BG)
RING = (245, 245, 247)  # heller Ring um das Rad


def hsv_to_rgb(h, s, v):
    i = int(h * 6.0)
    f = h * 6.0 - i
    p = v * (1.0 - s)
    q = v * (1.0 - f * s)
    t = v * (1.0 - (1.0 - f) * s)
    i %= 6
    if i == 0: r, g, b = v, t, p
    elif i == 1: r, g, b = q, v, p
    elif i == 2: r, g, b = p, v, t
    elif i == 3: r, g, b = p, q, v
    elif i == 4: r, g, b = t, p, v
    else: r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)


def make_png(size, maskable=False, corner_ratio=0.22):
    cx = cy = (size - 1) / 2.0
    wheel_r = size * (0.34 if maskable else 0.40)   # etwas mehr Rand bei maskable
    hub_r = wheel_r * 0.30
    ring_w = max(1.0, size * 0.012)
    corner = 0 if maskable else size * corner_ratio
    px = bytearray()
    for y in range(size):
        px.append(0)  # Filter-Byte pro Zeile
        for x in range(size):
            # abgerundete Ecken (nur wenn nicht maskable): aussen transparent
            a = 255
            if corner > 0:
                # Abstand zur naechsten Ecke pruefen
                dxc = min(x, size - 1 - x)
                dyc = min(y, size - 1 - y)
                if dxc < corner and dyc < corner:
                    ddx = corner - dxc
                    ddy = corner - dyc
                    if math.hypot(ddx, ddy) > corner:
                        px.extend((0, 0, 0, 0))
                        continue
            dx = x - cx
            dy = y - cy
            dist = math.hypot(dx, dy)
            if dist <= hub_r:
                r, g, b = HUB
            elif dist <= wheel_r:
                if dist >= wheel_r - ring_w or dist <= hub_r + ring_w:
                    r, g, b = RING
                else:
                    ang = (math.atan2(dy, dx) / (2 * math.pi)) % 1.0
                    sat = (dist - hub_r) / (wheel_r - hub_r)
                    r, g, b = hsv_to_rgb(ang, min(1.0, 0.35 + sat * 0.65), 1.0)
            else:
                r, g, b = BG
            px.extend((r, g, b, a))

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)  # 8-bit RGBA
    idat = zlib.compress(bytes(px), 9)
    return sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", idat) + chunk(b"IEND", b"")


TARGETS = [
    ("icons/icon-192.png", 192, False),
    ("icons/icon-512.png", 512, False),
    ("icons/icon-maskable-512.png", 512, True),
    ("icons/apple-touch-icon.png", 180, True),
]

if __name__ == "__main__":
    import os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(base, "icons"), exist_ok=True)
    for path, size, mask in TARGETS:
        data = make_png(size, maskable=mask)
        with open(os.path.join(base, path), "wb") as f:
            f.write(data)
        print(f"geschrieben: {path} ({size}x{size}, {len(data)} bytes)")
