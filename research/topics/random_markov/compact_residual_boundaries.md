# 紧 Markov 同步残差：一般模、无正幂界与两种假零

本页先补全 C14 的通用紧性与 gauge 定理，再固定三个不同对象。C143 是紧可数二映射模型；C144 是连续正方形上的随机投影；末节复核 C71 的四状态 OT 放松。三者均使用完整平方欧氏运输成本，但状态、映射和假零机制分别定义。历史材料只作末尾溯源，以下证明不以其省略内容为前提。

<a id="crb-residual"></a>
## 1. 残差与量词

给定紧集 \(G\subset\mathbb R^d\)、有限个连续自映射 \(T_j:G\to G\) 和概率 \(p_j\ge0\)、\(\sum_jp_j=1\)。实际链每步用与当前状态独立的新指标。对 \(G\) 上 Borel 概率律写

\[
\mu P=\sum_jp_j(T_j)_\#\mu,\qquad
\mathcal I=\{\pi:\pi P=\pi\}\ne\varnothing,\qquad
d(\mu)=\min_{\pi\in\mathcal I}W_2(\mu,\pi).
\tag{B1}
\]

\(W_2\) 使用 \(\|x-y\|^2\)，不是概率向量的 Euclidean 范数。令 \(\operatorname{Opt}(\mu,\pi)\) 是这对完整边缘的 \(W_2\)-最优计划集；定义

\[
c_R(x,y)=\sum_jp_j\|(x-T_jx)-(y-T_jy)\|^2,
\qquad
\Psi(\mu)^2=
\min_{\pi\in\mathcal I}\min_{\eta\in\operatorname{Opt}(\mu,\pi)}\int c_R\,d\eta.
\tag{B2}
\]

每一对状态共用同一个 \(j\)。外层遍历全部不变律，不预设最近不变律；内层必须最优，不能先最小化 \(c_R\) 而忘掉输入运输成本。\(\Psi\)、\(W_2(\mu,\mu P)\) 与条件刷新残差是不同函数。

本页的严格一般 gauge 指连续、严格递增、无界的 \(\rho:[0,\infty)\to[0,\infty)\)，且 \(\rho(0)=0\)。局部正幂 EB 在 \(\bar\pi\in\mathcal I\) 的含义为

\[
\exists q>0, K<\infty, r>0\quad
\forall\mu:\ W_2(\mu,\bar\pi)<r
\Longrightarrow d(\mu)\le K\Psi(\mu)^q.
\tag{B3}
\]

可取 \(K\ge0\)；负系数不提供非平凡上界。以下失败结论对每个 \(q>0,K\ge0,r>0\) 给同一已固定系统内的见证律。

<a id="crb-compact-gauge"></a>
### 紧性引理：本页有限连续随机表示所需的全部门

\(\mathscr P(G)\) 在 \(W_2\) 下紧；\(P\) 连续，\(\mathcal I\) 紧，(B1)–(B2) 中的极小值取得，\(\Psi\) 下半连续。若 \(\Psi^{-1}(0)=\mathcal I\)，则存在严格一般 gauge 使

\[
d(\mu)\le\rho(\Psi(\mu))\qquad(\mu\in\mathscr P(G)).
\tag{B4}
\]

**证明。** 紧度量空间上的概率律弱序列紧，且在有界空间上弱收敛等价于 \(W_2\) 收敛。这两个基础紧性事实可由有限网格重构：逐级取细有限分割，使每格直径趋零，对格质量作对角抽取；连续函数在每格的振幅趋零给极限积分。反过来，在极限律的零质量边界处分割，弱收敛使同格可匹配质量趋于 1；同格运输成本至多网格直径平方，其余成本至多 \(\operatorname{diam}(G)^2\)。于是 \(W_2\) 成本趋零。相同论证适用于 \(G\times G\)。

对连续测试函数 \(f\)，\(\sum_jp_jf(T_jx)\) 连续，故 \(P\) 连续，\(\mathcal I\) 闭且紧。固定边缘的计划集非空紧；连续运输成本取到最小值。由三角不等式，\((\mu,\pi)\mapsto W_2(\mu,\pi)\) 连续，故最优性约束

\[
\int\|x-y\|^2d\eta=W_2(\mu,\pi)^2
\]

是闭条件。\(c_R\) 连续有界，因此 (B2) 的联合可行集非空紧且目标连续，极小值取得。若 \(\mu_k\to\mu\)，先取目标值趋于下极限的子列，再从其极小对 \((\pi_k,\eta_k)\) 抽收敛子列。极限仍可行，故 \(\Psi(\mu)^2\le\liminf_k\Psi(\mu_k)^2\)。

现在令 \(\omega(s)=\sup\{d(\mu):\Psi(\mu)\le s\}\)。对角计划保证 \(\Psi=0\) 于 \(\mathcal I\)，故集合非空；\(\omega\) 有界、非降，exact-zero 给 \(\omega(0)=0\)。若 \(s_k\downarrow0\) 而某些 \(\mu_k\) 满足 \(\Psi(\mu_k)\le s_k,d(\mu_k)\ge\epsilon>0\)，紧性及下半连续给一个距离至少 \(\epsilon\) 的零残差极限，矛盾。因此 \(\omega(s)\to0\)。

取 \(B>\operatorname{diam}(G)\)，递归选 \(s_n\downarrow0\)、\(s_{n+1}<s_n/2\)、\(\omega(s_n)\le B2^{-n}\)。指定 \(\rho(0)=0\)、\(\rho(s_n)=B2^{1-n}\)，相邻结点间线性插值，并在 \(s\ge s_1\) 置 \(\rho(s)=B+s-s_1\)。在 \([s_{n+1},s_n]\)，有 \(\rho(s)\ge B2^{-n}\ge\omega(s_n)\ge\omega(s)\)；在更大参数上 \(\rho\ge B>\omega\)。这给 (B4) 的严格 gauge。反向若有任何零处取零的 gauge 界，\(\Psi(\mu)=0\) 必给 \(d(\mu)=0\)，因 \(\mathcal I\) 闭而 \(\mu\in\mathcal I\)。证毕。

以上是本页有限随机表示的直接证明。下面在 C14 原有的共同 a.e. 连续量词下，补全任意噪声域的同一结论。

<a id="crb-general-gauge"></a>
### C14：任意噪声域上的同一紧性与 gauge 命题

- **Status**：`derived-checked`，这是 C14 原命题在其原 a.e. 连续量词下的证明补全，不改变残差或输入最优计划域。
- **完整量词**：固定非空紧集 \(G\subset\mathbb R^d\)、任意概率空间 \((\Xi,\mathcal F,\vartheta)\)，以及映射 \(T:\Xi\times G\to G\)，对 \(\mathcal F\otimes\mathcal B(G)\) 与 \(\mathcal B(G)\) 联合可测。存在**一个共同的**可测集 \(\Xi_0\in\mathcal F\)、\(\vartheta(\Xi_0)=1\)，使每个 \(\xi\in\Xi_0\) 的完整自映射 \(x\mapsto T_\xi x\) 在整个 \(G\) 连续。不要求关于 \(\xi\) 的连续性，不要求统一 Lipschitz 常数，也不要求噪声空间可数或标准 Borel。实际每步指标独立同分布为 \(\vartheta\)，并独立于当前状态。

原 CM-M §1 的“\(T_\xi:G\to G\) continuous for almost every \(\xi\)”正是上述**先取满概率噪声集、再量化全部状态**的量词。本节不把它换成“对每个状态另选异常集”或只在状态分布几乎处处连续的条件；那些是不同前件。

对每个 Borel 集 \(A\subseteq G\)，定义

\[
P(x,A)=\int_\Xi\mathbf1_A(T_\xi x)\,\vartheta(d\xi),\qquad
(\mu P)(A)=\int_G P(x,A)\,\mu(dx).
\tag{CG1}
\]

继续取 \(\mathcal I=\{\pi:\pi P=\pi\}\)、\(d(\mu)=\inf_{\pi\in\mathcal I}W_2(\mu,\pi)\)，并用**同一指标**定义

\[
c_R(x,y)=\int_\Xi\|(x-T_\xi x)-(y-T_\xi y)\|^2\,\vartheta(d\xi),
\]
\[
\Psi(\mu)^2=\inf_{\pi\in\mathcal I}\ 
\inf_{\eta\in\operatorname{Opt}(\mu,\pi)}\int_{G\times G}c_R(x,y)\,\eta(dx,dy).
\tag{CG2}
\]

C14 原先假设 \(\mathcal I\ne\varnothing\)，本节保留该命题身份；下面另证明此非空性其实已由当前紧性与连续性前件保证。**结论**是：核连续、\(\mathcal I\) 紧、(CG2) 极小值取得、\(\Psi\) 下半连续，且

\[
\Psi^{-1}(0)=\mathcal I
\quad\Longleftrightarrow\quad
\exists\text{严格一般 gauge }\rho\quad
\forall\mu\in\mathscr P(G):\ d(\mu)\le\rho(\Psi(\mu)).
\tag{CG3}
\]

**可测性和连续性。** 联合可测性使 \(x\mapsto P(x,A)\) 可测；对固定 \(x\)，(CG1) 是概率测度，所以 \(P\) 是 Markov 核。对任意有界 Borel 函数 \(f\)，有限测度的 Fubini 定理给

\[
\int_G f\,d(\mu P)
=\int_G\int_\Xi f(T_\xi x)\,\vartheta(d\xi)\,\mu(dx).
\tag{CG4}
\]

这里可测且有界，绝对可积，交换积分的门已满足。因而 (CG1) 等于随机自映射的平均推前，也正是独立新指标下的一步律。

若 \(f\in C(G)\)、\(x_n\to x\)，则对于**同一个** \(\Xi_0\) 内每个 \(\xi\)，有 \(f(T_\xi x_n)\to f(T_\xi x)\)；绝对值统一不超过 \(\|f\|_\infty\)。有界控制收敛得到
\(Pf(x_n)\to Pf(x)\)，故 \(Pf\in C(G)\)。于是 \(\mu_n\to\mu\) 弱收敛时，(CG4) 使 \(\mu_nP\to\mu P\) 弱收敛；由前述紧状态空间上的弱收敛/\(W_2\) 等价，这也是 \(W_2\) 连续。

令 \(D=\operatorname{diam}(G)\)。位移函数在 \(\Xi\times G\) 联合可测，故同步平方成本在 \(\Xi\times G\times G\) 可测，并且处处满足

\[
0\le\|(x-T_\xi x)-(y-T_\xi y)\|^2\le4D^2.
\tag{CG5}
\]

若 \((x_n,y_n)\to(x,y)\)，同一 \(\Xi_0\) 上被积函数逐点收敛。常数 \(4D^2\) 可积；再次控制收敛给 \(c_R(x_n,y_n)\to c_R(x,y)\)。因此 \(c_R\) 在完整 \(G\times G\) 上连续有界。这里没有在某个状态相关异常集之外偷取统一结论。

**不变律非空及紧性。** 任取 \(\mu_0\in\mathscr P(G)\)，定义 Cesàro 平均 \(\sigma_N=N^{-1}\sum_{k=0}^{N-1}\mu_0P^k\)。概率律紧性给一个弱收敛子列 \(\sigma_{N_j}\to\pi\)。对任意 \(f\in C(G)\)，

\[
\left|\int f\,d(\sigma_NP)-\int f\,d\sigma_N\right|
=\frac1N\left|\int f\,d(\mu_0P^N)-\int f\,d\mu_0\right|
\le\frac{2\|f\|_\infty}{N}.
\tag{CG6}
\]

核连续使极限满足 \(\int f\,d(\pi P)=\int f\,d\pi\)；连续函数区分紧度量空间上的概率律，故 \(\pi P=\pi\)。又 \(\mathcal I\) 是连续映射 \(\mu\mapsto\mu P\) 的固定点集，因而闭且紧。这既验证原有的非空假设，也表明本结论不需先有轨道收敛。连续距离函数在 \(\mathcal I\) 上取到最小值，且 \(|d(\mu)-d(\nu)|\le W_2(\mu,\nu)\)。

**联合最优计划闭性、取得与下半连续。** 对每对边缘 \((\mu,\pi)\)，产品计划说明耦合集非空；其边缘约束闭，故在紧的 \(\mathscr P(G\times G)\) 中紧。连续成本 \(C(x,y)=\|x-y\|^2\) 取到最小值，所以 \(\operatorname{Opt}(\mu,\pi)\ne\varnothing\)。若
\((\mu_n,\pi_n,\eta_n)\to(\mu,\pi,\eta)\)，且每个 \(\eta_n\) 边缘为 \((\mu_n,\pi_n)\)、\(\pi_n\in\mathcal I\)、\(\eta_n\in\operatorname{Opt}(\mu_n,\pi_n)\)，则边缘投影和 \(\mathcal I\) 的闭性保留边缘和不变约束。最优性也保留，因为

\[
\int C\,d\eta
=\lim_n\int C\,d\eta_n
=\lim_n W_2(\mu_n,\pi_n)^2
=W_2(\mu,\pi)^2.
\tag{CG7}
\]

最后一步由 \(W_2\) 三角不等式对两边缘的连续性给出。因此联合可行关系是紧空间中的闭集；固定 \(\mu\) 的纤维非空紧。\(c_R\) 连续保证 (CG2) 两层 infimum 联合取得。这一步保留全部不变目标与该目标对应的**输入最优**计划，不把目标预先固定为最近不变律。

现在给任意 \(\mu_n\to\mu\)。\(0\le\Psi^2\le4D^2\)，可取一个实现目标值下极限的子列；给其各项取极小对 \((\pi_n,\eta_n)\)，再抽收敛子列。由 (CG7)，极限对可用于 \(\mu\)，所以
\(\Psi(\mu)^2\le\int c_Rd\eta=\liminf_n\Psi(\mu_n)^2\)。平方根连续递增，故 \(\Psi\) 下半连续。无需对全部 \(\mu\) 构造可测的极小计划选择。

**严格 gauge 的两个方向。** 不变律的对角计划输入最优且同步成本为零，故 \(\mathcal I\subseteq\Psi^{-1}(0)\)。假设 exact-zero。对 \(s\ge0\)，令
\(\omega(s)=\max\{d(\mu):\Psi(\mu)\le s\}\)。子水平集由下半连续性闭，由不变律非空而非空，因此紧；距离连续，最大值存在。\(\omega\) 非降、\(0\le\omega\le D\)、\(\omega(0)=0\)。若存在 \(s_n\downarrow0\) 与 \(\omega(s_n)\ge\epsilon>0\)，取相应极大律并抽收敛子列；下半连续性给极限 \(\Psi=0\)，距离连续性给极限距离至少 \(\epsilon\)，与 exact-zero 矛盾。因此 \(\omega(s)\to0\)。

为保留严格连续可逆的 gauge，而非只有非降包络，取 \(B>D\)，逐次选 \(s_{n+1}<s_n/2\)、\(\omega(s_n)\le B2^{-n}\)。设 \(\rho(0)=0\)、\(\rho(s_n)=B2^{1-n}\)，相邻结点间线性插值，\(s\ge s_1\) 则设 \(\rho(s)=B+s-s_1\)。每段斜率正，结点值趋零，尾部无界；故 \(\rho\) 连续严格递增、无界。在 \([s_{n+1},s_n]\)，\(\rho(s)\ge B2^{-n}\ge\omega(s_n)\ge\omega(s)\)，在 \([s_1,\infty)\) 上则 \(\rho\ge B>D\ge\omega\)。遂对全部律得 \(d(\mu)\le\omega(\Psi(\mu))\le\rho(\Psi(\mu))\)。反向 (CG3) 的 gauge 界在 \(\Psi(\mu)=0\) 时给 \(d(\mu)=0\)，紧闭 \(\mathcal I\) 使 \(\mu\in\mathcal I\)。证毕。

有限随机表示是取 \(\Xi=\{j\}\)、\(\vartheta(\{j\})=p_j\) 的特例；零概率指标的连续性无关。C143 和 C144 使用此前件，分别说明 (CG3) 不给任何正幂模，以及 exact-zero 本身不能由一步平稳反推。本节未使用 almost-firm 不等式、动力收敛或外部运输正则性定理，也不宣称 \(\Psi\) 上半连续。

<a id="crb-object"></a>
## 2. C143-v1：紧可数二映射完整对象

- **Status**：`derived-checked`，范围限下述固定对象及本页证明中的量词。
- **对象**：对每个整数 \(n\ge1\)，置

\[
t_n=2^{-n},\quad \delta_n=2^{-3n-10},\quad e_n=\delta_n^n,\quad h_n=2-e_n,
\qquad G_n=t_n+\delta_n\{0,1/2,1,h_n\},
\]
\[
G=\{0\}\cup\bigcup_{n\ge1}G_n\subset\mathbb R.
\tag{B5}
\]

为免 Dirac 符号与尺度混淆，本页 \(\delta_n\) 是正标量，\(\delta_x\) 是点 \(x\) 的 Dirac 律。写块内点为 \(x_{n,0},x_{n,m},x_{n,1},x_{n,h}\)，其顺序就是 (B5) 的顺序。映射完全由表给定：

| 输入 | \(x_{n,0}\) | \(x_{n,m}\) | \(x_{n,1}\) | \(x_{n,h}\) | \(0\) |
| --- | --- | --- | --- | --- | --- |
| \(T\) | \(x_{n,1}\) | \(x_{n,m}\) | \(x_{n,0}\) | \(x_{n,1}\) | \(0\) |

每步以 \(7/8\) 选恒等映射，以 \(p=1/8\) 选 \(T\)。因此

\[
P=\tfrac78 I+\tfrac18T_\#,\qquad
c_R(x,y)=\tfrac18|(x-Tx)-(y-Ty)|^2.
\tag{B6}
\]

距离、全部不变律和 \(\Psi\) 严格取 (B1)–(B2)。

<a id="crb-theorem"></a>
### 精确结论

1. \(G\) 紧，\(T\) 在 \(G\) 上 \(L=5/4\)-Lipschitz。全部状态对满足期望 almost-firm 式
   \[
   \mathbb E|T_\xi x-T_\xi y|^2+c_R(x,y)
   \le(1+45/64)|x-y|^2.
   \tag{B7}
   \]
   这里对应 \(\alpha=1/2\)、\(\tau=(1-\alpha)/\alpha=1\)。
2. \(\mathcal I\) 恰为以下所有律：每块第四点质量为零、第一和第三点质量相等；各中点与 0 的质量任意且总质量为 1。原同步残差满足 \(\Psi^{-1}(0)=\mathcal I\)，并有 (B4) 的严格一般 gauge。
3. 对每个 \(\mu\in\mathscr P(G)\)，
   \[
   d(\mu P)^2\le\frac{3125}{3267}d(\mu)^2.
   \tag{B8}
   \]
   令 \(R\mu=T_\#\mu\)、\(\Pi\mu=(R\mu+R^2\mu)/2\)、\(r_0=\sqrt{7/8}\)、\(C=\sqrt2L^2(1+L^2)\)。同一个 \(C,r_0\) 对全部 \(\mu\) 和全部整数 \(k\ge0\) 给
   \[
   \Pi\mu\in\mathcal I,\qquad
   W_2(\mu P^k,\Pi\mu)\le Cr_0^kd(\mu),
   \tag{B9}
   \]
   \[
   \sum_{k\ge0}W_2(\mu P^{k+1},\mu P^k)
   \le C\frac{1+r_0}{1-r_0}d(\mu).
   \tag{B10}
   \]
   这是律空间有限长度；不声明随机样本路径有限长度。(B8)–(B10) 的常数不声称最优。
4. 在同一个不变律 \(\delta_0\) 的每个正半径 \(W_2\) 球内，每个正幂 EB 都失败：
   \[
   \forall q>0\ \forall K\in[0,\infty)\ \forall r>0\ \exists\nu:\quad
   W_2(\nu,\delta_0)<r,\qquad d(\nu)>K\Psi(\nu)^q.
   \tag{B11}
   \]

下文完整证明四项。(B11) 不排除一般 gauge；它也不反驳固定有限状态的 C15。

<a id="crb-block"></a>
## 3. 有限块运输的直接证书

先允许 \(0\le e\le1/100\)，置 \(h=2-e\)，状态 \((0,1/2,1,h)\)，映射 \(T=(1,1/2,0,1)\)，更新概率仍为 \(1/8\)。以**行概率向量** \(v=(a,b,c,d)\) 表示律，转移矩阵为

\[
Q=\begin{pmatrix}
7/8&0&1/8&0\\0&1&0&0\\1/8&0&7/8&0\\0&0&1/8&7/8
\end{pmatrix}.
\tag{B12}
\]

解 \(vQ=v\) 得 \(d=0,a=c\)，故不变律正是 \((r,1-2r,r,0)\)、\(0\le r\le1/2\)。令 \(E_e(v)\) 为 \(v\) 到这整个不变律集的平方 \(W_2\) 距离。

目的点只有 \(z=0,1/2,1\)。允许目的质量自由，但必须使到 0 与到 1 的总质量相等。为每个实数 \(\lambda\) 设

\[
g_\lambda(0)=\lambda,\quad g_\lambda(1/2)=0,\quad g_\lambda(1)=-\lambda,
\qquad
f_\lambda(x)=\min\{x^2-\lambda,(x-1/2)^2,(x-1)^2+\lambda\}.
\tag{B13}
\]

逐点有 \(f_\lambda(x)+g_\lambda(z)\le|x-z|^2\)，而不变目的律的 \(g\) 积分是 0，因此

\[
E_e(v)\ge\sup_{\lambda\in\mathbb R}\sum_xv_xf_\lambda(x).
\]

这里等号不需额外引用 LP 强对偶。右侧是凹分段仿射函数 \(F\)。在 \(\lambda<-1/4\) 每个 \(f_\lambda(x)\) 非降；在 \(\lambda>h-3/4\) 每个 \(f_\lambda(x)\) 非增（代入四个 \(x\) 的三条直线即得）。故可在紧区间 \([-1/4,h-3/4]\) 取最大值 \(\lambda_*\)。

在最大值处，所有当前最小直线的斜率按行权重相加所能组成的区间包含 0：否则 \(F\) 的左右导数同为正或同为负，不能最大。三条候选直线的斜率分别为 \(-1,0,1\)。于各源点按适当比例把该行质量分给取到最小值的目的点，使加权斜率为 0；等价于总到达 0 与 1 的质量相等。此计划的逐对不等式全取等，目的律不变。因此

\[
E_e(v)=\max_{\lambda\in[-1/4,h-3/4]}\sum_xv_xf_\lambda(x).
\tag{B14}
\]

此论证同时给出一个最优原问题计划。零行质量无须选择条件比例。

在 \(e=0\) 时，三线下包络的全部断点为 \(-3/4,-1/4,1/4,3/4,5/4,7/4\)；外侧两个分别被 \(-1/4,5/4\) 的向量逐分量控制。四个剩余断点给行向量

\[
f_A=(1,0,-1,3)/4,\quad f_B=(-1,0,1,5)/4,
\quad f_C=(-3,-2,1,7)/4,\quad f_D=(-5,-4,-1,9)/4,
\]
\[
E_0(v)=\max_{j=A,B,C,D}vf_j^T.
\tag{B15}
\]

在任意两断点间 \(F\) 仿射，故无遗漏的内点极大值。置 \(q_0=15/16\)，直接有理运算给

\[
\begin{aligned}
q_0(\tfrac9{10}f_A+\tfrac1{10}f_B)^T-Qf_A^T&=(0,0,0,\tfrac18)^T,\\
q_0(\tfrac1{10}f_A+\tfrac9{10}f_B)^T-Qf_B^T&=0,\\
q_0(\tfrac2{15}f_A+\tfrac{23}{30}f_C+\tfrac1{10}f_D)^T-Qf_C^T&=(0,\tfrac3{64},0,0)^T,\\
q_0(\tfrac{11}{90}f_A+\tfrac{79}{90}f_D)^T-Qf_D^T&=(\tfrac18,\tfrac{17}{96},\tfrac9{64},0)^T.
\end{aligned}
\tag{B16}
\]

每个左侧第一项是 \(q_0\) 乘凸组合、每个右侧非负。左乘任意概率行 \(v\)，再对 \(j\) 取最大，得 \(E_0(vQ)\le(15/16)E_0(v)\)。

将源第四点 2 移到 \(2-e\) 不变可行运输质量。其到每个 \(z\in\{0,1/2,1\}\) 的成本比为
\((1-e/(2-z))^2\in[(1-e)^2,1]\)；其余成本不变。因此

\[
(1-e)^2E_0(v)\le E_e(v)\le E_0(v),\qquad
E_e(vQ)\le\frac{15}{16(1-e)^2}E_e(v).
\tag{B17}
\]

最后固定 \(s=1/4\)、\(v_s=(s,1-2s,0,s)\)。保留源 0 和中点质量、把第四点质量全送到 1，产生不变目标 \((s,1-2s,s,0)\)，成本 \(s(1-e)^2\)。在 (B13) 取 \(\lambda=1/4\)，源值为 \((-1/4,0,1/4,(h-1)^2+1/4)\)，其与 \(v_s\) 的积也为 \(s(1-e)^2\)。故

\[
E_e(v_s)=s(1-e)^2.
\tag{B18}
\]

<a id="crb-global-transport"></a>
## 4. 由块到整个可数域：几何、距离与收缩

\(e_n\le1/100\)、\(\delta_{n+1}=\delta_n/8\)、\(t_n/\delta_n=2^{2n+10}\ge4096\)。每块四点不同，各块分离，唯一聚点为 0；所以 \(G\) 紧。块内最大割线斜率为 \(1/(1-e_n)\le100/99\)，且 \(|Tx-x|\le\delta_n\)。对 \(n<m\)，

\[
\operatorname{dist}(G_n,G_m)\ge t_n/2-\delta_n/4
\ge4(\delta_n+\delta_m).
\tag{B19}
\]

第一步用 \(t_m\le t_n/2\)、\(h_m\delta_m\le2\delta_n/8\)；第二步用上述 \(4096\) 余量。于是跨块有 \(|Tx-Ty|\le|x-y|+\delta_n+\delta_m\le(5/4)|x-y|\)。与 0 的点对由 \(|x|\ge t_n\ge4096\delta_n\) 同样得界。故 \(T\) 全域 \(L=5/4\)-Lipschitz，\(I-T\) 为 \(9/4\)-Lipschitz，

\[
\mathbb E|T_\xi x-T_\xi y|^2+c_R(x,y)
\le\left[\tfrac78+\tfrac18\bigl((5/4)^2+(9/4)^2\bigr)\right]|x-y|^2
=\tfrac{109}{64}|x-y|^2,
\]

即 (B7)。各块和 0 在转移下分别封闭；逐单点平稳方程给 §2 所述全部不变律。不能把守恒块质量假定为最近目标必须保持的质量；下面直接证明这件距离事实。

设 \(S=G\setminus\{x_{n,h}:n\ge1\}\)，每个不变律均支撑于 \(S\)。令 \(m_n=\mu(G_n)\)；若 \(m_n>0\)，令 \(v_n\) 是该块条件质量向量。则

\[
\boxed{d(\mu)^2=\sum_{n\ge1}m_n\delta_n^2E_{e_n}(v_n).}
\tag{B20}
\]

\(m_n=0\) 的项定义为 0，不选任意条件律。为证下界，对每个正质量块选 (B14) 的 \(\lambda_n\in[-1/4,h_n-3/4]\subset[-1/4,5/4]\)；零质量块任取 \(\lambda_n=0\)，无需定义其条件律。把 (B13) 的源、目的势分别平移并乘 \(\delta_n^2\)，且于 0 都设为零。块内对偶不等式成立。源势满足 \(f_n\le9/4\)（用中点目的成本），目的势满足 \(|g_n|\le5/4\)，因此对不同块

\[
f(x)+g(z)\le\tfrac94\delta_n^2+\tfrac54\delta_m^2
\le16(\delta_n+\delta_m)^2\le|x-z|^2
\quad(x\in G_n,z\in G_m\cap S).
\]

与 0 的对也因 \(t_n\ge4096\delta_n\) 满足该不等式。各局部势另有统一下界（例如 \(f_n\ge-5/4\)），故缩放拼出的势有界可测并趋零于聚点。不变目的律每块的端点质量平衡，使 \(\int g\,d\pi=0\)；有界性保证逐块求和合法。对**任意**不变目的律和任意运输计划积分，得 (B20) 右侧为成本下界。

反向取各块的最优原计划，按 \(m_n\) 加权，0 处质量对角耦合；可数和定义概率计划，其列边缘不变，成本恰为右侧。因此 (B20) 成立，并构造了保持块质量的全域最近计划；没有断言每个最优计划都保持块。

核保持 \(m_n\)，条件质量按 \(Q\) 转移。将 (B17) 逐项代入 (B20)，得

\[
d(\mu P)^2\le\frac{15}{16(99/100)^2}d(\mu)^2
=\frac{3125}{3267}d(\mu)^2,
\]

即 (B8)，而 \(3125/3267<1\)。

<a id="crb-exact-zero"></a>
## 5. Exact-zero 与一般 gauge

块内位移标签 \(x-Tx\) 依次为

\[
-\delta_n,\quad0,\quad\delta_n,\quad\delta_n(1-e_n).
\tag{B21}
\]

每块三个非零标签互异，跨块也互异：正标签落在 \([(99/100)\delta_n,\delta_n]\)，相邻尺度缩小八倍；负标签只有 \(-\delta_n\)。零标签点恰为所有中点和 0。

由紧性引理，若 \(\Psi(\mu)=0\)，确有不变目标 \(\pi\) 和输入最优计划 \(\eta\) 取到它。非负积分为零与 \(p=1/8>0\) 迫使 \(\eta\)-几乎处处两个位移标签相等。每个非零标签的源点只能送往同一个点；第四点在 \(\pi\) 中质量为零，故 \(\mu\) 也不给它质量；第一、第三点的源质量分别等于 \(\pi\) 的相应质量，故平衡。剩余质量只在固定点，遂 \(\mu\in\mathcal I\)。反向由对角计划成立。

标签向零聚集不损害这个论证，因为已先证极小值取得；只有标签分离而没有取得，不能从 infimum 为零推出计划支持性质。现在 exact-zero 和紧性引理给全律空间的严格 gauge (B4)，无须用任何收敛结论。

<a id="crb-rate"></a>
## 6. 指定极限律、统一相对率与律空间长度

表中直接有 \(T^3=T\)，故 \(R^3=R\)、\(R\Pi=\Pi\)。于是 \(\Pi\mu\) 不变；每个不变 \(\pi\) 由 \(\pi P=\pi\) 得 \(R\pi=\pi\)，因此 \(\Pi\pi=\pi\)。两个计划以相同权重混合给平方运输成本的凸性，故

\[
W_2(\Pi\mu,\Pi\nu)^2
\le\tfrac12(L^2+L^4)W_2(\mu,\nu)^2
\le L^4W_2(\mu,\nu)^2.
\tag{B22}
\]

记 \(a_k=(7/8)^k,b_k=(3/4)^k\)。\(k\) 次独立 Bernoulli 主动更新的次数为零、奇数、正偶数的概率分别是
\(a_k,(1-b_k)/2,(1+b_k)/2-a_k\)；其皆非负并和为 1。因此

\[
\mu P^k=a_k\mu+\tfrac{1-b_k}{2}R\mu+
\left(\tfrac{1+b_k}{2}-a_k\right)R^2\mu.
\tag{B23}
\]

若 \(a_k\le1/2\)，因 \(b_k\le a_k\)，此式等于非负混合

\[
(1-2a_k)\Pi\mu+a_k\mu+(a_k-b_k/2)R\mu+(b_k/2)R^2\mu.
\tag{B24}
\]

后三项权重和为 \(2a_k\)。分别把它们耦合到同一个 \(\Pi\mu\)，并用 \(R\Pi\mu=R^2\Pi\mu=\Pi\mu\) 与 Lipschitz 界，得

\[
W_2(\mu P^k,\Pi\mu)^2\le2a_kL^4W_2(\mu,\Pi\mu)^2.
\]

若 \(a_k>1/2\)，直接用 (B23) 全部权重和 \(1\le2a_k\) 得同一界。取最近不变律 \(\pi\)，(B22) 给
\(W_2(\mu,\Pi\mu)\le W_2(\mu,\pi)+W_2(\Pi\pi,\Pi\mu)\le(1+L^2)d(\mu)\)，证明 (B9)。最后通过同一个 \(\Pi\mu\) 用三角不等式连接连续两时刻，再求几何级数，得 (B10)。

<a id="crb-no-power"></a>
## 7. 所有正幂 EB 失败的同一见证序列

在第 \(n\) 块放全部质量，固定 \(s=1/4\)，定义

\[
\nu_n=s\delta_{x_{n,0}}+(1-2s)\delta_{x_{n,m}}+s\delta_{x_{n,h}}.
\tag{B25}
\]

支撑包含于 \([t_n,t_n+2\delta_n]\)，所以 \(W_2(\nu_n,\delta_0)\le t_n+2\delta_n\to0\)。由 (B18)、(B20)，

\[
d(\nu_n)=(1-e_n)\delta_n\sqrt s>0.
\tag{B26}
\]

(B18) 的计划保留前两项，把第四点送到第三点；经 §4 已证是全域最近计划，因此也为其固定输入、目标两边缘的最优计划：若这对边缘另有成本更小的计划，就违背全域最近性。它故可合法代入原始 (B2)，而非代入放松残差。

唯一非零的同步位移差在第四点至第三点，大小为 \(\delta_ne_n\)。其质量为 \(s\)，主动映射概率为 \(p=1/8\)。故

\[
0<\Psi(\nu_n)\le\sqrt{ps}\,\delta_ne_n
=\sqrt{ps}\,\delta_n^{n+1}.
\tag{B27}
\]

严格正性用 §5 exact-zero 与 (B26)。这里仅需上界，不宣称计划也最小化残差。对固定 \(q>0\)，

\[
\frac{d(\nu_n)}{\Psi(\nu_n)^q}
\ge\frac{(1-e_n)\sqrt s}{(ps)^{q/2}}
\delta_n^{1-q(n+1)}\longrightarrow\infty.
\tag{B28}
\]

确切地，该幂的以 2 为底对数为 \((3n+10)(q(n+1)-1)\to+\infty\)。给定 \(q,K,r\)，取同一个足够大的 \(n\)，便同时满足球约束与严格违界，得 (B11)。甚至可再加任意正残差阈值，因为 (B27) 同时趋零。

<a id="crb-fixed-formula"></a>
### 固定 almost-firm 标量公式的限定后果

此小节单独固定 \(0<\alpha<1\)、\(\tau=(1-\alpha)/\alpha>0\) 和有限 \(\varepsilon_f\ge0\)，并假设

\[
\mathbb E|T_\xi x-T_\xi y|^2+\tau c_R(x,y)
\le(1+\varepsilon_f)|x-y|^2
\tag{B29}
\]

在 0 的一个完整相对状态邻域的**全部状态对**上成立。每个这样的邻域包含完整尾块。取其中第四点和第三点，得到

\[
\frac{\mathbb E|T_\xi x-T_\xi y|^2}{|x-y|^2}
=\tfrac78+\frac1{8(1-e_n)^2}>1.
\]

因此任何固定有效的 \(\varepsilon_f\) 必严格为正。若一个严格 gauge 既给 \(\delta_0\) 附近的 (B4)，又使

\[
\Theta_\rho(t)^2=(1+\varepsilon_f)t^2-\tau[\rho^{-1}(t)]^2,
\qquad0\le\Theta_\rho(t)<t
\tag{B30}
\]

对所有充分小 \(t>0\) 成立，则 \(\rho^{-1}(t)>\sqrt{\varepsilon_f/\tau}\,t\)。令 \(t=\rho(s)\) 得充分小 \(s\) 上 \(\rho(s)<\sqrt{\tau/\varepsilon_f}\,s\)。这把局部 gauge EB 变成线性 EB，与 (B25)–(B28) 矛盾。因此仅此**指定固定参数公式**无局部严格兼容 gauge；不排除别的速率证明，也不排除 §5 的一般 gauge。

<a id="crb-false-zero-object"></a>
## 8. C144-v1：随机投影在原始 OT 定义中有假零

- **Status**：`derived-checked`，范围限本节正方形及所列残差和锚点。
- **完整对象**：现在重新固定 \(G=[0,1]^2\)、\(\beta=(\delta_0+\delta_1)/2\)，每步以公平独立 \(j\in\{0,1\}\) 更新 \(T_j(x,y)=(x,j)\)。这是到两条闭凸水平线段的 Euclidean 投影。\(\mathcal I,d,\Psi\) 使用此新对象的 (B1)–(B2)，不是 C143 的函数。

对每个输入律，有

\[
\mu P=\mu_x\otimes\beta,\quad P^2=P,\quad
\mathcal I=\{\nu\otimes\beta:\nu\in\mathscr P([0,1])\},
\]
\[
\Psi(\mu)=W_2(\mu_y,\beta),\quad
Z_\Psi=\{\mu:\mu_y=\beta\},\quad
 d_{W_2}(\mu,Z_\Psi)=\Psi(\mu).
\tag{B31}
\]

**证明。** 更新保留第一坐标并用独立 bit 替换第二坐标，给前一行和所有不变律。对任意两状态，同步位移差为 \((0,y-y')\)，输出差为 \((x-x',0)\)；两者平方和恰为输入平方距离。这也给 \(\alpha=1/2,\varepsilon_f=0\) 的精确期望 firmness。

任意不变目标的第二边缘是 \(\beta\)，故每个合法计划的残差平方至少为 \(W_2(\mu_y,\beta)^2\)。反向固定任意 \(a\in[0,1]\)，目标取 \(\delta_a\otimes\beta\)；先最优耦合 \(\mu_y\) 与 \(\beta\)，再用源律 \(x\mid y\) 的条件分布提升。到第一坐标 \(a\) 的成本 \(\int|x-a|^2d\mu\) 与计划无关，因此提升后的计划对完整平方成本也是最优的，残差正好等于该第二边缘距离。标准 Borel 紧空间上条件分布存在，此处只将其用于给定联合律对一个坐标的分解，不作跨参数选取。

仅按上述最优边缘耦合改变源第二坐标而保留第一坐标，则产生一个第二边缘为 \(\beta\) 的律，证明到 \(Z_\Psi\) 的距离上界；任意这样的目的律的第二边缘下界给反向。于是 (B31) 全部成立。

<a id="crb-false-zero-witness"></a>
### 完整局部见证、最近锚点与实际极限锚点

对 \(0<t<1/2\)，定义

\[
\mu_t=\tfrac12\delta_{(1/2-t,0)}+\tfrac12\delta_{(1/2+t,1)},
\qquad\bar\pi=\delta_{1/2}\otimes\beta.
\tag{B32}
\]

其第二边缘为 \(\beta\)，但两坐标相关，所以 \(\Psi(\mu_t)=0\) 而 \(\mu_t\notin\mathcal I\)。事实上

\[
d(\mu_t)=W_2(\mu_t,\bar\pi)=t,\qquad\mu_t\to\bar\pi\in\mathcal I.
\tag{B33}
\]

为对**所有**不变目标证明这个精确距离，将第一坐标中心化。源写成 \((tS,(S+1)/2)\)，\(S\) 为公平符号；任意不变目标写成 \((X,(W+1)/2)\)，其中 \(|X|\le1/2\)、\(W\) 公平且与 \(X\) 独立。任意联合耦合中令 \(m=\Pr(S\ne W)\)，则
\(\mathbb E[WX]=0\)，且 \(|\mathbb E[SX]|=|\mathbb E[(S-W)X]|\le m\)。成本因此至少

\[
t^2+\mathbb EX^2-2t\mathbb E[SX]+m
\ge t^2+\mathbb EX^2+(1-2t)m\ge t^2.
\]

取 \(X=0,W=S\) 即到 \(\bar\pi\) 的计划达到该界，并且第二坐标相同，所以残差为零。这证明 (B33)，也说明把外层只限于最近不变锚点仍有假零。

实际极限 \(\mu_tP\) 的中心化表示为 \((tU,(W+1)/2)\)，其中 \(U,W\) 独立公平符号。任意耦合的成本为
\(4t^2\Pr(S\ne U)+\Pr(S\ne W)\)。在事件 \(U\ne W\)（概率 \(1/2\)）上，至少支付 \(\min\{4t^2,1\}=4t^2\)，故最小成本至少 \(2t^2\)。取 \(S=W\) 达到它、保持正确公平源边缘，同时同步位移差为零。因此连指定实际极限目标也有一个合法输入最优零残差计划。

任意非空有限映射复合仍为 \((x,y)\mapsto(x,j_{\rm last})\)；对任意固定共同复合词，位移差仍为 \((0,y-y')\)。若复合指标独立公平，其核和不变律也仍如 (B31)，所以同一假零见证保持。对以 (B33) 最优输入计划启动的两条同步路径，第一步第二坐标已经相等，后来一直相等；第一坐标每步都不移动。因此任意有限或非负无限和的逐步同步位移差平方在该耦合下均为零。这里明确指这类同噪声路径代价，不赋给其它未定义的路径残差。

每个律一步变成不变律仍不能推出此 \(\Psi\) 识别 \(\mathcal I\)。任何 \(\rho(0)=0\) 的局部不变集 gauge 都被 (B32)–(B33) 否定；与此同时，到残差自身零集 \(Z_\Psi\) 的全局线性界在 (B31) 以常数 1 成立。两种目标不可互换。

<a id="crb-relaxed-ot"></a>
## 9. C71 的另一个假零：改变输入计划域

此处复用 [C71 的同一四状态对象](lazy_cycle_ot.md#lc-object)，不另立 Claim，也不改 C144 的含义。取 \(G=(0,1,3,4)\)、循环 \(T:0\mapsto1\mapsto3\mapsto4\mapsto0\)，概率 \(0<p<1\) 选 \(T\)、\(1-p\) 选恒等；唯一不变律为均匀 \(\pi\)。同步成本为

\[
C_{ij}=|g_i-g_j|^2,\quad
R_{ij}=p(d_i-d_j)^2,\quad(d_i)=(-1,-2,-1,4),
\]
\[
\Psi(\mu)^2=\min_{\eta\in\operatorname{Opt}_C(\mu,\pi)}R\cdot\eta,
\qquad
\widetilde\Psi(\mu)^2=\min_{\eta\in\Gamma(\mu,\pi)}R\cdot\eta.
\tag{B34}
\]

\(\Gamma\) 表示所有计划，\(\operatorname{Opt}_C\) 表示同边缘的输入最优计划。取 \(\mu^+=(1/2,1/4,0,1/4)\)，各 \(1/4\) 质量放在 \((0,0),(0,3),(1,1),(4,4)\) 得 \(R\)-成本 0、\(C\)-成本 \(9/4\)，故 \(\widetilde\Psi(\mu^+)=0\)。

完整平方成本的最优计划却把各 \(1/4\) 放在 \((0,0),(0,1),(1,3),(4,4)\)，其成本 \(5/4\)、残差平方 \(p/2\)。确证其为唯一最优计划：当源点 \(x<x'\)、目的点 \(y<y'\) 时，交叉代价比有序代价多 \(2(x'-x)(y'-y)>0\)。最优计划不能交叉，按从左到右累积质量匹配又唯一确定上述计划。因此

\[
\Psi(\mu^+)^2=p/2>0,\qquad\widetilde\Psi(\mu^+)=0,\qquad\mu^+\ne\pi.
\tag{B35}
\]

原 \(\Psi\) 的 exact-zero 也可直接复核：零成本仅允许相同标签配对，唯一可能的非对角边为 \(0\to3,3\to0\)。目的点 1 的质量要求 \(1\to1\) 有 \(1/4\)；任意前述跨边都会与该正质量边交叉，违反严格交换改进，故只能对角且 \(\mu=\pi\)。这与 §8 有本质对象差别：§8 原始最优计划已经有假零，本节假零来自删除输入最优约束。更强的 C71 锐界不由本页重复验收，仍用其既有完整证明。

<a id="crb-obligations"></a>
## 10. 接收范围、证明义务与来源

| 义务 | 本页关闭位置与结论 |
| --- | --- |
| 紧集、自映射、全部概率、全部不变律 | (B5)–(B7)、(B12)、§4；没有未定义第四支 |
| C14 一般噪声域是否保留原 a.e. 量词 | [通用对接节](#crb-general-gauge) 的共同 \(\Xi_0\)、(CG1)–(CG7)、有界控制收敛与严格包络 |
| infimum 为零能否取到 | §1 联合可行集紧性；§5 才使用标签支持 |
| 单块证明是否偷换全域最近目标 | (B13)–(B20) 全 \(G\times S\) 势不等式与全域原计划 |
| 所有初值与所有时间的统一率 | §6 指定同一 \(\Pi\) 与统一 \(C,r_0\)；长度只属律 |
| 见证对是否真为输入 OT 最优 | §7 用全域最近性推出固定两边缘最优，残差只需上界 |
| 是否量化每个正幂和每个局部球 | (B28) 显式发散与同序列趋 \(\delta_0\) |
| 一般 gauge 是否存在 | §1 的明确严格包络与 §5 exact-zero；不从速率反推 |
| 投影假零是否针对所有不变目标 | (B33) 对任意独立 \((X,W)\) 的下界；最近与实际极限锚另证 |
| 松弛 OT 是否另一个对象 | (B34)–(B35) 同核两残差；复用 C71，不合并 C144 |

**尚未核与不作结论的范围。** 本页不核外部优先权；不把可数域的 \(T\) 称为凸近端映射；不把 law-space 有限长度称为样本路径长度；不声称 (B8)–(B10) 的全局常数锐；C14 的验收严格保留共同满概率噪声集上各完整自映射连续的量词，不涵盖另换的状态几乎处处连续条件；不认证未指明的其它 almost-firm 速率公式。C143 的状态不移给来源整篇、条件刷新、Gaussian 模型或其它历史结论。

**来源仅作溯源。** 文件
`history/sources/次单调论文研究/MARKOV_PAPER_THEOREM_PACKAGE.md`
的 SHA-256 为
`473c2c70c7c332fc61b7baea29bb29ca101f87be38b158a5d8e9c7d8f77c6835`。

| 来源范围 | 本页去向 |
| --- | --- |
| §1、Theorem 1，32–127 行 | §1 的 [C14 通用证明](#crb-general-gauge) 保留原共同 a.e. 连续量词，重构一般噪声域的核/成本连续、极小取得、下半连续及严格 gauge；Cesàro 非空性另列补充 |
| Theorem 2，131–191 行 | C144 / §8 正方形投影及其两个锚点、复合与路径代价限制 |
| Theorem F 后的 OT strictness 段，273–279 行 | §9 同一 C71 对象的有限成本重算；不新增 Claim |
| Lemma 3，285–351 行 | §3 四点块的标量势证明与有理证书 |
| Theorem 4，353–494 行 | C143 / §§2、4–7 紧可数完整模型及全部主量词 |
| Corollary 5，496–524 行 | §7 的 (B29)–(B30) 固定公式限定后果 |

本页证据为规范层逐式重构及对 (B16) 的有理运算复核；不依赖历史验证脚本的 PASS 标签，不主张新颖性。CM-NO-POWER / E41 应链接 C143 的完整对象、全域距离与 (B11)；CM-FALSE-ZERO / E40 应链接 C144，不能改指 (B35) 的松弛残差。
