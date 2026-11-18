# RLEB 与输出相对步长接口的量词阻塞

## Status

`derived-checked` obstruction。本文只比较仓库正式 RLEB 主定理
`theorem_spine.tex` 的 P1--P4 与用户接口
\[
\tag{A}d(y,S)\le \kappa d(x,S),\qquad
\tag{B}\|x-y\|\le B_0d(y,S).
\]
它不提出新的收敛定理；作用是固定下一轮任务的可满足量词。

## Formal RLEB 前提

正式主定理的 P1--P4 分别是输入 coverage、非线性 RL 最近零锚估计、完整真残差误差界
\(d(y,S)\le\psi(r_F(y))\) 及输出窗、直接兼容
\(\psi(B_R(t)/\lambda)\le\kappa t\) 与 Dini 长度预算，其中
\[
B_R(t)=\frac{t+\omega(t)}2.
\]
它们推出的是
\[
d(y,S)\le\kappa d(x,S),\qquad
\|x-y\|\le B_R(d(x,S)),
\]
而不是输出相对的 (B)。这两个步长界的分母不同，不能在摘要中视为同一条件。

## Exact counterexample

取
\[
X=\mathbb R,\quad \lambda=1,\quad S=\{0\},\quad
F(y)=\operatorname{sgn}(y)\sqrt{|y|},
\]
以及完整近端关系
\[
x=y+F(y).
\]
映射 \(h(y)=y+\operatorname{sgn}(y)\sqrt{|y|}\) 是严格递增满射，所以完整 resolvent 全域单值且 coverage 全域成立。固定
\[
R=\frac14,\quad \gamma=\frac12,\quad L=\frac12,
\quad \omega(t)=L\sqrt t,\quad
\psi(s)=s^2,\quad \kappa=\frac12,\quad \bar t=\frac14.
\]

### P1--P2

P1 由 \(h\) 的满射性成立。\(F\) 单调，因此对任意两图点
\[
|\Delta y-\Delta v|\le |\Delta y+\Delta v|.
\]
取零图点作为最近零锚，且在 \(|x|\le R\) 时
\[
|x|\le \sqrt R\sqrt{|x|}=L|x|^{1/2}=\omega(|x|),
\]
得到正式 RL/P2 的最近锚估计。等价地，P2 的右端
\((|x|^2-\omega(|x|)^2)/4\) 在该窗口不为正，而
\(\langle y,x-y\rangle=|y|^{3/2}\ge0\)。

### P3

对每个输出
\[
r_F(y)=\sqrt{|y|},\qquad d(y,S)=|y|=\psi(r_F(y)),
\]
所以完整真残差误差界在整个输出集上成立。

### P4 与长度预算

\[
B_R(t)=\frac{t+\frac12\sqrt t}{2},\qquad
\frac{B_R(t)^2}{t}=\frac t4+\frac{\sqrt t}4+\frac1{16}\le\frac14<\kappa
\]
对 \(0<t\le R\) 成立。因此直接兼容成立；\(B_R(R)=R\le\bar t\)，且
\[
\sum_{j\ge0}B_R(\kappa^jR)
=\frac{R}{2(1-\kappa)}+
\frac{L\sqrt R}{2(1-\sqrt\kappa)}<\infty.
\]
\(U=X\) 时留域预算自动成立。故该例满足正式 RLEB 的全部 P1--P4。

### Failure of output-relative (B)

取 \(y\downarrow0\) 且 \(y>0\)。则
\[
x=y+\sqrt y,\qquad \|x-y\|=\sqrt y,qquad d(y,S)=y,
\]
从而
\[
\frac{\|x-y\|}{d(y,S)}=y^{-1/2}\longrightarrow\infty.
\]
因此不存在有限常数 \(B_0\) 使输出相对的 (B) 成立。

## Logical consequence

令 \(H_{\rm RLEB}\) 表示正式 P1--P4。若存在任何中间条件 \(M\) 满足
\[
H_{\rm RLEB}\Longrightarrow M\Longrightarrow (A)+(B),
\]
则传递性给出 \(H_{\rm RLEB}\Longrightarrow(B)\)，与上例矛盾。因此在当前正式定义下，用户要求的“严格弱于 RLEB 且强于 A+B”的任务没有可满足解；问题不在候选 \(M\) 尚未找到，而在比较链的前提与结论不相容。

## Minimal repair

有两种不改变数学对象的修正：

1. 将接口 (B) 改成正式主定理实际给出的输入步长包络
   \(\|x-y\|\le B_R(d(x,S))\)，再研究一个严格介于 P1--P4 与该接口之间的独立条件；或
2. 明确把输出相对 (B)（或一个逐输出、选中值的上界 \(\|x-y\|\le C d(y,S)\)）加入旧基线 \(H_{\rm old}\)，然后再寻找
   \(H_{\rm old}\Rightarrow M\Rightarrow(A)+(B)\) 且反向严格失败的条件。

在修正前，任何声称完成该中间定理的结果都必然偷换了 B 的定义、量词或旧 RLEB 前提。
