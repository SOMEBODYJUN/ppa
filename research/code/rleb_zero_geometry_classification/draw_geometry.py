"""Draw forward geometric consequences; arrows are schematic limit directions."""
import os
from pathlib import Path
from urllib.request import urlretrieve
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, Rectangle
import numpy as np

out = Path(os.environ.get("RLEB_FIGURE_DIR", "rleb_geometry"))
out.mkdir(parents=True, exist_ok=True)
font = Path(os.environ.get("RLEB_CJK_FONT", str(out / "NotoSansCJKsc-Regular.otf")))
if not font.exists():
    font.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve("https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Regular.otf", font)
font_manager.fontManager.addfont(str(font))
plt.rcParams.update({"font.family": font_manager.FontProperties(fname=str(font)).get_name(), "font.size": 12, "axes.unicode_minus": False})
ink, teal, pale, orange = "#213B48", "#087F80", "#DCEFEB", "#B75031"
fig, axs = plt.subplots(2, 2, figsize=(12, 8.6), facecolor="#FCFCF9")
for ax in axs.flat:
    ax.set(xlim=(-1.65, 1.65), ylim=(-1.55, 1.5), aspect="equal")
    ax.axis("off")
def label(ax, x, y, text, color=ink, size=12):
    return ax.text(x, y, text, ha="center", va="center", color=color, fontsize=size)
def ring(ax, center=(0, 0), radius=0.9, tube=False):
    if tube:
        ax.add_patch(Circle(center, radius + .26, fc=pale, ec="none"))
        ax.add_patch(Circle(center, radius - .26, fc="#FCFCF9", ec="none"))
    ax.add_patch(Circle(center, radius, fill=False, ec=teal, lw=3))

a, b, c, d = axs.flat
a.set_title("A  局部 RLEB + 连续单值完整近端", color=ink, fontsize=15, pad=14)
ring(a, tube=True)
assert Q(26, 100) < Q(6, 10) - Q(26, 100)  # strict budget in a wider open tube
for r in (Q(64, 100), Q(67, 100), Q(9, 10), Q(113, 100), Q(116, 100)):
    y = (r + Q(9, 10))/2
    assert abs(y - Q(9, 10)) == abs(r - Q(9, 10))/2
    assert 2*y - Q(9, 10) == r
assert all(.9-.26 < r < .9+.26 for r in (.67, 1.13))
for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
    u = np.array([np.cos(angle), np.sin(angle)])
    for start in (.67, 1.13):
        a.annotate("", xy=.9*u, xytext=start*u, arrowprops={"arrowstyle": "->", "color": teal, "lw": 1.2})
label(a, 0, 0, "零簇 M\n可以有环洞", teal)
label(a, 0, -1.4, "邻近点能连续收拢到零簇；零点自身不移动")

b.set_title("B  局部集合特点：邻域回缩、局部可缩", color=ink, fontsize=15, pad=14)
b.add_patch(Circle((-1.05, .42), .07, fc=teal))
ring(b, (0, .42), .3)
b.add_patch(Rectangle((.72, .12), .6, .6, fc=pale, ec=teal, lw=2))
for x, text in [(-1.05, "孤立点"), (0, "闭环"), (1.02, "有角点的区域")]:
    label(b, x, -.06, text, size=11)
intervals = [(0., 1.)]
for _ in range(3):
    intervals = [(p, p+(q-p)/3) for p,q in intervals] + [(q-(q-p)/3, q) for p,q in intervals]
for p, q in intervals:
    b.plot([2.4*p-1.2, 2.4*q-1.2], [-.7, -.7], color=orange, lw=4)
label(b, 0, -.98, "排除 Cantor 式无限碎裂（图中仅为有限示意）", orange, 10)
label(b, 0, -1.4, "可以不凸、不光滑；紧零簇只有有限个组件")

c.set_title("C  严格环形吸引管 + 全局总指数为 1", color=ink, fontsize=15, pad=14)
ring(c, tube=True)
c.add_patch(Circle((.13, .12), .09, fc=orange))
label(c, .13, .12, "?", "white", 10)
label(c, 0, -.3, "环内还须有零点\n具体位置未定", orange)
label(c, 0, -1.4, "已知环簇之外必须补偿；橙点仅标记存在性")

d.set_title("D  再要求全空间轨道趋向同一零簇", color=ink, fontsize=15, pad=14)
d.add_patch(Rectangle((-1.25, -.45), .9, .9, fc=pale, ec=teal, lw=2))
label(d, -.8, 0, "整块零集\n仍然允许", teal)
ring(d, (.85, 0), .43)
d.plot([.48, 1.22], [-.48, .48], color=orange, lw=2)
label(d, .85, -.75, "环洞不能保留", orange, 11)
label(d, 0, -1.4, "集合整体必须可缩；不同初值仍可趋于不同零点")

fig.suptitle("RLEB 条件怎样约束零点集合", fontsize=22, color=ink, y=.975)
fig.text(.5, .923, "青色：已认证零簇　浅色：邻域／区域　橙色：补偿或排除", ha="center", color=ink, fontsize=11)
fig.text(.5, .028, "条件逐项标在图上。仅锚定多值 RLEB 不自动给出 B；箭头是环形模型的极限方向。", ha="center", color=ink, fontsize=10)
fig.subplots_adjust(left=.045, right=.955, top=.845, bottom=.08, hspace=.43, wspace=.16)
fig.canvas.draw()
for text in fig.findobj(matplotlib.text.Text):
    if text.get_visible() and text.get_text():
        box = text.get_window_extent(fig.canvas.get_renderer())
        assert box.x0 >= 0 and box.y0 >= 0 and box.x1 <= fig.bbox.width and box.y1 <= fig.bbox.height
for ext in ("png", "pdf", "svg"):
    path = out / ("RLEB零点集合直观特征." + ext)
    fig.savefig(path, dpi=200, facecolor=fig.get_facecolor())
    if ext == "svg":
        path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
plt.close(fig)
print("Saved PNG, PDF and SVG; text bounds passed.")
