# PPA 投稿稿：按口头汇报顺序的两日备讲与逐步推导

本讲义针对本轮附件 `PPA英语投稿.zip`（工作区名称 `02-PPA-.zip`）中的 `PPA_LaTeX`，以源文件的定理名称和公式定位。它是学习与备讲材料，不替换投稿源码，不改变仓库既有 Claim 的数学身份或证据状态。以 2026-11-12 的备讲任务为背景。

学习目标：面对空白纸，能说明每个条件解决什么问题，独立推出关键不等式，并知道结论在哪些附加条件下才能使用。完整例子不列入口头主线；必要的小反例只用于理解假设。

## 先校准六处会影响汇报的说法

1. **编号。** 这个 zip 中，定理 1 是普通 PPA 主定理，推论 2 是幂模推论，定理 2 是线性能量界，GPPA 是定理 3。以下按名称复习。
2. **Luke–Tam 原定理条件。** 正式版 Assumption 2(d)(ii) 为
   $$
   \tau(1+K/\lambda)^2<\tfrac12.
   $$
   这里 $K$ 是原文用 $\rho$ 表示的算子度量次正则常数，$\tau$ 是 $\lambda F$ 的次单调违反量。换成我们的反射常数是 $L^2=1+4\tau$。zip 的 $(K/\lambda)L<1$ **不是这个原文条件**。不要据此比较新旧参数。
3. **恢复旧理论的分支。** 一般模主定理的直接条件 $K(1+L)/(2\lambda)<1$ 不能单独恢复全部 Luke–Tam 情形；例如 $L=1$ 时它还要求 $\lambda>K$。用线性能量分支才能在对应局部假设下覆盖旧参数范围。第 8 节给出正确比较。
4. **弱凸的对象。** Luke–Tam Theorem 1 需要其定义下的局部**极大**次单调性，结论是纤维可表示为弱凸函数的子水平集（与窗口相交）。不能把它缩写成“零集是凸集”，也不能遗漏极大性。weakly convex 的拼写不是 weekly convex。
5. **sharp 的范围。** 平面旋转族的参数必须可实现：$\beta^2\ge0$。附录给出的临界非收敛构造覆盖 $0<\lambda/K\le2$，不是全部正 $\lambda/K$。线性能量充分条件、可行参数上的因子达等、可行临界边界的必要性，应分别陈述。
6. **第四章的准确内容。** 连续回缩给 ENR 结构，不自动给实解析集、光滑流形、唯一最近点或“任意包围边界都能映满零集”。Euler 那一步另需紧光滑无边界流形及全局指数条件；“完整刻画所有零集”的表述超出证明。

这些校准不需要你临时重写整篇文章；汇报应按核实后的数学来讲，并能指出投稿文字对应的修订位置。

## 两个准备日：复习顺序就是汇报顺序

每个学习块分三步：看讲义重建一次；合上材料写一次；用自己的话讲一次。卡住时只查卡住的那一行，再从该段开头重讲。

| 时间块 | 内容 | 离开这个块之前必须能做什么 |
|---|---|---|
| 第一天 0.5 小时 | 第 1 节，PPA/GPPA 与符号 | 从预解式写出图包含；解释真残差 |
| 第一天 1.5 小时 | 第 2 节，Minty 到 Luke–Tam | 写出次单调、almost firm、反射三种形式；列原文假设 |
| 第一天 1.5 小时 | 第 3–4 节，Hölder 到一般模 | 不看材料推出 RL、能量、半和步长以及兼容条件 |
| 第一天 2 小时 | 第 5–6 节，覆盖与普通 PPA 证明 | 按有限前缀归纳证明存在、留域、有限长与点收敛 |
| 第一天 1.5 小时 | 第 7–8 节，推论、参数与 sharp | 算出幂模常数；解释能量耦合为何更好及锐性边界 |
| 第一天 0.5 小时 | 闭卷复述第 1–8 节 | 30–40 分钟讲完前半部，记录真正断掉的三处 |
| 第二天 1.5 小时 | 第 9 节，GPPA | 说明仅换核哪里断了；重新写出四个条件与完整证明 |
| 第二天 1 小时 | 第 10 节，第三章 | 推出 hypo/cohypo/semimonotone 到 RL 的转换 |
| 第二天 1.5 小时 | 第 11 节，连续回缩 | 从统一尾界证明极限映射连续，区分回缩与投影 |
| 第二天 2 小时 | 第 12 节，Euler 与指数 | 会算四个典型空间的 Euler 数；逐项核指数工具条件 |
| 第二天 1.5 小时 | 第 13–14 节，完整彩排 | 先 70–90 分钟完整讲，再针对追问补短板 |
| 第二天 0.5 小时 | 空白纸最终检查 | 默写第 14 节的八组公式；只补仍推不出的内容 |

每两个学习块留休息。表内是有效学习时间，不要求连续坐满。前半天最重要的产出是会推，不是做漂亮幻灯片。

## 1. 先讲算法：到底在迭代什么

**口头开场。** “我们求解 $0\in F(x)$。PPA 把这个包含关系放到下一步点上；GPPA 则把原空间的增量换成核映射的增量。”

固定 $X=\mathbb R^n$、$F:X\rightrightarrows X$、$\lambda>0$。记
$$
S\subset\operatorname{zer}F=\{x:0\in F(x)\},\qquad
d(x)=\operatorname{dist}(x,S),\qquad r_F(y)=\inf_{w\in F(y)}\|w\|.
$$
本轮收敛证明中 $S$ 非空且闭。零集可以不止一个点，甚至不连通；不要预先假设凸性。

$$
y\in J_{\lambda F}(x)=(I+\lambda F)^{-1}(x)
\iff x\in y+\lambda F(y)
\iff (x-y)/\lambda\in F(y).
\tag{1.1}
$$
有核 $v:X\to X$ 时，
$$
y\in J^v_{\lambda F}(x)=(v+\lambda F)^{-1}(v(x))
\iff [v(x)-v(y)]/\lambda\in F(y).
\tag{1.2}
$$
取 $v=I$ 就是普通 PPA。两个**完整**预解式都满足
$$
\operatorname{Fix}J_{\lambda F}=\operatorname{Fix}J^v_{\lambda F}=\operatorname{zer}F,
\tag{1.3}
$$
因为令输入输出同为 $x$，左边的增量都是零。这不要求 $v$ 单射。

注意从 (1.1) 只得到
$$
r_F(y)\le\|x-y\|/\lambda,
\tag{1.4}
$$
因为所选的 $(x-y)/\lambda$ 只是 $F(y)$ 中一个值。集合值算子的“真残差”是整个纤维的 inf，通常不能写等号。

**本节自测。** 给定 $x,y$，从 $x-y\in\lambda F(y)$ 反向写回预解式；解释为何 (1.4) 的不等号方向不能反过来。

## 2. 经典背景：Minty、almost firm、Luke–Tam 与弱凸纤维

### 2.1 Minty 提供哪些东西

单调性为
$$
\langle u-z,u^*-z^*\rangle\ge0\qquad
((u,u^*),(z,z^*)\in\operatorname{gph}F).
$$
极大单调的“极大”是图不能在保持单调性的前提下真扩张。Minty 对应给出：在 Hilbert 空间中，极大单调 $F$ 的 $I+\lambda F$ 满射；预解式全域有定义、单值、牢固非扩张。有限维、有零点时，固定正步长的 PPA 收敛到零点。**一般的线性率还需额外正则性**。

单值性可当场证明。若同一输入 $x$ 有两个输出 $y,z$，则
$$
(x-y)/\lambda\in F(y),\quad(x-z)/\lambda\in F(z),
$$
单调性给 $-\|y-z\|^2/\lambda\ge0$，故 $y=z$。满射性是 Minty 的实质部分，不要把它说成这个两行计算已经证明的结论。

**背景路线只讲每篇解决什么。** Martinet/Rockafellar 建立近端迭代；Leventhal 把度量次正则接入 PPA 的线性率；Li–Mordukhovich 研究 Hölder 次正则下的 PPA；Luke–Thao–Tam 用 almost firm 与误差界作定量迭代分析；Luke–Tam 再把这种映射性质拉回原算子的次单调性。这里只需理解路线，不需两天内补完所有文献证明。

### 2.2 一套坐标统一三种表达

取两个图点并记
$$
a=u-z,\quad b=u^*-z^*,\quad c=a+\lambda b.
$$
它们对应输入差 $c$、输出差 $a$、位移差 $\lambda b$。定义
$$
J=J_{\lambda F},\qquad R=2J-I.
$$
反射输出差是 $a-\lambda b=2a-c$。核心恒等式为
$$
\boxed{\|a-\lambda b\|^2=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle.}
\tag{2.1}
$$
所以单调性等价于 $\|Rx-Rz\|\le\|x-z\|$，也等价于
$$
\|Jx-Jz\|^2+\|(I-J)x-(I-J)z\|^2\le\|x-z\|^2.
\tag{2.2}
$$
所有等价都在相同的已表示图块与输入域上讨论；这些代数等价不自动提供输入覆盖。

### 2.3 Luke–Tam 如何放松它

对缩放后的 $\lambda F$，用违反量 $\tau\ge0$ 写成
$$
\lambda\langle a,b\rangle\ge-\tau\|c\|^2.
\tag{2.3}
$$
由 (2.1) 以及 $\|c\|^2=\|a\|^2+\|\lambda b\|^2+2\lambda\langle a,b\rangle$，得到
$$
\begin{aligned}
\|a\|^2+\|\lambda b\|^2&\le(1+2\tau)\|c\|^2,\\
\|a-\lambda b\|&\le\sqrt{1+4\tau}\,\|c\|.
\end{aligned}
\tag{2.4}
$$
若 almost firm 的定义使用能量违反量 $\varepsilon$，即右边系数 $1+\varepsilon$，则
$$
\varepsilon=2\tau,\qquad L=\sqrt{1+4\tau}=\sqrt{1+2\varepsilon}.
\tag{2.5}
$$
原文 Proposition 4 对其术语下的 almost firm 限定 $\tau<1/2$；纯平方代数本身对任意 $\tau\ge0$ 有效。别把“averaged 参数 $\alpha=1/2$”与 zip 用来表示 $L^2-1$ 的另一个 $\alpha$ 混用；本讲义统一用 $\tau,\varepsilon,L$。

### 2.4 他们的局部收敛定理：先完整列条件

依据正式版 Assumption 2 与 Theorem 2，固定步长 $\lambda$，在共同集合 $D$ 上：

| 原文项目 | 数学内容 | 它解决的问题 |
|---|---|---|
| (a) | $S=\operatorname{zer}F\cap D\ne\varnothing$，且闭 | 有目标、极限可落回目标 |
| (b) | $J_{\lambda F}:D\rightrightarrows D$ 为自映射 | 轨道与目标在共同环境内 |
| (c) | 每个零点附近有算子线性次正则 $d(y,S)\le K r_F(y)$，并有原文的输出落在该邻域的输入集合非空条件 | 残差控制距离，且评价位置正确 |
| (d)(i) | $\lambda F$ 在 $U\times W$ 上极大次单调，违反量 $\tau$ | 能量估计及局部纤维闭性 |
| (d)(ii) | 令 $\bar F=F\cap(W/\lambda)$，有 $U'\subset(I+\lambda\bar F)(U)$ | 输入附近存在被认证的输出 |
| 参数 | $\tau(1+K/\lambda)^2<1/2$ | 距离因子小于 1 |

结论是足够靠近零点、按其局部规则选择的 PPA 轨道 R 线性收敛到零点。讨论“所有选择”时必须保留其局部允许关系，不应改成不受限的完整预解式。

### 2.5 他们说的 weakly convex 到底是什么

按原文约定，$f$ 弱凸是指 $f(x)+\tau\|x\|^2$ 凸；有的教材用 $\rho\|x\|^2/2$，两种常数相差 2。弱凸**函数**的子水平集可以不凸。例如 $-x^2$ 加 $x^2$ 为零函数，但 $\{-x^2\le-1\}$ 有两个分支。

Theorem 1 的机制可以自己推。为避免步长因素，先设 $\lambda=1$，固定窗口 $V\times W$。如果 $F$ 在该窗口极大次单调，则对固定 $v\in V$，
$$
F(v)\cap W=
\bigcap_{(u,u^*)\in\operatorname{gph}F\cap(V\times W)}
\{w\in W:\tau\|u+u^*-v-w\|^2+\langle u-v,u^*-w\rangle\ge0\}.
\tag{2.6}
$$
正向包含直接来自次单调。反向包含：如果候选 $(v,w)$ 与所有已有图点都兼容，加上它仍满足相同条件；极大性迫使它早已在图中。

把右边不等式负号移到左边，作为 $w$ 的函数，其二次项是 $-\tau\|w\|^2$，其余是仿射与常数。加上 $\tau\|w\|^2$ 后变仿射，所以是弱凸函数的子水平集。交换 $F$ 与 $F^{-1}$ 后，同样得到逆纤维及零集的表示。

**你可以这样过渡。** “旧理论的二次表达来自反射映射的 Lipschitz 控制。我先把这个控制换成 Hölder，看看拉回原图后会出现什么。”

## 3. 从反射的 Hölder 控制反推 RL 次单调

保持上一节 $a,b,c$ 的含义，假设
$$
\|a-\lambda b\|\le L\|c\|^\gamma,
\qquad 0<\gamma\le1.
\tag{3.1}
$$
这对应同一图块反射映射的 Hölder 控制。由 (2.1) 平方并移项，
$$
\boxed{\lambda\langle a,b\rangle\ge
\frac{\|c\|^2-L^2\|c\|^{2\gamma}}4.}
\tag{3.2}
$$
这就是幂型 RL 条件。反向把 (3.2) 代回 (2.1)，立即恢复 (3.1)，因此是精确等价而非仅充分条件。

再利用平行四边形恒等式，
$$
\boxed{\|a\|^2+\|\lambda b\|^2
\le\frac{\|c\|^2+L^2\|c\|^{2\gamma}}2.}
\tag{3.3}
$$
它就是口头路线中的“相应的扩张估计”：普通 firm 能量右边是 $\|c\|^2$，现在允许多出非线性违反量。

最后由
$$
a=\tfrac12[c+(a-\lambda b)],\qquad
\lambda b=\tfrac12[c-(a-\lambda b)],
$$
分别用三角不等式，得到
$$
\boxed{\max\{\|a\|,\|\lambda b\|\}\le
\frac{\|c\|+L\|c\|^\gamma}{2}.}
\tag{3.4}
$$
必须分别给两个向量用三角不等式；仅写一个关于范数和的不等式不足以解释半和常数。

**锚定到零点。** 一步 $y\in J_{\lambda F}(x)$，取 $p\in P_S(x)$。代入
$$
a=y-p,\quad\lambda b=x-y,\quad c=x-p,\quad\|c\|=d(x).
\tag{3.5}
$$
于是
$$
\|x-y\|\le B_\gamma(d(x)),\qquad
B_\gamma(t)=\tfrac12(t+Lt^\gamma).
\tag{3.6}
$$
这是第一个真正进入收敛证明的估计。

**量词必须区分。** 全对 RL 是 $\forall$ 两个图点；主定理只要求 $\forall x\,\forall y\in\mathcal J(x)\,\exists p\in P_S(x)$ 有相应零锚不等式。后者足够控制轨道，但不能据此推不同输入间的连续性、唯一性或全对结构。

**术语旁注。** 如果口头所说的“扩张”另指把部分定义的 Hölder 映射延拓到全空间，那是不同问题：全对、全尺度的 Hilbert Hölder 映射可借雪花嵌入与 Kirszbraun 同常数延拓。局部零锚主定理不需要它，普通存在性覆盖也不能用它无条件代替。两天备讲不必展开这一支。

## 4. 先反推收敛需要什么，再把 Hölder 换成一般模

### 4.1 三个不同任务

目标并不是只让 $d(x^k,S)\to0$。沿着一条零线走远，距离始终为零，点仍可不收敛。因此要分别获得：

1. **靠近目标：** $d_{k+1}\le\kappa d_k$，其中 $0<\kappa<1$。
2. **点不再漂移：** $\sum_k\|x^{k+1}-x^k\|<\infty$。
3. **局部条件始终能用：** 输入不离开工作域，并且每一步有允许输出。

### 4.2 用误差界反推兼容条件

广义度量次正则在实际输出上写为
$$
d(y)\le\psi(r_F(y)),
\quad\psi(0)=0,\quad\psi\text{ 非降且在零连续}.
\tag{4.1}
$$
若已知 $\|x-y\|\le B(d(x))$，则
$$
d(y)\le\psi(r_F(y))
\le\psi(\|x-y\|/\lambda)
\le\psi(B(d(x))/\lambda).
\tag{4.2}
$$
要右端不超过 $\kappa d(x)$，自然要求
$$
\boxed{\psi(B(t)/\lambda)\le\kappa t\quad(0<t\le R).}
\tag{4.3}
$$
这就是“倒着分析条件”的核心：条件是为了闭合距离估计而设计的。

### 4.3 为什么改成一般模

刚才真正用到的并不是 $t^\gamma$ 的特殊求导性质，而是它控制反射差。把
$$
Lt^\gamma\quad\text{换成}\quad\omega(t),
$$
其中 $\omega$ 有限、非降、在零连续、$\omega(0)=0$，得到
$$
\begin{aligned}
\|a-\lambda b\|&\le\omega(\delta),\quad\delta=\|c\|,\\
\lambda\langle a,b\rangle&\ge[\delta^2-\omega(\delta)^2]/4,\\
\|a\|^2+\|\lambda b\|^2&\le[\delta^2+\omega(\delta)^2]/2,\\
\max\{\|a\|,\|\lambda b\|\}&\le B(\delta):=[\delta+\omega(\delta)]/2.
\end{aligned}
\tag{4.4}
$$
前三行等价，第四行是它们的推论。在平方能量中替换的是 $L^2t^{2\gamma}\to\omega(t)^2$，不是把一个未平方的模直接塞进去。

### 4.4 一般模为什么还要额外可和

从距离几何衰减和步长上界，只能得到
$$
\|x^{k+1}-x^k\|\le B(\kappa^k d_0).
$$
故需要
$$
\boxed{\Theta(R):=\sum_{j=0}^{\infty}B(\kappa^jR)<\infty.}
\tag{4.5}
$$
连续趋零本身不足以保证该级数收敛。比如零点附近的模 $\omega(t)=1/\log(e/t)$ 沿几何点列大致为 $1/j$，不可和。幂模自动可和，一般模必须显式检查。

由 (4.5) 还能证明 $\Theta(t)\to0$（$t\downarrow0$）：固定有限前缀逐项趋零，尾和被 $\sum B(\kappa^jR)$ 的小尾控制。这里只需模在零连续，不必假装它在所有正点连续。

## 5. 回头解释存在性：覆盖是什么、哪些能直接复用

设 $V$ 是允许输出域，$W$ 是零附近的图值窗，定义
$$
\bar F(y)=F(y)\cap(W/\lambda),\qquad
\mathcal J(x)=J_{\lambda\bar F}(x)\cap V.
$$
那么
$$
x\in(I+\lambda\bar F)(V)
\iff\exists y\in V:\ x-y\in\lambda F(y),\ x-y\in W
\iff\mathcal J(x)\ne\varnothing.
\tag{5.1}
$$
所以覆盖条件
$$
U_R\subset V'\subset(I+\lambda\bar F)(V)
\tag{5.2}
$$
就是一个精确的局部可解性假设。它没有断言输出唯一，也没有断言每个完整预解式输出都在 $V$ 内。

**原文为什么要这些窗口？** 对非单调 $F$，隐式方程可能无解，也可能有远端额外根。$V$ 限定输出，$W$ 限定图值，$V'$ 指定确实被覆盖的输入。各处正则性必须作用在同一条允许关系上。

**能复用什么？** 覆盖与非空的等价解释 (5.1) 不依赖线性或 Hölder；保留同样的覆盖假设即可继续使用。因此不必另造一个“存在性定理”。但对具体算子验证覆盖、或同时缩小输入输出窗口时，仍须论证。Luke–Tam 缩窗还使用其能量估计，不能把全部缩窗过程称为与算子无关的纯点集拓扑事实。

**建议口头改成：** “我们保留相同形式的局部覆盖作为假设；它在新定理中仍只负责产生允许的下一步。接下来要证明的是，选好初值后下一步仍在这个覆盖能继续使用的输入域中。”

## 6. 普通 PPA 主定理：按人的推导顺序完整证明

### 6.1 四条假设与结论

固定非空闭 $S\subset\operatorname{zer}F$、开集 $U$、$R,\bar t>0$，工作域
$U_R=\{x\in U:d(x)\le R\}$。所有条件均针对同一允许关系 $\mathcal J\subset J_{\lambda F}$。

| 条件 | 精确内容 |
|---|---|
| A1 覆盖 | 每个 $x\in U_R$ 有非空 $\mathcal J(x)$，例如 (5.2) |
| A2 零锚 RL | 每个 $x\in U_R$、每个 $y\in\mathcal J(x)$，存在 $p\in P_S(x)$ 使 $\langle y-p,x-y\rangle\ge[d(x)^2-\omega(d(x))^2]/4$ |
| A3 真残差误差界 | 每个实际输出 $y$，若 $r_F(y)\le\bar t$，则 $d(y)\le\psi(r_F(y))$ |
| A4 窗口、兼容、可和 | $B(R)/\lambda\le\bar t$；$\psi(B(t)/\lambda)\le\kappa t$ 对全部 $0<t\le R$；$\Theta(R)<\infty$ |

若初值满足
$$
d_0\le R,\qquad\Theta(d_0)<D_U(x^0):=\operatorname{dist}(x^0,X\setminus U),
\tag{6.1}
$$
则每条允许轨道无限继续、留在 $U_R$、有限长并收敛到 $S\cap U$，且
$$
\begin{aligned}
d_k&\le\kappa^kd_0,\\
\|x^{k+1}-x^k\|&\le B(d_k)\le B(\kappa^kd_0),\\
\sum_{k=0}^\infty\|x^{k+1}-x^k\|&\le\Theta(d_0),\\
\|x^k-x^\infty\|&\le\Theta(d_k)\le\Theta(\kappa^kd_0).
\end{aligned}
\tag{6.2}
$$
注意：共同常数不表示所有选择有相同极限。

### 6.2 第一步：把几何条件翻译成步长

先只处理一个合法输入 $x$，不要假设无限轨道已存在。取 A2 的 $p$，用 (3.5) 与 (4.4) 得
$$
\|x-y\|\le B(d(x)).
\tag{6.3}
$$
$d(x)=0$ 时，$B(0)=0$ 迫使 $y=x$，所以零点被允许关系吸收。

### 6.3 第二步：先核残差窗口，再用正则性

$$
r_F(y)\le\frac{\|x-y\|}{\lambda}
\le\frac{B(d(x))}{\lambda}\le\frac{B(R)}\lambda\le\bar t.
$$
现在才有权调用 A3，于是
$$
\boxed{d(y)\le\psi(r_F(y))\le\psi(B(d(x))/\lambda)\le\kappa d(x).}
\tag{6.4}
$$
误差界在输出 $y$ 上使用，距离锚却是输入 $x$ 的最近零点；二者不要互换。

### 6.4 第三步：有限前缀归纳，防止局部性循环

设 $x^0,\ldots,x^k$ 已构造且均在 $U_R$。A1 给出任意允许的 $x^{k+1}$。只对这个有限前缀应用 (6.3)–(6.4)，得到
$$
d_{k+1}\le\kappa^{k+1}d_0\le R,
$$
以及
$$
\|x^{k+1}-x^0\|
\le\sum_{j=0}^{k}B(\kappa^jd_0)
\le\Theta(d_0)<D_U(x^0).
\tag{6.5}
$$
因此 $x^{k+1}\in U$，结合距离界得到 $x^{k+1}\in U_R$。归纳闭合，轨道才能无限继续。

**不要先假定每步都能用局部条件，写完无限和后再声称留域。** (6.5) 的有限前缀形式正好避免这一循环。

### 6.5 第四步：有限长推出 Cauchy

当 $m>k$ 时，
$$
\|x^m-x^k\|\le\sum_{j=k}^{m-1}B(\kappa^jd_0)
\le\Theta(\kappa^kd_0)\longrightarrow0.
\tag{6.6}
$$
所以序列 Cauchy；$\mathbb R^n$ 完备，存在极限 $x^\infty$。由 $d_k\to0$、距离函数连续及 $S$ 闭，极限属于 $S$。再令 (6.5) 中指标趋无穷，严格预算给极限仍在 $U$。从第 $k$ 步重新求和得到 (6.2) 的 $\Theta(d_k)$ 尾界。

### 6.6 第五步：为何确有一整个初始邻域

给定 $\bar x\in S\cap U$，取 $r_0>0$ 使 $B(\bar x,r_0)\subset U$。若 $x$ 足够靠近 $\bar x$，则
$$
d(x)\le\|x-\bar x\|,\qquad D_U(x)\ge r_0-\|x-\bar x\|.
$$
由 $\Theta(t)\to0$，可选 $\eta<R$ 使 $\eta+\Theta(\eta)<r_0$。这样 $B(\bar x,\eta)$ 中所有初值都满足预算。

这证明的是预算集合**包含一个开邻域**。一般模只在零连续时，不应无证明地把字面集合 $\{\Theta(d)<D_U\}$ 说成开集。

**本节闭卷任务。** 用一张纸，依次写出：半和步长 → 真残差窗口 → 距离收缩 → 有限前缀留域 → 尾和 Cauchy → 闭集落点。每根箭头说出用了哪个假设。

## 7. 推论 2：幂模只需代入，但要理解指数门

令
$$
\omega(t)=Lt^\gamma,\quad\psi(s)=Ks^q,
\qquad L\ge0,\ K>0,\ 0<\gamma\le1,\ q>0.
$$
计算兼容比值：
$$
\frac{\psi(B(t)/\lambda)}t
=\frac{K}{(2\lambda)^q}
\bigl(t^{1-1/q}+Lt^{\gamma-1/q}\bigr)^q.
\tag{7.1}
$$
当 $\gamma q\ge1$ 时，有 $q\ge1$、$1-1/q\ge0$、$\gamma-1/q\ge0$，所以右端非降，最大值在 $R$ 处：
$$
M(R):=\frac{K}{(2\lambda)^q}
\bigl(R^{1-1/q}+LR^{\gamma-1/q}\bigr)^q.
\tag{7.2}
$$
若 $M(R)<1$，取 $\kappa=M(R)$，并核残差窗
$(R+LR^\gamma)/(2\lambda)\le\bar t$，就闭合主定理条件。级数显式为
$$
\boxed{\Theta(t)=\frac{t}{2(1-\kappa)}+
\frac{Lt^\gamma}{2(1-\kappa^\gamma)}.}
\tag{7.3}
$$
距离 Q 线性：$d_k\le\kappa^kd_0$。点误差由 (7.3) 是 R 线性，上界可用 $C\kappa^{\gamma k}$ 表达；不要不加说明地把两者的因子都写成 $\kappa$。

**为什么出现 $\gamma q\ge1$？** 若 $L>0,\gamma<1$，小 $t$ 时 $B(t)\sim Lt^\gamma/2$，兼容比值近似常数乘 $t^{\gamma q-1}$。小于 1 的指数积使这个**直接证书**在零附近爆炸；大于 1 时缩窗可使它小；等于 1 时常数决定成败。这是证书门，不是所有算子实际收敛的必要条件。若 $L=0$，主导项不同，也不能强称 $\gamma q\ge1$ 必要。

**转场。** “幂型只是一般模的直接特例。线性情形还可保留平方能量来减少估计损失，这才是比较旧参数范围的地方。”

## 8. Luke–Tam 对比与 sharp：先能量，再可行性

### 8.1 我们的一步能量耦合

设 $\omega(t)=Lt$、$\psi(s)=Ks$，一步记
$$
d=d(x),\quad e=d(y),\quad s=\|x-y\|,\quad A=\|y-p\|.
$$
零锚能量给
$$
A^2+s^2\le\frac{1+L^2}{2}d^2.
\tag{8.1}
$$
真误差界给 $e\le(K/\lambda)s$，而 $e\le A$。于是
$$
\left(1+\frac{\lambda^2}{K^2}\right)e^2
\le A^2+s^2\le\frac{1+L^2}{2}d^2.
$$
即
$$
\boxed{e\le\rho_Ed,\qquad
\rho_E=\sqrt{\frac{1+L^2}{2(1+\lambda^2/K^2)}}.}
\tag{8.2}
$$
因此充分条件是
$$
\boxed{L^2<1+2\lambda^2/K^2.}
\tag{8.3}
$$
步长仍有 $s\le(1+L)d/2$，也可用 $s\le\sqrt{(1+L^2)/2}\,d$。残差窗应与选择的步长上界一致；有限长及留域证明用几何因子 $\rho_E$ 重做即可。

**这一步为什么更好？** 不先把能量拆成两个互不相干的最坏界，而是把误差界给出的 $s^2\ge(\lambda/K)^2e^2$ 直接加进能量左边，使两个条件在同一步耦合。

### 8.2 旧证明具体在哪里损失

Luke–Tam 先由三角不等式与算子误差界得到
$$
d(x)\le s+d(y)\le(1+K/\lambda)s.
\tag{8.4}
$$
再代入其能量
$e^2+s^2\le(1+2\tau)d^2$，得到
$$
e^2\le\left[1+2\tau-\left(\frac\lambda{\lambda+K}\right)^2\right]d^2.
\tag{8.5}
$$
这正对应原文条件 $\tau(1+K/\lambda)^2<1/2$（正式证明使用略放大的次正则常数保留严格余量）。

令 $t=\lambda/K>0$，$L^2=1+4\tau$。同样 $\tau\ge0$ 的参数表示下：

| 分支 | 小于 1 的充分条件 |
|---|---|
| Luke–Tam 正式版 | $L^2<1+2t^2/(1+t)^2$ |
| 本文半和直接证书 | $L<2t-1$，仅当右端为正才有意义 |
| 本文能量分支 | $L^2<1+2t^2$ |

因为 $(1+t)^2>1$，能量分支的数值范围严格包含原条件；但讨论整个定理的包含，还要对齐输出窗、覆盖、目标集与允许关系。$L=1$ 时能量因子为 $K/\sqrt{K^2+\lambda^2}<1$，无需 $\lambda>K$。这也立即解释半和分支为什么不足以恢复全部旧线性理论。

### 8.3 “只改三个条件”的安全讲法

可以说：“在我们这四项组织方式中，覆盖保留原形式；次单调换成一般模，误差界换成一般模，数值范围换成模兼容与长度可和。”

随后补一句：“此外，原文的全对及极大性在当前轨道定理中被较弱的最近零锚估计和显式闭目标所替代；第四章还会另加预解式的单值连续性。”这样既保留你的叙事，又不隐藏量词改变。

### 8.4 手推旋转族，不用背抽象的 sharp 宣言

记
$$
Q=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
F(y)=\frac{\alpha I+\beta Q}{\lambda}y,
\quad D=(1+\alpha)^2+\beta^2>0.
$$
由于 $Q^T=-Q,Q^TQ=I$，
$$
J_{\lambda F}=\frac{(1+\alpha)I-\beta Q}{D},\quad
S=\{0\},\quad K=\frac\lambda{\sqrt{\alpha^2+\beta^2}},
\tag{8.6}
$$
并有精确反射常数及距离比
$$
L^2=\frac{(1-\alpha)^2+\beta^2}{D},\qquad
\frac{\|Jx\|^2}{\|x\|^2}=\frac1D.
\tag{8.7}
$$
给定 $t=\lambda/K$、$L$，需要同时满足
$$
\alpha^2+\beta^2=t^2,\qquad
L^2(1+2\alpha+t^2)=1-2\alpha+t^2.
$$
解出
$$
\boxed{\alpha=\frac{(1-L^2)(1+t^2)}{2(1+L^2)},\quad
\beta^2=t^2-\alpha^2\ge0.}
\tag{8.8}
$$
在这个可行域内，$D=2(1+t^2)/(1+L^2)$，所以 $1/D=\rho_E^2$：能量因子每一步都达等。

在形式临界边界 $L^2=1+2t^2$，
$$
\alpha=-t^2/2,\quad\beta^2=t^2(1-t^2/4),\quad D=1.
\tag{8.9}
$$
当且仅当 $0<t\le2$ 时可取实 $\beta$。此时 $J$ 是非恒等正交变换，非零轨道范数不变，相邻步长为同一正数，故不收敛；$t=2$ 就是 $J=-I$ 的二周期。$t>2$ 时此构造无实参数，不能拿它证明该范围边界的必要性。

zip 主文里另一个标量叙述 $\alpha\to-1/2^+$ 给的是 $L\to3,t\to1/2$，而此时 (8.3) 的边界是 $L=\sqrt{3/2}$，不是 3。因此它不能承担所写的临界锐性证明；备讲直接使用 (8.6)–(8.9)。

**本节自测。** 为什么等式 $\beta^2\ge0$ 不是可略去的技术条件？怎样证明正交旋转轨道不收敛，而不仅仅说“范数不下降”？

## 9. GPPA：换成核增量以后，哪一根链断了

**口头过渡。** “前面我们用同一个量 $x-y$ 同时控制残差和物理步长。GPPA 中，进入算子的变成 $v(x)-v(y)$，这两个作用分开了。”

### 9.1 先识别三种距离，不能统称残差

$$
\underbrace{d(x,S)}_{\text{物理空间到零集距离}},\quad
\underbrace{\|v(x)-v(y)\|}_{\text{核步长}},\quad
\underbrace{\|x-y\|}_{\text{物理步长}}.
$$
仍有
$$
r_F(y)\le\|v(x)-v(y)\|/\lambda,
\tag{9.1}
$$
但不存在一般的逆向控制 $\|x-y\|\le C\|v(x)-v(y)\|$。非单射核会完全看不见某些方向；即使单射，也需要定量的逆连续性与可和条件。

**只用于自己理解的反模型。** 取 $v(u,z)=(u,0)$、$F(u,z)=(u,0)$。则 $S=\{0\}\times\mathbb R$，GPPA 只规定 $u_{k+1}=u_k/(1+\lambda)$，却允许任意 $z_{k+1}$。核坐标几何收敛、$d(x^k,S)\to0$，而 $z_k$ 可以发散。这说明物理步长桥必须另给；不必把此例纳入你不讲例子的正式主线。

### 9.2 先准确说 Boris 等人的原文做了什么

Le–Mordukhovich–Théra，arXiv:2608.01584v1，Definition 3 引入 adaptive strong monotonicity：对相应图值，
$$
\langle f-g,v(x)-v(z)\rangle\ge\epsilon\|v(x)-v(z)\|^2,
\quad f\in F(x),\ g\in F(z),\ \epsilon>0.
\tag{9.2}
$$
原文 Theorem 2 在 $S\ne\varnothing$、(9.2)、$\operatorname{ran}v\subset\operatorname{ran}(v+\lambda F)$ 下证明核到解锚的距离和核步长线性衰减；再用 $F^{-1}$ 的 R-Lipschitz 条件得到物理空间**到解集的距离**线性趋零。它没有在这些前提下证明任意物理轨道是 Cauchy 列。

自己可以重建其关键能量式：令
$a=v(y)-v(p),\ b=v(x)-v(y)$，其中 $p\in S$。由 GPPA 与 (9.2)，
$$
\langle a,b\rangle\ge\lambda\epsilon\|a\|^2.
$$
所以
$$
\|v(x)-v(p)\|^2=\|a+b\|^2
\ge(1+2\lambda\epsilon)\|a\|^2+\|b\|^2.
\tag{9.3}
$$
核距离因此收缩。$F^{-1}$ 的原文条件在相应窗口给
$d(y,S)\le C\|b\|/\lambda$，故到集合的距离衰减。

**出处边界。** 可以说本工作延续 GPPA 的核空间分析，并补上物理有限长度的接口。不要把自己的 $h$ 条件直接说成该 v1 Theorem 2 已提出或已证明的条件，也不要把其“距离趋零”转述成“点序列收敛”。

### 9.3 推导需要添加什么

取同一个物理最近零锚 $p\in P_S(x)$。先要求核距离有模控制
$$
\delta_v:=\|v(x)-v(p)\|\le a(d(x)).
\tag{9.4}
$$
比如 $v$ 在相关域 Lipschitz 时，$a(t)=L_vt$。核 RL 条件为
$$
\langle v(y)-v(p),v(x)-v(y)\rangle
\ge\frac{\delta_v^2-\omega_v(\delta_v)^2}{4}.
\tag{9.5}
$$
照搬半和代数，得到
$$
\|v(x)-v(y)\|\le
K_v(d(x)),\qquad K_v(t)=\tfrac12[a(t)+\omega_v(a(t))].
\tag{9.6}
$$
再由真残差误差界，若
$$
\psi(K_v(t)/\lambda)\le\kappa t,
\tag{9.7}
$$
就能推出 **物理距离** $d(y)\le\kappa d(x)$。但走到这里仍没有物理步长可和。

于是增加一个在实际允许步上成立的物理条件：
$$
\boxed{\|y-x\|\le h\bigl(d(x),\|v(y)-v(x)\|\bigr),}
\tag{9.8}
$$
其中 $h$ 对两变量分别非降，在 $(0,0)$ 连续，$h(0,0)=0$。定义
$$
H_v(t)=h(t,K_v(t)),\qquad
\Theta_v(t)=\sum_{j=0}^{\infty}H_v(\kappa^jt).
\tag{9.9}
$$
现在物理步长满足 $\|y-x\|\le H_v(d(x))$，证明才重新闭合。

### 9.4 Assumption 2 的四项和 GPPA 定理

| 条件 | 本轮 zip 的精确内容 |
|---|---|
| G1 局部存在 | 每个 $x\in U_R$ 有非空允许 $\mathcal J_v(x)\subset J^v_{\lambda F}(x)$ |
| G2 同锚核 RL | 每个允许步有同一 $p\in P_S(x)$ 同时满足 (9.4)、(9.5) |
| G3 物理位移 | (9.8) 对所有允许步成立 |
| G4 误差界与兼容 | 实际输出的真 $r_F$ 误差界；$K_v(R)/\lambda\le\bar t$；(9.7)；$\Theta_v(R)<\infty$ |

对初值另需
$$
d_0\le R,\qquad\Theta_v(d_0)<D_U(x^0).
\tag{9.10}
$$
结论与普通 PPA 相同地包括无限继续、留域、物理有限长和点收敛；估计为
$$
\begin{aligned}
d_k&\le\kappa^kd_0,\\
\|v(x^{k+1})-v(x^k)\|&\le K_v(\kappa^kd_0),\\
\|x^{k+1}-x^k\|&\le H_v(\kappa^kd_0),\\
\|x^k-x^\infty\|&\le\Theta_v(\kappa^kd_0).
\end{aligned}
\tag{9.11}
$$

**完整证明只有三个新计算和一个旧接口。** (9.5) 给核半和界 (9.6)；(9.1)、残差窗口及 (9.7) 给物理距离收缩；(9.8) 给物理步长界。最后把第 6 节的 $B,\Theta$ 换成 $H_v,\Theta_v$，逐有限前缀归纳，再求尾和。不要省略最后这个替换中的留域预算。

### 9.5 物理条件怎样验证，为什么允许两变量

若有局部逆 Lipschitz 界 $\|x-y\|\le C\|v(x)-v(y)\|$，取 $h(t,s)=Cs$ 即可。若只有逆 Hölder 界，取 $h(t,s)=Cs^\nu$，并核复合模的可和性。若实际算法能证明
$$
\|x-y\|\le c_1d(x)+c_2\|v(x)-v(y)\|,
$$
也可取 $h(t,s)=c_1t+c_2s$。后者只在允许步上约束核看不见的运动，不强迫核全域单射。

零点处 $d=0$，G2 使核增量为零，G3 再使物理增量为零。这个零吸收检查能迅速找出一个所谓物理条件是否太弱。

**退化回 PPA。** $v=I,a(t)=t,\omega_v=\omega,h(t,s)=s$，则 $K_v=H_v=B$、$\Theta_v=\Theta$。如果讲 SPD 预条件核，还需按其自然度量重写配对或用线性共轭逐项核验，不能只说“$M\succ0$，所以所有 Euclidean 条件自动成立”。

## 10. 第三章复习：不同次单调性怎样进入同一 RL 坐标

继续用 $a=u-z,b=u^*-z^*,c=a+\lambda b$。本节讨论的是**相同图块上的全对关系**。若只在零锚成立，则只能得到对应零锚结论。

### 10.1 Hypomonotonicity

假设 $\langle a,b\rangle\ge-h\|a\|^2$，$h\ge0$。要把右端换成输入差 $\|c\|$，先算
$$
\langle a,c\rangle=\|a\|^2+\lambda\langle a,b\rangle
\ge(1-\lambda h)\|a\|^2.
$$
若 $\lambda h<1$，Cauchy–Schwarz 给
$\|a\|\le\|c\|/(1-\lambda h)$。代回原式：
$$
\lambda\langle a,b\rangle\ge
-\frac{\lambda h}{(1-\lambda h)^2}\|c\|^2.
\tag{10.1}
$$
和 RL 系数 $(1-L^2)/4$ 对比，得到
$$
L_H=\frac{1+\lambda h}{1-\lambda h}.
\tag{10.2}
$$
思路是“先估输出差，再代回负项”，不需要死背转换常数。

### 10.2 Cohypomonotonicity

假设 $\langle a,b\rangle\ge-\rho\|b\|^2$，$\rho\ge0$。此时估计另一个变量：
$$
\langle c,b\rangle\ge(\lambda-\rho)\|b\|^2.
$$
若 $\lambda>\rho$，则 $\|b\|\le\|c\|/(\lambda-\rho)$，所以
$$
\lambda\langle a,b\rangle\ge-
\frac{\lambda\rho}{(\lambda-\rho)^2}\|c\|^2,
\qquad L_C=\frac{\lambda+\rho}{\lambda-\rho}.
\tag{10.3}
$$
两个步长门方向相反：hypo 要 $\lambda h<1$，cohypo 要 $\lambda>\rho$。它们的负项控制的是不同变量。

### 10.3 Semimonotonicity：配方比逐项粗估更清楚

假设
$$
\langle a,b\rangle\ge-h\|a\|^2-\rho\|b\|^2,
\qquad h,\rho\ge0.
$$
设 $p=\lambda h,q=\rho/\lambda,D=1-p-q>0$，以及 $m=a-\lambda b$。由
$a=(c+m)/2,\lambda b=(c-m)/2$，原约束等价于
$$
D\|m\|^2-2(p-q)\langle c,m\rangle
\le(1+p+q)\|c\|^2.
$$
配方：
$$
\left\|m-\frac{p-q}{D}c\right\|^2
\le\frac{1-4pq}{D^2}\|c\|^2.
\tag{10.4}
$$
这是以 $(p-q)c/D$ 为中心的球，距原点最远点的范数为
$$
\boxed{L_{SM}\|c\|,\quad
L_{SM}=\frac{|p-q|+\sqrt{1-4pq}}{1-p-q}.}
\tag{10.5}
$$
这给线性 RL 的转换。此处“锐”只说在这个二次约束下的最佳代数常数，不自动证明某篇收敛定理的所有条件或其全局最优性。令 $q=0$ 或 $p=0$ 恢复前两式。

### 10.4 从一般非线性负项得到一般模

若 $\langle a,b\rangle\ge-\|a\|\sigma(\|a\|)$，则
$$
\|c\|\ge\|a\|-\lambda\sigma(\|a\|)=:\phi_1(\|a\|).
$$
**另需**在认证的 $\|a\|$ 窗口上，$\phi_1$ 可单调反解，得到
$\|a\|\le\eta_1(\|c\|)$。才可定义
$$
\omega(\delta)=\sqrt{\delta^2+
4\lambda\eta_1(\delta)\sigma(\eta_1(\delta))}.
\tag{10.6}
$$
代回负项即可得 RL。cohypo 同理，但须从
$$
\|c\|\ge\lambda\|b\|-\sigma(\|b\|)=:\phi_2(\|b\|)
$$
在认证窗口上另取得 $\|b\|\le\eta_2(\|c\|)$，再用 (10.6) 的 $\eta_2$ 版本。不能仅由 $\|b\|=\|c-a\|/\lambda$ 就凭空得到只依赖 $\|c\|$ 的界；zip 对第二项的 $\eta_2$ 适用条件需要补全。

### 10.5 和 Luke–Tam 关系的使用边界

当 $L\ge1$ 时，$\tau=(L^2-1)/4\ge0$ 正好是 Luke–Tam 的线性次单调表达。$L<1$ 时 RL 更强，当然蕴含 $\tau=0$ 的单调性，但不能把负 $\tau$ 冒充原文规定的非负违反量。

可以直接调用旧文已经证明的**同图、同窗、同点对**关系；不能因为“我们是一般模”就无条件调用只对线性模成立的全部性质。尤其 $\gamma<1$ 时，$Lt^\gamma/t\to\infty$，一般没有统一有限线性 $L$ 可用。

**自测。** 不看材料写出 $\langle a,c\rangle$ 和 $\langle c,b\rangle$，用它们分别恢复两种转换；然后用 $m=a-\lambda b$ 推一次球约束。

## 11. 第四章第一部分：从统一收敛到连续回缩

### 11.1 先补四个概念

| 术语 | 本次只需掌握的定义与区别 |
|---|---|
| 连续像 | 连续映射 $P:K\to M$ 且 $P(K)=M$ |
| 回缩 retraction | $M\subset O$，$P:O\to M$ 连续，且对每个 $p\in M$，$P(p)=p$ |
| ENR | 某个 Euclidean 开邻域存在到该集合的连续回缩；不要求集合光滑 |
| 形变回缩 | 另有连接 $I$ 与回缩的连续同伦，且始终固定目标；单有极限回缩不能直接宣称它 |

最近点投影要求“最近”，动力系统的极限映射只要求“最后落在哪里”。后者可以不是最近点投影。$P$ 是回缩也不意味着 $P$ 单射或是同胚。

### 11.2 为什么此处要增加单值连续性

轨道定理只比较每一步与某个最近零锚，允许多值输出。要写 $T^k$ 和比较不同初值的极限，先要求**同一个**预解式 $T$ 在相关邻域是单值连续映射。

全对 RL 加覆盖能在同一认证图块上给此性质；主定理的零锚条件本身不能给。若采用某条连续选择，只能说该选择的吸引结构，不能冒充所有完整预解式分支。

### 11.3 精确条件与统一尾界

设 $M\subset\operatorname{zer}F$ 非空紧，主定理对同一目标 $S=M$ 在包含 $M$ 的开集 $U$ 上有统一常数。另设完整 $T=J_{\lambda F}$ 在工作域单值连续。令
$$
D=\operatorname{dist}(M,U^c)>0,
$$
取 $0<r<R$ 使 $r+\Theta(r)<D$。$U=X$ 时无边界预算限制。定义开距离管
$$
O_r=\{x:d(x,M)<r\}.
$$
对 $x\in O_r$，
$$
D_U(x)\ge D-r>\Theta(r)\ge\Theta(d(x,M)),
$$
故所有这些初值都满足收敛预算。一步距离收缩给
$T(O_r)\subset O_r$。若管中 $Tx=x$，则
$d(x,M)\le\kappa d(x,M)$，所以 $x\in M$：这也证明 $M$ 与附近其他完整零点隔离。

定义
$$
P(x)=\lim_{k\to\infty}T^kx.
$$
尾界统一为
$$
\boxed{\sup_{x\in O_r}\|T^kx-Px\|
\le\Theta(\kappa^kr)\longrightarrow0.}
\tag{11.1}
$$
这比每个初值分别收敛更强。

### 11.4 不背定理，直接证明极限映射连续

给 $x_0\in O_r$ 与 $\epsilon>0$，先选 $k$ 使统一尾界小于 $\epsilon/3$。有限次复合 $T^k$ 连续，所以 $x$ 充分靠近 $x_0$ 时
$\|T^kx-T^kx_0\|<\epsilon/3$。于是
$$
\|Px-Px_0\|\le
\|Px-T^kx\|+\|T^kx-T^kx_0\|+\|T^kx_0-Px_0\|<\epsilon.
\tag{11.2}
$$
因此 $P$ 连续。又 $T(p)=p$ 对 $p\in M$，故 $P(p)=p$，且所有极限在 $M$。所以 $P:O_r\to M$ 是连续回缩，$M$ 是 ENR。

**讲法。** “前半篇控制一条轨道，第四章把同一个尾界对一整圈初值统一起来。统一极限保留连续性，于是收敛算法自己给出了到零集的回缩。”

### 11.5 区域像与边界像：条件不能少

若 $M\subset K\subset O_r$，则
$$
M=P(M)\subset P(K)\subset M,
$$
所以 $P(K)=M$。例如取足够小的闭距离管作为有界闭区域。

但 $P(\partial K)=M$ 需要**关于这个具体 $P$** 的额外满射论证；空内部本身不够。圆的径向回缩 $P(x)=x/\|x\|$ 会把同心环域的两个边界圆都映满 $S^1$，因为可以对每个方向直接写出边界原像。不要把“存在某个边界投影”偷换成“动力极限 $P$ 在边界必满射”。

### 11.6 ENR 到底排除了什么

回缩直接给局部可缩性的一种精确形式。给 $p\in M$ 的相对邻域 $V$，由 $P$ 连续可取小球 $B(p,\epsilon)\subset O_r$，使其像落在 $V$。则
$$
H(t,x)=P((1-t)x+tp),\quad x\in M\cap B(p,\epsilon/2)
$$
把这个小邻域的包含映射在较大邻域 $V$ 中缩到 $p$。这是“局部可缩”的实际意义；不要求那个小邻域在自身内就可缩。

因此紧 ENR 具有有限多个连通分支及有限秩有理同调。Cantor 集与积聚离散序列的无穷分支、Hawaiian earring 在积聚点不可局部缩掉的小圈，都与这套结构不相容。结论依赖**连续单值预解式＋共同严格收缩＋统一可和尾界**，不是单凭“零集”或“每条轨道都收敛”得到。

光滑流形、凸多面体是 ENR 的典型成员，但 ENR 也可有分叉和角点。故这里称“收敛诱导的零集拓扑结构”比称“实解析几何结构”更准确。

### 11.7 关于你提到的“AI 给过弱凸反例”

正式汇报中的反例必须明确：否定的是凸性、某种集合弱凸性、统一常数的弱凸函数表示，还是某个证明步骤。它还必须核完整图/局部图、极大性与收敛假设。一个反驳凸性的圆，不反驳“弱凸函数的子水平集”表示；一个仅满足全对 RL 的 Cantor 零集，也不满足这里 ENR 的完整吸引假设。

本轮附件中未定位到足以逐项核验你所指旧反例的精确陈述。安全转场是：“一般模下，我们不直接套用线性理论的弱凸表示证明，而改研究统一收敛带来的邻域回缩结构。”暂不宣称“不存在任何弱凸表示”。

## 12. 第四章第二部分：Euler 示性数与指数平衡，从基础到证明

### 12.1 为什么突然出现一个整数

我们现在有一簇吸引零点 $M$。要问的不是又快了多少，而是：如果一个大球里的总固定点指数必须是 1，这簇零点贡献的指数够不够？如果不够，其他地方必须补上。

这里需要四项工具：同调与 Euler 数、同伦、Lefschetz 数、不动点指数。无需两天学完整代数拓扑，但要知道每项作用及适用条件。

### 12.2 同调与 Euler 数的最低必需知识

把空间剖分成顶点、边、面等。边界算子 $\partial$ 满足 $\partial^2=0$：“边界的边界为空”。$j$ 维同调是
$$
H_j=\ker\partial_j/\operatorname{im}\partial_{j+1},
$$
也就是闭合的 $j$ 维结构，扣掉那些已经是更高维结构边界的部分。取有理系数后是向量空间，维数 $b_j$ 叫 Betti 数。

$b_0$ 记录连通分支数，$b_1$ 记录独立的一维环，$b_2$ 记录独立的二维闭壳。有限型空间定义
$$
\boxed{\chi(M)=\sum_{j\ge0}(-1)^j b_j.}
\tag{12.1}
$$
若有有限剖分，也等于顶点数减边数加面数再交替下去。改变剖分不改变它；它是同伦不变量。

| 空间 | 非零 Betti 数（有理系数） | $\chi$ |
|---|---|---:|
| 一个点/闭球 | $b_0=1$ | 1 |
| 圆 $S^1$ | $b_0=1,b_1=1$ | 0 |
| 球面 $S^2$ | $b_0=1,b_2=1$ | 2 |
| 环面 $\mathbb T^2$ | $b_0=1,b_1=2,b_2=1$ | 0 |

“Euler 数是洞的个数”只能作非常粗的直觉，不能代替带交替符号的定义。

### 12.3 同伦与管邻域

$f,g:A\to B$ 同伦，是存在连续 $H:[0,1]\times A\to B$ 从 $f$ 变到 $g$。同伦映射在同调上诱导同一个线性映射。

此处**新增**假设：$M\subset\mathbb R^n$ 是紧 $C^2$ 嵌入、无边界光滑流形。足够小的闭管
$$
N_\epsilon=\{x:d(x,M)\le\epsilon\}
$$
有唯一连续的法向最近点投影 $\Pi:N_\epsilon\to M$，每个点可写 $x=p+n$。同伦
$$
H(t,x)=\Pi x+(1-t)(x-\Pi x)
\tag{12.2}
$$
沿法向把管缩到 $M$。所以包含映射 $j:M\hookrightarrow N_\epsilon$ 在同调上诱导同构。

这里 $\Pi$ 来自光滑管邻域定理；前一节的 $P$ 来自迭代极限。两者作用不同，不必相等。

### 12.4 Lefschetz 数：映射在拓扑结构上怎样作用

紧 ENR 的连续自映射 $T:N\to N$ 在每个 $H_j(N;\mathbb Q)$ 上诱导线性映射 $T_*$。定义
$$
\mathcal L(T)=\sum_j(-1)^j\operatorname{tr}(T_*|H_j).
\tag{12.3}
$$
恒等映射的每个迹都是 $b_j$，因此 $\mathcal L(I)=\chi(N)$。Lefschetz 数关心映射如何作用于环和壳，不是简单数固定点个数。

### 12.5 不动点指数：本次需要四个性质

对连续 $T$，在有界开域 $O$ 且边界无固定点时，Euclidean 指数可写成
$$
\operatorname{ind}(T,O)=\deg(I-T,O,0).
$$
你可以先把 degree 理解为带方向的零点总数，再用下面的精确定理性质操作。

| 性质 | 本次怎样用 |
|---|---|
| 存在性 | 指数非零推出内部有固定点；指数零不能推出没有固定点 |
| 可加性/局部化 | 固定点被几个不相交开域分开时，总指数是各部分之和；无固定点区域不贡献 |
| 同伦不变 | 连续变形过程中边界没有固定点，指数不变 |
| 紧 ENR 归一化 | 紧 ENR 自映射的总固定点指数等于它的 Lefschetz 数；必要时用交换性将子空间指数转成环境局部指数 |

一手接口见 Benjamin–Gottlieb 作者原文 §2.1，尤其 (2.1.1)、(2.1.2)、(2.1.4)、(2.1.6)、(2.1.7)。Dold 建立一般指数理论，Brown 给非线性分析中的系统表述。Poincaré–Hopf 是相关的向量场指数背景，但这里直接用的是不动点指数；不用额外把 $F$ 假定为一个光滑向量场。

### 12.6 关键桥：为什么吸引管的指数等于 $\chi(M)$

在足够小的光滑闭管 $N=N_\epsilon$ 上，距离收缩给
$$
T(N)\subset\operatorname{int}N,\quad
\operatorname{Fix}T\cap N=M,\quad T|_M=I.
\tag{12.4}
$$
于是 $T\circ j=j$。取同调：
$$
T_*j_*=j_*.
$$
因为 $j_*$ 是同构，故 $T_*=I$ 在每个同调群上成立。由 (12.3)，
$$
\mathcal L(T|_N)=\chi(N)=\chi(M).
$$
紧 ENR 的指数归一化，以及局部化/交换性把它识别为环境管内指数，得到
$$
\boxed{\operatorname{ind}(T,\operatorname{int}N)=\chi(M).}
\tag{12.5}
$$
这是比“吸引，所以指数等于 Euler”更可重建的证明。不要用 $(1-t)Tx+t\Pi x$ 作为当然合法的管内同伦；弯曲管一般不凸，线段未必留管。

**这里有限长扮演什么角色？** 它在上一节给连续极限回缩。对已经假设光滑 $M$ 的 (12.5)，严格管不变、固定 $M$ 和光滑法向回缩就足以完成同调论证，不需把两个证明说成同一步。

### 12.7 全局指数为什么是 1

为使几何最清楚，取 $\Omega=B(0,H)$，$\overline N\subset\Omega$，且 $T$ 在 $\overline\Omega$ 上连续。若
$$
\langle x-Tx,x\rangle>0\quad(x\in\partial\Omega),
\tag{12.6}
$$
则边界没有固定点。考虑向量场的同伦
$$
G_s(x)=(1-s)(x-Tx)+s x,\quad0\le s\le1.
$$
边界上
$$
\langle G_s(x),x\rangle
=(1-s)\langle x-Tx,x\rangle+s\|x\|^2>0,
$$
所以同伦不在边界产生零点。由 degree 的归一化，
$$
\boxed{\operatorname{ind}(T,\Omega)
=\deg(I-T,\Omega,0)=\deg(I,\Omega,0)=1.}
\tag{12.7}
$$
另一种足够条件是 $T(\overline\Omega)\subset\Omega$，其中 $\Omega$ 为球或有界凸开集；可用其可缩性与固定点指数归一化。

如果不额外假设大球向内，但有**全空间、全尺度**反射次线性增长
$\|Rx-R0\|\le L_*\|x\|^{\gamma_*}$、$\gamma_*<1$，则
$$
\|Tx\|\le\tfrac12(\|x\|+\|R0\|+L_*\|x\|^{\gamma_*})<\|x\|
$$
在充分大的球面成立，也可导出 (12.7)。这需要独立的全局假设，不能从局部收敛定理直接拿到。

### 12.8 最后的一行：缺额迫使管外有零点

两条边界上都没有固定点，可以按可加性分开管内与管外：
$$
\boxed{\operatorname{ind}(T,\Omega\setminus N)
=1-\chi(M).}
\tag{12.8}
$$
若 $\chi(M)\ne1$，右边非零，管外必有固定点。完整预解式满足 $\operatorname{Fix}T=\operatorname{zer}F$，所以管外必有另一个零点。

| 管内零簇 | 管内指数 | 管外剩余指数 | 正确结论 |
|---|---:|---:|---|
| 点 | 1 | 0 | 这一工具不强迫新增零点；不等于证明不存在 |
| 圆 | 0 | 1 | 必有额外零点 |
| 球面 | 2 | -1 | 必有额外零点；指数允许负号 |
| 环面 | 0 | 1 | 必有额外零点 |

不能把 $1-\chi(M)$ 当成新增零点的数量。若要从指数推数量，必须另有孤立性、非退化性和各点指数限制。也不能在没有径向对称时断言额外零点一定在“圆心”；这里只定位到指定管外区域。

**结尾口头句。** “局部收敛先让零簇成为吸引对象；光滑管把它的局部指数转成 Euler 数；大球里的总指数固定为 1。二者的差额若非零，就必须由其他零点补偿。”

## 13. 整场汇报的板书顺序与口头连接

按完整板书约 70–90 分钟设计。若老师频繁追问，先保留各段核心框式，背景展开可缩短。例子不排进主线。

| 顺序 | 讲什么 | 必须出现的板书 | 参考用时 |
|---|---|---|---:|
| 1 | 求零包含、PPA 与 GPPA | (1.1)–(1.4) | 4 分钟 |
| 2 | Minty、历史路线、Luke–Tam | (2.1)–(2.5)、原文条件表、弱凸的准确对象 | 10 分钟 |
| 3 | 我先改成 Hölder | (3.1)–(3.6) | 7 分钟 |
| 4 | 反推收敛条件，再换一般模 | (4.2)–(4.5) | 6 分钟 |
| 5 | 回到旧文解释覆盖 | (5.1)–(5.2) | 4 分钟 |
| 6 | 四假设与主定理证明 | 条件表、(6.3)–(6.6) | 12 分钟 |
| 7 | 幂模、旧理论、扩大范围与锐性 | (7.1)–(7.3)、(8.2)–(8.9) | 10 分钟 |
| 8 | GPPA 的缺口与补充条件 | 三种距离、(9.4)–(9.11) | 9 分钟 |
| 9 | 第三章的关系 | (10.1)、(10.3)、球约束 (10.4) | 6 分钟 |
| 10 | 连续回缩与区域像 | (11.1)、(11.2)、$P|_M=I$ | 7 分钟 |
| 11 | Euler、局部指数、总指数、缺额 | (12.1)、(12.5)、(12.7)、(12.8) | 10 分钟 |

可直接用的过渡句：

- 算法到经典理论：“隐式迭代第一件事是能否解出下一步，第二件事是解出的点会不会稳定。”
- 经典到新定义：“线性理论控制的是反射差的 Lipschitz 常数。我们先只改变这个控制尺度。”
- 定义到收敛：“新定义本身不保证收敛；我要看它能为一步迭代提供什么可用估计。”
- 一般模到假设：“为了让刚才的三条估计闭合，把覆盖、零锚、真误差界和模兼容分别列出来。”
- 主定理到 sharp：“直接条件便于处理一般模；线性时还可把误差界直接耦合进平方能量。”
- PPA 到 GPPA：“核增量仍控制残差，但已不再等于物理位移。”
- GPPA 到比较章：“接下来核对新条件和已知广义单调性处在什么关系中。”
- 比较章到几何：“除了轨道趋向哪里，我还想知道允许的极限零集能长成什么样。”
- 回缩到指数：“回缩描述局部形状；固定点指数把这个局部形状接到全局零点分布。”

## 14. 老师最可能追问的题目与答题骨架

不要把答案背成句子。先自己推，推不出再看右栏。

| 追问 | 应答的第一步与关键边界 |
|---|---|
| 单调和极大单调各负责什么？ | 单调给 firm/唯一性；极大单调通过 Minty 给全输入覆盖。普通局部 RL 不能自动取代覆盖。 |
| 为什么是 $2J-I$？ | 展开 $\|2a-c\|^2$，交叉项恰好为 $-4\lambda\langle a,b\rangle$。 |
| $1/4$、$1/2$ 从哪里来？ | 反射平方恒等式给 $1/4$，平行四边形给能量的 $1/2$，解和差各除以 2 给半和。 |
| 你到底改了几个条件？ | 按四项组织保留覆盖、替换其余三类；另明确全对到最近零锚、闭目标及几何段单值连续性的变化。 |
| 误差界为什么用在 $y$？ | 算法给出的图值属于 $F(y)$，真残差链在输出处成立。 |
| 最近点为什么存在？ | $S$ 非空闭，有限维中最小化序列可限制在有界球内再用紧性；不要求 $S$ 凸。 |
| 零点开始会不会跳到另一个零点？ | 对允许关系，$B(0)=0$ 或 GPPA 的 G2+G3 强迫不动。一般完整预解式未满足条件时可有额外分支。 |
| 距离趋零为何不够？ | 沿零集切向漂移；要补物理步长可和，才能保证点 Cauchy。 |
| 模趋零为什么还要可和？ | 连续模沿几何点列可以只有 $1/j$ 衰减。 |
| 你的留域证明是否循环？ | 只对已构造的有限前缀求和，证明下一步留域，才归纳到无限轨道。 |
| $\gamma q<1$ 就不收敛吗？ | 不能这么说；失败的是当前最坏模复合的直接统一证书，不是所有算子收敛。 |
| 你恢复 Luke–Tam 的是哪一支？ | 用 (8.4)–(8.5) 核旧参数，再用能量分支 (8.2) 比较；半和分支不包含全部旧情形。 |
| sharp 是对什么、所有参数都实现吗？ | 能量因子在 (8.8) 可行域达等；临界旋转非收敛仅覆盖 $0<t\le2$。 |
| GPPA 为什么不能只换 $x\to v(x)$？ | 核步长可和不意味着物理步长可和，尤其非单射核有不可见方向。 |
| 非单射核下固定点和零点仍相同吗？ | 对完整关系相同；由输入输出相等直接得零增量。单射性不是这个恒等式的前提。 |
| Boris 原文已证明点收敛吗？ | v1 T2 给核量线性衰减，附加逆算子条件给到零集距离趋零；当前物理有限长结论要另核。 |
| 回缩为什么连续？ | 先选共同迭代次数使两端尾项小，再用有限次迭代连续性；写 (11.2)。 |
| 你的 $P$ 是最近点投影吗？ | 不一定；它由动力极限决定。光滑管的 $\Pi$ 是另一映射。 |
| 连续像是否给解析结构？ | 不给实解析、光滑或同胚；回缩给 ENR，强于仅连续像，但仍允许角点和分叉。 |
| 为什么 Euler 数等于局部指数？ | 光滑管 $j_*$ 同构，$Tj=j$ 推 $T_*=I$，再用 Lefschetz 与指数归一化。 |
| 如果 $\chi=1$，就没有额外零点吗？ | 不能；剩余指数为零仍可有固定点和正负抵消。 |
| 为什么管外多一个零点而不是多 $1-\chi$ 个？ | 指数是带符号的拓扑计数；没有每点指数限制就不能直接数点。 |
| 一般核 GPPA 也能照搬 Euler 结论吗？ | 不能仅凭核收敛就搬；须另有同一物理连续单值映射、紧管结构和全局指数条件。 |

最终空白纸只留八组公式作提示，依次重建整场：

1. $x-y\in\lambda F(y)$，或 $v(x)-v(y)\in\lambda F(y)$。
2. $\|a-\lambda b\|^2=\|a+\lambda b\|^2-4\lambda\langle a,b\rangle$。
3. $B(t)=[t+\omega(t)]/2$，$d(y)\le\psi(B(d(x))/\lambda)$。
4. $\Theta(t)=\sum_jB(\kappa^jt)$，$\Theta(d_0)<D_U(x^0)$。
5. $[1+(\lambda/K)^2]d(y)^2\le(1+L^2)d(x)^2/2$。
6. $K_v=(a+\omega_v\circ a)/2$，$H_v(t)=h(t,K_v(t))$。
7. $\sup\|T^kx-Px\|\le\Theta(\kappa^kr)\to0$，$P|_M=I$。
8. $\operatorname{ind}_{\mathrm{tube}}=\chi(M)$，$\operatorname{ind}_{\mathrm{global}}=1$，$\operatorname{ind}_{\mathrm{outside}}=1-\chi(M)$。

## 15. 定位、来源与本轮核查边界

### 投稿 zip 的定位表

| 备讲段落 | zip 内完整路径 | 读取时重点 |
|---|---|---|
| 第 1–5 节 | `PPA_LaTeX/sections/preliminaries.tex` | 定义、Luke–Tam 转述、三种等价、两个迭代引理；文献转述应以正式原文校准 |
| 第 6–8 节 | `PPA_LaTeX/sections/theorem_spine.tex` | Assumption 1、Theorem 1、Corollary 2、线性能量 Theorem 2 |
| sharp 可行域 | `PPA_LaTeX/supplements/linear_attainment.tex` | $\beta^2\ge0$、边界 $0<t\le2$，纠正主文的全参数泛化 |
| 第 9 节 | `PPA_LaTeX/sections/gppa_theory.tex` | Assumption 2、Theorem 3；核步与物理步分开 |
| 第 10 节 | `PPA_LaTeX/sections/related_work.tex` | hypo/cohypo/semimonotone 的同图转换；非线性逆模条件须补全 |
| 第 11–12 节 | `PPA_LaTeX/sections/topological_obstruction.tex` | 回缩 Theorem 4、Euler Theorem 5；单值连续、紧性、光滑性与全局条件分别核验 |

### 已核的一手文献接口

- Luke–Tam, *Generalized Monotonicity and the Proximal Point Algorithm*, DOI [10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)：Definition 2、Propositions 3–4（印刷 pp.3–4）、Theorem 1（pp.4–5）、Assumption 2 与 Theorem 2（pp.9–10）。本讲义的参数比较由这些原式自行换算；不是照抄 zip 的概述。
- Le–Mordukhovich–Théra, [arXiv:2608.01584v1](https://arxiv.org/abs/2608.01584v1)：Definition 3（p.5）、Theorem 2 及其证明（pp.7–8）。本轮在线摘要核身份，正文使用仓库已经保存的作者 PDF `research/comparisons/2026_08_gppa_nfb/sources/gppa_2608.01584v1.pdf`；没有把摘要当作详细证明来源。
- Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*, [作者 PDF](https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf)，§2.1：局部化、可加性、紧 ENR 归一化、交换性和同伦不变。这里从这些性质及明确的管邻域结构重建局部指数桥；未把正文的 collar 主定理误称为本文的全部新结论。
- Minty 的满射对应、管邻域定理与基础同调理论作为标准定理导入；本轮没有重新证明这些基础定理，也未穷尽历史文献或认证新颖性。

### 规范研究入口，不与本次 zip 混版本

- `research/canonical/true_residual_selection_rleb.md`：C02-v3，同真残差、允许输出与有限前缀的收敛链。
- `research/canonical/physical_rleb_gppa.md`：C249–C253，物理核接口与线性能量分支。
- `research/canonical/rleb_kernel_topology_interfaces.md`：C254，局部指数桥；其全局反射前提与本 zip 的大球向内条件是不同充分接口，应分别核验。
- `research/canonical/holder_extension.md`：全对全尺度 Hölder 延拓；不是零锚收敛定理的隐含前提。

本轮已逐式重建反射/内积/能量等价、半和界、真残差链、有限前缀留域、一般模零点处尾连续性、幂模常数、线性能量与旋转可行性、GPPA 物理接口、三种单调性转换、统一极限回缩，以及带明确光滑/全局前提的指数平衡。已把投稿与原文不一致的比较、过强锐性表述和未核弱凸反例标在相应使用处。未进行整篇投稿的全面审稿或修改，也不把本教学材料登记成新的数学定理。

**使用方式。** 先沿第 1–12 节真正推一遍，再按第 13 节口头连起来，最后只用第 14 节的八组公式闭卷重建。对前两节的基础提问答不清时，先修那个断点，不靠继续抄后面的定理掩盖它。

