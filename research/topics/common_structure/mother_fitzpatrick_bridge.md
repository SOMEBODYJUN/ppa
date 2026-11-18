# 全图二次移位 Fitzpatrick 面：单调性、正则性与 PPA 的同一母结构

<a id="mother"></a>

## 0. 结论和范围

固定 \(X=\mathbb R^n\)、\(D\subset X\)、\(\Gamma_D=\{(y,v):y\in D,\ v\in F(y)\}\)。母对象是原图的全二次移位 Fitzpatrick 间隙面
\[
\mathfrak M_F^\tau(z,u)
 :=\sup_{(y,v)\in\Gamma_D}
 \left\{\langle z-y,v-u\rangle-\frac{\tau}{2}\|z-y\|^2\right\},
 \qquad \tau\ge0. \tag{M}
\]
上确允许为 \(+\infty\)。这是移位图 \(F+(\tau/2)I\) 的 Fitzpatrick 差，具有独立的图变分意义。

同一 \(M\) 的图截面和零锚截面分别恢复弱单调性和真残差正则性。把两个截面放回同一近端弦，在共同局部化和完整根覆盖下，还能推出输入距离收缩和输入步长界。这个桥不是把 \(\mathsf{Mon}\wedge\mathsf{Reg}\) 改名：零锚截面的反向必须用 PPA 覆盖，而双变量面保留了单个零截面丢掉的方向信息。

<a id="slices"></a>

## 1. 两个截面

### 引理 1（图零值等价于弱单调）

对 \(\beta\ge0\)，以下等价：
\[
\mathfrak M_F^{2\beta}(z,u)=0\quad((z,u)\in\Gamma_D)
\]
以及
\[
\langle v-w,y-z\rangle\ge-\beta\|y-z\|^2
\quad((y,v),(z,w)\in\Gamma_D). \tag{H_mon}
\]

**证明。** 对图上 \((z,u)\)，竞争点自身给 \(0\)，而
\[
\mathfrak M_F^{2\beta}(z,u)
=\sup_{(y,v)\in\Gamma_D}
\{\langle z-y,v-u\rangle-\beta\|z-y\|^2\}.
\]
上确不超过 \(0\) 当且仅当
\(\langle z-y,v-u\rangle\le\beta\|z-y\|^2\)，这正是
\((H_{\rm mon})\)。\(\square\)

### 引理 2（零锚上下界）

假设 \((H_{\rm mon})\)，取 \(a>2\beta\)，并令
\(g_a(z)=\mathfrak M_F^a(z,0)\)。对 \(z\in D\cap\operatorname{dom}F\) 有
\[
0\le g_a(z)\le\frac{r_F(z)^2}{2(a-2\beta)},
\qquad r_F(z)=\inf_{u\in F(z)}\|u\|. \tag{1}
\]
若 \(z=y+\lambda v\)、\((y,v)\in\Gamma_D\)、\(a<2/\lambda\)，则
\[
g_a(z)\ge c_a\|v\|^2,\qquad
c_a=\lambda\left(1-\frac{a\lambda}{2}\right)>0. \tag{2}
\]

**证明。** 任取 \(u\in F(z)\)。弱单调性给
\[
\langle z-y,v-u\rangle\le\beta\|z-y\|^2,
\]
从而
\[
\langle z-y,v\rangle-\frac a2\|z-y\|^2
\le\langle z-y,u\rangle-\frac{a-2\beta}{2}\|z-y\|^2
\le\frac{\|u\|^2}{2(a-2\beta)}.
\]
取上确和下确得 (1)。在 \(M\) 中取竞争点 \((y,v)\)，并用
\(z-y=\lambda v\)，得 (2)。\(\square\)

## 2. 正则性截面的定量桥

对 \(W\subset D\)，\(\mathrm{Cov}_\lambda(W,D)\) 表示每个 \(z\in W\) 至少存在
\((y,v)\in\Gamma_D\) 使 \(z=y+\lambda v\)。若要用于原完整预解式，另要求 FullCov：
每个完整根都存在，所有根的输出都在 \(D\)，且最近输入零锚也在 \(D\)。

### 定理 1（同一母面的增长和真残差）

固定 \(2\beta<a<2/\lambda\)，假设 \((H_{\rm mon})\)。在 \(W\) 上：

* 若 \(g_a(z)\ge\gamma d(z,S)^2\)，则
  \[
  d(z,S)\le K_+r_F(z),\qquad
  K_+=[2\gamma(a-2\beta)]^{-1/2}. \tag{3}
  \]
* 反过来，若 \(d(y,S)\le K r_F(y)\) 在 \(D\) 上成立，且
  \(\mathrm{Cov}_\lambda(W,D)\) 成立，则
  \[
  g_a(z)\ge\gamma_-d(z,S)^2,\qquad
  \gamma_-=\frac{c_a}{(\lambda+K)^2}. \tag{4}
  \]

**证明。** 第一方向把 (1) 与增长合并。第二方向取覆盖根
\(z=y+\lambda v\)，则
\[
d(z,S)\le\lambda\|v\|+d(y,S)
\le\lambda\|v\|+K r_F(y)
\le(\lambda+K)\|v\|.
\]
再用 (2) 即得 (4)。\(\square\)

同一证明对 \(\mathfrak M_F^a(z,\eta)\) 给出变右端的度量正则版本；零问题是 \(\eta=0\) 的截面。若只有一个选中支，(4) 只对该支成立，不能升级成完整 PPA 结论。

## 3. 同一近端弦上的 \(A+B\) 桥

### 定理 2（共同窗口：无损锚输运的窄窗）

设 \(S\) 非空闭，且：

1. \((H_{\rm mon})\) 对所有相关图对以 \(\beta\) 成立；
2. 对所有相关输出 \(y\)，完整真残差满足 \(d(y,S)\le K r_F(y)\)；
3. 每个完整根 \(x=y+\lambda v\) 的输出、某个最近输入零锚
   \(p\in P_S(x)\) 和比较图对都在同一 \(D\) 内；
4. \(\lambda\beta<1/2\) 且 \(\lambda>2\beta K^2\)。

则每个完整根满足
\[
d(y,S)\le\kappa d(x,S),\qquad
\|x-y\|\le d(x,S),\qquad
\kappa=\left(1-2\lambda\beta+\frac{\lambda^2}{K^2}\right)^{-1/2}<1. \tag{5}
\]
当 \(\beta>0\) 时参数窗非空当且仅当 \(2\beta K<1\)；\(\beta=0\) 时任意
\(\lambda>0\) 都允许。

**证明。** 取 \(p\in P_S(x)\)。弱单调性给
\(\langle v,y-p\rangle\ge-\beta\|y-p\|^2\)。于是
\[
\begin{aligned}
d(x,S)^2
&=\|x-p\|^2\\
&\ge(1-2\lambda\beta)\|y-p\|^2+\lambda^2\|v\|^2\\
&\ge(1-2\lambda\beta)d(y,S)^2+
  \frac{\lambda^2}{K^2}d(y,S)^2.
\end{aligned}
\]
这给第一式。由于 \(\lambda\beta<1/2\)，同一展开式给
\(\lambda\|v\|\le d(x,S)\)，即第二式。参数条件使括号严格大于 \(1\)。\(\square\)

若整条轨道留在窗口，则
\[
d(x_k,S)\le\kappa^k d(x_0,S),\qquad
\sum_{k\ge0}\|x_{k+1}-x_k\|
\le\frac{d(x_0,S)}{1-\kappa}. \tag{6}
\]
距离趋零只用 \(A\)；有限长度和点列收敛使用输入版 \(B\) 与几何级数。
一般 \(B\) 则把右端换成 \(\sum_jH(\kappa^jd_0)\)。对非凸、非孤立 \(S\) 只需核对最近输入锚是否留在同一局部图窗；若改用更大的弱单调参数窗，则还需另加 anchor-transport 估计。

这也说明参数门的必要性。\(F=-\beta I\)、\(K=1\) 时，
\(J_{\lambda F}(x)=x/(1-\lambda\beta)\) 在 \(0<\lambda\beta<1\) 扩张，正好落在桥接参数窗之外。

### 定理 2A（共同窗口：一般锚输运）

定理 2 的条件 \(\lambda\beta<1/2\) 是为了在没有额外几何控制时把
\(\|y-p\|^2\) 换成 \(d(y,S)^2\)。可以把这个窄窗替换成一个明确的锚输运假设。
对每个完整根 \(x=y+\lambda v\)，假设存在 \(p\in P_S(x)\) 使
\[
 \|y-p\|\le L\,d(y,S),\qquad L\ge1. \tag{AT}
\]
不再要求 \(\lambda\beta<1/2\)。同一平方展开给出
\[
\begin{aligned}
d(x,S)^2
&=\|y-p+\lambda v\|^2\\
&\ge (1-2\lambda\beta)\|y-p\|^2+\lambda^2\|v\|^2\\
&\ge \left(1-2\lambda\beta L^2+\frac{\lambda^2}{K^2}\right)d(y,S)^2, \tag{5A}\\
d(x,S)^2
&\ge\left(\lambda^2-2\lambda\beta L^2K^2\right)\|v\|^2. \tag{5B}
\end{aligned}
\]
第二行使用 \(\langle v,y-p\rangle\ge-\beta\|y-p\|^2\)，再用
\(d(y,S)\le K\|v\|\)。因此在
\[
\lambda>2\beta L^2K^2 \tag{Gate-AT}
\]
下，所有完整根同时满足
\[
d(y,S)\le\kappa_{\!L}d(x,S),\quad
\kappa_{\!L}:=
\left(1+\frac{\lambda^2}{K^2}-2\lambda\beta L^2\right)^{-1/2}<1,
\tag{6A}
\]
以及输入距离步界
\[
\|x-y\|=\lambda\|v\|
\le h_{\!L}d(x,S),\qquad
h_{\!L}:=\sqrt{\frac{\lambda}{\lambda-2\beta L^2K^2}}. \tag{6B}
\]
当 \(L=1\) 时，(Gate-AT) 正是 \(\lambda>2\beta K^2\)。这给出用户任务中的
临界参数门。对曲零集，\(L\) 是最近锚沿近端弦移动的精确代价。若同一锚同时属于
\(P_S(x)\) 和 \(P_S(y)\)，则 \(L=1\)。有限 reach 管、法向纤维保持或仿射零集的
法向近端通常可直接核验该情形。

若不满足 (AT)，定理 2A 不能由闭性自动补出。\(p\in P_S(x)\) 只给
\(\|y-p\|\ge d(y,S)\)，而在 \(\lambda\beta>1/2\) 时负项
\(-2\lambda\beta\|y-p\|^2\) 需要上界。远端或曲零集的移动锚正是此处的独立
几何退化。

这个缺口有一个局部、完整覆盖的有限图见证。取 \(X=\mathbb R\)、
\(\lambda=2\)、\(\beta=1/2\)、\(K=1\)，令 \(S=\{0,1\}\)，并令闭图为
\[
\Gamma=\{(0,0),(1,0)\}\cup
\{(y,0.4494):0.099\le y\le0.100\}.
\]
分支与 \(1\) 的点对满足
\[
(y-1)0.4494\ge-\tfrac12(1-y)^2
\]
（在 \(y=0.100\) 处仍为严格不等式），与 \(0\) 的点对为正，分支内部的值相同，
所以全图满足 \((H_{\rm mon})\)。分支上
\(d(y,S)\le0.100<0.4494=r_F(y)\)，零点处等式成立，故 \(K=1\) 的真残差
次正则成立。

在 \(U=(0.9980,0.9986)\) 中，每个输入都有完整分支根
\(y=x-0.8988\in(0.0992,0.0998)\)。例如 \(x=0.9984\) 时
\[
d(x,S)=0.0016,\qquad y=0.0996,\qquad d(y,S)=0.0996,\qquad
\|x-y\|=0.8988.
\]
因此即使 \(\lambda>2\beta K^2\)，\(A\) 和任何线性输入步长界都失败。
输入锚 \(p=1\) 满足 \(\|y-p\|=0.9004>9d(y,S)\)，正好显示
\(L>9\) 的锚输运代价。该例保留了全图点对、真残差和局部完整覆盖的量词，
说明缺口来自锚移动，而非选支遗漏。

## 4. 观察复合 \(F(y)=B(y)T(Cy)\)

设 \(C:X\to Z=\mathbb R^m\) 满射，\(T:Z\rightrightarrows Z\) 最大单调，
\(Z_0=T^{-1}(0)\ne\varnothing\)，且对完整活跃纤维的全部 \(w\in T(Cy)\)：
\[
b_-\|w\|\le\|B(y)w\|\le b_+\|w\|. \tag{7}
\]
令 \(c_-=\sigma_{\min}(C)>0\)、\(c_+=\|C\|\)，\(F(y)=B(y)T(Cy)\) 为完整像集。

### 命题 3（完整纤维和零集传递）

\[
S=F^{-1}(0)=C^{-1}(Z_0),\qquad
b_-r_T(Cy)\le r_F(y)\le b_+r_T(Cy), \tag{8}
\]
并且
\[
c_+^{-1}d_T(Cy,Z_0)\le d(y,S)\le c_-^{-1}d_T(Cy,Z_0). \tag{9}
\]
因此，对任意 \(q>0\)，
\[
d_T(z,Z_0)\le K_T r_T(z)^q
\Longrightarrow
d(y,S)\le c_-^{-1}K_Tb_-^{-q}r_F(y)^q, \tag{10}
\]
反向为
\[
d(y,S)\le K_Fr_F(y)^q
\Longrightarrow
d_T(Cy,Z_0)\le c_+K_Fb_+^q r_T(Cy)^q. \tag{11}
\]

**证明。** (8) 逐纤维使用 \(B\) 的上下界。对 (9)，用满射右逆
\(C^\dagger\)：给定 \(s\in Z_0\)，
\(y'=y+C^\dagger(s-Cy)\) 满足
\(\|y-y'\|\le c_-^{-1}\|Cy-s\|\)；反向不等式由
\(\|C(y-y')\|\le c_+\|y-y'\|\)。组合即可。 \(\square\)

### 命题 4（同一近端弦的 \(CB(y)\) 定向功）

记 \(Q_y=CB(y)\)，并假设
\[
\operatorname{sym}Q_y\succeq\mu I,\qquad
\|Q_y\|\le q_+,\qquad \mu>0. \tag{12}
\]
若 \(x=y+\lambda B(y)w\)、\(w\in T(Cy)\)，则
\[
\langle w,Cx-Cy\rangle
=\lambda\langle w,Q_yw\rangle\ge\lambda\mu\|w\|^2. \tag{13}
\]
对参考图母面 \(M_T\)，若 \(a\lambda q_+^2/2<\mu\)，则
\[
\mathfrak M_T^a(Cx,0)
\ge\lambda\left(\mu-\frac{a\lambda q_+^2}{2}\right)\|w\|^2. \tag{14}
\]
若 \(d_T(Cy,Z_0)\le K_T\|w\|\) 且所有根覆盖，则
\[
\mathfrak M_T^a(Cx,0)
\ge
\frac{c_-^2\lambda(\mu-a\lambda q_+^2/2)}
{(K_T+\lambda q_+)^2}\,d(x,S)^2. \tag{15}
\]

**证明。** (13) 由 \(Cx-Cy=\lambda Q_yw\)。在 \(M_T\) 中取竞争图点
\((Cy,w)\)，得
\[
\mathfrak M_T^a(Cx,0)
\ge\lambda\langle Q_yw,w\rangle-\frac{a\lambda^2}{2}\|Q_yw\|^2,
\]
即 (14)。又
\(d_T(Cx,Z_0)\le(K_T+\lambda q_+)\|w\|\)，而
\(d_T(Cx,Z_0)\ge c_-d(x,S)\)，故 (15)。\(\square\)

若 \(B(y)=b(y)C^\top\)、\(b(y)\in[b_-,b_+]\)，则
\(Q_y=b(y)CC^\top\)，正功门自动成立；常数 \(b\) 时
\(F=bC^\top TC\) 保持参考图单调性。若 \(b\) 仅 Lipschitz 且活跃 \(w\) 有界于 \(W\)，则
\[
\langle F(y)-F(y'),y-y'\rangle
\ge-L_b c_+W\|y-y'\|^2. \tag{16}
\]
一般 \(B\) 的上下界本身不传递单调性。一个可检验的补充是
\[
\left|\langle B(y)w-B(y')w',y-y'\rangle
-\langle w-w',C(y-y')\rangle\right|
\le\delta\|y-y'\|^2, \tag{17}
\]
它把参考图的单调性传成原图的 \(\delta\)-弱单调性；(12) 与 (17) 是不同义务。

令 \(C=B=I\) 恢复参考图。取 \(T=J\) 为二维九十度旋转时，
\(T\) 最大单调但非势，且
\(\mathfrak M_T^a(z,0)=\|z\|^2/(2a)\)，原 PPA 因
\(\|(I+\lambda J)y\|^2=(1+\lambda^2)\|y\|^2\) 收缩。这个自然见证说明母面不依赖势函数。

同一障碍还可精确嵌入 C314 四周期。取 \(X=\mathbb R^2\)、\(C=I\)、\(T=I\)，令
\(Q\) 为九十度旋转并 \(B=Q^\top-I\)。则 \(B\) 可逆、
\(\|Bw\|=\sqrt2\|w\|\)，零集仍为 \(\{0\}\)，而
\(I+B=Q^\top\)，所以 \(\lambda=1\) 的完整 PPA 是四周期 \(J_F=Q\)。
对任意图差分 \(\Delta y,\Delta v\) 有 \(\Delta y+\Delta v=Q^\top\Delta y\)、\(\|\Delta y+\Delta v\|=\|\Delta y\|\)，且 \(\|\Delta y-\Delta v\|=\sqrt5\|\Delta y\|\)，所以该图还满足精确的 RL\((1,1,\sqrt5)\)。
参考图 \(T=I\) 的面在 \(Cx\) 上仍是同一个
\(\mathfrak M_T^a(Cx,0)\)（例如 \(a=1\) 时为 \(\|x\|^2/6\)），
零集和纤维范数传递也与正例相同；但
\(\operatorname{sym}(CB)=-I\)，近端弦正功为负。这说明双变量参考面若不带入
\(CB\) 的方向信息，仍不能排除原空间周期轨道。

## 5. 同一对象的比较和边界

| \(M\) 的截面或附加门 | 参数/前提 | 结论 | 量词限制 |
|---|---|---|---|
| \(\mathfrak M^{2\beta}|_{\Gamma_D}=0\) | 完整图，\(\beta\ge0\) | \(\beta\)-弱单调 | 完整图块 |
| \(g_a\le r_F^2/[2(a-2\beta)]\) | \(a>2\beta\) | 间隙上界 | 不给根存在 |
| \(g_a\ge\gamma d^2\) | 二次增长 | 真残差 EB | 不需覆盖 |
| EB \(\Rightarrow g_a\ge c_ad^2/(\lambda+K)^2\) | EB + Cov，\(a<2/\lambda\) | 正则性变增长 | FullCov 才能覆盖所有输出 |
| \(\widetilde g_a=\sqrt{g_a}\) | \(2\beta<a<2/\lambda\)，增长 \(\widetilde g_a\ge\gamma d^2\) | 精确给 \(d^2\lesssim r_F\)；反向需 FullCov 与图值帽 | 对应 C331，临界曲率仍需方向门 |
| 两截面 + 近端弦（定理 2） | FullCov、\(\lambda\beta<1/2\)、\(\lambda>2\beta K^2\) | \(A+B\)、点收敛、有限长度 | 窄窗用正系数直接比较 |
| 两截面 + 近端弦（定理 2A） | FullCov、(AT) \(\|y-p\|\le Ld(y,S)\)、\(\lambda>2\beta L^2K^2\) | \(A+B\)，\(\kappa_L,h_L\) 显式 | 非凸非孤立目标要逐根核锚输运 |
| 观察复合 | (7)、(12) 或 (17) | 零集/残差传递和 \(CB(y)\) 正功 | 上下界本身不传递单调性 |

仅保留 \(g_a\) 不能识别动力学：已有两个完整图具有相同的零残差切片
\(g_1(s,n,h)=n^2/6+\|h\|^2/2\)，但法向近端倍率分别为 \(1/2\) 和 \(3/2\)。
若 \(\sigma_{\min}(C)=0\)、\(b_-=0\) 或
\(\operatorname{sym}(CB(y))\) 无正下界，传递常数或正功消失；这是可检测的退化判据，
也解释了只保留 C322 通信谱而丢掉位置输运的失败。\(F=-\beta I\) 是参数窗失败的最小见证。


还有一个临界边界不需要 reach：当 value-weighted 曲率系数为零，即完整图单调\(\beta=0\)，普通 PPA 对任意非空闭零集都满足 firm Fejér 恒等式
\[
\|x_{k+1}-p\|^2+\|x_k-x_{k+1}\|^2\le\|x_k-p\|^2,\qquad p\in S.
\]
所以每条完整轨道距离趋零、步长平方可和；有限维的聚点和闭图再给点列收敛。\(q=2\) 误差界在这条单调边界上只负责把距离和真残差接起来，不是点收敛的必要机制。

## 6. 唯一保留的下一义务

本页闭合了一个非势、可多值、非孤立零集的局部 \(A+B\) 子类，但没有闭合
\(q=2,\alpha=1\) 的最大临界类。下一义务固定为：在
\[
d(y,S)^2\le K_{\rm EB}r_F(y),\qquad 2CK_{\rm EB}<\lambda
\]
的全对亏损、完整根覆盖和共同留域下，判断严格平方余额是否足以排除
“距离趋零而点列不收敛”。反例必须保留同一常数和所有根量词；正面证明只需补
从平方耗散到切向 Cauchy 模的独立估计。当前母面结果不把临界平台候选升级为定理。

**状态**：本页引理、定理、命题及反例为本轮独立推导；外部先行性及一般
\(B(y)\) 的方向传递仍待逐式对比。
