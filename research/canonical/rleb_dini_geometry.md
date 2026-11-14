# PPA 的紧致 Dini 反例与可定义有限长度

核查范围为 `main@911cb5b4da26301db1a7d96725783dbb85a7972f` 的规范索引、C09/C10、C214/C219、解选择一手接口、当前 RLEB 正文及相关历史稿。C10 的普通 PPA 在非紧直线零集附近有精确对数发散，切向坐标趋无穷。C214/C219 是 GPPA 逆核后的物理长度反例，所指轨道仍收敛于一点。历史 `ppa_system_team/02_convergence_topology.md` §3.2 已有紧致状态上的旋转构思，但法向递推为 \(r\mapsto r/(1+r)\)，未建立同一 PPA 的真误差界和直接兼容。本文的新增范围是**给定任意非 Dini 凹模、紧目标、全局单值连续算子及唯一完整预解式、精确几何距离收缩和逐输出真误差界兼容同时成立**。未核全球优先性。

<a id="rdg-winding"></a>

## 1. 任意非 Dini 凹模的有界绕行

设 \(r_0>0\)，\(\omega:[0,r_0]\to[0,\infty)\) 连续、非减、凹，\(\omega(0)=0\)，且 \(\int_0^{r_0}\omega(t)\,dt/t=\infty\)。给定任意 \(\lambda>0\) 和 \(0<q<1\)，存在全局连续单值 \(F:\mathbb R^2\to\mathbb R^2\)，其完整预解式 \(J_{\lambda F}\) 为全局同胚，零集为 \(\{0\}\cup S\)，其中 \(S=\mathbb S^1\)。在一个统一小环带 \(U_R=\{x:d(x,S)\le R\}\) 上，完整预解式具有给定模 \(\omega\) 的最近零锚 RL、所有实际输出的真残差误差界、直接兼容及窗口，且 \(d(J_{\lambda F}x,S)=q\,d(x,S)\)。任意 \(x^0\in U_R\setminus S\) 的唯一轨道有界、无限长，聚点集正好为 \(S\)。因而以几何集合距离衰减和有界性取代 Dini 项，不能推出点收敛。这里的目标 \(S\) 是局部完整零集，对起点所在环带而言也是最近零点的正确集合。

**构造及窗口。** 凹性给 \(\omega(t)/t\) 随 \(t\downarrow0\) 单调，并趋于 \(+\infty\)，否则 Dini 积分有限。另外，对任意 \(M>0\)，可取 \(0<e<r_0\) 使 \(\omega(e)>2Me\)，再取 \(0<d<e\) 使 \(\omega(d)\le\omega(e)/2\)。任意在 \([0,d]\) 中取端点的非退化割线斜率至少为 \((\omega(e)-\omega(d))/(e-d)>M\)，由此得到靠近零的统一斜率下界且无需可微性。

固定 \(1<c<1/q\)，置 \(\kappa=qc\)。在小区间 \([0,\varepsilon]\) 上令
\[
 m(t)=\tfrac12(\omega(t)-(1+2q)t),\qquad
 H(t)=m(t)-(1+q)t,\qquad B(t)=\tfrac12(t+\omega(t))=m(t)+(1+q)t.
\]
用上述割线下界选 \(\varepsilon<\min(r_0,1/2)\)，使 \(0\le m\le1\)，\(m\) 的全部割线斜率严格大于 \(\max\{1+q,(1+q)(c+1)/(c-1)\}\)。于是 \(H\) 连续、严格增加、\(H(0)=0\)，且凡 \(0\le t\le\varepsilon/c\)，均有 \(H(ct)\ge B(t)\)。取 \(0<R\le\varepsilon/c\)，再要求 \(R<1/2\)，残差窗口 \(\bar t=H(\varepsilon)/\lambda\)，规范误差模定义为 \(\psi(s)=qH^{-1}(\lambda s)\)，\(0\le s\le\bar t\)。这个 \(\psi\) 连续严格增加且在零为零。显然 \(B(R)/\lambda\le\bar t\) 且 \(\psi(B(t)/\lambda)\le\kappa t\) 对所有 \(0\le t\le R\) 成立。

在 \([\varepsilon,\infty)\) 将 \(m\) 常数延拓，仍用同一字母。对 \(m\in[0,1]\)，令 \(R_m\) 为逆时针旋转，\(\cos\theta=1-m^2/2\)、\(\sin\theta=m\sqrt{1-m^2/4}\)，故每个单位向量 \(p\) 满足 \(\|R_m p-p\|=m\)。定义
\[
 h(r)=qr+(1-q)\min(2r,1),\qquad J(0)=0,\qquad J(rp)=h(r)R_{m(|r-1|)}p\quad(r>0,\ \|p\|=1).
\]
\(h\) 严格增加并把 \([0,\infty)\) 映满自身。对非零输出先以 \(h^{-1}\) 反演径向坐标，再反转对应旋转，即得连续逆。零点处 \(\|J(x)\|=h(\|x\|)\) 同时保证 \(J,J^{-1}\) 在零连续。取 \(F=(J^{-1}-I)/\lambda\)。于是 \(I+\lambda F=J^{-1}\)，完整预解式恰为 \(J\)，且 \(h(r)=r\) 的仅有半径是 0 和 1，所有半径 1 的点固定，故 \(\operatorname{zer}F=\{0\}\cup S\)。本文覆盖可用 \(U=V=V'=W=\mathbb R^2\) 及以上 \(R\) 表示，所有窗内输入输出均走同一完整单值图。

**零锚及真残差。** 对 \(x=rp\in U_R\)，最邻近 \(S\) 的点恰为 \(p\)，令 \(t=|r-1|\)，\(y=J(x)\)。因 \(r>1/2\)，\(h(r)=1+q(r-1)\)，从而 \(d(y,S)=qt\)。记 \(s=\|x-y\|\)。比较 \(x-y\) 与 \(p-R_{m(t)}p\) 得
\[
  H(t)=m(t)-(1+q)t\le s\le m(t)+(1+q)t=B(t).
\]
另有 \(\|2y-x-p\|\le 2m(t)+(1+2q)t=\omega(t)\)，即稿件逐输出最近零锚 RL。因 \(F\) 单值，\(r_F(y)=s/\lambda\)。因此在全部实际输出上 \(d(y,S)=qt\le qH^{-1}(s)=\psi(r_F(y))\)。\(S\) 在环带内固定，且 \(d(Jx,S)=q\,d(x,S)\) 使整个环带不变。

**无点极限。** 若 \(t_0>0\)，则 \(t_k=q^k t_0\)。升到实轴的角变量每步加 \(\theta_k=2\arcsin(m(t_k)/2)>0\)，且 \(\theta_k\to0\)。由于 \(\omega(t)/t\to\infty\)，有 \(H(t)\sim m(t)\sim\omega(t)/2\)。对任意单调非减 \(\omega\)，在区间 \([q^{j+1}t_0,q^jt_0]\) 的 Dini 积分夹在 \(\log(1/q)\) 乘两端点函数值之间，故 \(\sum_k\omega(t_k)=\infty\)。于是 \(\sum_k\theta_k=\infty\)，\(\sum_k s_k\ge\sum_kH(t_k)=\infty\)。对任意实角 \(\alpha\)，取累计角首次超过 \(\alpha+2\pi n\) 的指标，超出量被趋零的单次角步控制。半径趋 1，故圆周每个点均为聚点。聚点不得在圆外，因为径向距离趋零。

**范围。** 上述是逐输出零锚的相同给定模，未声称同一 \(\omega\) 有任意图点对 RL。若 \(\omega\) 在某个结构内可定义，上述 \(J,F,H,\psi\) 均可在该结构内定义，构造的角旋转只需实代数公式，证明中用的角提升不属于映射定义。例如 \(\omega(t)=[\log(e/t)]^{-a}\)、\(0<a\le1\)，在足够小起始窗内凹，故给出实指数域 \(\mathbb R_{\exp}\) 可定义的实例。由于直接兼容使用的模是所给 \(\omega\)，此结果是模型类上省去 Dini 的反例，对任意单独轨道或任意非凹模的必要性不作断言。

**可另选模的全对版本。** 若要攻击 C09 的全对版本，可改旋转剖面以供同一全对模通过直接兼容。局部取 \(b(t)=\omega(t)/2\)、\(\theta(t)=2\arctan b(t)\)、\(m(t)=2b(t)/\sqrt{1+b(t)^2}\)，再将 \(m\) 常数延拓，保留径向映射 \(h\)。构造和反演仍用前段矩阵 \(R_m\) 的代数式。\(\theta\) 凹增且局部取值在 \([0,\pi/3]\)。对输入 \(x=rp,x'=r'p'\)，限制 \(r,r'\in(1/2,3/2)\)、\(t=|r-1|,t'=|r'-1|\) 及 \(\delta=\|x-x'\|\) 均在剖面窗，交换两输入使 \(t\ge t'\)。由凹性、\(\theta(0)=0\) 得 \(0\le\theta(t)-\theta(t')\le\theta(|t-t'|)\le\theta(\delta)\)，所以 \(\|R_{m(t)}-R_{m(t')}\|_{\mathrm{op}}\le m(\delta)\)。还得到 \(t'\|R_{m(t)}-R_{m(t')}\|_{\mathrm{op}}\le \delta\)：若 \(t'<\delta\) 用 \(m(\delta)\le1\)，否则用凹性给的 \(\theta(t)-\theta(t')\le \theta(t')\delta/t'\) 并取窗使 \(\theta\le1\)。再用 \(\|p-p'\|\le4\delta\)、\(|h(r)-h(r')|\le q\delta\)、\(h(r')\le 1+qt'\)，把 \(J(x)-J(x')\) 分为径向差、方向差和旋转差，得到 \(\|J(x)-J(x')\|\le m(\delta)+(6+2q)\delta\)。因此 \(\widetilde\omega(\delta)=2m(\delta)+(13+4q)\delta\) 是全对反射模。此处选择了与给定 \(\omega\) 渐近相同的新模，未仅用同阶性传递兼容。

实际步长仍满足 \(s\ge H(t)=m(t)-(1+q)t\)。\(m\) 的割线斜率仍在零附近任意大，因为它是 \(b\) 和一个在零导数为 2 的光滑增函数的复合。固定 \(1<c<1/q\)，缩小剖面窗 \(\varepsilon\) 使 \(H\) 严增且 \(H(ct)\ge \widetilde B(t)=m(t)+(7+2q)t\) 对 \(0\le t\le \varepsilon/c\) 成立。再取覆盖输入区 \(U=\{x:d(x,S)<\varepsilon\}\) 和同一完整图在 \(U\) 输入的图块、工作尺度 \(R\le \varepsilon/c\)。按前式设 \(\psi(s)=qH^{-1}(\lambda s)\)、\(\bar t=H(\varepsilon)/\lambda\)，则同时满足 \(\widetilde B(R)/\lambda\le\bar t\)、\(\psi(\widetilde B(t)/\lambda)\le qc t\) 和真残差误差界。任意图块输入对若其对距 \(\le R\) 都可用 \(\widetilde\omega\)。由于 \(m(t)\sim\omega(t)\)，同一绕行和 Dini 发散证明成立。若 \(\omega\) 可定义，矩阵依旧仅用实代数函数，故这个全对实例亦可定义。


<a id="rdg-fullpair-v2"></a>
### 1A. 同一给定模的全对升级（C287-v2）

上一段的全对估计得到的是与给定模同阶的 \(\widetilde\omega\)，而不是同一个 \(\omega\)。下面把线性余量从旋转剖面中预先扣除，从而闭合同模版本。固定一个安全常数
\[
K=20.
\]
由凹性、\(\omega(0)=0\) 及非 Dini 条件，\(\omega(t)/t\to\infty\)；缩小 \(\varepsilon\) 后可令 \(\omega\) 在 \([0,\varepsilon]\) 的所有非退化割线斜率都大于 \(K\)，并且
\[
\Omega(t):=\omega(t)-Kt\ge0,
\qquad \Omega(t)/t\to\infty .
\]
\(\Omega\) 仍连续、非减、凹，且从 \(\omega\) 只减去一个可积的线性项，所以 \(\int_0^\varepsilon\Omega(t)\,dt/t=\infty\)。令
\[
b(t)=\frac{\Omega(t)}4,\qquad
\theta(t)=2\arctan b(t),\qquad
m(t)=\frac{2b(t)}{\sqrt{1+b(t)^2}}.
\]
再缩小 \(\varepsilon\) 使 \(m\le1\) 且 \(\theta\le1\)。函数 \(b,\theta,m\) 都连续、非减、凹；这里 \(b\mapsto2\arctan b\) 与 \(b\mapsto2b/\sqrt{1+b^2}\) 在所用区间上递增且凹。取 \(R_m(t)\) 为角度 \(\theta(t)\) 的平面旋转，则
\[
\|R_m(t)-I\|_{\mathrm{op}}=m(t),
\qquad
2m(t)=\frac{\Omega(t)}{\sqrt{1+b(t)^2}}\le\Omega(t).
\]

保留本节前段的径向函数 \(h\) 和完整映射
\[
J(rp)=h(r)R_m(|r-1|)p,
\qquad F=(J^{-1}-I)/\lambda .
\]
它们的全局同胚、零集、精确距离比、真残差和绕行证明不变。只需重做同窗的全对差分。若 \(x=rp,x'=r'p'\) 位于 \(1/2<r,r'<3/2\)，令 \(\delta=\|x-x'\|\le R\)，交换两点使 \(r\ge r'\)，并记 \(t=|r-1|,t'=|r'-1|\)。则
\[
|r-r'|\le\delta,\quad |t-t'|\le\delta,\quad
\|p-p'\|\le4\delta,\quad |h(r)-h(r')|\le q\delta,
\quad h(r')\le1+qt'.
\]
凹性给出
\[
\|R_m(t)-R_m(t')\|_{\rm op}\le m(\delta).
\]
若 \(t'<\delta\)，则 \(t'\|R_m(t)-R_m(t')\|_{\rm op}\le\delta\)（因 \(m\le1\)）；若 \(t'\ge\delta\)，由凹函数 \(\theta\) 的割线斜率和 \(\theta\le1\) 得同一不等式。因此
\[
\begin{aligned}
\|Jx-Jx'\|
&\le |h(r)-h(r')|+h(r')\|p-p'\|
       +h(r')\|R_m(t)-R_m(t')\|_{\rm op}\\
&\le m(\delta)+(4+4q)\delta .
\end{aligned}
\]
因此反射映射 \(C=2J-I\) 满足
\[
\|Cx-Cx'\|
\le2m(\delta)+(9+8q)\delta
\le2m(\delta)+K\delta
\le\Omega(\delta)+K\delta
=\omega(\delta).
\]
此外，最近零锚估计仍为 \(\|2Jx-x-p\|\le 2m(t)+(1+2q)t\le\Omega(t)+(1+2q)t\le\omega(t)\)。因此，**同一个给定的 \(\omega\)** 在该环带完整图的同窗输入对上给出全对 RL 模；这只是对输入距离不超过 \(R\) 的局部图块结论，不是环带外的全局断言。

兼容性与绕行估计沿用一个明确区分的内部模。定义
\[
\widehat\omega(t)=2m(t)+(13+4q)t,
\qquad
\widehat B(t)=\frac{t+\widehat\omega(t)}2=m(t)+(7+2q)t .
\]
由于 \(K=20\ge13+4q\)，上面的全对估计给出 \(\widehat\omega\le\omega\)；因此同一个给定 \(\omega\) 仍是全对 RL 和最近零锚 RL 的合法上界，但**直接兼容和真残差证明使用的是较小的 \(\widehat\omega\)**。由凹性和 \(m(t)/t\to\infty\)，左导数 \(m'_{-}(t)\to\infty\)；固定 \(1<c<1/q\)，再缩小 \(\varepsilon\) 使 \([0,c\varepsilon]\) 上每条割线斜率都大于
\[
\frac{(1+q)c+7+2q}{c-1}.
\]
于是 \(H(t)=m(t)-(1+q)t\) 严格增加，并有 \(H(ct)\ge\widehat B(t)\) 对 \(0\le t\le\varepsilon/c\)。在 \([0,H(\varepsilon)/\lambda]\) 上置 \(\psi(s)=qH^{-1}(\lambda s)\)，取 \(R\le\varepsilon/c\) 并沿用上文 coverage 与严格预算，即得 \(\psi(\widehat B(t)/\lambda)\le qc\,t<t\)，以及真实残差兼容。又因 \(m(t)\sim\Omega(t)/2\sim\omega(t)/2\)，有 \(\sum_km(q^kt_0)=\infty\)；每条非零轨道仍无限长且聚点集为整圆。

新增结论的精确范围是：每个连续、非减、凹且非 Dini 的 \(\omega\) 都有一个共同小窗，使该紧圆构造满足精确集合距离收缩，并在同一给定 \(\omega\) 下满足局部全对 RL；同时存在显式的 \(\widehat\omega\le\omega\) 使最近零锚、真残差和直接兼容形成完整 RLEB 反例。这里不把 \(\widehat\omega\) 偷换成 \(\omega\) 的兼容模，不声称每个非 Dini 模都强迫发散，也不声称该关系单调、来自次微分或代表自然凸优化模型。

<a id="rdg-tame"></a>

## 2. 多项式有界结构中的自动幂次步界

令 \(X=\mathbb R^n\)，\(S\subset X\) 非空闭，\(U\subset X\) 开，\(\bar x\in S\cap U\)，\(R>0\)，\(U_R=\{x\in U:d(x,S)\le R\}\)。假设 \(S,U\) 与允许的实际转移图 \(\mathcal A\subset U_R\times X\) 在同一多项式有界的 o-minimal 实域扩张中可定义，允许实参数。\(\mathcal A_x\) 对每个 \(x\in U_R\) 非空。对所有 \((x,y)\in\mathcal A\)，假设存在固定 \(0<\kappa<1\) 和统一有限函数 \(B:[0,R]\to[0,\infty)\)，满足
\[
  d(y,S)\le\kappa d(x,S),\qquad \|x-y\|\le B(d(x,S)),\qquad B(0)=0,\quad B(t)\to0.
\]
\(B\) 无需可定义、Dini 或幂次。实际转移可为普通 PPA 的完整预解式或指定图块，也可为任意其他满足同一两估计的关系。则存在 \(C,\alpha,r>0\)（\(r\le R\)，可取 \(0<\alpha\le1\)），任意 \((x,y)\in\mathcal A\) 且 \(d(x,S)\le r\) 都满足 \(\|x-y\|\le C d(x,S)^\alpha\)。对每个 \(d(x^0,S)\le r\) 且 \(C d(x^0,S)^\alpha/(1-\kappa^\alpha)<d(x^0,X\setminus U)\) 的初值，所有允许选择的轨道能无限生成、留域，收敛到 \(S\cap U\) 中一点，并有有限长度以及从第 \(k\) 步起的尾界 \(C\kappa^{\alpha k}d(x^0,S)^\alpha/(1-\kappa^\alpha)\)。这样的初值集合含 \(\bar x\) 的邻域。

**证明。** 对 \(0<t\le R\) 定义
\[
 D(t)=\sup\bigl(\{\|x-y\|:(x,y)\in\mathcal A,\ d(x,S)=t\}\cup\{0\}\bigr).
\]
有限维距离和上确界可由一阶实域量词定义，即使上确界未达到或相应纤维为空。统一上界给 \(0\le D(t)\le B(t)\to0\)。将 \(s\mapsto D(1/s)\) 在大 \(s\) 外分片延为零，得到全实轴上的可定义函数。[van den Dries–Miller, *Extending Tamm’s theorem*, §1.3 (1994)](https://www.numdam.org/item/AIF_1994__44_5_1367_0.pdf) 表明：在多项式有界 o-minimal 实域结构中，一元可定义函数在 \(+\infty\) 的芽或者最终为零，或者有非零实幂渐近主项。因此 \(D\) 近零全零或 \(D(t)=c t^\alpha+o(t^\alpha)\)，其中 \(c,\alpha>0\)，这由非负且趋零推出。适当调整常数及半径即得所称步界。每一步用覆盖构造，距离收缩给予 \(d_k\le\kappa^k d_0\)，幂次步界的初值总预算严格小于到域外的距离，逐步归纳得到留域。有限长度给 Cauchy 极限，闭 \(S\) 及严格预算给极限属于 \(S\cap U\)。若原工作域本来就是一个闭不变管，只须从该管的相应小距离层起步即可，不另需开域预算。

**与现有结果的关系。** 本库 `selection_primary_interfaces.md` §2.1 已核半代数一元增长和半代数闭图误差界。本推导的使用对象是**实际允许转移的统一位移包络**，并避免假设用户选用的松模本身可定义或可和。增长定理是已有工具，桥梁是对具体假设的推论。任意 o-minimal 结构不能替代多项式有界性，§1 的 \(\mathbb R_{\exp}\) 实例逐项满足统一趋零步界及严格几何距离收缩。也不能删去已有的严格几何收缩，把本条套到仅有慢收缩的半代数图。

<a id="rdg-index"></a>

## 3. 附带的严格区分

若 \(M\) 是紧致光滑无边界嵌入子流形，\(O_r\) 为具有最近点投影 \(P\) 的欧氏管，\(T\) 在闭管上连续、固定 \(M\) 中每一点，并将闭管映入开管，则 \(\mathrm{ind}(T,O_r)=\chi(M)\)，无须轨道有限长度或点收敛。令 \(D_s(x)=(1-s)x+sP(x)\) 为管的法向收缩。先由 \(D_s\circ T\) 把 \(T\) 同伦到 \(P\circ T\)，再由 \(P\circ T\circ D_s\) 把它同伦到 \(P\)。两段同伦在边界均没有固定点。按固定点指标交换性与紧 ENR 归一化，\(\operatorname{ind}(P,O_r)=\operatorname{ind}(\mathrm{id}_M,M)=\chi(M)\)。参见 [Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*, §2.1](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf) 的 (2.1.4)、(2.1.6)。这里的光滑管指标机制在 C231/C244/C254 已有使用。它可将稿中的 Euler 障碍与迭代极限回缩分开，§1 给出后者不存在而前者仍有意义的完整 PPA 实例。若还调用全域指数与分解，则全域连续性与全域边界无不动点仍须另给。

- 动力学近邻：[Kitchens–Misiurewicz](https://www.aimsciences.org/article/doi/10.3934/dcds.2010.27.787)研究旋转同胚的聚点集；[Absil–Mahony–Andrews](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf) §2 有光滑连续梯度流不收敛实例。这里需比较的是同一完整 PPA 的指定模、几何距离率与实际输出真残差兼容。先行检索范围未穷尽。
