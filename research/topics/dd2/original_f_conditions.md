# 原 F3 的等价可积性与保留 F1 时删除 F2

本页沿用 [E0](core.md#dd2-exact-contract)，原 \(\Phi\) 为同一最近输入锚的有符号下界，原 \(\psi\) 在完整真残差 \(\rho=r_F(y)\) 处评价，\(\rho\le s/\lambda\)。预设目标 \(\varphi\) 不由长度势替换。作者原 F1–F3 的现存转录和来源身份见[审计 §5.1](../../audit/FINAL_PROTOCOL_S4_S8_2026-11-21.md#dd2-original-f1-f3)；以下是独立推导，不声称本次重新取得了历史 509 行原附件。

<a id="dd2-original-integrability-equivalence"></a>
## FI1 · 非增上包络与原积分的可积性等价

先只固定正、有限、非减的 \(q:(0,R]\to(0,\infty)\)，记
\[
g(t)=\frac{t}{q(t)},\qquad P(t)=\int_0^t g(u)\,du .
\tag{FI1}
\]
这里及下文积分在零端按非负反常积分理解，不要求被积函数在零点有限。
若存在非增、正点有限的 \(\bar g\ge g\) 且 \(\int_0^R\bar g<\infty\)，显然 \(P(R)<\infty\)。
反向若 \(P(R)<\infty\)，取
\[
h(t)=2\int_{t/2}^R\frac{dv}{q(v)},\qquad
\bar g_*(t)=\sup_{t\le u\le R}\frac{u}{q(u)} .
\tag{FI2}
\]
正下界 \(q(t/2)>0\) 使 h 在正点有限且连续，h 非增。对任意 \(u\in[t,R]\)，
\[
h(t)\ge2\int_{u/2}^u\frac{dv}{q(v)}
       \ge\frac{u}{q(u)};
\]
所以 \(h\ge\bar g_*\ge g\)。Tonelli 给
\[
\int_0^R h(t)\,dt
=2\int_0^R\frac{\min\{2v,R\}}{q(v)}\,dv
\le4P(R).
\tag{FI3}
\]
因此三种条件等价：原 g 可积；其最小非增上包络可积；存在原 F3 所需的非增可积主函数。构造还给正窗连续的一个主函数。四倍仅比较上述同一整个 R 窗的积分；不能把固定 h 的较小尾段直接写成至多 \(4P(t)\)。

这是 [C406](inexact.md) 与 [PR4a–PR4b](potential_regularity.md#dd2-potential-regularity) 的同一支配机制。删除证明中的“非增上包络”步骤，使前提更便于核验，但在这个正非减分母范围内没有扩张零端可积的函数类。若另要求 \(\bar g(0)\) 为有限值，则已加入更强条件，不属于这里的等价。

## FI2 · 原 F3 积分与和函数逆积分

设 \([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在该区间连续严格增，\(\psi(0)=0\)，\(\lambda>0\)。只在这一分支定义
\[
b_{\rm inv}(v)=\lambda\psi^{-1}(v),\quad
q(t)=b_{\rm inv}(t/2),\quad
H(s)=s+\psi(s/\lambda)\quad(0\le s\le\lambda r_*).
\tag{FI4}
\]
H 连续严格增，其像为 \([0,\lambda r_*+\psi(r_*)]\)。在共同小窗
\[
0<R_0\le\min\{R,\psi(r_*)\}
\]
定义 \(\chi_\Sigma=H^{-1}\) 和 \(I_\Sigma(t)=\int_0^t u/\chi_\Sigma(u)\,du\)。
此处 R 是 q 的工作上限，须有 \(R/2\le\psi(r_*)\)。原模在 \([0,r_*]\) 以外可另有行为，不在此处作连续非减延拓。

对 \(0<t\le R_0\)，令 \(m=\min\{t/2,q(t)\}\)。它在 H 的定义域且 \(H(m)\le t\)，从而
\[
\min\{t/2,q(t)\}\le\chi_\Sigma(t),\qquad
\chi_\Sigma(t/2)\le q(t).
\tag{FI5}
\]
第二式由 \(H(q(t))=q(t)+t/2\ge t/2\) 得到；这里没有在超出定义域的 t 处评价 H。于是
\[
I_\Sigma(R_0)\le2R_0+P(R_0),\qquad
P(R_0)\le4I_\Sigma(R_0/2).
\tag{FI6}
\]
因为分母正且非减，离零紧段上的两个积分均有限。因此原 F3、\(P(R)<\infty\) 和和函数逆的零端可积性等价，完全不使用 F2 \(b_{\rm inv}(t)=o(t)\)。这不等于两套长度定理的全部前提等价：它们吸收同一 D 的条件还不同。

即使原模在较大残差处不单调，\(\chi_\Sigma\) 仍是上述局部尺度的有效步下界。若 \(s<\chi_\Sigma(t)\)，则真正
\(\rho\le s/\lambda<\chi_\Sigma(t)/\lambda\le r_*\)，所以此时才可在原分支比较
\(t\le a+s\le\psi(\rho)+s\le H(s)<t\)，矛盾。这不许可对一般大 s 无条件作 \(\psi(s/\lambda)\) 替换。

<a id="dd2-original-f1-without-f2"></a>
## FI3 · C453-v1：保持原 F1 不变的混合支付势

**状态：derived-checked。** 三席分别独立重构原逆域、积分等价和三分支支付，并复读实际终稿、完整剪切、身份与图边；零尺度、窗口、原目标及历史来源范围已核，无未关闭实质异议。

固定实 Hilbert 空间、非空闭 \(S\subseteq\operatorname{zer}F\)、\(\lambda>0\)、开工作域 U 和距离半径 \(R>0\)。允许关系在
\(U_R=\{x\in U:d(x,S)\le R\}\) 非空；对每条受检边保原 E0，包括最近输入锚存在、完整真残差属于 \(D_\psi\) 及原误差界。
设 \([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在该区间连续严格增、\(\psi(0)=0\)，且
\[
R/2\le\psi(r_*),\quad q(t)=\lambda\psi^{-1}(t/2)\ (0\le t\le R),\quad
P(t)=\int_0^t\frac{u}{q(u)}\,du,\quad P(R)<\infty .
\tag{FI7}
\]
q 在原窗连续严格增且 \(q(0)=0\)。保留作者原 F1 常数和同一 D：
\[
D(0)=0,\quad D(t)\ge0,\quad
\Phi(t)\ge-D(t)\quad(0\le t\le R),\qquad
D(t)\le\frac14q(t)^2\quad(0<t\le R).
\tag{FI8}
\]
不假设 F2，不限制原模在其余评价域的单调性。定义
\[
\alpha=\frac{16\sqrt3}{3},\quad
\beta=3+2\sqrt3,\qquad
W(t)=\alpha P(t)+\beta q(t).
\tag{FI9}
\]
则每条允许边满足
\[
a<t\quad(t>0),\qquad
s\le W(t)-W(a),\qquad
s=a=0\quad(t=0).
\tag{FI10}
\]
W 非负、连续、严格增且零端归零。对已从原数据另行认证的预设目标仍保 \(a\le\varphi(t)\)；FI10 不把 W 冒充目标。若
\[
x^0\in U_R,\qquad W(t_0)<d(x^0,U^c),
\tag{FI11}
\]
则全部允许轨道可续、留在 \(U_R\)，趋于 \(S\cap U\) 中一点，并满足
\[
\sum_{j\ge k}\|x^{j+1}-x^j\|\le W(t_k)\longrightarrow0.
\tag{FI12}
\]
在 \(U=H\) 无位置边界。上述常数是明确充分常数，不声称最优。

### FI4 · 原域反推与三种步的完整证明

**阈值引理。** 对 \(0<v\le R/2\)，若 \(a\ge v\)，则
\[
s\ge b_{\rm inv}(v).
\tag{FI13}
\]
否则真正 \(\rho\le s/\lambda<\psi^{-1}(v)\le r_*\)，已自动落在原严格分支中，于是
\(a\le\psi(\rho)<v\)，矛盾。没有在较大残差处代换原 \(\psi\)，也没有预先假定 \(a\le R\)。

同一锚的平方展开和原 F1 给
\[
a^2+s^2\le t^2+\tfrac12q(t)^2.
\tag{FI14}
\]
若 \(a\ge t/2\)，FI13 先给 \(s\ge q(t)>0\)，故
\(\Delta=t^2-a^2\ge s^2/2>0\)，证明 \(a<t\)。另一种情况 \(a<t/2\) 自带严格下降。所以先证明了 \(a<t\le R\)，才在后面评价 q(a) 和 P(a)。再由 FI13 用 \(v=a/2\) 得 \(q(a)\le s\)；a=0 时亦成立。

1. 若 \(a\ge t/2\)，q 非减和上式给
   \[
   P(t)-P(a)\ge\frac{\Delta}{2q(t)}
                 \ge\frac{s^2}{4q(t)}\ge\frac{s}{4}.
   \tag{FI15}
   \]
2. 若 \(a<t/2\) 且 \(q(t)\le2t\)，FI14 给 \(s\le\sqrt3t\)，而
   \[
   P(t)-P(a)\ge\int_{t/2}^t\frac{u}{q(t)}\,du
       =\frac{3t^2}{8q(t)}\ge\frac{3t}{16}.
   \tag{FI16}
   \]
   故 \(s\le\alpha[P(t)-P(a)]\)。
3. 若 \(a<t/2\) 且 \(q(t)>2t\)，置 \(\theta=\sqrt3/2<1\)。FI14 给
   \(s\le\theta q(t)\)，而 \(q(a)\le s\le\theta q(t)\)，从而
   \[
   s\le\frac{\theta}{1-\theta}[q(t)-q(a)]
        =\beta[q(t)-q(a)].
   \tag{FI17}
   \]

三种情况都被 FI9 支付。零输入时最近锚 p=x，
\(-s^2=\langle x-y,y-p\rangle\ge-D(0)=0\)，所以驻定。
有限前缀望远镜给总长至多 W(t0)，FI11 支付第一条拟出界边，因而所有选择留在 U，严格降距保距离窗。非空覆盖遂给续接。

若距离极限为 \(\ell>0\)，相邻距离比趋于1，最终全属第一种情况；那时
\[
t_k^2-t_{k+1}^2\ge\tfrac12q(t_k)^2
                       \ge\tfrac12q(\ell)^2>0,
\]
矛盾。因此 \(t_k\to0\)，W 的零端连续性给 FI12。有限长度给范数 Cauchy；S 闭和距离趋零识别目标，严格位置预算把极限留在 U。不需要 F 本身闭图。

在 E0 和上述局部原逆合同内，原 F1 已足以独立认证连续的安全目标
\[
A_{F1}(t)=\max\left\{\frac t2,
       \sqrt{\bigl[t^2-\tfrac12q(t)^2\bigr]_+}\right\}<t
       \quad(t>0),\qquad A_{F1}(0)=0 .
\tag{FI18}
\]
它不必非减。若先指定 \(\varphi\ge A_{F1}\)，上述原数据认证该目标；更小的预设目标必须另核。证明用实际净下降而非盲目复合 FI18。

<a id="dd2-f1-mixed-potential-example"></a>
## FI5 · 完整连续剪切说明 F2 可删而势的修正有内容

取 \(\lambda=1,H=\mathbb R^2,U=V_\psi=H,D_\psi=[0,\infty)\)，
\[
S=\mathbb R\times\{0\},\quad
\psi(\rho)=\rho^2,\quad \Phi(t)=-t/8,\quad D(t)=t/8,\quad
R=1/8,\quad \varphi(t)=t/2 .
\tag{FI19}
\]
原 \(b_{\rm inv}(v)=\sqrt v\)、\(q(t)=\sqrt{t/2}\) 满足 F1 等号；F2
\(b_{\rm inv}(t)=o(t)\) 失败。原
\[
P(t)=\frac{2\sqrt2}{3}t^{3/2}
\tag{FI20}
\]
有限，且 \(t/q(t)=\sqrt{2t}\) 被常数 \(\sqrt{2R}\) 非增主函数支配。
预设 \(\varphi=t/2\) 由同一数据认证全部 E0 边：若 \(a\ge t/2\)，FI15 前的能量给
\(t^2-a^2\ge t/4\)，但左侧至多 \(3t^2/4<t/4\) 于 \(0<t\le R\)，矛盾。

定义完整全域连续单值算子
\[
F(u,v)=(-\sqrt{|v|},\,7v),\qquad
J_{\!F}(u,v)=(u+\sqrt{|v|/8},\,v/8).
\tag{FI21}
\]
\(I+F\) 是全域同胚，故第二式确为全部近端且唯一；精确零集就是 S。
对输出 \(y=(u,v)\)，令 \(a=|v|\)，则输入
\(x=(u-\sqrt a,8v)\)、\(t=8a\)，最近输入锚 \(p=(u-\sqrt a,0)\)。直接算出
\[
\rho=s=\sqrt{a+49a^2},\quad
a\le\psi(\rho),\quad
\langle x-y,y-p\rangle=-a+7a^2\ge-t/8 .
\tag{FI22}
\]
零输入驻定、全部输入覆盖、正距离窗不变；实际 \(a=t/8<\varphi(t)\)。
沿任意 \(t_0>0\) 的真实轨道，\(t_k=8^{-k}t_0\)，并有
\[
\frac{\sqrt{t_k}}{\sqrt8-1}
\le\sum_{j\ge k}s_j
\le
\sqrt{1+49t_k/8}\,
\frac{\sqrt{t_k}}{\sqrt8-1}.
\tag{FI23}
\]
故真实尾长等价于 \(\sqrt{t_k}/(\sqrt8-1)\)。横向尾移恰为该无额外根因子的量；点极限及长度都存在。

然而 \(s\ge\sqrt{t/8}\)，\(P(t)-P(t/8)=O(t^{3/2})\)，所以任何固定有限倍的原 P 都不能支付这个同一图的全部小尺度边。新 q 项恰有实际需要的 \(\sqrt t\) 量级。
同一数据的 \(\chi_\Sigma+\chi_\Sigma^2=t\) 给 \(\chi_\Sigma\le t\)，原 C401 吸收条件也失败。甚至对这个固定图，任一有效步下界 \(\widetilde b(t)\le s(t)\) 都不能修复它：
\[
2D(t)=t/4>s(t)^2=t/8+49t^2/64
\quad(0<t\le R<8/49).
\tag{FI24}
\]
所以不只是默认候选选得不佳。这里放宽的是原 F2 及统一严格吸收所用的机制，FI1–FI6 的零端可积性本身未变。该结果不替代 C424 的消失余量判据，也不宣称公开新颖性、最优常数或原 F1 的必要性。
