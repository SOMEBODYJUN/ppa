# 正则化 GPPA 的持续误差：原关系残差的抵消估计与源 T4 包含

这是 C213 的独立正则化补充，固定一族 \(F+\epsilon v\)，不把它偷换成一条逐步变核或 \(\epsilon_k\) 变化的算法。外部比较为 [Le–Mordukhovich–Théra 2608.01584v1](https://arxiv.org/html/2608.01584v1) 的 Lemma 3 与 Theorem 4，归档原件与先前小技术门审查见[逐定理报告](../comparisons/2026_08_gppa_nfb/gppa_review.md)。新推导没有全球先行性认证。

<a id="grs-data"></a>
## 1. C216 的对象、域和全部前件

H 为实 Hilbert 空间。完整 \(F:H\rightrightarrows H\)，全域单值核 \(v:H\to H\) 全局 L-Lipschitz，\(L\ge0\)。要求全部原图点对满足
\[
\langle f-g,v(x)-v(y)\rangle\ge0.
\tag{RS1}
\]
固定 \(\lambda>0\)、\(\epsilon>0\)、\(\delta\ge0\)，且
\[
S=\operatorname{zer}F\ne\varnothing,
\quad S_\epsilon=\operatorname{zer}(F+\epsilon v)\ne\varnothing,
\quad a=\inf_{s\in S}\|v(s)\|.
\tag{RS2}
\]
F 的完整逆像在 0 满足源 R-continuity：存在 \(\sigma>0\)、非减 gauge \(\rho\)，\(\rho(0)=\rho(0+)=0\)，使全部 \(\|f\|<\sigma\) 有
\[
F^{-1}(f)\subset S+\rho(\|f\|)\mathbb B.
\tag{RS3}
\]
这强于仅距离界，并不要求 \(\rho\) 在正点右连续。考虑**每条已存在的**合法物理误差轨道
\[
v(x_k)-v(\widehat x_{k+1})
\in\lambda(F(\widehat x_{k+1})+\epsilon v(\widehat x_{k+1})),
\quad x_{k+1}=\widehat x_{k+1}+e_{k+1},
\quad\|e_{k+1}\|\le\delta.
\tag{RS4}
\]
若要保证任意初值和误差政策皆可继续，另加 \(\operatorname{ran}v\subset\operatorname{ran}(v+\lambda(F+\epsilon v))\)。RS2 的零点非空不自动给 coverage。下面的轨道条件定理本身不缺存在性假设。

<a id="grs-proof"></a>
## 2. 正则化零锚、核卷积与更紧原残差

取任意 \(s_\epsilon\in S_\epsilon\)，置 \(c_\epsilon=v(s_\epsilon)\)。RS1 作用于两个正则化零锚，给它们的核值相同，所以 \(c_\epsilon\) 不依赖选择。对每个原零点 s，RS1 作用于 \((s,0)\) 与 \((s_\epsilon,-\epsilon c_\epsilon)\) 给
\[
\|c_\epsilon\|^2\le\langle c_\epsilon,v(s)\rangle,
\quad\|c_\epsilon\|\le a.
\tag{RS5}
\]
此处取 inf 不要求最近零锚或 a 的最小值取得；a 有限，因为 S 非空且 v 全域有限。

置 \(q=(1+\lambda\epsilon)^{-1}\)、\(u_k=v(x_k)-c_\epsilon\)、\(w_{k+1}=v(\widehat x_{k+1})-c_\epsilon\)、\(D_k=\|u_k\|\)。RS4 给一个真实原关系值
\[
f_{k+1}=
\frac{v(x_k)-v(\widehat x_{k+1})}{\lambda}
-\epsilon v(\widehat x_{k+1})\in F(\widehat x_{k+1}).
\tag{RS6}
\]
RS1 与正则化零锚比较，恰为
\[
\langle u_k-(1+\lambda\epsilon)w_{k+1},w_{k+1}\rangle\ge0.
\tag{RS7}
\]
Cauchy–Schwarz 给 \(\|w_{k+1}\|\le qD_k\)，误差的全局向前模给
\[
D_{k+1}\le qD_k+L\delta,
\quad
D_k\le q^kD_0+\frac{L\delta(1-q^k)}{1-q}.
\tag{RS8}
\]
这就是 C213 的核卷积，但零锚为正则化零目标。

不能丢失 RS6 的抵消。展开平方并用 RS7 得
\[
\|u_k-(1+\lambda\epsilon)w_{k+1}\|^2
\le D_k^2-(1+\lambda\epsilon)^2\|w_{k+1}\|^2\le D_k^2.
\]
由于 RS6 等于
\((u_k-(1+\lambda\epsilon)w_{k+1})/\lambda-\epsilon c_\epsilon\)，所以
\[
\boxed{\ \|f_{k+1}\|\le D_k/\lambda+\epsilon a\ },
\quad
\limsup_k\|f_{k+1}\|\le
b_{\epsilon,\delta}:=
\frac{L\delta(1+\lambda\epsilon)}{\lambda^2\epsilon}+\epsilon a.
\tag{RS9}
\]
这一估计不要求 inverse kernel，不从物理误差后的 x_{k+1} 凭空生成精确原图值；原图值在真实精确输出 \(\widehat x_{k+1}\)。

<a id="grs-tube"></a>
## 3. 距离管、跳跃 gauge 与定量包含

若 \(b_{\epsilon,\delta}<\sigma\)，对每个 \(b_{\epsilon,\delta}<t<\sigma\)，RS9 保证最终 \(\|f_{k+1}\|\le t\)，RS3–4 给
\[
\limsup_k d(x_k,S)\le\delta+\rho(t).
\]
定义 \(\rho(b+)=\inf_{b<t<\sigma}\rho(t)\)，得到
\[
\boxed{\ \limsup_k d(x_k,S)
\le\delta+\rho(b_{\epsilon,\delta}+)\ }.
\tag{RS10}
\]
若 \(\rho\) 在 b 右连续，可以直接写 \(\rho(b)\)。仅原点右连续不能在正点省略 +。

源 T4 取 \(\delta=\epsilon^2\)，所以
\[
b_\epsilon=\frac{L\epsilon}{\lambda^2}
+\frac{L\epsilon^2}{\lambda}+\epsilon a.
\tag{RS11}
\]
源印刷 residual 预算是
\[
B_\epsilon=\frac{4L\epsilon}{\lambda^2}
+\frac{3L\epsilon^2}{\lambda}+\epsilon a.
\tag{RS12}
\]
当 \(L>0\)，\(B_\epsilon-b_\epsilon=3L\epsilon/\lambda^2+2L\epsilon^2/\lambda>0\)。因此 \(B_\epsilon<\sigma\) 时可直接取 t 为 B，恢复源原印结论 \(\epsilon^2+\rho(B_\epsilon)\)，**无须**正点右连续。取中间预算 \(t_\epsilon=(b_\epsilon+B_\epsilon)/2\) 还得到更小的同 gauge 有效预算；因 gauge 可能有平台，最终距离上界不声称总是严格更小。

当 \(L=0\)，v 恒为 c，RS4 直接给 \(f_{k+1}=-\epsilon c\)，\(a=\|c\|\)，所以只需 \(\epsilon a<\sigma\) 即有 \(d(x_k,S)\le\delta+\rho(\epsilon a)\)（k≥1），不需要正点连续，也不依赖不存在的严格预算裕度。

对每个小 \(\epsilon\) 各有一条 RS4 合法轨道并保持同一个 F,v,\(\lambda,\rho\) 时，由 RS11→0 与 \(\rho(0+)=0\)，
\[
\lim_{\epsilon\downarrow0}\limsup_k d(x_k^{(\epsilon)},S)=0.
\tag{RS13}
\]
这闭合源 T4 的正则化双极限距离输出和所有合法物理误差轨道的包含门；若需要全部初值存在，保留原 coverage 门。不能从 RS13 改写成单条逐步 \(\epsilon_k\downarrow0\) 轨道的结论。

<a id="grs-boundaries"></a>
## 4. 不能升级的结论与检验

源 T4 的正则化机制已明确接入；源 T1 的全部一般非单射结论、任意变核、不同的升维表示及其它论文的完整范围没有因此自动包含。本定理允许持续物理误差，结论是原零集距离管及正则化双极限；没有精确物理点收敛或有限长度承诺。C197 的核纤维振荡和 C213 的交替持续误差仍是有效边界。

相较源印预算，RS11 更紧，但它由相同前件和一个抵消恒等式推得；这不是全球新颖性证据，也不足以称整篇框架在任意表示下严格更好。严格性、价值和先行性分别评价。

[有限验证与参数](../code/gppa_scope/README.md)包括有理数反代、抵消平方身份、非单射核下的合法原图值、偏移零点、恒定核、零误差、持续及交替误差和 gauge 正点跳跃；一般量词由上述证明承担。
