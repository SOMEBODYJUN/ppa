# Spingarn 作者版本：一阶输入商与全图极大性

这里只认证实际取得的作者版本。1980完整作者稿、1981研究报告与后来两篇正式刊本
分别命名；定义原文身份为 primary-checked，四个GX对象的匹配依各自已核直接计算。
正式刊本正文/版本逐项比较仍 deferred；没有导入历史PPA收敛定理或先行性。

<a id="sp-versions"></a>
## 一手版本与精确页

作者为 Jonathan E. / J. E. Spingarn，旧源的R.缩写已纠正。

| 实读版本 | 可复读的一手来源与定位 |
| --- | --- |
| Bazaraa–Spingarn，Mathematical programming with and without differentiability，1980-08 Final Report | Georgia Tech [handle1853/36361](https://hdl.handle.net/1853/36361)，[机构PDF](https://repository.gatech.edu/bitstreams/265edf81-f3f1-41c1-92b4-c7021e562cdd/download)，191页；附录完整作者稿Submonotone subdifferentials of Lipschitz functions在印刷157–186，§II定义161–162（物理166–167） |
| 同名1981-06 Final Report | Georgia Tech [handle1853/36359](https://hdl.handle.net/1853/36359)，[机构PDF](https://repository.gatech.edu/bitstreams/d80188ab-cc04-4e34-8139-528b8e3052fd/download)，28页；strict hypo/全图极大性在印刷10–11（物理16–17），p.15将两项论文分别列为[1]/[4] |
| 正式刊本书目，仅身份 | [1981 TAMS264,77–89](https://www.ams.org/tran/1981-264-01/S0002-9947-1981-0597868-8/)，DOI10.1090/S0002-9947-1981-0597868-8；[1982 NFAO4(2),123–150](https://www.tandfonline.com/doi/abs/10.1080/01630568208816109)，Submonotone mappings and the proximal point algorithm |

正常无账号公开请求取得机构PDF，元数据核版本，定义扫描页逐符号看过。
1980稿页码不能改称1981刊本页；1981报告不是完整1982 mapping稿。
两份PDF SHA-256分别为2628d02f858a1675dc11aa289dcfb86b28fd7cea54e920fe877919d7e43a5b0f、
6517e6beb28fab21d350781a2473768fb374761ce203bbcb6b7baec205b75a88。

<a id="sp-first-order"></a>
## 1980稿的准确输入/输出量词

§II声明 \(T:\mathbb R^n\rightrightarrows\mathbb R^n\) 为图闭、凸值关系，允许空值。
普通submonotone at \(\bar x\) 是

\[
\liminf_{\substack{x\to\bar x,\ x\ne\bar x\\
u\in T(\bar x),\ v\in T(x)}}
\frac{\langle v-u,x-\bar x\rangle}{\|x-\bar x\|}\ge0.
\tag{SP80-A}
\]

固定的是输入，锚纤维全部 \(u\) 仍参与量词；不要求 \(v\to u\)，也不限制输出有界。
锚纤维空时真空成立。strict条件为

\[
\liminf_{\substack{x_1,x_2\to\bar x,\ x_1\ne x_2\\
u_i\in T(x_i),\ i=1,2}}
\frac{\langle x_1-x_2,u_1-u_2\rangle}{\|x_1-x_2\|}\ge0.
\tag{SP80-S}
\]

只有输入趋近，没有两图点共同趋向一个指定图点的门。local boundedness是随后
等价定理的额外假设，不属于这两个定义；本页不调用那些等价定理。

<a id="sp-maximal"></a>
## 1981报告的strict hypo与极大性

报告定义

\[
\forall K\subset\mathbb R^n\ \text{bounded},\quad
\exists k_K\ge0:\quad T+k_KI\text{ 在 }K\text{ 上单调}.
\tag{SP81-H}
\]

maximal另要求完整图不被另一满足SP81-H的关系图真包含。比较关系可各有自己的
\(k_K\)；这是整个类的全图包含极大性，不是固定 \(\sigma\) 的hypo类，
也不是固定LT参数/图窗极大性。SP80-S的一阶分母不等于SP81-H的平方预算；
两项名称不能合成同一个条件。

<a id="sp-gx-match"></a>
## 已核GX对象逐项匹配

| 完整规范对象 | 作者版本中的准确判断 |
| --- | --- |
| [GX053有界负平方](../topics/examples/bounded_negative_square.md#bns-geometry) | 图闭、凸值；两输入商 \(-(x_1+x_2)\lvert x_1-x_2\rvert\to0\)，所以满足1980稿strict条件；全域hypo系数1也给SP81-H。该页明示全域1-hypo真扩张，因此也排除1981报告的全类极大性，不靠名称推断 |
| [GX055孤立极点](../topics/examples/isolated_pole_relation.md#ip-geometry) | 图闭、凸值；零锚商 \(-1/x\to-\infty\) 合法排除SP80-A/S；输出逃逸不能删掉。bounded \(K=[0,\varepsilon]\) 迫使 \(k_K\ge1/x^2\)，故SP81-H也失败 |
| [GX056阶梯](../topics/examples/rational_irrational_staircase.md#gx056-rl) | 零锚商与两输入商的下极限分别为1、−1；完整图非闭，所以不能称属于1980稿声明的闭凸值关系类。近输入/跳输出亦排除SP81-H |
| [GX057乘积](../topics/examples/product_splice.md#gx057-rl-phase) | 输入趋近的strict商下极限−1与SP80-S对应；另强制图点趋同一输出后商0是不同条件。完整图非闭，不能由锚商0授予原稿类别成员；固定首坐标复制阶梯排除SP81-H |

本表不改变例卡独立的完整纤维/RL/残差/路径证明。七个历史出现位置对应同一个
版本与量词义务，不计成七个新定理。1981/1982刊本定义是否原样保留、精确算法
定理及局部窗仍须正式原页；当前作者版本足以支持上表明确限定的判断。
