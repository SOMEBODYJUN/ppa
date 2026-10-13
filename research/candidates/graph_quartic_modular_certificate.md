# 仿射三次系统的全根模 3 证书：图势与有向网络的共同附页

受检范围：`n=13` cycle graph、`J=1/4`、每个 `b_i` 为整数除以 `1000`，以及下述明确的一般充分引理。本页是候选附页，只登记应用诊断，不登记新 Claim、不改 canonical 或主稿。已读 `AGENTS.md`、`RESEARCH_PROTOCOL.md`、本地 academic-writing-skills 的 proof-review 模式与 `mathematics.md`、C231 和 C254 的对象及证明接口。

**裁决。** 候选证明成立，未找到 fatal objection。只须检查一个 `n×n` 模 3 行列式，即可证明该参数的**所有复零点**均非退化，并且恰有 `3^n` 个不同复零点。有限自由商环是防止“未知复根没有合法模 3 reduction”反驳的承重步骤；证明完全不把个别未知根约化模 3。目标 `n=13` 时行列式 residue 为 `2`，复零点数为 `1594323`。这不是实零点数，也不是隐藏零点枚举。

## 1. 精确的一般充分引理

令
\[
R=\mathbb Z_{(3)}=\{a/s:a,s\in\mathbb Z,\ 3\nmid s\},
\quad A\in R^{n\times n},\quad b\in R^n,
\]
\[
f_i(u)=u_i^3+\sum_{j=1}^n A_{ij}u_j-b_i,
\qquad B=R[u_1,\ldots,u_n]/(f_1,\ldots,f_n).
\]
若 `det(Ā)≠0` 于 `F_3`，则：

1. `B` 是秩 `N=3^n` 的有限自由 `R`-module，其基为 `u^α`，`0≤α_i<3`；此项其实无需行列式前提。
2. `δ=det DF` 在 `B` 中已经是单位。
3. `F=(f_i)` 在 `C^n` 上恰有 `3^n` 个不同零点，且每个零点的 Jacobian 都可逆。

该引理的系数 `A` 无需对称，`b` 无需小。对图势，取 `A=JL−I`，只是这个引理的准确特例。

## 2. 有限自由商环：首项及 product criterion 的实际检查

取任一 graded monomial order；`f_i` 的首项是系数 `1` 的 `m_i=u_i^3`，尾项
`g_i=Σ_j A_ij u_j−b_i` 的总次数至多 `1`。替换 `u_i^3=−g_i` 严格降低总次数，所以除法终止，得到指数都小于 `3` 的余式。这先给出 spanning。

不同首单项式两两互素。它们的唯一必要重叠在 `m_i m_j`，相应消去多项式为
\[
m_j f_i-m_i f_j=m_j g_i-m_i g_j
 =g_i f_j-g_j f_i. \tag{1}
\]
式 (1) 右边的表示最高总次数至多 `4`，严格小于重叠首项的次数 `6`；等价地，将 `m_j` 和 `m_i` 分别替换为 `−g_j` 和 `−g_i`，两项恰好抵消。所有更高重叠都是这个身份乘一个单项式。

为说明这在环 `R` 上也给出 independence，不偷偷使用 field division：若理想中有非零标准余式，把它写成 `Σ_i q_i f_i`，选使表示中最大首单项式最小的表示。若该最大项未相消，余式首项必被某个 `m_i` 整除，矛盾；若相消，用 (1) 成对替换相消项，严格降低该表示中的最大项，仍矛盾。此替换只乘加系数，首系数均为 `1`，没有除以任何非单位。故非零标准余式不在该理想中，标准单项式独立。

因此 `B` 为有限自由，rank 恰为 `N=3^n`。改变系数基环到 `F_3`、`Q` 或 `C` 都保持同一标准单项式基；特别是不存在无穷纤维或被遗漏的正维零分支。这里的 finite/free 不是由数值搜索或泛型参数得出。

## 3. Jacobian determinant 单位：无需约化任何复根

在 `R[u]` 中
\[
DF=A+3\operatorname{diag}(u_1^2,\ldots,u_n^2),
\quad \delta=\det DF.
\]
将商环约化模 `3` 得
\[
\overline B=B/3B
 =\mathbb F_3[u]/(\overline f_1,\ldots,\overline f_n),
\quad \overline\delta=c:=\det\overline A\ne0.
\]
考虑有限自由 `R`-module `B` 上的乘法 `m_δ:x↦δx`。**仅在证明中存在**的 `N×N` 矩阵 `M_δ` 在模 `3` 下为 `cI_N`，故
\[
\det M_\delta\bmod3=c^N\ne0.
\]
`R` 是局部环，元素 residue 非零等价于该元素为单位，所以 `det M_δ` 为 `R` 的单位。伴随矩阵公式给 `m_δ` 的逆；将其作用于 `1`，得到 `e∈B` 且 `δe=1`。因此 `δ` 已是 `B` 的单位，当然也是 `B⊗_R C` 的单位。

对任意复零点 `z`，evaluation 是 `B⊗C→C` 的同态。把 `δe=1` 代入，得到 `det DF(z)·e(z)=1`，从而 `det DF(z)≠0`。

这关闭了所谓“未知代数复根可能在 3 上有极点”攻击：证明走的是有限商环上的单位身份，再 evaluation；完全没有假定根坐标属于 `R` 或能够逐点模 `3` 约化。代码不用生成 `M_δ`，也不用求任何隐藏复根。`N×N` 矩阵的存在只用于简短抽象证明。

## 4. 为什么数量是恰好 `3^n` 个不同复零点

`B_C=B⊗_R C` 的复向量空间维数为 `N=3^n`。有限维交换复代数分解为其各零点对应的有限维 local Artin algebras（可由 commuting coordinate multiplication 的 joint generalized eigenspaces 与 Chinese remainder decomposition 得出）。

在零点 `z` 的 local factor 中，maximal ideal `m` 由 `u_i−z_i` 生成且 nilpotent。Taylor expansion 的线性项给
\[
DF(z)\,(u-z)=0\quad \bmod m^2.
\]
由于 `DF(z)` 可逆，`m/m^2=0`，即 `m=m^2`。nilpotence 再给 `m=m^k=0` 对充分大 `k`，所以这个 local factor 就是 `C`，维数恰为 `1`。因此所有零点 multiplicity 都为 `1`，不同零点数等于总维数 `N`。

实系数还给非实根 conjugate pairs，所以实零点数是奇数（`3^n` 为奇数）；这仍不把 `3^n` 解释成实零点数。

## 5. 目标 cycle 的精确行列式

令 `S` 为 cycle shift，`n≥3`，`L=2I−S−S^{-1}`。目标线性项为
\[
A=\tfrac14L-I=-\tfrac14(I+S)(I+S^{-1}).
\]
若 `n` 为奇数，`det(I+S)=det(I+S^{-1})=2`，所以
\[
\det A=(-\tfrac14)^n\cdot4=-4^{1-n}.
\]
`n=13` 时
\[
\det A=-4^{-12}=-\frac1{16777216},
\qquad \det\overline A=2\in\mathbb F_3.
\]
`1/4` 和 `1/1000` 都属于 `R`，并且二者模 `3` 都为 `1`。因此 `Ā=L−I`，全部 `b_i=m_i/1000`（任意整数 `m_i`）都合法。故候选证书实际上对**每个奇数 cycle 长度和任意这种有理 tilt**统一成立；`b` 的具体 numerator 不进入行列式检查。

## 6. 实零点下界：还需独立的全局 degree 桥

模证书只给所有复/实零点正则和复数量；实零点下界还需要确定全局 real degree。对 `J≥0` 和 graph Laplacian `L≥0`，直接计算
\[
\langle u,F(u)\rangle
=\sum_i u_i^4-\|u\|^2+J\langle u,Lu\rangle-\langle b,u\rangle
\ge \frac{\|u\|^4}{n}-\|u\|^2-\|b\|\|u\|.
\]
在充分大半径 `R` 的球面，这严格为正；同一界还排除所有更远的零点。沿 `(1−t)F+t Id` 的同伦球面仍无零点，所以
`deg(F,B_R,0)=deg(Id,B_R,0)=1`。全体实零点有限且正则，因此
\[
\sum_{z\in F^{-1}(0)\cap\mathbb R^n}\operatorname{sign}\det DF(z)=1. \tag{2}
\]

若独立认证了 `k≥1` 个不同严格局部极小零点，gradient 的 Hessian 在极小处半正定，结合全局非退化即正定；这些零点各给 `+1`。令 `N_extra` 为其余实零点数，则
\[
\sum_{\rm extra}\operatorname{sign}\det DF=1-k,
\quad N_{\rm extra}\ge k-1,
\quad N_{\rm extra}\equiv1-k\pmod2.
\]
所以至少 `2k−1` 个实零点。更精确地，若额外正指数点数为 `p`，负指数点数为 `q`，则 `q−p=k−1`，`N_extra=k−1+2p`。这里只推存在、数量与净指数，**不确定各额外点的位置，也不把负指数逐点认成 index-one saddle**（Hessian 有奇数个负特征值即可）。

这条 degree 证明独立于 C231/C254：后两者的完整近端、整管与全尺度次线性反射前件不由模证书供应。图四次势的近端远处为 cubic-root 量级，反射 `2T−Id` 保留线性主项，故不可把本次 degree 桥悄悄标为直接调用原 C254。

## 7. 攻击与边界

| 攻击或边界 | 精确结果 |
|---|---|
| Monic product criterion 只在 field 上适用？ | 本次首系数全为 `1`；式 (1) 给环上不除非单位的证明，有限自由结论成立。 |
| 根在 `3` 上有 pole，是否逃出证明？ | 不对根做 reduction；`δ` 的商环单位身份对任意复 evaluation 成立。 |
| `b_i` 不同、很大或 numerator 被 `3` 整除？ | 只要求 denominator prime to `3`；不影响 `δ̄=c`。 |
| 复总数可否直接当实总数？ | 不可；只可得实总数奇数，并用独立 degree 与已知局部指数给下界。 |
| 模行列式为零是否证明实际退化？ | 否，充分证书失效不等于退化；例如一般引理中的 `f(u)=u^3+3u`，`Ā=0`，但 `0,±i√3` 都正则。 |
| 目标退化参数 `n=12,J=1,b=0` | `u=0` 是零点，`DF(0)=L−I` 有显式 kernel `[2,1,−1,−2,−1,1]` 重复两次，所以确实退化。 |
| Coupling denominator 被 `3` 整除 | 一般不可约化；`n=6,J=1/3,b=0` 有 `L` eigenvalue `3`，所以 `u=0` 确实退化。 |
| Tilt denominator 被 `3` 整除 | 不仅原证明不能调用，一般引理删掉这个条件后会为假：见下面反例。 |

最后一项的明确有理反例（一般 affine-cubic 引理，不宣称它是目标 cycle）为
\[
A=\begin{pmatrix}0&1\\1&3\end{pmatrix},\quad
b=(1/27,1/3),\quad u=(1/3,0).
\]
`detĀ=2≠0`，`F(u)=0`，但
\[
DF(u)=\begin{pmatrix}1/3&1\\1&3\end{pmatrix},\qquad\det DF(u)=0.
\]
所以 `A` 的模证书不能单独抵消非法 tilt denominator。

## 8. 可复算检查及证据范围

运行：`python3 tmp/modular_zero_regularity.py`。仅用 Python 标准库的 `Fraction`、exact Gaussian elimination 和 modular Gaussian elimination；无浮点 tolerance、无 seed、无第三方依赖。结果写到 `tmp/modular_zero_regularity.json`。

目标 `13×13` 检查精确得 `detA=−1/16777216`、`detĀ=2`。另核了上述两个 cycle 退化参数和一般 denominator 反例。仅作为小维 sanity check，代码在 `n=2` 商环的 `9` 个标准单项式上比较了 `81` 个 monomial 的正反两种 reduction，并检查 `δ` 的 `9×9` 乘法矩阵 mod `3` 恰为 `cI`；生产参数从不构造指数大小矩阵。玩具 `(x^3−x,y^3−y)` 的 `9` 个显式实根全正则，总指数 `1`，`4` 个严格极小点外有 `5` 个实根，符合下界与 parity。

这些有限检查只核各明确实例和代码内部算术；一般有限自由、单位、复根计数和 degree 结论由本页逐步证明承担。独立 narrow counterattack 复核了 localization、非法分母与 local Artin factor 步骤，未找到现存 fatal objection。本页不核外部发表先行性。

## 有向主候选的准确复用

对于 D=(7/25)(I−S)+(11/50)(I−S⁻¹)，模3下两个方向权重都为1，故 D̄=L、Ā=L−I。上述一般引理明确不要求 A 对称，所以所有 complex roots 的正则性与数量同样成立。实指数必须另查 DH(p) 的可逆与方向；主卡给 connected SymDH 正定证明，不能从 DF 可逆自动替代。
