# C308 · 周期 SPD 变度量 PPA 的 Floquet 临界中心流形

**状态：** candidate / major-potential conditional；C307 的并行第二主线。

## 精确对象

取 \(F\in C^r(\mathbb R^n;\mathbb R^n)\) 强单调，\(F(0)=0\)，周期 SPD 度量 \(M_{k+p}=M_k\)，并定义完整精确步

\[
M_k(x_k-x_{k+1})=\lambda F(x_{k+1}).
\]

若每个 \(M_k+\lambda DF(0)\) 正定可逆，单步映射为

\[
T_k=(M_k+\lambda DF(0))^{-1}M_k,
\qquad
\Phi=T_{p-1}\circ\cdots\circ T_0,\qquad
P=D\Phi(0).
\]

候选主定理：若 \(P\) 有简单半单 multiplier \(1\)，其余 multiplier 满足 \(|\mu|<1\)，则 \(\Phi\) 在中心流形上的首个非零正规形系数决定临界命运。若

\[
\Phi|_{W^c}(u)=u+c_\ell u^\ell+o(|u|^\ell)
\]

且 \(\ell\) 是首个非零阶，则奇数 \(\ell\) 时 \(c_\ell<0\) 给两侧吸引、\(c_\ell>0\) 给两侧排斥；偶数 \(\ell\) 时两侧命运相反。若要断言精确周期，必须另加 \(\Phi|_{W^c}\equiv\operatorname{Id}\) 或明确的有限阶恒等条件；“所有已计算系数为零”本身不够。

## 可复核的强单调根式族

令

\[
A=I+3J=
\begin{pmatrix}1&-3\\3&1\end{pmatrix},
\quad
\lambda=\frac1{10},
\quad
\delta=\frac\pi3,
\quad
D=\operatorname{diag}\!\left(1,\frac{3\sqrt3-2}{23}\right),
\]

\[
M_k=R_{-k\delta}DR_{k\delta},\qquad p=6.
\]

在旋转坐标 \(z_k=R_{k\delta}x_k\) 中，线性一步为

\[
B=R_\delta(D+\lambda A)^{-1}D.
\]

直接化简得

\[
\operatorname{spec}(B)=\{1,q\},
\qquad
q=\frac{50-20\sqrt3}{39}\in(0,1),
\qquad
\operatorname{spec}(B^6)=\{1,q^6\}.
\]

因此 \(P=B^6\) 有简单中心 multiplier 1 与一条强稳定方向。取紧支 \(\chi\equiv1\) 于原点邻域并令

\[
F_\varepsilon(x)=Ax+\varepsilon\chi(\|x\|)\|x\|^2x.
\]

对足够小的 \(|\varepsilon|\)，对称 Jacobian 仍有统一正下界，故 \(F_\varepsilon\) 强单调、每个 \(M_k+\lambda F_\varepsilon\) 全域双射，且完整 resolvent 不依赖被删掉的远根。

在中心方向 \(v,w\) 归一化为 \(w^\top v=1\) 后，六步映射的三阶中心系数（按多项式展开约定）为

\[
c_3=\frac{156(-4643+243\sqrt3)}{288923}\ne0.
\]

因此

\[
u_{m+1}=u_m+\varepsilon c_3u_m^3+O(u_m^5).
\]

当 \(\varepsilon>0\) 时 \(\varepsilon c_3<0\)，中心方向两侧吸引且 \(u_m\sim(-2\varepsilon c_3m)^{-1/2}\)；当 \(\varepsilon<0\) 时中心方向排斥，除强稳定余维一流形外，小的非零中心坐标最终离开局部管。在线性 \(\varepsilon=0\) 情形，中心方向在六步后保持不动，原物理坐标形成 \(6\)-周期。

## 与既有仓库的差异与硬边界

- C284/UI33 已有同一类强单调原算子与旋转 SPD 的线性发散反例；它不能再被包装成“首次证明移动度量可发散”。
- 新增量必须是 PPA-specific 的周期 monodromy 临界分类、可计算高阶 jet 系数、强单调全局例及对平滑非线性扰动的命运翻转。
- 一般离散中心流形定理是外部工具，不承担新颖性本身；论文必须证明周期 resolvent 结构如何决定系数并给出 sharp 的正/负例。
- 需要处理 \(-1\) 临界、Jordan 块、多个单位 multiplier 和 flat center remainder；当前候选只覆盖单一简单 multiplier 1。

## 决定性下一步

1. 写出任意周期 SPD cocycle 的 p-step normal-form 定理和所有量词；
2. 证明上述根式族的三阶系数与全局强单调门，不依赖浮点数；
3. 给出至少一个与 C284 不同的周期或准周期设计准则，说明何时高阶 jet 可被算法设计者改变；
4. 完成变量度量 PPA、离散中心流形和非线性扰动文献的逐定理优先性审计。

