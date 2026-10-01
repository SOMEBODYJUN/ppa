# 有界负平方图：端点 Minty 折叠、零目标残差与实际越域

<a id="bns-object"></a>
## 完整对象与来源边界

在实数空间定义完整关系
\[
F(x)=\begin{cases}\{-x^2\},&0\le x\le1/2,\\
\varnothing,&\text{其余 }x,\end{cases}
\qquad S=F^{-1}(0)=\{0\}.
\tag{NS1}
\]
图紧，\(r_F(x)=x^2\) 仅对 \(x\in[0,1/2]\) 有限。对固定
\(\lambda>0\)，自然输入域为 \(D_\lambda=g_\lambda([0,1/2])\)，
\(g_\lambda(x)=x-\lambda x^2\)；反射坐标为
\(h_\lambda(x)=x+\lambda x^2\)。完整近端纤维是
\(J_{\lambda F}(p)=\{x\in[0,1/2]:g_\lambda(x)=p\}\)，不能在
\(D_\lambda\) 外自行延拓。

来源线索为 9/01 ZIP `work/c_gx053_065.md` 的 GX-053，精确成员路径见
[逐源去向](../../audit/UNIT_DISPOSITIONS.tsv)。下列断言重新从 (NS1)
计算；旧稿对 Spingarn 名称、VI 标签及外部先行性的归类不在本卡审查范围。

<a id="bns-minty"></a>
## C100-v1：全图成对模随步长的相变

任取两个**完整图点** \((x,-x^2),(y,-y^2)\)，记
\(a=x-y,s=x+y\in[0,1]\)，则
\[
\Delta g_\lambda=(1-\lambda s)a,\qquad
\Delta h_\lambda=(1+\lambda s)a,
\quad |a|\le\min\{s,1-s\}.
\tag{NS2}
\]
若 \(0<\lambda<1\)，\(g_\lambda\) 严格增，\(D_\lambda
=[0,1/2-\lambda/4]\)，完整 \(J\) 在此域单值；全图线性
all-pairs RL 的锐常数为 \((1+\lambda)/(1-\lambda)\)，由
\(x,y\uparrow1/2\) 的不同比值逼近。零邻域的局部线性下确界
为 1，但在任意非退化正侧窗口，实际锐系数严格大于 1。

在临界 \(\lambda=1\)，\(g\) 仍严格增且
\(D_1=[0,1/4]\)，完整纤维为
\[
J_F(p)=\left\{\frac{1-\sqrt{1-4p}}2\right\},
\quad p\in D_1.
\tag{NS3}
\]
全图线性 RL 不成立。对 \(0<\gamma<1\)，全图不等式
\(|\Delta h|\le L|\Delta g|^\gamma\) 的临界指数是 \(1/2\)，
且 \(L_{1,1/2}^*=2\)：对不同的两图点，(NS2) 在 \(\gamma=1/2\) 给
\[
\frac{|\Delta h|^2}{|\Delta g|}
=\frac{|a|(1+s)^2}{1-s}\le4,
\tag{NS4}
\]
\(x=1/2,y\uparrow1/2\) 使左式趋 4，并排除所有更高指数。
为固定更低指数的常数身份，\(0<\gamma<1/2\) 时的锐值为
\[
L_{1,\gamma}^*=
\begin{cases}
3\,2^{2\gamma-2},&0<\gamma\le1/3,\\
\displaystyle\frac1{1-\gamma}
\left(\frac{1-2\gamma}{1-\gamma}\right)^{1-2\gamma},
&1/3\le\gamma<1/2.
\end{cases}
\tag{NS5}
\]
证明是先按固定 \(s\) 取最大合法 \(|a|=\min(s,1-s)\)：
在 \(s\le1/2\) 结果递增，在 \(s\ge1/2\) 优化
\((1+s)(1-s)^{1-2\gamma}\)。其驻点
\(s=\gamma/(1-\gamma)\) 仅在 \(\gamma\ge1/3\) 进入后半区。
所有取等或逼近点对都在所声明的整个图内。

若 \(\lambda>1\)，顶点 \(x_*=1/(2\lambda)\) 落在区间内部。
对充分小的 \(t>0\)，\(x_*\pm t\) 有**相同** Minty 输入、
不同反射输出，故不存在任何在零处消失的全图 all-pairs 反射模。
这不否定隔离某个单调小图窗之后的局部条件。

<a id="bns-zero"></a>
## C101-v1：真零残差与全部合法正侧路径

固定目标 \((0,0)\)。每个域内输出满足精确恒等式
\[
d(x,S)=x=r_F(x)^{1/2}.
\tag{NS6}
\]
因此原算子固定零目标的最大局部幂次是 \(q=1/2\)，该幂
最小可行系数为 1；\(0<q<1/2\) 缩窗系数下确界为 0，
\(q>1/2\) 不成立。正目标的完整逆像为空，所以 (NS6)
不推出零附近双侧目标的两变量 MR。这里的残差是原算子的
**全纤维** \(r_F\)，不是输入的近端步残差。

固定 \(\lambda=1\) 并定义合法路径 \(p_{k+1}\in J_F(p_k)\)，
要求每一步 \(p_k\in D_1\)。从 \(p_0=0\) 出发恒为零；对每个
\(0<p_0\le1/4\)，所有合法步唯一，且由
\(p_k=p_{k+1}-p_{k+1}^2\) 得 \(p_{k+1}>p_k\)。若它无限合法，
有界递增极限 \(\ell\in(0,1/4]\) 必满足 \(\ell^2=0\)，矛盾。
所以**每个**正初值在有限步后输出离开 \(D_1\)，不能组成
无限合法 PPA 路径。图闭、全图半阶 RL 和真零残差半阶同时
成立，仍不提供零点输入球 coverage、收缩兼容或留域。

这张卡只审 GX-053 的这些完整图、成对模、零残差和路径单元；
没有把端点处的全图锐性说成零点附近的局部最优指数。
