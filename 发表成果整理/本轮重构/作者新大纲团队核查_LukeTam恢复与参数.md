# 作者新大纲团队核查：Luke–Tam 的线性恢复与参数

日期：2026-10-14。范围只限摘要的两条收敛路线及先行结合工作、第二章线性阶的恢复与参数比较。未改主稿、总大纲、Claim 或研究图；未作穷尽新颖性检索。

## 核查结论

1. **现行能量推论确实严格改进 Luke–Tam 正式版 Theorem 2 印出的充分参数预算和距离收缩因子。** 比较采用同一个原关系、同一步长、同一真残差误差界常数、同一目标距离、同一实际输出及认证窗。这不是只与 2023 扩展摘要或自行造出的粗估计比较。
2. 改善来自保留输出真误差界与一步平方能量的配合；Luke–Tam 正式版采用 Lemma 1 的输入步残差桥后估计。**这项代数机制在单调端点已经出现在 Leventhal 2009 Theorem 3.1 中。** 不能把单调性与次正则性的结合本身，或能量消元本身，写成首次。
3. “恢复 Luke–Tam”须分清两层：同一认证局部步上，线性几何、真实残差桥、距离 Q 线性与点误差 R 线性的机制可以精确重构；现稿并没有自动包含 Luke–Tam 对任意相对状态集 `D` 的全部局部定理。完整定理的包含还须携带相同 `D`、自映射、局部覆盖、截断选择及目标集。
4. **当前能量因子可以在具体完整线性算子上精确取等，但其显示参数门不能无范围地称为所有参数的最终 sharp 门。** 同一前件还保留直接步长估计，某些参数下它优于单独的能量消元。具体范围须接团队锐性核查，不把一例取等扩大为全参数最优。

## 一手版本和内部读取范围

正式比较源为 D. Russell Luke、Matthew K. Tam，*Generalized Monotonicity and the Proximal Point Algorithm*，*Mathematics of Operations Research*，Articles in Advance，2025-11-21，DOI [10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/full/10.1287/moor.2025.0863)。核查其 Definition 1、Definition 2、Proposition 3，以及 §4 的 Lemmas 1–2、Assumption 2、Theorem 2 和 Corollary 1/Remark 3；正式 PDF 印页 9–12。没有把 2023 RAMP 扩展摘要编号归给正式版。

本地正式 PDF 为 `tmp/semimonotone_sources/LukeTam.pdf`，对应提取文本已检查；出版社 HTML 的同式交叉复核成功。[出版社 PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)。正式版于引言明确把 2023 版本的“存在收敛选择”提升为其局部截断范围内的任意选择；不能继续把正式版描述为只控制存在的一条轨道。

内部对照读取：

- `发表成果整理/RLEB/sections/related_work.tex` 的线性参数识别与 `cor:linear-energy-convergence`。
- `发表成果整理/RLEB/sections/theorem_spine.tex` 的一般模主定理、幂次推论、输出真残差与严格长度预算。
- `research/canonical/true_residual_selection_rleb.md` 的允许近端关系、目标集身份及 Luke–Tam 截断覆盖映射。
- `research/novelty/2026_10_09/core_prior_art.md` 的原算子残差桥与两种线性预算；旧页已提示二者不是同一个预算。
- `research/LITERATURE.md` 的正式版读取记录及 Leventhal 分子辨识；`research/literature_refresh_2026_10_08.md`；早期 `RL_novelty_and_publication_assessment.md` 仅作历史边界对照。

## 正式版实际前件和结论

记 `D` 为源文相对状态集，`Z=zer F∩D`。源文 Assumption 2 有以下共同对象，而不是只有两个标量条件。

| 项 | 正式版的作用 | 恢复时必须带入的对象 |
|---|---|---|
| 2(a) | `Z` 非空闭 | 同一目标零集，而非未经比较的严格零子集 |
| 2(b) | `J_{λF}:D⇉D` 自映射 | 输入、输出保持同一个 `D` |
| 2(c) | 原算子在零点邻域的真残差误差界，常数 `ρ̄`；相应输出落入误差界邻域的输入集合非空 | `d(y,Z)≤ρ̄ d(0,F(y))`，误差界评价的是完整原关系 |
| 2(d)(i) | `λF` 在 `U×W` 上极大次单调，缺陷 `τ≥0` | 缩放的是 `λF`，图值窗是缩放后的 `W` |
| 2(d)(ii) | `U'⊂(I+λF̄)(U)`，`F̄(u)=F(u)∩(W/λ)`；并要求 `τ(1+ρ̄/λ)^2<1/2` | 同一截断图的 Minty 输入覆盖和参数门 |

Theorem 2 控制其给出的局部球内的选择
\[
x^{n+1}\in J_{\lambda F}(x^n)\cap B_\delta(\bar x),
\]
不是未经截断的完整近端纤维全部远端输出。其结论是收敛到局部零点的 **R 线性点收敛**。证明先对同一局部零集距离得到 **Q 线性**估计，再用 Lemma 2 的线性步长界求尾和。

若正文确要写“完整恢复其任意 `D` 的版本”，可在主定理明确允许不变状态集：把输入域写为 `D∩U_R`，并要求每个允许输出仍在 `D`，目标取闭 `S=zer F∩D`。有限前缀证明只需在每一步同时追踪 `x^k∈D`，其余距离、能量、长度和留开域论证不变。再携带源文截断图覆盖即可复用其局部对象。**这是可写明的相对状态扩展，不是现稿 `U_R` 全域量词已经自动包含 `D∩U_R`。** 本报告仅给准确修改方向，没有替作者更改主定理。

符号须照原文分开：Assumption 2(c) 的已认证误差界常数为 `ρ̄`；Theorem 2 证明任选稍大 `ρ>ρ̄`，仍使 `τ(1+ρ/λ)^2<1/2`。其显示因子为
\[
\kappa_{\rm LT}
=\sqrt{1+2\tau-\left(\frac{\lambda}{\lambda+\rho}\right)^2}.
\tag{LT1}
\]
先平方比较 `κ_LT²`，然后取根。不能把根内量写成距离 Q 因子；也不能把 R 线性点误差改成点误差每一步 Q 收缩。由于稍大常数可以任取，使用已认证 `K=ρ̄` 时，下面的 `κ_LT(K)` 是该证明显示因子的下确界；实际选 `ρ>K` 的因子更大。

Lemma 1 的真实作用为
\[
d(x,Z)\le\|x-y\|+d(y,Z)
\le\left(1+\frac{\rho}{\lambda}\right)\|x-y\|,
\qquad y\in J_{\lambda F}(x).
\tag{LT2}
\]
这里用的是 `r_F(y)≤||x−y||/λ`，并没有把所选图值范数与真残差相等同。Lemma 2 的条件是 `s_n≤c d_n` 和 `d_{n+1}≤κd_n`，直接给有限长度与 `||x^n−x∞||≤cκ^n d_0/(1−κ)`。这部分不是我们的新距离—长度原理。

## 线性阶的准确恢复和严格改善

设同一已认证局部步满足线性零锚反射估计与真残差误差界：
\[
\|2y-x-p\|\le Ld(x,S),\qquad
p\in P_S(x),\qquad
d(y,S)\le K r_F(y),\qquad
r_F(y)\le\frac{s}{\lambda},\quad s=\|x-y\|.
\]
在共同受检点对上，Luke–Tam 缺陷的精确缩放为
\[
\lambda\langle y-p,v\rangle
\ge-\tau\|(y-p)+\lambda v\|^2,
\qquad v=(x-y)/\lambda,
\qquad L^2=1+4\tau.
\tag{MAP}
\]
因此 `τ=(L²−1)/4` 仅用于 `L≥1` 的非负缺陷约定；`L<1` 的更强正性不能给源文一个负 `τ`。若只能用非负缺陷，则可放松为 `τ=0`，但会丢掉较强常数。

平行四边形给相同能量
\[
(d^+)^2+s^2\le\frac{1+L^2}{2}d^2=(1+2\tau)d^2.
\tag{E}
\]
由三角界 `d≤s+d^+≤(1+K/λ)s`，代回 (E)，立刻重构正式版显示的因子与预算：
\[
(d^+)^2\le\left[1+2\tau-
\left(\frac{\lambda}{\lambda+K}\right)^2\right]d^2,
\quad
\tau(1+K/\lambda)^2<\frac12.
\tag{R-LT}
\]
但是保留输出处的同一个真误差界 `d^+≤(K/λ)s`，直接消去 (E) 中的 `s²`，得到现稿能量推论：
\[
\rho_E^2=\frac{1+L^2}{2\{1+(\lambda/K)^2\}}
=\frac{1+2\tau}{1+(\lambda/K)^2},
\qquad
2\tau(K/\lambda)^2<1.
\tag{R-E}
\]
**这两种参数并不相同。** 令 `a=K/λ>0`，则
\[
\kappa_{\rm LT}(K)^2-\rho_E^2
=\frac{2\{a+\tau(1+a)^2\}}
       {(1+a^2)(1+a)^2}>0\qquad(\tau\ge0).
\tag{GAP}
\]
源门是 `τ<1/[2(1+a)²]`，能量门是 `τ<1/(2a²)`，后者严格更宽。比较源文稍大 `ρ>K` 时，严格改善仍成立。

改善的精确对象是 **Theorem 2 的显示充分门及显示距离因子**。这不证明原文所研究算法在旧门外不收敛，也不证明我们的整体理论优于其所有结果。源文 Remark 3 已单独回收 Leventhal 的单调端点。

当前一步反射还给 `s≤(1+L)d/2`，从而
\[
\|x^\infty-x^k\|
\le\frac{1+L}{2(1-\rho_E)}d(x^k,S).
\]
这给线性阶点误差的 R 因子 `ρ_E`；无需改变成点误差 Q 因子。局部球、初值预算及前置覆盖不同，不能只看这一尾系数就声称严格改善源文所有球半径或所有前因子。

## 同算子的严格参数见证，以及 sharp 的限制

令 `X=R²`、`λ=1`、`S={0}`，`Q` 为逆时针 90° 旋转，取完整线性算子
\[
F=-\frac27 I-\frac{3\sqrt5}{7}Q,
\qquad
J_F=\frac12 I+\frac{3\sqrt5}{10}Q.
\]
有
\[
F^\top F=I,\quad
J_F^\top J_F=\frac7{10}I,\quad
(2J_F-I)^\top(2J_F-I)=\frac95I.
\]
所以真误差界锐常数是 `K=1`，全对反射锐常数 `L²=9/5`，次单调锐缺陷 `τ=1/5`。完整近端覆盖全域。其完整图的极大次单调性也可直接检查：任意拟添加图点具有某个 Minty 输入，而原图在该输入已经有唯一图点；次单调不等式在相同输入的两图点上强制输出相同。

在完全相同的 `F,λ,K,τ` 上，源门左边为 `τ(1+K/λ)²=4/5>1/2`，不能调用源 T2 的显示充分条件；新门左边为 `2τ(K/λ)²=2/5<1`。新因子 `ρ_E²=7/10` 恰等于实际每步距离比的平方；这明确显示参数改善，并在该参数点认证能量因子的取等。任意有限局部误差界窗都可按现稿要求缩小 `R` 后使用，误差界和完整输出没有换对象。

但 (R-E) 不是无条件的全参数最终 sharp 门。相同前件还给直接因子
\[
\kappa_D=\frac{K}{2\lambda}(1+L).
\]
例如 `a=K/λ=1/4`、`τ=8`，能量门恰在边界 `2τa²=1`，却有
\[
\kappa_D=\frac{1+\sqrt{33}}8\approx0.84307<1.
\]
因而同一真误差界和反射条件仍足以保证收缩。这个反算直接阻止“能量门是所有参数下的必要充分边界”这一强句。建议将 sharp 具体写成已证明的参数扇区、最优统一包络或显示模型的取等身份，并由团队另文提供完整锐性证明。

## 单调端点及摘要的历史位置

当 `L=1,τ=0`，(R-E) 化为
\[
\rho_E=\frac{K}{\sqrt{K^2+\lambda^2}}<1
\qquad\text{对每个 }\lambda>0.
\]
这正是 Leventhal 2009 Theorem 3.1 的距离因子（其误差界常数取任何严格大于次正则模的可行常数）；没有额外 `λ>K` 门。原文证明明确保留 `d_{k+1}²+s_k²`，再把输出误差界代入，正与这里的单调端点同式。

Luke–Tam 正式版 Remark 3 的式 (31) 将分子印为 `λ²`；按其固定 `λ` 为近端步长、`ρ` 为误差界常数的约定，这与 Leventhal 原文和该能量推导不一致。现库此前已经指出这个分子问题。应引用 Leventhal 原文的 `K²/(λ²+K²)`，不能为“与 Luke–Tam 精确相同”而照抄该印式。

| 一手文献 | 可支持的摘要/引言位置 | 不能由它支持的强句 |
|---|---|---|
| R. T. Rockafellar (1976), *Monotone Operators and the Proximal Point Algorithm*, SIAM J. Control Optim. 14(5), 877–898；[作者全文](https://sites.math.washington.edu/~rtr/papers/rtr066-MonoOpProxPoint.pdf)，DOI `10.1137/0314056`，§3 式(3.1)、Theorem 2 | 经典极大单调 PPA；其单点逆 Lipschitz 条件给唯一零点的线性收敛 | 把该附加条件改成不要求唯一零点的普通次正则性；或改成整个邻域内两点逆 Lipschitz |
| F. J. Aragón Artacho、A. L. Dontchev、M. H. Geoffroy (2007), *Convergence of the Proximal Point Method for Metrically Regular Mappings*, ESAIM: Proceedings **17**,1–8；[出版 DOI](https://doi.org/10.1051/proc%3A071701)，Theorems **3.1、4.2、4.4** | Banach 空间之间的一般关系；度量正则性加局部闭图及充分小的近端扰动，保证每个邻近初值**存在**局部线性收敛序列；扰动 Lipschitz 常数趋零时可选超线性序列。强次正则性结果控制已存在且留在认证邻域的序列；强正则性再给邻域内唯一选择 | 只凭普通次正则性得到同结论；删除存在/留域量词；把小扰动系数误写成通常 PPA 小步长 |
| D. Leventhal (2009), *Metric Subregularity and the Proximal Point Method*, J. Math. Anal. Appl. 360(2), 681–688；[作者预印本全文](https://arxiv.org/pdf/0902.4200)，DOI `10.1016/j.jmaa.2009.07.012`，Theorem 3.1 | Hilbert 极大单调与普通度量次正则性结合，给零集距离局部 Q 线性；无需零点唯一 | Luke–Tam 是“首次把单调性和度量次正则性结合” |
| R. T. Rockafellar (2023), *Generic linear convergence through metric subregularity in a variable-metric extension of the proximal point algorithm*, Comput. Optim. Appl. **86**(3), 1327–1346；[作者全文](https://sites.math.washington.edu/~rtr/papers/rtr261-VariablePPA.pdf)，DOI `10.1007/s10589-023-00494-z`，Theorems 2.2、3.1 | 变度量/允许误差 PPA 的普通次正则性；有限维局部极大单调的可执行性与局部化 | 将全局极大单调与局部极大单调及其更新限制混成一个无条件结论 |
| Luke–Tam 2025 正式版，引言和 Assumption 2/Theorem 2 | 量化次单调性与普通度量次正则性共同保证适当局部选择的 R 线性点收敛；正式版自己引用 Leventhal [23]、Rockafellar 2023 [36] | 全球第一个结合者；只控制存在选择；未截断完整近端全部输出无条件收敛 |

Rockafellar 2023 作者 PDF 首页卷号为 85，而出版社和 Luke–Tam 正式版参考文献为 **86(3)**；书目采用后者。Leventhal arXiv 原稿页首显示重新编译日期 2018-10-26，版本标识仍为 `0902.4200v1`、2009-02-24，出版年份仍为 2009。

2007 正则性论文的原式为 `0∈g_n(x_{n+1}−x_n)+T(x_{n+1})`，`g_n(0)=0`，在同一原点邻域具有 Lipschitz 常数 `ℓ_n`。Theorem 3.1 要求 `sup ℓ_n<1/(2 reg T(\bar x|0))`；若 `g_n(u)=ℓ_nu`，通常近端步长是 `t_n=1/ℓ_n`。因此小 `ℓ_n` 与趋零 `ℓ_n` 对应大步长与趋无穷步长。Theorem 4.2 的条件收缩为 `||x_{n+1}−\bar x||≤κℓ_n/(1−κℓ_n)||x_n−\bar x||`，它自身不供应更新存在或留域。

该文[出版社原始全文 URL](https://www.esaim-proc.org/articles/proc/pdf/2007/02/proc071701.pdf)已定位，但本轮公共读取返回 403；[作者机构条目](https://orbilu.uni.lu/handle/10993/10818)读取亦受限。核查者实际阅读的是公开镜像中所附**原出版论文** pp.3–6，未用附加评论或二手论述承担定理判断；没有将这个读取记录伪称出版社直读成功。若最终把“原站直读”作为引用准入标准，则先只用已直读 Luke–Tam 引言对该路线的定位，待取得原站全文后再搬入细参数。

作者口述姓名应按数学出处落定：`Minty` 对应 1962 年 *Monotone (nonlinear) operators in Hilbert space*（Luke–Tam [29]）；`Luke–Tam` 对应上面的正式版。若句子实际指 PPA 的提出者，则 `Martinet` 1970 又是另一项史实，Numdam 原始条目为 [Brève communication. Régularisation d'inéquations variationnelles par approximations successives](https://www.numdam.org/item/M2AN_1970__4_3_154_0/)，4(R3),154–158。不能仅凭“Manetti”音形把 Minty 与 Martinet 合并，也不据语音补猜第三个人名。摘要可避免含混音译，直接列已核书目作者与年份。

## 第二章与摘要的可用写法

第二章依作者安排先列共同假设，再写一般模 PPA 主定理、幂次显式推论；随后把线性误差界的能量推论接在这一链上。比较节只回引这条结果并给参数识别，不在后部重新证明一遍。**线性恢复必须展示 (R-LT) 与 (R-E) 两个式子，才能使读者准确区分恢复旧机制和严格改进其显示参数。** 不能仅令 `γ=1` 后使用直接门 `κ_D<1`，那会遗漏所有步长的经典单调恢复。

可安全用于摘要/大纲的句子：

- “近端点法的收敛分析既有以单调性及其非扩张几何为基础的路线，也有 Aragón Artacho、Dontchev、Geoffroy 以度量正则性保证局部收敛选择序列的路线；单调性与度量次正则性的结合已见于 Leventhal 的线性收敛分析，Luke–Tam 进一步在量化次单调框架下给出适当局部近端选择的线性收敛保证。”
- “本文将反射几何与完整原关系的真实残差误差界在同一输出窗内配合，给出全部允许选择的局部有限长度与点收敛；线性阶重构 Luke–Tam 的收敛机制，并严格放宽其 Theorem 2 显示的充分参数条件、改善相同常数下的距离收缩因子。”
- 若摘要只能保留极短比较：“在线性阶，该结果恢复经典单调 PPA 的次正则收缩，并在共同认证条件下改进 Luke–Tam 的显示参数预算。”

禁写或须补限定的强句：

- “Luke–Tam 首次结合单调性和度量次正则性。”
- “我们的因子与 Luke–Tam 原文完全一样。”
- “只在旧版/粗估计上更好，正式版没有改善。”——与已核正式 T2 公式不符。
- “我们的输出残差误差界是新东西，他们只有输入残差。”——源 Lemma 1 明确从完整原算子输出真残差导出输入桥。
- “Luke–Tam 只保证存在一个收敛近端选择。”——这是其旧扩展摘要与正式版的区别，不能归给正式 T2。
- “本定理直接包含 Luke–Tam 任意 `D` 的完整定理，并控制其未截断全部输出。”
- “显示能量门和因子在全部 `L,K,λ` 下都是 sharp。”——上面的直接因子反算阻止此句。
- “线性阶严格改善 Leventhal 因子。”——单调端点同式；目前改善比较对象是 Luke–Tam T2 显示因子。

## Python 复算

以 Python 3 `fractions.Fraction` 对 64 组有理 `a>0,τ≥0` 检查 (GAP) 的精确恒等式与严格正性，并检查两种 `<1` 因子门分别等价于显示参数预算。另把矩阵写成 `αI+β√5Q`，用 `Q²=−I` 的有理系数乘法，精确检查见证的逆恒等式、`FᵀF`、`JᵀJ`、反射平方和次单调零余量。结果全部通过：

```json
{
  "exact_FtF": "I",
  "exact_JtJ": "(7/10)I",
  "exact_CtC": "(9/5)I",
  "sharp_tau": "1/5",
  "sharp_K": "1",
  "lambda": "1",
  "LT_budget_lhs": "4/5 > 1/2",
  "energy_budget_lhs": "2/5 < 1",
  "energy_factor_squared": "7/10",
  "LT_factor_squared_same_K": "23/20",
  "rational_checks": 64,
  "direct_factor_at_energy_boundary_a_1/4": 0.8430703308172536
}
```

有限算术核验确认公式计算，没有代替上面的全参数代数证明、局部留域证明或外部先行性认证。

核心复算代码（只需 Python 标准库，可直接运行）：

```python
from fractions import Fraction as Rat

checks = 0
for a in map(Rat, ['.01', '.1', '.25', '.5', '1', '2', '10', '100']):
    for tau in map(Rat, ['0', '.0001', '.01', '.1', '.2', '.5', '1', '10']):
        old = 1 + 2*tau - 1/(1+a)**2
        new = (1+2*tau)*a*a/(1+a*a)
        gap = 2*(a+tau*(1+a)**2)/((1+a*a)*(1+a)**2)
        assert old-new == gap > 0
        assert (tau*(1+a)**2 < Rat(1, 2)) == (old < 1)
        assert (2*tau*a*a < 1) == (new < 1)
        checks += 1

# 系数对表示 alpha*I + beta*sqrt(5)*Q，Q^2=-I。
def mul(x, y):
    a, b = x
    c, d = y
    return a*c-5*b*d, a*d+b*c

def transpose(x):
    return x[0], -x[1]

identity = (Rat(1), Rat(0))
f = (-Rat(2, 7), -Rat(3, 7))
j = (Rat(1, 2), Rat(3, 10))
c = (Rat(0), Rat(3, 5))
g = (1+f[0], f[1])
assert mul(j, g) == identity
assert mul(transpose(f), f) == identity
assert mul(transpose(j), j) == (Rat(7, 10), Rat(0))
assert mul(transpose(c), c) == (Rat(9, 5), Rat(0))
assert f[0] + Rat(1, 5)*mul(transpose(g), g)[0] == 0
print('PASS', checks)
```
