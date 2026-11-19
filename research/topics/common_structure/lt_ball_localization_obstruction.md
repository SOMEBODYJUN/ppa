# Luke–Tam 印刷定理的同球留域反例

<a id="lt-ball-counterexample"></a>
## C340：全部结构前提成立，不存在所声明的同半径球

**Status：derived-checked。** 本页只反驳 Luke–Tam 正式版 Theorem 2 的同球原根存在及同球极限子结论，不反驳其原图结构等价、距离估计或在适当不同初值域和工作域上的局部收敛机制。主代理核对原文并作精确代数检查，独立 Astra 研究席重新核对定义、Assumption 2 的全部前提、极大性及反例。公开勘误状态未核，不作优先权主张。

**原文定位。** D. R. Luke and M. K. Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, DOI [10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)，2025 年正式 13 页版：[PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)。Definition 2 为印刷 p.4；Assumption 2 与 Theorem 2 为 p.10。后者声明存在同一个 \(\delta>0\)，使每个 \(x\in B_\delta(\bar x)\cap D\) 都有原根属于 \(B_\delta(\bar x)\)，并对相应球内轨道声明极限也在该球。以下输入严格在开球内，输出严格在闭球外，因此不受球的开闭约定影响。

固定 \(X=D=\mathbb R^2\)、\(\lambda=1\)，定义完整单值原算子
\[
 F(a,b)=(-b/2,b),\qquad S=F^{-1}(0)=\mathbb R\times\{0\},\qquad \bar x=(0,0).
\tag{LB1}
\]
直接解两个坐标得完整近端
\[
 J_F(x_1,x_2)=(x_1+x_2/4,x_2/2).
\tag{LB2}
\]
它全域有且仅有一个原根，且自映射于 \(D\)。没有删支或改变原图。

### 逐项验证 Assumption 2

1. \(S\) 非空闭，故零点存在前提成立。
2. (LB2) 证明完整自映射前提。
3. 完整真残差为
   \[
   r_F(a,b)=\frac{\sqrt5}{2}|b|,\qquad d((a,b),S)=|b|=K r_F(a,b),\quad K=\frac2{\sqrt5}.
   \tag{LB3}
   \]
   对每个零点可取 \(\mathcal N=\mathbb R^2\)，于是原文的 \(\mathcal N'=\mathbb R^2\)。这里没有借用“非空即邻域”的错误推断。
4. 取 \(U=U'=W=\mathbb R^2\) 和 \(\tau=1/16\)。任意两图点之差写作 \(\Delta y=(a,b)\)、\(\Delta v=(-b/2,b)\)，则
   \[
   \langle\Delta y,\Delta v\rangle+\tau\|\Delta y+\Delta v\|^2
   =\frac{(2a-9b)^2}{64}\ge0.
   \tag{LB4}
   \]
   这正是 Definition 2 的全图次单调条件。极大性也直接成立：若新增相容图点 \((u,w)\)，由全输入覆盖找到原图点 \((y,v)\)，满足 \(u+w=y+v\)。在该点对上次单调性要求
   \[
   0\le\langle u-y,w-v\rangle=-\|u-y\|^2,
   \]
   故新增点已在原图。由于 \(W\) 为全空间，截取关系没有变化，\((I+F)(U)=\mathbb R^2\) 证明原文的局部值域覆盖。

最后，全部参数保持原值，且
\[
 \tau(1+K/\lambda)^2
 =\frac9{80}+\frac{\sqrt5}{20}
 <\frac14<\frac12.
\tag{LB5}
\]
第一个严格不等式也由 \(K<1\) 直接得到。以上同样适用于每个 \(\bar x\in S\)，因为沿第一坐标平移不改任何条件。

### 同球子结论失败

任给 \(\delta>0\)，取
\[
 x_\delta=\delta(19/20,1/4),\qquad
 J_Fx_\delta=\delta(81/80,1/8).
\]
精确计算给
\[
 \|x_\delta\|^2=\frac{193}{200}\delta^2<\delta^2,
 \qquad
 \|J_Fx_\delta\|^2=\frac{6661}{6400}\delta^2>\delta^2.
\tag{LB6}
\]
完整原根唯一，因此不存在另一支留在该球。这反驳了对每个球内初值存在同球原根的量词。

### 仍成立的动力学与可回收信息

对任意初值 \((a_0,b_0)\)，完整轨道为
\[
 x^k=\left(a_0+\frac{b_0}{2}(1-2^{-k}),\;2^{-k}b_0\right)
 \longrightarrow (a_0+b_0/2,0).
\tag{LB7}
\]
故这张原图实际上全初值收敛且有限长。对 (LB6) 的输入，极限为 \(\delta(43/40,0)\)，仍在同球外。错误在于把到零集的收缩升级成对某个固定零点的同半径球保持；切向输运会改变最终零点。

这也解释了 [此前 LT 接口审查](../../canonical/selection_literature_boundaries.md#sl-lt) 中 \(B_\delta\to B_r\) 的未闭步骤为何不能直接补成原印刷结论。可以另以严格长度预算选择更小初值域和较大工作域；该修订须独立陈述并证明。不能把反例写成“LT 的任何收敛结论均错误”，也不能用改换度量或改换球来宣称恢复了被反驳的原句。

本页是 G3 导入审查得到的障碍，不是共同条件 \(M\) 的完成证明。第二独立基准可采用经典最大单调 PPA；若继续导入 Luke–Tam 参数行，应将其有效图条件与被反驳的同球表述分开。
