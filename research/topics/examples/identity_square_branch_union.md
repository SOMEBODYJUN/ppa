# 身份与平方分支并图：好选择无法替代完整图

<a id="is-object"></a>
## 对象、来源与量词

固定任意 \(\lambda>0\)，在 \(\mathbb R\) 上定义**完整关系**
\[
F(x)=\{x,x^2\}\quad(x\in\mathbb R),\qquad S=F^{-1}(0)=\{0\}.
\tag{I1}
\]
两值在 \(x=0,1\) 重合，其余一般不同。下文 \(\inf_{v\in F(x)}|v|\) 始终对完整纤维取下确界。完整 \(J_{\lambda F}(p)=\{u:p-u\in\lambda F(u)\}\) 是集合值关系；指定分支 \(J_1(p)=p/(1+\lambda)\) 是另一个、较弱的算法对象。局部命题的邻域可随固定 \(\lambda\) 缩小。

历史观察别名 GX-068；线索为 [9/01 ZIP](../../../history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip) 内 work/c_gx066_077.md 的 GX-068 及 research/gap_examples.md 同号卡。ZIP SHA-256 为 b40d2aae4eef13ef2df2840df1b74333793e56de112addab7eca67dfc9bdd3ba；前一成员解压字节 SHA-256 为 e67b4a09a1d2fb9fcd4c2681f831d740a12989e7a731d884944f4ef1074a7105。以下推导独立于历史卡的验收标签；外部先行性尚未核。

<a id="is-operator-eb"></a>
## IS-OP-v1：完整算子真残差的锐半阶

对每个 \(0<|x|<1\)，
\[
r_F(x):=d(0,F(x))=\min\{|x|,x^2\}=x^2,\qquad d(x,S)=|x|.
\tag{I2}
\]
因此 \(d(x,S)=r_F(x)^{1/2}\)，固定目标的 \(q=1/2\) 误差界在整个小邻域上取等，最优模为 \(1\)。任何 \(q>1/2\) 的局部幂误差界失败，因为 \(|x|/r_F(x)^q=|x|^{1-2q}\to\infty\)。特别地，线性 metric subregularity 失败。零点孤立，结论不是定义域外空纤维造成的真空成立。

完整逆纤维同时解释另一种量词。对 \(|y|<1\)，
\[
F^{-1}(y)=
\begin{cases}
\{y\},&y<0,\\
\{0\},&y=0,\\
\{y,\sqrt y,-\sqrt y\},&y>0,
\end{cases}
\quad d(0,F^{-1}(y))=|y|.
\tag{I3}
\]
最后一个等号是**最近逆点**律，线性最优模 \(1\)；它与 (I2) 的最坏输入点量词不同。若要求对充分小的 \(|y|\) 和**所有** \(x\in F^{-1}(y)\) 且 \(|x|\) 充分小的局部逆像，都有 \(|x|\leq\kappa|y|^q\)，则 \(y>0\) 的平方根支排除 \(q>1/2\)，而 \(q=1/2\) 的局部最优模为 \(1\)。所以不能以最近逆点的线性律给完整逆关系的全部局部分支贴线性 calm 标签。

<a id="is-resolvent"></a>
## IS-STEP-v1：指定近端分支与完整步残差

由 (I1) 直接求解全部输出：
\[
J_{\lambda F}(p)=
\left\{\frac{p}{1+\lambda}\right\}
\ \cup\
\begin{cases}
\left\{\dfrac{-1+\sqrt{1+4\lambda p}}{2\lambda},
\dfrac{-1-\sqrt{1+4\lambda p}}{2\lambda}\right\},
&p\geq-1/(4\lambda),\\
\varnothing,&p<-1/(4\lambda).
\end{cases}
\tag{I4}
\]
并集第一项对**所有** \(p\in\mathbb R\) 存在；第二项的空集仅表示平方分支的自然输入域。式 (I4) 在 \(p=0\) 还含远输出 \(-1/\lambda\)，所以“完整 \(J(0)\) 只有零”是错误的。另一方面，固定点集
\(\operatorname{Fix}J_{\lambda F}=\{p:p\in J_{\lambda F}(p)\}=S=\{0\}\)，因为固定点条件等价于 \(0\in F(p)\)。

指定身份分支全域满足
\[
J_1(p)=\frac{p}{1+\lambda},\qquad
|p-J_1(p)|=\frac{\lambda}{1+\lambda}|p|.
\tag{I5}
\]
故这个**指定选择**的 fixed-point EB 具有精确线性模 \((1+\lambda)/\lambda\)，并在独立选择该分支时给 \(p_k=(1+\lambda)^{-k}p_0\)。这些常数不适用于完整关系的最小步残差
\[
r_J(p):=\inf_{u\in J_{\lambda F}(p)}|p-u|.
\tag{I6}
\]
写 \(u_+(p)=(-1+\sqrt{1+4\lambda p})/(2\lambda)\)。固定 \(\lambda\) 后，足够小的 \(p\) 有 \(u_+(p)=p+O(p^2)\)；身份支残差为 \(O(|p|)\)，远根 \(u_-(p)\to-1/\lambda\) 的步残差有正下界。因此对全部充分小的非零 \(p\)，(I6) 的极小者是近平方支，且
\[
r_J(p)=\lambda u_+(p)^2=\lambda p^2(1+o(1)).
\tag{I7}
\]
于是 \(d(p,\operatorname{Fix}J_{\lambda F})=|p|\leq\kappa r_J(p)^{1/2}\) 的局部最优模恰为 \(1/\sqrt{\lambda}\)，而所有指数 \(q>1/2\) 失败。这里“最优模”是邻域收缩时允许常数的下确界；在固定邻域上不声称端点常数本身必可取。完整 \(J\) 允许远输出，不得把局部近平方选择或 (I5) 默认为它的唯一迭代律。

<a id="is-collision"></a>
## IS-RL-v1：全对反射模的零分母碰撞

在任意零邻域取 \(0<y<1\) 足够小，令
\[
x=\frac{y+\lambda y^2}{1+\lambda}.
\]
完整图上的两点 \((x,x)\)、\((y,y^2)\) 具有相同 Minty 输入
\((1+\lambda)x=y+\lambda y^2\)，但 \(x<y\)。对应 Cayley 输出的差为 \(2(x-y)\ne0\)。因此任意包含这两个局部分支的图块在零点附近都不满足有限常数的全对 Hölder–RL，不论 \(\gamma>0\) 选为何值：右端输入差的 \(\gamma\) 次幂等于零。它同时说明完整 \(J_{\lambda F}\) 在任意零输入邻域里不是单值的；各单支可单值并不修复完整图。

<a id="is-boundary"></a>
## 调用边界与待审

两个半阶模的残差不同：\(r_F(x)\) 在**原算子输出纤维**取下确界；\(r_J(p)\) 在**同一 Minty 输入的近端输出纤维**取下确界。它们的精确常数分别为 \(1\) 与 \(1/\sqrt{\lambda}\)。同一对象的指定身份选择却给线性 fixed-point EB；这是分支选择与完整关系的量词分离，不表示真实残差的半阶规律被线性化。

自审边界：平方支只在 \(p\geq-1/(4\lambda)\) 存在，然而局部碰撞和 (I7) 同时使用 \(p\to0^\pm\)，故处于其域内；远根被 (I4) 保留且在 (I7) 中单独排除；(I3) 的最近点和全部逆像量词分开；全对 RL 的反例使用同一 \(\lambda\) 与同一图块。尚未核历史例卡所列完整 semimonotonicity 区域、两变量 Hölder MR 的全部目标窗口以及外部文献优先权。这些不能由本卡自动升级。
