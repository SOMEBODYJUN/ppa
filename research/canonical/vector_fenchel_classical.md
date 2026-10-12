# 向量 Fenchel–Young 完整 GPPA 的经典正面

本页 C269-v1 是一个自然共轭一致性模型的完整正面反审。全空间、全部 stationary 根、任意固定正步长和任意根切换均收敛；因此该模型不能作为“旧分析思想无法处理”的强优势例。证明为本轮推导，使用经典凸径向增量及逆模；没有认证某篇发表论文已经给出同式结果或其公开优先。

<a id="vfc-object"></a>
## 完整模型与全部纤维

任意 $n\ge1$，$x,s\in\mathbb R^n$，令 $B(t)=\|t\|^2t$、$C(t)=\|t\|^4t$、$R=B^{-1}$，均在零点连续取零。定义

\[
f(x,s)=\frac34\|x\|^{4/3}+\frac14\|s\|^4-\langle x,s\rangle\ge0,
\quad h(x,s)=\frac12\|x\|^2+\frac16\|s\|^6,
\]
\[
F=\nabla f=(R(x)-s,B(s)-x),\quad v=\nabla h=(x,C(s)),
\quad S=\{(B(c),c):c\in\mathbb R^n\}.
\tag{VF1}
\]

Fenchel 等号及第一梯度分量给 $S=\operatorname{argmin}f=F^{-1}(0)$，闭且非孤立；真残差是 $\|F\|$。核在原点退化，$R$ 在原点只有 $1/3$ 阶。固定任意 $\lambda>0$，输入域全 $\mathbb R^{2n}$，完整算法 $J^v_{\lambda F}=(v+\lambda F)^{-1}v$ 的全部输出写 $x=B(r)$ 后恰为

\[
a=B(r)+\lambda(r-s),\qquad
C(b)=C(s)+\lambda(B(s)-B(r)).
\tag{VF2}
\]

此式是全部纤维的双向身份，不只一支。每个输入均有根：$h+\lambda f-\langle v(a,b),(x,s)\rangle$ 为 $C^1$ coercive 函数，至少一个 global minimum 的 Fermat 条件供应根；全部其他 stationary 根均保留。

非极小根真实存在并可趋原点。任意单位 $u$、$t>0$，取输出 $(t^3u,0)$、输入 $((t^3+\lambda t)u,-(\lambda t^3)^{1/5}u)$，满足 VF2。其 joint stationary 子问题在纯 $s$ 方向的二阶项为零，而非零交叉 Hessian 块为 $-\lambda I$，存在负曲率方向，因此并非 local minimum。后面全部估计均包括这些根。

<a id="vfc-max"></a>
## 全部远输出的最大原则

令 $M=\max\{\|a\|^{1/3},\|b\|\}$。每个完整根都满足

\[
\max\{\|r\|,\|s\|\}\le M.
\tag{VF3}
\]

若 $\|r\|\ge\|s\|$ 且 $\|r\|>M$，VF2 第一式投影到 $r/\|r\|$ 给 $\|a\|\ge\|r\|^3+\lambda(\|r\|-\|s\|)>M^3$，矛盾。若 $\|s\|\ge\|r\|$ 且 $\|s\|>M$，第二式投影到 $s/\|s\|$ 给 $\|b\|^5\ge\|s\|^5+\lambda(\|s\|^3-\|r\|^3)>M^5$，矛盾。

完整纤维闭且由 VF3 有界，故紧。每个有限前缀可以继续，下一个 $M$ 不增；没有先假设输出留域。$M=0$ 强迫原点驻定。

<a id="vfc-contraction"></a>
## 两个单调增量之和：短承重证明

置 $N=a-B(b)$、$q=B(r)-B(s)$、$e=r-s$。$N$ 和 $q$ 是正常误差，**不是**真实残差 $\|F\|$。VF2 给

\[
C(s)-C(b)=\lambda q,\qquad N=q+\lambda e+B(s)-B(b).
\tag{VF4}
\]

$q=0$ 时单射性依次强制 $e=0$、$s=b$、$a=B(b)$，根即输入。以下 $q\ne0$，故 $M>0$。

取精确 secant $A=\int_0^1DB(s+te)dt$，$DB(z)=\|z\|^2I+2zz^T$。非恒定段使 $A\succ0$，VF3 给 $A\preceq3M^2I$，$q=Ae$，故
$\langle e,q\rangle\ge\|q\|^2/(3M^2)$。

令 $T=B\circ C^{-1}=\|z\|^{-2/5}z$。沿 $C(b),C(s)$ 的段取 secant $D$，则 $B(s)-B(b)=\lambda Dq$。非零处

\[
DT(z)=\|z\|^{-2/5}(I-\tfrac25nn^T),\qquad
D\succeq\frac3{5M^2}I.
\tag{VF5}
\]

因为该段的范数不超过 $M^5$。穿零时权重 $|t-t_0|^{-2/5}$ 可积，线段限制绝对连续，FTC 仍成立。点乘 VF4 的 $q$ 得

\[
\langle N,q\rangle
\ge\left(1+\frac{14\lambda}{15M^2}\right)\|q\|^2,
\qquad
\boxed{\|q\|\le\rho_M\|N\|},\quad
\rho_M=\left(1+\frac{14\lambda}{15M^2}\right)^{-1}<1.
\tag{VF6}
\]

这是 $N=(I+\lambda A^{-1}+\lambda D)q$ 的 SPD **之和**，不把两个 SPD 的乘积冒称正定，也不需要扇区转角门。

<a id="vfc-length"></a>
## 物理逆模、完整轨道与极限

全域 uniform monotonicity 给

\[
\langle B(r)-B(s),r-s\rangle\ge\|r-s\|^4/4,
\quad
\langle C(s)-C(b),s-b\rangle\ge\|s-b\|^6/16.
\tag{VF7}
\]

自足证明：差向量为 $L n$，起点写 $\alpha n+w$、$w\perp n$。第一式积分 $DB$ 得 $L^2\|w\|^2+3L^2[(\alpha+L/2)^2+L^2/12]\ge L^4/4$。第二式积分 $DC$ 的径向项至少 $5L^2\int_0^1(\alpha+tL)^4dt$，在 $\alpha=-L/2$ 最小为 $L^6/16$，垂直项均非负。Cauchy 及 VF4 给

\[
\|(a,b)-(x,s)\|
\le\lambda4^{1/3}\|q\|^{1/3}+(16\lambda\|q\|)^{1/5}.
\tag{VF8}
\]

初值 $W_0=(a_0,b_0)$ 的 $M_0>0$ 时，固定 $\rho=\rho_{M_0}$，最大原则和 VF6 对全部政策给 $\|N_k\|\le\rho^k\|N_0\|$。所以

\[
\sum_{k\ge0}\|W_{k+1}-W_k\|
\le\frac{\lambda4^{1/3}\rho^{1/3}\|N_0\|^{1/3}}{1-\rho^{1/3}}
+\frac{(16\lambda)^{1/5}\rho^{1/5}\|N_0\|^{1/5}}{1-\rho^{1/5}}<\infty.
\tag{VF9}
\]

每条完整轨道 Cauchy，极限满足 $a_\infty=B(b_\infty)$，属于完整 $S$。整个 $S$ 的零输入纤维均 singleton：$N=0$ 强制 $q=0$，再用 VF4 后的单射性。极限可依根选择不同；没有通用所有轨道闭式。共同率依初始有界集，不是非紧 $S$ 上一个统一全局率。任意 $\lambda>0$、所有维数、所有初值与全部 stationary 选择均被覆盖。

<a id="vfc-comparison"></a>
## 真实失败合同与淘汰理由

原目标 $f$ 的统一 Euclidean 二次 H1 确实失败。取输出 $r=tu$、$s=(t+t^3/\lambda)u$，输入 $a=0$、$b=[s^5+\lambda(s^3-t^3)]^{1/5}u$。$b=4^{1/5}tu+O(t^3)$，真实步长平方为 $\Theta(t^2)$，而输入 $f=O(t^4)$、输出 $f\ge0$，下降商趋零。

这不妨碍 VF3–9 的短经典正面。非强凸核、非单调联合梯度、向量维数和自然二次 H1 失败都不是强优势证明。该例保留非平凡优化来源、非极小完整根和正常误差重组价值；不替换 C241 原非 calm/尾界作用，也不推荐它承担“旧理论无法分析”的主例。更换反馈或核必须重新认证所有输出；本证明不授任意正定时变度量。

解析推导承担全称结论。[Python](../code/model_selection_limits/README.md)只反算根方程、系数、逆模与有限能量样本。
