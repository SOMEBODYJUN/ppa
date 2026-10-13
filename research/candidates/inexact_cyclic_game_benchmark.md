# 三人有向循环博弈：完整非精确输出的自然基准与经典恢复

本文件是独立候选证明，不登记新 Claim，也不改主稿。状态为 `candidate`：下述推导已逐项自检，尚待另一位研究者独立接收。它提供真正的 Nash 求解任务、未知零点、完整非精确输出及可计算停止准则；它**不**提供 RLEB 独占的新收敛机制。尖锐性分别限定为全域映射 Lipschitz 常数、全对逆亚单调常数及相应证书门，不偷换为轨道收敛的必要阈值。

## 1. 原始任务与完整零集

在 $X=\mathbb R^3$ 中，三个玩家分别选择实数 $x_i$，下标循环 $x_4=x_1$。给定外部数据 $b\in\mathbb R^3$，玩家 $i$ 最小化

\[
 j_i(x_i;x_{i+1})=\frac14x_i^4+\frac12x_i^2+3x_ix_{i+1}-b_ix_i.
 \tag{CG1}
\]

每个单人问题对自己的变量强凸且强制，因此联合策略为 Nash 均衡当且仅当

\[
 F_b(x)=x^{\circ3}+x+3Px-b=0,
 \qquad P(x_1,x_2,x_3)=(x_2,x_3,x_1).
 \tag{CG2}
\]

这不是共同目标的驻点替身：它确是每个玩家的全局最优反应。$\partial_{x_2}(F_b)_1=3$、$\partial_{x_1}(F_b)_2=0$，所以不存在以 $F_b$ 为梯度的 $C^2$ 势函数。最优反应 $\phi(b_i-3x_{i+1})$ 对邻居变量递减，其中 $\phi=(u\mapsto u^3+u)^{-1}$；这是有向循环的战略替代博弈。模型由原始成本给定，不由预先知道的均衡反造。它是有解释的数学基准，不宣称来自某个已部署市场或某篇文献的同一数值实例。

**全域唯一性。** 代入后 $x_1$ 满足

\[
 x_1=\phi\bigl(b_1-3\phi(b_2-3\phi(b_3-3x_1))\bigr).
 \tag{CG3}
\]

右端连续严格递减。左端减右端严格递增，并在两端分别趋于 $-\infty,+\infty$，因此恰有一个根。再逐级恢复 $x_3,x_2$。记此未知均衡为 $s_b$，完整零集恰为

\[
 S_b=F_b^{-1}(0)=\{s_b\}.
 \tag{CG4}
\]

相同证明对任意右端成立，故 $F_b$ 是全域双射。这里没有利用一个预知零点的坐标平移。

## 2. 一个尖锐的循环矩阵估计

**引理 CG-L。** 设 $c\ge\alpha>0$，$D=\operatorname{diag}(d_1,d_2,d_3)$ 且 $d_i\ge\alpha$。令

\[
 \mu=\frac{\sqrt{4\alpha^2+c^2}-c}{2},
 \qquad \mu^2+c\mu=\alpha^2.
\]

则

\[
 \|(D+cP)z\|\ge\mu\|z\|\quad(z\in\mathbb R^3).
 \tag{CG5}
\]

常数对整个对角参数类尖锐，其下确界可由一个 $d_i\to\infty$ 达到极限。

**证明。** 若三个分量同号，则逐项没有抵消，左端至少 $\alpha\|z\|$。其余情形经整体变号及循环置换，可写 $z=(u,v,-w)$，$u,v,w\ge0$。对所有允许的 $D$，左端平方至少

\[
 f=(\alpha u+cv)^2+(\alpha v-cw)_+^2+(\alpha w-cu)_+^2.
 \tag{CG6}
\]

此式只是下界：例如某分量为零时，不能把允许无限增大的对角参数当成有限参数下的精确消去。

1. 若 $\alpha v\ge cw$ 且 $\alpha w\ge cu$，则 $f=\|(\alpha I+cP)z\|^2$。该正规矩阵的最小奇异值平方为 $\alpha^2+c^2-\alpha c$，而其减去 $\mu^2$ 等于 $c(\mu+c-\alpha)\ge0$。
2. 若 $\alpha v<cw$ 且 $\alpha w\ge cu$，则
   \[
   f=\alpha^2u^2+(\alpha w-cu)^2+c^2v^2+2\alpha cuv
   \ge\mu^2(u^2+w^2)+\mu^2v^2.
   \]
   这里 $\begin{pmatrix}\alpha&0\\-c&\alpha\end{pmatrix}$ 的最小奇异值恰为 $\mu$，并且 $c\ge\alpha\ge\mu$。
3. 若 $\alpha v\ge cw$ 且 $\alpha w<cu$，则 $uv\ge w^2$，于是即使丢掉第二平方也有
   \[
   f\ge\alpha^2u^2+c^2v^2+2\alpha cuv
   \ge\alpha^2(u^2+v^2)+2\alpha c w^2
   \ge\mu^2(u^2+v^2+w^2).
   \]
4. 若两条不等式均反向，置 $\beta=c/\alpha\ge1$。当 $u=0$ 时三分量皆零；否则 $w\le\beta u$，$r=v/u\in[0,\beta^2]$，故
   \[
   \frac f{u^2+v^2+w^2}
   \ge\alpha^2\frac{(1+\beta r)^2}{1+\beta^2+r^2}
   \ge\frac{\alpha^2}{1+\beta^2}\ge\mu^2.
   \]
   中间函数在该区间递增，因为导数符号为 $\beta(1+\beta^2)-r>0$。最后一式等价于 $\alpha^4-\mu^2(\alpha^2+c^2)=c\mu^3\ge0$。

这穷尽符号与边界。为证尖锐，取 $D_M=\operatorname{diag}(\alpha,M,\alpha)$ 及 $z_M=(\mu,c\alpha/M,-\alpha)$。则

\[
 (D_M+cP)z_M=(\alpha\mu+c^2\alpha/M,0,-\mu^2),
\]

故商趋于 $\mu$。□

## 3. 真残差、完整近端覆盖及尖锐映射常数

对任意 $x,y$，

\[
 F_b(x)-F_b(y)=(D(x,y)+3P)(x-y),\qquad
 D_{ii}=1+x_i^2+x_iy_i+y_i^2\ge1.
 \tag{CG7}
\]

CG-L 取 $\alpha=1,c=3$，得到全域真误差界

\[
 \|x-s_b\|\le K\,r_{F_b}(x),\quad
 r_{F_b}(x)=\|F_b(x)\|,\quad
 K=\frac{\sqrt{13}+3}{2}<3.303.
 \tag{CG8}
\]

$F_b$ 单值，所以此处真残差确等于函数值范数；这一身份不移植到一般多值关系。$K$ 是 $F_b^{-1}$ 的尖锐全域 Lipschitz 常数：$DF_b$ 可实现每个对角 $D\ge I$，在 CG-L 尖锐参数处作局部差商即可逼近 $K$。这不声称对每个固定 $b$ 的根锚定 EB 常数也必须恰为 $K$。

固定 $\lambda>0$，记

\[
 H_\lambda(y)=y+\lambda F_b(y),\qquad T_\lambda=H_\lambda^{-1}.
 \tag{CG9}
\]

用 $g_\lambda(u)=(1+\lambda)u+\lambda u^3$ 代替 CG3 的 $u+u^3$，相同的三个递减映射复合证明 $H_\lambda$ 全域双射。因此对每个输入 $x\in\mathbb R^3$，**完整** $J_{\lambda F_b}(x)$ 非空且恰为 $\{T_\lambda x\}$，没有选支或远根删除。

当 $\lambda\ge1/2$ 时，CG-L 取 $\alpha=1+\lambda,c=3\lambda$，给出尖锐全域常数

\[
 \|T_\lambda x-T_\lambda z\|\le q_\lambda\|x-z\|,
 \quad q_\lambda=
 \frac{\sqrt{4(1+\lambda)^2+9\lambda^2}+3\lambda}
 {2(1+\lambda)^2}.
 \tag{CG10}
\]

尖锐性仍由可实现的 Jacobian 对角参数及 CG-L 极限给出，与 $b$ 无关。且 $q_\lambda<1$ 当且仅当 $\lambda>1$。这是在本公式范围内**全域欧氏映射严格收缩证书**的准确门，不能写成全部轨道收敛的必要门；$b=0$ 时均衡 Jacobian 的复杂特征对只要求局部线性稳定阈值 $\lambda>1/7$，$\lambda=1/7$ 的非线性边界行为未在此判定。

## 4. 全部非精确输出及可计算停止条件

令 $\lambda>1$、$q=q_\lambda$。对每个输入 $x\in\mathbb R^3$ 定义完整允许集合

\[
 \mathcal A_{\lambda,\sigma}(x)=
 \{y:\ \|e(x,y)\|\le\sigma\|y-x\|\},\qquad
 e(x,y)=y+\lambda F_b(y)-x.
 \tag{CG11}
\]

这是由停止规则规定的全部近似输出，不是原精确 resolvent。它包含唯一精确输出，故全输入非空；一般含有无穷多个点。固定

\[
 0\le\sigma<\sigma_{\rm suff}:=\frac{1-q}{2q}.
 \tag{CG12}
\]

则对每个输入及每个 CG11 输出，

\[
 y=T_\lambda(x+e),\quad
 \|y-s_b\|\le q(\|x-s_b\|+\|e\|)
 \le q(1+\sigma)\|x-s_b\|+q\sigma\|y-s_b\|.
\]

因此

\[
 \|y-s_b\|\le\kappa\|x-s_b\|,
 \qquad \kappa=\frac{q(1+\sigma)}{1-q\sigma}<1.
 \tag{CG13}
\]

此证明同时排除 $x=s_b$ 的全部非零输出，故未知零点一旦达到即吸收。每条任意切换近似输出的轨道全域存在、有限长，且

\[
 \|x^k-s_b\|\le\kappa^kK\|F_b(x^0)\|,
 \quad\sum_{k\ge0}\|x^{k+1}-x^k\|
 \le\frac{1+\kappa}{1-\kappa}K\|F_b(x^0)\|.
 \tag{CG14}
\]

不要求误差预先可和，求和性由合同推出。外层可用 $\|F_b(x)\|\le\varepsilon/K$ 认证距离误差不超过 $\varepsilon$。内层停止规则不含 $s_b$；若 $F_b(x)\ne0$ 且 $\sigma>0$，任何收敛到精确内层解的内层过程最终通过 CG11，因为右端趋于正数而左端趋零。若 $F_b(x)=0$ 则直接停止外层。此论断不把“某求根器收敛”当作已自动证明；CG3 的单调标量方程可用确定性括区间方法供应一种内层实现。

在 $\lambda=5,\sigma=1/4$，

\[
 q=(\sqrt{369}+15)/72\approx0.475130,
 \quad\sigma_{\rm suff}\approx0.552343,
 \quad\kappa=5q/(4-q)\approx0.673968<0.675.
 \tag{CG15}
\]

CG12 是由尖锐 $q$ 得到的**显式充分容差**，不是 CG11 算法可容许误差的已证最大值。三角不等式可能松弛；尚未求解完整非精确关系的最优阈值。不得给它贴“尖锐容差”的标签。

若采用正在研究的一般 gauge 形式，因本例 $\psi(t)=Kt$，可直接计算

\[
 \|e(x,y)\|\le\eta\psi(\|F_b(y)\|)=\eta K\|F_b(y)\|.
 \tag{CG16}
\]

当 $\eta K<\lambda$ 时，$\lambda\|F_b(y)\|\le\|x-y\|+\|e\|$，故 CG11 对 $\sigma=\eta K/(\lambda-\eta K)$ 成立。充分门为

\[
 \eta<\frac{\lambda(1-q)}{K(1+q)},
 \qquad\kappa=\frac{q\lambda}{\lambda-\eta K(1+q)}.
 \tag{CG17}
\]

例如 $\lambda=5,\eta=1/4$ 可认证。此桥只在本例真正单值残差下作等同。

## 5. 超出原欧氏极大单调，但完全兼容经典逆亚单调理论

首先，$DF_b(0)=I+3P$ 有特征值 $4,-1/2\pm(3\sqrt3/2)i$。因此 $F_b$ 不是欧氏单调；它有全域线性 EB 也不改变这一事实。反过来，单调 $F(x)=x^3$ 在零点附近不满足线性 EB。这是几何前件与误差界的独立角色，不能称“次正则性加强单调性”。

还能排除“只在未知均衡附近换个 SPD 即单调”的轻易解释。取原始数据 $b=(1,2,3)/1000$。CG8 给 $\|s_b\|<0.01236$，故 $DF_b(s_b)$ 与正规矩阵 $I+3P$ 的差范数小于 $0.000459$。正规矩阵的 resolvent 范数与连续扰动的特征值计数，使两个特征值仍落在 $-1/2\pm(3\sqrt3/2)i$ 的上述小圆盘内，实部严格为负。若某 SPD $M$ 使此邻域的 $F_b$ 在 $M$ 内积单调，则 $MDF_b(s_b)+DF_b(s_b)^TM\succeq0$；在任意复杂特征向量上评价要求对应特征值实部非负，矛盾。原始零点仍由 CG3 隐式确定，未先指定它。

但是，CG-L 取 $\alpha=2,c=3$ 得 $\mu=1$，代入 CG7 可知

\[
 \|(F_b(x)-F_b(y))+(x-y)\|\ge\|x-y\|,
\]

即

\[
 \langle x-y,F_b(x)-F_b(y)\rangle
 \ge-\frac12\|F_b(x)-F_b(y)\|^2.
 \tag{CG18}
\]

所以 $F_b$ 全域 $1/2$-cohypomonotone。由于 $F_b^{-1}$ 全域连续，$F_b^{-1}+\tfrac12 I$ 是全域连续单调映射，因而极大单调。常数 $1/2$ 亦为全对尖锐值：当一个 Jacobian 对角趋于无穷，其逆在另外两个坐标上趋于 $\begin{pmatrix}1&-3\\0&1\end{pmatrix}$，对称部分的最小特征值为 $-1/2$。

**同算法经典正面。** 对精确步 $x=y+\lambda F_b(y)$，CG18 给

\[
 \|x-s_b\|^2\ge\|y-s_b\|^2+
 \lambda(\lambda-1)\|F_b(y)\|^2.
 \tag{CG19}
\]

故每个 $\lambda>1$ 都由经典 Fejér + 真 EB 得全域线性收敛及有限长度；更好的 CG10 直接给 Banach 收缩。CG13 又直接把同一证明扩到全部相对误差输出，无需 KL 或 RLEB 父定理。其内层精度政策本身有实际可计算意义，却不是 RLEB 才能发现的能力。

Combettes–Pennanen 的作者预印本 *Proximal Methods for Cohypomonotone Operators*，Definition 2.2、Lemma 2.4、Theorem 3.1，提供明确经典接口：取单个 $A=F_b$、$\rho=1/2$、全域局部化 $V=X=\mathbb R^3$、近端参数 $\gamma_n=\lambda$、松弛 $\lambda_n^{\rm CP}=1$。其条件 $1/(1-\rho/\lambda)<2$ 恰为 $\lambda>1$；精确误差取零。固定的 $\lambda=5$ 完全进入该旧理论。该定理的非精确输入误差要求可和，不能在未证明时把它直接当作 CG11 常数相对误差定理；CG13 提供更短的独立同算法证明并随后推出误差可和。

Iusem–Pennanen–Svaiter 2003 的期刊摘要已明确包含非单调与固定相对误差；本轮作者 PDF 返回 404，未以摘要猜其每一项算法同一性。Pethick–Mavrothalassitis–Cevher 2025 的完整文中 Algorithm 1 有额外误差修正，且 Assumption 3.1 要求全域 Lipschitz 场，本例立方场不满足。因此不能字面导入其全域定理，也不能由这项失败宣称经典理论空白。

## 6. 对当前 RLEB 的接口与价值裁决

本例精确步在当前 C249 的 $v=I$ 框架中可直接认证。固定 $\lambda=5$，以 CG10 的 $q$ 定义

\[
 L=\sqrt{1+(2/5)(1+q)^2},\quad
 a(t)=t,\ \omega(t)=Lt,\ h(t,s)=s,\ \psi(t)=Kt.
\]

CG18 与 $\|x-y\|\le(1+q)\|x-s_b\|$ 给最近零锚反射模 $L$；CG8 给完整真 EB；全域覆盖见 CG9，$U=\mathbb R^3$，任何有限 $R$ 可取足够大的 $\bar t$。直接兼容系数 $K(1+L)/10<0.783$。这比已经由同一原始矩阵估计得到的 $q<0.476$ 更松，也不更便宜。CG11 不是 C249 的精确包含，必须另加误差桥，不能无声改父定理。

**选择结果。** 保留为自然、非势、无法由固定 SPD 原场单调性解释的完整非精确基准；可展示未知 Nash 点的残差停止、任意合格内层输出的统一率和误差预算。否定“独占 RLEB 强优势主应用”的推荐：同一个短原始证书已经给出经典全域收缩与逆亚单调恢复。唯一未决的是该精确循环矩阵常数的公开先行性及 CG11 最优容差，不能由本轮未搜到判首创。

## 一手来源与读取范围

- Combettes–Pennanen 2004，作者完整预印本 [sicon3.pdf](https://pcombet.math.ncsu.edu/sicon3.pdf)，上述确切条目；期刊 DOI [10.1137/S0363012903427336](https://doi.org/10.1137/S0363012903427336)。本轮仅读取网页解析，未将全文存入仓库。
- Iusem–Pennanen–Svaiter 2003，*SIAM J. Optim.* 13(4), 1080–1097，[期刊原始摘要与元数据](https://epubs.siam.org/doi/10.1137/S1052623401399587)。只承担“固定相对误差非单调 PPA 并非新主题”，不承担未经读取的精确定理映射。
- Pethick–Mavrothalassitis–Cevher，ICLR 2025，[正式论文](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f44f98e5e70dea605d0c5baca231c58-Paper-Conference.pdf)，Assumption 3.1、Algorithm 1、Section 7；区分其带修正算法与 CG11。
- Parise–Ozdaglar，*A variational inequality framework for network games*，[期刊条目](https://www.sciencedirect.com/science/article/pii/S0899825618301891)仅用于有向网络博弈的领域定位；CG1 不伪装成该文的同一具体模型。

所有 CG1–CG19 数学结论由本文件自足证明承担；没有从领域定位或摘要导入隐含条件。
