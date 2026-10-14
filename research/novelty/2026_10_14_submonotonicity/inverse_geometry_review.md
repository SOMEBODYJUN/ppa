# 逆图侧非线性化：精确桥、参数优势及失败边界

日期：2026-10-14。范围：独立研究审查，不改主稿、总账、图；以下“推导”不声明外部新颖性。所用仓库契约为 `research/NOTATION_CONTRACT.md`、`research/foundations.md` 与 `research/canonical/true_residual_selection_rleb.md`。读取了本地 academic-writing-skills 的 mathematics、mathematical-exposition、execution-and-acceptance 指南。

结论：逆图耗散是有实质不同能力的入口。它能保留近端步的方向信息，能通过固定二次 shift 恢复经典 Minty 覆盖，并能以高阶正余项恢复普通 PPA 在 averaged 临界参数上的点收敛。但把负二次项简单换为低阶幂并不会自动得到更好的理论；它可能连完整近端纤维单值都不保证。RL 一般模与逆图一般模分别控制不同变量，不能互相更名。下文给出同一完整 F、同一 lambda、真 residual 下的严格参数比较及两个方向的具体反例。

## 1. 一手来源与实际读取范围

| 来源及版本 | 本轮实际读取位置 | 可用事实及限制 |
| --- | --- | --- |
| Combettes–Pennanen, *Proximal Methods for Cohypomonotone Operators*, SIAM J. Control Optim. 43(2), 731–742 (2004), DOI [10.1137/S0363012903427336](https://epubs.siam.org/doi/10.1137/S0363012903427336)；实际全文是[作者 sicon3.pdf](https://pcombet.math.ncsu.edu/sicon3.pdf)，12页，首页含 to appear 与出版日期占位符 | 作者印页3–5 Definitions 2.1–2.2、Lemmas 2.3–2.4；印页5–9 Theorem 3.1及完整证明；印页9–11 Algorithm 4.1、Theorem 4.3及证明 | 局部 maximal cohypomonotonicity 经固定 shift 转为 maximal monotonicity；Theorem 3.1限定球内选取、参数余量、初值及误差预算。Theorem 4.3由强二阶充分条件和梯度线性无关认证非凸NLP的逆局部Lipschitz。作者版不是本轮核过逐字一致的刊本。 |
| Heinz H. Bauschke–Walaa M. Moursi–Xianfu Wang, *Generalized monotone operators and their averaged resolvents*, [arXiv:1902.09827v1](https://arxiv.org/pdf/1902.09827v1)，2019-02-26提交、PDF首页2019-02-22，23页；刊本元数据 [10.1007/s10107-020-01500-6](https://link.springer.com/article/10.1007/s10107-020-01500-6)，2020-04-25 online、Math. Program. 189, 55–74 (2021) | v1印页4–8 Definition 2.3、Lemmas 2.5–2.7、Propositions 2.9–2.15、Theorem 2.16；印页11–12 Proposition 3.13、Corollaries 3.14–3.15 | 将有符号 rho-comonotonicity 与 resolvent 单值、完整域、conically nonexpansive/averaged精确对应。本报告公式独立重推，不混用刊本编号。v1 Proposition 3.13(vi)文字写“rho-monotone”；本报告不调用该行，用Lem2.7、Thm2.16、Prop3.13(v)、Cor3.14。 |
| Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, [MOR正式PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)，2025-11-21 Articles in Advance，13页 | 印页4 Definition 2、Proposition 3；印页10 Assumption 2(d)(ii)、Theorem 2；印页1引言 | Definition2是输入剪切变量的二次缺陷。下面只比较其显示兼容门，不把失败解释为排除一切LT相关算法。 |
| Gárciga Otero–Iusem, *Proximal methods in reflexive Banach spaces without monotonicity*, JMAA330(1), 433–450 (2007)，[DOI10.1016/j.jmaa.2006.07.076](https://www.sciencedirect.com/science/article/pii/S0022247X06008006) | 仅找到出版社元数据与摘要；全文访问403，作者/预印本检索未取得该篇 | **未核全文。** 只作为“相对于regularizing function的Banach非线性化”检索线索；不写其定义、算法或定理包含，不据摘要认定它覆盖本报告的固定Euclidean完整PPA。 |

本轮临时取证副本及SHA256（最终报告以公开URL与确切版本定位为依据，不要求提交外文全文）：

- `sources/cp_sicon3_author.pdf`：`f8a3cdf805cf50300d8670e79b4b7767b683bd8347600511144b41968ed342ff`。
- `sources/bmw_1902_09827v1.pdf`：`743e9921ba75c7eb0354c00a81637737cf1cc1f08dce232473056549fe957e1b`。
- 对应 `.txt` 是 `pdftotext -layout` 的检索副本，不作为版本替代。LT由网页PDF解析实际读取，本轮未在此子任务存本地副本。

## 2. 固定对象与逆模的反射坐标

固定实Hilbert空间 H、完整关系 F、lambda>0；需要强点收敛的自足命题另限 H=R^n。令 S=F^{-1}(0) 非空闭，真残差始终为 r_F(u)=inf_{w in F(u)}||w||。任意两个完整图点 (u,w),(v,z)，写

\[
a=u-v,\quad b=\lambda(w-z),\quad p=a+b,\quad c=a-b.
\]

输入型RL一般模是

\[
\|c\|\le\omega(\|p\|),\qquad\omega(0)=0.\tag{I1}
\]

逆图型候选则是

\[
\langle a,b\rangle\ge-\phi(\|b\|),\qquad\phi(0)=0.\tag{I2}
\]

若原物理坐标条件为 <a,w-z> >= -eta(||w-z||)，则 **phi_lambda(t)=lambda eta(t/lambda)**，换步长不可沿用旧phi。恒等式给出

\[
\|c\|^2\le\|p\|^2+4\phi\!\left(\frac{\|p-c\|}{2}\right).\tag{I3}
\]

这是关于未知c的隐式估计。I1则直接约束||c||关于已知||p||；二者的模作用在不同变量。

由I2还得到

\[
\langle p,b\rangle\ge\|b\|^2-\phi(\|b\|).\tag{I4}
\]

若 m(t)=t-phi(t)/t 在有关值对窗上正且严格递增，则 ||p||>=m(||b||)，故

\[
\|b\|\le m^{-1}(\|p\|),\qquad
\|c\|\le\|p\|+2m^{-1}(\|p\|).\tag{I5}
\]

零输入须另处理：p=0时，I2强制 t²<=phi(t)。因此 **phi(t)<t²于全部可能的非零同输入值差** 是完整纤维单值的充分门。作为仅凭I2推出单值的统一门，这个严格条件不可删除：只要某t>0有phi(t)>=t²，取a=-b、||b||=t的两个图点便符合条件而共输入。若只核局部图块，这只排除图块内碰撞，不排除完整图远支。

例如 phi(t)=t²-c t^{q+1}、q>1、c>0，在非负且非减的小值差窗上，I5给Hölder型模 d+2(d/c)^{1/q}。这是“shift后的逆图有高阶正余量”的信息，与“负缺陷改为t^q”并非一回事；它仍需完整coverage及收敛输入。

## 3. 二次逆模：单值、覆盖、松弛与收敛门必须分开

CP使用rho>=0；BMW使用有符号参数beta，二者关系beta=-rho。完整rho-cohypomonotonicity是

\[
\langle u-v,w-z\rangle\ge-\rho\|w-z\|^2.
\tag{I6}
\]

设 B=F^{-1}+rho Id。I6等价于B单调，完整的“maximal rho-cohypo”等价于B极大单调（BMW Lem2.7的显式图剪切）。由图点 u in F^{-1}(w)有

\[
x=u+\lambda w\in B(w)+(\lambda-\rho)w.\tag{I7}
\]

当lambda>rho，B的极大单调性和正系数Minty定理给所有x的唯一w，进而唯一完整u=x-lambda w。因此：

| 任务 | 参数/条件 |
| --- | --- |
| 排除完整同输入碰撞 | lambda>rho及全图I6；不用最大性 |
| 覆盖全部H | 上项加B极大单调；由I7证明 |
| 标量反射RL | 上项令kappa=rho/lambda<1，则L=(1+kappa)/(1-kappa)=(lambda+rho)/(lambda-rho) |
| J非扩张 | lambda>=2rho及I6，已有覆盖时为全域映射 |
| J averaged及普通PPA标准弱收敛 | lambda>2rho、B极大单调、S非空；averaged参数alpha=1/[2(1-rho/lambda)]；有限维得到强收敛 |
| 松弛PPA x^+=x+theta(Jx-x) | lambda>rho、0<theta<2(1-rho/lambda)及覆盖/局部留域等条件 |

反射RL界推导：I3与phi(t)=kappa t²给s²<=d²+kappa(d+s)²，解二次式得s<=(1+kappa)d/(1-kappa)。该界在F=-(1/rho)Id、lambda>rho取等。

方向信息则给更直接的恒等式。对零点s与真实近端输出u，b=x-u=lambda w，

\[
\|u-s\|^2+(1-2\rho/\lambda)\|x-u\|^2
\le\|x-s\|^2.\tag{I8}
\]

松弛时直接展开得到

\[
\|x+\theta(u-x)-s\|^2
\le\|x-s\|^2-\theta[2(1-\rho/\lambda)-\theta]\|x-u\|^2.
\tag{I9}
\]

它保留步项的系数，I1的纯范数摘要可能丢掉这个方向信息。若lambda>2rho且同窗真EB d(u,S)<=K r_F(u)，真实包含仅给r_F(u)<=||x-u||/lambda，I8遂给

\[
d(u,S)\le q_{\rm inv}d(x,S),\qquad
q_{\rm inv}=\frac{K}{\sqrt{K^2+\lambda(\lambda-2\rho)}}<1.\tag{I10}
\]

该推导要对全部完整输出及使用的零锚成立；EB的残差阈值、coverage、有限前缀留域仍须共窗。I10不能把选中w范数当真residual。全域假设下这些局部门自动满足。

**最大性的作用不是装饰。** 只核I6的受限关系F(u)=u、domF={0}，自然输入域只有{0}；不能由几何推出邻域coverage。lambda=rho边界即使B极大单调也不够：令lambda=rho=1、F^{-1}(w)=e^w-w，则B=e^w全域连续单调且极大单调，而自然近端输入x=e^w只能覆盖(0,infinity)。S={1}，仍不能声称全H coverage。lambda=rho还可能碰撞，例如F=-Id、lambda=1，J(0)=H。

## 4. CP局部定理不能升级为任意完整纤维定理

CP Def2.2的局部最大性要求存在**在指定逆图窗上恰好相等**的极大shift扩展，强于孤立写下局部成对不等式。其Theorem3.1使用逆坐标V×X_i：V含0，S_i=X_i∩zerA_i闭且有统一邻管余量，gamma_n-rho_i有正下界，theta_n/(1-rho_i/gamma_n)属于[epsilon,2-epsilon]；另有近初值、小可和双误差预算及**近端输出选在构造球B内**。证明先把原关系与扩展的B×B近端图等同，再用Lemma2.4转单调resolvent。它并未排除B外全部原生远输出。

此处有实质完整纤维反例。lambda=1，取完整F的图为

\[
\{(u,u):u\in\mathbb R\}\ \cup\ \{(10,p-10):|p|\le1\}.
\tag{I11}
\]

这是全域coverage的闭图关系，S={0}。在状态窗X=(-1,1)、值窗V=(-1,1)，它与全域Id的图相同，因而局部maximal cohypo rho=0认证不变；小输入x的球内输出x/2存在唯一。但完整J_F(x)还含10。对x=0，完整选择能从解跳出认证窗。CP球内选择结论没有失败，失败的是把它读成完整J全部输出结论。要与当前目标比较，必须证明远支排除或对全部完整输出直接验证。

CP Theorem4.3是自然模型正面认证，而非凭定义改写：非凸NLP的强二阶充分条件与相应活跃梯度独立，经所引强正则性事实给KKT关系的逆局部Lipschitz；Lemma2.3给局部最大cohypo；再带大步长、误差及球内输出条件接Theorem3.1。这条原模型入口有独立价值，但这里不重新认证其所引NLP强正则性外部定理，也不解除远支门。

## 5. 真正的参数优势：保留逆步方向优于单个L/K摘要

取同一完整原关系、全域参数

\[
F=\operatorname{diag}(-1,0.01):\mathbb R^2\to\mathbb R^2,
\qquad\lambda=3,\qquad S=\{0\}.
\tag{I12}
\]

全部对象可直接反算：

\[
J_{3F}=\operatorname{diag}(-1/2,100/103),\quad
C=2J-I=\operatorname{diag}(-2,97/103).
\tag{I13}
\]

完整coverage、图闭、同窗retention皆全域。cohypo锐rho=1：第一坐标给等号，第二坐标正；F^{-1}+Id=diag(0,101)极大单调。真r_F(u)=sqrt(u_1²+10^{-4}u_2²)，所以锐线性EB为K=100。全对反射RL锐L=2，不能通过缩小零点邻域改小；LT对lambda F的锐tau=(L²-1)/4=3/4。

| 固定lambda=3的证书 | 精确数值/结果 |
| --- | --- |
| 完整PPA实际operator收缩 | ||J||=100/103<1 |
| 逆图I8/averaged | lambda>2rho，即3>2；I10给q_inv=100/sqrt(10003)<1 |
| 当前RL+真EB直接兼容 | K(1+L)/(2lambda)=50，失败 |
| 仓库RL+EB能量证书 | q_E=(1+L²)/(2[1+(lambda/K)²])=25000/10009>1，失败 |
| LT正式Assumption2(d)的显示兼容门 | tau(1+K/lambda)²=10609/12≈884.0833，远大于1/2 |

继续同一F、任意lambda>1，锐L=(lambda+1)/(lambda-1)、K=100，得到不同的**充分证书门**：逆图为lambda>2，直接RL兼容为lambda>101，RL能量为lambda(lambda-1)²>20000（阈值27.8149026946），LT显示兼容为lambda(lambda-1)²>2(lambda+100)²（阈值33.5960216205）。实际完整PPA锐收敛阈值也是lambda>2：负坐标在lambda=2形成两周期、1<lambda<2放大；正坐标对任意lambda>0缩小。

这个严格优势不是“逆图条件更弱”的证明：有限rho-cohypo在lambda>rho蕴含线性RL；这里逆图是在**保留更强方向信息后给较好证书**。单个最坏L来自负方向、最坏K来自弱正方向，合并为纯标量丢失了关联。增加矩阵/方向条件或使用具体J的收缩亦可修复RL分析，不能据此排除整个RL家族。

## 6. 非线性逆模可以恢复临界端点，但结论不同

固定lambda=1，令完整

\[
B(w)=w^3-\tfrac12 w,\qquad F=B^{-1}.\tag{I14}
\]

F是真多值闭关系、domF=R、S={0}。完整近端输入

\[
x=B(w)+w=w^3+\tfrac12w\tag{I15}
\]

严格递增且满射，所以完整J在R上唯一；u=J(x)=w^3-w/2。rho=1/2是cohypo锐值，因为w趋0的差商趋-1/2；B+(1/2)Id=w³极大单调。因此lambda=2rho恰在非扩张边界，任何更小常数rho都不可认证。

对任意w,z，令t=|w-z|。恒等式

\[
(w-z)(w^3-z^3)-\tfrac14(w-z)^4
=\tfrac34(w-z)^2(w+z)^2\ge0
\tag{I16}
\]

给

\[
\langle\Delta u,\Delta w\rangle
\ge-\tfrac12t^2+\tfrac14t^4
\ge-\phi(t),\qquad\phi(t)=\frac{t^2}{2+t^2}<\tfrac12t^2\quad(t>0).
\tag{I17}
\]

第二个差正好为t^6/[4(2+t²)]。phi非负、非减、连续且零消失，但phi(t)/t²趋1/2，因此不能换成某固定kappa<1/2。

零锚能量给

\[
|J(x)|^2\le|x|^2-h(|x-J(x)|),
\quad h(t)=t^2-2\phi(t)=\frac{t^4}{2+t^2}>0.
\tag{I18}
\]

任意完整PPA从任何x0开始，|x_k|非增、sum h(|x_k-x_{k+1}|)<infinity；h在有界正尺度上有正下界，故步趋0。有界序列存在聚点，近端图闭且所选图值等于步趋0，所以聚点属于S={0}，整个序列趋0。此证明使用完整coverage/全部输出/图闭，**不用EB、Dini或统一线性收缩**。

该正面不能冒称有限长度。小非零初值给交替符号，反解I15得w=2x-16x³+O(x^5)，从而

\[
T(x)=J(x)=-x+16x^3+O(x^5).
\tag{I19}
\]

取a_k=|x_k|，则a_{k+1}=a_k-16a_k³+O(a_k^5)，故a_{k+1}^{-2}-a_k^{-2}趋32，a_k~(32k)^{-1/2}。交替号给步长a_k+a_{k+1}，其和发散。因此它是**完整普通PPA点收敛但无限长度**的严格例子。它改善lambda=2rho处的标准固定averaged充分门，说明非线性逆耗散有可检验内容；不声明这是外部未见的新结果，也不说它满足当前RL一般模有限长度定理。

更一般的自足有限维命题是：完整coverage、S非空闭、F图闭，且对每个完整近端输出与零锚有I2；若h(t)=t²-2phi(t)在t>0处正且下半连续，则Fejér留在初值到某零点的闭球，sum h(step)<infinity、步趋0、聚点在S；对某聚点用Fejér单调性，得到整个轨道强收敛。局部版本必须先把此闭球全部输入、全部完整输出、值尺度与图闭放在认证共窗，不能先假定轨道已留域。

## 7. 简单低阶逆模会允许完整纤维碰撞

设phi(t)=C t^q，0<q<2、C>0。由于phi(t)/t²趋infinity，这不是I1那种“在零输入自动排除碰撞”的模。如下反例同时具有完整coverage和完整闭S。

取lambda=1、epsilon=0.1，完整F=B_epsilon^{-1}，

\[
B_\epsilon(w)=w^3-(1+\epsilon^2)w,
\qquad x=B_\epsilon(w)+w=w^3-\epsilon^2w.\tag{I20}
\]

输入三次函数满射，完整J覆盖R；S={0}，图闭。对任意两图点，

\[
\langle\Delta u,\Delta w\rangle\ge-(1+\epsilon^2)|\Delta w|^2.
\]

在值对差窗t=|Delta w|<=1/2，1.01t²<=t^{3/2}，所以完整图满足q=3/2、C=1的逆模I2。但x=0的三个w为0、+/-epsilon，相应u=-w；故

\[
J_F(0)=\{0,-0.1,0.1\}.\tag{I21}
\]

这些碰撞输出与图值都可通过减小epsilon任意接近0。真residual在u近0由最小绝对值逆根决定，线性EB可成立，但既不排除碰撞也不使零输入全部驻定。任意含三支的全对零消失RL均被I21直接否定。

低阶“负逆缺陷”一般不能提供最大shift：sup phi(t)/t²=infinity，无法从该证书推出任何有限rho的B=F^{-1}+rho Id单调；更不能免费调用经典Minty。一个关系实际可能有更强证书，这里说的是该显示模本身的保证。

## 8. RL有完整非Lipschitz收敛模型，有限cohypo不能覆盖

任取0<gamma<1，固定lambda=1，定义完整单值原F

\[
F(u_1,u_2)=(-2^\gamma|u_2|^\gamma,u_2).\tag{I22}
\]

完整近端T(x_1,x_2)=(x_1+|x_2|^gamma,x_2/2)，全域唯一；C(x)=(x_1+2|x_2|^gamma,0)，S=R×{0}完整且闭。对任意||x-y||<=R，

\[
\|C(x)-C(y)\|\le(R^{1-\gamma}+2)\|x-y\|^\gamma.
\tag{I23}
\]

真r_F(u)>=2^gamma|u_2|^gamma，故d(u,S)<=r_F(u)^{1/gamma}/2。实际轨道x_{2,k}=2^{-k}x_{2,0}，切向增量|x_{2,k}|^gamma可和，所以完整PPA有限长度收敛至S。

然而在完整图中取u_t=(t^{gamma/2},t)、v=0。于是

\[
-\frac{\langle u_t,F(u_t)\rangle}{\|F(u_t)\|^2}
=\frac{2^\gamma t^{3\gamma/2}-t^2}{2^{2\gamma}t^{2\gamma}+t^2}
\sim2^{-\gamma}t^{-\gamma/2}\longrightarrow\infty.\tag{I24}
\]

两图点和图值均趋零，故任何有限局部rho-cohypo都失败。它证明rho-cohypo不能支配真正HölderRL的完整非Lipschitz机制。不能据此排除所有任意逆模，因为某弱逆模可能包含I22；但若该模宽到允许I20碰撞，它还需要额外单值/coverage/耗散门。

## 9. 审查范围、计算与研究判断

可复现代码为 `research/code/submonotonicity_routes/inverse_verify.py`，命令 `python3 research/code/submonotonicity_routes/inverse_verify.py`。Python3.12.14，标准库；有理数计算I12精确常数、200组seed20261014的I16代数身份；二分100次计算指定参数边界；浮点复算10^5步I14轨道。末次k=10^5时k|x_k|²≈0.0312490109292趋1/32、长度前缀≈222.357665。I24指定点列所需rho递增。数值不证明全称；I1–I24的全称与渐近结论由显示证明承担。

读者与证据检查：定义先于反射恒等式，单值/coverage/收敛门分开，严格优势由同F同lambda同真residual实例承担；I14先证明完整身份再证明收敛，随后给无限长度限制；I20/I22分别攻击逆模碰撞与有限co局限。源文版本、定位与未读Banach全文限制已明确。未做刊本全文逐字对照、未证明2007Banach框架的普通EuclideanPPA包含、未认证任何结论全球新颖性；主稿/图/总账在本任务外。

因此，逆图二次shift路线更利于既有原模型认证、完整全域Minty存在性及保留步方向；逆图高阶正余项能改善临界参数上的点收敛。输入RL一般模更直接保障所认证完整纤维的零输入一致性、组织非Lipschitz反射几何与有限长度。若目标固定为完整普通PPA有限长度，不能因“逆图更接近原算子”就宣称它更本质；若目标包括无EB的渐近点收敛、临界参数或原生KKT认证，则它有已证明的独立优势。把两者做成可选择的验证入口，比将所有非线性化收编为RL更准确。
