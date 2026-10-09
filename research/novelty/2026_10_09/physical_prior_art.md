# C210/C214 的物理长度先行核对及临界共振推进

本报告由独立任务代理完成。基线为主代理指定的 5726c10083cb2dbaef52e2ec802d89c8fd9d39c1；没有修改旧 Claim、旧 canonical 或总账，没有 commit/push。主代理随后明确授权新建 C219 的独立证明与复算文件。

## 1. 裁决与适用边界

**几何半阶、一般 inverse-Hölder 不保长度、以及复合 Dini 的采样求和，不宜作为全球首创点。** 已找到与 C214 射线限制完全同式的 2019/2021 一级先行。完整 GPPA 的全图编码、残差身份和允许输出桥不由该几何论文自动提供。没有检索命中整个 GPPA 合取，不是全球新颖性证明。

| 被审原子 | 本轮判断 | 留下的实质义务 |
| --- | --- | --- |
| C210：核 Cauchy + 全端点逆模零连续 ⇒ 物理 Cauchy | 连续模直接作用于两端点的初等推导；独立首创价值弱 | 必须在实际全端点域有同一模；物理极限属于同一零集另用闭性/真 EB/完整拉回 |
| C210：\(\sum\eta(B(\kappa^jr))<\infty\) 与 \(\int\eta(B(t))dt/t<\infty\) | 单调几何采样的积分比较；Dini 是步包络的等价判据，不是每个轨道长度的必要条件 | 认证原 GPPA 的实际步包络、全纤维输出、coverage、领圈和留域 |
| C210：Hölder 逆能输送点但未必输送有限长 | 经典 variation/spiral 现象；不能单列成新发现 | 明确点尾、相邻步和全端点模的不同量词 |
| C214：\(r e^{ic/r}\) 的最佳射线指数 \(1/2\) | Fraser Th2.3 已直接覆盖，含正负相位与尺度换元 | 整个平面 twist 及其平面 inverse 的 all-pairs 模需要额外论证；仓库 GP33 提供了该桥 |
| C214：连续螺旋可能无限长 | 已有一级文献的长度积分直接解释 | 连续弧无限长不能推出指定离散采样长度无限；必须证明 GP37–39 或共振分类 |
| C214：完整核有限长、物理趋零却长度无限 | 已读几何/优化源没有直接陈述同一完整 GPPA 合取 | 不能据此宣称没有其它先行、或任意换图/坐标均无法导入 |
| 新 C219：\(a=2\) 的全 \(c\) 判据 | 本轮得到严格独立证明与余项控制；补足原“可能共振”提醒 | 尚无全球优先性认证；只授予指定临界尾轨道 |

## 2. 一级来源与实际阅读回执

下列都是作者论文、作者书稿或出版者原文；检索摘要没有代替所列定理正文。读取范围不等于全篇验收。

<a id="ppa-frase"></a>
### 2.1 Fraser：C214 的射线函数已有精确先行

Jonathan M. Fraser, *On Hölder solutions to the spiral winding problem*，2019 作者预印本 [arXiv:1905.07563v1 PDF](https://arxiv.org/pdf/1905.07563)。对应刊本书目信息为 *Nonlinearity* 34 (2021), 3251–3270；本轮定理调用严格使用所读 v1，未核刊本逐条版本差异。

实际读：§1；§2 Theorems 2.1–2.3、Corollary 2.4（PDF pp.4–5）；§3 的 forward 正则性和最高指数证明（PDF pp.6–8）。inverse 的定理陈述已核，证明未全文重审。另请求了 PDF p.5 截图，但检索后端只回图片占位，未进行图片目读；公式依据 PDF 正文解析。

Th2.3 定义

\[
g_t(x)=x^{tp}e^{i/x^t},\qquad p,t>0,
\]

其 forward 最佳指数为 \(\min\{tp/(t+1),1\}\)，inverse 指数按原文 \((\alpha,\beta)\)-Hölder 定义为 \(1/\max\{tp,1\}\)。取 \(p=t=1\) 即 C214 的径向曲线 \(r e^{i/r}\)。常数 \(c\ne0\) 经正尺度换元和共轭不改变最佳 \(1/2\)。

**精确挑战**：这个 inverse 是“螺旋弧 → 参数区间”的逆，在此 \(p=t=1\) 是 Lipschitz；C214 的 \(g^{-1}:\mathbb C\to\mathbb C\) 是反向 twist，是另一个对象。不能把前者的 inverse 指数写成后者的平面 inverse 结论。射线限制却已足以阻断整个平面上任何大于半阶的模。

### 2.2 Chrontsios-Garitsis–Vellis：variation 已为螺旋正则性提供精确量尺

*Hölder spiral arcs*，[arXiv:2502.18788v3 HTML](https://arxiv.org/html/2502.18788v3)，2025-07-30。实际读：§1、Th1.1、§2 Prop2.1 及证明、§3 Th3.1 及证明。

Prop2.1 把 metric arc 的 \(s\)-variation 与最佳 \(1/s\)-Hölder 参数化常数相联系。Th1.1 对 almost circular spiral、\(s>1\)，以各整圈最大半径的 \(s\) 次幂求和给充要条件；Th3.1 的一般整圈版本允许 \(s\ge1\)。

**精确挑战**：这些结论关于整条连续 arc 的参数化，不认证 GPPA 的指定时间采样、核/物理残差、完整纤维或零集。因此可直接削弱几何首创措辞，不能自动吞并完整 C214。

### 2.3 Friz–Victoir：有限长度经 Hölder 映射自然给高阶 variation

作者书稿 [*Multidimensional Stochastic Processes as Rough Paths*, May 6 draft PDF](https://page.math.tu-berlin.de/~friz/master4_May6th.pdf)。实际读：ch.5 的 variation 定义、Prop5.10 与 Prop5.15，PDF pp.99–102，邻近印刷 pp.85–89。本草稿为 Prop5.15，未核正式书版编号；不得冒写为已核正式 Prop5.14。

Prop5.15：连续有限 \(p\)-variation 路径可经连续递增时间变换写成 \(1/p\)-Hölder 路径。与 variation 定义直接配合，\(\alpha\)-Hölder 映射将有限 1-variation 路径送到有限 \(1/\alpha\)-variation；不授予有限 1-variation。

### 2.4 Monti–Socionovo：连续螺旋长度积分已属现成工具

Roberto Monti、Alessandro Socionovo，[*Non-minimality of spirals in sub-Riemannian manifolds*](https://link.springer.com/article/10.1007/s00526-021-02077-4)，*Calc. Var.* 60, 218 (2021)。实际读：作者、日期、引言的曲线形式与 §6 开头的 (6.1) 和紧邻 rectifiability 说明；未验收其非极小性主定理证明。

该处的平面投影为 \(t e^{i\varphi(t)}\)，长度为

\[
\int_0^1\sqrt{1+t^2\varphi'(t)^2}\,dt,
\]

并给 \(t\varphi'\in L^1\) 的 rectifiability 门。代入 \(\varphi(t)=ct^{-b}\)，\(c\ne0\)，连续径向螺旋有限长恰在 \(b<1\)。

**精确挑战**：原无限长连续弧的某次稀疏采样仍可有限长；原 C214 的 \(a>2\) 就是这种情况。整圈共振更直接显示连续长度和离散长度必须分开。

### 2.5 Attouch–Bolte–Svaiter：KL 抽象下降已广泛给有限长度

[*Convergence of descent methods for semi-algebraic and tame problems: proximal algorithms, forward–backward splitting, and regularized Gauss–Seidel methods*，作者 PDF](https://bolte.perso.math.cnrs.fr/MPA.pdf)，对应 *Math. Programming* 137 (2013), 91–129。实际读：§2.3 H1–H3、Lemma2.6 的初值长度预算与证明、Th2.9–2.10（作者 PDF pp.8–13）。请求 PDF pp.8、12 截图后仅返回占位；上述公式核对依赖正文解析。

Th2.9 对 \(\mathbb R^n\) 上 proper-lsc \(f\)，要求充分平方下降 H1、相对 subgradient 步误差 H2、值连续聚点 H3，以及该聚点的 KL 性；给趋临界点与有限长度。Th2.10 另有 H4 局部模型门给留域。

**与 C210 的关系**：若为同一物理轨道另造出这样的 \(f\) 并认证全部门，就能调用该源；C210 没有要求这套目标函数数据。C214 的已证无限长轨道不可能同时满足 Th2.9 全部前件，这是逻辑反证，不是对任意改图/升维的排除。仅喊“没有 KL 假设”不足以证明新颖。

### 2.6 Bolte–Daniilidis–Ley–Mazet：一般 desingularizing 模与长度积分更早已有

[*Characterizations of Łojasiewicz inequalities: subgradient flows, talweg, convexity*，作者 PDF](https://bolte.perso.math.cnrs.fr/grad_talweg.pdf)，对应 *Trans. AMS* 362 (2010), 3319–3363。实际读：§3.3 的 (23)–(24)、Th18/Remark19（作者 PDF pp.15–17）；§3.4 Lemma23、Th24 及相邻证明（PDF pp.22–23）。Th18 的请求截图只回占位；核对依赖正文解析。

Th18 在 lsc-semiconvex、非临界小正层和局部 norm-compact sublevel 下，将 KL、subgradient 曲线长度、talweg 有限长及 level 上 inverse slope 可积联系起来。Th24 对 semiconvex 函数的真正 proximal minimization 和适当 tail KL 模给强收敛与函数值模控制。

**精确挑战**：其积分变量是目标函数值，integrand 是 level 上 inverse slope；GP13 是核零距离的几何采样、integrand 为物理步模。没有 \(F=\partial f\)、同一目标值/距离和 descent identity 桥，不能把两种积分写成同一 theorem。一般“非幂 desingularizing 模 + 长度”也不能独立作为新发现。

## 3. C210 可从什么直接推出，什么仍需 GPPA 桥

此节为独立数学比较，不归因于任何未读定理。

设核轨道 \(z_k=v(x_k)\) 有尾变差 \(L_k\to0\)。全端点界

\[
\|x_j-x_k\|\le\eta(\|z_j-z_k\|)\le\eta(L_k)
\]

立即给物理 Cauchy。若只知相邻界，则这个论证不成立；须求和相邻物理步。
若 \(d_k\le\kappa^kr\) 且核步 \(\|z_{k+1}-z_k\|\le B(d_k)\)，则

\[
\sum_k\|x_{k+1}-x_k\|\le\sum_k\eta(B(\kappa^kr)).
\]

对非减 \(H=\eta\circ B\)，在每个几何壳积分比较便是 GP16。这个部分不利用 PPA、残差或单调性，因而不宜独立标成 PPA 创新。反过来，单独抽象求和并未给 GPPA 轨道存在、全纤维控制、核收缩、物理零成员或留域；这些合取是原定理真正应被审的内容。

例如 \(\eta(t)\asymp t^\alpha\)、\(B(t)\asymp[\log(e/t)]^{-a}\)，包络 Dini 恰为 \(a\alpha>1\)。这只是该统一包络的门；SR4 的共振轨道在 \(a\alpha=1\) 仍有限长，精确示范“包络充分”与“实际轨道必要”的差别。

## 4. 两参数 twist：可证明的边界与不能贸然推广的区域

为避免 \(b=\log4\) 的字母冲突，此节令 twist 功率为 \(b>0\)，另记 \(h=\log4\)。保留原完整 \(G_a\)，定义

\[
g_b(z)=e^{ic|z|^{-b}}z,\quad g_b(0)=0,\qquad
v_b=(g_b^{-1},I),\quad F_{a,b}=G_a\circ v_b .
\]

全图 coverage、正常真残差和零集身份均按原 C214 的双射拉回保持。以下只讨论同一负实射线核尾 \(w_k=(-\rho_k,0,y_k)\)，\(a>1,c\ne0\)。

### 4.1 平面逆模指数和先行映射

令 \(\delta=|z-z'|\)、\(R=\max(|z|,|z'|)\)。若 \(\delta\ge R/2\)，输出差不超过 \(4\delta\)；否则两半径至少 \(R/2\)，均值定理给

\[
|g_b(z)-g_b(z')|
\le\delta+|c|b2^{b+1}\delta R^{-b},\qquad
|g_b(z)-g_b(z')|\le2R.
\]

在 \(R=\delta^{1/(b+1)}\) 两侧分用这两界，得全域模
\(C(\delta+\delta^{1/(b+1)})\)；同证明给平面 \(g_b^{-1}\)。有界领圈内可吸收线性项。
取 \(r'=(r^{-b}+\pi/|c|)^{-1/b}\)，输入差 \(\asymp r^{b+1}\)、输出差 \(\asymp r\)，故最佳局部指数恰为 \(1/(b+1)\)。

**Fraser 参数映射**是 \(t=b,p=1/b\)，所以相同最佳射线指数已有 Th2.3；新写的平面估计只是明确其 GPPA all-pairs 桥，不能另称几何首创。

### 4.2 实际采样长度不等于 \(a>b+1\)

令 \(p=a-1>0\)，\(K=h^{-a}/(a-1)\)。对整条小窗对数尾，

\[
\rho_k\sim Kk^{-p},\qquad
\Delta\theta_k\sim cbpK^{-b}k^{bp-1}.
\]

当 \(bp<1\) 时，角增量趋零而径向变化相对角弦为小量，故

\[
|g_b(-\rho_{k+1})-g_b(-\rho_k)|
\sim |c|bpK^{1-b}k^{p(b-1)-1}.
\tag{PA1}
\]

这是由极坐标弦长恒等式直接得出的实际步，不是松 Hölder 包络。

| 参数区域 | 指定轨道的可证结论 | 证明 |
| --- | --- | --- |
| \(0<b<1,\ a>1\) | 总物理长度有限 | 连续径向弧的导数长度积分有限；单调半径采样弦长和被该弧长控制 |
| \(b\ge1,\ b(a-1)<1\) | 总物理长度无限 | PA1 的幂至少为 \(-1\) |
| 任意 \(b>0,\ a>2\) | 总物理长度有限 | 每步切向长度至多 \(\rho_k+\rho_{k+1}\)，半径级数可和 |
| \(b(a-1)=1\) 且相位极限不在 \(2\pi\mathbb Z\)，\(b\ge1\) | 总物理长度无限 | 弦长 \(\sim2K|\sin(L/2)|k^{-1/b}\)，\(L=cK^{-b}\) |
| \(b=1,a=2\) | 本轮 SR4 完全分类 | 非共振调和；整圈共振平方可和 |
| \(b>1,\ 1+1/b<a\le2\)，以及其它临界共振 | 本报告不宣称全称分类 | 快速相位可能存在离散 aliasing；需要额外相位分布/算术证明 |

统一平面 Hölder 包络要求 \(a/(b+1)>1\)，即 \(a>b+1\)。上表说明它一般只是充分门：当 \(b<1\) 时全部 \(a>1\) 已给此轨道有限长；当 \(b>1\) 时半径可和已能认证 \(2<a\le b+1\) 内的实际有限长。原 \(b=1\) 的校准例正好匹配半阶 Dini，不可凭一个族推广到任意指数的普适充要门。

## 5. 本轮可接续新增与复算范围

[C219 独立证明](../../canonical/gppa_spiral_resonance.md#gsr-statement) 固定 \(a=2\)、\(0<y_0\le e^{-2}\)、任意 \(c\in\mathbb R\)，得到

\[
\sum_k\|x_{k+1}-x_k\|<\infty
\iff c(\log4)^2\in2\pi\mathbb Z .
\]

该证明有 Euler–Maclaurin 的显式余项，并用准确 tail-shift 将相邻 inverse-tail 误差控制到 \(701/[1800(k+q)^4]\)。它保持原完整关系和合法 warped GPPA，不是任意人为设计的序列。

[标准库 Decimal 脚本](../../code/gppa_novelty/spiral_resonance_check.py) 已实际运行通过。\(q=3,3.5,10\)，\(k=10,100,1000,10000\)，12 组 tail/余项核验、72 组步常数核验；90 位精度，最大解析 EM 截断界约 \(3.529\times10^{-83}\)。\(q=3,k=10000\) 下各预言常数归一化比落在 \(1\) 到 \(1+1.09\times10^{-7}\)。[JSON 原结果](../../code/gppa_novelty/spiral_resonance_check.json) 保留全部参数和数值。

这不是区间算术证书，有限数值不证明长度分类。所有无穷结论由 canonical 中 SR7–15 的独立余项和求和证明承担。原 C214 的 \(c=\pi/h^2\) 不共振，原无限长裁决不变。未核全球优先性，不写“全球第一”。

## 6. 检索范围、获取限制和剩余挑战

实际联网查询覆盖 “Hölder spiral winding”、inverse-Hölder/rectifiability、Dini finite length、radial twist、p-variation composition、KL abstract descent 与 subgradient talweg。使用两个检索引擎，以上定理均读一级源正文；Fraser HTML 获取失败后改读 arXiv PDF，作者书稿的正式版编号未补猜。没有下载或读取 Library/其它对话文件。

剩余挑战按精确对象列出：

1. 对 C210 的整个 GPPA 合取寻找直接旧定理，而不是仅按 “generalized PPA / finite length” 标题匹配。
2. 若用 KL 或 metric-descent 框架导入，写同一完整轨道的 objective/metric、充分下降、相对误差、模和物理输出回代。当前没有这种通用桥，也没有排除任意允许桥。
3. 若评价 C219 的研究价值，定位为离散采样共振的校准细化和对“包络必要性”的真实边界；不要把已知半阶螺旋或一般求和重新命名。
4. \(b>1\) 的快速相位区域需要自己的数学。图像或有限 partial sum 无法代替相位分布，也不能据此补全“精确 \(a,b\) 阈值”。
