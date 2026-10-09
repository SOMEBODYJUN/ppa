# 一般模 GPPA 的误差传播：物理输出误差与核坐标误差分开

这是本库直接推导的条件定理，不是 arXiv:2608.01584v1 Theorem 4 的复述。该文考虑物理输出误差及正则化；本页吸收它的误差建模思想，但对固定完整关系给出不同的、明确受限的收缩管估计。持续误差不被写成精确点收敛。

<a id="gi-data"></a>
## 固定对象与所有假设

令 H 为实 Hilbert 空间，F:H⇉H 为固定完整关系，v:H→H 为单值核，λ>0。置

\[
Q=v(H),\quad A(z)=\bigcup_{v(x)=z}F(x),\quad
S=\operatorname{zer}F,\quad Z=v(S)=\operatorname{zer}A.
\tag{GI1}
\]

并集为空时 A(z)=∅。假设 Z 非空闭，R>0，Q_R={z∈Q:d(z,Z)≤R}。对每个 z∈Q_R，完整核近端

\[
J_{\lambda A}(z)=\{w:z-w\in\lambda A(w)\}
\]

非空单值，记 Tz；特别 Tz∈Q。存在 0<θ<1 以及连续非减 B:[0,R]→[0,∞)，B(0)=0，使全部 z∈Q_R 满足

\[
d(Tz,Z)\le\theta d(z,Z),\qquad
\|Tz-z\|\le B(d(z,Z)).
\tag{GI2}
\]

这两式可由核全对 RL、完整核真残差 EB、直接或能量兼容证书推出；本页明确将它们作为前件，不从算法名称猜测。若 B(t)=(t+ω(t))/2，ω 是反射模，就是本库的一般模接口。coverage 只在真实像集 Q 上要求，不要求 v 满射，不要求 Q 闭，也不要求核本身单调。

<a id="gi-tube"></a>
## C213：核输出误差的精确卷积与持续误差管

考虑全部满足

\[
z_{k+1}=Tz_k+e_k,\qquad z_{k+1}\in Q,\qquad
\|e_k\|\le E_k
\tag{GI3}
\]

的轨道。规定 E_k≥0，定义确定性包络

\[
D_0=d(z_0,Z),\qquad D_{k+1}=\theta D_k+E_k.
\tag{GI4}
\]

若 z_0∈Q_R 且每个 D_k≤R，则所有步骤可按 GI1–3 继续，且

\[
d(z_k,Z)\le D_k
=\theta^kD_0+\sum_{j=0}^{k-1}\theta^{k-1-j}E_j,
\quad
\|z_{k+1}-z_k\|\le B(D_k)+E_k.
\tag{GI5}
\]

证明：距离函数对误差是 1-Lipschitz，故 GI2–3 给 d(z_{k+1},Z)≤θd(z_k,Z)+E_k。由归纳得到 D_k 控制，因 D_k≤R，下一步完整 coverage 合法；实际 z_{k+1}∈Q 是独立前件，不能从小误差自动推得。展开 GI4 得卷积，三角不等式得步界。

若 E_k≤δ，且

\[
\max\{D_0,\delta/(1-\theta)\}\le R,
\tag{GI6}
\]

则 D_k≤θ^kD_0+δ(1−θ^k)/(1−θ)≤R，从而

\[
\limsup_{k\to\infty}d(z_k,Z)\le\delta/(1-\theta).
\tag{GI7}
\]

若 E_k→0，卷积趋零：对任意 ε>0，后段 E_j≤(1−θ)ε/2，有限前段乘 θ 的高次后小于 ε/2。因此 d(z_k,Z)→0。这个结论仍未给点收敛。

若另有

\[
\sum_{k=0}^{\infty}[B(D_k)+E_k]<\infty,
\tag{GI8}
\]

则核轨道有限长、Cauchy。Hilbert 完备给极限；由 GI8 可知 E_k→0，GI5 给距离趋零，闭 Z 给极限属于 Z。长度尾不超过对应 GI8 的尾和。仅有 ΣE_k<∞ **不能**对任意非线性 B 自动推出 GI8；实际包络的可和性须另查。

<a id="gi-physical"></a>
## 文献物理误差模型到本页的确切桥

原物理模型为

\[
\widehat x_{k+1}\in(v+\lambda F)^{-1}(v(x_k)),\quad
x_{k+1}=\widehat x_{k+1}+a_k.
\tag{GI9}
\]

若 GI1–2 已对同一完整 F,v 认证，并且核在这些实际点对满足

\[
\|v(\widehat x_{k+1}+a_k)-v(\widehat x_{k+1})\|
\le\tau(\|a_k\|)
\tag{GI10}
\]

其中 τ 非减，则 z_k=v(x_k)、e_k=v(x_{k+1})−v(\widehat x_{k+1}) 正好满足 GI3，E_k=τ(‖a_k‖)。确切性来自完整核纤维：v(\widehat x_{k+1})=Tz_k。没有声称误差后 x_{k+1} 本身仍是原关系的精确近端输出。

若 v 是双射，且其逆满足全域连续非减模 ρ、ρ(0)=0：

\[
\|v^{-1}(z)-v^{-1}(w)\|\le\rho(\|z-w\|),
\tag{GI11}
\]

则对每个 x、z=v(x)，用 Z 中的近极小锚并令误差趋零，得到

\[
d(x,S)\le\rho(d(z,Z)).
\tag{GI12}
\]

GI7 因而给

\[
\limsup_k d(x_k,S)\le
\rho\!\left(\frac{\tau(\delta_x)}{1-\theta}\right)
\tag{GI13}
\]

当 ‖a_k‖≤δ_x 且 GI6 对 δ=τ(δ_x) 成立。ρ 的连续性用于 limsup 与近极小锚；非连续 gauge 不能无说明地换到端点。

全域双 Lipschitz 情形 τ(t)=Lt、ρ(t)=Mt，GI13 的误差管半径为 MLδ_x/(1−θ)。核若 m-强单调，则 Cauchy–Schwarz 给 ‖x−y‖≤‖v(x)−v(y)‖/m；它不单独证明 v 的满射性或 coverage。

核点收敛及 GI11 给物理点收敛；物理有限长还需 Σρ(B(D_k)+E_k)<∞。当 ρ(t)=Mt，此条件由 GI8 自动得到。非单射核若只有指定截面，此物理结论只能授予该截面政策，不能授予完整 warped 纤维的所有选择。

<a id="gi-boundaries"></a>
## 不能升级的边界与反例

1. 持续误差只保证收缩管。H=R、F(x)=x、v=Id、λ=1 时 Tz=z/2。取 e_k=(−1)^kδ，z_0=0；精确解为 z_k=(2δ/3)[(−1)^{k−1}+(1/2)^k]，趋向两个不同的奇偶极限，故不点收敛且长度无限。距离的 limsup 是 2δ/3，满足 GI7 的上界 2δ；上界不宣称锐。
2. 不同的噪声模型有不同桥。输入误差 z_{k+1}=T(z_k+e_k) 需要在扰动输入处 coverage，递推为 θ[d(z_k,Z)+E_k]；它不是 GI3 的输出误差常数。
3. 本页没有把源稿 F+εv 的解偏移、正则化极限或非消失误差精确稳定性定理整体涵盖。要导入那些内容，须对每个正则化关系重新认证核图、零集、coverage 和模。文献中有用的思想已吸收，原定理的范围仍保持独立。
4. 这些估计是证明。有限脚本只复算卷积、反向代入及边界参数，不以大量 PASS 推出任意 F,v 的真值。
