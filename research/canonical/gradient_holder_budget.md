# 三维梯度 Hölder–RL 的临界集与最小预算

固定 \(\lambda>0\)、\(0<\gamma<1\) 及非空紧 \(K\subset\mathbb R^3\)。用 properly critical 指存在光滑 proper \(h:\mathbb R^3\to\mathbb R\)，使 \(\operatorname{Crit}h=K\)。对光滑 \(f\)，在 [C03 的全对全尺度](global_shadow.md#gsh-object) 意义下讨论 \(F=\nabla f\)，求临界集恰为 \(K\) 时所有可用 \(L\) 的下确界。

<a id="ghb-topology"></a>
## C295 · properly critical 恰为有某个有限预算的三维梯度零集

**必要性与近端意义。** 给定全局 Hölder–RL 的光滑梯度。令 \(G(x)=x+\lambda\nabla f(x)\)。从反射差上界可见 \(G\) 单射，且
\[
 2\|x\|\le\|G(x)-G(0)\|+L\|G(x)-G(0)\|^\gamma.
\]
因此 \(G\) 是 proper；由不变域定理和闭像性，其像开且闭，故为全空间。进一步令 \(w=\|G(x)-G(0)\|\)。反向三角给 \(w-Lw^\gamma\le2\|x\|\)，从而 \(w=O(1+\|x\|)\)。回代得
\[
 \nabla f(x)=x/\lambda+O(1+\|x\|^\gamma).
\]
沿射线积分，\(f(x)=\|x\|^2/(2\lambda)+O(1+\|x\|^{1+\gamma})\)，所以 proper 且强制。函数 \(g(x)=\|x\|^2/2+\lambda f(x)\) 的任意线性倾斜均强制，且其梯度零点唯一。每个 \(x\) 因而是 \(g-\langle G(x),\cdot\rangle\) 的唯一全局极小点。严格支撑不等式给严格凸 \(g\)，完整近端确为唯一全局近端最小化。

**保留临界集的二次尾。** 给定 properly critical \(K\)。取相反号如有必要，使 \(h(x)\to+\infty\) 当 \(\|x\|\to\infty\)。这是因为 \(\mathbb R^3\) 的充分远外部连通，proper 性使 \(h\) 在那里避开任给紧区间。选取高于全部临界值的 \(a\)，令 \(S=\{h=a\}\)。归一化外向梯度 \(\nabla h/\|\nabla h\|^2\) 在任意紧值段内可双向流动，将外部 \(h\ge a\) 写为 \(S\times[a,\infty)\)。每个分量均达无穷远，任意大球的外侧连通且最终包含在 \(h>a\)，故 \(S\) 连通。把 \(S\) 上的任意环沿该乘积推到一个大球之外，在外部收缩，再投回 \(S\)。故 \(S\) 单连通，是光滑二球面。

此处导入三维光滑 Schoenflies 与光滑环域结论：两个嵌套光滑二球面之间的闭区域微分同胚于 \(S^2\times[0,1]\)。三维可从拓扑环域与 Moise 的三维光滑化得到。产品坐标只须在两边和选定 collar 相容，允许改变各边切向参数；collar 唯一性给调整。取充分大的圆球边界包围 \(S\)，使乘积的内领口沿 \(h\) 增大，外领口沿半径增大。在环域上构造严格随产品高度增大的函数，近内端等于 \(h\)，近外端等于 \(\|x\|^2/2+b\)。具体做法是先在两领口继承正的高度导数，在中段以正函数相连，再加中间非负 bump 的倍数使积分匹配外端目标值。充分大的 \(b\) 保证倍数正，允许其随切向坐标光滑变化。由此可取 \(h_Q\) 在原内域与 \(h\) 相同，只有原临界集，且外部为精确二次尾。这一步无需移动 \(K\)。下一节给任意严格大于直径阈值的实现，因而特别保证某个有限预算。

**拓扑后果。** 用 Grayson–Pugh 1993 的 Theorem 2.9，三维非空连通紧 \(K\) 可实现恰当其为 cellular。用 Theorem 4.13，tame 两分支 link 恰允许 unlink 与 Hopf link。Theorem 2.15 给任意 tame 至少三分支 link 的正面实现。这里的拓扑分类是外部定理，梯度 Hölder–RL 与 proper 临界集之间的预算和解析归约由本页给出。[Grayson–Pugh 原文](https://www.numdam.org/item/PMIHES_1993__77__5_0.pdf)，[三维光滑 Schoenflies 证明](https://cjhb.site/Files.php/HTML/C3.12%20Low-Dimensional%20Topology%20and%20Knot%20Theory/notes.pdf)，[环域定理与三维光滑化接口，§17](https://people.mpim-bonn.mpg.de/aruray/documents/top_manifolds.pdf)。

<a id="ghb-infimum"></a>
## C296 · 给定嵌入的最小预算下确界

对每个 properly critical \(K\)，有
\[
 \inf\{L\ge0:\ \operatorname{Crit}f=K,\ f\in C^\infty,\ 
          \nabla f\text{ 满足固定 }\lambda,\gamma\text{ 的全局 RL}\}
 =\operatorname{diam}(K)^{1-\gamma}.
\]
每个严格较大的预算均可由光滑微分同胚完整预解式实现。任取临界点对，在 RL 式中梯度差为零，故下界直接成立。

**光滑凸包围。** 令 \(A=\operatorname{conv}K\)。以支持半径 \(\eta\) 的光滑非负单位积分核卷积 \(d_A\)。所得凸光滑函数 \(\varphi_\eta\) 与 \(d_A\) 一致差不超过 \(\eta\)。则 \(B=\{\varphi_\eta\le2\eta\}\) 是紧凸体，包含 \(A\) 于内部，且 \(B\subset A+3\eta\overline{\mathbb B}\)。因水平严格高于最小值，凸性保证梯度在边界非零。因此 \(B\) 光滑，直径可任意接近 \(\operatorname{diam}K\)。

**指定有符号距离领口。** 令 \(s\) 为 \(B\) 边界外向有符号距离，双侧小领口内光滑。选择 \(B\) 内一点作原点，在射线 \(r\theta\) 上边界为 \(r=\rho(\theta)\)，而 \(\partial_r s>0\) 于一致小领口。构造全局沿射线的微分同胚，固定包含 \(K\) 的内部邻域，在领口把半径换成 \(R+s\)，其中 \(R\) 任意大。具体可在两个转换半径间平滑插值正径向导数，在內转换区加正 bump 的倍数匹配 \(R+s-r\) 的积分差，倍数因 \(R\) 大可取正。外部保持正导数且最终取导数 1。原点附近保持恒等。把 \(h_Q\) 与此微分同胚复合，领口内即为 \((R+s)^2/2+b\)。再经严格递增光滑标量重参数化，在领口取 \(\sqrt{2(u-b)}-R\)，得到函数 \(h\) 在领口等于 \(s\)。标量函数的导数可在领口值区之外以全局正光滑函数延拓。复合未改变完整临界集 \(K\)。

**内外拼接。** 取光滑非降 \(\chi\)，在 0 附近取 0，在 \([1,\infty)\) 取 1。置
\[
 f_\epsilon(x)=
 \begin{cases}
  \epsilon h(x)/\lambda,&x\in B,\\
  \displaystyle\lambda^{-1}\int_0^{s(x)}[\epsilon+u\chi(u/\epsilon)]\,du,&x\notin B.
 \end{cases}
\]
接缝两侧在小领口都等于 \(\epsilon s/\lambda\)。光滑凸体外部的距离函数光滑，理由是外法线坐标 \((z,s)\mapsto z+s\nu(z)\) 双射，法向切向微分的特征值为 \(1+s\kappa_i>0\)。其距离函数凸，外侧势为凸的非降标量复合，且外侧径向导数正。故 \(\operatorname{Crit}f_\epsilon=K\)，并有 \(\lambda\nabla^2 f_\epsilon\ge-\epsilon M I\)，其中 \(M=\max\{0,-\inf_B\lambda_{\min}(\nabla^2 h)\}\)。

比较 \(f_0=d_B^2/(2\lambda)\)。记 \(A_0=\max\{1,\sup_B\|\nabla h\|\}\)。内侧立即满足 \(\|\lambda\nabla f_\epsilon-\lambda\nabla f_0\|\le\epsilon A_0\)，外侧用 \(0\le\epsilon-s(1-\chi(s/\epsilon))\le\epsilon\) 得同界。对 \(\epsilon M<1\)，\(G_\epsilon=I+\lambda\nabla f_\epsilon\) 的导数对称正定且有统一下界，故强单调、proper 且为光滑微分同胚。\(G_0^{-1}\) 为 1-Lipschitz，其 Cayley 映射为 \(P_B\)，因为在每条外法线上 \(G_0\) 把投影不变的法向位移翻倍。故
\[
 C_\epsilon=2G_\epsilon^{-1}-I,\quad
 \|C_\epsilon-P_B\|_\infty\le2\epsilon A_0,\quad
 \operatorname{Lip} C_\epsilon\le\frac{1+\epsilon M}{1-\epsilon M}.
\]
最后一项用 Hessian 的特征值变换 \((1-\lambda\mu)/(1+\lambda\mu)\)。值域直径至多 \(\operatorname{diam} B+4\epsilon A_0\)。由 \(\min\{as,b\}\le a^\gamma b^{1-\gamma}s^\gamma\)，全尺度 Hölder 半范数至多
\[
 \left(\frac{1+\epsilon M}{1-\epsilon M}\right)^\gamma
 (\operatorname{diam}B+4\epsilon A_0)^{1-\gamma}.
\]
先固定 \(B\) 令 \(\epsilon\downarrow0\)，再取 \(\operatorname{diam}B\downarrow\operatorname{diam}K\)，得上界。

<a id="ghb-endpoint"></a>
## 同一阈值的端点例

设 \(d=\operatorname{diam}K>0\)，取直径点对 \(a,b\)。若有 \(L=d^{1-\gamma}\) 的光滑实现，在固定 \(y=b\) 的平方 RL 不等式中 \(x=a\) 取等。对 \(x\) 求导得
\[
 \nabla^2 f(a)(a-b)=\frac{1-\gamma}{\lambda(1+\gamma)}(a-b).
\]
另一方面，若沿 \(K\) 有趋于 \(a\) 的割线单位方向极限 \(v\)，因梯度在 \(K\) 全为零，\(\nabla^2f(a)v=0\)，故 \(v\) 必与直径方向正交。非退化线段因此不取到阈值。正则四面体的四个顶点也不取到：每个顶点三条独立直径方向都被迫有相同正特征值，四点均为严格非退化局部极小；若它们是强制函数的全部临界点，其负梯度流的每个轨道有紧子水平集，聚点集连通并包含于四个临界点，故都收敛。各非退化极小点的吸引域是非空两两不交的开集，将不可能覆盖连通的 \(\mathbb R^3\)。四面体顶点本身 properly critical，由四个单点均 cellular 及 Grayson–Pugh Corollary 2.7。

端点可达到。设 \(K=\{-ae_1,0,ae_1\}\)、\(a>0\)。选 \(\kappa>0\) 满足 \(2\kappa/\sinh(2\kappa)=\gamma\)，令 \(c(u)=a\tanh(\kappa u/a)/\tanh\kappa\)，\(C(p)=(c(p_1),0,0)\)。\(c(u)/u\) 在 \(u>0\) 严格递减，故固定点恰为 \(K\)。固定输入间距时 \(\tanh\) 差以中心区间最大，因其导数偶且在正半轴递减。中心差商 \(2c(t)/(2t)^\gamma\) 的导数符号由 \(2\kappa t/[a\sinh(2\kappa t/a)]-\gamma\) 决定。故最大值在 \(t=a\)，为 \((2a)^{1-\gamma}\)。同一维估计也给三维上界，在轴线上取等。\(J=(I+C)/2\) 是全局光滑强凸梯度，逆是其凸共轭的梯度。写 \(J^{-1}=I+\lambda\nabla f\) 即得光滑 \(f\) 及完整 RL。

本页关闭严格预算差的猜想，端点达到性的完整分类、固定定量误差界下的预算以及外部精确优先仍开放。几何结论未计算或认证近端动力学的速度。
