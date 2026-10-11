# 指数缺额的锐零点代价与原常数完成的单点基准

本页接续 C231–C235，基线 `8f27b321c4014c6f508f98428f4fd78015ff64ab`。固定整个输入管和完整近端映射，不把“保零集”“保原常数”“全域收敛”合并。C236 允许有限新 Hölder 常数；C237 保持精确原常数。经典 degree/Hopf 和凸投影是明确已有工具，本页推导不认证发表优先。本轮由主代理完成显示证明、反向重构和有限复算，未声称新增独立代理审查。

<a id="scc-data"></a>
## 固定数据与分量缺额

沿用 [ZPC-DATA](zero_preserving_completion.md#zpc-data)：\(H=\mathbb R^n\)、\(n\ge2\)、\(\lambda>0\)，非空紧无边界嵌入 \(C^2\) 流形 \(M\)，\(0<\rho<\operatorname{reach}(M)\)，\(N=N_\rho\)，整个 \(N\) 上指定 \(T_0\)，满足
\[
T_0|_M=\operatorname{Id},\qquad d(T_0p,M)\le\theta d(p,M),\quad 0\le\theta<1,
\qquad C_0=2T_0-\operatorname{Id}\text{ 为有限 }\gamma\text{-Hölder},\quad0<\gamma<1.
\tag{SC1}
\]
**不要求管外连通。** 取足够大的闭球 \(\overline B_R\) 把 \(N\) 包含于内部。紧带边界流形
\(W=\overline B_R\setminus\operatorname{int}N\)
有有限个连通分量 \(W_1,\ldots,W_s\)。令 \(D_0=\operatorname{Id}-T_0\)。在全部边界给定
\[
g(p)=D_0(p)/\|D_0(p)\|\quad(p\in\partial N),\qquad
g(p)=p/R\quad(p\in\partial B_R).
\tag{SC2}
\]
按每个 \(W_j\) 的诱导边界定向定义
\[
\delta_j=\deg(g|_{\partial W_j}),\qquad
\sum_{j=1}^{s}\delta_j=1-\chi(M).
\tag{SC3}
\]
内边界的定向与 \(N\) 的定向相反；第二式由 C231 的局部指数与外球次数 1 得到。增大 \(R\) 只在唯一的外部连通分量附加球壳，其余分量不变；\(\delta_j\) 不依赖这种增大。

每个全域完成仍用 Z1：\(\widehat T=(\operatorname{Id}+\widehat C)/2\)，完整图为
\(\{(\widehat T(p),(p-\widehat T(p))/\lambda):p\in H\}\)。故 \(\operatorname{zer}\widehat F=\operatorname{Fix}\widehat T\)，完整 \(J_{\lambda\widehat F}=\widehat T\)。这里只计管外新增零点。

<a id="scc-sharp"></a>
## C236-v1 · 分量缺额给出可达到的最小新增零点数

**精确陈述。** 对每一组 SC1 数据：

1. 存在保整个 \(C_0\) 的全域有限同指数 Hölder 完成，其全部管外零点有限。此类完成中的最小新增零点数为
   \[
   \boxed{\min\#(\operatorname{zer}\widehat F\setminus M)
   =\#\{j:\delta_j\ne0\}.} \tag{SC4}
   \]
   对每个 \(\delta_j\ne0\)，可把唯一新增零点放在任意预先指定的 \(q_j\in\operatorname{int}W_j\)，其局部指数恰为 \(\delta_j\)。
2. 若要求全部新增零点在其邻域内 \(\widehat T\) 为 \(C^1\)，且
   \(\det(I-D\widehat T(q))\ne0\)，则最小数量为
   \[
   \boxed{\min\#(\operatorname{zer}\widehat F\setminus M)
   =\sum_j|\delta_j|.} \tag{SC5}
   \]
   各分量中的 \(|\delta_j|\) 个点可任意预先指定，指数全取 \(\operatorname{sgn}\delta_j\)。
3. 两种达到构造均可使 \(\widehat C\) 紧支撑。因此不连通管外的无新增零点完成，恰以**每个** \(\delta_j=0\) 为充要条件。

当 \(W\) 连通，SC4 是 0（\(\chi(M)=1\)）或 1（\(\chi(M)\ne1\)），SC5 是 \(|1-\chi(M)|\)。这把 C233 的无零延拓与任意整数缺额的补偿统一起来。SC4 不把一个高指数孤立零点称为非退化零点，也不宣称补偿零点是吸引子。

### 下界：次数逐分量守恒

任意有限全域 Hölder 完成是次线性的。对充分大的外球，位移
\(\widehat D=(\operatorname{Id}-\widehat C)/2\)
在外边界非零，归一化位移同伦于 \(p/R\)：线性同伦 \(p-t\widehat C(p)\) 在球面保持非零。该外球可随完成增大，SC3 的缺额不变；不能假定初始指定球已包含任意完成的全部新增零点。

故 \(\deg(\widehat D,\operatorname{int}W_j,0)=\delta_j\)。若 \(\delta_j\ne0\)，该分量有零点。这给 SC4 下界。若全部新增零点有限且非退化，各点指数为
\(\operatorname{sgn}\det D\widehat D(q)=\operatorname{sgn}\det(I-D\widehat T(q))\in\{-1,1\}\)；加法性使数量至少 \(|\delta_j|\)，给 SC5 下界。非退化零点类自动有限：全部固定点紧，整个管边界无固定点，孤立点不可能在管外固定点集内部聚积。

### 任意整数指数的单点模型

对非零整数 \(k\)，把 \(\mathbb R^n=\mathbb C\times\mathbb R^{n-2}\)，定义
\[
A_k(z,w)=(f_k(z),w),\qquad
f_k(re^{it})=re^{ikt},\qquad f_k(0)=0.
\tag{SC6}
\]
它满足 \(\|A_k(x)\|=\|x\|\)，所以唯一零点为 0。\(f_k\) 在 \(z\ne0\) 的极坐标微分为两个旋转与 \(\operatorname{diag}(1,k)\) 的乘积，算子范数至多 \(\max(1,|k|)\)。沿线段积分；经过 0 的线段拆成两段并取极限，得到全域 Lipschitz 性。沿负实轴的极角跳变因整数 \(k\) 不改变映射值。

取小球内非零正实目标 \((a,0)\)。恰有 \(|k|\) 个原像，均有 \(w=0,|z|=a\)，各点微分行列式符号为 \(\operatorname{sgn}k\)，乘上其余坐标的恒等映射不改符号。正则值次数为 \(k\)，所以 \(\deg(A_k,B_\varepsilon,0)=k\)。这独立证明任意整数指数可由单个孤立零点承担，包含负数及高绝对值。

在所选小球 \(\overline B_{\varepsilon_j}(q_j)\subset\operatorname{int}W_j\) 指定
\(D(p)=A_{\delta_j}(p-q_j)\)，\(C(p)=p-2D(p)\)。球内完整近端固定点恰为 \(q_j\)，其局部指数为 \(\delta_j\)。对 SC5，改在 \(|\delta_j|\) 个不交小球用 \(D(p)=B_j(p-q)\)：正号取 \(B_j=I\)，负号取 \(B_j=\operatorname{diag}(-1,1,\ldots,1)\)。它们都是非退化模型。

### 去掉小球，原值延拓，再提升 Hölder

在每个 \(W_j\) 去掉选定小球的内部，得 \(V_j\)。\(n\ge2\) 时从连通流形内部去掉有限个不交闭球的内部仍连通：路径遇到球时可沿连通的球面改道。\(V_j\) 是紧、定向、连通的 \(n\) 维带边界流形。原边界位移的次数为 \(\delta_j\)，小球边界在 \(V_j\) 中定向反转；因此全部边界总次数为
\[
\delta_j-\sum_{q\text{ 位于 }W_j}\operatorname{ind}(q)=0. \tag{SC7}
\]
\(\delta_j=0\) 的分量不挖球。调用 C233 已逐项核验的一手 Hopf 延拓接口：[tom Dieck §2.10(2.10.1)，印页 74–75](https://www.uni-math.gwdg.de/tammo/GT03.pdf)，或 [Freire Extension Theorem，印页 74–75](https://web.math.utk.edu/~afreire/teaching/m562s26/notes_on_manifolds.pdf)。连续边界数据、可能不连通的边界、连通 \(V_j\) 和诱导总次数零全部满足；边界 cofibration 保持原值。得到无零的连续球值延拓，再把边界的正幅度以 \(\log\) 延拓，得到每个 \(V_j\) 上无零连续 \(D\)，与全部给定位移原样相接。

Hölder 提升不能省略。令 \(E\) 为原闭管与所有指定小球的并。各块内部 \(C\) 为有限 \(\gamma\)-Hölder；不同紧块间距离为正、有界值域控制跨块点对，故 \(C|_E\) 有某个有限全对 Hölder 常数。HE-EXT 给全域同指数基准 \(C_b\)，精确保持全部块。在 \(V=\bigcup_jV_j\) 上，连续 \(D\) 有正最小范数 \(m\)。以光滑向量函数一致逼近到 \(m/4\)，在全部内边界的薄 collar 使用 \(D_b=(\operatorname{Id}-C_b)/2\)，在外球边界使用 \(p/2\)。有限不交边界 collar 的凸 cutoff 拼接同 C233 Z4；每个参与项距 \(D\) 小于 \(m/4\)，故拼接范数至少 \(3m/4\)。

置 \(\widehat C=p-2D_h\) 于剩余区域，原闭管/小球上用指定 \(C\)，外球之外为 0。接缝附近精确使用共同 \(C_b\) 或 0；紧域有限局部 Hölder 界与远点对的有界值域界给某个有限全域 \(\widehat L\)。没有新增其它零点，整个原输入管完全保持，完成紧支撑。SC4、SC5 均达到。证毕。

<a id="scc-examples"></a>
## 指数与数量为何必须分开

以下都选择余维至少二的嵌入，保证管外连通；每个指定整管满足 SC1 后才调用结论。表中不认证最优 Hölder 常数或全域收敛。

| 零流形 | Euler 特征 | 缺额 | 最少一般孤立补偿点 | 最少非退化补偿点 |
| --- | ---: | ---: | ---: | ---: |
| 圆 \(S^1\subset\mathbb R^3\) | 0 | 1 | 1 | 1 |
| \(\mathbb{RP}^2\subset\mathbb R^5\) | 1 | 0 | 0 | 0 |
| 二球面 \(S^2\subset\mathbb R^4\) | 2 | −1 | 1 | 1 |
| 双柄闭曲面 \(\Sigma_2\subset\mathbb R^4\) | −2 | 3 | 1 | 3 |

双柄曲面可先嵌入 \(\mathbb R^3\) 再放入 \(\mathbb R^4\)；其一个 0 胞腔、四个 1 胞腔、一个 2 胞腔给 \(\chi=1-4+1=-2\)。RP² 使用 C234 的嵌入及胞腔计算。表的最后一行说明：缺额 3 能集中于一个指数 3 的孤立零点；要求非退化才必须分成至少三个点。SC6 的高指数模型通常不在零点处可微，不满足 SC5 条件；一般孤立点可承载高指数并不等于非退化点可承载它。

<a id="scc-singleton"></a>
## C237-v1 · 单点零集的精确最小预算及全域收敛

现在独立固定 \(M=\{m\}\)、\(N=\overline B_\rho(m)\)、\(\rho>0\)。允许任意实 Hilbert 空间 \(H\)，任意连续 \(T_0:N\to N\)，只要求
\[
T_0(m)=m,\quad\|T_0(p)-m\|\le\theta\|p-m\|,quad0\le\theta<1,
\quad L_0=[2T_0-\operatorname{Id}]_{\gamma,N}<\infty.
\tag{SC8}
\]
固定 \(0<\gamma<1\)。\(L_0\) 是给定数据的精确 Hölder 半范数，允许 0。令 \(P_N\) 为闭球的度量投影，定义
\[
\widehat C=C_0\circ P_N,\qquad\widehat T=(\operatorname{Id}+\widehat C)/2.
\tag{SC9}
\]
则
\[
[\widehat C]_{\gamma,H}=L_0,
\qquad\operatorname{Fix}\widehat T=\{m\},
\qquad\|\widehat T^k x-m\|\le q^k\|x-m\|,
\quad q=\max\{\theta,1/2\}<1.
\tag{SC10}
\]
因此在同一整管数据的保零完成类中，精确最小完成常数 \(L_*=L_0\)，且达到；每个指定预算 \(L\ge L_0\) 都可保常数完成。完整关系用 Z1，保持全部输入上的近端动力身份。这里没有全域单值原关系声称。

**证明。** 投影非扩张，故 \([C_0\circ P_N]_{\gamma,H}\le L_0\)；限制回 \(N\) 得反向不等式。这既证明达到，也给任何保持原数据的完成的预算下界。

对 \(r=\|x-m\|>\rho\)，\(p=P_Nx=m+\rho(x-m)/r\)，于是
\[
\widehat T(x)=T_0(p)+(x-p)/2,\qquad
\|\widehat T(x)-m\|\le\theta\rho+(r-\rho)/2
\le\max(\theta,1/2)r. \tag{SC11}
\]
\(r\le\rho\) 时直接用 SC8。因此每点都有同一径向严格收缩 SC10；唯一固定点为 \(m\)，归纳给全域点收敛。不是对任意两点的 Banach 收缩断言，不要求 \(T_0\) Lipschitz，不需选择最优点对使半范数取到。C0 有界且投影定义在全部 Hilbert 空间，所有公式良定。证毕。

<a id="scc-frontier"></a>
## 本轮关闭与留下的义务

- 关闭：有限新常数下的锐新增零点数，全部管外分量的必要充分条件，指定补偿位置与指数；一般孤立点/非退化点的不同精确代价。
- 关闭：单点严格球管的原常数完成，精确最小预算达到及全域径向收敛，包含非 Lipschitz 原数据和零半范数端点。
- 仍开放：\(\chi(M)=1\) 的非单点零流形，在固定整个原管的条件下，是否总能保持原 \(L\)；若不能，须给同一数据的定量反例。尤其 C234 的 RP² 完成最小常数及达到性尚未算出。
- 不混同：SC4/SC5 不是原常数预算定理，指定零点位置可能增大常数；单点投影不能直接用于非凸管，后者的最近点全域投影不自动连续。允许有限新常数的 Euler 分类没有授予全域吸引或发表优先。

**本轮实际攻击范围。** 下界从任意完成重新推外球同伦，构造则从指定局部指数独立推SC7，不把加法公式当构造存在。逐项核n≥2去球连通、负指数、边界定向、正则原像仅需局部可微、原闭管仅Hölder时的跨块与接缝、完整Z1图及全部新增点。单点分支独立用限制给预算下界、投影给上界、管外径向式给唯一零点；检查θ=0、θ=1/2、θ趋1和L0=0。有限迭代最初固定步数不足以达到θ接近1样例的目标精度，改用解析q界给步数后通过；这不是数学反例。未实施其它代理审查、全域Hopf数值构造或发表优先认证。

[有限复算](../code/sharp_completion_cost/README.md)检查指数模型、计数反算、精确预算样例和完整图参数化；没有实现 Hopf 无零延拓器，也不以有限搜索证明一般数学结论。
