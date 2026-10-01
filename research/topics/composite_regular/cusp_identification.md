# 尖点外层：真多值图与一步局部识别

<a id="ci-object"></a>
## CI-OBJECT · 完整对象

在 \(\mathbb R^2\) 设 \(c(s,t)=t-(s_+)^2\)，\(S=c^{-1}(0)\)，取 \(\nu>0\) 与连续、严格递增、无界的 \(\eta:[0,\infty)\to[0,\infty)\)，\(\eta(0)=0\)。令
\[
\phi_\nu(z)=\nu|z|+\int_0^{|z|}\eta(u)\,du,\quad
f_\nu=\phi_\nu\circ c,\quad F_\nu=\partial f_\nu.
\]
有限凸外层与 \(C^{1,1}\) 满行秩内层给精确链式规则
\[
F_\nu(s,t)=(-2s_+,1)\partial\phi_\nu(c(s,t)).
\]
若 \(c\ne0\)，外层次梯度是单点 \(\operatorname{sign}(c)[\nu+\eta(|c|)]\)；若 \(c=0\)，为整段 \([-\nu,\nu]\)。故 \(F_\nu\) 在**每个** \(S\) 点真多值，且
\[
r_{F_\nu}(s,t)=
\begin{cases}
0,&c(s,t)=0,\\
[\nu+\eta(|c(s,t)|)]\sqrt{1+4s_+^2}\ge\nu,&c(s,t)\ne0.
\end{cases}
\]
因此 \(\operatorname{zer}F_\nu=S\)，不是某一个被选中的解。外层目标 \(C=\{0\}\) 的残差在零点为零、在非零点为 \(\nu+\eta(|z|)\)；例如 \(\Psi_\phi(q)=\eta^{-1}((q-\nu)_+)\) 是合法趋零 gauge 且给 \(d(z,C)\le\Psi_\phi(r_{\partial\phi_\nu}(z))\)。

<a id="ci-identify"></a>
## C40-v1 / CI-IDENTIFY · 明确的局部一步捕获门

任取 \(0<R<1/2\)，置
\[
M=\nu+\eta(R+R^2),\quad h=2M,\quad
r=\frac{R(1-2R)}4,
\]
再固定 \(\lambda>0\) 满足 \(\lambda h<1\)。对**每个**输入
\[
x\in B_{r/2}(0),\qquad
d(x,S)<\lambda\nu(1-\lambda h),
\]
由 [CS-PROX](../../canonical/composite_subregularity.md#cs-prox) 定义的 **\(B_R(0)\) 内唯一局部近端输出** \(y\) 必属于 \(S\)；以后按此局部近端规则的轨道停在 \(y\)。这里不声称完整 \(J_{\lambda F_\nu}(x)\) 的所有远端输出均相同。

**证明。** \(Dc=(-2s_+,1)\) 满行秩，\(\sigma_0=1,\beta=2\)；在闭球上 \(|c|\le R+R^2\)，故所有相关外层次梯度范数不超过 \(M\)。代入 CS-EB/CS-PROX 的半径与 hypomonotonicity 条件，得唯一球内近端输出 \(y\in B_r(0)\)，并由同图最近零点比较得
\[
\|x-y\|\le \frac{d(x,S)}{1-\lambda h}<\lambda\nu.
\]
近端包含式给 \((x-y)/\lambda\in F_\nu(y)\)，所以 \(r_{F_\nu}(y)\le\|x-y\|/\lambda<\nu\)。CI-OBJECT 的逐点残差式迫使 \(y\in S\)。因为 \(r<R/4\)，\(y\in B_{R/2}\)；且 \(0\in F_\nu(y)\)，同一个局部强凸近端问题对输入 \(y\) 有唯一输出 \(y\)。证毕。

这是一条**跳跃残差造成的识别**机制，不能解读成一般 \(\gamma<1\) RL 的新收敛定理。图多值、外层残差有间隙，但被认证的局部近端输出依然单值；这三个量词须分别保留。

<a id="ci-source"></a>
## 来源与未闭问题

历史 [复合模块 §5.3](../../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/C11复合次正则_定量模块与未解边界.md) 只给多值公式及“步残差小于 \(\nu\) 即识别”的观察。本页补齐曲面对象、闭球乘子预算、步长、输入半径及从实际近端步获得小残差的条件。状态 `derived-checked` 限于这些直接推导；外部 identifiable-manifold 先行性尚未核。本例满行秩，不推进秩亏开放问题。
