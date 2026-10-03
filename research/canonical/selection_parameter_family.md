# 几何尾选择模的任意指数完整二支族

<a id="pf-object"></a>
## C139：对象、参数与完整纤维

固定 Euclidean \(E=\mathbb R^3\)、\(\lambda=1\)、
\(0<\gamma<1\)、\(0<q<1\) 和 \(A,B>0\)。所有常数在让
初值趋于零前固定。对 \(a\ge0\) 令
\[
h_a(p)=p+B\min\{p_+,a\}^{\gamma},\qquad
\tau_a=h_a^{-1}.
\]
这是连续、严格递增且满射 \(\mathbb R\to\mathbb R\)：在
\(p\le0\) 为恒等，在 \(0<p<a\) 为 \(p+Bp^\gamma\)，在
\(p\ge a\) 为 \(p+Ba^\gamma\)。三段在边界接合。
给 \(u=(\xi,\eta,y)\) 定义**完整**关系
\[
F(u)=\begin{cases}
\{(-Aa^\gamma,\tau_a(\eta)-\eta,a-y),
(-Aa^\gamma,\tau_a(\eta)-\eta,-a-y)\},
&y\ge0,\ a=y/q,\\
\varnothing,&y<0.
\end{cases}                                                     \tag{PF-1}
\]
\(y=0\) 的两支合一。由于 \(\tau_a(\eta)-\eta\) 随
\((a,\eta)\) 连续，且绝对值不超过 \(Ba^\gamma\)，图闭。
\(\gamma\) 为正有理数时图半代数；这里的实参数系数无需有理。
完整零集为 \(S=\mathbb R^2\times\{0\}\)。

对每个输入 \(x=(z,p,r)\in E\)，由 \(x=u+v\) 的第三坐标
得到 \(r=\pm a\)，故 \(a=|r|\)、\(y=q|r|\)；若 \(r\ne0\)，
符号唯一确定图支。第一坐标给 \(\xi=z+A|r|^\gamma\)，
第二坐标给 \(p=\tau_{|r|}(\eta)\)，因此 \(\eta=h_{|r|}(p)\)。
\(r=0\) 时两支合一，亦唯一。所以**全部**近端纤维为
\[
J_F(x)=\{T(x)\},\qquad
T(z,p,r)=\bigl(z+A|r|^\gamma,
p+B\min\{p_+,|r|\}^\gamma,q|r|\bigr).              \tag{PF-2}
\]
不存在只验正输入而遗漏的远支。取 \(\gamma=1/2,q=1/4,A=B=1\)
恰得到 [C137/C138 的同一个完整图](selection_geometric_cap.md#gc-object)。

<a id="pf-certificates"></a>
## 全对模、真残差与严格兼容的固定门

令 \(C=2T-I\)。对输入点对 \(\delta=\|x-x'\|\le R\)，
\(|s^\gamma-t^\gamma|\le|s-t|^\gamma\)，且
\(\min\{p_+,|r|\}\) 对 \((p,r)\) 的 Euclidean 距离
为 1-Lipschitz。\(C\) 的前两项非线性差范数至多
\(2\sqrt{A^2+B^2}\,\delta^\gamma\)；其线性余项
\((z,p,2q|r|-r)\) 的 Lipschitz 常数不超过 \(1+2q\)。
故完整图满足输入对距 \(R\) 内的全对
\[
\mathrm{RL}(1,\gamma,L_R;R),\qquad
L_R=2\sqrt{A^2+B^2}+(1+2q)R^{1-\gamma}.             \tag{PF-3}
\]
取输入 \((0,t,t),(0,t,0)\)，\(t\downarrow0\)，前两
反射差的主项为 \((2At^\gamma,2Bt^\gamma)\)。因此大于
\(\gamma\) 的全对指数失败，局部最优系数极限为
\(2\sqrt{A^2+B^2}\)；不声称每个固定 \(R\) 的 \(L_R\) 最小。

对 \(u=(\xi,\eta,y)\in\operatorname{dom}F\)，\(a=y/q\)，
由于 \(0<q<1\)，两图值中第三坐标的最小平方是
\((1-q)^2a^2\)。**全部图值的最小残差**精确为
\[
r_F(u)^2=A^2a^{2\gamma}+(\tau_a(\eta)-\eta)^2
 +(1-q)^2a^2\ge A^2a^{2\gamma}.                    \tag{PF-4}
\]
因 \(d(u,S)=y=qa\)，\(d(u,S)\le\psi(r_F(u))\)，其中
\(\psi(s)=q(s/A)^{1/\gamma}\)。沿 \(\eta\le0,a\downarrow0\)
此系数渐近取到。对指定 \(R>0\)，先令 \(\psi\) 的定义域
覆盖全部零锚比较得到的选中图值范数，例如
\(\bar s\ge(R+L_RR^\gamma)/2\)。于是直接兼容商由
\[
\kappa_R=q\left(
\frac{\sqrt{A^2+B^2}+(1+q)R^{1-\gamma}}{A}
\right)^{1/\gamma}                                      \tag{PF-5}
\]
控制。只要固定
\[
0<B/A<\sqrt{q^{-2\gamma}-1},\quad
0<R^{1-\gamma}<
\frac{Aq^{-\gamma}-\sqrt{A^2+B^2}}{1+q},             \tag{PF-6}
\]
就有 \(\kappa_R<1\)。同一完整图的全输入 coverage、
最近零锚、真 EB、gauge 定义域和严格兼容俱备，可调用
[C02-v2 的单值图块定理](../rleb_ppa.md#r02-proof)。实际法向
率为 \(q\)，而 \(R\downarrow0\) 的保守证书率
\(\kappa_*=q(1+(B/A)^2)^{1/(2\gamma)}>q\)；二者不可混同。

<a id="pf-sharp"></a>
## 共同几何尾与同图配对的任意指数锐阶

固定 \(0<r_0<1\)，以 \(x_0=(0,0,r_0)\)、
\(x_\varepsilon=(0,\varepsilon,r_0)\) 比较；若要在
同一个严格证书内读此配对，另固定 \(r_0\le R\) 且 (PF-6)。
在本配对 \(r_k=r_0q^k\)，正初值的第二坐标满足
\[
p_{k+1}=p_k+B\min\{p_k,r_k\}^\gamma.             \tag{PF-7}
\]
不论第二坐标，全部 \(|r_0|\le R\) 轨道的共同点尾由
\[
\|T^kx-\Pi(x)\|\le
\frac{\sqrt{A^2+B^2}\,R^\gamma}{1-q^\gamma}q^{\gamma k}
 +Rq^k                                                     \tag{PF-8}
\]
控制；[SS-TRANSFER](solution_selection_rates.md#ss-transfer)
给两点对数上界的指数
\(\beta=\gamma\log(1/q)/\log(1/\gamma)\)。
负法向初值从第一步起进入正侧，第一步的切向增量仍由
\(\sqrt{A^2+B^2}|r_0|^\gamma\) 控制，故 (PF-8) 包括 \(k=0\)。

为独立证明同图下界，令 \(t=\log(1/\varepsilon)\)，
\(N=\min\{k:p_k\ge r_k\}\)。\(N\to\infty\)：对固定有限
\(k\) 迭代随 \(\varepsilon\downarrow0\) 趋零，而 \(r_k>0\)。
在 \(k<N\) 的未饱和段，
\[
\log p_{k+1}=\gamma\log p_k+
\log(B+p_k^{1-\gamma}),
\quad |\log p_k+t\gamma^k|\le C_0
\quad(0\le k\le N),                                      \tag{PF-9}
\]
其中 \(C_0=\max\{|\log B|,|\log(B+r_0^{1-\gamma})|\}/(1-\gamma)\)
不依赖 \(\varepsilon,N\)。写 \(a=\log(1/q)\)。
由 \(p_N\ge r_0q^N\) 使用 (PF-9) 的**上界**，
由 \(p_{N-1}<r_0q^{N-1}\) 使用**下界**，得到
\[
t\gamma^N\le aN+C_0-\log r_0,
\quad t\gamma^{N-1}>a(N-1)-C_0-\log r_0.             \tag{PF-10}
\]
于是 \(t\gamma^N=\Theta(N)\)，
\(N=(\log t-\log\log t)/\log(1/\gamma)+O(1)\)。
切换后永远饱和，精确地
\[
p_\infty=p_N+\frac{B r_N^\gamma}{1-q^\gamma},
\quad p_N<r_{N-1}+B r_{N-1}^\gamma=O(r_N^\gamma).       \tag{PF-11}
\]
另一条零第二坐标的轨道始终为零，其余极限坐标相同。因此
\[
\|\Pi(x_\varepsilon)-\Pi(x_0)\|=\Theta(r_N^\gamma)
=\Theta\!\left[
\left(\frac{\log\log(1/\varepsilon)}
{\log(1/\varepsilon)}\right)^\beta\right].           \tag{PF-12}
\]
常数依赖**固定** \(\gamma,q,A,B,r_0\)，不声称归一化极限。
这匹配共同尾所得的 \(\beta\) 阶，并排除本配对的任意正阶
Hölder；它不证明把保守证书 \(\kappa_R\) 固定成实际 \(q\)
后的更窄类也锐。

**来源与未闭范围。** SS1 修订包 `research_note.md` 359–448 行
给出对象线索；本页独立固定全部参数、完整纤维、真实残差、
有限半径与首次切换。外部原创性、§5.2 的额外切向条件及
任意超线性尾的另一模型族不在此证明范围；§5.2
三角动力学的不同充分门另见 [C140](selection_tangential_condition.md#tc-triangle)。
