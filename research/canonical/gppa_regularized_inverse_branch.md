# 正则化持续误差的逆核分支：固定正则化零点的物理距离管

本页是 C216 的附加分支，身份 **C220-v1 / GP-REG-INVERSE**，状态 `derived-checked`。其机制在普通极大单调、核为 Id 的情形已有一级先行：Le–Mordukhovich–Théra，[2606.01536v2](https://arxiv.org/html/2606.01536v2)，2026-09-08，§3 Theorem 3。这里把该分支按本库完整物理/核量词接到 C216；**不是首创声明**。[独立审查](../novelty/2026_10_09/new_claim_review.md)已重构 RI7、跳跃 gauge 和标量锐性；零维比较边界已修复并复验。

<a id="gri-data"></a>
## 1. 对象、存在和独立残差窗口

沿用 [C216 的 RS1–4](gppa_regularized_stability.md#grs-data)：实 Hilbert H，固定完整 F、全域单值 L-Lipschitz 核 v（L≥0），完整 (F,v) pair-monotone；λ,ε>0、δ≥0，S=zer F 与 Sε=zer(F+εv) 非空；a=inf_{s∈S}||v(s)||；F⁻¹ 在 0 的完整 R-continuity 具有半径 σ>0、非减 gauge ρ，ρ(0)=ρ(0+)=0。每条**已存在**的合法轨道满足

\[
v(x_k)-v(\widehat x_{k+1})
\in\lambda\bigl(F(\widehat x_{k+1})+\epsilon v(\widehat x_{k+1})\bigr),
\quad x_{k+1}=\widehat x_{k+1}+e_{k+1},\quad\|e_{k+1}\|\le\delta.
\tag{RI1}
\]

若要求全部初值、全部允许误差政策都有无限轨道，仍须另证正则化 warped coverage；逆核估计不生成 coverage。以下距离管要求独立窗口

\[
\epsilon a<\sigma.
\tag{RI2}
\]

追加一个全域逆 Lipschitz 门：存在 m>0，使

\[
\|x-y\|\le m^{-1}\|v(x)-v(y)\|\qquad(x,y\in H).
\tag{RI3}
\]

RI3 只给 v 单射和现有像上的反演控制，不要求 v 满射。若 H 非平凡且同时 v 为 L-Lipschitz，则 m≤L。可用局部认证版本：对于所选固定 sε∈Sε，RI3 只需在全部被使用的点对 (x_k,sε) 或 (hat x_{k+1},sε) 上成立，分别授予下面 RI6 或 RI7；若只核 x 点对，不自动授予 hat 分支。局部认证窗口必须先于调用证明，不能用最后的距离管倒推留域。

<a id="gri-proof"></a>
## 2. 正则化零点偏移与两种物理噪声管

取一个已存在 sε∈Sε，cε=v(sε)。完整 pair-monotonicity 作用于两个正则化零图点给

\[
-\epsilon\|v(s_\epsilon)-v(t_\epsilon)\|^2\ge0,
\]

故 cε 不依赖选择；全域 RI3 时 Sε 事实上是单点。与每个原零图点 (s,0) 比较又给

\[
\|c_\epsilon\|^2\le\langle c_\epsilon,v(s)\rangle,
\qquad \|c_\epsilon\|\le a.
\tag{RI4}
\]

这里 a 取 inf 即可，不要求最小值取得。实际原图值 -εcε∈F(sε) 的范数至多 εa<σ，所以 R-continuity **直接在固定真实值上**给

\[
s_\epsilon\in S+\rho(\epsilon\|c_\epsilon\|)\mathbb B,
\qquad d(s_\epsilon,S)\le\rho(\epsilon a).
\tag{RI5}
\]

RI5 不经过残差的 limsup，故不要求 ρ 在正点 εa 右连续。不要求给 S 的最近点：对固定 sε 的集合距离直接使用三角不等式即可；即使将 R-continuity 降成距离型界，也可用近极小锚。

置 q=(1+λε)⁻¹、Dk=||v(xk)−cε||、wk+1=v(hat xk+1)−cε。与正则化零锚比较得到

\[
\langle v(x_k)-c_\epsilon-(1+\lambda\epsilon)w_{k+1},w_{k+1}\rangle\ge0,
\quad \|w_{k+1}\|\le qD_k,
\]

因而

\[
D_k\le q^kD_0+\frac{L\delta(1-q^k)}{1-q}.
\]

若 RI3 在实际 xk 与 sε 上合法，则

\[
d(x_k,S)\le D_k/m+\rho(\epsilon a),
\quad
\boxed{\limsup_kd(x_k,S)\le
\frac{L\delta}{m}\left(1+\frac1{\lambda\epsilon}\right)+\rho(\epsilon a).}
\tag{RI6}
\]

全域 RI3 还可在真实精确物理输出上调用，使 RI6 的物理噪声项进一步降低：

\[
d(x_{k+1},S)
\le\delta+\|\widehat x_{k+1}-s_\epsilon\|+d(s_\epsilon,S)
\le\delta+qD_k/m+\rho(\epsilon a),
\]

于是

\[
\boxed{\limsup_kd(x_k,S)\le
\delta+\frac{L\delta}{m\lambda\epsilon}+\rho(\epsilon a).}
\tag{RI7}
\]

H 非平凡时，RI7 减 RI6 等于 δ(1−L/m)≤0，故全域情形可直接用 RI7。H={0} 时所有真实距离均为0，两条上界仍成立，不比较其预算大小。单步 hat 与 x 的物理误差 δ 应在回代后收费一次，不必把它放大为 Lδ/m。没有把误差后 xk 冒充原 F 的精确图点。

<a id="gri-combination"></a>
## 3. 与残差分支的最小值、双极限和先行范围

若 C216 的残差窗口亦合法，即

\[
b_{\epsilon,\delta}:=
\frac{L\delta(1+\lambda\epsilon)}{\lambda^2\epsilon}+\epsilon a<\sigma,
\]

则同一轨道、同一完整对象、同一 gauge 上可取两条已证估计的最小值：

\[
\boxed{\limsup_kd(x_k,S)\le
\min\left\{\delta+\rho(b_{\epsilon,\delta}+),
\ \delta+\frac{L\delta}{m\lambda\epsilon}+\rho(\epsilon a)\right\}.}
\tag{RI8}
\]

若仅 RI2 合法，RI7 仍可单独调用；不能强求较大的 bε,δ 也进 σ 窗。若仅 actual 逆门合法，用 RI6 替换 RI8 第二项。ρ(b+) 是 C216 的右上端点；RI7 的 ρ(εa) 无此 +，两者不能混淆。

固定 F,v,λ,m,L,ρ，对每个小 ε 各有一条无限合法 RI1 轨道。若 δ=δ(ε)→0 且 δ(ε)/ε→0，则 RI2 最终合法且 RI7→0，得到

\[
\lim_{\epsilon\downarrow0}\limsup_kd(x_k^{(\epsilon)},S)=0.
\tag{RI9}
\]

特别 δ=ε² 给 δ+Lε/(mλ)+ρ(εa)。这是轨道族双极限，不是一条逐步 εk→0 的算法。持续误差不保证物理点收敛或有限长度。

v=Id、m=L=1，且 F 极大单调时，Sε 的存在和 coverage 由标准强单调 resolvent 理论保证；RI7 恢复 [2606.01536v2 §3 Theorem 3](https://arxiv.org/html/2606.01536v2) 的原预算

\[
\delta(1+1/(\lambda\epsilon))+\rho(\epsilon a).
\tag{RI10}
\]

该先行源 §2 已明确 (1+α)⁻¹ 的强单调 resolvent 因子；故该因子和卷积不是本页创新。本页 RI7 的 warped 身份和 min 合并是已有桥的明确组合。源 2606.01536v1 的定理正文此次未成功获取；不能把已读 v2 的具体公式未经核对追溯到 June v1。此分支不宣称覆盖全部非单射核，也不替代 C216 在无逆控制时的原残差管。

## 4. 精确标量检验与不锐边界

令 H=R、v=Id、F(x)=μ(x−s)，μ>0；S={s}，ρ(t)=t/μ，a=|s|。sε=μs/(μ+ε)，p=(1+λ(μ+ε))⁻¹。合法轨道恰为

\[
x_{k+1}-s_\epsilon=p(x_k-s_\epsilon)+e_{k+1}.
\]

所有 |e|≤δ 的轨道满足

\[
\limsup_k|x_k-s|\le
\frac{\epsilon|s|}{\mu+\epsilon}
+\frac{\delta(1+\lambda(\mu+\epsilon))}{\lambda(\mu+\epsilon)}.
\tag{RI11}
\]

取恒定误差与 sε−s 同号（s=0 可取任意号），即有常值极限达到 RI11；这是该指定完整线性对象的**锐管**。它一般严格小于 RI7 和 C216，所以二者不声称逐对象最佳。真实精确输出的原图值还满足可取等的

\[
\limsup_k|f_{k+1}|\le
\frac{\mu\epsilon|s|}{\mu+\epsilon}
+\frac{\mu\delta}{\lambda(\mu+\epsilon)}.
\tag{RI12}
\]

RI11–12 来自显式递推，既不授予任意关系的锐性，也不以有限数值替代证明。可复算检查见 [stability_review.py](../code/gppa_novelty/stability_review.py)，独立敌对审查见 [stability_review.md](../novelty/2026_10_09/stability_review.md)。
