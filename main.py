#!/usr/bin/env python3
"""Copy entry.png to /output/entry.png (Python standard library only)."""
import hashlib
import os
import shutil


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = "/output/entry.png"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
if os.path.getsize(SRC) != os.path.getsize(OUT) or _sha256(SRC) != _sha256(OUT):
    raise SystemExit("copy verification failed")
print(f"copied entry.png ({os.path.getsize(OUT)} bytes, sha256 {_sha256(OUT)[:16]}...)")
