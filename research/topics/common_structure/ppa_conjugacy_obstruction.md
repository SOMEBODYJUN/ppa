# 保目标距离的原近端共轭无法恢复两类欧氏几何

<a id="ppa-conjugacy"></a>

固定步长 \(\lambda>0\)。以下两对完整单值原算子分别检验通常两点单调性和指定幂的真度量次正则性。每对都有全域唯一原根、相同的目标集、保目标距离且逐点固定目标的原近端共轭，并共享一组原 P1–P4 数据。因而这些观察不能单独决定两类性质。这里的共轭只指固定步长 \(HJ_1=J_2H\)，向量值仍在原欧氏度量下比较。

## 全剪切长度和解析共轭仍不决定两点单调

取 [C353](radial_shear_obstruction.md#shear-obstruction) 中的两种四维场
\[
 F_0(y)=dK_0y,\qquad F_1(y)=dK_{\|y\|^2}y,\qquad d>1/\lambda,quad S=\{0\}.
\]
其中 \(K_t=\cos(t)I+\sin(t)J\)，\(I,J\) 为反对易的正交复结构。两者完整残差都是 \(d\|y\|\)，且对全部实参数 \(\mu\) 的剪切长度都是 \(\sqrt{1+\mu^2d^2}\|y\|\)。原 RLEB 共同取 \(\omega(t)=t,\psi(s)=s/d,\kappa=1/(\lambda d)\) 以及任意正 \(R\)、真帽 \(\bar t\ge R/\lambda\) 和 \(U=X\)。第一图单调。第二图在每个正半径处的对称导数在 \(y\) 与 \(K'_{\|y\|^2}y\) 所张平面上有特征值 \(\pm d\|y\|^2\)，故任一原点邻域都含违反单调的割线。

额外地令 \(k=\sqrt{1+\lambda^2d^2}\) 及 \(Q_t=(\mathrm{Id}+\lambda dK_t)/k\)。\(Q_t\) 对实 \(t\) 正交，两条近端输入映射是 \(P_0(y)=kQ_0y\) 与 \(P_1(y)=kQ_{\|y\|^2}y\)，皆全域双射。定义
\[
 B_N(t)=Q_{t/k^2}Q_{t/k^4}\cdots Q_{t/k^{2N}} Q_0^{-N}.
\]
它等于按 \(j=1,\dots,N\) 排列的 \(Q_0^{j-1}Q_{t/k^{2j}}Q_0^{-j}\) 的积。每个因子与单位阵之差的范数在任一复紧集上一致为 \(O(k^{-2j})\)，因为 \(Q_t\) 整解析且 \(Q_0\) 正交。积的范数由 \(\prod_j(1+O(k^{-2j}))\) 一致控制，乘积差由剩余因子差的尾和控制，故 \(B_N\) 局部一致收敛到整矩阵函数 \(B\)。实轴上 \(B\) 正交，\(B(0)=\mathrm{Id}\)。从有限积直接得 \(B_N(k^2t)Q_0=Q_tB_{N-1}(t)\)，极限保持等式。于是
\[
 H(y)=B(\|y\|^2)y
\]
是保范数的全局实解析微分同胚，逆为 \(B(\|y\|^2)^\top y\)，并且 \(DH(0)=\mathrm{Id}\)。代入得到 \(HP_0=P_1H\)，取逆即得原近端共轭。与 C353 相比，此处还匹配了整个固定步长动力关系，且用的是切于恒等的解析换坐标。

## 精确目标距离与原非线性数据仍不决定真残差幂

取 \(X=\mathbb R^2,S=\{0\}\times\mathbb R\)，参数满足
\[
 0<\gamma_1<\gamma_2<1,\qquad \sigma>\gamma_2/\gamma_1,\qquad
 0<\alpha<1,\quad b>0.
\]
令 \(\phi(t)=\alpha t\min(t^{\sigma-1},1)\) 对 \(t\ge 0\)，并令 \(f(u)=\operatorname{sgn}(u)\phi(|u|)\)。对 \(\gamma=\gamma_1,\gamma_2\) 定义
\[
 J_\gamma(u,z)=(f(u),z+b|u|^\gamma),\qquad
 F_\gamma(y)=\lambda^{-1}(J_\gamma^{-1}(y)-y).
\]
\(f\) 是保序全域同胚，\(J_\gamma\) 也是全域同胚。公式确定完整连续单值原图，且原唯一近端恰为 \(J_\gamma\)，零集恰为 \(S\)。

对 \(x=(u,z)\) 及 \(y=J_\gamma(x)\)，若 \(t=|u|\le1\)，则
\[
 d(y,S)=\alpha t^\sigma,qquad
 \lambda r_{F_\gamma}(y)
 =\sqrt{(t-\phi(t))^2+b^2t^{2\gamma}}.
\]
因此 \(r_{F_\gamma}(y)\asymp t^\gamma\) 当 \(t\downarrow0\)。在任意正小零管内，以完整残差规定的幂界 \(d(y,S)\le C r_{F_\gamma}(y)^p\) 对某个有限 \(C\) 成立，当且仅当 \(0<p\le\sigma/\gamma\)。此结论在相对于任一零点的邻域也成立，因为表达式与切向坐标无关。

两图共享原 P1–P4。输入最近零点为 \((0,z)\)，且反射范数是
\(\sqrt{(2\phi(t)-t)^2+4b^2t^{2\gamma}}\)。由于 \(0\le\phi(t)\le t\)，两图同取
\[
 \omega(t)=t+2bt^{\gamma_1},\qquad
 B(t)=t+bt^{\gamma_1},\qquad
 \psi(s)=\alpha(\lambda s/b)^{\sigma/\gamma_2}.
\]
\(\lambda r_{F_\gamma}(y)\ge bt^{\gamma_2}\) 证 P3，而反射长度上界证 P2。先取任意固定 \(0<\kappa<1\) 与正 \(\bar t\)，再取同一 \(0<R\le1\) 足够小。因 \(\sigma\gamma_1/\gamma_2>1\)，有 \(\psi(B(t)/\lambda)/t\to0\)，故兼容在整个 \(0<t\le R\) 成立；缩小 \(R\) 也可使 \(B(R)/\lambda\le\bar t\)。两项幂都正，Dini 和有限。取 \(U=X\)，全部管内初值可用。单图最优反射幂是 \(\gamma\)，由反射第二分量给下界。

对 \(t\ge0\) 令
\[
 L_\gamma(t)=b\sum_{j\ge0}(\phi^{\circ j}(t))^\gamma.
\]
因为 \(\phi(t)\le\alpha t\)，这一级数局部一致收敛，并满足 \(L_\gamma(t)-L_\gamma(\phi(t))=bt^\gamma\)。因此
\[
 H(u,z)=(u,z+L_{\gamma_1}(|u|)-L_{\gamma_2}(|u|))
\]
是保 \(d(\cdot,S)\) 且逐点固定 \(S\) 的全域同胚。级数等式给出 \(HJ_{\gamma_1}=J_{\gamma_2}H\)。所有配对原轨道的目标距离序列完全相同。任取 \(p\in(\sigma/\gamma_2,\sigma/\gamma_1]\)，规定幂 \(p\) 的完整真残差界只在第一图成立。

## 限制的精确范围

如果候选及其恢复所用前提对相应共轭与所列保留数据全部不变，所声称的恢复就与对应反例冲突。第一项表明两点单调的恢复需要跨点的欧氏方向信息，即使在解析共轭下也如此。第二项表明保留精确目标距离仍不足以恢复完整残差的最优幂，换坐标可改变射向同一输出的完整原弦长度。若共轭在相关输入和输出上是双 Lipschitz，则完整原弦长度及到目标距离各自双侧可比，固定幂次正则性会随共轭转移。后一事实来自 \(\lambda r_F(y)=\inf_{x:\,y\in J_{\lambda F}(x)}\|x-y\|\)，无需纤维极小值达到。反例未排除记录这些欧氏信息、或辅助假设能区别两个对象的候选。公开优先性未判定。
