# 残差窗口到邻域误差界的精确充分门

版本 RW-v1，2026-10-01。固定**完整**关系的最小残差，避免把某条选中分支的范数替代下确界。

<a id="rw-object"></a>
## RW-OBJECT · 两种量词

实 Hilbert 空间 \(H\) 上 \(F:H\rightrightarrows H\)，\(S=F^{-1}(0)\ni\bar u\)，\(r_F(u)=\inf_{v\in F(u)}\|v\|\)；空纤维取 \(+\infty\)。令 \(\eta\in(0,\infty]\) 及有限非减 gauge \(\psi:[0,\eta)\to[0,\infty)\)，\(\psi(0)=0\)、\(\psi(t)\to0\) 当 \(t\downarrow0\)。

**窗口版**：存在邻域 \(U\ni\bar u\) 和 \(0<\delta<\eta\)，使每个 \(u\in U\) 且 \(r_F(u)<\delta\) 满足 \(d(u,S)\le\psi(r_F(u))\)。

本页的**可评价邻域版**：存在邻域 \(V\ni\bar u\)，使每个 \(u\in V\) 且 \(r_F(u)<\eta\) 满足同一不等式；不要求 \(r_F(u)<\delta\)。当 \(\eta=\infty\)，所有有限残差都可评价。若希望连 \(+\infty\) 或超过有限 \(\eta\) 的残差也写入公式，必须先另给 gauge 的扩展定义，不能对未定义的 \(\psi(r_F(u))\) 断言不等式。

<a id="rw-positive"></a>
## C59-v1 / RW-POSITIVE · 正阈值门

**命题。** 若窗口版成立且还可选其阈值 \(0<\delta<\eta\) 满足 \(\psi(\delta)>0\)，则在
\[
V=U\cap B(\bar u,\psi(\delta))
\tag{RW-1}
\]
上可评价邻域版成立。若 \(\psi\) 有非减延拓至全部 \([0,\infty)\)（可令空纤维处取 \(+\infty\)），同一 \(V\) 上还可对全部可评价残差陈述不等式，故覆盖通常的无窗口邻域版本。正幂 \(\psi(t)=\rho t^q\)、\(\rho,q>0\)，是特殊情形。

**证明。** 对 \(u\in V\) 且 \(r_F(u)<\delta\)，用原窗口界。对 \(\delta\le r_F(u)<\eta\)，由于 \(\bar u\in S\)，
\[
d(u,S)\le\|u-\bar u\|<\psi(\delta)\le\psi(r_F(u)).
\]
如果 gauge 已全域延拓，对 \(r_F(u)\ge\eta\) 的有限值作相同单调性论证；空纤维按所声明的 \(+\infty\) 约定处理。□

这是一条**充分**门，不声称 \(\psi(\delta)>0\) 对具体 \(F\) 必要。例如若邻域中全部残差本来已小于 \(\delta\)，即使 \(\psi(\delta)=0\) 也没有新点要控制。

<a id="rw-flat"></a>
## RW-FLAT · 闭图仍不足以删掉正阈值门

令 \(H=\mathbb R\)、\(F(0)=\{0,1\}\)，而 \(F(u)=\{1\}\) 对 \(u\ne0\)。完整图 \(\mathbb R\times\{1\}\cup\{(0,0)\}\) 闭；\(S=\{0\}\)、\(r_F(0)=0\)，对所有 \(u\ne0\) 有 \(r_F(u)=1\)。令全域有限非减 gauge \(\psi(t)=\max\{t-2,0\}\)（原点连续），取 \(\delta=1/2\)。窗口版只检验 \(u=0\)，所以成立；任意零邻域含非零 \(u\)，其 \(d(u,S)=|u|>0=\psi(1)\)，可评价邻域版失败。

这个反例不满足 all-pairs RL，也不声称在附加 RL/coverage 下仍失败；它只否定从**窗口版定义、闭图及一般允许的 gauge**无条件推出邻域版。若另外知道靠近 \(\bar u\) 的所有有限残差都落在窗口内，那是另一条可用桥。

<a id="rw-source"></a>
## 来源、状态与调用

- 历史来源：[RL_foundations.md 定义0.4](../../history/sources/次单调论文研究/RL_foundations.md) 的窗口约定和幂函数缩域证明；[PD-RESIDUAL](parameter_dictionary.md#pd-residual) 记录真残差与分支范数方向。本页从一般非减 gauge 独立推导正阈值判据，并新构造闭图反例；不主张文献新颖性。
- 状态：derived-checked，限于本页明确的残差定义域、完整零集和 gauge 量词。任何算法输入还需实际输出位于 \(V\)、真残差窗口、coverage 与留域分别核验。
