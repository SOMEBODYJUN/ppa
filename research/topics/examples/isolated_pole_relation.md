# 孤立零图点与极点支：锐反射模、残差逃逸和完整路径

<a id="ip-object"></a>
## 完整对象、来源和局部窗口

在实数空间固定 \(0<\varepsilon<1\)，定义完整关系
\[
F(x)=
\begin{cases}
\{0\},&x=0,\\
\{-1/x\},&0<x\le\varepsilon,\\
\varnothing,&\text{其余 }x .
\end{cases}
\qquad S=F^{-1}(0)=\{0\}.
\tag{IP1}
\]
其定义域是**连通**区间 \([0,\varepsilon]\)。图由孤立点
\((0,0)\) 和极点支组成，图不连通且闭：极点支上
\(x\downarrow0\) 时输出趋 \(-\infty\)，不产生有限图聚点。
任何输出窗 \(|v|<1/\varepsilon\) 都只含零图点。

来源为 [9/01 ZIP](../../../history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip)
内 work/b_monotonicity_gaps.md §MGB-05（行 197–240）和
work/c_gx053_065.md §GX-055（行 221–310）；对象在
research/gap_examples.md §GX-055（行 579–586）及
research/example_properties.md §GX-055（行 814–822）重述。
以下从 (IP1) 独立计算。来源的“disconnected domain”应改为
“disconnected graph”；历史 Spingarn 名称、最大性名称和外部先行性
均不在这里验收。

全部逆纤维为
\[
F^{-1}(v)=
\begin{cases}
\{0\},&v=0,\\
\{-1/v\},&v\le-1/\varepsilon,\\
\varnothing,&\text{其余 }v .
\end{cases}
\tag{IP2}
\]

<a id="ip-minty"></a>
## 全步长的完整近端纤维与锐全对模

固定任意 \(\lambda>0\)。极点支的 Minty 输入与反射输出为
\[
g_\lambda(x)=x-\lambda/x,\qquad
h_\lambda(x)=x+\lambda/x,\qquad 0<x\le\varepsilon.
\tag{IP3}
\]
\(g_\lambda'(x)=1+\lambda/x^2>0\)。记
\[
b_\lambda=\varepsilon-\lambda/\varepsilon,\qquad
j_\lambda(p)=\frac{p+\sqrt{p^2+4\lambda}}2.
\]
自然输入域和**全部**近端纤维为
\[
D_\lambda=(-\infty,b_\lambda]\cup\{0\},\qquad
J_{\lambda F}(p)=
\begin{cases}\{j_\lambda(p)\},&p\le b_\lambda,\\
\varnothing,&p>b_\lambda\end{cases}
\ \cup\
\begin{cases}\{0\},&p=0,\\
\varnothing,&p\ne0.\end{cases}
\tag{IP4}
\]
这里两个集合必须取并，不能把 \(p=0\) 的极点输出漏掉。
完整反射 \(R_{\lambda F}(p)=\{2x-p:x\in J_{\lambda F}(p)\}\)
同样是集合并：在极点输入上贡献
\(\{\sqrt{p^2+4\lambda}\}\)，在零输入另贡献 \(\{0\}\)。

| 步长 | 零输入完整纤维 | 零附近完整输入覆盖 | 完整图全对 RL |
| --- | --- | --- | --- |
| \(0<\lambda<\varepsilon^2\) | \(\{0,\sqrt\lambda\}\) | 有输入球，因 \(b_\lambda>0\) | 任意零消失模失败 |
| \(\lambda=\varepsilon^2\) | \(\{0,\varepsilon\}\) | 无输入球，\(D_\lambda=(-\infty,0]\) | 任意零消失模失败 |
| \(\lambda>\varepsilon^2\) | \(\{0\}\) | 无输入球，零为 \(D_\lambda\) 的孤立点 | 锐线性模如下 |

对两个非零图点记 \(a=x-y,b=F(x)-F(y)=a/(xy)\)。于是
\[
\frac{|a-\lambda b|}{|a+\lambda b|}
=\frac{|xy-\lambda|}{xy+\lambda}<1
\quad(x\ne y).
\tag{IP5}
\]
对 \((x,-1/x)\) 与 \((0,0)\)，则
\[
ab=-1,\qquad
\frac{|a-\lambda b|}{|a+\lambda b|}
=\frac{x^2+\lambda}{|x^2-\lambda|}.
\tag{IP6}
\]
若 \(\lambda\le\varepsilon^2\)，取 \(x=\sqrt\lambda\) 即得相同
Minty 输入 0、不同反射输出 \(2\sqrt\lambda\) 和 0，排除每个
\(\omega(0)=0\) 的全对反射模。

若 \(\lambda>\varepsilon^2\)，(IP6) 随 \(x^2\) 递增，并在
\(x=\varepsilon\) **取到**最大值。因此完整图的锐线性 RL 模
及此处明定方向的非负 LT 违约模分别为
\[
L_{\lambda,1}^*=
\frac{\lambda+\varepsilon^2}{\lambda-\varepsilon^2},
\qquad
\tau_\lambda^*=
\frac{\lambda\varepsilon^2}{(\lambda-\varepsilon^2)^2},
\quad
\lambda ab\ge-\tau_\lambda^*|a+\lambda b|^2 .
\tag{IP7}
\]
第二式可直接由 (IP6) 的
\(\lambda x^2/(\lambda-x^2)^2\) 最大化得到，也满足
\(\tau_\lambda^*=(L_{\lambda,1}^{*\,2}-1)/4\)。
极点支内部给非负内积，故不增加违约模。
这里使用的是打印出的代数条件，不借用未核的历史定理。

任何 \(0<\gamma<1\) 的**全图全尺度** RL 都失败：
用极点输入 \(p\to-\infty\) 与零输入比较，反射输出为
\(\sqrt{p^2+4\lambda}\)，其与 \(|p|^\gamma\) 的比值趋无穷。
在 \(\lambda>\varepsilon^2\) 时，若再允许 \(\gamma>1\)，
取任一固定内部极点处趋同的不同点对，因
\(h_\lambda'\ne0\)，也会失败。因此全图唯一可能的正幂指数是 1，
且恰在 \(\lambda>\varepsilon^2\) 成立。

同一完整 \(J_{\lambda F}:D_\lambda\to\mathbb R\) 在
\(\lambda>\varepsilon^2\) 的锐 Lipschitz 模还可直接计算为
\[
K_\lambda^*=\frac{\varepsilon^2}{\lambda-\varepsilon^2}.
\tag{IP8}
\]
极点支点对的比值是 \(xy/(xy+\lambda)\)，而相对零输入的比值
是 \(x^2/(\lambda-x^2)\)；后者在端点取到更大的上确界。
所以 \(\lambda>2\varepsilon^2\) 时这个非自映射的 Lipschitz 模
小于 1，仍须另核其输出能否充当下一输入。

<a id="ip-geometry"></a>
## 图几何的两种局部量词

由 (IP5) 的 \(ab=a^2/(xy)>0\) 与 (IP6) 的 \(ab=-1\) 得
\[
\inf_{a\ne0}\frac{ab}{a^2}=-\infty,\qquad
\inf_{b\ne0}\frac{ab}{b^2}=-\varepsilon^2.
\tag{IP9}
\]
因此完整图无有限 hypomonotone 模，而
\(ab\ge-\varepsilon^2 b^2\) 的 cohypomonotone 系数锐；
第二个下确界由零图点与端点取到。
任一**仅限制输入**的零邻域仍使第一下确界为 \(-\infty\)。
若同时限制输出到零附近，图只剩 \((0,0)\)，成对条件全都真空；
不能把这两种“局部”窗口混用。

来源打印的固定端一阶商可无外部引用地核算：
\[
\frac{(F(0)-F(x))(0-x)}{|x|}=-1/x\longrightarrow-\infty.
\tag{IP10}
\]
同一固定端序列也排除允许该端点的两移动输入一阶商条件。
此结论的输出逃逸也符合[1980作者稿的准确量词](../../canonical/spingarn_author_definitions.md#sp-gx-match)；
两正式刊本对应仍未闭，
也不把输出逃逸序列当作趋向 \((0,0)\) 的图点序列。

<a id="ip-residual"></a>
## 真实零残差、零局部系数和缺失目标纤维

按完整纤维计算，
\[
r_F(x)=
\begin{cases}0,&x=0,\\1/x,&0<x\le\varepsilon,\\
+\infty,&\text{其余 }x.\end{cases}
\tag{IP11}
\]
每个 \(q>0\) 在有限残差点上都有精确比值
\[
\frac{d(x,S)}{r_F(x)^q}=x^{q+1},\qquad 0<x\le\varepsilon.
\tag{IP12}
\]
全定义域上 \(d(x,S)\le\kappa r_F(x)^q\) 的锐系数是
\(\varepsilon^{q+1}\)；限制到 \(0\le x\le a\le\varepsilon\) 后是
\(a^{q+1}\)。因此每个正幂的固定零目标 MSR/SMSR 的最优
**局部系数下确界**为 0，但常数 0 不在任何含正定义域点的
固定输入邻域上成立。域外点仅对 \(\kappa>0\) 使用
\(\kappa(+\infty)=+\infty\)，不计算 \(0\cdot(+\infty)\)。

这里有真实的域内序列 \(x\downarrow0\)，其残差趋无穷：
零系数机制是残差逃逸与图点孤立。若采用
[D04](../../foundations.md) 的有限残差窗口
\(r_F(x)\le\bar t<1/\varepsilon\)，窗口内却只有零点；
这个小残差 EB 本身没有测量非零输出。

由 (IP2)，每个足够小的非零目标 \(v\) 都有空逆纤维。
取 \(x=0\) 时，任意正指数、有限系数的两变量 MR 或固定输入
HREG 的左边 \(d(0,F^{-1}(v))=+\infty\)，右边只含有限的
\(|v|^q\)，所以均失败；SMR 同样没有定义在整个目标球上的
非空逆定位。反向关系在近零目标上只有 \(\{0\}\) 或空纤维，
故 calm/isolated calm 的零系数包含式成立，但其非零目标部分真空。
Aubin 包含式用目标 0 的 \(\{0\}\) 对非零目标的空集即失败。

<a id="ip-path"></a>
## 完整近端的全部无限路径与留域障碍

固定同一 \(\lambda>0\)，称路径合法若
\(p_{k+1}\in J_{\lambda F}(p_k)\) 在每一步成立；
继续下一步须 \(p_{k+1}\in D_\lambda\)。

若 \(\lambda>\varepsilon^2\)，非零合法输入必在负极点输入支上，
其输出为正，而 \(D_\lambda\) 除 0 外只有负数。因此每个非零
输入只有一个合法步，输出后即无法继续。零输入的唯一输出为零。
即使 (IP8) 小于 1，这个域障碍仍在。

若 \(\lambda=\varepsilon^2\)，负输入同样一步后离域；从零输入
可一直选零，或在某步选 \(\varepsilon>0\) 后立即离域。

若 \(0<\lambda<\varepsilon^2\)，\(D_\lambda=(-\infty,b_\lambda]\)
包含零输入球，但零输入可选 \(\sqrt\lambda\)。
任何极点步后输出为正；只要它仍可作下一输入，后续正侧步满足
\[
p_{k+1}-p_k=\lambda/p_{k+1}\ge\lambda/\varepsilon>0.
\tag{IP13}
\]
正输入却必须始终不超过有限的 \(b_\lambda\)，故极点步之后
不可能有无限合法后续路径。从零可任意有限时间等待再选极点，
但一旦选择极点便有限步离域。

综上，对**每个** \(\lambda>0\)，唯一无限合法完整近端路径是
恒零路径，任何非零初值都没有无限合法路径。
这不是非零轨道的收敛速率。完整图线性 RL 成立的步长恰好
没有零输入球；有零输入球的步长又有同输入碰撞。
真零残差的全部正幂 EB 与严格 (IP8) 均不填补输入覆盖和留域。

<a id="ip-scope"></a>
## 本卡的审查范围

本卡独立证明了完整原图与逆纤维、全步长完整近端/反射纤维、
锐 RL/LT 与两种单参数图模、固定零目标的真实残差系数、
缺失目标纤维以及全部无限合法路径的分类。
路径分类与 (IP8) 是本卡从原对象新增的直接推导。
没有数值网格或外部定理承担一般量词证明；历史名称、最大性
类别及外部优先性仍未审，也不关闭同 ZIP 的其它 GX 卡。
