# GX-059–065 的剩余属性：完整纤维、VI 符号与局部逆稳定

本页只补现有对象卡中未逐项写出的属性，不替代其主要证明。状态为下列定义和直接计算范围内的 `derived-checked`；所列外部文献归属由 [LITERATURE](../../LITERATURE.md) 的指定版本一手记录另裁决，直接推导与文献事实分层。
来源是 Z07 `work/c_gx053_065.md` 的 551–908、927–1125 行，其成员为1219条物理LF行，SHA-256为 `55df53d130f510c873e2a9d4c4afec9b32eb1930811ad458348088ed452748f4`，与Z05同路径成员逐字节相同。完整 locator与逐单元去向见 [GX059_065_UNITS.tsv](../../audit/GX059_065_UNITS.tsv)。GX 是历史观察号，不是新增独立算子数。本表另覆盖交叉审计1136–1140行；负责范围中的空行和分隔线附于邻接单元，无未分配非空正文。909–926行的公共VI约定以及其余公共文献/数值范围不由本表裁决。

<a id="gxp-conventions"></a>
## 局部定义与证据范围

在实 Hilbert 空间中，对完整图点 \((x,v),(y,w)\) 记 \(a=x-y,b=v-w\)。本页 hypomonotonicity 的非负缺陷是最小 \(h\ge0\)，使全体图点对满足 \(\langle a,b\rangle\ge-h\|a\|^2\)；cohypomonotonicity 则要求某个有限 \(k\ge0\) 使 \(\langle a,b\rangle\ge-k\|b\|^2\)。标量特例的内积就是乘积。二者不等于任意二参数图区域。

为核来源中的 \(\tau\)，只使用明确的同参数不等式
\[
\lambda\langle a,b\rangle\ge-\tau\|a+\lambda b\|^2. \tag{GP1}
\]
当同图全对线性反射锐常数为 \(L\ge1\) 时，展开两平方给 \(\tau^*=(L^2-1)/4\)，与 [PD-TIED](../../canonical/parameter_dictionary.md#pd-tied) 一致。此处是代数定义，不以历史文献命名充当证明。

实标量域 \(E\) 上的 VI 定义固定为对全部 \(x,y\in E\)：
\[
F(x)(y-x)\ge0\Rightarrow F(y)(y-x)\ge0\quad\text{（pseudo）},
\]
\[
F(x)(y-x)>0\Rightarrow F(y)(y-x)\ge0\quad\text{（quasi）}. \tag{GP2}
\]
这是点对符号定义。原来源对 Lei–He 指定稿的归属已在 [LIT-LEI-HE](../../LITERATURE.md#lit-lei-he-2020) 一手核定；这里的数学判断仍由直接代入完成。
普通 MR/MSR/SMR/SMSR 的目标量词采用 [PD-REGULARITY](../../canonical/parameter_dictionary.md#pd-regularity)；所有局部锐模以下均指缩邻域后可行常数的下确界。强度量正则要求目标整个邻域内的完整局部逆纤维非空单值。

<a id="gxp-diagonal"></a>
## GX-059 中的上游 D 与有限截断

[GX-059 的完整图](skew_compact_diagonal.md#scd-object) 是实 \(\ell^2\) 上 \(F=D+B\)，不是仅有 \(D\)。对源卡另提到的 \(D(x_n)=(x_n/n)\)，完整值域是
\[
\operatorname{ran}D=\{y\in\ell^2:(ny_n)_n\in\ell^2\}. \tag{GP3}
\]
有限支撑序列全在此域，故值域稠密；\(y_n=1/n\) 属于 \(\ell^2\)，但 \((ny_n)_n\) 不属于 \(\ell^2\)，所以值域真且非闭。\(De_n=e_n/n\) 也见证无统一正下界。该非闭值域不是 \(F\) 的值域：C102 已证明 \(\operatorname{ran}F=\ell^2\)。

“上游也有病态”只能保留这个值域及无正强单调模的具体意思。\(D\) 本身满足
\(\langle h,Dh\rangle\ge\|Dh\|^2\)，cocoercivity 锐系数为 1（\(h=e_1\) 取等），且是 rectangular：对任意 \(x\in\ell^2,v=Dy\in\operatorname{ran}D\)，置 \(w=z-x,d=y-x\)，有
\[
\langle x-z,v-Dz\rangle
=\langle w,Dw\rangle-\langle w,Dd\rangle
\ge-\tfrac14\langle d,Dd\rangle> -\infty. \tag{GP4}
\]
最后一步是逐坐标完成平方。因此不能把 \(F\) 的非 rectangular 标签转给 \(D\)。

截取前 \(K\) 个二坐标块得到 \(F^{(K)}\) 在 \(\mathbb R^{2K}\) 的完整图。强单调锐系数为 \(1/(2K)\)，而 \(\|F^{(K)}\|=3/2\)（首块给锐性），故至少有正 cocoercivity 系数 \(2/(9K)\)。它的 rectangular 配对关于变量的二次主项正定，所以下确界有限；同时各块仍有奇异值 1，故完整逆像锐系数仍为 1。有限截断消去了零强单调与非 rectangular 的无限维分离，不能提供与 \(K\) 无关的正强单调下界。有限维 \(D\) 截断也满射，因而不会保留 (GP3) 的非闭值域。

<a id="gxp-nonnegative-defects"></a>
## GX-059–063 的非负缺陷

C102/C104/C120 的完整单调图分别给 GX-059、GX-060、GX-061 的非负 hypo 缺陷 0。对 (GP1)，GX-059 的高编号块使 \(\lambda\langle a,Fa\rangle/\|(I+\lambda F)a\|^2\to0\)；GX-060/061 的非零零均值图点差使分子恰为 0。所以这三图的有符号 \(\tau\) 下确界也恰为 0，而非仅“0 可行”。

[旋转族](planar_rotation_family.md#pr-cyclic) 的 \(\langle a,Q_\theta a\rangle=\cos\theta\|a\|^2\)。因此其非负 hypo 缺陷是 \(\max\{0,-\cos\theta\}\)；GX-062/063 两角为 0。两角的 signed \(\tau\) 为负，而仅允许非负参数时为 0，具体数值已由 C122/C123 核算；非负 hypo 缺陷 0 并不否定正强单调性。

<a id="gxp-sine-inverse"></a>
## GX-064 的完整原算子纤维与 VI 类

对象固定为完整 \(F(x)=2+\sin x\) 在 \(\mathbb R\)。\(F\) 连续且严格为正，所以 (GP2) 的 pseudo 前件迫使 \(y-x\ge0\)，后件随 \(F(y)>0\) 成立；quasi 是更弱的前件，亦成立。普通单调却失败：如 \(x=\pi/2,y=3\pi/2\)，有 \(x<y,F(x)>F(y)\)；任何包含正弦严格下降子段的区间都有同样点对。

对于 \(v\in[1,3]\)，令 \(\alpha=\arcsin(v-2)\in[-\pi/2,\pi/2]\)，则全部逆纤维为
\[
F^{-1}(v)=\{\alpha+2m\pi,\pi-\alpha+2m\pi:m\in\mathbb Z\}. \tag{GP5}
\]
两解族来自一周期内的全部正弦解；在 \(v=1,3\) 重合的解只计一次。\(v\notin[1,3]\) 时纤维为空，特别是完整零集为空。

<a id="gxp-sine-hypo"></a>
## GX-064 的 hypo/cohypo 与 subcritical τ

对 \(x\ne y\)，令 \(m=(F(x)-F(y))/(x-y)\)。均值定理给 \(-1\le m\le1\)；取两点趋于 \(\pi\) 则 \(m\to-1\)。因此全图 hypo 锐缺陷为 1。取 \(x=\pi/2,y=\pi/2+\varepsilon\)，割线 \(m=(\cos\varepsilon-1)/\varepsilon<0\) 且 \(m\uparrow0\)；于是 \(ab/b^2=1/m\to-\infty\)，任何有限 cohypo 缺陷均失败。

对 \(0<\lambda<1\)，C81 已核完整近端全域单值及锐 \(L=(1+\lambda)/(1-\lambda)\)。由 (GP1) 得
\[
\tau^*_\lambda=\frac{\lambda}{(1-\lambda)^2}. \tag{GP6}
\]
也可直接取最小割线极限 \(m\to-1\)，使 \(-\lambda m/(1+\lambda m)^2\) 逼近 (GP6)；所以这里的系数是下确界，非仅安全上界。

<a id="gxp-sine-regular-points"></a>
## GX-064 的非零目标端点及普通参考点

C82 已证明在 \((\bar x,\bar v)=(\pi/2,3)\) 的固定目标最大幂 \(q=1/2\)、该幂缩窗模 \(\sqrt2\)、较小正幂模下确界 0，普通 MSR/SMSR 失败。两目标 MR/SMR（包括正幂残差的 MR）失败，因任意目标邻域有 \(v>3\) 的空逆纤维。即使只许下侧目标，\(v=3-\varepsilon\) 的两个解 \(\pi/2\pm\arccos(1-\varepsilon)\) 都趋于 \(\bar x\)，局部完整逆像也不是单值。

若 \(\cos\bar x\ne0\)，连续导数使一个小开区间 \(U\ni\bar x\) 上 \(F'\) 同号且 \(|F'|\ge a>0\)。于是 \(F|_U\) 单射，像包含 \(\bar v=F(\bar x)\) 的开邻域 \(W\)，且全部 \(F^{-1}(v)\cap U\) 正是这一支。均值定理给逆分支 Lipschitz 常数 \(1/a\)；缩窗可令 \(a\to|\cos\bar x|\)，而任意局部常数须至少是逆分支在 \(\bar v\) 的导数绝对值。因此普通 SMR 的精确缩窗模为
\[
\frac1{|\cos\bar x|}. \tag{GP7}
\]
这是完整原算子的局部逆像观察，不是 C81 的 Minty 临界指数。

<a id="gxp-square-inverse"></a>
## GX-065 的完整原纤维、VI 分离与图缺陷

对象固定为 \(F(x)=\{x^2\}\) 当 \(x\in[-1,1]\)，域外为空。其完整纤维是
\[
F^{-1}(v)=
\begin{cases}
\{\pm\sqrt v\},&0<v\le1,\\
\{0\},&v=0,\\
\varnothing,&\text{其它 }v.
\end{cases} \tag{GP8}
\]
在 (GP2) 的声明域 \([-1,1]\) 内，quasi 的严格前件使 \(x\ne0,y>x\)，后件由 \(y^2\ge0\) 成立；但 \(x=0,y=-1\) 的 pseudo 前件等于 0，后件为 \(-1<0\)。这直接证明 quasi 而非 pseudo，不需要文献实例认证。

两点差 \(b=(x+y)a\)，故 hypo 缺陷至多 2；取两点趋于左端点 \(-1\) 给锐值 2。取 \(x=0,y=-\varepsilon\) 使斜率 \(m=x+y=-\varepsilon\uparrow0\)，于是 \(ab/b^2=1/m\to-\infty\)，没有有限 cohypo 缺陷。

<a id="gxp-square-subcritical"></a>
## GX-065 的 subcritical 完整近端与 τ

对 \(0<\lambda<1/2\)，\(g_\lambda=x+\lambda x^2\) 在完整域严格增，自然输入域为 \([\lambda-1,\lambda+1]\)。解二次方程得到全部近端纤维：
\[
J_{\lambda F}(p)=
\left\{\frac{-1+\sqrt{1+4\lambda p}}{2\lambda}\right\}
\quad(p\in[\lambda-1,\lambda+1]), \tag{GP9}
\]
域外为空。另一根小于 \(-1\)，因 \(-1/\lambda<-2\) 且两根和为 \(-1/\lambda\)，故没有被遗漏的第二支。C83 的全图线性锐反射模为 \(L=(1+2\lambda)/(1-2\lambda)\)，(GP1) 因而给
\[
\tau^*_\lambda=\frac{2\lambda}{(1-2\lambda)^2}. \tag{GP10}
\]
割线 \(x+y\to-2\) 给下确界锐性；这些是完整有界图和同一步长的参数，不增加全实线 coverage。

<a id="gxp-square-regular-points"></a>
## GX-065 的零目标与普通非零参考点

C84 已证明零目标的固定幂 MSR/SMSR 当且仅当 \(0<q\le1/2\)，端点锐模 1、较低正幂缩窗模下确界 0；普通 MSR/SMSR 失败。负目标纤维为空，故任意双侧目标邻域的 MR/SMR 失败；正目标的小两支 \(\pm\sqrt v\) 又否定零点附近完整逆像的单值性。

若 \(0<|\bar x|<1\)，取只含 \(\bar x\) 同号且避开域端点的开区间 \(U\)。平方映射在 \(U\) 严格单调，其像含 \(\bar v=\bar x^2\) 的开邻域，(GP8) 中唯一落在 \(U\) 的解是同号平方根。导数的连续性和均值定理给 ordinary SMR，缩窗锐模为
\[
\frac1{2|\bar x|}. \tag{GP11}
\]
下界由逆分支导数给出。这只针对非零**内点**，不把域端点偷换成拥有双侧目标 coverage 的参考点。

本页没有新增 PPA 收敛推论：GX-064 的零集仍为空，GX-065 的完整两侧合法路径及留域边界仍以 C84 为准。
