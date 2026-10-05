# 一般模的局部动力学：Dini 长度、对数接缝与连续回缩

本页补全 C09、C10、C11 的规范证明。C09/C11 固定同一局部图块和其唯一近端映射；C10 另给一张完整双支关系，其完整近端由全部纤维反演。历史 TeX 只作末尾溯源，不补正文前提。这里的 \(X=\mathbb R^n\) 使用 Euclidean 范数；没有将量词扩大为任意 Hilbert 空间。

<a id="gm-data"></a>
## 1. C09/C11 的共同对象与全部局部门

固定关系 \(F:X\rightrightarrows X\)、非空闭集 \(S\subset F^{-1}(0)\)、图块 \(\mathcal G\subset\operatorname{gph}F\)、开集 \(U\subset X\)，以及

\[
\lambda>0,\quad R>0,\quad\bar t>0,\quad0<\kappa<1.
\]

不要求 \(S=F^{-1}(0)\)，不要求 \(\mathcal G=\operatorname{gph}F\)。定义

\[
J_{\lambda F}(x)=\{u:x-u\in\lambda F(u)\},\qquad
J_{\mathcal G}(x)=\{u:(u,(x-u)/\lambda)\in\mathcal G\},
\]
\[
r_F(u)=\inf_{v\in F(u)}\|v\|,\qquad
U_R=\{x\in U:d(x,S)\le R\},\qquad
D_U(x)=d(x,X\setminus U).
\tag{GM1}
\]

约定空集距离为 \(+\infty\)，故 \(U=X\) 时 \(D_U\equiv+\infty\)。因为 \(S\) 在有限维空间中非空闭，每个 \(P_S(x)\) 非空：最近点极小序列可限制在一个有界闭球内并抽收敛子列。

以下前件须在**同一** \(F,S,\mathcal G,U,\lambda,R\) 上同时成立。

1. **输入与零锚覆盖。** 对每个 \(x\in U_R\)，\(J_{\mathcal G}(x)\ne\varnothing\)，且存在 \(p\in P_S(x)\) 满足 \((p,0)\in\mathcal G\)。最近点可依 \(x\) 改变，不要求连续选取。
2. **全对一般模。** \(\omega:[0,R]\to[0,\infty)\) 连续非减，\(\omega(0)=0\)。对每对 \((u,v),(u',v')\in\mathcal G\)，只要输入对距离 \(\delta=\|(u+\lambda v)-(u'+\lambda v')\|\le R\)，就有
   \[
   \|(u-\lambda v)-(u'-\lambda v')\|\le\omega(\delta).
   \tag{GM2}
   \]
   同输入 \(\delta=0\) 也在量词内，跨支图点也须比较。
3. **真实输出 EB 与评价域。** \(\psi:[0,\bar t]\to[0,\infty)\) 非减，\(\psi(0)=0\)，在 0 右连续。对每个 \(y\in J_{\mathcal G}(U_R)\) 且 \(r_F(y)\le\bar t\)，
   \[
   d(y,S)\le\psi(r_F(y)),\qquad
   \frac{R+\omega(R)}{2\lambda}\le\bar t.
   \tag{GM3}
   \]
   \(r_F\) 对完整 \(F(y)\) 取最小下确界，不是对图块或所选图值取范数。
4. **同尺度直接兼容。** 对每个 \(0<t\le R\)，
   \[
   \psi\!\left(\frac{t+\omega(t)}{2\lambda}\right)\le\kappa t.
   \tag{GM4}
   \]
5. **Dini 条件。**
   \[
   \int_0^R\frac{\omega(t)}t\,dt<\infty.
   \tag{GM5}
   \]

(GM2) 在同输入的两图点上给 \(u-u'+\lambda(v-v')=0\) 与 \(u-u'-\lambda(v-v')=0\)，所以 \(u=u',v=v'\)。因此 \(J_{\mathcal G}\) 在其自然输入域单值，前件 1 才进一步保证其在整个 \(U_R\) 有定义。以下记 \(T=J_{\mathcal G}|_{U_R}\)；不从单值性推导 coverage。

<a id="gm-one-step"></a>
## 2. 同图块的一步估计及残差域核验

取任意 \(x\in U_R\)，令 \(x^+=Tx\)、\(d=d(x,S)\)、\(d^+=d(x^+,S)\)、\(s=\|x^+-x\|\)。由前件 1 取最近零锚 \(p\)。置
\(a=x^+-p\)、\(b=x-x^+\)，则 \(a+b=x-p\)，且输入点对距离正是 \(d\le R\)。把同图块的近端点 \((x^+,b/\lambda)\) 与 \((p,0)\) 代入 (GM2)，得 \(\|a-b\|\le\omega(d)\)。平行四边形恒等式及 \(d^+\le\|a\|\) 给

\[
(d^+)^2+s^2\le\frac{d^2+\omega(d)^2}{2}.
\tag{GM6}
\]

反三角不等式又给
\(|2s-d|=|\|2b\|-\|a+b\||\le\|b-a\|\)，故

\[
(2s-d)^2\le\omega(d)^2,\qquad
s\le h_\omega(d):=\frac{d+\omega(d)}2.
\tag{GM7}
\]

真实残差及**所选图值**同时满足

\[
0\le r_F(x^+)\le\|b/\lambda\|=s/\lambda
\le\frac{d+\omega(d)}{2\lambda}
\le\frac{R+\omega(R)}{2\lambda}\le\bar t.
\tag{GM8}
\]

所以 (GM3) 的残差门已验证，\(\psi\) 的每次评价也在定义域内。单调性才允许从真正残差转到所选值：

\[
d^+\le\psi(r_F(x^+))\le\psi(s/\lambda)
\le\psi\!\left(\frac{d+\omega(d)}{2\lambda}\right)
\le\kappa d.
\tag{GM9}
\]

最后一步在 \(d>0\) 用 (GM4)。若 \(d=0\)，闭性给 \(x\in S\)，最近点只能是 \(p=x\)，(GM7) 强制 \(s=0\)，所以 \(Tx=x\)、\(d^+=0\)；不需要把正参数兼容式硬代入 0。

以上只要求输入 \(x\) 属于 \(U_R\)；还没有假设输出仍在 \(U\)。留域将在下文由预算证明，不以循环假设使用下一步 coverage。

<a id="gm-dini-length"></a>
## 3. Dini 与几何采样的等价、连续长度函数

对任意固定 \(0<r\le R\)、\(0<\theta<1\) 和每个整数 \(j\ge0\)，\(\omega\) 非减给

\[
\log(1/\theta)\,\omega(\theta^{j+1}r)
\le\int_{\theta^{j+1}r}^{\theta^jr}\frac{\omega(t)}t\,dt
\le\log(1/\theta)\,\omega(\theta^jr).
\tag{GM10}
\]

有限求和后令上限趋无穷，即使两边可能无穷也保持单调极限。因此

\[
\int_0^R\frac{\omega(t)}t\,dt<\infty
\quad\Longleftrightarrow\quad
\sum_{j=0}^\infty\omega(\theta^jr)<\infty
\tag{GM11}
\]

对每个固定 \((r,\theta)\) 成立。反向由级数得 \(\int_0^r<\infty\)，剩余积分 \(\int_r^R\le\omega(R)\log(R/r)\) 有限；初项 \(\omega(r)\) 有限，所以下界漏掉第 0 项不影响等价。故“存在一个 \((r,\theta)\)”也等价于“每个 \((r,\theta)\)”。不要求 \(\omega\) 凹或严格递增。

以后固定动力学中的 \(\theta=\kappa\)，定义

\[
\ell_\omega(r)=\sum_{j=0}^\infty h_\omega(\kappa^jr)
=\frac{r}{2(1-\kappa)}+\frac12\sum_{j=0}^\infty\omega(\kappa^jr),
\qquad0\le r\le R.
\tag{GM12}
\]

各项 \(\omega(\kappa^jr)\le\omega(\kappa^jR)\)，后者级数由 (GM11) 可和。故定义级数在整个 \([0,R]\) 一致收敛；有限部分连续，极限连续。\(\ell_\omega\) 非减、\(\ell_\omega(0)=0\)、\(\ell_\omega(r)\to0\) 当 \(r\downarrow0\)，并有**精确恒等式**

\[
\boxed{\ell_\omega(r)=h_\omega(r)+\ell_\omega(\kappa r).}
\tag{GM13}
\]

结合 (GM7)、(GM9) 与 \(\ell_\omega\) 非减，实际一步满足

\[
\boxed{s+\ell_\omega(d^+)\le
h_\omega(d)+\ell_\omega(\kappa d)=\ell_\omega(d).}
\tag{GM14}
\]

等号属于长度**上界函数**的递推；没有把实际步长 \(s\le h_\omega(d)\) 宣称为等号。后文的开域不变性正由这项剩余预算给出。

<a id="gm-dini-theorem"></a>
## 4. C09：严格预算下的唯一图块轨道

- **Status**：`derived-checked`，范围为 §1 的同一图块及全部前件。
- **精确命题**：若 \(x^0\in U\)、\(d_0=d(x^0,S)\le R\)，且

\[
\ell_\omega(d_0)<D_U(x^0),
\tag{GM15}
\]

则唯一图块轨道 \(x^{k+1}=Tx^k\) 对全部整数 \(k\ge0\) 存在、留在 \(U_R\)，并有

\[
d_k:=d(x^k,S)\le\kappa^kd_0,\qquad
s_k:=\|x^{k+1}-x^k\|\le h_\omega(\kappa^kd_0),
\tag{GM16}
\]
\[
\sum_{j=0}^{N-1}s_j+\ell_\omega(d_N)\le\ell_\omega(d_0)
\quad(N\ge0),\qquad
\sum_{j=0}^\infty s_j\le\ell_\omega(d_0).
\tag{GM17}
\]

轨道收敛到某个 \(x^\infty\in S\cap U\)，且每个 \(k\ge0\) 满足

\[
\|x^\infty-x^k\|\le\sum_{j=k}^\infty s_j
\le\ell_\omega(d_k)\le\ell_\omega(\kappa^kd_0)
=\frac12\left[\frac{\kappa^kd_0}{1-\kappa}
+\sum_{j=k}^\infty\omega(\kappa^jd_0)\right].
\tag{GM18}
\]

**留域和存在性的逐步证明。** 初值已在 \(U_R\)，coverage 给唯一下一点；(GM9) 给其距离不超过 \(\kappa d_0\)。假设已合法构造到 \(x^k\in U_R\)。下一点由 coverage 存在，应用 (GM14) 并逐步求和，得

\[
\sum_{j=0}^k s_j+\ell_\omega(d_{k+1})\le\ell_\omega(d_0).
\]

所以 \(\|x^{k+1}-x^0\|\le\ell_\omega(d_0)<D_U(x^0)\)。这说明 \(x^{k+1}\in U\)；同时 (GM9) 给 \(d_{k+1}\le\kappa d_k\le R\)，从而下一轮 coverage 合法。若 \(U=X\)，留域自动成立，而 \(\ell_\omega\) 仍须由 Dini 保证有限。归纳给全部轨道、(GM16) 和有限版 (GM17)。

步长级数有界使轨道 Cauchy；Euclidean 完备性给极限。\(d_k\to0\) 与闭 \(S\) 给 \(x^\infty\in S\)。又
\(\|x^\infty-x^0\|\le\ell_\omega(d_0)<D_U(x^0)\)，所以极限也在 \(U\)。将 (GM14) 从 \(k\) 求至任意后续时间并丢掉非负末项，或从 \(k\) 重新使用同一几何上界，得到 (GM18)。

**完整近端的边界。** 此命题唯一性属于 \(J_{\mathcal G}\)。把同一轨道直接转为完整近端的一个充分门，是另证所有相关可达输入上的完整纤维等式 \(J_{\lambda F}(x)=\{Tx\}\)；它不是 C09 的已有前件。其它允许多输出的完整收敛版本须独立证明，本页不把该等式称为一切完整收敛定理的必要条件。下面 C11 只使用同一个 \(T\)，无需增加这项等式，也无需把 \(S\) 改成完整零集。

<a id="gm-retraction"></a>
## 5. C11：开域、前向不变、统一尾与连续回缩

- **Status**：`derived-checked`，对象与前件完全沿用 §1。
- **精确开域**：

\[
\mathcal O=\{x\in U:d(x,S)<R,\ \ell_\omega(d(x,S))<D_U(x)\}.
\tag{GM19}
\]

则 \(\mathcal O\) 开，\(S\cap U\subseteq\mathcal O\)，且 \(T(\mathcal O)\subseteq\mathcal O\)。每个 \(x\in\mathcal O\) 的图块轨道极限定义一个连续回缩

\[
\Pi:\mathcal O\longrightarrow S\cap U,\qquad
\Pi(x)=\lim_{k\to\infty}T^kx,\qquad
\Pi(p)=p\quad(p\in S\cap U).
\tag{GM20}
\]

这里的“回缩”只说连续且在目标子空间上为恒等，不额外声称 \(\mathcal O\) 对 \(S\cap U\) 有强形变回缩。

**开性及包含。** 若 \(U\ne X\)，\(D_U\) 是有限 1-Lipschitz 函数。距离到 \(S\) 连续，\(\ell_\omega\) 连续，因此 (GM19) 的两个严格不等式定义开集。若 \(U=X\)，第二不等式自动成立，\(\mathcal O=\{d(x,S)<R\}\) 也开。对每个 \(p\in S\cap U\)，\(d(p,S)=0\)、\(\ell_\omega(0)=0<D_U(p)\)，故 \(p\in\mathcal O\)。这也涵盖 \(S\cap U=\varnothing\) 时的空集结论。

**前向不变不能只靠粗总长界。** 取 \(x\in\mathcal O\)，记 \(d,d^+,s\) 如 §2。已有 \(d^+\le\kappa d<R\)。若 \(U\ne X\)，距离函数的 Lipschitz 性和精确预算递推给

\[
\begin{aligned}
D_U(Tx)&\ge D_U(x)-s
>\ell_\omega(d)-s\\
&\ge\ell_\omega(d)-h_\omega(d)
=\ell_\omega(\kappa d)
\ge\ell_\omega(d^+).
\end{aligned}
\tag{GM21}
\]

右侧非负，故 \(D_U(Tx)>0\) 还同时证明 \(Tx\in U\)。两项严格不等式即 \(Tx\in\mathcal O\)。\(U=X\) 时只需距离收缩即可。没有先假定输出留在 \(U\) 再调用其正距离。

**同一图块的连续性。** 对任意 \(x,y\in U_R\) 且 \(\delta=\|x-y\|\le R\)，(GM2) 与平行四边形恒等式给

\[
\|Tx-Ty\|^2+\|(x-Tx)-(y-Ty)\|^2
\le\frac{\delta^2+\omega(\delta)^2}{2}.
\tag{GM22}
\]

所以 \(\|Tx-Ty\|\le m_\omega(\delta)\)，其中
\(m_\omega(t)=\sqrt{(t^2+\omega(t)^2)/2}\to0\)。这已足以证明 \(T\) 在 \(U_R\) 的相对连续性，尤其在开域 \(\mathcal O\) 连续；不需把 \(\delta\le R\) 误作全部远距离对的估计。由前向不变，每个有限迭代 \(T^k:\mathcal O\to\mathcal O\) 都连续。

**全部初值上的共同尾。** C09 给每个 \(x\in\mathcal O\) 的极限于 \(S\cap U\)；因 \(d(x,S)<R\)，(GM18) 给

\[
\sup_{x\in\mathcal O}\|T^kx-\Pi(x)\|
\le\ell_\omega(\kappa^kR)\longrightarrow0.
\tag{GM23}
\]

这在整个可能无界的 \(\mathcal O\) 上一致，无须紧化初值域。为直接核连续性，给定 \(x\in\mathcal O\)、\(\varepsilon>0\)，先取 \(k\) 使两项尾各小于 \(\varepsilon/3\)，再由该固定 \(T^k\) 的连续性令 \(y\) 充分接近 \(x\)，使中间项 \(\|T^kx-T^ky\|<\varepsilon/3\)。三角不等式得到 \(\|\Pi(x)-\Pi(y)\|<\varepsilon\)。最后，§2 已证每个 \(p\in S\cap U\) 满足 \(Tp=p\)，所以 \(\Pi p=p\)，证明 (GM20)。

<a id="gm-local-contractibility"></a>
### 局部可缩的精确量词与显式同伦

令 \(A=S\cap U\)。对每个 \(p\in A\) 和每个 \(A\) 中含 \(p\) 的相对邻域 \(V\)，存在更小的相对邻域 \(W\subseteq V\)，以及连续映射

\[
H:[0,1]\times W\to V,\qquad
H(0,x)=x,\quad H(1,x)=p,\quad H(t,p)=p.
\tag{GM24}
\]

这精确表示包含映射 \(W\hookrightarrow V\) 在 \(V\) 内同伦于常值；没有断言可以让所有中间像都留在 \(W\)。

证明不需导入拓扑定理。取相对开集 \(V_0\) 使 \(p\in V_0\subseteq V\)。\(\Pi\) 连续且 \(\Pi(p)=p\)，所以可取 \(\epsilon>0\)，使 Euclidean 球 \(B(p,\epsilon)\subset\mathcal O\)，且 \(\Pi(B(p,\epsilon))\subset V_0\)。令 \(W=A\cap B(p,\epsilon/2)\)。对 \(x\in W\)，线段 \((1-t)x+tp\) 留在 \(B(p,\epsilon)\)，于是

\[
H(t,x)=\Pi((1-t)x+tp)
\tag{GM25}
\]

满足 (GM24)。因 \(\Pi x=x\)，\(W\subset V_0\)，故确为所需较小邻域。\(\mathcal O\) 是 \(A\) 的 Euclidean 开邻域，(GM20) 又是回缩，因此 \(A\) 是 Euclidean neighborhood retract。此结论来自整个局部假设的合取，不否定另一个定理在缺少这些前件时实现任意紧零集；若某零集在一点不满足 (GM24)，整套 C09/C11 前件就不能在该点的上述开域中同时成立。

<a id="gm-log-object"></a>
## 6. C10：每个正参数的完整对数双支关系

- **Status**：`derived-checked`，范围为每个固定 \(a>0\) 的以下完整关系、步长 1 和 Euclidean \(\mathbb R^2\)。
- **完整剖面**：置 \(r_a=e^{-a}\)，定义

\[
\ell_a(0)=0,\qquad
\ell_a(t)=[\log(e/t)]^{-a}\quad(0<t\le r_a),
\]
\[
\ell_a(t)=\frac{1+a e^a t}{(a+1)^{a+1}}\quad(t\ge r_a).
\tag{GM26}
\]

第二式正是接点的切线：\(\ell_a(r_a)=(a+1)^{-a}\)、\(\ell_a'(r_a)=a e^a/(a+1)^{a+1}\)。在 \((0,r_a]\)，

\[
\ell_a'(t)=\frac{a}{t[\log(e/t)]^{a+1}}>0,\qquad
\ell_a''(t)=\frac{a\,[a+1-\log(e/t)]}{t^2[\log(e/t)]^{a+2}}\le0.
\tag{GM27}
\]

接点左右一阶导数相同，右侧导数保持该正值；所以 \(\ell_a\) 全域连续、严格递增、凹、无界。0 处连续来自对数趋无穷，凹性由正半轴凹性取极限延至 0。对非负 \(u,v\)，凹性与 \(\ell_a(0)=0\) 给
\(\ell_a(u)\ge u\ell_a(u+v)/(u+v)\)、\(\ell_a(v)\ge v\ell_a(u+v)/(u+v)\)（\(u+v=0\) 单独平凡），相加得到次可加性。因此

\[
\ell_a(u+v)\le\ell_a(u)+\ell_a(v),\qquad
|\ell_a(u)-\ell_a(v)|\le\ell_a(|u-v|)\quad(u,v\ge0).
\tag{GM28}
\]

这里次可加性用的是完整切线延伸后的凹性；不能只核对数公式局部后直接用于任意远处点对。

定义完整关系

\[
F_a(\xi,y)=
\begin{cases}
\{(-\ell_a(4y),3y),\ (-\ell_a(4y),-5y)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}
\tag{GM29}
\]

每支是连续函数在闭半平面上的图，有限并仍闭；\(y>0\) 两值不同，\(y=0\) 两值同为零。因此 \(S_a=F_a^{-1}(0)=\mathbb R\times\{0\}\)。

<a id="gm-log-prox"></a>
### 完整近端、跨支全对模与非幂见证

对任意输入 \((p,q)\in\mathbb R^2\)，两支近端方程分别为

\[
(p,q)=(\xi-\ell_a(4y),4y),\qquad
(p,q)=(\xi-\ell_a(4y),-4y),\qquad y\ge0.
\]

第一支恰处理 \(q\ge0\)，第二支恰处理 \(q\le0\)；\(q=0\) 时两者给同一输出。因此全部纤维反演得全域单值**完整**近端

\[
J_a(p,q)=J_{F_a}(p,q)=\left(p+\ell_a(|q|),\frac{|q|}{4}\right),
\qquad
C_a=2J_a-I=\left(p+2\ell_a(|q|),\frac{|q|}{2}-q\right).
\tag{GM30}
\]

对任意两个输入 \(z=(p,q),z'=(p',q')\)，令 \(\delta=\|z-z'\|\)。由 (GM28)，
\(|\ell_a(|q|)-\ell_a(|q'|)|\le\ell_a(||q|-|q'||)\le\ell_a(\delta)\)。故反射的横、纵差分别不超过 \(\delta+2\ell_a(\delta)\) 和 \(3\delta/2\)。于是

\[
\|C_az-C_az'\|\le\Omega_a(\delta),\qquad
\Omega_a(t)=\sqrt{(t+2\ell_a(t))^2+\frac94t^2}.
\tag{GM31}
\]

(GM30) 已覆盖每一个图点，所以 (GM31) 等价于完整 \(F_a\) 在 \(\lambda=1\) 的全部图点对一般模 RL，包括跨正负输入两支。\(\Omega_a\) 连续非减、在零处消失。

当 \(t\downarrow0\)，\(t/\ell_a(t)\to0\)，故 \(\Omega_a(t)\sim2\ell_a(t)\)。对每个 \(\gamma>0\)，\(\ell_a(t)/t^\gamma\to\infty\)，所以 \(\Omega_a\) 没有局部正幂上界。还可直接验证此图没有被该上界遮住的更好幂模：输入 \((0,t),(0,0)\) 的反射差为 \((2\ell_a(t),-t/2)\)，范数至少 \(2\ell_a(t)\)。因此任何声称同一完整图全对 \(Ct^\gamma\) 的有限 \(C\) 都在这条趋零输入对上失败。

代换 \(u=\log(e/t)\) 得

\[
\int_0^{r_a}\frac{\ell_a(t)}t\,dt
=\int_{a+1}^{\infty}u^{-a}\,du,\qquad
\int_0^{r_a}\frac{\Omega_a(t)}t\,dt<\infty
\quad\Longleftrightarrow\quad a>1.
\tag{GM32}
\]

后一个等价用 \(\Omega_a\sim2\ell_a\)；远离 0 的有限积分不影响 Dini 判别。

<a id="gm-log-residual"></a>
### 真最小残差、精确 gauge 与小尺度兼容

两支图值平方范数依次为 \(\ell_a(4y)^2+9y^2\)、\(\ell_a(4y)^2+25y^2\)，故

\[
r_{F_a}(\xi,y)=
\begin{cases}
\chi_a(y):=\sqrt{\ell_a(4y)^2+9y^2},&y\ge0,\\
+\infty,&y<0.
\end{cases}
\qquad \psi_a=\chi_a^{-1}:[0,\infty)\to[0,\infty).
\tag{GM33}
\]

\(\chi_a\) 连续严格递增、零处为零且 \(\chi_a(y)\ge3y\to\infty\)，所以该逆函数存在并连续严格递增。在有限残差域 \(y\ge0\) 上，

\[
d((\xi,y),S_a)=y=\psi_a(r_{F_a}(\xi,y)).
\tag{GM34}
\]

域外残差为 \(+\infty\)，不向只有有限参数定义域的 gauge 代入无穷。负输入 \(q<0\) 的选中近端图值在第二支，但完整最小残差仍由第一支取得；两者不能相等替换。

对每个固定 \(\kappa\in(1/4,1)\)，存在 \(R_*>0\)，使

\[
\psi_a\!\left(\frac{r+\Omega_a(r)}2\right)\le\kappa r
\qquad(0<r\le R_*).
\tag{GM35}
\]

这里给出可核的充分比较，不靠省略的渐近反演。置 \(c=4\kappa>1\)、\(L=\log(e/r)\)，先令 \(r\) 小到 \(cr\le r_a\)。由积分形式的均值公式，

\[
\ell_a(cr)-\ell_a(r)
=a\int_{L-\log c}^{L}u^{-a-1}\,du
\ge a\log(c)L^{-a-1}>0.
\]

而 \(\sqrt{A^2+B}\le A+B/(2A)\) 给

\[
\frac{r+\Omega_a(r)}2
\le\ell_a(r)+r+\frac{9r^2}{32\ell_a(r)}.
\]

因 \(rL^{a+1}\to0\)、\(r^2L^{2a+1}\to0\)，可以选同一个 \(R_*\)，使最后两项之和不超过 \(a\log(c)L^{-a-1}\) 对全部 \(0<r\le R_*\) 成立。于是
\((r+\Omega_a(r))/2\le\ell_a(cr)\le\chi_a(\kappa r)\)，应用递增逆函数即得 (GM35)。

这说明每个 \(a>0\) 都有同图块兼容的小尺度证书。若需按 §1 的有限 gauge 域记录，可预取任意 \(\bar t>0\)，再缩小 \(R\le R_*\) 到 \((R+\Omega_a(R))/2\le\bar t\)，并限制 \(\psi_a\) 到 \([0,\bar t]\)。全图取作图块、\(U=\mathbb R^2\) 时 coverage 与零锚自动成立。只有 \(a>1\) 才同时满足 Dini；\(a\le1\) 时不能调用 C09 的有限长度结论。

<a id="gm-log-dynamics"></a>
### 全初值轨道与 \(a=1\) 边界

给任意 \(z^0=(p_0,q_0)\)，令 \(r_0=|q_0|\)。完整近端 (GM30) 逐步给

\[
|q_k|=r_k:=4^{-k}r_0,\qquad
p_k=p_0+\sum_{j=0}^{k-1}\ell_a(r_j).
\tag{GM36}
\]

\(q_k\ge0\) 对 \(k\ge1\) 成立；\(q_0\) 可正可负。\(r_0=0\) 时轨道恒定。若 \(r_0>0\)，对每一步到完整零集距离都精确乘 \(1/4\)。

每步长度为 \(\sqrt{\ell_a(r_k)^2+(q_{k+1}-q_k)^2}\)，下界为横向增量 \(\ell_a(r_k)\)，上界为该增量加垂向变差。若 \(q_0\ge0\)，垂向总变差为 \(r_0\)；若 \(q_0<0\)，首步变差是 \(5r_0/4\)，其后为 \(3r_k/4\)，总和 \(3r_0/2\)。因此

\[
\sum_{k\ge0}\|z^{k+1}-z^k\|<\infty
\quad\Longleftrightarrow\quad
\sum_{k\ge0}\ell_a(4^{-k}r_0)<\infty.
\tag{GM37}
\]

对任意 \(r_0>0\)，选整数 \(K\) 使 \(4^{-K}r_0\le r_a\)。从 \(k\ge K\) 起，

\[
\ell_a(4^{-k}r_0)
=[\log(e/r_0)+k\log4]^{-a},
\tag{GM38}
\]

括号此时至少为 \(a+1>0\)。有限的初始切线段不影响求和；正项级数 (GM38) 恰在 \(a>1\) 收敛。因此，对于每个 \(r_0>0\)，轨道有限长且收敛到 \(S_a\) 中一点当且仅当 \(a>1\)；若 \(0<a\le1\)，\(p_k\to+\infty\)，尽管 \(d(z^k,S_a)=4^{-k}r_0\to0\)。尤其 \(a=1\) 是发散的调和边界，不属于有限长一侧。

当 \(a>1\)，令 \(A_k=\log(e/r_0)+k\log4\)，则最终 \(A_k>0\)，递减函数的积分夹逼给

\[
\sum_{j=k}^\infty A_j^{-a}
\sim\int_k^\infty[\log(e/r_0)+t\log4]^{-a}\,dt
=\frac{A_k^{1-a}}{(a-1)\log4}.
\]

上下夹逼的误差至多首项 \(A_k^{-a}\)，与所写积分之比趋零。垂向 \(r_k\) 指数趋零，相对于该多项式对数尾可忽略，所以完整点尾满足

\[
\|z^\infty-z^k\|
\sim\frac{[\log(e/r_0)+k\log4]^{1-a}}{(a-1)\log4}.
\tag{GM39}
\]

此族证明“集合距离几何下降”不够推出点收敛，并显示此族的 Dini 门槛恰为 \(a>1\)。它不证明任意非 Dini 模、任意关系或任意路径都会发散。

<a id="gm-audit-source"></a>
## 7. 已闭义务、身份边界与来源

| 命题/义务 | 本页证据与范围 |
| --- | --- |
| C09 一步及 gauge 域 | (GM6)–(GM9)；先用同图块零锚，再核完整最小残差与选中范数同时落在 \([0,\bar t]\) |
| Dini 与采样、连续长度函数 | (GM10)–(GM14)；一个/任意采样参数等价、一致收敛及精确剩余预算 |
| C09 唯一图块轨道 | (GM15)–(GM18)；每步先证严格留域再续 coverage；极限在 \(S\cap U\) |
| C11 不变开域 | (GM19)–(GM21)；\(U=X\) 的无穷距离单列，实际步长只取上界 |
| C11 统一极限与局部可缩 | (GM22)–(GM25)；整个 \(\mathcal O\) 的共同尾、\(W\hookrightarrow V\) 的显式线段后复合 \(\Pi\) 同伦 |
| C10 完整图与非幂模 | (GM26)–(GM32)；切线拼接凹性/次可加、两支全输入反演、跨支点对与直接幂次失败见证 |
| C10 真残差和严格兼容 | (GM33)–(GM35)；完整最小分支、空域 \(+\infty\)、逆 gauge 与每个 \(\kappa>1/4\) 的小尺度门 |
| C10 轨道边界 | (GM36)–(GM39)；正负初值、零轨道、每个 \(a>0\)、有限初始延伸段与 \(a=1\) |

C09/C11 不要求额外完整纤维等式，不要求 \(S\) 是完整零集；向完整 \(J_{\lambda F}\) 作同一轨道转移可另用相关范围的全纤维一致性作为充分门。C11 没有新增固定关系条件。C10 的全图计算不自动授予其它模型任何误差界或收敛结论。本页没有核外部先行性；没有把局部可缩解释为任意小邻域自身可缩，也没有把回缩自动加强为强形变回缩。

**来源定位。** 历史包为
`history/sources/次单调论文研究/RLEB_投稿扩展版_完整源码_2026-09-19.zip`，SHA-256：
`66597a9a1af42d4209842a688a249486f22ae5a4918e897551011d26999ff0d2`。

| ZIP 成员与字节哈希 | 已重构范围 |
| --- | --- |
| `RLEB_投稿扩展版_2026-09-19/sections/extensions_moduli_structure.tex`；SHA-256 `dfacf9d8705c35b025ed55a6b22a3db12c4495a989a56b1cb8c003dcbea20dfb` | 14–115 行一般模定义及 `thm:modulus-dini` → C09；124–297 行剖面及 `thm:logarithmic-seam` → C10；305–395 行长度递推及 `prop:limit-retraction` → C11 |
| `RLEB_投稿扩展版_2026-09-19/sections/theorem_spine.tex`；SHA-256 `75b374b08d64114b9b7a6d153e7258df89490db067ec79e9590c599a1c08677c` | 4–13 行空间/零集，48–80 行图块近端与单值，82–138 行真实 gauge 及 A1–A4，150–193 行一步证明所需约定；本页直接重写，不隐含引用旧证明 |

来源其它章节、一般 Hilbert 结构、随机推论和完整多选择版本不由本页验收。C09/C10/C11 的数学身份维持原版本；新增文字关闭的是正文对象、假设、证明与边界义务，不主张新颖性。
