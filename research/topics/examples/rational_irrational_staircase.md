# 有理／无理符号阶梯的完整纤维与输入断层

**状态与范围。** C110/C111 的结论直接从完整关系重算；不承接历史
Spingarn 命名、极大性标签、先行性或同 ZIP 其它 GX 的状态。
来源线索为 [9/01 ZIP](../../../history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip)
的 `work/c_gx053_065.md` GX-056（行 312–387）；同一成员在早期
`RL_monotonicity_regularity_research_checkpoint_2026-09-01.zip` 中与之
逐字节相同，SHA-256 为
`55df53d130f510c873e2a9d4c4afec9b32eb1930811ad458348088ed452748f4`。

<a id="gx056-object"></a>
## 1. 完整对象、全部逆像与闭图边界

固定 \(0<\delta<1/2\)，在实直线上声明**完整关系**
\[
F_\delta(x)=
\begin{cases}
\{0\},&x=0,\\
\{\operatorname{sgn}(x)c(x)\},&0<|x|<\delta,\\
\varnothing,&|x|\ge\delta,
\end{cases}
\qquad
c(x)=\begin{cases}1,&x\in\mathbb Q,\\2,&x\notin\mathbb Q.\end{cases}
\tag{RS1}
\]
这里 \(\pm\delta\) 不在定义域。设
\[
A_1=\mathbb Q\cap(0,\delta),\quad
A_2=(\mathbb R\setminus\mathbb Q)\cap(0,\delta),\quad
A_{-1}=-A_1,\quad A_{-2}=-A_2.
\]
全部逆像为
\[
F_\delta^{-1}(y)=
\begin{cases}
\{0\},&y=0,\\
A_y,&y\in\{-2,-1,1,2\},\\
\varnothing,&\text{其余 }y.
\end{cases}
\tag{RS2}
\]
因此 \(S=F_\delta^{-1}(0)=\{0\}\)，值域只有五个点。
四个非零逆纤维均非闭，且分别在相应开半区间稠密；例如
正无理数 \(x\) 满足 \(F_\delta(x)=\{2\}\)，但
\(d(x,F_\delta^{-1}(1))=0\)。不能用零距离把一个缺失的图点补入关系。

由有理数与无理数的稠密性，完整图的闭包恰为
\[
\overline{\operatorname{gph}F_\delta}
=\{(0,0)\}
\cup\bigl([0,\delta]\times\{1,2\}\bigr)
\cup\bigl([-\delta,0]\times\{-1,-2\}\bigr).
\tag{RS3}
\]
原图不是闭图，在任意非零图点也不是局部闭图：任意充分小的
水平窗中，同一输出水平的正确算术类型点可收敛到错误算术类型点。
但在 \((0,0)\) 取输出窗 \((-1,1)\)，局部图仅为孤立点
\(\{(0,0)\}\)，故在参考点确实局部闭。
这不表示 \(F_\delta\) 在 \(x=0\) 连续；沿正有理数趋零，输出恒为 1。

<a id="gx056-fibers"></a>
## C110-v1：每个步长的完整近端纤维与算术区别

固定任意 \(\lambda>0\)。自然输入域和完整近端为
\[
D_\lambda=\{0\}\cup\bigcup_{u\in\{-2,-1,1,2\}}(A_u+\lambda u),
\tag{RS4}
\]
\[
J_{\lambda F_\delta}(p)
=\begin{cases}\{0\},&p=0,\\\varnothing,&p\ne0\end{cases}
\ \cup\
\{p-\lambda u:u\in\{-2,-1,1,2\},\ p-\lambda u\in A_u\}.
\tag{RS5}
\]
反射的**完整纤维**相应为
\(\{2x-p:x\in J_{\lambda F_\delta}(p)\}\)；合法水平支上的值是
\(p-2\lambda u\)。公式 (RS5) 在所有输入均适用，空纤维照实保留。

几何上，四个非零支分别位于
\[
(\lambda,\lambda+\delta),\quad(2\lambda,2\lambda+\delta),\quad
(-\lambda-\delta,-\lambda),\quad(-2\lambda-\delta,-2\lambda).
\tag{RS6}
\]
所以对**每个**步长，
\[
D_\lambda\cap(-\lambda,\lambda)=\{0\},\qquad
\sup_{p\in D_\lambda}|p|=2\lambda+\delta.
\tag{RS7}
\]
零点输入没有任何非退化球覆盖。

若 \(\lambda\ge\delta\)，同侧两个开区间不交，(RS5) 在自然域上
单值。在 \(\lambda=\delta\) 时，两个闭包虽然相接，接点
\(p=\pm2\delta\) 都不在自然域：它们需要被排除的输出坐标
\(x=\pm\delta\) 或非零水平支上的 \(x=0\)。

若 \(0<\lambda<\delta\)，正侧重叠窗是
\(O_+=(2\lambda,\lambda+\delta)\)。其中一级支存在当且仅当
\(p\in\lambda+\mathbb Q\)，二级支存在当且仅当
\(p\notin2\lambda+\mathbb Q\)。因此：

| 步长类型 | 重叠窗内的全部纤维 |
| --- | --- |
| \(\lambda\in\mathbb Q\) | \(p\in\mathbb Q\) 时只有 \(p-\lambda\)，\(p\notin\mathbb Q\) 时只有 \(p-2\lambda\)；整个 \(O_+\) 都在自然域，完整近端仍单值。 |
| \(\lambda\notin\mathbb Q\) | \(p\in\lambda+\mathbb Q\) 时有两个值 \(p-\lambda,p-2\lambda\)；\(p\in2\lambda+\mathbb Q\) 时为空；其余 \(p\) 只有 \(p-2\lambda\)。前两类互不相交且均稠密。 |

负侧重叠窗 \(O_-=(-\lambda-\delta,-2\lambda)\) 由奇对称给出：
\(J(-p)=-J(p)\)。特别是“\(\lambda\le\delta\) 均有精确碰撞”是错误陈述；
在 \(\lambda=\delta\) 或有理的 \(0<\lambda<\delta\) 上，完整近端单值。
这些单值情形仍未必有连续反射。

<a id="gx056-rl"></a>
## 3. 全图线性 RL 的锐值与全部消失模的失败门

对任意两个完整图点 \((x,u),(y,v)\)，写 \(a=x-y,b=u-v\)。
本文的全图 RL 是
\[
|a-\lambda b|\le L|a+\lambda b|^\gamma
\quad\text{对全部完整图点对成立}.
\tag{RS8}
\]
若 \(b=0\)，两个差都等于 \(a\)。若 \(b\ne0\)，置
\(t=a/b\)。跨符号点对及零点配对有 \(t\ge0\)；负值仅来自同侧
两个不同水平。所有点对满足 \(t> -\delta\)，且
\[
\inf_{b\ne0}t=-\delta.
\tag{RS9}
\]
例如取正有理数 \(x_n\uparrow\delta\) 与正无理数 \(y_n\downarrow0\)，
则 \(b=-1,a\to\delta\)，故 \(t\to-\delta\)。

当 \(\lambda>\delta\) 时，
\[
\boxed{L_{\lambda,1}^*=\frac{\lambda+\delta}{\lambda-\delta}},\qquad
\boxed{\tau_\lambda^*=\frac{\lambda\delta}{(\lambda-\delta)^2}}.
\tag{RS10}
\]
第一式证明：\(t\ge0\) 时比值
\(|t-\lambda|/(t+\lambda)\le1\)；\(-\delta<t<0\) 时该比值为
\((\lambda-t)/(\lambda+t)\)，在左端趋于 (RS10)，由 (RS9) 序列锐逼近。
第二式对应明确量词
\[
\lambda ab\ge-\tau|a+\lambda b|^2
\quad\text{对全部图点对成立},
\]
由 \(\tau=(L^2-1)/4\) 得到，同一序列证明锐性。
上述上确界都不是某个不同图点对取到的最大值。

自然输入域直径的上确界是 \(\Delta=4\lambda+2\delta\)。因此在
\(\lambda>\delta\) 时，每个 \(0<\gamma<1\) 有例如
\[
L_{\lambda,\gamma}\le
L_{\lambda,1}^*(4\lambda+2\delta)^{1-\gamma}.
\tag{RS11}
\]
这是可靠上界，未声称是最优系数。较小指数来自有界尺度继承。
即使容许 \(\gamma>1\)，同一水平支上的任意接近不同点有
\(b=0\)，比值 \(|a|^{1-\gamma}\to\infty\)，故最高全对幂指数是 1。

当 \(0<\lambda\le\delta\)，更强的否定成立：不存在有限模
\(\omega\) 满足 \(\omega(0)=0\)、\(\omega(s)\to0\) 且
\(|a-\lambda b|\le\omega(|a+\lambda b|)\) 对全图成立。

- **\(\lambda=\delta\)。** 用 (RS9) 的端点序列，
  \(|a+\lambda b|=|a-\delta|\to0\)，而
  \(|a-\lambda b|=a+\delta\to2\delta>0\)。
- **\(0<\lambda<\delta\)、有理 \(\lambda\)。** 固定有理
  \(x\in(\lambda,\delta)\)，取无理 \(y_n\to x-\lambda\) 且
  \(0<y_n<x\)，则 \(b=-1,a_n\to\lambda\)，输入差趋零而反射差趋
  \(2\lambda>0\)。虽然没有精确碰撞，仍失败。
- **\(0<\lambda<\delta\)、无理 \(\lambda\)。** 固定有理
  \(x\in(\lambda,\delta)\)，\(y=x-\lambda\) 正且无理。
  此时 \(a=\lambda,b=-1\)，输入差正好为零、反射差为
  \(2\lambda>0\)，是完整纤维的精确碰撞。

尤其在临界步长，单值反射在 \(p\to2\delta\) 的两个支极限分别是
0 和 \(-2\delta\)，不能连续延拓至这个遗漏输入。
阈值以上虽有 Lipschitz 反射，它也只定义于所声明的自然域。

### 同一图的两个可复核几何商

(RS9) 还直接给锐界 \(ab\ge-\delta b^2\)。不存在有限常数
\(h\) 使 \(ab\ge-h a^2\)：固定一个正有理数 \(x\)，取正无理
\(y_n\uparrow x\)，则 \(b=-1\)，\(ab/a^2=-1/(x-y_n)\to-\infty\)。
另外，固定零端点的明确一阶商是
\(xu/|x|=c(x)\)（\(u\in F_\delta(x),x\ne0\)），其下极限为 1；两个端点共同趋零的
\(ab/|a|\) 下极限则为 \(-1\)。同侧不同水平给下界 \(-1\)
并可取到，其他类型非负。这里不给这些公式添加尚未核的历史命名。

<a id="gx056-residual"></a>
## C111-v1：真实零残差、最小步残差与路径边界

原算子的**全纤维**真实残差为
\[
r_{F_\delta}(x)=
\begin{cases}
0,&x=0,\\
c(x),&0<|x|<\delta,\\
+\infty,&|x|\ge\delta.
\end{cases}
\qquad d(x,S)=|x|.
\tag{RS12}
\]
固定任意 \(q>0\) 和 \(0<\eta\le\delta\)。在整个输入窗
\(|x|<\eta\) 上满足
\(d(x,S)\le K r_{F_\delta}(x)^q\) 的最小系数**恰为**
\[
K_q(\eta)=\eta.
\tag{RS13}
\]
因为非零残差至少为 1，\(K=\eta\) 足够；正有理数趋于 \(\eta\)
给比值趋于 \(\eta\)，排除任何更小系数。
故每个固定 \(q>0\) 的局部系数下确界为 0，固定目标 MSR 与
strong MSR 相同（零集为单点），不存在一个有限“最高幂”。
任意非退化输入窗都不能以字面 \(K=0\) 成立。
这里没有非零点残差趋零的渐近幂律；若残差窗要求 \(r_F<\varepsilon<1\)，
活跃点仅为 \(x=0\)，须另标为残差窗口的真空陈述。

普通 MR、任意正幂的两变量 MR、strong MR 和逆 Aubin 均失败。
例如取 \(x=0\) 与 \(0<|y_n|<1,y_n\to0\)，则
\[
d(0,F_\delta^{-1}(y_n))=+\infty,
\qquad d(y_n,F_\delta(0))=|y_n|<\infty.
\tag{RS14}
\]
也不可能给全部邻近目标一个非空逆分支。
反之，逆的 calmness／isolated calmness 在 \((0,0)\) 可以取字面系数 0：
\(|y|<1\) 时，完整逆纤维若非空就只有 \(y=0\) 的 \(\{0\}\)。
这个 inclusion 不要求遗漏目标存在逆像，不能替代 MR 的覆盖量词。

### 输入步残差是另一观察

对 \(p\in D_\lambda\) 定义完整最小步残差
\(s_\lambda(p)=d(p,J_{\lambda F_\delta}(p))\)。它在非零点为
\(\lambda\) 或 \(2\lambda\)，在零点为零；
\(\operatorname{Fix}J=\{0\}\)。整个自然输入域上的线性界锐系数为
\[
\boxed{\forall p\in D_\lambda:\quad
|p|\le\left(1+\frac\delta\lambda\right)
\inf_{x\in J_{\lambda F_\delta}(p)}|p-x|}.
\tag{RS15}
\]
选择实现最小步的支 \(u\)，有
\(|p|=|p-\lambda u|+\lambda|u|\) 及
\(0<|p-\lambda u|<\delta\)，所以比值小于
\(1+\delta/\lambda\)。令正有理输出趋于 \(\delta\)，一级支总存在，
最小步等于 \(\lambda\)，比值趋于该系数。
这不是 (RS13) 的模；输入和残差都不同。
近零输入窗与自然域的交集只有零点，任何近零步界仅在此交集成立，
不给完整输入球的算法存在性。本文不作 \(0\cdot(+\infty)\) 运算。

<a id="gx056-paths"></a>
## 5. 所有合法路径的有限步终止

固定任意 \(\lambda>0\)，令合法步
\(p_{k+1}\in J_{\lambda F_\delta}(p_k)\)。非零输入的每个合法输出
保持同一符号且非零。写 \(c_k\in\{1,2\}\)，有
\[
|p_{k+1}|=|p_k|-\lambda c_k\le|p_k|-\lambda.
\tag{RS16}
\]
经过 \(n\) 个合法步仍有 \(0<|p_n|\le|p_0|-n\lambda\)，故
\(n<|p_0|/\lambda\)。每个非零初值的每条最大合法路径都在有限步后
遇到空近端纤维；它们不能无限合法，也不可能命中零点。
从零出发则唯一地恒为零。

若 \(\lambda\ge\delta\)，结论更精确：任何非零
\(p_0\in D_\lambda\) 只有一个合法输出，且
\(0<|p_1|<\delta\le\lambda\)，由 (RS7) 得
\(p_1\notin D_\lambda\)。因此恰有第一步，没有第二步。
在 \(\lambda=1\)，全图 Lipschitz RL、真实零目标任意幂 EB、零点局部闭图
同时成立，仍不能推出非零初值的无限 PPA 路径。

<a id="gx056-correspondence"></a>
## 6. 与规范绝对值次梯度例的关系及审查边界

现有 [绝对值次梯度卡](absolute_value_subgradient.md#av-object)
（C78/C79，历史 GX-077）也有原算子残差跳跃和固定零目标模下确界 0。
两对象的完整图及覆盖结论不同：

| 坐标 | 本关系 \(F_\delta\) | 规范 \(\partial|\cdot|\) |
| --- | --- | --- |
| 零点纤维 | \(\{0\}\) | \([-1,1]\) |
| 原零残差在非零近点 | 1 或 2 | 1 |
| 固定零目标局部线性模下确界 | 0 | 0 |
| 邻近非零目标完整逆像 | 空 | \(|y|<1\) 时为 \(\{0\}\) |
| MR／strong MR | 失败 | 局部成立，模下确界 0 |
| 近零 Minty 输入 | 自然域仅含零点 | 完整输入球中每点均有近端 |
| 近零步残差 EB | 自然域交集上真空 | 非零近点实际锐系数 1 |
| 全图线性 RL | 恰当 \(\lambda>\delta\)，锐值 (RS10) | 每个 \(\lambda>0\)，锐值 1 |
| 图闭性 | 全图非闭，零图点孤立局部闭 | 完整图闭 |

故本卡精化一个已有残差跳跃机制，不能因固定目标模同为 0 而把
MR、步残差、近端覆盖或轨道性质当成重复结论。
从 \(\lambda>\delta\) 的 Lipschitz Cayley 映射到自然域闭包的唯一连续延拓
与 [C58 的闭包桥](../../canonical/closed_graph_minty_domain.md#cg-closure)
相容；临界步长两支不兼容极限说明其消失模前提不能省。

**已关闭的对象与量词异议：** 全部空纤维明确；端点未擅自加入；
步长以下的单值和碰撞分开；在零点的图窗与仅限制输入的窗分开；
原算子残差与完整最小步残差分开；锐上确界、缩窗下确界与字面零系数分开。
**未处理的独立工作：** 次线性 RL 最优系数、完整二参数区域、
历史 Spingarn 名称和外部先行性。本卡没有替这些问题宣布验收。

<a id="gx056-source"></a>
## 7. 精确来源定位与原审计用语

主来源：

`history/sources/次单调论文研究/RL_monotonicity_regularity_research_checkpoint_2026-09-01.zip!/work/c_gx053_065.md`

GX-056 位于成员 **312–387 行**；成员 SHA256
`55df53d130f510c873e2a9d4c4afec9b32eb1930811ad458348088ed452748f4`。
该成员给对象、逆纤维线索、锐线性 RL／LT、固定目标残差跳跃和零点局部闭图。
(RS5) 的全部算术纤维、阈值以下的单值区别、每种步长的消失模反例、
(RS13)/(RS15) 的固定窗口锐系数与 (RS16) 的每选择有限终止为本草案直接补算。

同 ZIP `research/gap_examples.md` 的 GX-056 为 **588–596 行**；
`work/c_consistency_audit.md` 的 CCA-M08 为 **175–194 行**。
CCA-M08 把旧 `C-DISAGREE-056` 分成两项：旧 B 值
\((1+2\delta)/(1-2\delta)\) 原本明确是安全界，替换为锐值应标
`C-SHARPEN`；零点局部闭图属于范围修正 `C-DISAGREE-SCOPE`。
本草案确认这些数学区别，不把较松上界报告为原稿的虚假锐性声明。

作者版本的定义与本对象的非闭门另见[Spingarn逐对象匹配](../../canonical/spingarn_author_definitions.md#sp-gx-match)；不把打印商满足与原作者闭关系类成员身份混同。
