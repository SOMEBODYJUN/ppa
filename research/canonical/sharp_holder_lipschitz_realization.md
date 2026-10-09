# 精确 Hölder 预算下的全域单值 Lipschitz 零集实现

本页为 **C222 的独立规范证明**，状态 `derived-checked`：SHLR1–21经不同审查者逐式重建；外部优先性未认证。它重构正式附件 `cor:lipschitz_realization` 的数学陈述，并用一个平方距离混合替代局部 bump 与可数凸组合。C04 的有限维必要性不作为本页的证明前提；本页只证明给定紧集的充分实现。精确身份与全库登记见[Claim总账](../../CLAIMS.md#c222)，本页不认证外部优先性。

<a id="shlr-object"></a>
## SHLR-OBJECT · 精确对象与结论

令 \(H\) 为任意实 Hilbert 空间，\(K\subset H\) 为非空紧集，固定
\[
\lambda>0,\qquad 0<\gamma<1,\qquad 0<\eta<1,
\qquad D=\operatorname{diam}K,\qquad Q=\overline{\operatorname{conv}}K.
\tag{SHLR1}
\]
则存在一个全域单值 Lipschitz 映射 \(F:H\to H\)，使
\[
\begin{aligned}
F^{-1}(0)&=K,\\
\operatorname{Lip}F&\le\frac{1+\eta}{\lambda(1-\eta)},\\
\sup_{u\in H}\left\|F(u)-\frac{u-P_Qu}{\lambda}\right\|
&\le\frac{\eta D}{\lambda}.
\end{aligned}
\tag{SHLR2}
\]
这里参照映射的符号是 \((\operatorname{Id}-P_Q)/\lambda\)，与 Cayley 约定 \(p=x+\lambda v\)、\(C(p)=x-\lambda v\) 一致。

同一个 \(F\) 的 Cayley 映射 \(C:H\to Q\) 在全空间满足
\[
\|C(p)-C(q)\|\le D^{1-\gamma}\|p-q\|^\gamma,
\qquad \operatorname{Fix}C=K.
\tag{SHLR3}
\]
若 \(D>0\)，\(D^{1-\gamma}\) 是该 \(C\) 的最小全局 \(\gamma\)-Hölder 常数；\(D=0\) 时最小常数为零。故给定任何 \(L>0\) 且 \(D^{1-\gamma}\le L\)，\(F\) 的整个图在固定 \((\lambda,L,\gamma)\) 下满足全尺度 RL，且在该固定参数类内 graph-maximal。这包括直径边界 \(D=L^{1/(1-\gamma)}\)。

本结论不说 \(F\) 强单调；若 \(K\) 有两个不同点，强单调性与该零集不相容。这里实现的是一个完整逆纤维，不同时预设正向纤维。

<a id="shlr-margin"></a>
## SHLR-MARGIN · 平方距离的凸包余量

以下设 \(D>0\)。记 \(d(y)=\operatorname{dist}(y,K)\)。对所有 \(y,z\in Q\)，
\[
\|y-z\|^2+d(y)^2\le D^2.
\tag{SHLR4}
\]
证明：先有 \(\|k-z\|\le D\) 对 \(k\in K,z\in Q\) 成立，因为该估计在 \(z\) 为有限凸组合时由三角不等式成立，并可取极限。取有限凸组合 \(y_m=\sum_i a_i k_i\to y\)，\(a_i\ge0\)、\(\sum_i a_i=1\)。Hilbert 方差恒等式给
\[
\|y_m-z\|^2
=\sum_i a_i\|k_i-z\|^2-\sum_i a_i\|k_i-y_m\|^2
\le D^2-d(y_m)^2.
\]
距离函数连续，故取极限得 SHLR4。这也说明 \(\operatorname{diam}Q=D\)、\(d(y)\le D\) 及 \(\|y-k_0\|\le D\) 对任意指定 \(k_0\in K\) 和 \(y\in Q\) 成立。

<a id="shlr-mix"></a>
## SHLR-MIX · 一个平方距离混合即达到预算边界

固定 \(k_0\in K\)，取
\[
0<\alpha\le\min\left\{\frac{1-\gamma}{6},\frac{\eta}{3}\right\},
\quad
E(y)=-\frac{\alpha d(y)^2}{D^2}(y-k_0),
\quad S(y)=y+E(y)\qquad(y\in Q).
\tag{SHLR5}
\]
因 \(0\le\alpha d(y)^2/D^2\le\alpha<1\)，\(S(y)\) 是 \(y\) 与 \(k_0\) 的凸组合，所以 \(S(Q)\subset Q\)。若 \(y\in K\)，则 \(E(y)=0\)。若 \(y\in Q\setminus K\)，紧性使 \(K\) 闭，故 \(d(y)>0\)，且 \(y\ne k_0\)，于是 \(E(y)\ne0\)。因此
\[
\operatorname{Fix}S=K,\qquad
\sup_{y\in Q}\|E(y)\|\le\alpha D.
\tag{SHLR6}
\]

令 \(h=\|y-z\|\)。距离函数为 \(1\)-Lipschitz，故
\[
\begin{aligned}
\|E(y)-E(z)\|
&\le\frac{\alpha}{D^2}
\left[d(y)^2h+|d(y)^2-d(z)^2|\,\|z-k_0\|\right]\\
&\le3\alpha h\le\eta h.
\end{aligned}
\tag{SHLR7}
\]
另用 SHLR4 及三角不等式，有
\[
\|E(y)-E(z)\|
\le\frac{\alpha}{D}\bigl(d(y)^2+d(z)^2\bigr)
\le\frac{2\alpha}{D}(D^2-h^2).
\tag{SHLR8}
\]
因此
\[
\|S(y)-S(z)\|
\le h+\alpha\min\left\{3h,\frac{2(D^2-h^2)}D\right\}.
\tag{SHLR9}
\]
对 \(t\in[0,1]\)，逐区间 \(t\le1/2\)、\(t\ge1/2\) 得
\[
\min\{3t,2(1-t^2)\}\le6t(1-t).
\tag{SHLR10}
\]
对 \(0<t\le1\)，函数 \(t^{-(1-\gamma)}\) 的凸性及在 \(1\) 处的切线给
\[
t^\gamma-t
=t\bigl(t^{-(1-\gamma)}-1\bigr)
\ge(1-\gamma)t(1-t).
\tag{SHLR11}
\]
\(t=0\) 时也成立。将 \(t=h/D\) 代入 SHLR9，并用 \(6\alpha\le1-\gamma\)，得到
\[
\|S(y)-S(z)\|\le D^{1-\gamma}\|y-z\|^\gamma
\qquad(y,z\in Q).
\tag{SHLR12}
\]
此外 SHLR7 给 \(\operatorname{Lip}S\le1+\eta\)。

<a id="shlr-cayley"></a>
## SHLR-CAYLEY · 全空间映射及精确最小常数

闭凸集 \(Q\) 的 Hilbert 度量投影 \(P_Q:H\to Q\) 存在、非扩张、单调，且 \(\operatorname{Id}-P_Q\) 非扩张。所需性质和证明可由 [FF-PROJECTION](finite_fiber_classification.md#ff-projection) 的投影变分不等式重建：互用该不等式得 \(\|P_Qa-P_Qb\|^2\le\langle P_Qa-P_Qb,a-b\rangle\)，展开平方即得残差非扩张。

定义
\[
R=S\circ P_Q=P_Q+E\circ P_Q:H\to Q.
\tag{SHLR13}
\]
非扩张性与 SHLR12 使 \(R\) 满足 SHLR3 的 Hölder 界，且 \(\operatorname{Lip}R\le1+\eta\)。若 \(R(a)=a\)，值域条件使 \(a\in Q\)，于是 \(P_Qa=a\) 及 \(S(a)=a\)，故 \(a\in K\)。反向每个 \(k\in K\) 显然固定，因而 \(\operatorname{Fix}R=K\)。

任意固定 \(K\) 每点且有全局 Hölder 常数 \(B\) 的映射，对不同 \(k,l\in K\) 必须有
\(\|k-l\|\le B\|k-l\|^\gamma\)，故 \(B\ge\|k-l\|^{1-\gamma}\)。取上确界即得 \(B\ge D^{1-\gamma}\)。因此上界 SHLR3 对 \(R\) 的常数恰为最小预算，并非只有任意接近该预算。

<a id="shlr-invert"></a>
## SHLR-INVERT · 单值全域 Lipschitz 原映射

定义 \(G=(\operatorname{Id}+R)/2\)。由投影单调及 SHLR7，
\[
\begin{aligned}
2\langle G(a)-G(b),a-b\rangle
&=\|a-b\|^2+\langle P_Qa-P_Qb,a-b\rangle\\
&\quad+\langle E(P_Qa)-E(P_Qb),a-b\rangle\\
&\ge(1-\eta)\|a-b\|^2.
\end{aligned}
\tag{SHLR14}
\]
同时 \(\operatorname{Lip}G\le M=(2+\eta)/2\)，强单调模至少 \(c=(1-\eta)/2>0\)。对任意 \(u\in H\) 及 \(0<t<2c/M^2\)，
\[
\|[a-t(G(a)-u)]-[b-t(G(b)-u)]\|^2
\le(1-2tc+t^2M^2)\|a-b\|^2.
\tag{SHLR15}
\]
括号内系数小于一，故 Banach 固定点定理在完备 \(H\) 上给 \(G(a)=u\) 的唯一解。这证明 \(G\) 双射；SHLR14 与 Cauchy–Schwarz 另给
\[
\operatorname{Lip}G^{-1}\le\frac2{1-\eta}.
\tag{SHLR16}
\]
置
\[
F(u)=\frac{a-R(a)}{2\lambda}=\frac{a-u}{\lambda},
\qquad a=G^{-1}(u).
\tag{SHLR17}
\]
因为 \(\operatorname{Id}-P_Q\) 非扩张，SHLR7 给
\(\|(a-R(a))-(b-R(b))\|\le(1+\eta)\|a-b\|\)。结合 SHLR16 得 SHLR2 的 Lipschitz 界。

\(F(u)=0\) 等价于 \(a=R(a)\)，即 \(a\in K\)，此时 \(u=G(a)=a\)。故完整零集为 \(K\)。又
\[
u+\lambda F(u)=a,\qquad u-\lambda F(u)=R(a).
\tag{SHLR18}
\]
所以 \(F\) 的 Cayley 映射恰是全域 \(R\)。SHLR3 转写为整个图的同参数 RL 界。若在该固定参数类增加图点，令新点的 \(p=x+\lambda v\)；SHLR18 已给同一个 \(p\) 的旧图点，二者比较时 RL 右侧为零，迫使 \(x-\lambda v\) 也相同，故图点相同。这证明 graph-maximal，而无需把 RL 图极大性混同于 maximal monotone。

<a id="shlr-residual"></a>
## SHLR-RESIDUAL · 统一逼近投影残差及符号

置 \(G_0=(\operatorname{Id}+P_Q)/2\)。它强单调模至少 \(1/2\)，且
\[
G_0^{-1}(u)=2u-P_Qu.
\tag{SHLR19}
\]
事实上投影变分不等式使 \(P_Q(u+s(u-P_Qu))=P_Qu\) 对每个 \(s\ge0\) 成立；取 \(s=1\) 即核 SHLR19。

令 \(a=G^{-1}(u)\)、\(a_0=G_0^{-1}(u)\)。利用 \(G_0^{-1}\) 的 Lipschitz 常数至多二及 \(G=G_0+E\circ P_Q/2\)，
\[
\|a-a_0\|
\le2\|G_0(a)-G_0(a_0)\|
=\|E(P_Qa)\|\le\alpha D\le\eta D.
\tag{SHLR20}
\]
而 \((a_0-u)/\lambda=(u-P_Qu)/\lambda\)，所以 SHLR17 与 SHLR20 给
\[
\sup_{u\in H}\left\|F(u)-\frac{u-P_Qu}{\lambda}\right\|
\le\frac{\alpha D}{\lambda}\le\frac{\eta D}{\lambda}.
\tag{SHLR21}
\]
较小的 \(\alpha D/\lambda\) 是本构造的附带界，不声称全类最优。对 \(D=0\)、\(K=\{k_0\}\)，直接取 \(R\equiv k_0\)、\(F(u)=(u-k_0)/\lambda\)，全部结论成立且逼近误差为零。

<a id="shlr-priority"></a>
## SHLR-PRIORITY · 来源身份、独立接收和范围

正式附件与仓库 [S23 原 TeX](../../history/sources/次单调论文研究/最新成果/Holder_RL_Formal_Manuscript.tex) 的 SHA-256 同为 `1c7c870d1468a565792aa44b98c95b60031fd7e586c46d1f175f824dd2e92deb`。其 `cor:lipschitz_realization`（lines 875–945）陈述是有限维、\((\operatorname{Id}-P_Q)/\lambda\) 参照。本页 SHLR14–21 独立核完该 corollary 的反演、常数和参照符号，并说明这些充分实现步骤不使用有限维性。本页只固定非空紧 \(K\) 的范围，未把其它集合类默认为 C222。

Goebel, *Remarks on fixed point sets*, Stud. Univ. Babeș-Bolyai Math. **61** (2016), 429–434，**Claim 1，pp.431–432**，已发表任意闭固定集的 \((1+\varepsilon)\)-Lipschitz 自映射；原文混合因子是 \(\varepsilon\operatorname{dist}(y,K)/(2\operatorname{diam}Q)\)，不是 SHLR5 的平方距离。[期刊原文 PDF](https://www.cs.ubbcluj.ro/journal/studia-mathematica/journal/article/view/159/pdf)。**SHLR4 与平方距离混合的精确预算配对是本轮独立推导，不是该旧文已陈述的定理。**

这证明达到边界可由一个初等的经典固定集混合变体、Hilbert 方差余量及 Cayley 反演完成。它减少所需构造机制，不能单凭“可直接推导”就宣布旧文已发表 C04 的精确边界。数学成立、经典可导出性和公开优先性须分别判断；精确边界的发表先行比较仍须核旧文正文及其版本。

数值复算见 [structure_priority_check.py](../code/gppa_novelty/structure_priority_check.py)；有限样本只检查算术与实现，不替代本页全参数证明。独立接收范围及先行文献实际阅读记录见 [structure_priority_followup.md](../novelty/2026_10_09/structure_priority_followup.md)。
