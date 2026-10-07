# ℓ¹ 停止平滑、Hölder 扩张与概率值域

本页固定 C181/C182 的对象及证明。外部起点为 [LIT-OAI-CATALOG-2026](../LITERATURE.md#lit-oai-catalog-2026) 第332项；这里独立重构其实数主定理的承重链，再接明确的一手扩张定理。常数损失、概率值域与原生残差是不同接口。证据为逐式重构及下方边界检查；未作独立代理接收、Lean覆盖或全球先行性认证。

<a id="lm-object"></a>
## LM-OBJECT · C181 的全部量词

固定整数 n,t≥1，随机矩阵 A=(a_ij)，概率行向量 π 满足 πA=π（允许 π_i=0，不要求可逆），及任意 x_1,…,x_n∈ℓ¹(ℝ)。存在 y_1,…,y_n∈ℓ¹，使
\[
 \sum_i\pi_i\|x_i-y_i\|_1^2+t\sum_{i,j}\pi_i a_{ij}\|y_i-y_j\|_1^2
 \le3024\sum_{i,j}\pi_i\left(\frac1t\sum_{s=1}^t A^s\right)_{ij}\|x_i-x_j\|_1^2.\tag{LM1}
\]
平稳而非可逆的范围也在外部原稿 Remark5.1 明示，不记为本库新颖性。它是允许自由选择 y_i 的平滑不等式；不是原数据的收缩、指定近端更新或到不变律的误差界。

<a id="lm-proof"></a>
## LM-PROOF · 二元编码、四次势与停止鞅

**有限二元编码。** 对每个原坐标 k，置 v(k)=min_i x_i(k)，对非空真子集 B⊂{1,…,n} 置 b_B(k)=(min_(i∈B)x_i(k)−max_(i∉B)x_i(k))_+。这些向量属于ℓ¹，因为 |v(k)|≤Σ_i|x_i(k)|，b_B(k)≤2Σ_i|x_i(k)|。只保留 w_B=||b_B||_1>0 的有限族，令 z_i(B)=1_(i∈B)，Q=[0,1]^B，T(u)=v+Σ_B u_B b_B。

按每个坐标的有序相邻差拆分，只有嵌套的上水平集有正 b_B(k)，所以 T(z_i)=x_i 且
\[
 \|x_i-x_j\|_1=\sum_Bw_B|z_i(B)-z_j(B)|=\|z_i-z_j\|_H^2,
 \quad\|T(u)-T(u')\|_1\le\|u-u'\|_{1,w}.\tag{LM2}
\]
这里 ||u||_H²=Σ_Bw_Bu_B²，||u||_(1,w)=Σ_Bw_B|u_B|。若族为空则所有 x_i 相等，取 y_i=x_i 即可。

**平坦三次函数。** 令 φ(r)=3r²−2r³、Φ(u)_B=φ(u_B)。对任意二元中心 e、a=u−e、δ=u'−u，有 |φ'(r)|≤6|r−e_B|，从而
\[
 \|\Phi(u')-\Phi(u)\|_{1,w}\le6\|a\|_H\|\delta\|_H+3\|\delta\|_H^2.
\]
置 F_e(u)=||u−e||_H⁴，其一阶余量恰为
\[
 R=F_e(u')-F_e(u)-4\|a\|_H^2\langle a,\delta\rangle_H
 =2\|a\|_H^2\|\delta\|_H^2+(2\langle a,\delta\rangle_H+\|\delta\|_H^2)^2.\tag{LM3}
\]
因此 ||a||²||δ||²≤R/2，||δ||⁴≤4R，平方上一界给 ||Φ(u')−Φ(u)||_(1,w)²≤108R。对Q值鞅 M_m 和初始可测二元 e，线性项条件期望为零；Q有界，势可有界收敛，非负增量可单调收敛，故
\[
 \mathbb E\sum_{m\ge0}\|\Phi(M_{m+1})-\Phi(M_m)\|_{1,w}^2
 \le108\mathbb E\|M_\infty-e\|_H^4.\tag{LM4}
\]

**停止表示。** 令 p=1/(t+1)、q=t/(t+1)，G=pΣ_(s≥0)q^sA^s，h_i=(Gz)_i∈Q，y_i=T(Φ(h_i))。从平稳A链出发，每个活状态 i 以概率 p 死亡并取值 z_i，以概率 qa_ij 转至活状态 j 并取值 h_j；死亡后固定。等式 h_i=pz_i+qΣ_j a_ijh_j 使所附值 M_m 是鞅。它几乎处处有限时死亡，终值为 z_(X_S)，其中 S 是独立几何变量，P(S=s)=pq^s。中心 e=z_(X_0) 初始可测。

设 B₀=Σ_iπ_i||z_i−Φ(h_i)||_(1,w)²、E_A=Σ_ijπ_i a_ij||Φ(h_i)−Φ(h_j)||_(1,w)²。时刻m的死亡和活跃跳跃贡献分别为 pq^mB₀、q^(m+1)E_A，故总期望恰为 B₀+tE_A。由(LM2)–(LM4)，(LM1)左边≤108 E||x_(X_S)−x_(X_0)||_1²。

**几何时间到有限平均。** 对任意平稳链及任意度量数据，记 D(s)=E d(x_(X_s),x_(X_0))²、W=t⁻¹Σ_(s=1)^tD(s)。Minkowski与平稳性给 √D(r+s)≤√D(r)+√D(s)，故 D(t)≤4W，D(jt+r)≤2j²D(t)+2D(r)。J=floor(S/t) 满足 EJ²≤ES²/t²=2+1/t≤3；R₀=S−tJ 的每个取值概率≤2/t，因为 q^t≤1/2。因此 ED(R₀)≤2W，ED(S)≤28W。(LM1)随即由108·28=3024成立。整个证明只用πA=π；零π坐标、t=1、退化相同数据均已包含。

<a id="lm-extension"></a>
## LM-EXTENSION · C182 的两个源空间范围

<a id="lm-mn-definitions"></a>
**导入定理的常数约定。** 源空间 \((X,d)\) 的 Markov type 2 常数 \(M_2\) 指：对全部有限平稳可逆链 \((Z_s)\)、全部状态数据 \(x_i\in X\) 和整数 \(t\ge1\)，有
\(\mathbb E d(x_{Z_t},x_{Z_0})^2\le M_2^2 t\,\mathbb E d(x_{Z_1},x_{Z_0})^2\)。目标的 metric Markov cotype 2 常数 \(N_2\) 使用 (LM1) 的同一 Cesàro 归一化，将 3024 换成 \(N_2^2\)，量化全部有限平稳可逆链和目标数据，并允许逐组选择平滑点；C181 更强的非可逆范围并非扩张导入所需。\(W_2\)-barycenter 常数 \(\Gamma\) 指有限支撑概率律上的映射 \(\beta\)，满足 \(\beta(\delta_y)=y\) 和 \(d(\beta\mu,\beta\nu)\le\Gamma W_2(\mu,\nu)\)。此处目标为实 \(\ell^1\)，\(\beta\) 为均值且 \(\Gamma=1\)。该 \(W_2\) 是以目标 \(\ell^1\) 距离定义的运输距离，不是 PPA 旁支的条件距离或同步残差。

导入 [LIT-MN-EXTENSION](../LITERATURE.md#lit-mn-extension) 的 Theorem1.11 / Corollary1.13：源有 Markov type2，目标有 metric Markov cotype2、W₂ barycenter，且为对偶Banach时，任意子集的 Lipschitz 映射可全域扩张，常数≤c M₂ N₂，其中c是统一绝对常数。ℓ¹=c₀*，均值重心由 Jensen/任意耦合给 W₂ 常数1；C181给N₂≤12√21。固定一个共同 K≥1，使 K≥c·12√21。

1. **Hilbert 源、0<γ≤1。** γ=1 时 Hilbert 的M₂=1：有限可逆链上对向量坐标用自伴随A的谱及1−r^t≤t(1−r)，r∈[−1,1]，再加总即可。0<γ<1 时先用 [HE-SNOWFLAKE](holder_extension.md#he-snowflake) 把(H,||·||^γ)等距嵌入Hilbert，扩张后拉回。故任意 D⊂H、f:D→ℓ¹、||f(x)−f(y)||_1≤L||x−y||^γ，存在全H上的同数据扩张，系数≤KL。
2. **任意度量源、0<γ≤1/2。** (X,d^γ) 有M₂≤1：对每条t步路径，用2γ≤1得到 d(X₀,X_t)^(2γ)≤Σ_(s=1)^t d(X_(s−1),X_s)^(2γ)，再取平稳期望。直接调用同一定理，不需Hilbert嵌入，得到任意D⊂X上ℓ¹值γ-Hölder映射的全X扩张，仍为KL。

空D任取常值；L=0及非空D取原常值。K可对两个范围的全部源、域、γ及维数统一；此处未给最小K或K=1。第二范围没有证明任意度量源在γ>1/2的同结论。

<a id="lm-simplex"></a>
## LM-SIMPLEX · 概率值域可以显式保持

令 Δ={a∈ℓ¹:a_k≥0,Σ_k a_k=1}，固定e₁。对x∈ℓ¹，a=x_+、s=||a||_1，定义
\[
 \mathcal P(x)=\begin{cases}a+(1-s)e_1,&s\le1,\\a/s,&s\ge1.\end{cases}\tag{LM5}
\]
这是Δ上的恒等回缩。正部1-Lipschitz。若a,b的和都≤1，差≤||a−b||_1+|s−r|；若s≥r≥1，差≤(||a−b||_1+s−r)/s；若s≥1≥r，经a插入给差≤(s−1)+||a−b||_1+(1−r)。三种均≤2||a−b||_1，故P为2-Lipschitz。

因此上述两个源范围的Δ值数据可扩张为全域**概率值**数据，系数≤2KL。有限单纯形用同一公式且同一常数；以TV=||·||_1/2计目标距离，常数损失仍为2K。C181对Δ值数据再复合P，亦给Δ中的平滑点与12096常数。这里保持的只是非负性和总质量，不保持预定守恒边缘、平稳律集合、W₂常数或任何原生核。

<a id="lm-cayley"></a>
## LM-CAYLEY · 扩张接入ℓ¹完整关系的确切结论

对完整非空关系F:ℓ¹⇉ℓ¹，λ,L>0、0<γ≤1/2，假设全图全尺度满足 ||Δu−λΔv||_1≤L||Δu+λΔv||_1^γ。同输入唯一性的代数不需Hilbert，故D={u+λv}上C(u+λv)=u−λv良定。LM-EXTENSION第二项给Ĉ:ℓ¹→ℓ¹，系数KL；令
\[
 \operatorname{gph}\widehat F=\left\{\left(\frac{p+\widehat C(p)}2,\frac{p-\widehat C(p)}{2\lambda}\right):p\in\ell^1\right\}.\tag{LM6}
\]
则F⊂F̂，完整J_(λF̂)(p)={(p+Ĉ(p))/2}在全部ℓ¹非空单值，且F̂在**放宽后的**(λ,γ,KL)下图极大：相同Minty输入强制相同反射输出。若D真小则扩图严格。不能倒推F在原(λ,γ,L)下图极大必满域；预算放大是此接口的一部分。γ>1/2的ℓ¹源完成没有由第一项认证。

<a id="lm-boundaries"></a>
## LM-BOUNDARIES · 适用边界与本轮认识

C181实数主定理的四个承重步骤已逐式重构，C182的扩张导入全部对象条件已核。原稿复数推论、其Lean文件、全部相关722稿件及全球新颖性未验收。没有把平滑点当作指定近端输出，没有把一般ℓ¹闭子空间当作继承相同扩张性质的目标；P只保证Δ值域。

对本项目，现已补出任意度量源的半阶概率参数化扩张及允许常数损失的ℓ¹ Cayley完成；原Hilbert同常数工具本来更强，未被替代。新完成可改变零集、完整逆纤维和真残差。要接入RLEB，还须对**同一个完成后关系**另证真EB、零集、兼容与留域；尤其无Hilbert内积时不能照搬R01能量恒等式。C181也不生成自然算子母空间、保纲桥或总体类规模比较。
