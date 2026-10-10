# 切向有向面积：绝对长度之外的 PPA 点收敛研究种子

日期 2026-10-10。这个独立方向来自一位 Astra 的模型构造与主代理的解析重构/有限复算。**Status：`candidate`**：以下精确模型和证明草案已固定，已由构造者核读最终正文，尚缺未参与构造者的独立接收；一般原生算子判据与发表先行性开放。它不声称满足旧严格兼容前件而推翻旧收敛定理。

<a id="ta-object"></a>
## TA1 · 全部输入的真实普通 PPA

写 \(u=(w,z,r)\in\mathbb C\times\mathbb R\times\mathbb R\)。取 \(p>0,\omega\in\mathbb R\)，令
\[
d(0)=0,\quad d(r)=|r|^p\exp(i\omega/|r|)\ (r\ne0),
\]
\[
T(w,z,r)=\left(w+d(r),\ z+\tfrac12\operatorname{Im}(\bar w d(r)),\ r/(1+|r|)\right).
\tag{TA1}
\]
这是 \(\mathbb R^4\) 到 \(\mathbb R^3\times(-1,1)\) 的同胚。对输出 \(|r|<1\)，置 \(s=r/(1-|r|),b=d(s)\)，定义完整单值原关系
\[
F(w,z,r)=(-b,-\tfrac12\operatorname{Im}(\bar w b),s-r),
\tag{TA2}
\]
slab 外为空值。反算中央坐标时 \(\operatorname{Im}(\bar b b)=0\)，所以 \(F=T^{-1}-I\)。故 \(\lambda=1\) 的**完整** \(J_F=T\) 在全部 \(\mathbb R^4\) 上单值，\(S=\mathbb R^3\times\{0\}\)。同一原关系的真残差满足
\[
d(u,S)=|r|\le\|F(u)\|^{1/p}\quad(|r|<1).
\tag{TA3}
\]
原因是 \(\|F(u)\|\ge|b|=|s|^p\) 且 \(|r|\le|s|\)。对 \(0<p<2\)，取 \(w=0,r\to0\) 时 \(s-r=O(r^2)\)，证明该 EB 幂 \(q=1/p\) matching。

<a id="ta-area"></a>
## C232-v1 · 精确点/长度分类候选

对任意非零法向初值 \(r_0\)，置 \(t_0=1/|r_0|\)。真实 PPA 有
\[
|r_n|=(t_0+n)^{-1},\quad
d_n=(t_0+n)^{-p}\exp(i\omega(t_0+n)).
\tag{TA4}
\]
若 \(\omega\notin2\pi\mathbb Z\)，则 \(w_n\) 收敛，并且
\[
z_N-\tfrac14\cot(\omega/2)\sum_{n<N}(t_0+n)^{-2p}
\quad\text{有有限极限}. \tag{TA5}
\]
预期由下面草案得到：非共线相位 \(\omega\notin\pi\mathbb Z\) 的点收敛当且仅当 \(p>1/2\)；反向共线相位 \(\omega\in\pi+2\pi\mathbb Z\) 对每个 \(p>0\) 点收敛；同向相位 \(\omega\in2\pi\mathbb Z\) 点收敛当且仅当 \(p>1\)。全部相位的有限长度恰为 \(p>1\)。\(r_0=0\) 是固定点，不能包含在这些必要性量词内。

**证明草案。** 记 \(a_n=(t_0+n)^{-p},q=e^{i\omega}\)。\(q\ne1\) 时 Dirichlet 判别给 \(R_n=\sum_{j\ge n}d_j\) 收敛。两次 Abel 求和，利用差分 \(a_n-a_{n+1}\) 非负单调，给
\[
R_n=\frac{d_n}{1-q}+O(a_n/(t_0+n)).
\]
具体余项可取
\[
\left|R_n-\frac{d_n}{1-q}\right|
\le\frac{2(a_n-a_{n+1})}{|1-q|^2}
\le\frac{2p}{|1-q|^2}\frac{a_n}{t_0+n}.
\]
于是 \(w_n=w_\infty-R_n\)，TA1 的中央步为
\[
z_{n+1}-z_n
=\tfrac12\operatorname{Im}(\bar w_\infty d_n)
+\tfrac14\cot(\omega/2)a_n^2
+O(a_n^2/(t_0+n)).
\]
第一项级数收敛，误差项绝对可和，得 TA5。非零 cot 时 \(\sum a_n^2\) 的敛散给点分类；\(q=-1\) 的步全在同一水平直线上，中央自面积为零。\(q=1\) 时水平位移是同向正级数。每步长度至少 \(|d_n|=a_n\)，故 \(p\le1\) 长度无限；\(p>1\) 时水平有界，中央步为 \(O(a_n)\)，法向总变差有限，故全长度有限。独立接收还须检查每个余项与共线退化量词。

**决定性对照。** \(p=1/3\) 时，\(\omega=\pi\) 与 \(\omega=\pi/2\) 的法向距离完全相同，水平增量均条件可和，真 EB 同为 \(q=3\)；前者点收敛，后者 \(z_N\sim(3/4)N^{1/3}\)。一阶切向可和不足以判点收敛，二阶有向面积可以保留净漂移。

<a id="ta-frontier"></a>
## 新机制、先行祖先与必须完成的工作

水平场 \(X=\partial_x-(y/2)\partial_z,Y=\partial_y+(x/2)\partial_z\) 有 \([X,Y]=\partial_z\)。交换子/周期运动生成位移是经典非完整控制机制，参见 Murray–Sastry, *Nonholonomic Motion Planning: Steering Using Sinusoids*, IEEE TAC 1993，[作者存档](https://authors.library.caltech.edu/records/4g4pk-07277)。本轮一位代理读了全文；主代理尚未核全文，故不将它登记为主代理已核的定理导入。本页的候选分类只使用显示的初等 Abel 推导。

真正目标 **Q-TA-v1（open）**：从一类事先指定的原生完整算子及有限周期 resolvent 展开，认证首个非零切向交换子及可控余项，得到绝对长度预算之外的点收敛/逃逸判据。应先做二步幂零/有限周期类，而不是定义“面积收敛”然后将其同义改写为轨道收敛。

高阶交换子阶 \(\ell\) 对应门槛 \(p=1/\ell\) 仅是猜想种子，未证。有限切向窗的尖锐 Hölder–RL 模仍需单列完整证明；不能在此将代理报告的指数 \(p/2\) 自动升级为本库已审定理。发散轨道会离开有界切向窗，局部证书不授予全轨道留域。不可和的小切向偏差也可破坏条件抵消，鲁棒扰动合同是另一个实质义务。

代码 [verify_area.py](../code/tangential_area/verify_area.py) 复算完整包含式和相位基准，[area_results.json](../code/tangential_area/area_results.json) 记录参数、seed、精度和实际有限输出；不是无限级数证明。
