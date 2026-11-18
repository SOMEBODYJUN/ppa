# 普通 PPA 的两步净位移与方向残差

## 共同对象

沿用 [正式稿 P1–P4](../../发表成果整理/RLEB/sections/theorem_spine.tex) 及 [C318](ppa_ab_necessary_bounds.md#ab-scope) 的普通 PPA。固定欧氏空间、原关系 \(F\)、固定 \(\lambda>0\)、非空闭目标 \(S\subseteq\operatorname{zer}F\)、开集 \(U\)、半径 \(R>0\) 和 \(0<\kappa<1\)。记 \(d(x)=d(x,S)\)，\(U_R=\{x\in U:d(x)\le R\}\)。对 \(x\in U_R\)，取非空 \(\mathcal J(x)\subseteq J_{\lambda F}(x)\)。完整版本取等号。设 \(\omega\) 是非减有限、在零处连续且取零的模，\(H(t)=(t+\omega(t))/2\)。条件 A、B 分别是 \(d(y)\le\kappa d(x)\) 及 \(\|x-y\|\le H(d(x))\)，逐一量化所有允许步。

旧结构包指最近零锚 P2、真残差误差界 P3、尺度兼容 \(\psi(H(t)/\lambda)\le\kappa t\)。旧完整包还包括 Dini 长度条件和 P1。下文比较始终用同一 \(\lambda,S,\mathcal J,U_R,\kappa\)；证明正向蕴含时使用原模。与外文定理的可迁移范围另见 [文献边界](#td-literature)。

<a id="td-cancellation"></a>
## 1. C319：允许相邻位移相消的两步收敛定理

在覆盖、A、B 下，假设存在一个有限非负非减函数 \(W:[0,R]\to[0,\infty)\)，满足 \(W(0)=0\)、在零处连续，而且对**每一对可拼接的允许步** \(x\to y\to z\)（量化 \(x,y\in U_R,\ y\in\mathcal J(x),\ z\in\mathcal J(y)\)，无须预设 \(z\in U\)）有
\[
 \|z-x\|\le W(d(x))-W(d(z)). \tag{T1}
\]
记 \(\Gamma(t)=\max\{W(t),H(t)+W(\kappa t)\}\)。若 \(x^0\in U_R\) 且
\[
 \Gamma(d(x^0))<\operatorname{dist}(x^0,X\setminus U),
\]
那么任意允许选择均可无限延拓，留在 \(U_R\)，并收敛到某个 \(x^\infty\in S\cap U\)。对每个 \(k\ge0\)，有
\[
 \sum_{j=0}^{\infty}\|x^{k+2j+2}-x^{k+2j}\|\le W(d(x^k)),
 \qquad
 \|x^k-x^\infty\|\le W(d(x^k)). \tag{T2}
\]

**证明。** 第一步存在，且位移至多 \(H(d(x^0))\le\Gamma(d(x^0))\)。后续只对已经存在的有限前缀分奇偶。若下一步生成 \(x^n\)，A 先给 \(d(x^n)\le\kappa^n d(x^0)\)，故 \(W(d(x^n))\) 有定义。T1 可用在末两步，因为它们的输入都已知在窗内。偶数点到 \(x^0\) 的距离不超过偶数子序列的弦长和，望远镜求和给上界 \(W(d(x^0))\)。奇数点到 \(x^1\) 同理至多 \(W(d(x^1))\)，故到 \(x^0\) 至多 \(H(d(x^0))+W(\kappa d(x^0))\)。二者均小于开窗余量，完成留域和覆盖归纳。

沿偶数子序列用 T1 求和，得到 Cauchy 性。B 和 \(d(x^k)\to0\) 给 \(\|x^{2j+1}-x^{2j}\|\to0\)，因此奇数子序列也收敛到同一点。闭性及严格留域余量把极限定位在 \(S\cap U\)。以任意 \(k\) 为起点沿同奇偶子序列求和，即得 T2。

**旧包的蕴含。** 对旧 RLEB 取 \(W=\Theta_H=\sum_{j\ge0}H(\kappa^j\cdot)\)。Dini 给有限性，非减性及零处连续性可由可和的共同上界得到。A、B 给 \(\|y-x\|\le W(d(x))-W(d(y))\)，把两步相加并用三角不等式得到 T1。此时 \(W(t)=H(t)+W(\kappa t)\)，故 \(\Gamma=\Theta_H\)，初值预算与旧稿相同。若把 Dini 固定为共同假设，任何 A+B 都推出 T1，故 T1 单独无法提供该子类上的结构性严格分离。

<a id="td-links"></a>
### 从原图验证两步相消

若 \(x-y=\lambda v\)、\(y-z=\lambda w\)，则两步左端为 \(\lambda\|v+w\|\)。这是先加位移向量，再取范数。一个可直接核对的子类是横轴目标 \(S=\mathbb R^m\times\{0\}\) 上的全域双射
\[
 T(a,b)=\bigl(a+\operatorname{sgn}(b)g(|b|),-\kappa b\bigr).
\]
其中 \(g(0)=0\)，\(g:[0,R]\to\mathbb R^m\) 在零连续且总变差有限，窗外可常值延拓。记 \(V(t)\) 为 \(g\) 在 \([0,t]\) 上的总变差。变差区间可加，故 \(V(t)-V(s)\ge\|g(t)-g(s)\|\) 对 \(0\le s\le t\)。\(V(t)\to0\) 也可直接由定义证明。对任意 \(t_j\downarrow0\)，取 \([0,R]\) 上任意有限分割，等待 \(t_j\) 小于其第一个正分割点，用 \(t_j\) 替代 0 并利用 \(g(t_j)\to g(0)\)，得 \(\operatorname{Var}_{[t_j,R]}g\uparrow\operatorname{Var}_{[0,R]}g\)。因此 \(W(t)=t+V(t)\) 满足 T1，因为两步切向增量至多 \(V(t)-V(\kappa t)\le V(t)-V(\kappa^2t)\)，法向净位移为 \(t-\kappa^2t\)。

取 \(m=1\)、\(\lambda=1\)、\(R=1\)，并取递增的
\[
 h(0)=0,\qquad h(t)=[\log(e^2/t)]^{-1/2}\quad(0<t\le1).
\]
以下比较 \(T_-(a,b)=(a+\operatorname{sgn}(b)h(|b|),-\kappa b)\) 和 \(T_+(a,b)=(a+h(|b|),-\kappa b)\)，同一 \(h\) 在 \(t>1\) 常值延拓。两者均连续双射。其完整原算子由 \(F=T^{-1}-I\) 给出，零集恰为横轴。直接重构原图，输出法向坐标为 \(b'=-\kappa b\)，图值法向坐标为 \(b-b'=(1+\kappa)b\)，切向坐标为相应的负平移。两图均满足 A 和最近零锚 P2，可统一用
\[
 \omega(t)=(1+2\kappa)t+2h(t)
\]
控制以 \((a,0)\) 为最近零锚的反射，因此满足同一个 B。每步的锚定反射范数至少 \(2h(t)\)，任何有效的最近零锚模都不满足 Dini，不能靠另选较小模恢复旧 RLEB。

- 对 \(T_-\)，取 \(W=t+h(t)\) 得 T1，故全部轨道收敛。任何 \(b_0\ne0\) 的轨道却有 \(s_k^2\ge h(\kappa^k|b_0|)^2=1/(\log(e^2/|b_0|)+k\log(1/\kappa))\)（入窗后）。步长平方和发散，因此步长和也发散。
- 对 \(T_+\)，同向切向位移不断累加，轨道切向发散，因为 \(h(\kappa^k|b_0|)\) 的和发散。它满足同一 A+B，故 A+B 不推出 T1。

C277 的 JP13 在同一逐步图上支付每个实际步长，不能覆盖 \(T_-\) 的无限长度轨道。若把两步复合当作新转移，当然可以在这个复合图上重用通常的长度论证，B 负责把偶数和奇数子序列合并。这里没有改变 PPA 的更新。

<a id="td-directional"></a>
## 2. C320：用保留方向的图值包络替换标量兼容

保留 P1、最近零锚 P2 和真残差 P3（含 \(H(R)/\lambda\le\bar t\)）。写 \(Y=\mathcal J(U_R)\)。对每个 \(t\in[0,R]\) 定义
\[
 V_t=\{(x-y)/\lambda : x\in U_R,\ d(x)\le t,\ y\in\mathcal J(x)\}.
\]
要求存在嵌套的闭、中心对称凸集 \(K_t\)（对称中心为零），使
\[
 V_t\subseteq K_t\subseteq\overline B(0,H(t)/\lambda),
 \qquad
 Y\cap F^{-1}(K_t)\subseteq\{y:d(y)\le\kappa t\}. \tag{D1}
\]
这里 \(F^{-1}(K_t)=\{y:F(y)\cap K_t\ne\varnothing\}\) 使用完整原纤维。D1 在同一个窗口把一个尺度上的所有已达图值与**所有**输出纤维交叉比较。等价的最小检验是取 \(K_t=\overline{\operatorname{conv}}(\{0\}\cup V_t\cup(-V_t))\)，因为任一可行的 \(K_t\) 都包含这个集合，且反过来该最小集在 P2 下自动嵌套并落在外球内。

旧结构包推出 D1，取 \(K_t=\overline B(0,H(t)/\lambda)\) 即可。P2 给出图值包络。若 \(y\in Y\) 的某个图值属于该球，则 \(r_F(y)\le H(t)/\lambda\) 且落在 P3 的评价窗，故 \(d(y)\le\psi(H(t)/\lambda)\le\kappa t\)；\(t=0\) 时用 \(\psi(0)=0\)。反之，D1 给 A，因为任一步 \(x\to y\) 的实际图值位于 \(K_{d(x)}\)。B 仍由 P2 得到。D1 可单独通过原图的切法分量估计验证。

**同一 Dini 基线上的两侧严格性。** 固定 \(X=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\)、\(\lambda=1\)、\(U=X\)、\(R=1\)、\(\kappa=3/4\)、\(\omega(t)=t+2\sqrt t\)、\(\psi(s)=3s/2\)、\(\bar t=2\)。以下都取完整双射 \(T=J_F\)，令 \(F=T^{-1}-I\)。两个算子都满足旧结构包在这些参数下所必然蕴含的同一线性残差常数 \(2\kappa\lambda=3/2\)。这个必要常数来自旧兼容：若 \(2\lambda r_F(y)\le R\)，在 \(t=2\lambda r_F(y)\) 使用 \(H(t)\ge t/2\)；否则用 \(d(y)\le\kappa R\)。

1. 取 \(T(a,b)=(a+\sqrt{b_+},3b/5)\)。图值为 \((-\sqrt{b_+},2b/5)\)，输出距离为图值法向绝对值的 \(3/2\) 倍。选 \(K_t\) 为 \([-\sqrt t,\sqrt t]\times[-2t/5,2t/5]\) 与 \(\overline B(0,H(t))\) 的交。图值属于此集，且只要完整图值落入 \(K_t\)，就有 \(d(y)\le3t/5\le\kappa t\)。P2 的左侧反射范数不超过 \(2\sqrt t+t/5\)。P3 由 \(d(y)=(3/2)|v_2|\le(3/2)\|v\|\) 得到。对旧整窗兼容，任意有效的最近零锚模在正高处至少 \(2\sqrt t\)，而负高输出迫使任意有效真残差模在小正数上至少 \(3s/2\)。因此旧兼容左侧至少 \((3/2)\sqrt t\)，即使重选旧模和收缩因子也无法恢复。
2. 取 \(T(a,b)=(a,q(b)b)\)，其中 \(q(b)=1/5\) 当 \(b\ge0\)，\(q(b)=3/5\) 当 \(b<0\)。完整近端满足相同的 P2、P3、A、B、Dini。正高 \(b=t\) 的图值 \((0,4t/5)\) 必在 \(K_t\)。中心对称性迫使 \((0,-4t/5)\) 也在其中；它是负高输入 \(b=-2t\) 的图值，输出距离为 \(6t/5>t\)。取 \(0<t\le1/2\)，便违反 D1。任意缩小工作半径仍可作同样检验，且任何 \(\kappa'<1\) 都无法挽救该检验。

第一例的方向识别对线性观察还有一个精确边界。设 \(L:\mathbb R^2\to\mathbb R^m\) 为固定线性映射。以 \(r_L(y)=\inf_{v\in F(y)}\|Lv\|\) 为真观察残差，考虑用 \(d(y)\le\chi(r_L(y))\)、\(\rho(d(x))\ge\|L((x-y)/\lambda)\|\) 及 \(\chi(\rho(t))\le\kappa t\) 认证 A，其中 \(\chi\) 为模。对该例，可行当且仅当 \(Le_1=0\) 且 \(Le_2\ne0\)。若 \(Le_2=0\)，负半边有零观察残差及正输出距离。若 \(Le_2\ne0\)，负半边给 \(\chi(s)\ge3s/(2\|Le_2\|)\) 于小正数。若再有 \(Le_1\ne0\)，正半边的 \(\|Lv\|\ge\|Le_1\|\sqrt t-2\|Le_2\|t/5\) 打破兼容。若恰好只保留法向，则 \(\rho(t)=2\|Le_2\|t/5\)、\(\chi(s)=3s/(2\|Le_2\|)\) 立即可用。特别地，任何可逆线性换范数都无法作出这项观察残差认证。

<a id="td-combined"></a>
## 3. 合起后的中间条件及比较边界

令 \(M\) 由最近零锚 P2、真残差 P3、方向条件 D1 和两步条件 T1 组成，覆盖、闭目标及工作窗是共同背景。旧完整 RLEB 推出 \(M\)，而 \(M\) 推出 A+B 及 §1 的点收敛。两个结构蕴含即使固定同一个 Dini 模都严格，见 §2 两例：T1 在该基线上由 A+B 自动提供，D1 的分离仍在。若基础问题只固定 Dini 而研究结构，可省去 T1。若目标是避免 Dini并允许轨道无限长度，则保留 T1。

§1 的 \(T_-\) 确实满足完整的 \(M\)。取真残差模 \(\psi(s)=\kappa s/(1+\kappa)\)。对每个 \(t\)，令 \(K_t\) 为 \([-h(t),h(t)]\times[-(1+\kappa)t,(1+\kappa)t]\) 与 \(\overline B(0,H(t))\) 的交，则 P2 给外球，图值法向恒等式给逆向包含。\(T_+\) 也满足相同方向条件，但不满足 T1。故在这一组固定、合法的非 Dini 参数上，是否发生跨步相消决定了这两个已验证子类的区别。

此 \(M\) 与 Luke–Tam 的原条件不构成包含关系。§2 第二例的原算子连续单调且全域，线性次正则及覆盖成立，可取 Luke–Tam 的零违约参数，但方向包络失败。其最大单调性也可直接看出：把任一单调相容图点 \((u,v)\) 与 \((u\pm\varepsilon w,F(u\pm\varepsilon w))\) 比较，取 \(\varepsilon\downarrow0\)，得 \(\langle w,v-F(u)\rangle=0\) 对任意 \(w\)。而 §2 第一例的反射在输入 \((a,t)\) 与 \((a,0)\) 之间有 \(2\sqrt t\) 的切向差，故任何有限的 Luke–Tam 两点线性模均失败。原始子类可用 C277 的条件逐一认证；C320 给出的是与原图方向集合有关的通用检验和任意换范数的明确边界。公开先行性未核。

<a id="td-common-contract"></a>
## 4. 同一旧结构下的三类轨道及 C317 的修复

固定 \(X=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\)、\(U=X\)、\(\lambda=1\)、\(R=e^{-8}\)、声明收缩因子 \(\kappa=3/4\)，并令 \(q=1/4\)。取 \(h(0)=0\)、\(h(t)=[\log(1/t)]^{-1/2}\) 当 \(0<t\le R\)，在窗外常值延拓。以下三个 \(T\) 均是连续双射，且完整原算子为 \(F=T^{-1}-I\)，零集恰为横轴：
\[
\begin{aligned}
 T_{\mathrm{fast}}(a,b)&=(a+h(|b|),\operatorname{sgn}(b)|b|^2),\\
 T_{\mathrm{alt}}(a,b)&=(a+\operatorname{sgn}(b)h(|b|),-qb),\\
 T_{\mathrm{drift}}(a,b)&=(a+h(|b|),-qb).
\end{aligned}
\]
第一式的法向映射是全域严格递增满射，后两式法向线性双射。三式的逆均先恢复法向输入再恢复平移。零高度点固定，非零高度切向位移非零。

三者共享旧 P1、P2、P3 和 P4 的标量兼容：
\[
 \omega(t)=(1+2q)t+2h(t),\quad H(t)=(1+q)t+h(t),\qquad
 \psi(0)=0,\quad \psi(s)=\tfrac12e^{-1/s^2}\ (0<s\le\bar t=1).
\]
由 P2 反射的切向分量绝对值为 \(2h(t)\)，法向绝对值在第一例至多 \(t\)、后两例为 \((1+2q)t\)。因此同一锚定模成立，且任一有效锚定模均至少为 \(2h(t)\)，在任意缩窗上都非 Dini。因 \(F\) 单值，\(r_F(y)=\|y-x\|\ge h(t)\)，所以 \(\psi(r_F(y))\ge t/2\ge d(y)\)。亦有 \(H(R)<1\)。为核兼容，令 \(\ell=\log(1/t)=1/h(t)^2\) 及 \(c=1+q\)，则
\[
 \frac{\psi(H(t))}{t}
 =\frac12\exp\!\left(\frac1{h(t)^2}-\frac1{(h(t)+ct)^2}\right)
 \le\frac12\exp(2ct\ell^{3/2})
 \le\frac12\exp(2c e^{-8}8^{3/2})<\frac34 .
\]
第一个不等号来自对 \(a\mapsto a^{-2}\) 积分；第二个来自 \(e^{-\ell}\ell^{3/2}\) 在 \(\ell\ge8\) 递减。零尺度由各模零值处理。

三者的结论不同。

- 快速法向收缩令 \(h(t^2)=h(t)/\sqrt2\)。取 \(W_1(t)=t+h(t)/(1-1/\sqrt2)\)，则 \(W_1(t)-W_1(t^2)=t-t^2+h(t)\ge\|T_{\mathrm{fast}}x-x\|\)。故旧 C317 的**一步**势条件成立，全部窗内轨道有限长。这是相对于最近零锚旧 Dini 门的严格例，无须借助全对模。有限长度的机制是 [C309](ppa_nonlinear_gauge_and_coupled_obstruction.md#c309-theorem) 中实际非线性收缩的采样可和。
- 交替位移给 T1，全部轨道收敛，但非零高度的每条轨道连步长平方和都发散。
- 同向位移使点列发散。后两例给出的输入距离、输出距离、步长范数和锚定反射范数逐点一致，输出上的完整真残差也一致，因为其大小只依赖输出高度。这些单步标量数据不足以区分两例，区别在于可拼接转移的切向方向。

[C317 原窄 bump](../candidates/rleb_telescoping_strict_candidate.md) 仅使**全对** RL 模非 Dini，与最近零锚版本相比不构成严格例。这里 \(T_{\mathrm{fast}}\) 的切向锚定下界修复了该漏洞。三图均保留真正的旧 P4 兼容，故这个对照也表明，只有删除 Dini、没有补入实际收缩或跨步方向信息，不能从旧结构统一推出点收敛。独立代理提出共同结构对照；上文取幂 \(1/2\) 使同一对照还能区分平方耗散。

### 任意给定严格递增模的有限长度实现

固定任意连续严格递增 \(h:[0,R]\to[0,\infty)\) 且 \(h(0)=0\)，任取 \(c,\eta\in(0,1)\)。令
\[
 H(t)=t+h(t),\quad \omega(t)=t+2h(t),\quad \psi(s)=cH^{-1}(s)\ (0\le s\le H(R)),
 \quad \phi(t)=\min\{\psi(h(t)),h^{-1}(\eta h(t))\}.
\]
两支均连续严格递增且零处为零，故 \(\phi\) 也具有这些性质，且 \(\phi(t)\le ct\)。在窗外将 \(\phi\) 用正斜率线性延拓、将 \(h\) 常值延拓。取 \(\lambda=1\) 的完整双射 \(T(a,b)=(a+h(|b|),\operatorname{sgn}(b)\phi(|b|))\)，再令 \(F=T^{-1}-I\)。其零集恰为横轴，完整真残差为步长。锚定反射的范数在 \(2h(t)\) 与 \(t+2h(t)\) 之间，故 P2 成立，任一可用锚定模至少为 \(2h(t)\)。因 \(r_F(y)\ge h(t)\) 且 \(\phi(t)\le\psi(h(t))\)，得 P3；由 \(\psi(H(t))=ct\) 得同窗标量兼容。取 \(W_1(t)=t+h(t)/(1-\eta)\)，利用 \(h(\phi(t))\le\eta h(t)\) 即有
\[
 W_1(t)-W_1(\phi(t))\ge t-\phi(t)+h(t)\ge\|y-x\|.
\]
这样每个窗内初值对应有限长轨道，即使所有有效的最近零锚模都是非 Dini。这个构造说明 C309/C277 的实际采样或一步势对任意给定的严格递增非 Dini 高度都可实现。

<a id="td-literature"></a>
## 5. 一手证明实验与取舍

- **Rockafellar 1976 与 Solodov–Svaiter 1999。** Rockafellar 的准则 (A) 及 Theorem 1 使用非精确近端输出的误差容差和。Solodov–Svaiter 的 Algorithm 3.1、Lemma 4.1 和 Corollary 4.2 用固定相对误差与额外校正步获得到每个零点的平方距离下降、辅助步平方可和，再由 Theorem 3.1 得弱收敛。它取代的是预设的**内层求解误差**可和。直接照搬会改变更新并需要最大单调图。保留原更新时，C277 JP19–JP20 已刻画可用的全零锚 Fejér 分支，但存在最近零锚的原 P2 不提供全零锚下降，§1 的平方和发散轨道也排除其一般正平方耗散版本。 [Rockafellar 原文](https://www.ceremade.dauphine.fr/~carlier/Rockafellar1976.pdf) · [Solodov–Svaiter 原文](https://pages.cs.wisc.edu/~solodov/solsva99Teps.pdf)
- **Combettes 2001。** Theorem 3.11 提供由准 Fejér 与聚点条件转向点收敛的判别。Remark 7.5 的归一化投影次梯度法允许 \(\gamma\in\ell^2\setminus\ell^1\)，范数平方是能量递推中的误差；这证明另一种算法可在不预设步幅绝对可和时取得点收敛。§1 移植的是控制适当的轨道量并另证全序列收敛的原则，T1 由两次原近端图值的向量和给出。 [Combettes 原文](https://pcombet.math.ncsu.edu/ipa.pdf)
- **LMZ v1。** Theorem 5.1 的 (5.3) 用反复出现的解奇异化函数差支付实际步长，结论仍是有限长度。对本页的 \(T_-\)，取常见候选 \(E(x)=d(x)^2\)，则 \((E(x)-E(y))/\|x-y\|^2\to0\)，所以无法提供统一的平方下降。更强地，沿这条轨道任何有下界的能量都无法给 \(E(x)-E(y)\ge c\|x-y\|^2\)（\(c>0\)），因为步长平方和已经发散。已证的次梯度接口继续由 C311 保留。 [LMZ v1 §5](https://arxiv.org/html/2406.13207v1#S5) · [C311](ppa_nonlinear_gauge_and_coupled_obstruction.md#c311-kl)

两条证明均做了独立审查：Astra Max 重构了 D1、两个严格分离及线性观察测试，另检验 T1 的多值合成量词、留域和两类发散；主代理逐式复核并分别记录已有机制及其范围。
