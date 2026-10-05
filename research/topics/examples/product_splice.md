# 负平方与符号阶梯的完整乘积：全图锐模与图窗边界

本卡固定 C112–C114 的完整关系、残差、全图与图窗量词。所有结论直接从下列完整关系推导；不调用外部定理，也不把图邻域、仅限输入的窗口和完整乘积互换。

<a id="gx057-object"></a>
## 1. 完整对象、逆像和真残差

固定 \(0<\delta<1/2\)，采用 \(H=\mathbb R^2\) 的 Euclidean 范数。令
\[
A(x)=\begin{cases}\{-x^2\},&0\le x\le1/2,\\
\varnothing,&\text{其余 }x,
\end{cases}
\qquad
B(t)=\begin{cases}
\{0\},&t=0,\\
\{\operatorname{sgn}(t)c(t)\},&0<|t|<\delta,\\
\varnothing,&\text{其余 }t,
\end{cases}
\tag{P1}
\]
其中 \(c(t)=1\) 对有理数，\(c(t)=2\) 对无理数。完整乘积为
\[
F(x,t)=A(x)\times B(t),\qquad
\operatorname{dom}F=[0,1/2]\times(-\delta,\delta),\qquad
\operatorname{zer}F=\{(0,0)\}=:S.
\tag{P2}
\]
它在其域上单值。完整逆像是 \(F^{-1}(\alpha,\beta)=A^{-1}(\alpha)\times B^{-1}(\beta)\)，其中
\[
A^{-1}(\alpha)=\begin{cases}\{\sqrt{-\alpha}\},&-1/4\le\alpha\le0,\\
\varnothing,&\text{其余 }\alpha,
\end{cases}
\]
且 \(B^{-1}(0)=\{0\}\)；\(B^{-1}(\sigma)\) 是符号为 \(\sigma\in\{-1,1\}\) 的非零有理半区间，\(B^{-1}(2\sigma)\) 是同符号的无理半区间，其余逆像为空。因此
\[
\operatorname{ran}F=[-1/4,0]\times\{0,\pm1,\pm2\}.
\tag{P3}
\]
完整图不是闭图：固定第一坐标，对同一输出 1 的有理正输入趋近无理正输入即可。第二输出满足 \(|v_2|<1\) 的图点却只能有 \(t=0,v_2=0\)；所以在任意 \(((x,0),(-x^2,0))\) 附近存在闭的局部图块。

原关系的**全纤维**零残差，域外约定为 \(+\infty\)，是
\[
r_F(x,t)=\begin{cases}
x^2,&t=0,\ 0\le x\le1/2,\\
\sqrt{x^4+c(t)^2},&0<|t|<\delta,\ 0\le x\le1/2,\\
+\infty,&(x,t)\notin\operatorname{dom}F,
\end{cases}
\quad
d((x,t),S)=\sqrt{x^2+t^2}.
\tag{P4}
\]

<a id="gx057-zero-eb"></a>
## 2. 固定零目标：锐半阶与目标窗口障碍

在整个有限纤维域上都有
\[
d((x,t),S)\le r_F(x,t)^{1/2}.
\tag{P5}
\]
当 \(t=0\) 时是恒等式 \(x=(x^2)^{1/2}\)。当 \(t\ne0\) 时，左侧小于 \(\sqrt{1/4+\delta^2}<1\)，右侧至少为 1。因此半阶的最小全域系数及零点的最小局部系数都恰为 1。

对固定零目标，最大的局部残差指数是 \(q_*=1/2\)。若 \(q>1/2\)，沿 \((x,0)\to(0,0)\) 有
\[
\frac{d((x,0),S)}{r_F(x,0)^q}=x^{1-2q}\longrightarrow+\infty.
\]
若 \(0<q<1/2\)，在 \(\|(x,t)\|\le\varepsilon\) 内，轴上比值至多 \(\varepsilon^{1-2q}\)，轴外比值至多 \(\varepsilon\)。缩窗系数下确界为 0。零点是孤立逆点，故这些固定目标 MSR 和 SMSR 的结论相同。

任意幂的双侧目标 MR/SMR 在零点都失败。例如任意小的 \((\alpha,0)\) 且 \(\alpha>0\) 没有逆像，而 \(r_{F-(\alpha,0)}(0,0)=\alpha<\infty\)。第二目标坐标的任何充分小非零值也没有逆像。

零目标的锐点是 \((0,0)\)，与后面的临界 RL 锐点 \((1/2,0)\) 不同。在临界图点，以目标 \((-1/4,0)\) 定义固定目标残差，轴上是
\[
r_{F-(-1/4,0)}(x,0)=(1/2-x)(1/2+x).
\]
因此该目标的最大局部固定目标指数是 1，线性系数下确界为 1；轴外输出跳跃不改变此值。它不是零目标的半阶命题。

<a id="gx057-complete-resolvent"></a>
## 3. 任意步长的完整近端纤维

固定 \(\lambda>0\)。令 \(g_\lambda(x)=x-\lambda x^2\)，并记
\[
D_{A,\lambda}=g_\lambda([0,1/2])=
\begin{cases}
[0,(2-\lambda)/4],&0<\lambda\le1,\\
[\min\{0,(2-\lambda)/4\},1/(4\lambda)],&\lambda>1.
\end{cases}
\tag{P6}
\]
完整第一纤维为
\[
J_{\lambda A}(p)=
\left\{\frac{1\pm\sqrt{1-4\lambda p}}{2\lambda}\right\}\cap[0,1/2],
\qquad p\in D_{A,\lambda},
\tag{P7}
\]
重合根只计一次。它在 \(0<\lambda\le1\) 单值；\(\lambda>1\) 时必须保留全部合法根。特别地，\(J_{\lambda A}(0)=\{0\}\) 对 \(\lambda<2\)，而 \(J_{\lambda A}(0)=\{0,1/\lambda\}\) 对 \(\lambda\ge2\)。

第二坐标的自然域为五个算术簇的并：
\[
D_{B,\lambda}=\{0\}\cup
\bigcup_{\sigma=\pm1}
\left[\sigma\bigl(\lambda+(\mathbb Q\cap(0,\delta))\bigr)
\ \cup\
\sigma\bigl(2\lambda+((\mathbb R\setminus\mathbb Q)\cap(0,\delta))\bigr)\right].
\tag{P8}
\]
对每个 \(p\)，完整纤维包括 \(p-\sigma k\lambda\) 的**全部**合法候选：\(k=1\) 要求该候选有理、符号为 \(\sigma\) 且绝对值在 \((0,\delta)\)；\(k=2\) 要求无理及相同符号、范围。另有 \(J_{\lambda B}(0)=\{0\}\)。

当 \(\lambda\ge\delta\) 时，两个同号几何簇不相交，故第二纤维单值。当 \(0<\lambda<\delta\) 时，第二纤维出现两个元素**当且仅当 \(\lambda\) 无理**：碰撞必须满足
\[
t_{\rm rat}+\lambda=t_{\rm irr}+2\lambda,
\qquad t_{\rm rat}-t_{\rm irr}=\lambda.
\tag{P9}
\]
有理 \(\lambda\) 不可能等于有理数减无理数；无理 \(\lambda\) 时选 \(t_{\rm rat}\in\mathbb Q\cap(\lambda,\delta)\)，再取 \(t_{\rm irr}=t_{\rm rat}-\lambda\)，即有合法正侧碰撞。负侧同理。

完整乘积始终满足集合恒等式
\[
D_\lambda=D_{A,\lambda}\times D_{B,\lambda},\quad
J_{\lambda F}(p_1,p_2)=J_{\lambda A}(p_1)\times J_{\lambda B}(p_2),\quad
R_{\lambda F}(p)=\{2z-p:z\in J_{\lambda F}(p)\}.
\tag{P10}
\]
该恒等式不以单值性为前提。\(D_\lambda\) 外没有完整近端值；不可自行补上连续分支。
因此完整 \(J_{\lambda F}\) 在其自然域单值，当且仅当
\(\lambda\le1\ \text{且}\ (\lambda\ge\delta\ \text{或}\ \lambda\in\mathbb Q)\)。

<a id="gx057-rl-phase"></a>
## 4. 完整图的成对 RL 相变与不良图几何

取完整图点 \((z,F(z)),(w,F(w))\)，记 \(a=z-w,b=F(z)-F(w)\)，\(s=x+y\in[0,1]\)。第一坐标有
\[
b_1=-sa_1,\quad
\Delta M_{+,1}=(1-\lambda s)a_1,\quad
\Delta M_{-,1}=(1+\lambda s)a_1,
\qquad |a_1|\le\min\{s,1-s\}.
\tag{P11}
\]
第二坐标只有同一符号的不同输出层会使 \(a_2b_2<0\)；这时 \(|b_2|=1\) 且 \(a_2/b_2\in(-\delta,0)\)，下确界 \(-\delta\) 可由有理/无理稠密性逼近。其余 \(b_2\ne0\) 的类型都有 \(a_2/b_2\ge0\)，而 \(b_2=0\) 的反射比值为 1。因此 \(\lambda>\delta\) 时第二坐标的锐线性系数为
\[
L_{B,\lambda,1}^*=\frac{\lambda+\delta}{\lambda-\delta}.
\tag{P12}
\]

由 Euclidean 直积的逐坐标平方和，并以另一坐标固定取得下界，得到完整相变：

| 步长 | 全图最大 RL 指数 | 锐线性系数或失败机制 |
| --- | --- | --- |
| \(0<\lambda\le\delta\) | 无任何正指数 | 阶梯中 \(\Delta M_+\to0\)，\(\|\Delta M_-\|\to2\lambda>0\) |
| \(\delta<\lambda<1\) | 1 | \(L_{\lambda,1}^*=\max\{(1+\lambda)/(1-\lambda),(\lambda+\delta)/(\lambda-\delta)\}\) |
| \(\lambda=1\) | \(1/2\) | 第一坐标的端点二次平坦；完整乘积的锐半阶常数见 §5 |
| \(\lambda>1\) | 无任何正指数 | 第一坐标的精确 Minty 碰撞 |

这里 RL 表示 \(\|a-\lambda b\|\le L\|a+\lambda b\|^\gamma\) 对所有完整图点对成立。对第一行，\(\lambda<\delta\) 可在正半区间内选有理和无理输入差趋于 \(\lambda\)；\(\lambda=\delta\) 则令有理输入趋于 \(\delta\)、无理输入趋于 0。即使 \(\lambda\) 有理、完整纤维仍单值，任意原点连续的消失模也失败。对末行，在 \(x_*=1/(2\lambda)\) 两侧选 \(x_*\pm h\)，第一 Minty 输入相同而反射输出不同，第二坐标固定为 0 即可。

在 \(\delta<\lambda<1\)，锐 LT 非负违反系数为
\[
\tau_\lambda^*=
\max\left\{\frac{\lambda}{(1-\lambda)^2},
\frac{\lambda\delta}{(\lambda-\delta)^2}\right\}
=\frac{(L_{\lambda,1}^*)^2-1}{4}.
\tag{P13}
\]
两支在 \(\lambda=\sqrt\delta\) 相等；这是该区间的最优线性步长，给 \(L_*=(1+\sqrt\delta)/(1-\sqrt\delta)\)。自然域及反射像有界，所以在线性区间每个 \(0<\gamma<1\) 也有有限系数；在临界步每个 \(0<\gamma<1/2\) 也有有限系数。较低指数只是有界域上的继承。

全图没有有限 hypomonotonicity 系数：固定第一坐标，选正侧有理 \(t_n\) 和无理 \(v_n\)，使 \(t_n-v_n\downarrow0\) 且输出差为 \(-1\)，则 \(\langle a,b\rangle/\|a\|^2\to-\infty\)。全图也没有有限 cohypomonotonicity 系数：第二坐标固定为 0，第一坐标用 \(x=h,y=0\)，得到 \(\langle a,b\rangle/\|b\|^2=-1/h\to-\infty\)。这两个机制属于不同坐标。

仅令两个**输入**趋于同一 \((\bar x,0)\) 时，第一阶商的精确下极限为
\[
\liminf_{\substack{z,w\in\operatorname{dom}F,\\z,w\to(\bar x,0),\ z\ne w}}
\frac{\langle z-w,F(z)-F(w)\rangle}{\|z-w\|}=-1.
\tag{P14}
\]
负的阶梯项至少为 \(-|a_2|\)，第一项除以 \(\|a\|\) 后趋于 0；上面的有理/无理序列给锐性。若同时要求输出趋于 \((-\bar x^2,0)\)，阶梯点已被排除，商的下极限变为 0。本文仅核这两个打印出的公式，不授予未核历史名称。
若固定一个输入端点为 \((\bar x,0)\)，其商的下极限也为 0：阶梯贡献为 \(|t|c(t)\ge0\)，第一坐标的负贡献除以输入距离后趋于 0，且沿 \(t=0\) 逼近给出等号。

<a id="gx057-sharp-product-half"></a>
## 5. 临界步的完整乘积锐半阶常数

在 \(\lambda=1\)，第一坐标满足
\[
|\Delta M_{-,1}|^2\le4|\Delta M_{+,1}|,
\]
所以半阶至少有限，且固定第二坐标为 0、取 \(x=1/2,y\uparrow1/2\) 给最大指数 \(1/2\)。但**完整乘积的锐系数严格大于 2**。

下面给其精确一变量表示。令
\[
K_0=\frac{265}{4\sqrt{257}},\qquad
c_\delta=(1+\delta)^2,\quad d_\delta=(1-\delta)^2,
\]
\[
H_\delta(h)=
\frac{c_\delta+h^2(2-h)^2}{\sqrt{d_\delta+h^4}},
\qquad 0\le h\le1/2.
\]
则完整乘积的锐半阶系数是
\[
\boxed{(L_{1,1/2}^{\rm full})^2
=\max\left\{K_0,\ \max_{0\le h\le1/2}H_\delta(h)\right\}.}
\tag{P15}
\]
尤其 \(L_{1,1/2}^{\rm full}\ge\sqrt{K_0}>2\)。极限常数 \(\sqrt{K_0}\) 约为 2.03287；该数字仅帮助阅读，(P15) 是精确式。

**证明。** 写 \(A=|\Delta M_{-,1}|^2,B=|\Delta M_{+,1}|^2\)。平方后的半阶比值为
\[
\frac{A+|\Delta M_{-,2}|^2}{\sqrt{B+|\Delta M_{+,2}|^2}}.
\tag{P16}
\]
第二坐标各类型的闭包上：

1. 同输出时 \(d_2=r_2=|a_2|<\delta\)。令 \(D=\sqrt B\le1/4\)，则 \(A\le4D\) 且
   \((4D+d_2^2)^2\le16(D^2+d_2^2)\)，因为 \(8D+d_2^2<16\)。故这一类比值至多 4。
2. 同符号不同层时，\(d_2=1+t,r_2=1-t\)，\(-\delta\le t\le\delta\)；(P16) 随 \(t\) 严格下降，故上确界在 \((d_2,r_2)=(1-\delta,1+\delta)\)。有理输入趋于 \(\delta\)、无理输入趋于 0 给该极限。
3. 与零点比较或跨符号比较时，\(d_2=k+u,r_2=k-u\)，\(k\in\{1,2,3,4\}\)，\(u\ge0\) 且 \(u<k\)。固定 \(k\) 时 (P16) 随 \(u\) 下降；令 \(u\downarrow0\) 后，其值随 \(k\) 增加，因为 \(A\le9/16<1\)。因此仅须保留 \((d_2,r_2)=(4,4)\)，由正负无理输入趋于 0 给出。

对这两个剩余第二坐标极限，固定 \(s=x+y\) 后令 \(z=|x-y|^2\)，比值是 \((\alpha z+c)/\sqrt{\beta z+d}\)，其中 \(\alpha=(1+s)^2,\beta=(1-s)^2\)。导数符号是 \(\alpha\beta z+2\alpha d-\beta c\)，随 \(z\) 非减，故最大值在 \(z=0\) 或 \(z=\min\{s,1-s\}^2\)。当 \(s\le1/2\)，用 \(s'=1-s\) 保持最大合法 \(|x-y|=s\)，分子增大、分母减小。于是只须取 \(x=1/2,y=1/2-h\)，给 \(A=h^2(2-h)^2,B=h^4\)。零差情形已经包含在 \(h=0\)。

第二极限 \((4,4)\) 给函数 \((16+h^2(2-h)^2)/\sqrt{16+h^4}\)，它在 \([0,1/2]\) 递增，端点值是 \(K_0\)。确切地，导数符号为
\(64-96h+16h^2-2h^5+h^6\)，在该区间为正：前两项至少 16，其余项至少 \(-1/16\)。第一极限给 \(H_\delta\)。所有第二坐标极限可在保持第一点对固定时独立逼近，故得到锐性和 (P15)。

若希望免除数值优化，\(H_\delta\) 的唯一最大点也有精确描述。其导数符号是
\[
E_\delta(h)=4d_\delta-6d_\delta h
+(2d_\delta-c_\delta)h^2-2h^5+h^6.
\tag{P17}
\]
在 \([0,1/2]\) 上 \(E_\delta\) 严格下降：当 \(2d_\delta-c_\delta>0\)，
\(E_\delta'(h)\le-4d_\delta-c_\delta-(10-6h)h^4<0\)；该项非正时更直接。因 \(E_\delta(0)>0\)，最大点为 \(h_\delta=1/2\) 若
\[
\delta\le\frac{28-\sqrt{399}}{20},
\]
否则是 \((0,1/2)\) 内唯一满足 \(E_\delta(h_\delta)=0\) 的根。因而 (P15) 的第二最大值是 \(H_\delta(h_\delta)\)。

<a id="gx057-window-separation"></a>
## 6. 图邻域与仅限输入的窗口

临界图点为 \((\bar z,\bar v)=((1/2,0),(-1/4,0))\)。只要第二输出窗口为 \(|v_2|<1\)，完整图中第二坐标被强制为 \((t,v_2)=(0,0)\)。第一坐标的任意非退化端点窗口 \(x\in[1/2-\eta,1/2]\) 上都有锐半阶系数 **2**：
\[
\frac{|a_1- b_1|^2}{|a_1+b_1|}
=\frac{|a_1|(1+s)^2}{1-s}\le4,
\]
且 \(x=1/2,y\uparrow1/2\) 逼近 4，同时排除每个 \(\gamma>1/2\)。该图邻域不包含第二坐标的任何非零阶梯输出。

相反，仅限制输入为 \(x\in[1/2-\eta,1/2]\)、\(|t|<\varepsilon\)，保留全部输出，其中 \(\eta,\varepsilon>0\)，则仍有最大指数 \(1/2\)，但每个固定窗口的锐半阶系数**严格大于 2**。选第一点对 \(x=1/2,y=1/2-h\)，\(0<h\le\min\{\eta,1/2\}\)，再令第二输入为正负无理数趋于 0，得到极限
\[
Q_{1,1/2}^2\longrightarrow
\frac{16+(2h-h^2)^2}{\sqrt{16+h^4}}>4.
\tag{P18}
\]
因此固定输入窗口中的模不能直接继承为 2。若同时 \(\eta,\varepsilon\downarrow0\)，这些窗口锐系数的下确界仍为 2：第一差满足 \(A\le4\eta^2,B\le\eta^4\)，第二坐标的两种剩余极限分别趋于 \((1,1)\) 和 \((4,4)\)；§5 的类型分解给上极限 4 的平方系数，第一坐标端点给下界。应区分“固定窗口锐系数”和“缩窗系数下确界”。

在零点，仅限输入的窗口 \(x\in[0,\eta]\)、\(|t|<\varepsilon\)，其中 \(0<\eta<1/2,0<\varepsilon<\delta\)，反而有锐**线性**系数
\[
\max\left\{\frac{1+2\eta}{1-2\eta},
\frac{1+\varepsilon}{1-\varepsilon}\right\},
\tag{P19}
\]
由 (P11) 和 (P12) 同样证明；缩窗下确界为 1。零点的图邻域也有线性 RL。全图在 \(\lambda=1\) 的半阶锐性位于另一端点，不能称为零点的局部最优指数。

<a id="gx057-ppa-obstruction"></a>
## 7. 完整近端的路径障碍

令合法固定步路径为 \(p_{k+1}\in J_{\lambda F}(p_k)\)，每步均要求 \(p_k\in D_\lambda\)。对任意固定 \(\lambda>0\)，**每条从非零初值出发的合法路径都只能有有限多个成功步**。

若某一步第一坐标为正，则
\[
p_{k,1}=p_{k+1,1}-\lambda p_{k+1,1}^2,
\qquad p_{k+1,1}>p_{k,1}>0.
\tag{P20}
\]
无限合法时，第一坐标有界递增，极限 \(\ell>0\)；传入等式得 \(\lambda\ell^2=0\)，矛盾。初始第一坐标若为负，自然域要求 \(\lambda>2\)；(P7) 的负根被舍去，唯一合法正根满足
\[
p_{1,1}>1/\lambda>1/(4\lambda)=\max D_{A,\lambda}.
\]
所以第一坐标在一次成功步后即离开自然域，没有第二步。初始第一坐标为 0 时，可一直选择 0；若 \(\lambda\ge2\) 选择远根 \(1/\lambda\)，该远根也大于 \(\max D_{A,\lambda}\)，下一步立即失败。

若第二坐标非零，合法输出与输入同号，且
\[
|p_{k,2}|=|p_{k+1,2}|+\lambda c(p_{k+1,2})
\ge|p_{k+1,2}|+\lambda.
\tag{P21}
\]
非零输入不可能近端到 0，因为 \(J_{\lambda B}(p)\ni0\) 当且仅当 \(p=0\)。因此连续成功步的数量有限。两者合起来，唯一无限合法路径是恒零路径；从零出发选择远根的有限分支仍须保留。

在审查的临界步 \(\lambda=1\)，这两个断点尤为直接：\(D_{A,1}=[0,1/4]\)，正第一坐标有限步离开它；\(D_{B,1}\cap(-\delta,\delta)=\{0\}\)，非零第二坐标在一次成功近端后立刻离开第二自然域。域内非零第二坐标甚至没有第一步。每个合法步仍满足
\[
r_F(p_{k+1})=\|p_k-p_{k+1}\|/\lambda,
\]
因为原关系单值；真正缺失的是下一步的完整纤维和留域。

粗幂界也不满足线性收缩兼容：零目标 EB 的任何有效连续 gauge 对小 \(s\) 都须至少为 \(\sqrt s\)。在 \(\lambda=1\)，半阶 RL 的正系数 \(L\) 给兼容测试的残差上界
\(a(r)=(r+Lr^{1/2})/2\)，所以
\[
\psi(a(r))\ge\sqrt{a(r)}\ge\sqrt{L/2}\,r^{1/4}.
\]
它不能被固定 \(\kappa r\) 支配。实际有限步越域已经独立证明了算法障碍，不以该充分条件的失败代替路径论证。

<a id="gx057-source-review"></a>
## 8. 来源逐项裁决与剩余义务

精确来源是
`history/sources/次单调论文研究/RL_monotonicity_regularity_research_checkpoint_2026-09-01.zip!/work/c_gx053_065.md`。
另一个 ZIP `history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip` 有字节相同的成员；两者成员 SHA-256 都是
`55df53d130f510c873e2a9d4c4afec9b32eb1930811ad458348088ed452748f4`。

| 原成员行号 | 单元 | 本次裁决 |
| --- | --- | --- |
| 49–64、69–150 | GX-053 对象、两坐标及残差 | 第一坐标从 (P1) 独立推导后，与现行 `bounded_negative_square.md` 的 C100/C101 比较，相符；其余历史名称未纳入 |
| 312–326 | GX-056 对象和图闭性 | 第二坐标直接用 (P1) 定义；全图非闭及零输出附近隔离均已证 |
| 346–374 | GX-056 RL 与近端 | 锐线性系数相符；补足所有 \(\lambda\le\delta\) 的消失模障碍及完整纤维的有理/无理碰撞条件 |
| 388–399 | GX-057 乘积、逆像和近端 | 乘积恒等式保持；单值性必须按步长/算术条件分别声明，不能全参数默授 |
| 400–414 | 图几何和第一阶商 | 全图两种有限模失败保持；第一阶商的输入极限与完整图点极限由 (P14) 分开 |
| 416–423 | 临界图邻域和仅限输入窗口 | 图邻域的锐模 2 保持；固定输入窗口的模严格大于 2 已证，缩窗下确界另为 2；完整乘积锐模见 (P15) |
| 425–440 | 真零残差和 MSR/SMSR | 半阶及系数 1 保持，并加强为整个有限纤维域的 (P5)；双侧目标失败给出显式空逆像 |
| 442–444 | 历史候选裁决 | 本稿只以上面的独立证明接纳具体单元，未接纳任何全局研究评级 |

**数学义务。** 本稿范围内的对象、全纤维、残差、指数、线性锐模、完整半阶锐模和固定步路径已给出封闭证明，没有依赖未核外部定理。外部先行性、历史 Spingarn 命名、非固定步算法、图外扩张和任何选择构造不在本稿断言范围；如要研究它们，应先固定新关系/量词另立身份。

**复用边界。** 第一和第二坐标已分别在 [C100/C101](bounded_negative_square.md) 与 [C110/C111](rational_irrational_staircase.md) 重写；本卡仍逐项打印完整乘积的证明，因为直积的全图半阶锐系数、图邻域与仅限输入的窗口不是分量常数的逐项最大。外部先行性与历史命名另核。

作者版本的定义与本对象的非闭门另见[Spingarn逐对象匹配](../../canonical/spingarn_author_definitions.md#sp-gx-match)；不把打印商满足与原作者闭关系类成员身份混同。
