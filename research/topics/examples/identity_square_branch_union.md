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

<a id="is-mr"></a>
## IS-MR-v1：完整逆纤维的两变量半阶正则（C92）

对任意固定 \(0<\delta\le 1/3\) 和**全部** \(|x|,|y|<\delta\)，完整关系 (I1) 满足
\[
d(x,F^{-1}(y))\le d(y,F(x))^{1/2}
=\min\{|y-x|,|y-x^2|\}^{1/2}.
\tag{I8}
\]
这里两边分别取完整逆纤维与完整输出纤维，不是选定的身份分支。证明须同时对两个残差成立。身份支给 \(d(x,F^{-1}(y))\le|x-y|\le\sqrt{|x-y|}\)，因为 \(|x-y|<2\delta<1\)。若 \(y\ge0\)，平方支给 \(\pm\sqrt y\in F^{-1}(y)\)，因而
\(d(x,F^{-1}(y))\le||x|-\sqrt y|\le\sqrt{|x^2-y|}\)。若 \(y=-a<0\)，完整逆像仅为 \(\{-a\}\)，且 \(2|x|+a<3\delta\le1\)，所以
\[
d(x,F^{-1}(y))^2=|x+a|^2
\le x^2+a(2|x|+a)\le x^2+a=|x^2-y|.
\]
这同时证明包括正、负目标的共同窗口，而非仅固定目标零点的 (I2)。

在每个该窗口，取 \(y=0\)、\(0<|x|<\delta\) 得 \(d(x,F^{-1}(0))=|x|=d(0,F(x))^{1/2}\)；故半阶系数 1 取等，所有更高正指数的有限局部系数均失败。对较低指数 \(0<q<1/2\)，缩窗可用系数 \((2\delta)^{1/2-q}\)，其下确界为零。对**系数恰为 1 的对称开方窗**，半径 \(1/3\) 最大：若 \(\delta>1/3\)，取 \(1/3<t<\min\{\delta,1\}\)、\(x=t,y=-t\)，便有 \(d(x,F^{-1}(y))^2=4t^2>t+t^2=d(y,F(x))\)。此最大窗观察是本库的新推导，不冒称旧审计原文。

等价的局部逆 Hölder–Aubin 形式须写出成员量词：\(|u|,|v|<\delta\)，\(z\in F^{-1}(u)\cap(-\delta,\delta)\) 时，以 (I8) 的 \((x,y)=(z,v)\) 得
\(d(z,F^{-1}(v))\le|u-v|^{1/2}\)，锐系数亦为 1（取 \(u=t^2,v=0,z=t\)）。这不提供单值局部化：每个充分小的正目标都有 \(y,\pm\sqrt y\) 三个趋零逆点；身份选择 \(y\mapsto y\) 虽然连续，也不代表完整逆关系单值。与 (I3) 的最近逆点线性界、(I2) 的固定目标半阶、(I7) 的近端步残差及全对 RL 碰撞均是不同量词。

来源为同一 ZIP 的 `work/c_consistency_audit.md` §CCA-M14（成员 SHA-256 `44942cb65a7ae675d669fda4de90757630130be3987f6f5eef26d8cf6594290f`）。旧审计的局部半阶观察在此独立证明；同图 semimonotonicity 区域另见下节 C95，外部先行性仍未裁决。

<a id="is-semimono"></a>
## IS-SEMIMONO-v1：完整并图的精确二参数区域（C95）

对任意实数 \(\mu,\rho\)，考虑完整图或原点处同时含两支的任意充分小**共同图点窗**上的全对条件
\[
\langle a,b\rangle\ge\mu|a|^2+\rho|b|^2,
\qquad a=x-x',\quad b=v-v',\quad (x,v),(x',v')\in\operatorname{gph}F.
\tag{I9}
\]
其精确参数区域在完整图与该局部 germ **相同**：
\[
\Sigma(F)=\{(\mu,\rho):\mu<0,\ \rho<0,\ \mu\rho\ge1/4\}.
\tag{I10}
\]
这是允许负参数的图不等式区域，不表示原图有非负次单调常数或全对 RL。

先证所有有限斜率都可在趋零的**跨支图点对**实现。给定 \(t\ne1\)，取非零 \(y\to0\)，令身份支输入 \(x=(y^2-ty)/(1-t)\)；则 \(x,y\to0\)、\(a=x-y\ne0\)，而 \(b=x-y^2=t a\)。斜率 \(t=1\) 由身份支的两个不同图点实现。因此 (I9) 对完整图或任何含两支的共同原点窗成立，当且仅当
\[
t-\mu-\rho t^2\ge0\quad\text{对每个 }t\in\mathbb R;
\tag{I11}
\]
同输入不同支的 \(a=0,b\ne0\) 还要求 \(\rho\le0\)，这已由 (I11) 蕴含。二次多项式全域非负强制 \(\rho<0\)；其最小值在 \(t=1/(2\rho)\)，条件 \(1/(4\rho)-\mu\ge0\) 等价于 \(\mu\rho\ge1/4\)，并给 \(\mu<0\)。反向对任意图点，若 \(a\ne0\) 以 \(t=b/a\) 代 (I11)，\(a=0\) 用 \(\rho<0\) 即得 (I9)。这也逐坐标证明没有有限的单独 hypomonotonicity 或 cohypomonotonicity 下界：跨支斜率 \(t\to-\infty\) 使 \(ab/a^2=t\to-\infty\)，\(t\to0^-\) 使 \(ab/b^2=1/t\to-\infty\)。

这一区域与 [C89 的平移 Cayley 球](../../canonical/non_tied_cayley.md#nt-quadratic) 的门有精确**不相交**关系：对每个 \(\lambda>0\)，令 \(A=1+\lambda\mu+\rho/\lambda\)、\(\Delta=1-4\mu\rho\)，则 (I10) 和 AM–GM 给 \(A\le1-2\sqrt{\mu\rho}\le0\)、\(\Delta\le0\)。等号 \(A=0\) 仅在 \(\mu\rho=1/4,\lambda=\sqrt{\rho/\mu}\) 出现。故没有一个认证 (I10) 的参数对能满足 C89/C91 的 \(A>0,\Delta\ge0\) 联合门，不能用二参数不等式为本完整并图补出 Minty 单值性。直接地，斜率 \(t=-1/\lambda\) 的局部跨支图点对有 \(a+\lambda b=0\)、\(a-\lambda b=2a\ne0\)。此处是**同图、全部图点**的门冲突，并非声称 C89 对任意负参数图都失败；本图还有 (I8) 的两变量半阶 MR 与同输入跨支碰撞。

来源为同一 ZIP `work/c_gx066_077.md` 的 GX-068 semimonotonicity 区域，以上实现全部实斜率与 C89 门对照由本库逐式重算。只关闭这一完整区域单元；历史 VI 分类及外部先行性另审。

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

自审边界：平方支只在 \(p\geq-1/(4\lambda)\) 存在，然而局部碰撞和 (I7) 同时使用 \(p\to0^\pm\)，故处于其域内；远根被 (I4) 保留且在 (I7) 中单独排除；(I3) 的最近点和全部逆像量词分开；全对 RL 的反例使用同一 \(\lambda\) 与同一图块。C92 的两变量半阶只在明示的共同窗口使用完整逆纤维；C95 的全对二参数区域包含全部跨支斜率且不能调用 C89 的正 \(A\) 门。历史 VI 分类及外部文献优先权尚未核。
