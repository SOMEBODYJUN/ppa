# DD1：已有估计、分段锐门与公开先例核查

检索日期：2026-11-20。范围：六路独立网络检索及主线程原文复核；不是系统综述，也不是全球优先权认证。数学身份以仓库实际文件为准。

## 1. 本轮结论

**尚未检出完整 DD1 分段锐门连同两类临界构形的直接外部先例；已经确认其补偿机制及主要组成估计有先例。** 特别是 Alcantara 的 arXiv:2611.20523v1 明文给出第二个收缩因子；同文还给出第一项所用的步长界。因此不能以没有命中同一分段公式为由，称两个估计、整个补偿思想或 DD1 全部内容首次出现。

可能仍有独立贡献的对象是：在明确的最近零锚量词下，确定完整最优参数区域，给出两种边界实现及必要性范围。它目前是**公开新颖性未决**，不是已认证首创。证明很短、来源接近、结果正确和结果新颖是不同判断。

## 2. 固定被检索的精确命题

在有限维欧氏空间，取非空闭集 $S$，$p\in P_S(x)$、$q\in P_S(y)$。记

$$
a=\|x-p\|>0,\quad s=\|x-y\|,\quad b=\|y-p\|,\quad t=\|y-q\|.
$$

对固定 $\rho>0,\sigma\ge0$，假设

$$
s^2+b^2\le(1+2\sigma)a^2,\qquad t\le\rho s.
$$

最近点关系还给 $t\le b$、$a\le\|x-q\|$。DD1 的两项上界是

$$
\frac ta\le\min\left\{
\frac{\rho(1+\sqrt{1+4\sigma})}{2},
\rho\sqrt{\frac{1+2\sigma}{1+\rho^2}}
\right\}.
$$

保证这一几何类的所有构形都有 $t<a$ 的精确严格门为

$$
\sigma<T(\rho),\qquad
T(\rho)=\begin{cases}
(1-\rho)/\rho^2,&0<\rho\le1/2,\\
1/(2\rho^2),&\rho\ge1/2.
\end{cases}
$$

算子版本：$x-y\in\lambda F(y)$，$S\subset\operatorname{zer}F$，某个 $p\in P_S(x)$ 满足

$$
\langle y-p,x-y\rangle\ge\Phi(d(x,S)),\qquad
d(y,S)\le\ell r_F(y),\quad
r_F(y)=\inf_{v\in F(y)}\|v\|.
$$

取 $\rho=\ell/\lambda$、$\sigma_R=\sup_{0<u\le R}[-\Phi(u)]_+/u^2$，则 $\sigma_R<T(\rho)$ 在正距离输入上提供统一一步收缩和输入距离型步界。轨道结论还需要同一允许关系的覆盖、残差评价窗、零输入吸收和留域；这不是任意原算子自动成立的结论。

## 3. 逐项文献比对

以下文献事实均已由主线程打开原始论文核对；变量替换及推导另列为本库分析。

| 原始来源与定位 | 已核文献事实 | 与 DD1 的关系 |
| --- | --- | --- |
| Gárciga Otero–Iusem, *Regularity results for semimonotone operators*；2010-05-17 预印本，Definition 2、Theorem 3、Corollary 3、Remark 3，印刷页 8–9 | 全图点对的半单调不等式；$L(1)=\tfrac12(1+\sqrt{(1+r)/(1-r)})$ | 换参后就是第一项中的根式常数；不是完整 DD1 的原文陈述。 |
| Luke–Thao–Tam, MOR 43(4), 2018, pp.1143–1176；Theorem 2.1，pp.1152–1153 | almost averagedness 与残差控制结合给 $c=\sqrt{1+\varepsilon-(1-\alpha)/(\alpha\kappa^2)}$ | 补偿机制明确已有；其输入距离误差界不能与 DD1 输出距离误差界直接混同。 |
| Lauster–Luke, 2021；Corollary 19 后的讨论 | 明确讨论 firmness violation 必须由足够强的 metric-subregularity gauge 补偿 | “一方减弱、另一方补偿”的总体研究叙事已有明确先例。 |
| Evens–Pas–Latafat–Patrinos, arXiv:2305.03605v2，2024-05-06；Proposition 4.12(ii)，印刷页 21 | 一般 $(\mu,r)$-semimonotone resolvent 的 Lipschitz 常数 | 特定参数也恢复第一根式常数；假设仍是较强的全图点对条件。 |
| Luke–Tam, MOR, DOI 10.1287/moor.2025.0863；2025-11-21 在线发表，式(30)、Assumption 2(d)(ii)、Theorem 2，pp.10–11 | 式(30) 与 DD1 平方和前提一致；其门是 $\sigma(1+\rho)^2<1/2$，归一化极限因子 $\sqrt{1+2\sigma-(1+\rho)^{-2}}$ | 极近前驱，但该显式参数门较保守。完整局部收敛定理还含独立存在性和局部化条件。 |
| Alcantara, arXiv:2611.20523v1，官方提交 2026-11-16，PDF 日期 2026-11-17；Proposition 3.4 证明式(11) 后，p.9；Remark 3.5，p.11 | 证明中给 $m_\varepsilon(\beta)=(1+\sqrt{1+4\beta\varepsilon})/(2\beta)$；Remark 3.5 明写普通 PPA 平方因子 $(1+2\nu)h^2/(1+h^2)$ 及条件 $2\nu h^2<1$ | 第二项逐式相同。第一项的关键步长估计和输出误差界也同文已有。未检出作者明确陈述完整分段锐门与边界实现。 |

原文链接：

- Otero–Iusem [2010 预印本](https://webdoc.sub.gwdg.de/ebook/serien/e/IMPA_A/672.pdf)；正式版 DOI [10.1590/S1807-03022011000100002](https://doi.org/10.1590/S1807-03022011000100002)。精确公式定位采用实读预印本。
- Luke–Thao–Tam [正式 PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2017.0898)。
- Lauster–Luke [正式全文](https://link.springer.com/article/10.1186/s13663-021-00698-0)。
- Evens 等 [arXiv v2](https://arxiv.org/pdf/2305.03605v2)。
- Luke–Tam [正式 PDF](https://pubsonline.informs.org/doi/pdf/10.1287/moor.2025.0863)。
- Alcantara [版本记录](https://arxiv.org/abs/2611.20523)、[固定 v1 HTML](https://arxiv.org/html/2611.20523v1)、[固定 v1 PDF](https://arxiv.org/pdf/2611.20523v1)。

## 4. 精确换参：相同到什么程度

### 4.1 旧二次结构与 DD1 的量词差别

令 $u=y-p,w=x-y$。则

$$
\langle u,w\rangle\ge-\sigma\|u+w\|^2
\iff
\langle u,w\rangle\ge-\frac{\sigma}{1+2\sigma}(\|u\|^2+\|w\|^2).
$$

取 $r=2\sigma/(1+2\sigma)\in[0,1)$，这就是 Otero–Iusem 定义中的二次式。其 $r>0$ 版本在 $\sigma>0$ 时直接适用，$\sigma=0$ 为单调端点。又有

$$
\frac{1+r}{1-r}=1+4\sigma.
$$

所以根式常数不是新公式。旧全图点对假设强于“对每个允许近端步存在一个旧点最近锚”；相同二次式不证明两个完整定理等价。

### 4.2 Alcantara 的两项估计与 DD1

令该文 $z^k=x,q^k=x-y,w=p$、$\beta_k=1,\varepsilon=\sigma$。其式(11) 变为

$$
\langle x-y,x-p\rangle\ge\|x-y\|^2-\sigma\|x-p\|^2,
$$

这与 DD1 平方和前提等价。其证明中的 $\|q^k\|\le m_\sigma(1)d_k$ 正是

$$
s\le\frac{1+\sqrt{1+4\sigma}}2a.
$$

Remark 3.5 的 $h=\chi_A/\text{(PPA step)}$ 对应本稿 $\rho=\ell/\lambda$，$\nu=\sigma$，所以原文明确给出了第二因子。把同文的步长估计与其输出误差界相乘即可重建第一因子；取最小值和解小于 1 的条件是本库的代数比较。

必须区分：该文 Proposition 3.4 的完整定理要求存在固定 $\kappa>0$ 使所有 $k$ 均有 $\Delta_k\ge\kappa$；在普通未松弛、参数固定的 PPA 情形即 $2\sigma\rho^2<1$。因此不能直接调用其完整定理覆盖 DD1 扩展区。这里指出的是其证明中单步估计已提供所需代数构件；超出原定理门时，需独立核对估计条件、证明留域和给出锐性。

### 4.3 哪一段确实扩大了显式充分门

相对 Alcantara 明写的第二门，DD1 只在 $0<\rho<1/2$ 增加区域

$$
\frac1{2\rho^2}\le\sigma<\frac{1-\rho}{\rho^2}.
$$

例如 $\rho=1/4$ 时，第二门为 $\sigma<8$，完整锐门为 $\sigma<12$。这证明两个显式证书的覆盖不同，不能单凭此例证明新的机制或全球优先性。$\rho\ge1/2$ 的阈值与其第二门完全一致。

一般函数条件 $\sigma_R<T(\ell/\lambda)$ 允许先以二次包络控制负缺陷；这比固定写出 $\Phi=-\sigma t^2$ 灵活，但推理在包络层仍归约于固定 $\sigma$。不能仅由函数记号更一般就认定产生独立新机制。

## 5. 与团队既有 C285 的身份对应

仓库 [C285-v1 正文](../canonical/rleb_sharp_linear_frontier.md) 已有三项精确因子和分段门。设

$$
L=\sqrt{1+4\sigma},\qquad\eta=1/\rho,\qquad A=(1+L)/2.
$$

则其 $\omega(a)=La$ 反射约束等价于 DD1 平方和约束；其三项因子变为

$$
m=\min\left\{A,\rho A,\rho\sqrt{\frac{1+2\sigma}{1+\rho^2}}\right\}.
$$

其门 $L<\sqrt{1+2\eta^2}$（$\eta\le2$）、$L<2\eta-1$（$\eta>2$）正好化为 DD1 的 $T(\rho)$。C285 还给本身所定最近零锚类上的完整闭图临界反例；不可据此转称更强的全对、连续单值或固定一维子类同样锐。

本轮是给既有数学资产增加外部文献证据，没有重新发现或新增这一数学定理。Git 记录显示 C285 文件由 `24c6465` 引入；Git 时间戳和未认证公开传播均不能单独决定论文优先权。团队内部对应关系不是外部先例，也不否定作者独立整理 DD1 的价值。

<a id="dd1-scope"></a>
## 6. 搜索时发现的两个表述边界

1. **零距离退化。** 当前竞赛稿题面没有写 $a>0$。取 $x=y\in S$，两前提成立但 $0<0$ 不成立。因此严格下降题需明定 $x\notin S$；原题面未经此修补不能作为成立的全量词命题。一般收缩不等式 $t\le\kappa a$ 不受此反例影响。本轮记录问题，不静默修改题面身份。
2. **上界不等于全参数最优因子。** DD1 两项的最小值始终是上界，但全参数精确值还要考虑 $t\le b\le Aa$。例如 $\sigma=1,\rho=10$，两项最小值约为 $1.723$，而 $A=(1+\sqrt5)/2\approx1.618$ 已更小。C285 已包含该第三项。几何严格收缩的 $T$ 锐性仍成立，因为 $A\ge1$。讨论稿所述“临界线以下两项上界可达到”不由这个反例否定。

Hilbert 扩展须明确最近点存在，不能只用非空闭集；本报告精确对象限制在有限维。上述边界与新颖性分开，不把写法缺项解释成数学机制失败。

## 7. 检索覆盖与尚未排除的范围

六路主题为：普通 PPA 前驱；almost averaged/HPE；几何和公式精确检索；semimonotone/weak Minty；近期版本及引用链；独立反例和等价表述攻击。使用两种网页检索引擎及全文文献检索；决定性结论来自原文，不来自模型记忆、摘要或搜索结果排名。

以下列出**实际执行的代表检索式**，并非伪造完整检索数据库。检索包含同义词、变量替换及中文，不只检索 DD1 名称：

```text
proximal point algorithm hypomonotone metric subregularity linear convergence sharp rate Leventhal
"proximal point" "sharp" "submonotonicity"
"submonotonicity" "contraction factor"
"submonotonicity" "piecewise"
"proximal point" "subregularity" "piecewise"
"proximal" "sqrt(1+4" "subregularity"
"proximal point" "1+sqrt" "subregularity"
"proximal" "1-rho" "subregularity"
"(1-rho)/rho^2" theorem
"1/(2*rho^2)" contraction
"sharp" "distance" "nearest point" "Apollonius" contraction
"Thales" "Voronoi" "contraction"
"nearest point" "sharp" "contraction" "inequality"
"Apollonius" "Voronoi" "sharp inequality"
"nearest-point" "piecewise" "contraction factor"
"单调性" "正则性" "锐" "收缩"
"锐" "最近点" "距离" "收缩"
"almost averaged" "sharp" "contraction" error bound
"almost firmly nonexpansive" "sharp" subregularity
"quasi firmly Fejér" "sharp"
"weakly monotone" "metric subregularity" "proximal" rate sharp
"semimonotone" "error bound" "contraction"
"Regularity results for semimonotone operators"
"performance estimation" "metric subregularity" proximal point
"Generalized Monotonicity and the Proximal Point Algorithm"
"moor.2025.0863" sharp
"Luke" "Tam" "submonotonicity" "2026"
"Degenerate Preconditioned Proximal Point Algorithms as Forward Methods for Nonmonotone Inclusions"
"DD1" "proximal point"
```

还检查了 LMZ arXiv:2406.13207 的一般 gauge/KL 方向，未在所读部分定位相同分段门；这不是全篇排除证明。Le–Mordukhovich–Théra arXiv:2608.01584 的官方全文读取受阻，作者主页可确认题名，但镜像版本日期未核，故保留未核范围。全站不可检索论文、书籍、学位论文、会议讲义及等价换参结果仍可能存在。付费数据库的穷尽检索未完成。

本轮对最接近原文的判断是“未定位其明文分段锐门”，而不是“该结果不能由原文推出”。特别是 Alcantara 已有两项构件，此区别必须保留。

## 8. 下一项最有信息量的行动

先把 C285/DD1 与 Alcantara Proposition 3.4 的量词、局部窗口、允许多值关系和尖锐反例逐项并排，形成可引用的比较命题。重点检验其原文未利用的 $\rho<1/2$ 区域及几何锐性；继续沿 semimonotone、quasi firmly Fejér 和 sharp residual estimates 的引用链寻找等价结果。取得未核全文后再更新结论。

可用于对外汇报的当前措辞：

> 已有文献包含 DD1 的主要组成估计。我们在最近零锚几何下给出完整分段锐阈值及临界构形；截至本次检索，尚未找到这一完整锐结论的直接先例。

这句话报告可复核的结果与检索边界，不将“尚未发现”升级成首创认证。
