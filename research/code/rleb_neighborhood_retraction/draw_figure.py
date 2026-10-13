#!/usr/bin/env python3
"""Exact vector schematic; no network, TeX, or nonstandard plotting helpers.
Run: python3 research/code/rleb_neighborhood_retraction/draw_figure.py
Optional: --language cn --font /path/to/NotoSansCJKsc-Regular.otf
Finite arithmetic/geometry checks diagnose this illustration, not the theorem.
"""
import argparse
import hashlib
import json
import platform
import re
from pathlib import Path
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import to_rgb
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Wedge
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SIZE = (180.0, 110.0)  # mm, preserved without bbox_inches='tight'
COLORS = dict(ink="#18354A", teal="#007E80", orange="#B85C00",
              muted="#52616B", fill="#E7F0F2", rule="#BDC9CD")
RADIUS, TUBE = 1.0, 0.35
# (angle in degrees, input radius); each arrow ends at radius 1.
ARROWS = [(25, 1.27), (65, .73), (105, 1.27), (155, .73),
          (205, 1.27), (245, .73), (290, 1.27), (335, .73)]
LABELS = {
    "en": ["(a) Continuous limit retraction", "(b) Admissible shapes",
           "(c) Excluded accumulation", "Illustrative annular model",
           "fixed zero", "Singleton", "Finite cross", "branching",
           "Filled square", "corners + interior", "Separate models:",
           "no convexity or smoothness required", "Perfect Cantor", "dust",
           "isolated points", "Shrinking essential", "circles",
           "Finite levels are drawn;", "only the infinite limits are excluded.",
           "Local RLEB + continuous single-valued full proximal map "
           + r"$T$" + " + uniform vanishing physical length tails."],
    "cn": ["(a) 连续极限回缩", "(b) 允许的局部形状", "(c) 排除的无限积聚",
           "示例：环形邻域", "固定零点", "单点", "有限十字", "允许分叉",
           "实心方形", "角点与内部", "不同模型的示例：", "无需凸性或光滑性",
           "完美 Cantor", "尘集", "孤立点积聚", "不断缩小的", "本质环圈",
           "仅画有限层级；", "被排除的是相应的无限极限。",
           "完整前提：局部 RLEB + 连续单值完整物理近端 "
           + r"$T$" + " + 一致趋零的物理长度尾界。"],
}


def projection(x, check_domain=True):
    """P on the OPEN illustrated tube; x=0 is not a zero-distance input."""
    x = np.asarray(x, dtype=float)
    r = np.linalg.norm(x, axis=-1, keepdims=True)
    if np.any(r == 0) or (check_domain and np.any(abs(r - 1) >= TUBE)):
        raise ValueError("Input is outside the open illustrated annulus U")
    return x / r


def step(x, check_domain=True):
    return (np.asarray(x) + projection(x, check_domain)) / 2


def luminance(color):
    c = np.asarray(to_rgb(color))
    c = np.where(c <= .04045, c / 12.92, ((c + .055) / 1.055) ** 2.4)
    return float(c @ np.array([.2126, .7152, .0722]))


def validate_math():
    """Independent exact formulas plus sampled edge/geometry regressions."""
    theta = np.linspace(0, 2 * np.pi, 129)[:-1]
    unit = np.column_stack((np.cos(theta), np.sin(theta)))
    # Include both certified CLOSED-window boundaries and zero distance.
    radii = np.array([.65, .650001, .73, 1., 1.27, 1.349999, 1.35])
    x = (radii[:, None, None] * unit).reshape(-1, 2)
    p = projection(x, False)
    y = step(x, False)
    d = abs(np.linalg.norm(x, axis=1) - 1)
    residual = abs(np.linalg.norm(y, axis=1) - 1)
    assert np.max(abs(residual - d / 2)) < 1e-14
    assert np.max(abs((2 * y - p) - x)) < 1e-14  # complete-fiber inversion
    assert np.max(abs(step(unit) - unit)) < 1e-14
    assert np.max(abs(projection(unit) - unit)) < 1e-14
    assert np.all(d < .8 - d)  # strict budget uses W, not the narrower U
    tail_errors = []
    for k in (0, 1, 2, 8, 24):
        z = x.copy()
        for _ in range(k):
            z = step(z, False)
        exact = p + 2. ** (-k) * (x - p)
        tail_errors.append(float(np.max(abs(z - exact))))
        assert np.max(np.linalg.norm(z - p, axis=1)) <= .35 * 2. ** (-k) + 1e-14
    exclusions = [[0, 0], [.65, 0], [1.35, 0], [.649999, 0], [1.350001, 0]]
    for q in exclusions:
        try:
            projection(q)
        except ValueError:
            continue
        raise AssertionError(f"Open-domain exclusion failed: {q}")
    for r in (.650001, 1, 1.349999):
        projection([r, 0])
    for angle, radius in ARROWS:
        u = np.array([np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))])
        segment = np.linspace(radius, 1, 101)[:, None] * u
        assert np.all(abs(np.linalg.norm(segment, axis=1) - 1) < TUBE)
        assert np.allclose(projection(segment[-1]), segment[-1])
    # At coordinate input zero the COMPLETE resolvent is radius-1/2 circle.
    z = .5 * unit
    assert np.max(abs(z + (z - unit))) == 0
    return {"status": "passed", "sampled_inputs": len(x),
            "max_iterate_formula_error": max(tail_errors),
            "open_domain_exclusions": exclusions,
            "closed_certificate_window": [.65, 1.35],
            "working_domain_W": [.2, 1.8], "tail_bound": "0.35 * 2**(-k)",
            "scope": "finite diagnostics; universal formulas proved in caption"}


def draw(language, font, grayscale=False):
    labels = LABELS[language]
    colors = COLORS.copy()
    if grayscale:
        colors = {k: str(luminance(v) ** (1 / 2.2)) for k, v in colors.items()}
    if font:
        font_manager.fontManager.addfont(font)
        family = font_manager.FontProperties(fname=font).get_name()
    else:
        family = "DejaVu Sans"
    style = {"font.family": family, "font.size": 8, "mathtext.fontset": "dejavusans",
             "pdf.fonttype": 42, "svg.fonttype": "path", "svg.hashsalt": "rleb-retraction",
             "figure.facecolor": "white", "savefig.facecolor": "white"}
    with plt.rc_context(style):
        fig = plt.figure(figsize=np.array(SIZE) / 25.4, dpi=200)
        ax = fig.add_axes([0, 0, 1, 1], xlim=(0, SIZE[0]), ylim=(0, SIZE[1]))
        ax.set_aspect("equal")
        ax.axis("off")
        def text(x, y, s, size=8, color="ink", ha="left", **kwargs):
            return ax.text(x, y, s, fontsize=size, color=colors[color],
                           ha=ha, va="center", **kwargs)
        for x, label in zip((4, 74, 125), labels[:3]):
            text(x, 104, label, 8.7, weight="bold")
        for x in (70, 121):
            ax.plot([x, x], [16, 100], color=colors["rule"], lw=.55)
        text(35, 98, labels[3], 7.6, "muted", "center")
        center, scale = np.array([35., 68.]), 20.
        ax.add_patch(Wedge(center, scale * 1.35, 0, 360, width=scale * .7,
                           facecolor=colors["fill"], edgecolor="none"))
        for r in (.65, 1.35):
            ax.add_patch(Circle(center, scale * r, fill=False, lw=.8,
                                edgecolor=colors["muted"], linestyle=(0, (2, 2))))
        ax.add_patch(Circle(center, scale, fill=False, edgecolor=colors["teal"], lw=1.9))
        for angle, radius in ARROWS:
            u = np.array([np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))])
            a, b = center + scale * radius * u, center + scale * u
            ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=7,
                                        lw=1.05, color=colors["orange"], shrinkA=0, shrinkB=0))
        fixed = center + scale * np.array([-1., 1.]) / np.sqrt(2)
        ax.plot(*fixed, marker="s", ms=3.7, color=colors["ink"])
        ax.plot([14, fixed[0] - 1], [88, fixed[1] + 1], color=colors["ink"], lw=.6)
        text(10, 90, labels[4], 7.6)
        text(37, 91.5, r"$U$", 9)
        text(57, 68, r"$M$", 9, "teal")
        text(35, 35, r"$P(x)=\lim_{k\to\infty}T^k x$", 10, ha="center")
        text(35, 27, r"$P:U\to M\ \mathrm{continuous},\quad P|_M=\mathrm{id}_M$",
             8.1, ha="center")
        text(35, 20, r"$T=(I+\Pi_M)/2,\qquad P=\Pi_M$", 8.2, ha="center")
        # Three separate examples: no union of the shapes is asserted.
        ax.plot(83, 82, "o", ms=4.5, color=colors["teal"])
        text(94, 82, labels[5])
        ax.plot([77, 89], [62, 62], color=colors["teal"], lw=2.4, solid_capstyle="round")
        ax.plot([83, 83], [56, 68], color=colors["teal"], lw=2.4, solid_capstyle="round")
        text(94, 64, labels[6]); text(94, 59, labels[7], 7.2, "muted")
        ax.add_patch(Rectangle((77, 35), 12, 12, facecolor=colors["fill"],
                               edgecolor=colors["teal"], lw=1.5))
        text(94, 43, labels[8]); text(94, 38, labels[9], 7.2, "muted")
        text(95.5, 24, labels[10], 7.4, "muted", "center")
        text(95.5, 19, labels[11], 7.2, "muted", "center")
        # C x C, shown at level 3 by interval-center squares (not a finite exclusion).
        starts = np.array([0.])
        for _ in range(3):
            starts = np.r_[starts / 3, (starts + 2) / 3]
        points = starts + .5 / 27
        gx, gy = np.meshgrid(points, points)
        ax.scatter(128 + 15 * gx.ravel(), 75 + 15 * gy.ravel(), marker="s", s=3.1,
                   color=colors["orange"], linewidths=0)
        text(148, 85, labels[12], 7.7); text(148, 80, labels[13], 7.7)
        ns = np.arange(1, 15)
        ax.scatter(129 + 14 / ns, np.full(len(ns), 62), s=7,
                   color=colors["orange"], linewidths=0)
        ax.plot(129, 62, "s", ms=2.6, color=colors["orange"])
        text(148, 65, r"$\{0\}\cup\{1/n:n\geq1\}$", 7.2)
        text(148, 60, labels[14], 7.5)
        for n in range(1, 10):
            r = 7 / n
            ax.add_patch(Circle((129 + r, 41), r, fill=False,
                                edgecolor=colors["orange"], lw=.75))
        text(148, 44, labels[15], 7.5); text(148, 39, labels[16], 7.5)
        text(150.5, 24, labels[17], 7.2, "muted", "center")
        text(150.5, 19, labels[18], 7.2, "muted", "center")
        ax.plot([4, 176], [12, 12], color=colors["rule"], lw=.6)
        text(90, 6, labels[19], 7.4, ha="center")
        fig.canvas.draw()
        renderer, box = fig.canvas.get_renderer(), fig.bbox
        outside = [t.get_text() for t in ax.texts if not box.contains(*t.get_window_extent(renderer).p0)
                   or not box.contains(*t.get_window_extent(renderer).p1)]
        assert not outside, f"Clipped text: {outside}"
        return fig, {"text_count": len(ax.texts), "text_outside_page": outside,
                     "font_sizes_pt": sorted({t.get_fontsize() for t in ax.texts})}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("en", "cn"), default="en")
    parser.add_argument("--font", help="Existing local font file; never downloaded")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "发表成果整理/本轮重构/图件")
    args = parser.parse_args()
    if args.language == "cn" and not args.font:
        parser.error("Chinese rendering requires --font with an existing CJK font")
    if args.font and not Path(args.font).is_file():
        parser.error("--font must name an existing local font")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = {"math": validate_math(), "size_mm": SIZE,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "matplotlib": matplotlib.__version__}}
    suffix = "" if args.language == "en" else "-cn"
    stem = args.output_dir / ("rleb-neighborhood-retraction" + suffix)
    fig, report["layout"] = draw(args.language, args.font)
    pdf_fonttype = 42 if args.language == "en" else 3  # CJK OTF has CFF outlines.
    with plt.rc_context({"pdf.fonttype": pdf_fonttype, "svg.fonttype": "path", "svg.hashsalt": "rleb-retraction"}):
        for ext in ("pdf", "svg", "png"):
            metadata = {"CreationDate": None, "ModDate": None} if ext == "pdf" else {"Date": None}
            temporary = stem.with_suffix(".tmp." + ext)
            fig.savefig(temporary, dpi=400, transparent=False,
                        metadata=metadata if ext != "png" else None)
            if ext == "svg":
                temporary.write_text("\n".join(line.rstrip() for line in temporary.read_text().splitlines()) + "\n")
            temporary.replace(stem.with_suffix("." + ext))
    plt.close(fig)
    pdf = stem.with_suffix(".pdf").read_bytes()
    svg = ET.parse(stem.with_suffix(".svg")).getroot()
    page = [float(v) for v in re.search(rb"/MediaBox\s*\[([^]]+)\]", pdf)[1].split()]
    assert np.allclose(np.array(page[2:]) * 25.4 / 72, SIZE, atol=1e-7)
    svg_mm = [float(svg.attrib[k].removesuffix("pt")) * 25.4 / 72 for k in ("width", "height")]
    assert np.allclose(svg_mm, SIZE, atol=1e-5)
    assert b"/Subtype /Image" not in pdf
    if pdf_fonttype == 42:
        assert b"/Subtype /Type3" not in pdf and b"/FontFile2" in pdf
    assert not list(svg.iter("{http://www.w3.org/2000/svg}image"))
    report["vector"] = {"pdf_page_mm": list(np.array(page[2:]) * 25.4 / 72),
                         "svg_page_mm": svg_mm, "pdf_image_objects": 0, "svg_image_elements": 0,
                         "svg_fonts": "portable glyph paths", "pdf_fonttype": pdf_fonttype}
    report["contrast_on_white"] = {k: (1.05 / (luminance(v) + .05)) for k, v in COLORS.items()}
    for k in ("ink", "teal", "orange", "muted"):
        assert report["contrast_on_white"][k] >= 4.5
    gray, _ = draw(args.language, args.font, grayscale=True)
    gray.savefig(HERE / ("grayscale-preview" + suffix + ".png"), dpi=200)
    plt.close(gray)
    report["sha256"] = {ext: hashlib.sha256(stem.with_suffix("." + ext).read_bytes()).hexdigest()
                        for ext in ("pdf", "svg", "png")}
    (HERE / ("validation" + suffix + ".json")).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "passed", "output": str(stem), "checks": report["vector"]}, indent=2))


if __name__ == "__main__":
    main()
