#!/usr/bin/env python3
"""Regenerate the two-glyph author font from the installed MuPDF CJK font.

Normal manuscript compilation uses the supplied .ttf/.enc/.tfm files and
does not require Python, PyMuPDF, fontTools, or ttf2tfm.
"""
from io import BytesIO
from pathlib import Path
import subprocess

import fitz
from fontTools import subset
from fontTools.ttLib import TTFont

base = Path(__file__).resolve().parent
source = fitz.Font("china-s")
font = TTFont(BytesIO(source.buffer))
assert all(cp in font.getBestCmap() for cp in (0x83E0, 0x841D))
options = subset.Options()
options.glyph_names = True
subsetter = subset.Subsetter(options=options)
subsetter.populate(unicodes=[0x83E0, 0x841D])
subsetter.subset(font)
font["post"].formatType = 2.0
font["post"].extraNames = []
font["post"].mapping = {}
for identifier, value in {
    1: "AuthorNameCJK", 2: "Regular", 4: "AuthorNameCJK Regular", 6: "AuthorNameCJK"
}.items():
    font["name"].setName(value, identifier, 3, 1, 0x409)
font.save(base / "author-cjk.ttf")
glyphs = ["uni83E0", "uni841D"] + [".notdef"] * 254
encoding = "/AuthorNameCJKEncoding [\n" + "\n".join(
    " ".join("/" + name for name in glyphs[i:i + 8])
    for i in range(0, 256, 8)
) + "\n] def\n"
(base / "author-cjk.enc").write_text(encoding, encoding="ascii")
subprocess.run(
    ["ttf2tfm", "author-cjk.ttf", "-n", "-T", "author-cjk.enc", "-u", "author-cjk.tfm"],
    cwd=base,
    check=True,
)
print("Created native pdfLaTeX font resources for 菠萝.")
