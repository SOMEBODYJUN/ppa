# 一般模 RLEB 与广义 PPA：完成的融合及严格比较

<a id="gpm-verdict"></a>
## 完成结论与精确比较对象

**我们的一般模反射几何和真残差理论已经接到固定核的完整 GPPA。** 新条件不是把普通变量机械换一个名字，而是核完整纤维、残差评价域、标量能量、物理提升和留域的合取。保留能量分支后，它涵盖 Le–Mordukhovich–Théra 2608.01584v1 Theorem 2 的全部核收敛实例，并有严格增加的固定核实例。还构造了非线性强单调核下的完整双支族：在同一完整图和指定广义算法上，任意源配对单调核都不能保持这些轨道，而新证书成立。

“严格增加”有证明；“整篇文章在所有改写下绝对更好”没有被证明。源文二次范数是能量表达，不是“算法最多二次收敛”。它的固定核 Theorem 2 给线性上界；我们另有任意指定 \(\nu>1\) 的精确物理 Q-\(\nu\) 族，包括 \(\nu>2\)，也有非幂次 Dini 族。广义更新的核 \(v\) 是固定的；本轮不偷换成逐步变化的 \(v_k\)。

<a id="gpm-objects"></a>
## 完整对象与新的反射条件

在实 Hilbert 空间上固定完整 \(F:H\rightrightarrows H\)、单值全域核 \(v:H\to H\)、\(\lambda>0\)：

\[
v(x_k)-v(x_{k+1})\in\lambda F(x_{k+1}),\quad
A(z)=\bigcup_{v(x)=z}F(x),\quad Q=v(H),\quad
\operatorname{zer}A=v(\operatorname{zer}F).
\]

这给核坐标 \(z_k=v(x_k)\) 的**完整** PPA，且 \(r_A(v(x))\le r_F(x)\)。非单射核不能把这个不等式改成等号。全核图反射条件为

\[
\|v(x)-v(y)-\lambda(f-g)\|
\le\omega\!\left(\|v(x)-v(y)+\lambda(f-g)\|\right),
\quad f\in F(x),\ g\in F(y),
\]

对指定同一图块及核输入对尺度内的**全部**点对成立。覆盖需另证；完整 warped 纤维可能仍多值。若 \(v=\operatorname{Id}\)，准确退回本库普通 RLEB–PPA；若 \(v\) 非线性，给真正广义算法。核本身单调不是源文必要条件，不过本轮严格例子可以采用非线性强单调核。

<a id="gpm-theorem"></a>
## C208/C209：一般模的完整标量定理

共同前件在 [NGK-2](../comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md#ngk-data)逐项列全：同一图块在真实像集 \(Q\cap U\) 的 coverage；闭核零目标 \(Z\) 的所有零锚；同尺度全对反射模 \(\omega\)；实际输出的完整核真残差 EB \(d(z^+,Z)\le\psi(r_A(z^+))\)；\(B(R)/\lambda\le\bar t\) 的评价域门。这里

\[
B(t)=\frac{t+\omega(t)}2,\qquad C(t)=\frac{t^2+\omega(t)^2}2.
\]

最近锚可用近极小列；任意 Hilbert 闭非凸集不被假定有最近点。一步结论严格为

\[
(d^+)^2+s^2\le C(d),\quad s\le B(d),\quad
r_A(z^+)\le s/\lambda\le\bar t,
\quad d^+\le\psi(s/\lambda).
\]

若 \(\psi\) 连续严格增加，令 \(g=\psi^{-1}\)、\(V(t)=t^2+\lambda^2g(t)^2\)，则

\[
V(d^+)\le C(d).
\]

因此同时保留 **直接** \(\psi(B(d)/\lambda)\) 与 **能量** \(V^{-1}(C(d))\) 两个标量上界；逆函数上端用已证输出范围截断。再有源式零锚耗散 \(\langle f,z^+-p\rangle\ge a(d^+)\) 时，\(W=V+2\lambda a\) 又给 \(W(d^+)\le d^2\)。取有效上界的最小值为 \(\tau(d)\)。

若同窗 \(\tau(t)<t\) 且 \(H_\tau(r)=\sum_{j\ge0}B(\tau^j(r))\) 可和，严格初值预算 \(H_\tau(d_0)<d(z_0,H\setminus U)\) 给全部核轨道存在、留域、有限长、极限在闭 \(Z\cap U\)，尾不超过 \(H_\tau(\tau^k(d_0))\)。常用充分门是 \(\tau(t)\le\kappa t\) 与 \(\int_0^R\omega(t)dt/t<\infty\)。另一个独立能量门为 \(R\le\psi(\bar t)\)、\(C(t)\le qV(t)\)、\(q<1\)，它给几何能量及可和核步长，不必强加 Dini。

完整证明含域、零退化、逆截断及逐步留域，见 [NGK-1–5](../comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md#ngk-object)。原普通 PPA 证明身份保持；新 Claim 是广义固定核对象。

<a id="gpm-inclusion"></a>
## 吸收源文机制，并真正证明包含

源 ASM 前提
\(\langle\Delta f,\Delta v\rangle\ge\varepsilon\|\Delta v\|^2\)
强制 \(v(S)=\{z_*\}\)，并在完整 \(A\) 上给 \(\omega(t)=t\)、\(\psi(s)=s/\varepsilon\)。于是

\[
V(t)=(1+\lambda^2\varepsilon^2)t^2,\quad
\tau_E(t)=\frac{t}{\sqrt{1+\lambda^2\varepsilon^2}}<t
\]

对 **每个** \(\lambda\varepsilon>0\) 成立。直接分支孤立使用会漏源实例；即使锐模也可能失败，见 [F55](../../FAILED_ROUTES.md#f55)。把源的零锚耗散保留为 \(a(t)=\varepsilon t^2\)，还得 \(\tau_A(t)=t/(1+\lambda\varepsilon)\)。这个加强只是同一前提的初等推导，不被包装成另一个新颖性发现。

源逆像 R-continuity 接成 \(d(x_{k+1},S)\le\rho(s_k/\lambda)\)（选中残差进入源规定的局部半径后），保留了真实物理集合距离结论。它不能替代核纤维控制。**吸收的是精确核更新、完整配对条件、锚耗散、残差桥与误差建模；没有强迫新理论也必须配对单调。** 源完整范围逐项映射见 [NGK-7](../comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md#ngk-source-inclusion)。

<a id="gpm-physical"></a>
## C210：物理点、物理长度与回缩分别成立的条件

若实际物理点对有统一反演/选中纤维模 \(\|x-y\|\le\eta(\|v(x)-v(y)\|)\)，核有限长与 \(\eta(0+)=0\) 输送物理端点 Cauchy；零成员身份还需同一零集的闭性与真 EB、闭图零极限门或 homeomorphic 完整拉回。

**物理有限长**的统一包络证书要求 \(\sum_j\eta(B(\tau^j(d_0)))<\infty\)。几何距离情形的充分门是 \(\int_0^R\eta(B(t))dt/t<\infty\)。强单调核给 Lipschitz 逆，幂模自然通过；Hölder 逆与非幂模要检查复合 Dini。物理留域需要在输出领圈先认证反演界，不能循环假设输出已在初值邻域。

同图全对模加核连续性、唯一物理输出和严格共同长度预算给连续物理极限回缩；homeomorphic 拉回的回缩版本只需核 Dini。非单射核政策只在受控截面或允许转移范围获得物理结论，不能覆盖任意完整输出；若只有相邻允许转移界，则点收敛也须变换后的步长可和，不能仅凭模连续。见 [GP1–27](../comparisons/2026_08_gppa_nfb/gppa_physical_transfer.md#gp-data)。

<a id="gpm-strict"></a>
## C211/C212：严格扩张例子和“任意阶”的范围

全图共轭 \(F^V=G\circ V\)、\(J_{\lambda F^V}^V=V^{-1}J_{\lambda G}V\) 保留完整两支、全部纤维和真残差。可取

\[
V(\xi,\eta,y)=(\xi+c\sin y,\eta,y+b\tanh y),
\quad b>0,\quad0<c<1,
\]

它非线性、全域双 Lipschitz 且 \((1-c/2)\)-强单调。cap、超线性和对数族均给同对象证书；无需删支。

超线性族每个 \(\nu>1\)、\(0<\gamma<1\)、\(A,B>0\)，有真 EB 幂 \(q=\nu/\gamma\)、小窗严格兼容、精确法向 \(r_{k+1}=r_k^\nu\)；对指定非正第二切向初值与 \(0<r_0<1\)，物理点误差满足

\[
\lim_{k\to\infty}\frac{e_{k+1}}{e_k^\nu}=A^{1-\nu}.
\]

这是任意指定 Q-\(\nu\) 的真实族，超二次情形明确存在。一般幂条件本身只给核零距离上界：\(q\gamma>1\) 自动小窗兼容；\(q\gamma=1\) 需要 \(C[L/(2\lambda)]^q<1\)；其余失败是**该测试**失败，不是轨道发散。非幂次 \(a>1\) 对数族还给多项式点尾和可和实际步长。

完整双支、连通正法向片和公共递增切向剖面，通过有限变差分割，强制任意源配对单调核的正常分量恒定；与指定非驻定更新矛盾。这个排除允许核完全不连续，也允许任意正步长。见 [完整共轭和证明](../comparisons/2026_08_gppa_nfb/gppa_strict_extension_examples.md)。但保零集删支导入仍成立，故不宣称这些轨道不能借源框架的合法改写证明收敛。

另有弱单调壳层证书：\(\psi(s)=Ks^q\)、\(q>1/2\) 足以核有限长。\(F(x)=\operatorname{sgn}(x)|x|^p\)、\(v=\operatorname{Id}\)、\(1<p<2\) 是固定核 T2 的严格非 ASM 例，拥有多项式率。源 T1 可以证明它的收敛；严格性不被扩大成整个 GPPA 文献排除。见 [NGK-6/10](../comparisons/2026_08_gppa_nfb/gppa_nonlinear_kernel_theorem.md#ngk-shell)。

<a id="gpm-spiral"></a>
## C214：融合后新识别出的锐门槛

将完整对数双支关系以切向极坐标 twist \(g(z)=e^{ic/|z|}z\) 拉回；核逆的任意零邻域上两点 Hölder 界的最佳指数为 \(1/2\)，真物理残差和正常零距离保持不变。核 Dini 在 \(a>1\) 成立，物理点也收敛，却在 \(1<a<2\) 有步长 \(\sim c(a-1)/k\)，因而物理长度无限。\(a=2\) 使用明确校准 \(c=\pi/(\log4)^2\) 仍发散；\(a>2\) 半径级数可和，物理有限长。

这个校准完整族的物理长度门恰为 \(a>2\)，匹配半阶逆的复合 Dini。它同时有连续极限回缩，证明“点收敛／回缩”和“物理有限长”不能互相偷换。完整构造、Hölder 最优性及无限轨道证明见 [GP28–40](../comparisons/2026_08_gppa_nfb/gppa_physical_transfer.md#gp-spiral)。

<a id="gpm-errors"></a>
## C213：持续误差思想的可用融合

保留源物理输出模型，但用实际核向前模把误差换成核输出误差。若 \(z_{k+1}=Tz_k+e_k\in Q\)、\(\|e_k\|\le E_k\)、\(d(Tz,Z)\le\theta d(z,Z)\)，则

\[
d(z_k,Z)\le\theta^kD_0+
\sum_{j<k}\theta^{k-1-j}E_j.
\]

持续误差 \(E_j\le\delta\) 在完整认证领圈给 \(\limsup d(z_k,Z)\le\delta/(1-\theta)\)；逆模输送非线性物理误差管。误差趋零仅给零集距离趋零，点/长度仍需相应可和性。源正则化 \(F+\epsilon v\) 的全部结论不在此自动包含。见 [完整误差定理与反例](gppa_inexact_modulus.md#gi-data)。

<a id="gpm-assets"></a>
## 可直接接续的成果与未闭边界

- [完整定理研究稿](../manuscripts/gppa_modulus/gppa_modulus.pdf)和[数学源稿](../manuscripts/gppa_modulus/gppa_modulus.tex)集中呈现证明。
- [独立审查记录](../audit/GPPA_MODULUS_RECEPTION_2026_10_09.md)列实际受检范围、已落实的陈述修正和仍未核的先行性；不是全库清洗完工证明。
- [有限复算入口](../code/gppa_modulus/README.md)保存源代码、全部参数、精确反算、浮点容差和实际结果。计算不替代正文证明。

当前剩余义务是完整新理论的全球先行性、任意变核/升维/改图表示分类及一般原生模型应用；固定核一般模定理、源 T2 核包含、明确严格例和物理边界已形成可复用资产。这里的局部算法理论没有覆盖或改写附件的全尺度结构/影子/纤维命题，后者的研究身份保持独立。
