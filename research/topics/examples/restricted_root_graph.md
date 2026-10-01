# 负平方根的受限图和完整母图：同名对象的 resolvent 不同

<a id="sr-object"></a>
## 两个对象与来源身份

半直线母关系 \(F_\infty(x)=\{-\sqrt x\}\) 当 \(x\ge0\)，其余
\(F_\infty(x)=\varnothing\)。它的**受限图**定义为
\[
\Gamma=\{(t^2,-t):0\le t\le1/4\},\qquad
F_U(x)=\{-\sqrt x\}\ (0\le x\le1/16),
\tag{SR1}
\]
且在其他 \(x\) 处 \(F_U(x)=\varnothing\)。于是
\(\operatorname{gph}F_U=\Gamma\)，但 \(F_U\ne F_\infty\)。下文
\(J_{F_U}\) 与 \(J_{F_\infty}\) 均为各自**完整**单位步长
resolvent；不能将前者在受限自然输入域上的公式称作母图的
完整 resolvent。

来源：9/01 ZIP `research/gap_examples.md` 的 GX-032 最先写母图，
随后将图限制到 \(U=[0,1/16]\)；同包
`work/c_gx027_039.md` 的 GX-032 对这个受限图算常数。精确成员
见[逐源去向](../../audit/UNIT_DISPOSITIONS.tsv)。下文重新计算
两个完整关系的图和路径；旧稿的 LT 命名/外部定理调用与优先性
仍是独立待审材料。

<a id="sr-geometry"></a>
## C85-v1：受限图的锐成对几何

任取 \(s\ne t\in[0,1/4]\)，设 \(c=s+t\in(0,1/2)\)，并令图差
\(a=t^2-s^2=(t-s)c\)、\(b=-t+s=-(t-s)\)，单位步长
Minty 差 \(d=a+b=(t-s)(c-1)\)、Cayley 差
\(r=a-b=(t-s)(c+1)\)。所以
\[
\frac{-ab}{d^2}=\frac{c}{(1-c)^2},\quad
\frac{|r|}{|d|}=\frac{1+c}{1-c},\quad
\frac{-ab}{b^2}=c,\quad
\frac{-ab}{a^2}=\frac1c.                              \tag{SR2}
\]
前三个比值随 \(c\) 增大，取 \(s,t\to1/4\) 的不同点趋于
\(c=1/2\)。因此对**整个** \(\Gamma\) 的最小有效常数是
\[
ab\ge-2d^2,\qquad |r|\le3|d|,\qquad
ab\ge-\tfrac12 b^2.                                \tag{SR3}
\]
分别是此处写明方向的非负 LT 违约模、全对线性 RL 模、
cohypomonotone 模；取等无须由不同点达到。取 \(s=0,t\downarrow0\)
使 (SR2) 最后一项无界，说明包含原点的任何右图窗都无有限
\(ab\ge-\rho a^2\) 的 hypomonotone 常数。对
\(0<\gamma<1\)，有界 Minty 域继承某个有限全对 Hölder 常数，
此句不宣称其锐值。

<a id="sr-escape"></a>
## C86-v1：真实二次 EB 与无第二个合法受限步

写 \(p=t^2-t\)。它在 \([0,1/4]\) 严格下降，故
\[
D_U=\operatorname{ran}(I+F_U)=[-3/16,0],\quad
t(p)=\frac{1-\sqrt{1+4p}}2,\quad
J_{F_U}(p)=\{t(p)^2\}.                              \tag{SR4}
\]
对每个 \(p\in D_U\setminus\{0\}\)，唯一实际输出
\(J_{F_U}(p)=t(p)^2>0\) 已**不在** \(D_U\)；因此受限算法的非零
初值仅有一步，不能组成无限合法路径。对 \(0\le x\le1/16\)
有 \(S_U=\{0\}\)、\(r_{F_U}(x)=\sqrt x\)，从而
\[
d(x,S_U)=x=r_{F_U}(x)^2,qquad
\frac{J_{F_U}(p)}{|p|^2}=\frac1{(1-t(p))^2}\longrightarrow1
\quad(p\uparrow0).                                  \tag{SR5}
\]
真残差固定零目标的局部最大幂是 \(q=2\)，在该幂的锐系数为
1；更大幂沿 \(x\downarrow0\) 失败。尽管沿实际输入有锐二次
**一步**估计，缺少受限自然域的不变性就没有“二次收敛轨道”。

<a id="sr-parent"></a>
## C87-v1：母关系的远支与全部合法路径

母图的参数 \(t=\sqrt x\in[0,\infty)\) 给输入 \(p=t^2-t\)，
自然域 \(D_\infty=[-1/4,\infty)\)。令
\(t_\pm(p)=(1\pm\sqrt{1+4p})/2\)。全部纤维为
\[
J_{F_\infty}(p)=
\begin{cases}
\varnothing,&p<-1/4,\\
\{t_-^2,t_+^2\},&-1/4\le p\le0,\\
\{t_+^2\},&p>0.
\end{cases}                                         \tag{SR6}
\]
在 \(p=-1/4\) 重根只算一个输出。尤其
\(J_{F_\infty}(0)=\{0,1\}\)：图点 \((0,0),(1,-1)\) 的
Minty 输入相同，Cayley 输出分别为 0、2。因此完整母图不满足
任何 \(\omega(0)=0\) 的全对反射模，受限图的 \(L=3\) 不能转授。

每个非零自然输入的任一第一步输出为正；此后输出唯一，且
\(x_{k+1}-x_k=\sqrt{x_{k+1}}>0\)。若它有有限极限
\(\ell>0\)，取极限得到 \(\sqrt\ell=0\)，矛盾，故路径趋
\(+\infty\)。零初值可恒选 0，也可在任一步选 1 后发散。

<a id="sr-boundary"></a>
## 身份与推论的精确边界

在受限图上可同时成立 (SR3) 的全对证书、(SR5) 的真输出
EB 和一个漂亮的二次一步比值，却无法合法续步；把图扩大回
母关系则改变了完整 resolvent 的纤维，立刻引入同输入跨支
碰撞和发散路径。这是**对象身份和输入不变性**的障碍，不是
对加了 coverage、完整排他与严格留域前提的局部 PPA 定理的
反例。来源其余 GX 观察和定理先行性另审。
