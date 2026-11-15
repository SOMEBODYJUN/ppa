# Lipschitz 跨点误差的精确方差判据

设 \(X,Y\) 是实 Hilbert 空间，\(A\subset X\) 非空，\(C:A\to Y\)，\(\sigma\ge0\)。数据点 \(a\in A\) 有有限平方容差 \(e_a\ge0\)。问题是能否找到同一个全域 \(\sigma\)-Lipschitz 映射 \(N:X\to Y\)，使
\[
 \|C(a)-N(q)\|^2\le \sigma^2\|a-q\|^2+e_a\qquad(a\in A,\ q\in X). \tag{1}
\]
若 \(w\) 是有限支撑概率权重，记 \(\operatorname{Var}_w Z=\sum_a w_a\|Z(a)-\sum_b w_b Z(b)\|^2\)，并用 \(I(a)=a\)。源与目标无需可分。数据集可以不闭。

<a id="qca-criterion"></a>
## C290 · 异质平方容差的等价条件

(1) 的充要条件为
\[
 \operatorname{Var}_w C-\sigma^2\operatorname{Var}_w I\le \sum_a w_a e_a. \tag{2}
\]
无限维目标测试全部有限支撑的 \(w\)。若 \(\dim Y=n<\infty\)，只需测试支撑大小至多 \(n+1\)。特别地，公共平方容差的最优值是
\[
 B_\sigma(C)=\sup_w\{\operatorname{Var}_w C-\sigma^2\operatorname{Var}_w I\}\in[0,\infty], \tag{3}
\]
这里可在有限维目标使用相同的支撑限制。单点权重给下界零。若 (3) 有限，存在达到这个容差的全域映射。任意无限数据上不要求上确界由某个有限支撑权重取到。

**必要性。** 给定 \(w\)，在 (1) 取 \(q=\sum w_a a\)，加权求和。左边等于 \(\operatorname{Var}_w C+\|\sum_a w_a C(a)-N(q)\|^2\)，右边等于 \(\sigma^2\operatorname{Var}_w I+\sum_a w_a e_a\)。舍去左边的非负项即得 (2)，包括支撑超过 \(n+1\) 的权重。

**有限球判据。** 对 \(Y\) 中有限个中心 \(z_i\) 及平方半径 \(r_i^2\ge0\)，闭球共交当且仅当对每个概率向量 \(w\)，\(\operatorname{Var}_w z\le\sum_i w_i r_i^2\)。必要性同样由加权平方分解。反向取 \(y_*\) 为 \(\max_i(\|y-z_i\|^2-r_i^2)\) 的最小点。投影到中心的有限凸包不会增大任一平方距离，故存在最小点。该点属于活跃中心的凸包，否则沿活跃中心凸包方向移动可同时严格降低各个活跃平方距离，有限个不活跃约束已有严格余量。令 \(w\) 是把 \(y_*\) 表成活跃中心凸组合的权重。最优值即 \(\operatorname{Var}_w z-\sum_i w_i r_i^2\)，由假设非正。

**充分性。** 假设部分映射 \(N:S\to Y\) 已有 Lipschitz 界，且同全部 \(a\in A,q\in S\) 满足 (1)。初始 \(S=\varnothing\) 合法。将 \(q\notin S\) 加入定义域时，候选值是下列闭球的交点：
\[
 \overline B\big(C(a),\sqrt{\sigma^2\|a-q\|^2+e_a}\big)\quad(a\in A),\qquad
 \overline B\big(N(s),\sigma\|s-q\|\big)\quad(s\in S). \tag{4}
\]
对有限子族取概率权重 \(w\)，有限维情形只取至多 \(n+1\) 个球。把索引按球的来源分组，即使两个球来自同一源点也保留不同索引。记数据组总权重 \(t=\sum_{a\in A}w_a\)，以及 \(E=\sum_{a\in A} w_a e_a\)。记每个球的源位置为 \(u_i\)，中心为 \(z_i\)。按有序点对的半和公式计算 \(\operatorname{Var}_w z-\sigma^2\operatorname{Var}_w u\)。数据–数据项由 (2) 对归一化权重界为 \(tE\)，混合项由部分映射的 (1) 界为 \((1-t)E\)，已有值之间的项由 Lipschitz 性界为零。空组的贡献直接取零。于是
\[
 \operatorname{Var}_w z-\sum_i w_i r_i^2
 \le E-E-\sigma^2\Big\|\sum_i w_i u_i-q\Big\|^2\le0.
\]
有限球判据给相应子族相交。有限维由 Helly 定理从至多 \(n+1\) 个球推到任意有限子族，再用一个紧球的有限交性质。无限维对所有有限子族已有交点，各闭球弱闭，只需一个球弱紧。于是 (4) 给单点延拓。部分映射按延拓排序，每条链的并保持两个逐对条件，Zorn 引理所得极大映射须全域。令 \(e_a=B_\sigma(C)\) 完成 (3)。

**实际检验点与全域一致性。** 判据的违例是有限个数据点及其权重，查询点可选这些点的重心。若每个查询点的原始数据球有交点，必要性的同一推导给 (2)，充分性再把逐点可行提升为同一个 Lipschitz 选择。已指定的锚可作为额外观测加入并赋零容差，但新数据也必须经过 (2)。

<a id="qca-shadow"></a>
## C291 · 固定维数正反近似的最优因子

令 \(n\ge1\)，\(H=\mathbb R^n\)。假设非空全图满足 [C03](global_shadow.md#gsh-object) 的全对全尺度 Hölder–RL 条件，参数 \(\lambda,L>0\)、\(0<\gamma<1\)，记 \(R=L^{1/(1-\gamma)}\)。Cayley 数据为 \(C(x+\lambda v)=x-\lambda v\)。令 \(j_n^2=n/[2(n+1)]\)。则存在同一个强单调双 Lipschitz 同胚 \(A:H\to H\)，对每个 \((x,v)\in\operatorname{gph}F\) 满足
\[
 \lambda\|v-A(x)\|\le j_n R,\qquad \|x-A^{-1}(v)\|\le j_n R. \tag{5}
\]
固定 \(n\) 的类中 \(j_n\) 最小。

**上界。** 若同一数据各对的二次超额均至多 \(M\ge0\)，则任意支撑至多 \(n+1\) 的 \(w\) 有方差差至多 \(\frac M2(1-\sum w_a^2)\le j_n^2 M\)。C290 给 (1)，取 \(e_a=j_n^2 M\)。对本题取 \(\sigma=\sqrt\gamma\) 和 \(M=(1-\gamma)R^2\)。该 \(M\) 是 \(L^2t^{2\gamma}-\gamma t^2\) 在 \(t=R\) 的最大值，由凹函数 \(s^\gamma\) 在 \(s=R^2\) 的切线式即得。将 \(N\) 通过 [C03 的两次反演](global_shadow.md#gsh-shadow) 转回 \(A\)。比较点取相同原 \(x\) 或相同原 \(v\)，则反射与 Minty 差的范数相等，分别为 \(\lambda\|v-A(x)\|\) 和 \(\|x-A^{-1}(v)\|\)。代入 (1) 并除以 \(1-\gamma\) 得 (5)。同一反演给强单调常数至少 \((1-\sqrt\gamma)/(\lambda(1+\sqrt\gamma))\)。

**下界。** 取 \(F\) 的图为 \(n+1\) 个点 \((x_i,0)\)，其中 \(x_i\) 是边长 \(R\) 且均值为零的正则 \(n\) 单纯形顶点。不同顶点的两侧距离在 RL 式取等。任意候选 \(A^{-1}(0)=z\) 到这些顶点的平方距离均值为 \(j_n^2R^2+\|z\|^2\)。因而任意同底点正反近似即使不限于强单调也不能用更小因子。用 [同常数 Hölder 延拓](holder_extension.md) 时保留这些原图点，所以下界也适用于具有满 Minty 输入的同参数极大关系。

<a id="qca-complexity"></a>
## C292 · 有限数据的精确复杂性与近似

输入为同一有限维欧氏空间中互异的有理点 \(a_i\) 及有理像 \(c_i=C(a_i)\)，维数随输入变化。即使固定 \(\sigma=1/2\) 且 \(C\) 在数据上满足 \(\|c_i-c_j\|\le\|a_i-a_j\|^{1/2}\)，判定 (1) 是否有公共有理容差 \(b\ge0\) 的解也是 coNP-完全。精确求 (3) 为 NP-hard。通过 Cayley 变换这类输入都是 \((\lambda,L,\gamma)=(1,1,1/2)\) 的有限 RL 图，适用前提可用有理算术验证。

**构造。** 给定 \(m\ge2\) 个顶点的无向简单图 \(G\)，令 \(r=1/m\)。为每个顶点分配互不重叠的 \(m-1\) 个源坐标，令 \(a_i\) 在其中取 \(2r\)，余处取零。目标空间的坐标约定为每一条非边对应一个共享坐标，顶点 \(i\) 在与它关联的各个共享坐标取 \(r\)。再为 \(i\) 配私有坐标，每个也取 \(r\)，使它共恰有 \(m\) 个非零坐标。源与目标嵌入同一个空间的两个正交块。总维数 \(O(m^2)\)，构造为多项式规模。不同 \(i,j\) 有
\[
 \|a_i-a_j\|^2=8(m-1)r^2,\qquad
 \|c_i-c_j\|^2=2r^2(m-\mathbf1_{\{i,j\}\notin E(G)}).
\]
上式给 \(\|c_i-c_j\|^4\le 4/m^2\le8(m-1)/m^2=\|a_i-a_j\|^2\)，故满足指定 Hölder 条件。二次超额恰为 \(2r^2\mathbf1_{\{i,j\}\in E(G)}\)。因此 (3) 和 Motzkin–Straus 定理 1 给
\[
 B_{1/2}(C)=2r^2\max_{w\in\Delta_m}\sum_{\{i,j\}\in E(G)}w_iw_j
 =r^2(1-1/\omega(G)). \tag{6}
\]
对 \(2\le k\le m\)，给容差 \(b=r^2(1-1/(k-1))\)。不可行当且仅当 \(\omega(G)\ge k\)，即 CLIQUE 的肯定实例。

**不可行证书。** 设 \(M_{ij}=\|c_i-c_j\|^2-\sigma^2\|a_i-a_j\|^2\)，则 (3) 是 \(w^TQw\) 在 \(\Delta_m\) 上的最大值，\(Q=M/2\) 为有理对称矩阵。若最大值大于 \(b\)，取一个最大点，支撑记为 \(S\)。它在该面相对内部，故 \(Q_{SS}w_S=\mu\mathbf 1\)，并且 \(\mu=w_S^T Q_{SS}w_S>b\)。所有满足该线性等式和 \(\sum w_i=1\) 的解具有相同 \(\mu\)，因为用两解交叉乘积和对称性可把各自的 \(\mu\) 写成同一个数。加入 \(w_i\ge0\) 得非空有界有理多面体，取顶点。Cramer 公式及行列式位长界给多项式位长的有理 \(w\)，代回即可核查。于是不可行问题在 NP 中，加上上述归约得结论。

**公共预算的近似。** 枚举从 \(m\) 个数据点有放回取 \(s\ge1\) 个点的全部多重集，用其经验权重求最大值 \(B_s\)。从任一最优 \(w\) 独立取样时，样本两两平方超额的期望是 \((1-1/s)B_\sigma(C)\)，因为 \(M_{ii}=0\)，\(s(s-1)\) 个不同抽样位置给原独立权重的期望。故
\[
 (1-1/s)B_\sigma(C)\le B_s\le B_\sigma(C).
\]
取固定精度即有多项式时间近似方案，\(s>1\) 时 \(B_s/(1-1/s)\) 是可行预算的上界。若存在公共预算的完全多项式时间相对近似方案，则取 \(\varepsilon=1/(4m^2)\)，用 (6) 的相邻隔距至少 \(r^2/[m(m-1)]\) 恢复最大团数，从而有 \(\mathrm P=\mathrm{NP}\)。这里的复杂性针对全查询跨点约束和最优公共平方预算。同站点近似、真实最优正反纤维误差、以及 C19 的给定带余量可行构造分别是其他问题。

<a id="qca-prior"></a>
## 对照与复算

- 普通同常数延拓是 C290 在 \(e_a=0\) 的特例。证明中的加权球交和 Helly 步使用经典 Kirszbraun 方法。所用的任意 Hilbert 同常数定理与可用边界见 [C03 的一手接口](global_shadow.md#gsh-import)。[Aschenbrenner–Fischer，Proc. LMS 102 (2011), 468–502](https://doi.org/10.1112/plms/pdq029)。
- Levy–Rice 1983，Theorem 3 与 Corollary 2，给 Hilbert 间的定性一致 Lipschitz 逼近及延拓条件。C290 固定斜率、逐数据平方容差，并要求全部比较点满足同一跨点不等式。[原文](https://dml.cz/bitstream/handle/10338.dmlcz/106224/CommentatMathUnivCarol_024-1983-2_6.pdf)。
- Ciosmak 2026，Theorem 1.1，刻画哪些参考映射允许每个适当初始 Lipschitz 映射作保持统一距离的延拓。它的等价命题有任意初始映射的量词及参考映射的重心收缩条件。C290 的存在量词、逐点平方容差和方差差对应不同合同。其证明与 Ciosmak 2024 Theorem 1.2 的一般球交框架有实质方法重合。外部精确先行性继续开放。[2026 原文](https://arxiv.org/abs/2607.17672)，[2024 原文](https://arxiv.org/abs/2402.14699)。
- (6) 导入 Motzkin–Straus Theorem 1，系数以无序边计数。CLIQUE 的多项式归约见 Karp 1972，Main Theorem 中 SATISFIABILITY 到 CLIQUE 的归约。[Motzkin–Straus 原文](https://doi.org/10.4153/CJM-1965-053-6)，[Karp 原文](https://www2.seas.gwu.edu/~simhaweb/champalg/tsp/papers/KarpOriginal.pdf)。
- 单纯形网格 PTAS 与多项分布方法已有一般版本，参见 [de Klerk–Laurent–Sun，Math. Program. 151 (2015), 433–457](https://doi.org/10.1007/s10107-014-0825-6)。这里给本问题的零对角相对界及从几何数据到该规划的可逆识别。
- [精确复算](../code/quadratic_cross/verify.py)逐图核反算及小维权重。独立审查先重构 C291 所用球交，再在未读主证明时重构 C290，另用不同有理坐标构造和图枚举复核 (6)。外部优先性和四大期刊主贡献门均未通过，具体审查及下一步见[研究检查点](../audit/ORIGINAL_DISCOVERY_CHECKPOINT.md)。
