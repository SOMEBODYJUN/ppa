# 准解析性给出精确近端动力学的正则性分界

用包含阶乘的总权重 \(M=(M_j)_{j\ge0}\)，\(M_0=1\)、\(M_j>0\)。假设 \(M_j/j!\) 对数凸。几何因子重标定不改变函数类，可使 \(M_1\ge1\)。在每个紧子集 \(Q\) 上，Roumieu 类 \(E^{\{M\}}\) 要求存在 \(C,h>0\) 使全部 \(j\) 有 \(\|D^j f\|_Q\le C h^j M_j\)。Beurling 类 \(E^{(M)}\) 要求每个 \(h>0\) 都有相应 \(C\)。阶数用多线性算子范数或局部所有多重偏导，有限维下一个指数因子可互相转换。

<a id="qpd-dichotomy"></a>
## C302 · 所有强对数凸总权重的准解析分界

固定 \(\lambda>0\)、有限维欧氏空间。权重的两侧由 \(\sum_{j\ge1}M_{j-1}/M_j\) 判别。

- **发散。** 对每个 \(f\in E^{\{M\}}\)，任何有界固定步长全局精确 PPA 轨道都有有限长度且收敛至一个临界点。只要求各步全局近端最小解存在。标准梯度下降的有界轨道同样有限长度，步长按 C299。
- **收敛。** [C297](exact_proximal_limit_sets.md#epl-characterization) 的每个同维可实现紧集，均由某个 \(f\in E^{(M)}\) 实现，且保留强制性、\(\nabla^2f\ge-I/(2\lambda)\)、完整光滑近端及指定聚点集等于完整全局最小集。可分别采用 C297 精确二次外尾或 [C298](exact_proximal_limit_sets.md#epl-budget) 的任意严格 Hölder 预算。标准梯度下降版本也可在该 Beurling 类实现。

因此在维数至少二时，准解析性恰是这组权重上所有有界精确近端轨道必有单点极限的分界。在一维，同维补分量边界已经只允许单点。准解析方向不对原权重附加导数封闭，非准解析构造亦无需假定原权重适度增长或强非准解析。

**准解析方向。** 在包含有界轨道及闭包于内部的紧盒上限制 \(f\)，扩到略大盒后仿射重标定。Rolin–Speissegger–Wilkie Theorem 1 对强对数凸准解析总权重使用移位类的并，故该限制在其 o-minimal 结构中可定义。原文末尾的更正约束抽象 Theorem 5.2，明确完整系统满足更正条件，具体 Theorem 1 仍适用。Kurdyka 的可定义梯度不等式给盒内部的 KL 性质。用 Attouch–Bolte–Svaiter Theorem 2.9，或直接应用其下降与相对误差论证：精确 PPA 给
\[
 f(x_k)-f(x_{k+1})\ge\|x_{k+1}-x_k\|^2/(2\lambda),\qquad
 \|\nabla f(x_{k+1})\|=\|x_{k+1}-x_k\|/\lambda .
\]
在紧盒外取 \(+\infty\) 得 proper 下半连续可定义扩展，盒内以原函数和值梯度验证 H1、H2。有界轨道和连续性给 H3。由定理得有限长度及临界收敛。梯度下降用 C299 整段的端点下降及全局 Lipschitz 梯度给相应 H1、H2。原轨道或导数仍属于同一个权重类均无需假设。

<a id="qpd-weight"></a>
## 非准解析时的内部权重

记 \(w_j=(M_j/j!)/(M_{j-1}/(j-1)!)\)，非降。令 \(v_j=\min(w_j,e^j)\)，则 \(v_j\) 非降，\(v_j\to\infty\)，且
\[
 \sum_j\frac1{jv_j}\le\sum_j\left(\frac1{jw_j}+\frac{e^{-j}}j\right)<\infty .
\]
取正阈值 \(T_i\uparrow\infty\)，使 \(\sum_i1/T_i<\infty\) 且
\[
 \sum_j\frac{\min(v_j/T_i,1)}{jv_j}\le2^{-i}.
\]
后者由支配收敛可逐个满足。设 \(d(t)=1+\sum_i\min(t/T_i,1)\)。它趋无穷，\(d(t)/t=1/t+\sum_i\min(1/T_i,1/t)\) 非增。于是
\[
 N_0=1,\qquad \frac{N_j}{N_{j-1}}=\frac{jv_j}{d(v_j)}
\]
定义强对数凸、非准解析且导数封闭的内部权重。非准解析由交换非负和得到 \(\sum_j d(v_j)/(jv_j)<\infty\)。导数封闭用 \(N_j/N_{j-1}\le j e^j\)。并且相邻比之商 \( (N_j/N_{j-1})/(M_j/M_{j-1})\le1/d(v_j)\to0\)，故 \(N\ll M\)，即 \((N_j/M_j)^{1/j}\to0\)。将 \(N\) 以几何因子归一化维持全部性质。于是对任意 \(A>0\) 都有
\[
 \sup_{m\ge0} A^m N_m/M_m<\infty. \tag{1}
\]
这一内部权重与任意非准解析总权重的常用缓增长子序列相关，但这里还保留除阶乘后的对数凸及导数封闭。下文使用 Rainer 综述 Corollary 3.12 的非负 \(E^{\{N\}}\) 截断，以及 Rainer–Schindl 的 composition / inversion 接口。它们对归一化 \(N\) 的条件成立，因为 \(N_j/j!\) 的根非降、包含解析函数，且导数封闭。

<a id="qpd-realization"></a>
## 全阶估计与平坦延拓

**解析几何输入。** 对 C297 的任一非单点 \(K\)，保留 Fokin 的正则嵌入尾。Johanis Theorem 1 或 Whitney 1934 Lemma 6 给参数开区间上任意精细的解析 \(C^1\) 逼近。用旧曲线的管投影参数 \(\pi\)，要求新曲线在旧管内，\((\pi\circ z)' >1/2\)、\(|\pi(z(t))-t|<1/4\)，且位置误差趋零。这些条件由逐参数位置与导数的足够小误差保证，给新曲线单射正则、在补集内 proper、聚点集恰为 \(K\)。此后用新解析曲线。正交管坐标的参数存在解析局部逆，可由 \(\langle x-z(t),z'(t)\rangle=0\) 及其非零参数导数看到。允许管半径随参数缩小，为避免引入任意光滑数据，可用同一精细逼近取严格低于安全光滑半径的正解析半径。截断对正交位移平方除以该半径平方作 \(E^{\{N\}}\) 复合。

**均匀的局部全阶界。** 取同一个非负 \(E^{\{N\}}\) 一维 bump 的整数平移，正值区重叠覆盖参数尾部。与 C297 同样取它们的正线性组合 \(w_0\)，令 \(\rho(t)=\int_t^\infty w_0(u)\,du\)。在第 \(j\) 个紧参数段及小重叠上，对 \(\rho,\rho'\) 可以同时要求
\[
 \sup |D^m\rho|+\sup |D^m\rho'|\le \delta_j A_0^m N_m\qquad(m\ge0), \tag{2}
\]
其中 \(A_0\) 统一，\(\delta_j>0\) 可事先任意小。对 \(m\ge1\)，\(\rho\) 的导数是局部各 bump 的低一阶导数，\(\rho'\) 的导数为原 bump 导数。所需有限种邻接平移的幅度可统一控制，且 \(N_{m-1}\le N_m\)。对 \(m=0\) 把各项积分也限定为更早已指定预算的最小值乘可和几何因子。全程系数严格正，所以 \(\rho'<0\)。

在一个固定的闭管计算段，C297 的平方内部写为
\[
 \rho+\rho'\,\mathcal B(x,\rho,\rho'),
\]
其中 \(\mathcal B\) 在小幅度变量上与 \(x\) 同时解析，因为精确弦的逆在零附近解析，且 \(v/(2\rho)\) 已因式分解。各固定局部的解析导数满足 Cauchy 型 \(C A^m m!\)，远离逆分支边缘。由 (2) 有
\[
 \|D^m H_1\|\le C_j\delta_j^2 A_j^m N_m
 \quad(m\ge0,\ 0<\delta_j\le\delta_j^0), \tag{3}
\]
其中 \(C_j,A_j\) 与 \(\delta_j\) 无关。为核这点，置 \(W_m=N_m/m!\)。归一化 \(m\) 阶导数后，解析外函数复合的第 \(k\) 项由对所有有序分解 \(r_1+\cdots+r_k=m\) 求和控制，每项内函数权重因子 \(\prod_i W_{r_i}\le W_m\)，来自 \(W\) 对数凸和 \(W_0=1\)。分解数至多 \(2^{m-1}\)，其余解析系数、有限维坐标数与输入常数只贡献指数因子。反过来，\(\rho\circ t(x)\)、\(\rho'\circ t(x)\) 的外函数含 \(\delta_j W_k\)，而内函数 \(t(x)\) 解析，故用 \(W_k\le W_m\) 同样保持线性幅度 \(\delta_j\)。两个因子相乘仍保留权重：导数除以 \(m!\) 后用 \(W_l W_{m-l}\le W_m\)，至多 \(m+1\) 个分拆。平方因此带来 \(\delta_j^2\)，乘固定截断后仍如此。解析逆、管坐标和截断在每个将用的紧段先固定，故无需假定它们的常数全局一致。

**同一函数的 Beurling 控制。** 令 \(d_j\le1\) 为第 \(j\) 个闭管截断段与 \(K\) 的距离。令 (3) 的 \(C_j\delta_j^2\sup_m (j A_j)^m N_m/M_m\le2^{-j}d_j^2\)，由 (1) 可做。再纳入 C297 的 \(h<1/4\)、\(|h'|<1/2\)、曲线像振幅及整体二阶小预算。于是对每个固定 \(h_0>0\)，从 \(j\ge1/h_0\) 起全阶在该段满足 \(\|D^mH_1\|\le2^{-j}d_j^2 h_0^m M_m\)。较早有限段属于 \(E^{\{N\}}\subset E^{(M)}\)。每个导数跨 \(K\) 的零延拓仍由距离的二次小量保证，故 \(H_1\in E^{(M)}\)，且仍保留精确弦。没有把有限阶小量直接当成全阶界。

C297 的辅助非负 \(q\) 取在补集覆盖上的 \(E^{\{N\}}\) bump。每个紧支撑 bump 的全阶可用 \(C_jA_j^mN_m\) 界，利用 (1) 选其正振幅使第 \(j\) 项在所有 \(m\) 上至多 \(2^{-j}M_m/j^m\)。每个给定 \(h_0\) 的级数尾遂在对应 Beurling 半范数收敛，少数首项也属于该类。每点的正性和 \(S\) 上全阶零不变。对 C297 的二次尾，固定 \(E^{\{N\}}\) bump 积分成单调截断即可，凸尾本身局部属于 \(E^{\{N\}}\)。此后按 C297 的精确近端方程与采样证明完成。

对 C298 的严格预算，选解析光滑凸 \(B\) 逼近凸包，以防普通光滑边界引入非受控几何。例如把凸包距离平方用方差小的正 Gaussian 卷积，再加小正二次项。Gaussian 卷积解析，因为复小邻域有一致可积的 Gaussian 及多项式增长控制。Jensen 保证卷积不低于原距离平方，在 \(K\) 上又至多为 Gaussian 的二阶矩。略高的水平集给所需包围及直径，额外二次项保证严格凸且边界正则。正外法线参数在边界领口及整个外部局部解析可逆。因此 C298 的距离外尾用 \(E^{\{N\}}\) 截断及积分，内侧保留 \(E^{(M)}\) 核，所有 \(C^2\) 全域估计照旧。若要同一构造再经 Moreau 包络保持权重，可先取满足上述条件的内部导数封闭 \(P\ll M\)，对 \(P\) 应用已证构造，然后通过 \(P\) 中的导数、逆与复合闭性得到包络，最后嵌入 \(E^{(M)}\)。

<a id="qpd-scale"></a>
## 对数临界尺度与文献范围

令 \(M_j^{(\alpha)}=j!\prod_{i=1}^j \log(i+e)^\alpha\)，\(\alpha\ge0\)。除阶乘后的相邻比非降，准解析判据为 \(\sum_{j\ge1}[j\log(j+e)^\alpha]^{-1}\)，恰在 \(\alpha\le1\) 发散。故这个族在 \(\alpha=1\) 有精确分界。对任意有限 \(\alpha>1\)，此权重严格小于每个 \((j!)^s\)（\(s>1\)）的等级，因此同一个构造可以属于所有这些局部 Roumieu Gevrey 类。Gevrey 任意接近解析的结论不要求套用强非准解析的同阶 Whitney 延拓。

- Rolin–Speissegger–Wilkie，JAMS **16** (2003), 751–777，Theorem 1 与末尾更正，给准解析侧结构。[原文 DOI](https://doi.org/10.1090/S0894-0347-03-00427-2)，[全文转录](https://www.academia.edu/59742720/Quasianalytic_Denjoy_Carleman_classes_and_o_minimality)。Kurdyka，AIF **48** (1998), 769–783, Theorem 1，[全文](https://www.numdam.org/article/AIF_1998__48_3_769_0.pdf)。Attouch–Bolte–Svaiter Theorem 2.9，[正文](https://bolte.perso.math.cnrs.fr/MPA.pdf)。Lageman 2007 的 analytic-geometric 连续/离散梯度型收敛是相邻既有先行。[DOI](https://doi.org/10.1002/mana.200410564)。
- 解析精细逼近用 Johanis 2015 Theorem 1，[原文](https://emis.de/ft/27712)。非准解析截断用 Rainer 2022 Corollary 3.12，[原文](https://www.mat.univie.ac.at/~armin/publ/survey-UET.pdf)。稳定性用 Rainer–Schindl, *Equivalence of stability properties for ultradifferentiable function classes*, Theorems 1–2，[原文](https://www.mat.univie.ac.at/~armin/publ/equivalence_publ.pdf)。Rainer–Schindl 2014 §5.19–5.21 已知所有非解析 Gevrey 的交本身非准解析，[原文](https://www.tuwien.at/mg/arainer/wp-content/uploads/2025/03/composition1-publ.pdf)。
- Haraux–Jendoubi arXiv:1502.06841 的 Remark 9.1.2 对特定连续梯度圆例的 \(G^{1+1/k}\) 正则性提出猜测。这里的构造解决的是整个权重族和精确离散轨道的实现，不凭此断定原指定公式的正则性或猜测在刊本后的当前状态。[原文](https://arxiv.org/pdf/1502.06841)。Fokin 的拓扑类与近端离散的具体增量见 [C297 先行范围](exact_proximal_limit_sets.md#epl-prior)。
