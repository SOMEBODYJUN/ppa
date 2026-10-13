# Continuous neighborhood retraction schematic

Self-contained mathematical line art for a general research-paper figure, built at **180 × 110 mm**. The source is `draw_figure.py`; it requires only existing NumPy and Matplotlib and does not call a network service or install packages. The repository root is inferred from the script location. All definitions, a standalone bilingual caption, alt text, exact complete-resolvent realization, proof mapping and scope boundaries are in [the caption](../../../发表成果整理/本轮重构/RLEB邻域回缩示意图_图注.md).

```bash
python3 research/code/rleb_neighborhood_retraction/draw_figure.py
python3 research/code/rleb_neighborhood_retraction/draw_figure.py --language cn --font /workspace/scratch/cabc4e00b63a/tmp/NotoSansCJKsc-Regular.otf
```

Run from the repository root. `--output-dir PATH` redirects the figure files. English is the default and needs no extra font. The optional Chinese command requires an already available font; the script never downloads or commits it. Rerunning deliberately replaces only this script's output stems.

Outputs in `发表成果整理/本轮重构/图件/`:

- `rleb-neighborhood-retraction.{pdf,svg,png}`: English vector PDF/SVG and 400 dpi PNG preview.
- `rleb-neighborhood-retraction-cn.{pdf,svg,png}`: optional Chinese counterparts.

Local diagnostic outputs are `validation.json`, `validation-cn.json`, and the corresponding `grayscale-preview*.png`. JSON records versions, arithmetic results, page size, raster-object absence, text bounds, foreground contrast and output hashes. No randomness, sampled observations, statistical uncertainty, smoothing, or inferred data are involved. The drawn sets are explicit mathematical schematics. SVG glyph outlines make the appearance portable; the English PDF uses embedded TrueType/CID fonts. The optional Chinese PDF uses embedded vector Type 3 glyphs because the supplied CJK OTF contains CFF outlines; this avoids misidentifying CFF as TrueType in the PDF. Neither PDF contains raster images. No `bbox_inches='tight'` resize is used.

The general theorem contract requires a **continuous single-valued complete physical map** and **uniform vanishing physical length tails**, in addition to the local RLEB gates. The complete-map transfer is not silently identified with canonical C11's graph-block scope. M is the certified cluster; a general retraction is not identified with a nearest-point projection or a deformation retraction. The annulus has a separately proved radial model. Its strict budget uses the wider work-domain W, not the narrower pictured open U. The right-hand drawings represent three specific infinite limits; finite approximations themselves are not excluded.

For independent export inspection:

```bash
/usr/bin/pdfinfo 发表成果整理/本轮重构/图件/rleb-neighborhood-retraction.pdf
pdffonts 发表成果整理/本轮重构/图件/rleb-neighborhood-retraction.pdf
pdfimages -list 发表成果整理/本轮重构/图件/rleb-neighborhood-retraction.pdf
```

The downloaded, unmodified **scientific-visualization** skill materially guided exact-size vector export, semantic rather than decorative encoding, caption/alt text, palette redundancy, contrast and grayscale checks, and post-export inspection. Its pinned source and installation audit are in [Astra论文制图技能与任务说明.md](../../../发表成果整理/本轮重构/Astra论文制图技能与任务说明.md). No helper from the skill is executed or required by this script. No particular journal's compliance is asserted.

Software-method attribution: Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*. arXiv:2609.00065. <https://doi.org/10.48550/arXiv.2609.00065>. Parent independently verified the current arXiv metadata (v2, 2026-09-02). The mathematical definitions and conclusions come from the repository sources linked in the caption, not from the plotting skill.

Independent parent review also checked 48 exact rational cases (six rational unit directions and eight radii), plus the center fiber, using `Fraction` arithmetic. These checks covered the complete inverse equation, reflected anchor, true residual, and the exact budget endpoints 7/20 < 9/20 with residual window 7/40. The universal inverse identity is proved analytically in the caption; the finite arithmetic cases do not prove completeness by sampling.
