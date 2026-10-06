# 两支图的 signed-Schur 增长证书

版本 **SS-GROWTH-v2**，2026-10-02；独立重构，状态 `derived-checked`。这里验证的是一个有限维、一维法向、两支接缝的条件证书：切向反演、输入覆盖、跨支排他及全对反射模。真实残差 EB、零点锚、收缩兼容和轨道留域是另外的条件。

**版本区别。** 本版要求参数化在闭参数域的邻域有 \(C^1\) 延拓，而图包含只要求在显示的闭参数域上成立。S19 原稿的 “are defined on a neighborhood of their displayed parameter domains and take values in \(\operatorname{gph}F\)” 未明说图包含的范围；其原措辞及平方根实例的适用问题保留在 [SS-SOURCE](#ss-source)，不把两种读法默认为同一版本。

<a id="ss-interface"></a>
## SS-INTERFACE · 与全局对象、符号和证据状态的接口

本页可从下面的完整假设直接使用，不依赖 S19 的叙述次序。所有结果的基础对象均是**固定同一个** \(F,\lambda,Q,g_+,g_-\)，改变图、步长或参数块后须重新核界。与[参数字典](parameter_dictionary.md#pd-quantifiers)的对应为：\(\Gamma=G_{\mathrm{rep}}\cap X^{-1}(B_r\times\mathbb R)\) 给表示图的全对**一般反射模** (SS-11)；只有另核 SS-POWER 的幂增长条件，才在输入直径至多 \(D\) 的子块得到 \(\mathrm{RL}(\lambda,1/p,L_D;D)\) 的幂模证书。覆盖集是较小的 \(U\)，完整图识别只在 \(U\) 使用 (SS-13)。切向球内而 \(U\) 外的表示图点仍受 (SS-11) 控制，但不由此得到完整近端结论。

| 本页符号 | 含义与跨页使用限制 |
| --- | --- |
| \(Xg,Yg\) | 同一图点的 Minty 输入与反射坐标，对应字典的 \(u+\lambda v,u-\lambda v\)；\(X\) 在此不是环境空间的名字 |
| \(z,a,t,\sigma\) | 修正后的切向输入、原切向参数、非负法向参数、分支符号；\(t\) 不是迭代时间或残差 |
| \(R,T,r\) | 参数切向半径、参数法向上界、输入切向半径；不是 [R01](../rleb_ppa.md#r01) 的残差/解集距离窗 |
| \(\mu,H,B,K_z,K_\pm\) | 本参数块的导数界；\(\mu\) 不是字典 tied 参数，\(H\) 不是 Hilbert 空间 |
| \(p,p',V,C_B\) | Schur 增长幂、共轭幂、两支预算最大值、法切混合系数；\(V\) 不是 R03 的能量函数，\(1/p\) 只提供 RL 指数，未指定 EB 幂 |
| \(J_{\mathrm{rep}},J_{\mathcal G},J_{\lambda F}\) | 表示图、目标图块和完整关系的近端；(SS-13) 核清后才在 \(U\) 上识别 |

源稿所谓 “complete branches” 只要求在整个显示参数块一致验算；它不替代完整 \(F\) 的纤维排他。源稿 “corank-one seam” 在这里仅标示**一个标量法向变量**的构造：假设本身不要求接缝处 \(\operatorname{rank}DX=n-1\)，例如 \(h(t)=t\) 允许全秩。所用强单调反演、隐函数微分和标量增长均在下文展开；“RLEB-specific output” 只指这三项给出的联合接口，不认证外部新颖性或优先权。通向 [R01/R02](../rleb_ppa.md#r01) 还需 SS-OBLIGATIONS 的独立输入。

<a id="ss-object"></a>
## SS-OBJECT · 空间、图块与全部假设

固定 \(n\ge2\)、\(\lambda>0\)，并以正交坐标写 \(\mathbb R^n=\mathbb R^{n-1}\times\mathbb R\)。\(P,N\) 分别为切向、标量法向投影。对图点 \(g=(u,v)\) 定义

\[
Xg=u+\lambda v,\qquad Yg=u-\lambda v.
\tag{SS-1}
\]

令 \(R,T,\mu>0\)，\(H,B,K_z,K_+,K_-\ge0\)，

\[
Q=\overline B_R^{n-1}\times[0,T].
\]

两映射 \(g_\sigma=(u_\sigma,v_\sigma)\)，\(\sigma\in\{+1,-1\}\)，在 \(Q\) 的开邻域为 \(C^1\)，且 **对每个 \(q\in Q\)** 有 \(g_\sigma(q)\in\operatorname{gph}F\)。写 \(X_\sigma=Xg_\sigma\)、\(Y_\sigma=Yg_\sigma\)。全部以下条件均在同一 \(Q\) 上一致成立：

1. **公共接缝与切向中心。**

   \[
   g_+(a,0)=g_-(a,0)=g_0(a),\qquad PX_\sigma(0,0)=0.
   \tag{SS-2}
   \]

2. **切向可逆性及法向参数引起的切向漂移。** 令

   \[
   A_\sigma=P D_aX_\sigma,\qquad b_\sigma=P\partial_tX_\sigma.
   \]

   则

   \[
   \operatorname{sym}A_\sigma\succeq\mu I,\qquad
   \|b_\sigma\|\le H.
   \tag{SS-3}
   \]

   因而 \(A_\sigma\) 可逆，并有 \(\|A_\sigma^{-1}\|\le1/\mu\)。

3. **切向消元后的三个导数界。**

   \[
   \begin{aligned}
   \|ND_aX_\sigma A_\sigma^{-1}\|&\le B,\\
   \|D_aY_\sigma A_\sigma^{-1}\|&\le K_z,\\
   \|\partial_tY_\sigma-D_aY_\sigma A_\sigma^{-1}b_\sigma\|
      &\le K_\sigma.
   \end{aligned}
   \tag{SS-4}
   \]

4. **两侧相反的定向增长。** \(h_\sigma:[0,T]\to[0,\infty)\) 为 \(C^1\)、凸、严格递增，且 \(h_\sigma(0)=0\)，并有

   \[
   \sigma\bigl(N\partial_tX_\sigma
      -ND_aX_\sigma A_\sigma^{-1}b_\sigma\bigr)
      \ge h_\sigma'(t).
   \tag{SS-5}
   \]

矩阵范数和向量范数均为欧氏范数。取

\[
0<r<\mu R-HT.
\tag{SS-6}
\]

这同时要求 \(\mu R>HT\)。所表示的图为

\[
G_{\mathrm{rep}}=g_+(Q)\cup g_-(Q).
\]

<a id="ss-growth"></a>
## SS-GROWTH-v2 · 覆盖、无碰撞与全对模

在 SS-OBJECT 的全部假设下，结论如下。

**切向反演与覆盖。** 对每个 \(z\in B_r^{n-1}\)、\(t\in[0,T]\) 和分支 \(\sigma\)，恰有一个 \(\alpha_\sigma(z,t)\in B_R^{n-1}\) 满足

\[
PX_\sigma(\alpha_\sigma(z,t),t)=z.
\tag{SS-7}
\]

这些反演映射为 \(C^1\)，接缝处 \(\alpha_+(z,0)=\alpha_-(z,0)\)。定义

\[
\begin{aligned}
n_\sigma(z,t)&=NX_\sigma(\alpha_\sigma(z,t),t),\\
y_\sigma(z,t)&=Y_\sigma(\alpha_\sigma(z,t),t),\\
\nu(z)&=n_+(z,0)=n_-(z,0),\qquad
y_0(z)=y_+(z,0)=y_-(z,0).
\end{aligned}
\tag{SS-8}
\]

则 \(\nu\) 连续，且所表示的图覆盖开输入领圈

\[
U=\{(z,s):\|z\|<r,\quad
       \nu(z)-h_-(T)<s<\nu(z)+h_+(T)\}.
\tag{SS-9}
\]

**无碰撞。** 在 \(G_{\mathrm{rep}}\) 中，只要切向输入属于 \(B_r^{n-1}\)，相同完整输入 \(Xg=Xg'\) 就蕴含相同图点 \(g=g'\)。两支在接缝的重复参数化仅表示同一个图点。因此在 \(U\) 上有所表示图的单值近端 \(J_{\mathrm{rep}}\)。

**全对反射模。** 令

\[
\begin{aligned}
C_B&=\sqrt{1+B^2},\\
V(q)&=\max\{K_+t+K_-s:\ 0\le t,s\le T,
                \ h_+(t)+h_-(s)\le q\},\quad q\ge0,\\
\omega(d)&=K_zd+V(C_Bd).
\end{aligned}
\tag{SS-10}
\]

对 **任意两** 所表示图点，只要二者切向输入均在 \(B_r^{n-1}\)，置 \(d=\|Xg-Xg'\|\)，则

\[
\|Yg-Yg'\|\le\omega(d),
\tag{SS-11}
\]

等价地，

\[
\|u-u'\|^2+\lambda^2\|v-v'\|^2
\le\frac12\bigl(d^2+\omega(d)^2\bigr).
\tag{SS-12}
\]

\(V,\omega\) 非减，\(V(0)=\omega(0)=0\)，且在零点连续。对输入属于 \(U\) 的点，(SS-12) 的左边等于

\[
\|J_{\mathrm{rep}}x-J_{\mathrm{rep}}x'\|^2
+\|(x-J_{\mathrm{rep}}x)-(x'-J_{\mathrm{rep}}x')\|^2.
\]

**全纤维门。** 若所需局部图块 \(\mathcal G\subset\operatorname{gph}F\) 另满足

\[
\mathcal G\cap X^{-1}(U)
 =G_{\mathrm{rep}}\cap X^{-1}(U),
\tag{SS-13}
\]

则在 \(U\) 上 \(J_{\mathcal G}=J_{\mathrm{rep}}\)，上述结论对输入属于 \(U\) 的图点对适用于该图块；(SS-13) 不转移 \(U\) 外的所表示图点对。要把结论赋予完整 \(J_{\lambda F}\)，必须以 \(\mathcal G=\operatorname{gph}F\) 核 (SS-13)。

### 独立证明

**1. 切向存在、唯一和光滑反演。** 固定 \(t,\sigma\)，写 \(f(a)=PX_\sigma(a,t)\)。沿 \(Q\) 内的切向线段积分 (SS-3)，得

\[
\langle f(a)-f(a'),a-a'\rangle\ge\mu\|a-a'\|^2.
\tag{SS-14}
\]

又 \(\|f(0)\|\le Ht\le HT\)。当 \(\|a\|=R\)、\(\|z\|<r\) 时，

\[
\langle f(a)-z,a\rangle
\ge\mu R^2-(HT+\|z\|)R>0.
\tag{SS-15}
\]

若闭球上 \(f-z\) 没有零点，则

\[
a\longmapsto-R\frac{f(a)-z}{\|f(a)-z\|}
\]

是闭球到其自身的连续映射。Brouwer 不动点定理适用于这个非空、紧、凸的有限维闭球，给一个球面不动点；在那里 (SS-15) 的内积为 \(-R\|f(a)-z\|<0\)，矛盾。零点不在边界，故在 \(B_R\) 内。由 (SS-14) 唯一。

对任何向量 \(w\)，\(\langle A_\sigma w,w\rangle\ge\mu\|w\|^2\)，从而 \(\|A_\sigma w\|\ge\mu\|w\|\)，故方阵 \(A_\sigma\) 可逆。参数化隐函数定理的 \(C^1\) 与方阵可逆条件均满足。局部反演由唯一性拼成 (SS-7)，并有

\[
D_z\alpha_\sigma=A_\sigma^{-1},\qquad
\partial_t\alpha_\sigma=-A_\sigma^{-1}b_\sigma.
\tag{SS-16}
\]

端点 \(t=0,T\) 的微分由邻域的 \(C^1\) 延拓保证；延拓点不需属于图。公共接缝给 \(\alpha_+(z,0)=\alpha_-(z,0)\)。

**2. 消元后的导数和输入覆盖。** 所有右端在各自修正参数 \((\alpha_\sigma(z,t),t)\) 上计算。由链式法则，

\[
\begin{aligned}
D_zn_\sigma&=ND_aX_\sigma A_\sigma^{-1},\\
\partial_tn_\sigma&=N\partial_tX_\sigma
   -ND_aX_\sigma A_\sigma^{-1}b_\sigma,\\
D_zy_\sigma&=D_aY_\sigma A_\sigma^{-1},\\
\partial_ty_\sigma&=\partial_tY_\sigma
   -D_aY_\sigma A_\sigma^{-1}b_\sigma.
\end{aligned}
\tag{SS-17}
\]

于是

\[
\|D_zn_\sigma\|\le B,\quad
\sigma\partial_tn_\sigma\ge h_\sigma'(t),\quad
\|D_zy_\sigma\|\le K_z,\quad
\|\partial_ty_\sigma\|\le K_\sigma.
\tag{SS-18}
\]

对 \(t>s\)，\(n_+(z,t)-n_+(z,s)\ge h_+(t)-h_+(s)>0\)；负支反向严格递增。两支从同一 \(\nu(z)\) 出发，分别至少到达 \(\nu(z)+h_+(T)\) 和 \(\nu(z)-h_-(T)\)。标量中值定理给 (SS-9) 的覆盖。相同 \(z\) 时两法向范围只在 \(t=0\) 接触，所以完整输入相同只可能为同分支同参数，或同一接缝图点。这证明无碰撞。

**3. 凸增长控制同支参数差。** 对凸函数 \(h\)、\(h(0)=0\) 及 \(0\le s\le t\)，

\[
h(t)-h(s)\ge h(t-s).
\tag{SS-19}
\]

当 \(t>0\) 时，凸性分别给 \(h(s)\le(s/t)h(t)\) 和 \(h(t-s)\le((t-s)/t)h(t)\)；相加即得 (SS-19)。

同支点的修正参数为 \((z,t),(w,s)\)。积分 (SS-18)、使用 (SS-19) 及切向球的凸性，得

\[
\begin{aligned}
h_\sigma(|t-s|)
&\le |n_\sigma(z,t)-n_\sigma(w,s)|+B\|z-w\|\\
&\le C_B\sqrt{\|z-w\|^2+
    |n_\sigma(z,t)-n_\sigma(w,s)|^2}=C_Bd.
\end{aligned}
\tag{SS-20}
\]

输出差至多 \(K_z\|z-w\|+K_\sigma|t-s|\)。在 (SS-10) 中将另一支参数置零，便有 \(K_\sigma|t-s|\le V(C_Bd)\)。

**4. 跨支通过公共接缝比较。** 对正支 \((z,t)\)、负支 \((w,s)\)，

\[
\begin{aligned}
h_+(t)+h_-(s)
&\le n_+(z,t)-n_-(z,s)\\
&\le |n_+(z,t)-n_-(w,s)|+B\|z-w\|\le C_Bd.
\end{aligned}
\tag{SS-21}
\]

沿 \(y_+(z,t)\to y_0(z)\to y_0(w)\to y_-(w,s)\) 比较，

\[
\|y_+(z,t)-y_-(w,s)\|
\le K_+t+K_z\|z-w\|+K_-s
\le K_zd+V(C_Bd).
\tag{SS-22}
\]

反过来的分支次序由对称性处理。结合第 3 步得 (SS-11)。

**5. 图恒等式、零点模与全纤维。** 剪切恒等式

\[
2(\|u-u'\|^2+\lambda^2\|v-v'\|^2)
=\|Xg-Xg'\|^2+\|Yg-Yg'\|^2
\tag{SS-23}
\]

给 (SS-12)。定义 \(V\) 的可行集非空紧致，且随 \(q\) 增大而增大，故极大值存在、非减。若 \(q_j\downarrow0\)，任意相应可行参数都满足 \(h_+(t_j),h_-(s_j)\le q_j\)；由严格递增及零点值，\(t_j,s_j\to0\)。所以 \(V(q_j)\to0\)。最后 (SS-13) 是把已证的所表示图纤维直接识别为所需图块的额外恒等式。□

<a id="ss-power"></a>
## SS-POWER-v2 · 幂次常数及其适用范围

若 \(h_\sigma(t)=c_\sigma t^p\)、\(c_\sigma>0\)、\(p>1\)，置

\[
p'=\frac p{p-1},\qquad
C_p=\left[(K_+c_+^{-1/p})^{p'}
          +(K_-c_-^{-1/p})^{p'}\right]^{1/p'}.
\tag{SS-24}
\]

则 \(V(q)\le C_pq^{1/p}\)。因而对**切向输入都在 \(B_r^{n-1}\)**、输入直径至多 \(D>0\) 的任意所表示图子块，所有图点对满足全对 RL

\[
\|Yg-Yg'\|\le L_D\|Xg-Xg'\|^{1/p},\qquad
L_D=K_zD^{1-1/p}+C_B^{1/p}C_p.
\tag{SS-25}
\]

**证明。** 在可行参数上取 \(x=c_+^{1/p}t\)、\(y=c_-^{1/p}s\)。于是 \(x^p+y^p\le q\)，二维 Hölder 不等式给 (SS-24) 的上界。即使无约束极大点超过 \(T\)，这仍是有效上界。再用 \(d\le D^{1-1/p}d^{1/p}\)。□

当 \(p=1\) 时，令

\[
C_1=\max\{K_+/c_+,K_-/c_-\},\qquad
\gamma=1,\quad L=K_z+C_BC_1.
\tag{SS-26}
\]

这是线性预算的直接上界，包含 \(K_\sigma=0\) 的退化情形。

**两支幂次不同。** 若 \(h_\sigma(t)=c_\sigma t^{p_\sigma}\)、\(p_\sigma\ge1\)，令 \(p=\max\{p_+,p_-\}\) 及 \(\widetilde c_\sigma=c_\sigma T^{p_\sigma-p}\)。因为

\[
h_\sigma(t)\ge\widetilde c_\sigma t^p\quad(0\le t\le T),
\tag{SS-27}
\]

可直接在 (SS-20)、(SS-21) 的预算中用 \(\widetilde c_\sigma\)，得到 (SS-25) 或 (SS-26)。**这只是分配预算的比较，不是新 Schur 导数界。** 当 \(p_\sigma<p\) 时，在 \(t=T\) 有

\[
h_\sigma'(T)=p_\sigma c_\sigma T^{p_\sigma-1}
<p\widetilde c_\sigma T^{p-1}.
\]

所以不可把 (SS-27) 误读为以新幂次重新满足 (SS-5)。

### 基本幂次式的主常数不能统一缩小

在 \(K_z=0\)、\(C_p>0\) 时，(SS-25) 的系数 \(C_B^{1/p}C_p\) 对这组假设是锐的。一个独立见证是在 \(n=2\) 中取

\[
\begin{array}{ll}
X_+(a,t)=(a,Ba+c_+t^p),&Y_+(a,t)=(K_+t,0),\\
X_-(a,t)=(a,Ba-c_-t^p),&Y_-(a,t)=(-K_-t,0).
\end{array}
\tag{SS-28}
\]

通过 (SS-1) 的逆线性变换定义图点。其数据为 \(\mu=1,H=0,K_z=0\)，其余界正好为给定 \(B,K_\sigma,c_\sigma\)。若非整数 \(p>1\)，以 \(|t|^p\) 延拓即可获得所需 \(C^1\) 延拓；图包含仍只在 \(Q\) 检查。

给充分小的 \(q>0\)，选二维 Hölder 等号参数，使

\[
c_+t^p+c_-s^p=q,\qquad K_+t+K_-s=C_pq^{1/p}.
\]

这些参数小于 \(T\)。再选

\[
z-w=-\frac{Bq}{1+B^2}.
\]

两输入的法向差为 \(q/(1+B^2)\)，故 \(d=q/C_B\)，输出差为 \(C_pq^{1/p}\)。它们的 RL 比值恰为 \(C_B^{1/p}C_p\)。\(z,w\) 可都取在任意给定的小切向球内。此见证不声称含 \(K_zD^{1-1/p}\) 的整个有限直径公式总是最优；额外的跨支输出匹配也会限制此见证。

<a id="ss-jet"></a>
## SS-JET-v2 · 修正坐标中的跨支输出匹配

设两支增长均为 \(h_\sigma(t)=ct^p\)，\(c>0,p\ge1\)。在 **同一修正切向输入 \(z\)** 上另假设

\[
\|y_+(z,t)-y_-(z,t)\|\le Et^p,
\qquad z\in B_r^{n-1},\quad0\le t\le T.
\tag{SS-29}
\]

令 \(K=\max\{K_+,K_-\}\)。只对与 SS-GROWTH-v2 相同的**切向输入均在 \(B_r^{n-1}\)** 的图点对，(SS-11)、(SS-12) 中可改用

\[
\omega_{\mathrm{jet}}(d)
=\left(K_z+\frac{EC_B}{2c}\right)d
 +K(C_B/c)^{1/p}d^{1/p}.
\tag{SS-30}
\]

于是直径 \(D\) 上有

\[
L_D^{\mathrm{jet}}
=\left(K_z+\frac{EC_B}{2c}\right)D^{1-1/p}
 +K(C_B/c)^{1/p}.
\tag{SS-31}
\]

**证明。** 同支点已由 (SS-20) 满足此式。跨支时若 \(t\ge s\)，先从 \(y_+(z,t)\) 到 \(y_+(z,s)\)，再用 (SS-29)，最后在负支沿切向到 \(w\)，得

\[
\|y_+(z,t)-y_-(w,s)\|
\le K(t-s)+Es^p+K_z\|z-w\|.
\]

若 \(s\ge t\)，交换两支，使用 \(Et^p\)。由 (SS-21)，

\[
c(t^p+s^p)\le C_Bd,\qquad
|t-s|\le(C_Bd/c)^{1/p},\qquad
\min\{t,s\}^p\le C_Bd/(2c).
\]

代入即得。□

一个充分条件是 \(\|\partial_ty_+(z,t)-\partial_ty_-(z,t)\|\le pEt^{p-1}\)，因为公共接缝允许从零积分。这两项是 (SS-17) 的 Schur 表达式，分别在 **自己的** \(\alpha_\sigma(z,t)\) 上求值；在相同原参数 \(a\) 上比较两支导数不能未经证明替代此条件。

若已有共同幂次、不同正系数 \(h_\sigma(t)=c_\sigma t^p\)，可取 \(c=\min\{c_+,c_-\}>0\) 再使用本节：原导数下界 \(p c_\sigma t^{p-1}\) 确实不小于 \(p c t^{p-1}\)，同支与跨支预算也随之成立。这是 C118-v2 的共同增长下界，不能和 (SS-27) 中只控制函数值的不同幂次比较混用。

<a id="ss-exponent"></a>
## SS-EXPONENT-v2 · 何时 \(1/p\) 确为最大指数

保留幂次证书，固定 \(z_0\in B_r^{n-1}\)。若某支及常数 \(C,c_0,t_0>0\) 满足

\[
|n_\sigma(z_0,t)-\nu(z_0)|\le Ct^p,\qquad
\|y_\sigma(z_0,t)-y_0(z_0)\|\ge c_0t
\quad(0<t<t_0),
\tag{SS-32}
\]

则任何包含该弧和接缝点的图邻域上，全对 RL 指数不能超过 \(1/p\)。当 \(p>1\) 时，所表示的单值近端在该接缝输入处不 calm；通过 (SS-13) 识别的单值局部近端也不 calm。

**证明。** 固定切向输入时 \(d\le Ct^p\)。若有指数 \(\theta>1/p\)，则 \(c_0t\le LC^\theta t^{p\theta}\)，与 \(t\downarrow0\) 矛盾。另一方面，\(2\Delta u=\Delta X+\Delta Y\)，所以

\[
2\|\Delta u\|\ge c_0t-Ct^p.
\]

当 \(p>1\) 时，\(\|\Delta u\|/\|\Delta X\|\to\infty\)，排除单值映射在该输入的 calmness。□

此结论不把一个图块弧的非 calmness 未经纤维识别赋给任意完整多值 \(J_{\lambda F}\)。

<a id="ss-square-root"></a>
## SS-SQUARE-ROOT-v2 · 原生图导数和常数校准

固定 \(\lambda=1\)，取完整关系

\[
F(\xi,y)=
\begin{cases}
\{(-2\sqrt y,3y),(-2\sqrt y,-5y)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}
\tag{SS-33}
\]

在 \(|a|\le R,0\le t\le T\) 上的图参数为

\[
g_+(a,t)=((a,t^2),(-2t,3t^2)),\qquad
g_-(a,t)=((a,t^2),(-2t,-5t^2)).
\tag{SS-34}
\]

两映射有全平面的多项式 \(C^1\) 延拓；它们在 \(t<0\) 的延拓值不属 (SS-33) 的图。因此这是 SS-GROWTH-v2 的实例，不能不处理原措辞就称为邻域全图包含的实例。

独立计算得

\[
\begin{aligned}
X_\pm(a,t)&=(a-2t,\pm4t^2),\\
Y_+(a,t)&=(a+2t,-2t^2),\qquad
Y_-(a,t)=(a+2t,6t^2).
\end{aligned}
\tag{SS-35}
\]

故

\[
\mu=1,\ H=2,\ B=0,\ K_z=1,\quad
h_+(t)=h_-(t)=4t^2,
\]

\[
K_+=4\sqrt{1+T^2},\qquad K_-=4\sqrt{1+9T^2}.
\tag{SS-36}
\]

具体地，\(A_\sigma=1,b_\sigma=-2\)，法向 Schur 导数为 \(\pm8t\)，输出 Schur 导数为 \((4,-4t)\)、\((4,12t)\)。

对 \(0<r<R-2T\)，切向修正为 \(a=z+2t\)，从而

\[
n_\pm(z,t)=\pm4t^2,\quad
y_+(z,t)=(z+4t,-2t^2),\quad
y_-(z,t)=(z+4t,6t^2).
\tag{SS-37}
\]

完整图在

\[
U=(-r,r)\times(-4T^2,4T^2)
\]

上满足 (SS-13)：任何完整图点的输入法向坐标为 \(\pm4y\)，故 \(y<T^2\)、\(t=\sqrt y<T\)；再由切向输入 \(z=a-2t\) 得 \(|a|<r+2T<R\)。它必在所表示的两支内，反向覆盖则已由 (SS-37) 证明。

由 SS-POWER-v2，直径 \(D\) 上可取

\[
\gamma=\tfrac12,\qquad
L_D=\sqrt D+\sqrt{8+40T^2}.
\tag{SS-38}
\]

又 \(y_+(z,t)-y_-(z,t)=(0,-8t^2)\)，所以 \(E=8,c=4,p=2\)，SS-JET-v2 给

\[
L_D^{\mathrm{jet}}=2\sqrt D+2\sqrt{1+9T^2}.
\tag{SS-39}
\]

当 \(r,T\to0\)、\(D\) 为相应领圈直径时，(SS-39) 趋于 \(2\)。在 \(z=0\) 的正支与其接缝点上，

\[
d=4t^2,\qquad
\|\Delta Y\|=\sqrt{16t^2+4t^4},\qquad
\frac{\|\Delta Y\|}{d^{1/2}}=\sqrt{4+t^2}\longrightarrow2.
\tag{SS-40}
\]

故 \(2\) 是这种收缩领圈的最优渐近常数，最大指数为 \(1/2\)；并不声称 (SS-38)、(SS-39) 是每个固定领圈的最小常数。

**独立的真实残差检查。** 这里 \(S=\mathbb R\times\{0\}\)，且对 \(y\ge0\)

\[
r_F(\xi,y)=\sqrt{4y+9y^2},\qquad
d((\xi,y),S)=y\le\tfrac14r_F(\xi,y)^2.
\tag{SS-41}
\]

必须在两个图值中取最小范数；较小者是正支。系数 \(1/4\) 在 \(y\downarrow0\) 锐。这是对 (SS-33) 的另外一次全纤维计算，不是从 Schur 证书推出的 EB。

<a id="ss-attacks"></a>
## SS-ATTACKS · 四项不能省去的检查

### 1. 逐支光滑与逐支 Hölder 不能代替相反定向

在 \(n=2\) 的 Minty 坐标中取

\[
X_+(a,t)=X_-(a,t)=(a,t^2),\qquad
Y_\pm(a,t)=(a,\pm t),\qquad t\ge0.
\tag{SS-42}
\]

通过 (SS-1) 的逆线性变换，这些确实定义算子图。两支光滑、半代数、公共接缝，各自的 Minty 映射单射；其法向逆满足 \(|t-s|\le|t^2-s^2|^{1/2}\)。有界输入块上的切向项也给各支 \(1/2\) 阶反射模。

但任意 \(t>0\) 的两支图点输入相同，\(Y\) 相差 \((0,2t)\)，原始输出 \(u\) 相差 \((0,t)\)。因此任何在零处消失的全对反射模都失败。只有负支定向条件失败：\(-\partial_tNX_-=-2t\) 不是 \(2t\) 的下界。并图在 \((X,Y)\) 坐标中是光滑抛物面 \(X_N=Y_N^2,X_P=Y_P\)，按两开支和接缝分层仍不能排除碰撞。

**源稿一维见证及 Whitney 断言的直接核验。** 删除切向坐标得到源稿 \(X_\pm=t^2,Y_\pm=\pm t\)。每支相对接缝的反射比 \(t/(t^2)^\theta\) 在 \(\theta>1/2\) 时无界，故逐支半阶确为最大指数；完整并图仍有同输入碰撞。二维直积的统一参数化为
\[
\Phi(a,\tau)=((a,\tau^2),(a,\tau)),\qquad \tau\in\mathbb R.
\]
它是光滑半代数嵌入，分层取 \(\tau>0,\tau<0,\tau=0\)。两开层趋向接缝时，其切空间趋于
\(\operatorname{span}\{(1,0,1,0),(0,0,0,1)\}\)，包含接缝切线，满足 Whitney (a)。从 \(\Phi(a_i,\tau_i)\) 到接缝点 \(\Phi(b_i,0)\) 的割线方向为 \((a_i-b_i,\tau_i^2,a_i-b_i,\tau_i)\)；其归一化的第二坐标绝对值至多 \(|\tau_i|\to0\)，任何极限都落入上述极限切空间，满足 Whitney (b)。删掉切向分量给原一维抛物线的同一证明。因此即使这里完整核过 Whitney 分层，它仍不供应相反定向或并图全对模；没有调用任意分层的逆定理。

### 2. 凸性是同支全对模的承重条件

若只删除 \(h_\sigma\) 的凸性，取 \(T=1\)、\(h(t)=t-t^2/2\)，并令

\[
X_\pm(a,t)=(a,\pm h(t)),\qquad
Y_\pm(a,t)=(\pm t,0).
\tag{SS-43}
\]

这里 \(h\) 是 \(C^1\)、严格递增、零点为零，两侧 Schur 导数恰为 \(\pm h'(t)\)，其余数据可取 \(\mu=1,H=B=K_z=0,K_+=K_-=1\)。覆盖和无碰撞仍成立。

然而同正支 \(t=1,s=1-\varepsilon\)、相同切向输入给

\[
d=h(1)-h(1-\varepsilon)=\varepsilon^2/2,\qquad
\|\Delta Y\|=\varepsilon.
\]

由于 \(h(t)\ge t/2\)，定义 (SS-10) 的任何可行参数都满足 \(t+s\le2q\)，故 \(V(d)\le2d=\varepsilon^2\)。当 \(0<\varepsilon<1\) 时，(SS-11) 失败。即使只比较开领圈内的点，取 \(t=1-\varepsilon,s=1-2\varepsilon\)，也有 \(d=3\varepsilon^2/2\)、\(V(d)\le3\varepsilon^2<\varepsilon=\|\Delta Y\|\)（\(0<\varepsilon<1/3\)）。这精确定位了 (SS-19) 的用途；不是对覆盖结论的反例。

### 3. 单个接缝点的 Taylor 幂次不能替代切向一致下界

取

\[
X(a,t)=(a,t^3-at),\qquad Y(a,t)=(a,t).
\tag{SS-44}
\]

在 \(a=0\) 上法向律为 \(t^3\)。但每个充分小 \(a>0\) 都有

\[
X(a,0)=X(a,\sqrt a),\qquad
Y(a,0)\ne Y(a,\sqrt a).
\]

因此同输入碰撞进入任意小接缝窗口。其真正 Schur 法向导数是 \(3t^2-a\)，而不是只在 \(a=0\) 观察到的 \(3t^2\)。

### 4. 所表示图的完整性不能由导数界推出

给任何符合本证书的所表示图，在 \(x_0\in U\) 的唯一图点 \((u_0,v_0)\) 以外，再向完整 \(F\) 的图加入

\[
(u_1,(x_0-u_1)/\lambda),\qquad u_1\ne u_0.
\tag{SS-45}
\]

参数化上的全部导数条件保持成立，所表示的覆盖与模也保持成立，但完整 \(J_{\lambda F}(x_0)\) 至少有两值。故 (SS-13) 是独立排他门，不是 Schur 条件的后件。

<a id="ss-obligations"></a>
## SS-OBLIGATIONS · 使用此证书时仍需证明什么

若原生支由 \(G_\sigma(a,t,w)=0\) 隐式给出，且在同一参数块上已证 \(D_wG_\sigma\) 可逆、实际 \(C^1\) 解支存在，则逐参数微分直接给
\[
D_{(a,t)}w=-(D_wG_\sigma)^{-1}D_{(a,t)}G_\sigma.
\]
矩阵区间界可以用此式认证 (SS-3)–(SS-5)，**前提是**解支存在、图包含和完整活动支清单另核。多块有限图册的重叠全纤维与定量输入链几何则仍是未证明的额外义务，不由单块证书自动拼接。

这里 \(G_\sigma\) 要在相关点的开邻域为 \(C^1\)，\(D_wG_\sigma\) 是方阵。单点可逆只由隐函数定理产生该点附近的支；要覆盖整个闭参数块，须先核这些局部支能拼成实际同一支及其所需延拓。区间矩阵界给定量认证的**途径**，源稿未提供任何特定活动系统的数值区间执行记录。

<a id="ss-atlas-boundary"></a>
**有限图册的精确未闭门。** S19 LF 333–335 只提出 chaining 方向，没有给链引理、图册或常数。本页不据此授予一般有限图册定理。拟使用者至少须明定目标输入集 \(E\)、覆盖它的各领圈 \(U_i\)、同一完整关系和步长。若目标是完整 \(J_{\lambda F}\)，须逐领圈核**全部纤维**，仅核所选输出在重叠相同不足以排除完整图的其它值。另一个较弱问题是拼接指定选择：此时可逐领圈证明该选择存在，并逐重叠核所选输出完全一致，但结论仅属于这个指定选择。

两种问题均还须证明：任意 \(x,x'\in E\) 都有 \(x=x_0,\ldots,x_m=x'\)，相邻点落入同一可用图块，且链长和各步尺度受一个随 \(\|x-x'\|\to0\) 消失的统一预算控制。只知道图册有限或重叠非空，不提供这种定量控制；在 Hölder 情形也不能无成本地把 \(\sum_j\|x_j-x_{j-1}\|^\gamma\) 换成端点距离的 \(\gamma\) 次幂。高余维或任意多同侧支的推广还须新的排他/覆盖机制，当前两支一法向证明没有这些结论。

| 证明义务 | 本文件已证明的部分 | 再使用时的独立输入 |
| --- | --- | --- |
| 切向求解 | (SS-3)、(SS-6) 给整个 \(B_r\times[0,T]\) 的唯一内点反演 | 两支实际存在；\(C^1\) 延拓；全部界在整个 \(Q\) 一致成立 |
| 法向覆盖与碰撞 | 相反定向、严格增长和公共图接缝给两侧输入领圈与无碰撞 | 完整活动分支清单及 (SS-13)；不能只核选中的两支 |
| 全对模 | 同支凸增量及跨支分配预算给 (SS-11) | 不能把沿单弧、逐支或单个 Taylor 点的检查当作这些全称条件 |
| 幂次常数 | (SS-25)、(SS-26) 有效；\(K_z=0\) 的基本主系数锐 | 使用同一输入块的直径 \(D\)；不同幂次只比较预算 |
| 输出匹配改善 | 额外 (SS-29) 给 (SS-30) | 在修正后的同一输入 \(z\) 上证明匹配；原参数匹配不能直接替代 |
| 指数最优及非 calm | 双边弧证据 (SS-32) 充分 | 还要上界 \(O(t^p)\) 及输出下界 \(\Omega(t)\)，不是仅有 (SS-5) |
| PPA 收敛 | 本证书供给几何、coverage，完整性核后供给所需近端 | 非空闭目标 \(S\subset F^{-1}(0)\)、最近零点图锚、实际输出上的真实残差 EB、统一收缩兼容、初值留域预算 |
| 文献与更大图族 | 无外部先行性判断 | 先行性；有限图册的重叠全纤维和链几何；多同侧支或高余维推广均未证明 |

证明使用 Brouwer 和参数化隐函数定理；其有限维紧凸球、连续自映射、\(C^1\) 与方阵可逆门已在正文核清。这里只做内部数学重构，不作外部优先权审查。

<a id="ss-source"></a>
## SS-SOURCE · 精确来源与原版本保留

来源 S19：[RLEB_投稿扩展版_完整源码_2026-09-19.zip](../../history/sources/次单调论文研究/RLEB_投稿扩展版_完整源码_2026-09-19.zip)，成员

`RLEB_投稿扩展版_2026-09-19/sections/appendix_signed_schur.tex`。

| 源单元 | 精确成员行 / label | 本版去向与限定 |
| --- | --- | --- |
| 主定理及证明 | 21–218；`thm:signed-schur-growth`；(S1)–(S14) | SS-GROWTH-v2；明确分开邻域 \(C^1\) 延拓与 \(Q\) 上图包含 |
| 幂次常数 | 220–251；`cor:schur-power-constants`；(S15) | SS-POWER-v2；不同幂次的比较只用于预算，不升级 Schur 导数 |
| 输出匹配 | 253–298；`prop:schur-matched-jet`；(S16)–(S17) | SS-JET-v2；同修正输入比较 |
| 最大指数 | 300–320；`prop:schur-sharp-exponent` | SS-EXPONENT-v2；非 calm 只赋予所表示/已识别的单值近端 |
| 原生平方根测试 | 342–406；`prop:schur-square-root-test`；(S18) | SS-SQUARE-ROOT-v2；图包含仅在 \(t\ge0\)，原措辞的严格应用问题见下 |
| 同侧碰撞 | 408–432；`prop:schur-collision-counterexample` | (SS-42) 是原一维见证的切向直积，处于主定理的 \(n\ge2\) 范围 |
| 切向一致性反例 | 434–442 | (SS-44) 独立重算 |
| 原生隐式微分与图册提议 | 322–340 | SS-OBLIGATIONS 展开隐函数门；有限图册与多支/高余维推广保留精确未闭义务 |
| 逆函数工具的关系与证据边界 | 444–452 | SS-INTERFACE 给可复用接口；联合证书不认证新颖性，真残差 EB 仍独立 |

ZIP SHA256：`66597a9a1af42d4209842a688a249486f22ae5a4918e897551011d26999ff0d2`。

成员 SHA256：`9927b4006234fa5f435d831a8583c426311906ba8288a60894516f97cea829d2`。

<a id="ss-version-recovery"></a>
**原稿身份与账本版本的恢复约定。** 本页的 `S19-SG-v1` 是对上述固定成员 LF 21–120 原始主定理及 LF 122–218 证明的**来源标签**，并不是 `C117-v1`；同理，原稿 LF 220–320 的幂次/jet/指数命题、LF 342–406 的平方根命题不自动构成 `C118-v1`、`C119-v1` 的可调用账本版本。已检查本文件的首次 git 引入 `6bec2e2`：规范正文和当时 `CLAIMS.md` 都从 `v2` 开始。本次没有恢复到更早的 C117–C119-v1 命题卡，不能根据编号反造其前提、证据或原文。

| 可恢复身份 | 状态 | 可用范围 |
| --- | --- | --- |
| S19-SG-v1，固定成员 LF 21–218 | `source-report`；两种图包含读法逐项保留 | 原文身份可以引用；不得把其中未分辨的范围作为单一认证命题 |
| 原稿幂次/jet/指数，LF 220–320 | 原式和证明位置已恢复；规范数学由 C118-v2 承担 | 继承切向球限制；幂次预算比较与导数下界分开；完整近端需另核纤维 |
| 原稿平方根，LF 342–406 | `source-report` 身份；强邻域图包含读法下的应用未成立 | C119-v2 仅使用闭参数域图包含，另有完整纤维核验 |
| C117-v2、C118-v2、C119-v2 | `derived-checked`，以本页明写的假设和证明为准 | 唯一可直接调用的三张当前规范卡 |
| 未恢复的 C117-v1、C118-v1、C119-v1 | 不登记猜测性数学内容，不作为有效前驱卡 | 若今后出现准确旧稿或 commit，再逐条恢复；当前调用者转到相应 v2，不能把旧裸编号当成独立证据 |

**原版本 S19-SG-v1 的范围歧义保留为 candidate/source identity，不静默覆盖。** 原稿第 31–32 行原措辞为：

> are defined on a neighborhood of their displayed parameter domains and
> take values in \(\operatorname{gph}F\).

若这句话表示 **邻域内所有参数值也必须属于图**，它是比 SS-GROWTH-v2 更强的假设；其抽象定理是本版的逻辑推论，没有被反例否定。不过原稿平方根测试的多项式延拓在 \(t<0\) 给 \(-2t>0\)，而完整关系 (SS-33) 要求第一图值分量为 \(-2\sqrt{t^2}=-2|t|<0\)。因而该实例不能满足这个邻域全图包含读法。

这个问题不仅是换一个延拓公式：若一个 \(C^1\) 图参数化延续 (SS-34) 到 \(t<0\) 且仍在该完整图中，其第一图值分量在零点的导数必须为 \(-2\)，故负 \(t\) 时它为正；但 (SS-33) 中该分量始终非正，矛盾。原例应用在该字面读法下保持候选适用状态，需先修正参数化假设范围。

SS-GROWTH-v2、SS-SQUARE-ROOT-v2 明写了所需范围，只在 \(Q\) 要求图包含；邻域延拓仅用于端点隐函数和微分。主证明不曾使用延拓点的图包含。除这项假设范围和相应版本标记外，主定理的覆盖、模和全纤维结论保持原量词。凸性攻击 (SS-43)、基本幂次主常数的锐见证 (SS-28) 和平方根真实残差的重算 (SS-41) 是本稿的独立补充，不冒充原源文字。

2026-10-06 已对该精确成员全部 **452 物理 LF 行**作[独立断言枚举](../audit/SIGNED_SCHUR_FULL_UNITS.tsv)；[覆盖与未闭义务](../audit/SIGNED_SCHUR_FULL_COVERAGE.md)分别记录来源版本歧义、有限图册提议和叙述定位。枚举完成不等于关闭这些额外义务，也不关闭同一 ZIP 的其它成员。新增的符号接口、Whitney (a)/(b) 核验和隐式/图册范围说明补齐来源余项，不更改 C117–C119-v2 的主证书对象或证据等级。
