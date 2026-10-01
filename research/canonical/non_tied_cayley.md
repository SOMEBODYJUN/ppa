# 非 tied 二参数图：平移 Cayley 球、锐常数与极大性

<a id="nt-object"></a>
## NT-OBJECT · 身份、量词与来源

版本 NT-v1，2026-10-01。C89 包含 NT-QUADRATIC、NT-SHARP 与 NT-STEP 的同图条件链；C90 是可独立使用的图变换；C91 另调用 Hilbert 扩张以刻画满域。固定非零实 Hilbert 空间 \(H\)、非空图
\(\Gamma\subset H\times H\)、实参数 \(\mu,\rho\) 和步长 \(\lambda>0\)。
这里的二参数条件始终是**同一图的全部点对**：
\[
\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2,
\qquad a=x-x',\ b=v-v',\quad (x,v),(x',v')\in\Gamma.
\tag{NT1}
\]
固定基点的单锚条件不够。代数部分允许指定图块；后文“极大”只指
在整个 \(H\times H\) 中保持同一 \((\mu,\rho)\) 的图包含极大，
不指局部邻域内的极大性，也不指极大单调，除非参数正好为零。

主要来源是 [9/01 monotonicity ZIP](../../history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip)
成员 `work/a_monotonicity.md` §2.1，精确对应 (2.1)–(2.4)、退化面和单调变换。
ZIP SHA-256 为 `b40d2aae4eef13ef2df2840df1b74333793e56de112addab7eca67dfc9bdd3ba`，
成员字节 SHA-256 为 `ca1a8009975c27fd3d93aeeb97e93f348f87acdeb5db10e55e531197ffe74490`。
[另一个 checkpoint](../../history/sources/次单调论文研究/RL_monotonicity_regularity_research_checkpoint_2026-09-01.zip)
的同路径成员具有相同字节哈希；其 ZIP SHA-256 为
`fbd73364456dba5d487ed86758a70e597c3e902201aa4ed68d6c2373fa2f1feb`。
两份副本不是两份独立数学证据。

**证据范围**：下文平方恒等式、最优常数、退化例与图变换均在此直接证明；
NT-MAXIMAL 唯一外部数学输入是规范库已核的 Hilbert 同常数 Lipschitz 扩张。
来源引用的论文命名、原定理编号和新颖性不在本页验收；无限维范围来自本页证明，
并非把来源所报有限维论文定理改写为无限维 paper fact。

<a id="nt-quadratic"></a>
## C89-v1 / NT-QUADRATIC · 精确的交叉项与平移球

令
\[
m=\lambda\mu,\qquad s=\rho/\lambda,\qquad
A=1+m+s,\qquad B=m-s,\qquad \Delta=1-4\mu\rho.
\tag{NT2}
\]
对同一图点对置 \(d=a+\lambda b\)、\(r=a-\lambda b\)。
不加任何参数符号限制，(NT1) 精确等价于
\[
A\|r\|^2+2B\langle d,r\rangle
\le(1-m-s)\|d\|^2.
\tag{NT3}
\]
若另有 \(A>0\)、\(\Delta\ge0\)，则等价地
\[
\left\|r+\frac BA d\right\|
\le\frac{\sqrt\Delta}{A}\|d\|.
\tag{NT4}
\]
特别地，Minty 自然域及 Cayley 映射
\[
D=\{x+\lambda v:(x,v)\in\Gamma\},\qquad
C(x+\lambda v)=x-\lambda v
\tag{NT5}
\]
良定，且 (NT1) 等价于 \(G=C+(B/A)I:D\to H\) 为
\(\sqrt\Delta/A\)-Lipschitz。相应图块近端映射为 \(J=(I+C)/2\)。
若 \(\Gamma\) 仅是 \(\operatorname{gph}F\) 的一部分，这里的 \(J\)
仍只是图块映射；完整纤维相等要另证。

**证明。** 用
\(a=(d+r)/2\)、\(\lambda b=(d-r)/2\) 和
\(4\lambda\langle a,b\rangle=\|d\|^2-\|r\|^2\) 展开 (NT1)，
移项即得 (NT3)。又有
\[
A(1-m-s)+B^2=1-4ms=\Delta,
\]
配方给 (NT4)。当 \(d=0\) 时，(NT3) 与 \(A>0\) 强迫 \(r=0\)，
故两个 Minty 输入相同的图点必相同。反向将 (NT4) 平方并撤销配方，
即恢复 (NT1)。所有量词都在同一个 \(D\) 上，证明没有产生 \(D=H\)。

<a id="nt-sharp"></a>
## NT-SHARP · 两个不同的锐普适常数

在 \(A>0\)、\(\Delta\ge0\) 下，每一张满足 (NT1) 的图都满足
\[
\operatorname{Lip}(C;D)\le
L_C:=\frac{|m-s|+\sqrt\Delta}{1+m+s},
\tag{NT6}
\]
\[
\operatorname{Lip}(J;D)\le
L_J:=\frac{|1+2s|+\sqrt\Delta}{2(1+m+s)}.
\tag{NT7}
\]
对固定参数和步长，这两个常数在**所有满足 (NT1) 的图**中分别最优，
甚至可由具有完整 Minty 域 \(D=H\) 的线性关系达到。
“最优”不表示每个给定算子的最优常数都等于该普适上界；两个上界也不必由同一张图取等。

**证明。** (NT4) 及三角不等式立即给 (NT6)。又
\[
2(Jp-Jq)=\left(1-\frac BA\right)(p-q)+(Gp-Gq),
\]
且 \(A-B=1+2s\)，故得 (NT7)。

为证锐性，取任意实数
\[
c\in\left[\frac{-B-\sqrt\Delta}{A},\frac{-B+\sqrt\Delta}{A}\right],
\quad C_c(p)=cp\quad(p\in H),
\]
并定义**完整关系图**
\[
\Gamma_c=\left\{\left(\frac{1+c}{2}p,
\frac{1-c}{2\lambda}p\right):p\in H\right\}.
\tag{NT8}
\]
其自然域就是 \(H\)，而 (NT4) 等价于
\(|c+B/A|\le\sqrt\Delta/A\)，所以整图满足 (NT1)。
在两个端点取 \(|c|\) 的较大值，恰得 (NT6)；在两个端点取
\(|1+c|/2\) 的较大值，恰得 (NT7)。由于 \(H\ne\{0\}\)，这些比值可由不同输入取到。
当端点 \(c=-1\) 时，(NT8) 是 \(\{0\}\times H\) 的竖直完整关系；
它是合法集合值对象，不能因原算子不是单值而删去取等例。

### 单一反射常数丢失的信息

固定 \(\lambda=1,\mu=1,\rho=0\)，则 (NT4) 要求
\(\|\Delta C+\tfrac12\Delta p\|\le\tfrac12\|\Delta p\|\)。
完整图 \(F_-(x)=3x\) 与 \(F_+(x)=x/3\) 的 Cayley 映射分别是
\(C_-=-I/2\)、\(C_+=I/2\)，反射 Lipschitz 常数同为 \(1/2\)。
前者满足 (NT1)，后者因 \(\langle a,b\rangle=\|a\|^2/3<\|a\|^2\)
而失败。故反射模的一个数不能恢复非 tied 二参数条件。
当 \(m=s\) 时交叉项才消失，恢复
[PD-TIED](parameter_dictionary.md#pd-tied) 的精确曲线；
它不能用于替代本页的整个二参数区域。

<a id="nt-step"></a>
## NT-STEP · 锐步长门与退化面

若 \(\Delta>0\)，则 \(A>0\) 精确等价于
\[
\frac{2[-\rho]_+}{1+\sqrt\Delta}<\lambda<
\frac{1+\sqrt\Delta}{2[-\mu]_+},
\tag{NT9}
\]
右端分母为零时取 \(+\infty\)，\([t]_+=\max\{t,0\}\)。
这是**整个二参数类统一保证 Minty 单射及上述有限常数**的锐条件。
某一特定图在此区间外仍可能有单值近端；不声称逐算子的必要性。

**证明。** \(A>0\) 等价于 \(\mu\lambda^2+\lambda+\rho>0\)。
若 \(\mu,\rho\ge0\)，全部正步长可用。若 \(\mu\ge0,\rho<0\)，
唯一正根为 \(-2\rho/(1+\sqrt\Delta)\)，取其右侧；此式也覆盖 \(\mu=0\)。
若 \(\mu<0,\rho\ge0\)，取正根 \((1+\sqrt\Delta)/(-2\mu)\) 的左侧。
若两参数均负，\(0<\Delta<1\)，开口向下且两个正根之间恰为 (NT9)。

反向攻击在所有 \(A\le0\) 的参数步长组合上都有效：取
\(F(x)=-x/\lambda\) 的全图，则 (NT1) 等价于
\(-1\ge m+s\)，正是 \(A\le0\)。此时
\(D=\{0\}\)、\(J_{\lambda F}(0)=H\)。因此端点不得仅因 (NT7) 的形式可写
而收入允许步长；任意原点消失的全对反射模在此图上均失败。

另外两种来源退化面可直接裁决：

1. 若 \(\mu,\rho<0\) 且 \(\mu\rho\ge1/4\)，**每一张图**都满足 (NT1)。
   令 \(\alpha=-\mu,\beta=-\rho\)，则
   \(\langle a,b\rangle+\alpha\|a\|^2+\beta\|b\|^2
   \ge(2\sqrt{\alpha\beta}-1)\|a\|\|b\|\ge0\)。
   此时 \(A\le0\) 对全部正步长成立，没有本页的统一单射门。
2. 若 \(\mu,\rho>0\) 且 \(\mu\rho>1/4\)，任意满足 (NT1) 的非空图只有一个点。
   Cauchy–Schwarz 与加权算术几何平均使非零差满足
   \(\|a\|\|b\|\ge2\sqrt{\mu\rho}\|a\|\|b\|\)，不可能；
   若其中一差为零，(NT1) 又强迫另一差为零。
   当 \(\mu\rho=1/4\) 时，同一取等分析给 \(b=2\mu a\)，
   所以图包含于某一仿射斜率图 \(v=2\mu x+v_0\)。
   这里 \(A>0,\Delta=0\)，NT-QUADRATIC 与 NT-SHARP 仍适用，
   但下一节含 \(1/\sqrt\Delta\) 的变换不适用。

<a id="nt-transform"></a>
## C90-v1 / NT-TRANSFORM · 保图包含的单调变换

只假设 \(\Delta>0\)，无需选择步长或要求 (NT9)。令
\[
t=\sqrt\Delta,\qquad \nu=\frac{2\mu}{1+t},\qquad
\xi=\frac\rho t,
\]
并对每个图点定义
\[
w=v-\nu x,\qquad z=x-\xi w.
\tag{NT10}
\]
则 \(\Gamma\) 满足 (NT1) 当且仅当
\(\mathcal M=\{(w,z):(x,v)\in\Gamma\}\) 单调。
若 \(\Gamma=\operatorname{gph}F\)，这就是关系
\(\mathcal M=(F-\nu I)^{-1}-\xi I\)，所有逆均保留完整纤维。
而且 \(\Gamma\) 为全局同参数图极大当且仅当 \(\mathcal M\) 极大单调。

**证明。** 由 \(2\rho\nu=1-t\)、\(\mu=\nu-\rho\nu^2\)，直接展开得
\[
\langle\Delta w,\Delta z\rangle
=\frac1t\left(\langle a,b\rangle-\mu\|a\|^2-\rho\|b\|^2\right).
\tag{NT11}
\]
式子在 \(\rho=0\) 或 \(\mu=0\) 时也成立，不需要除以这些参数。
映射 (NT10) 可由 \(x=z+\xi w\)、\(v=w+\nu x\) 反演，
所以是 \(H\times H\) 上的线性双射，并双向保持严格图包含。
(NT11) 给性质等价，图包含双射给极大性等价。
这是任意实 Hilbert 空间上的直接证明，没有调用有限维闭图或满域定理。

<a id="nt-maximal"></a>
## C91-v1 / NT-MAXIMAL · 全局同参数极大性与完整 Minty 域

固定 \(\lambda>0\) 且 \(A>0,\Delta\ge0\)。非空图 \(\Gamma\) 满足 (NT1) 时，
\[
\Gamma\text{ 为全局同 }(\mu,\rho)\text{ 参数图极大}
\quad\Longleftrightarrow\quad D=H.
\tag{NT12}
\]
任意这样的图都有保持相同二参数的完整 Minty 域扩张。
本节所用扩张结论是
[HE-EXTENSION](holder_extension.md#he-extension) 的 \(\gamma=1\) 情形：
任意实 Hilbert 源/目标间、任意子集上的 \(K\)-Lipschitz 映射，
有同常数的全空间扩张；该接口在
[LIT-ALM-2021 Theorem 1.2](../LITERATURE.md#lit-alm-2021) 已逐项核验。

**证明。** 由 NT-QUADRATIC，\(G=C+(B/A)I\) 是
\(K=\sqrt\Delta/A\)-Lipschitz。扩张为 \(\widehat G:H\to H\)，
再置 \(\widehat C=\widehat G-(B/A)I\)，按 Cayley 逆坐标构造
\[
\widehat\Gamma=\left\{\left(\frac{p+\widehat C(p)}2,
\frac{p-\widehat C(p)}{2\lambda}\right):p\in H\right\}.
\]
NT-QUADRATIC 保证该整图满足 (NT1)，且包含原图。若 \(D\ne H\)，
任取缺失输入所得图点不属于原图，扩张严格，故原图不极大。
若 \(D=H\)，任何同参数新图点都有与原图某点相同的 Minty 输入；
(NT3) 与 \(A>0\) 强迫反射相同，图点亦相同，因此不存在真扩张。
当 \(K=0\) 时，非空域上的 \(G\) 是常值，常值扩张已足够。

**调用边界。** 这里的全图、全对和同参数均为承重条件。
对局部图块加上未定义清楚的“局部极大”标签，不能得到整个 \(H\) 的 coverage；
即使 \(D=H\)，本页也没有证明原算子真残差 EB、零集存在、留域或近端收敛。
例如 \(\mu=\rho=0\) 下完整常值图 \(F(x)=v_0\ne0\) 满输入且满足 (NT12)，
却没有零点。此例的同参数图极大性由 (NT12) 已证，毋需另引定理。

<a id="nt-audit"></a>
## 来源去向与本页新增部分

| 精确来源单元 | 本页去向 | 证据与范围 |
| --- | --- | --- |
| §2.1 定义、(2.4) | NT-OBJECT、NT-QUADRATIC | 全对量词与交叉项独立展开；平移球为本页配方 |
| §2.1 (2.2)–(2.3) | NT-STEP、NT-SHARP | 步长门和 \(L_J\) 重证；\(L_C\)、两个普适锐性和端点碰撞为本页补证 |
| §2.1 两个退化面 | NT-STEP | 正正单点/仿射与负负全图均直接证明 |
| §2.1 单调逆变换与同参数极大性 | NT-TRANSFORM | 显式双射及二次型恒等式直接证明；Hilbert 范围为本页推导 |
| §2.1 满域与极大性句 | NT-MAXIMAL | 同参数平移球结合已核 Hilbert 扩张；不调用来源所报外部定理 |
| §2.1 (2.1) 逆与缩放 | 定义的直接代换 | \(F^{-1}\) 交换 \(\mu,\rho\)；对 \(c>0\)，\(cF\) 变为 \((c\mu,\rho/c)\)，因为对 (NT1) 乘以 \(c\) 后令新差为 \(cb\) |

本页状态为 `derived-checked`，只覆盖上述数学单元。独立代理重算了配方、两个锐常数、步长端点、变换恒等式与极大性范围；其检查特别保留了右端零分母约定及 NT-MAXIMAL 的 \(\Delta\ge0\) 门。这不是外部同行评审。
外部文献名称/优先权、同稿 §2.2 及以后其他类、局部极大性的不同约定仍未在本页验收。
本页没有以相同字节副本或已有 PD-TIED 再登记一份独立成果；
新内容是独立二参数下可直接调用的完整证明链及其明确边界。
