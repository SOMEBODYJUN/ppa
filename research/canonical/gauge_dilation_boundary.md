# 同一个超线性 gauge 不能无条件穿过 Minty 坐标

本页补全 foundations 来源 §7.2 的阶梯 gauge 边界。结论针对同一个函数 \(\psi\) 的逐点比较；[IZ-GERM](isolated_zero_flatness.md#iz-germ) 保留自变量重标度的正向结论继续成立。全部论证在下面直接给出，不使用来源稿代替证明。

<a id="gd-object"></a>
## GD-OBJECT · gauge 与完整标量关系

令 \(t_n=2^{-2^n}\)（\(n=0,1,\ldots\)），所以 \(t_0=1/2\)、\(t_1=1/4\)、\(t_{n+1}=t_n^2\)。在 \([0,1/2)\) 定义

\[
\psi(0)=0,\qquad
\psi(t)=t_n^2\quad\text{当 }t_n\le t<t_{n-1},\ n\ge1.
\tag{GD-1}
\]

区间互不相交且覆盖 \((0,1/2)\)，端点取右侧较大值。\(\psi\) 有限、非减、严格正于正自变量，且 \(\psi(t)=o(t)\)。确实，在第 \(n\) 个区间内有 \(0<\psi(t)/t\le t_n\)，而 \(t\downarrow0\) 时相应 \(n\to\infty\)。本例只要求在零点连续，不宣称 \(\psi\) 在正点连续。

固定 \(H=\mathbb R\)、\(\lambda=1\)、\(p=0\)，声明**完整图**

\[
\operatorname{gph}F=\{(0,0)\}
 \cup\{(y_n,w_n)=(-t_n^2,t_n):n\ge1\}.
\tag{GD-2}
\]

因此 \(F(0)=\{0\}\)、\(F(y_n)=\{t_n\}\)，其余点为空；图是非空紧集，完整零集为 \(S=\{0\}\)。使用真实全纤维残差 \(r_F(y)=\inf_{w\in F(y)}|w|\)，空纤维残差为 \(+\infty\)。

<a id="gd-theorem"></a>
## C159-v1 · 真实超线性 EB 不保证不重标度的同 gauge 分支界

对 GD-OBJECT 有以下三个同时成立的结论。

1. 对任意 \(0<\delta<1/2\)，在整个 \(\mathbb R\) 的所有 \(r_F(y)<\delta\) 的点上，
   \[
   |y|=\psi(r_F(y)). \tag{GD-3}
   \]
   特别地，这是同一完整关系、孤立零点和真实残差上的窗口 EB。
2. 完整 resolvent 的自然输入域为
   \[
   D=\{0\}\cup\{x_n=t_n-t_n^2:n\ge1\},
   \qquad J_F(0)=\{0\},\quad J_F(x_n)=\{y_n\}. \tag{GD-4}
   \]
   对所有 \(C<\infty\) 和所有含 \((0,0)\) 的图邻域，总有其中的图点使
   \[
   |y|>C\psi(|x|),\qquad x=y+w. \tag{GD-5}
   \]
   即使 \(|y|\le\psi(|w|)\) 在完整图上成立，固定同一 \(\psi\) 的 \(J\)-界仍在每个 graph germ 失败。
3. 正确的重标度界在整个自然输入域成立：
   \[
   |J_Fx|\le\psi(2|x|)\quad(x\in D), \tag{GD-6}
   \]
   这里 \(|J_Fx|\) 表示唯一输出的绝对值，所有右侧自变量都属于 \([0,1/2)\)。

**证明。** 有限残差点恰为 \(0,y_1,y_2,\ldots\)。由完整单点纤维，\(r_F(y_n)=t_n\) 且 \(\psi(t_n)=t_n^2=|y_n|\)，零点两边均零，得 GD-3。自然输入就是各图点的 \(y+w\)；函数 \(t-t^2\) 在 \((0,1/4]\) 严格递增，所以不同 \(t_n\) 给不同正输入，各完整输入纤维只有所列输出。这证明 GD-4。

因为 \(0<t_n\le1/4\)，有
\[
t_{n+1}=t_n^2\le x_n=t_n-t_n^2<t_n,
\qquad \psi(x_n)=t_{n+1}^2=t_n^4.
\]
故 \(|y_n|/\psi(x_n)=t_n^{-2}\to\infty\)。同时 \((y_n,w_n)\to(0,0)\)，因此任意缩小 graph germ 和有限常数都不能修复 GD-5。

最后 \(t_n\le2x_n<2t_n\le1/2\)，最右等号仅在 \(n=1\) 的粗界，实际 \(2x_1=3/8<1/2\)。\(\psi\) 非减给 \(\psi(2x_n)\ge\psi(t_n)=|y_n|\)；零输入也成立。这证明 GD-6。□

<a id="gd-dilation"></a>
## 缺少的是固定 dilation 控制

令 \(s_n=t_n/2\)。由于 \(t_{n+1}\le s_n<t_n\)，
\[
\frac{\psi(2s_n)}{\psi(s_n)}
=\frac{t_n^2}{t_{n+1}^2}=t_n^{-2}\longrightarrow\infty.
\tag{GD-7}
\]
所以 \(\psi=o(\mathrm{id})\) 不蕴含 \(\psi(2t)=O(\psi(t))\)。若另有这一 dilation 界，IZ-GERM 的 \(\lambda=1\) 重标度结果 \(|y|\le\psi(2|x|)\) 才能推出 \(|y|\le C\psi(|x|)\)。本例在 \(\lambda=1\) 已失败，因此无需改变步长归一化来制造障碍。

<a id="gd-scope"></a>
## 身份、来源与边界

- **Status：** `derived-checked` 限 GD-1–7 的显式 gauge、完整图、残差和坐标计算；不作外部先行性判断。
- **依赖：** [D01 的完整残差与 Minty 坐标](../foundations.md#d01)、[IZ-GERM 的带重标度正向关系](isolated_zero_flatness.md#iz-germ)。反例的所有性质在本页直接证明。
- **来源：** `history/sources/次单调论文研究/RL_foundations.md` 物理 LF 1088–1134，特别是 1117–1126 的同 gauge / dilation 边界；该处只提到阶梯构造，本页给出函数、端点和完整原图。
- **适用边界：** \(D\) 不含零点的输入邻域，故本例不认证局部全输入 PPA；正点不连续的 gauge 也不反驳额外要求连续 gauge 的命题。反射缺陷恒等式 \(|(y-w)+x|=2|y|\) 使同 gauge 的反射缺陷界同样失败，正确的 \(2\psi(2|x|)\) 界仍成立。没有把选中残差替代为完整残差：两者在所声明完整单点纤维处确实相等。
