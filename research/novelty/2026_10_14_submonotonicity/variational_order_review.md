# 变分符号序、弱 Minty 与完整 PPA：有用的入口及其边界

日期：2026-10-14。范围：有限维普通 PPA 与 C249 的 `v=Id` 接口；不改主稿、Claim 总账或关系图。本页数学推导已逐式核对，外部首创性未认证。

## 1. 比较对象与读取分母

固定同一个完整关系 `F:R^n⇒R^n`、同一个 `λ>0`、原完整零集 `S=zer F` 和完整迭代

\[
J(x)=(I+\lambda F)^{-1}(x),\qquad x^{k+1}\in J(x^k),
\qquad r_F(y)=\inf_{v\in F(y)}\|v\|.
\tag{VO1}
\]

“全部选择收敛”必须同时保住输入 coverage、所有完整输出、零输入吸收、真残差评价域及局部留域。一个 VI 外投影方法、一个受限图块、一个 Minty 锚或一个选择值残差，均不能直接替代 VO1。比较点收敛、有限长度和统一率时分别写结论，不按定义中的自由度排序“本质性”。

实际使用仓库 `$academic-writing-skills` 的数学证明审查及论证模式，读取 AGENTS、RESEARCH_PROTOCOL、C249 与 C02-v3。原仓库已有平方图、负恒等、弱 Minty 排除例，以下尽量只给新的短诊断与必要桥；已有排除结论用定位引用。

| 一手版本 | 本次实际读取 | 可以导入的事实；仍需携带的前提 |
| --- | --- | --- |
| [El Farouq, JOTA 109 (2001), 311–326](https://perso.isima.fr/~naelfaro/publis/ElFarouq-JOTA-Proximal-Pseudomonotonie.pdf)；作者托管刊本 | Definition 2.1；Algorithm 3.1；Lemma 4.1；Assumption 4.1；Theorem 4.1 及证明；Lemmas 4.2–4.4；Theorem 4.2 | 其直接 Bregman/普通 PPA 已用伪单调零锚；T4.1 还要求连续、有限 weak-monotonicity 常数 L、强凸核梯度常数 b、`0<α<λ_k<b/L`，完整收敛还用核梯度 Lipschitz。不能把该文 T4.1 简写成“仅伪单调”。 |
| [Lei–He，Optimization Online，2020 作者提交稿](https://optimization-online.org/wp-content/uploads/2020/02/7602.pdf) | 全文对象声明；Defs 2.1–2.3；Prop 3.1；Algorithm 1；Prop 3.2 及证明；T3.1 及证明 | 有限维、连续单值 F、非空闭凸 C；pseudo 的符号前件为 `≥0`，quasi 为 `>0`。Prop 3.2 为连续 F 加非空 MVI 提供隐式 VI 子问题存在。Algorithm 1 选择历史切平面再投影；T3.1 的外步一般不是原普通 PPA。 |
| [Evens–Pas–Latafat–Patrinos, 2305.03605v2, 2024-05-06](https://arxiv.org/pdf/2305.03605v2) | Def 2.1；Assumption I；Lemma 2.3；T2.4 及证明；Def 2.12；T2.13 及证明 | Def 2.1：`<v,y-p>≥<v,Vv>` 对全部完整图点及 `p∈S*⊂zer F`。T2.4 另要 outer semicontinuity、完整 resolvent 满定义域、PSD P、谱正性及松弛余量；完整迭代极限需要其全零锚门。T2.13 还明列闭凸零集、全零锚、连续 resolvent 与真 metric subregularity。不混用其他版本编号。 |
| [Daniilidis–Georgiev, Approximate convexity and submonotonicity, JMAA 291 (2004), 292–301](https://www.arisdaniilidis.at/DG_ac.pdf)；作者托管 12 页稿 | §1 定义 (1)；T2；Defs 7、10、11；T12、T13 及相关证明 | 其 submonotonicity 使用局部一阶误差 `−ε||x−y||`；cyclic 版测试细分闭多边形。T13 在 Banach 空间把 locally Lipschitz、directionally approximately convex 与 Clarke 次微分的 maximal cyclic submonotonicity 相联。这是势函数表示结论，不是 PPA 收敛定理。 |

一手来源引用使用上表公共 URL；下载文件仅用于临时取证，不构成交付依赖。Langenberg 2010 的 *Pseudomonotone operators and the Bregman Proximal Point Algorithm* 此次只取得[出版社预览](https://link.springer.com/article/10.1007/s10898-009-9470-7)，未读其定理正文；不据摘要判定全类包含。Daniilidis–Georgiev–Penot 2003 的[另一个 PDF](https://www.arisdaniilidis.at/DG_cyclic.pdf)文本编码异常，本页定义依据已实际读清的 2004 一手重述，不宣称完成所有 cyclic 原始先行版本审查。

## 2. 伪单调确实可以供应完整 PPA；拟单调不能照搬

先严格限于单值 `F:C→R^n`。使用 VI 定义

\[
\langle F(x),y-x\rangle\ge0\Rightarrow
\langle F(y),y-x\rangle\ge0 \quad\text{(pseudo)},
\tag{VO2}
\]

拟单调把前件改为严格正。不是 Brézis 的弱序列 pseudomonotonicity，也不默认给任意多值原图赋同名性质。

对于 `p∈zer F`，pseudo 的前件恒为零，所以

\[
\langle F(y),y-p\rangle\ge0\quad\forall y,\ p\in S.
\tag{VO3}
\]

quasi 的严格前件在零锚处永远不触发；这是最短的逻辑断点。不能只把 `≥` 改成 `>` 而保留完整 PPA 定理。

**本页自足桥 VO-PSEUDO。** 若 `F:R^n→R^n` 全域连续、VI 意义伪单调、`S≠∅`，则任意固定 `λ>0` 的完整 `J` 满定义域、每纤维非空紧，`J(p)={p}` 对全部 `p∈S`；每条完整 PPA 轨道点收敛到 S。此桥不需要完整 J 单值。它是标准零锚/Fejér 机制的独立重构，不提出新定理先行性。

证明：对固定输入 x 和零点 p，令 `G(y)=y+λF(y)−x`。在 `||y−p||=r>||x−p||` 的球面上，VO3 给

\[
\langle G(y),y-p\rangle\ge r^2-r\|x-p\|>0.
\]

连续向量场的 Brouwer 球边界论证给球内零点：若无零点，则将每个点沿 `−G/||G||` 映到该球面，Brouwer 固定点与严格外向性矛盾。故每个完整输入至少有一个输出。任意完整输出满足 `x−y=λF(y)`，于是

\[
\|y-p\|^2+\|x-y\|^2\le\|x-p\|^2,
\quad \forall p\in S.
\tag{VO4}
\]

纤维闭且由 VO4 有界，故紧；`x=p` 强制 `y=p`。全部轨道有界且步平方可和，故步趋零；由 `F(x^{k+1})=(x^k−x^{k+1})/λ` 与连续性，每个聚点属于 S。选一个聚点 p，VO4 使到 p 的距离非增，其子列趋零，故整列趋 p。这里所有输出逐一进入同一个推导，没有偷选一个好分支。

### 真线性 EB 追加后的有限长度

若在全部实际输出有 `d(y,S)≤C r_F(y)`，VO4 对 `p∈P_S(x)` 给

\[
d_+^2+s^2\le d^2,\quad d_+\le(C/\lambda)s,
\quad d_+\le\kappa d,
\quad\kappa=\frac C{\sqrt{C^2+\lambda^2}}<1.
\tag{VO5}
\]

因此 `s≤d`，总长 `≤d_0/(1−κ)`。局部版本另外保留全纤维 coverage、真 EB 评价窗 `R/λ≤bar t` 与严格预算 `d_0/(1−κ)<dist(x^0,R^n\U)`，用有限前缀先证明留域。VO5 是 [C250](../../canonical/physical_rleb_gppa.md#prg-energy) 的 `v=Id, a=ω=Id, h(t,q)=q, ρ(q)=q, g(q)=q/C` 特例；直接 C249 的粗 `ψ(K(t)/λ)` 门则会要求 `C/λ<1`。故“普通伪单调 + 真线性 EB”不是新收敛机制，但保留能量比先丢弃法向能量项更有效。

## 3. 伪单调不保证单值；也不保证有限长度

### 同一个单点零集，完整近端可多值且所有分支仍收敛

取全域光滑单值 `F(y)=y(2+sin y)`、`λ=1`。其符号与 y 相同，除零外不消失。标量符号直接核 VO2：`y>x` 的触发要求 `F(x)≥0`，从而 `F(y)≥0`；`y<x` 的触发要求 `F(x)≤0`，从而 `F(y)≤0`。`S={0}`。

`g(y)=y+F(y)=y(3+sin y)` 连续、两端趋 `±∞`，故 full coverage。输入 `x=3π` 的完整纤维至少包含 `π` 与 `3π/2`，因为二者 g 值都恰为 `3π`。所有同符号根满足 `|x|/4≤|y|≤|x|/2`；全部轨道绝对值几何收缩，标量总长恰 `|x^0|`，zero 吸收，真残差 `r_F(y)≥|y|`。任一 full-graph 零处消失的全对反射模都会因同输入两输出碰撞失败；同一完整算法却已有锚定证书。此例增加非空零集，避免复抄仓库 `F=2+sin y` 的空零集例。

### 全域单值近端、所有点趋零，物理长度仍为无穷

在 `R^2` 令 `K(x_1,x_2)=(-x_2,x_1)`，取

\[
F(x)=\|x\|^2Kx,\qquad S=\{0\},\qquad \lambda>0.
\tag{VO6}
\]

它伪单调：若 x、y 非零，VO2 两个内积分别是同一 `\langle Kx,y\rangle` 乘正数 `||x||²`、`||y||²`；某点为零时后件仍为零。它一般不单调：x=(1,0)、y=(0,−2) 给 `<F(y)−F(x),y−x>=−6`。

完整近端式 `x=y+λ||y||²Ky` 的半径满足

\[
\|x\|^2=r^2+\lambda^2r^6.
\tag{VO7}
\]

右侧在 `r≥0` 严格增、满覆盖；每个半径对应可逆旋转伸缩矩阵，故完整 J 全域唯一，`J(0)={0}`。非零轨道的半径 `r_k↓0`，真残差恰 `r_F(x)=||x||³`。置 `v_k=r_k^{−4}`，VO7 给

\[
v_k=\frac{v_{k+1}}{(1+\lambda^2/v_{k+1})^2},\qquad
v_{k+1}-v_k\longrightarrow2\lambda^2.
\]

所以 `r_k~(2λ²k)^{−1/4}`，而实际物理步长

\[
\|x^{k+1}-x^k\|=\lambda r_{k+1}^3\asymp k^{-3/4}.
\tag{VO8}
\]

长度发散。零集与 `F=I` 完全相同，且 coverage、single fiber、zeroabsorb 均保真；区别来自方向与真残差增长。VO6 有全零锚 Minty 与真 `1/3` 阶 EB，仍不足以支持 C249 的有限长度结论。这是“点收敛研究更宽”与“同一个有限长度合同更宽”的明确分界。

## 4. 拟单调与循环次单调的最短失败证据

**VO-QUASI。** 取全域光滑 `F(y)=y²/(1+y²)`、`λ=3`、`S={0}`。F 非负，故 quasi；pseudo 失败于 `x=0,y<0`。`g(y)=y+3F(y)` 连续、两端趋 `±∞`，full coverage 成立。完整零输入纤维恰为

\[
J(0)=\left\{0,\frac{-3-\sqrt5}{2},\frac{-3+\sqrt5}{2}\right\}.
\tag{VO9}
\]

从零输入选任一负根后，每个后续完整输出均严格 `y<x<0`：`g(y)=x<0` 排除 y≥0，且 `x−y=3F(y)>0`。若无限轨道有有限极限 ℓ，则连续近端式给 `F(ℓ)=0`，与始终 `x^k≤x^1<0` 矛盾，故每条该负轨道趋 `−∞`。full coverage 没有解决全纤维零吸收；同一个 `S={0}` 的拓扑也没有控制轨道。此例在整个实线修补旧平方图的 coverage 缺陷，仍显示 quasi 的算法缺口。

**VO-CYCLIC。** D–G 的 cyclic submonotonicity 要求：对每条闭多边形与 `ε>0` 存在 `δ>0`，其所有 δ-细分及完整图值满足

\[
\sum_i\langle v_i,x_{i+1}-x_i\rangle
\le\varepsilon\sum_i\|x_{i+1}-x_i\|.
\tag{VO10}
\]

δ-细分还携带管内、短边、顺序及每段方向逼近条件（Defs 10–11）；它是小网格循环的近可积性条件，不能读成固定 proximal λ 的步界。

例如 `F(x)=−x=∇(−x²/2)`，任意闭细分有

\[
\sum_i(-x_i)(x_{i+1}-x_i)
=\frac12\sum_i|x_{i+1}-x_i|^2
\le\frac\delta2\sum_i|x_{i+1}-x_i|.
\]

取 `δ≤2ε` 即 VO10。凹二次 f 是 C¹、locally Lipschitz、approximately convex（局部二次误差可吸入一阶 ε 误差），由该一手 T13，其 Clarke 次梯度甚至是 maximal cyclically submonotone。固定 `λ=1/2` 的完整 PPA 为 `J(x)=2x`：full coverage、single fiber、S={0}、zeroabsorb 均成立，而任意非零轨道发散。`λ=1` 还出现 `J(0)=R` 及其他输入空纤维。循环的 maximality 因而不能供应近端 coverage 或稳定参数。

D–G 的价值是辨认“哪些图可由 lower-C¹/近似凸势生成”，适合势函数与积分问题。若进一步用能量/KL/minimum selection，必须证明原完整 stationary 关系与该 argmin 关系相等；不能据有势函数就删掉其他驻点。它不是 VO1 的普适收敛入口。

## 5. 弱 Minty 是真正的另一路，但必须保全零锚与步长

标量 convention 固定为

\[
\langle v,y-p\rangle\ge\rho\|v\|^2,
\quad(y,v)\in\operatorname{gph}F,\quad p\in S.
\tag{VO11}
\]

negative comonotonicity 的两点式 `<y−z,v−w>≥ρ||v−w||²` 代入 `(z,w)=(p,0)` 供应 VO11；逆向不由此成立。VI 伪单调供应其 `ρ=0` 版本。

在 Evens 等 v2 中取 `P=λ^{−1}I`、未松弛外步 `λ_k=1`，对应本页同一完整普通 PPA。其 `α_k=1+ρ/λ`，所以有正下降余量的门是

\[
\sigma:=1+2\rho/\lambda>0.
\tag{VO12}
\]

对于 `ρ<0` 即 `λ>−2ρ`。不能只援用 Assumption I.a4 的较弱 `λ>−ρ`：后者还须配合合法松弛。极大两点 comonotonicity 可能供应 full resolvent range；仅有 VO11，source 特意把 full domain 另列为 a2。

### 保留能量的真 EB 路线

本页直接扩展 VO5：对每个合法完整输入 x、每个完整输出 y，在同一个最近原零锚 p（可依输出变化）满足 VO11，且 full coverage、`d(y,S)≤C r_F(y)`，则

\[
d_+^2+\sigma s^2\le d^2,
\qquad r_F(y)\le s/\lambda,
\qquad d_+\le\frac{C}{\sqrt{C^2+\lambda^2+2\rho\lambda}}d,
\qquad s\le d/\sqrt\sigma.
\tag{VO13}
\]

证明只展开 `x−p=(y−p)+(x−y)`，并用近端图值 `v=(x−y)/λ`；真 EB 始终作用于 `inf_F`。记上式因子为 κ，则全部选择总长 `≤d_0/[√σ(1−κ)]`。局部使用先核 `R/(λ√σ)≤bar t`、全部实际输出的 EB 和完整纤维 coverage，再要求同一严格留域预算。零输入直接由 VO13 强制 y=x。这条同最近锚的逐输出推导不要求一般 J 单值，也不依赖已存在轨道的先验有界性。

若改用**全零锚且全球 full coverage** 的 VO11，VO13 的基础能量不等式本身强迫 S 凸：取任意 p,q∈S、`m=(1−t)p+tq` 和任一 y∈J(m)，把到 p、q 的两个能量式分别乘 `1−t,t` 相加，方差恒等式消去常数，得到

\[
\|y-m\|^2+\sigma\|m-y\|^2\le0.
\]

故 y=m、m∈S。有限维 outer semicontinuity、full coverage、全零锚及 σ>0 也直接给 VO4 的 Fejér/聚点证明。来源 T2.13 的凸性前提仍须如实列出，不能靠本页局部逐输出证明删除来源条款；全球情形的凸性可单独证明。只比较实际最近锚的局部门则没有这条对两个任意零点同时比较的强度。

### 仅一个 Minty 锚不保完整原零集的吸收

取 `F(y)=y(y−1)²`、`S={0,1}`、`λ=16/3`。完整 `g(y)=y+λF(y)` 为连续三次函数、两端趋 `±∞`，故 full coverage。对锚0，`F(y)y=y²(y−1)²≥0`，是全图 `ρ=0` weak Minty；`J(0)={0}`。但完整纤维恰有

\[
J(1)=\{1,1/4,3/4\},
\quad g(y)-1=(y-1)[1+\lambda y(y-1)].
\tag{VO14}
\]

原零点1可离开。并且 `y→1−` 时该锚的比例为

\[
\frac{F(y)(y-1)}{F(y)^2}=\frac1{y(y-1)}\to-\infty,
\]

故1没有任何有限标量 weak Minty 系数。source 的 `S*={0}` 和原 `S={0,1}` 真实不同；全零锚门不可省。改变目标为 `{0}` 或停止政策为“检测任一零点便停”会改变合同，必须明说。

## 6. 对“是否有更本质的非线性化”的范围裁决

| 路线 | 研究目的 | 完整 PPA 的可认证性 | 对当前 C249/有限长度目标的判断 |
| --- | --- | --- | --- |
| VI 伪单调 | 保符号传播与 Minty 解；允许非单调 F | 连续全域单值 + 非空全零集给任意 λ 的 full coverage/零吸收/全部点收敛；多值版本须重写量词 | 有效老路线；真线性 EB 后是 C250 能量特例。VO6 排除单凭它得到有限长度。 |
| VI 拟单调 | 更弱符号序、VI/MVI 存在及外投影求解 | 零锚前件不触发；必须追加 MVI/算法条件。VO9 保 full coverage 后仍发散 | 不是普通完整 PPA 的无条件宽推广；Lei–He 历史切平面外步改变算法。 |
| cyclic submonotonicity | 次梯度积分、lower-C¹/近似凸势表示 | 细分循环误差不控制固定 λ 的纤维或位移；VO-CYCLIC 连 maximal 也发散 | 有另一种结构意义；需独立能量、真 EB、全驻点桥与留域，不能宣布比 LT→RL 更好。 |
| 全零锚 weak Minty/negative comonotone | 以残差二次预算容纳非单调方向，给 Fejér/松弛PPA | σ>0 + full coverage + 原图闭/osc；追加真 EB 得 VO13 的全部物理长度。只一个锚不保全零吸收 | 真实替代证书入口；某些参数上直接能量更短更锋利。全零锚全球路线限制凸零集，有限二次预算排除某些非calm RLEB例，不能全包含 C249。 |
| C249 的允许输出/最近物理零锚/一般模 | 分开距离压缩、位移可和、物理提升与原完整残差 | 每一实际完整输出单独认证 G1–G5 及预算；选择可以多值 | 其“本质”在固定算法的定量接口。是否容易从原始模型认证及是否有旧能量回收，要逐模型比较。 |

与 C249 不包含的方向有现成完整证据：[C256 的 ACH12](../../canonical/amplitude_circle_hamilton.md#ach-sharp) 在每个固定圆零点排除任意有限 weak Minty 矩阵，同时认证同一完整 J 的 C02-v3/C249 接口；其完整零集包含中心，认证域和原零集均须原样携带。[C276](../../topics/inexact_ppa/sharp_precision_frontier.md#isp-object) 的平移模型亦已有明确二次弱 Minty 排除。这里不重抄其证明，也不据这些模型排除一般非二次 Lyapunov 方法；C256 的机械能正面回收已经登记。

对于普通完整 PPA，最值得继续研究的是**固定图/固定 λ/全输出的非线性方向预算**，以及它能否在同一真 EB 下直接推出距离及长度；若只有某种序关系，不能借名称中“更广义”取得这些量化接口。VO13 示范了一条更有效的既有能量入口，VO8/VO9/VO-CYCLIC 给出不能随名称移植的实际失败。没有证据支持“其它方向已经全面优于 LT→RL”，也没有证据支持“LT→RL 是唯一可能的非线性化”。

## 7. 计算证据与新意边界

独占复算文件：[order_verify.py](../../code/submonotonicity_routes/order_verify.py)。运行：

```
python3 research/code/submonotonicity_routes/order_verify.py > research/code/submonotonicity_routes/order_verify_results.json
```

Python 标准库，确定性，无 seed、无外部依赖，65 次二分。运行通过：VO9 零输入三个根精确回代；负支1000步约 `−3002.38247`，最大包含缺陷 `4.55e−13`；伪单调多纤维的两根精确回代；VO6 非单调见证以整数精确算出 `−6`，其200000步 `r_k(2k)^(1/4)=0.99999945`、`v_{k+1}−v_k≈1.99999250`、部分长度46.358；VO14 三根与循环恒等式回代通过。浮点轨道只支持指定实例，发散、无限长度与全部纤维结论由正文解析论证承担。

本轮新取得的是短且保真的比较证据、逐输出的能量桥、全零锚的凸性门及阅读分母；未注册新的全局 Claim，不把诊断例包装成自然高价值应用。伪单调/Fejér/weak Minty 的机制均有已读先行；例子的确切公开优先未穷尽。Langenberg 2010、完整 pseudomonotone 多值文献及不同 cyclic 原始版本继续标未读全。任何“第一”“全面包含”“更本质”的公开结论还需要另立精确目标与一手全文审查。
