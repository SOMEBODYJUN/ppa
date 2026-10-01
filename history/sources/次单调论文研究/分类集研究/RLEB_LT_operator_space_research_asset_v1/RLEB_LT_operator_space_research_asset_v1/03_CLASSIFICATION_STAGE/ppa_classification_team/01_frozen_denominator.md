# RLEB–LT 比较的冻结分母与对象侧分子

日期：2026-09-20。任务性质：下一阶段的规格冻结和承重证明，不是新的纲大小判决。

依据：`ppa_system_team/01_ambient_axioms.md`、`02_convergence_topology.md`、`03_certificate_embeddings.md`、`06_resolvent_family.md`、`07_embedding_math_audit.md`、`08_architecture_audit.md`、`10_final_blueprint.md`。本报告不重审原 RLEB 主定理，不把紧源算子图卡的结论未经证明搬到保留域外纤维的原算子图表。

## 0. 本次冻结的准确结论

固定一个事先验证可实现的规格 \(P\)，可以把以下对象严格冻结：

\[
\boxed{
\mathfrak D_\omega^\lambda(P)
\subset\mathfrak A^{B\rightsquigarrow W}(U,S,\lambda)
\subset\mathfrak A(U,S,\lambda).
}
\]

三层都保留完整原图 \(G=\operatorname{gph}F\)。第一层只用共同实际轨道尾来定义，第二层只用共同留域来定义，第三层只用完整局部适定性和精确零集来定义；没有一层以 RLEB、LT、Hölder 指数、EB 指数或预设法向下降律为成员条件。

已独立写出的结论：

1. \(\mathfrak A(U,S,\lambda)\) 在原 Attouch–Wets 子空间拓扑中为 Polish、\(G_\delta\)，故非空时 Baire。
2. 留域层和实际尾层均相对闭，因而 Polish。
3. 实际尾层内，保留原图坐标的全时间轨道拓扑与原 AW 拓扑相同。
4. 两套理论的成员资格可直接写成原对象的反射模、完整纤维残差和标量兼容不等式；无需对证书总空间作纲推断。
5. 同步长、同工作接口下，LT 公共 all-pairs 收敛证书进入 RLEB-energy；这个包含不自动保持同一个保守尾估计。

尚未证明：上述中立分母内任何 RLEB/LT 类的稠密性、内部、第一纲或余稀性。

一个必须修正的表达：局部情形中，同胚是

\[
(F,T_F)\longmapsto F,
\]

而不是 \(F\mapsto T_F|_U\)。后者一般不单射，甚至会遗忘真实最小残差；第 3 节给出两者同属共同几何尾层的明确反例。

## 1. 冻结规格 P：哪些量不许随证明结果改变

固定

\[
P=(E,U,S,\lambda,B,W,r_*,\omega),
\tag{1.1}
\]

并满足：

- \(E=\mathbb R^d\)，\(d\ge1\)，使用原欧氏范数。
- \(S\subset E\) 非空、闭、非单点；\(U\subset E\) 开且 \(S\subset U\)。因此全局精确零集和局部精确固定点集都可以写为同一个 \(S\)。
- \(\lambda>0\) 是首轮固定步长。允许换步长的次级比较另写量词，不代换首轮对象。
- \(B\) 是非空紧初值块；\(W\) 是紧工作集，\(B\subset W\Subset U\)。首攻实例宜令 \(B\) 有非空内部，避免只比较若干离散初值。
- 定义最近解锚点集
  \[
  Q_S(W)=\bigcup_{x\in W}P_S(x),\qquad H=W\cup Q_S(W).
  \tag{1.2}
  \]
  有限维下最近点存在，且 \(Q_S(W)\)、\(H\) 紧。由 \(S\subset U\)，\(H\Subset U\)。
- 固定观察尺度 \(r_*>0\)，满足
  \[
  D_W:=\max_{x\in W}d(x,S)\le r_*.
  \tag{1.3}
  \]
  后面的两理论都在同一 \(H\)、同一 pair 尺度 \(r_*\) 上接受检验。
- \(\omega=(\omega_n)_{n\ge0}\) 是预先固定的非负、非增、趋零序列。它是实际 Cauchy 尾预算，不是某套理论给出的保守公式。
- 每个用于实际纲比较的具体规格都必须先给出一个
  \[
  F_\star\in\mathfrak D_\omega^\lambda(P)
  \tag{1.4}
  \]
  的非空性见证。没有这个见证，不称其为有意义的比较实例。

这里给出的是“任意已验证可实现规格”的总定理，不是暗中为某个预期答案选择 \(S\) 或 \(\omega\)。后来改变 \(P\) 的任何坐标，都构成另一条命题，不能与本实例的纲判决合并。

**标准首攻实例。** 可以固定非点闭凸集或正维仿射片 \(S\)，取 \(U=E\)、\(s_0\in S\)、\(W=\overline B_R(s_0)\)、\(B=\overline B_b(s_0)\)，其中 \(0<b\le R\)。取预先确定的 \(\omega\) 且 \(\omega_0\ge\max_Bd(x,S)\)。投影 \(T=P_S\) 给非空性见证，因为 \(P_S(W)\subset W\)，一次迭代后驻定；由完整表示式构造对应 \(F_\star\)。该见证只验证规格可实现，不将其他成员限定为投影、单调或法向压缩。

**为何任意 S 不能略过可实现性。** 若某个全域/前向不变层要求极限为连续回缩，则 \(S\) 的回缩几何会限制层是否非空。任意闭 \(S\)、任意初值域、任意 \(\omega\) 的组合并不自动可实现。

## 2. 完整原图、精确零集和 Polish 良定图表

### 2.1 完整原图的 AW 空间

令 \(Z=E\times E\)，\(\mathcal G=\mathrm{CL}_*(Z)\) 为非空闭子集空间。定义

\[
d_{\rm AW}(G,G')=
\sum_{j=1}^{\infty}2^{-j}
\min\left\{1,\sup_{\|z\|\le j}
\left|d(z,G)-d(z,G')\right|\right\}.
\tag{2.1}
\]

这是一个可分完备距离。简证：将 \(G\) 映到 1-Lipschitz 距离函数 \(d(\cdot,G)\)。局部一致 Cauchy 极限 \(f\) 仍为非负 1-Lipschitz 函数。因为 \(d(0,G_j)\) 有界，可取有界近似最近点并抽收敛子列，故 \(f\) 有零点。再对任意 \(z\) 取有界最近点子列，得到

\[
f(z)=d(z,\{f=0\}).
\]

所以距离函数像在 \(C_{\rm loc}(Z,\mathbb R)\) 中闭；后者为可分完备空间。有限维 proper 性在最近点子列中确实被使用。

固定 \(\lambda\)，令

\[
L_\lambda(u,v)=(u+\lambda v,u),\qquad
\Gamma_{G,\lambda}=L_\lambda G.
\tag{2.2}
\]

这是整个原图的可逆线性坐标变换，在 AW hyperspace 上诱导同胚，并且

\[
y\in J_{\lambda F}(x)
\iff (x,y)\in\Gamma_{G,\lambda}.
\tag{2.3}
\]

没有裁掉图块、输入纤维或输出纤维。

### 2.2 先加唯一局部坐标，再证明没有改变原图拓扑

取 \(U\) 的紧耗尽

\[
K_j=\{x\in U:\|x\|\le j,\ d(x,E\setminus U)\ge1/j\},
\]

空集忽略，\(U=E\) 时边界距离条件自动满足。用

\[
d_U(T,T')=\sum_{j\ge1}2^{-j}
\min\{1,\|T-T'\|_{K_j}\}
\tag{2.4}
\]

赋予 \(C(U,E)\) 标准 Polish 拓扑。定义

\[
\mathcal L_{U,\lambda}
=\{(G,T):\Gamma_{G,\lambda}\cap(U\times E)=\operatorname{gph}T,
\ T\in C(U,E)\}.
\tag{2.5}
\]

**定理 2.1。** \(\mathcal L_{U,\lambda}\) 在 \(\mathcal G\times C(U,E)\) 中闭。

证明。若 \((G_j,T_j)\to(G,T)\)，则对每个 \(x\in U\)，\((x,T_jx)\to(x,Tx)\) 给极限图的正向包含。反过来，若 \((x,y)\in\Gamma_{G,\lambda}\)、\(x\in U\)，图下极限给 \((x_j,y_j)\in\Gamma_{G_j,\lambda}\to(x,y)\)。由于 \(U\) 开，最终 \(x_j\) 在一个共同紧内球内；于是 \(y_j=T_jx_j\to Tx\)。两方向给完整等式。证毕。

令

\[
\mathcal P_{U,\lambda}=\{G:\exists T, (G,T)\in\mathcal L_{U,\lambda}\}.
\tag{2.6}
\]

这里的 \(T=T_G\) 唯一。

**定理 2.2。** \((G,T_G)\mapsto G\) 是到 \(\mathcal P_{U,\lambda}\) 的同胚，其中右侧使用原 AW 子空间拓扑。因此 \(\mathcal P_{U,\lambda}\) 是 AW-Polish、\(G_\delta\)。

逆连续性的关键证明如下。若 \(G_j\to G\) 且都在该类，而 \(T_j\not\to T\) compact-open，则存在 \(x_j\to x\in U\) 和 \(\varepsilon>0\)，使输出与 \(Tx\) 保持至少 \(3\varepsilon/4\) 的距离。图下极限另外给 \(z_j\to x\)、\(T_jz_j\to Tx\)。线段 \([x_j,z_j]\) 最终在 \(U\) 内。连续性给 \(w_j\) 位于该短线段且

\[
\|T_jw_j-Tx\|=\varepsilon/2.
\]

有限维球面紧性产生极限图点 \((x,y)\) 且 \(y\ne Tx\)，违背完整单值性。故逆连续。闭 Polish 图表与原图像同胚，后者完全可度量；度量空间中的完全可度量子空间为 \(G_\delta\)。证毕。

### 2.3 精确零集，不只含有 S

定义

\[
\mathfrak A(U,S,\lambda)
=\{G\in\mathcal P_{U,\lambda}:\operatorname{zer}F=S\}.
\tag{2.7}
\]

“含有 S”是闭条件 \(S\times\{0\}\subset G\)。排除额外零点可写成

\[
\bigcap_{j,m\ge1}\{G:d(C_{j,m},G)>0\},
\quad
C_{j,m}=\{(u,0):\|u\|\le j,\ d(u,S)\ge1/m\}.
\tag{2.8}
\]

每个非空 \(C_{j,m}\) 紧，距离条件开；空集忽略。因此 (2.7) 为 AW-\(G_\delta\)，仍 Polish。因 \(S\subset U\)，完整身份给

\[
\operatorname{Fix}(T_G|_U)=\operatorname{zer}F=S.
\tag{2.9}
\]

若只取 \(S\subset\operatorname{zer}F\)，则后面的实际 Cauchy 极限可能落在额外零点上；不能省略 exact-S。

### 2.4 一个实际可用的完备兼容距离

在闭基空间

\[
\mathcal L^S=\{(G,T)\in\mathcal L_{U,\lambda}:S\times\{0\}\subset G\}
\]

先取 \(d_{\rm AW}+d_U\)。把 (2.8) 的非空紧测试集枚举为 \(C_\ell\)，令 \(\delta_\ell(G)=d(C_\ell,G)>0\)。则

\[
\rho_{\mathfrak A}(G,G')=
d_{\rm AW}(G,G')+d_U(T_G,T_{G'})+
\sum_{\ell\ge1}2^{-\ell}
\min\{1,|\delta_\ell(G)^{-1}-\delta_\ell(G')^{-1}|\}
\tag{2.10}
\]

是 \(\mathfrak A\) 上与 AW 相容的完备距离。Cauchy 序列先在闭 \(\mathcal L^S\) 中有极限；每个倒数坐标仍 Cauchy，阻止 \(\delta_\ell\to0\)，所以极限不会新增长出额外零点。可分性来自原 AW 子空间拓扑。

## 3. 局部 T 不能代替完整 F：同一收敛动力也会丢真实残差

取 \(E=\mathbb R^2\)、\(\lambda=1\)、\(S=\mathbb R\times\{0\}\)、\(U=\mathbb R\times(-1,1)\)。定义

\[
F_0(p,r)=\{(0,-19r/9)\},
\qquad
G_1=\operatorname{gph}F_0
\cup\{((0,4/5),(0,3/10))\}.
\tag{3.1}
\]

两个图都闭，且零集精确为 \(S\)。新增图点的 proximal 输入是

\[
(0,4/5)+(0,3/10)=(0,11/10)\notin U.
\]

因此两者在整个 \(U\) 上的完整 resolvent 都是

\[
T(p,r)=(p,-9r/10).
\tag{3.2}
\]

取 \(B=W=[-1,1]\times[-9/10,9/10]\)。它对两者都前向不变，且两者的所有 B-轨道相同，并满足

\[
\sup_{x\in B,m\ge n}\|T^mx-T^nx\|
\le 2(9/10)^n.
\tag{3.3}
\]

故二者同属这个固定共同尾层。但在实际局部输出 \(u_0=(0,4/5)=T(0,-8/9)\) 处，

\[
r_{F_0}(u_0)=76/45,
\qquad r_{F_1}(u_0)=3/10.
\tag{3.4}
\]

所以：即使给出整个局部全时间轨道，也未恢复原算子的真实 EB 数据。纯局部 \(F\mapsto T|_U\) 只是一条连续遗忘映射，不是同胚；不得在其像中证明纲结论后无桥梁拉回原图类。

只有 \(U=E\) 且整个 resolvent 全域连续单值时，才有真正的一一恢复式

\[
F(u)=\{(x-u)/\lambda:T(x)=u\}.
\tag{3.5}
\]

## 4. 中立留域层和共同实际尾层

### 4.1 留域层不偷设 W 对所有点前向不变

定义

\[
\mathfrak A^{B\rightsquigarrow W}
=\{G\in\mathfrak A:\forall x\in B,\forall n\ge0,
\ x_n^G(x)\text{ 有定义且属于 }W\},
\tag{4.1}
\]

其中 \(x_0^G(x)=x\)、\(x_{n+1}^G(x)=T_G(x_n^G(x))\)。完整单值性已经消除了分支量词；没有偷换成“存在一条好分支”。

**定理 4.1。** 留域层在 \(\mathfrak A\) 中闭，且每个有限轨道映射

\[
G\longmapsto x_n^G\in C(B,W)
\tag{4.2}
\]

连续。

证明。对固定有限步数归纳。若 \(G_j\to G\)，定理 2.2 给 \(T_j\to T\) 在 \(W\Subset U\) 上一致。已知第 n 步轨道一致收敛且其值在闭集 W 内，则

\[
\|T_jx_n^{G_j}-Tx_n^G\|_B
\le\|T_j-T\|_W+
\sup_{x\in B}\|T(x_n^{G_j}(x))-T(x_n^G(x))\|\to0,
\]

后一项用 T 在 W 上的一致连续性。极限仍在 W，故可继续下一步。每个有限留域条件闭，取可数交即得结论。证毕。

### 4.2 实际尾层定义

\[
\boxed{
\mathfrak D_\omega^\lambda(P)=
\left\{G\in\mathfrak A^{B\rightsquigarrow W}:
\|x_m^G-x_n^G\|_B\le\omega_n
\quad\forall m\ge n\ge0\right\}.
}
\tag{4.3}
\]

这个定义只观察实际有限时刻轨道，不含 RLEB/LT 标签、特定正则模、证书或极限映射标签。

**定理 4.2。** \(\mathfrak D_\omega^\lambda(P)\) 相对闭于 \(\mathfrak A\)，因而 Polish；若已验证非空，则 Baire。每个成员有连续极限

\[
\Pi_G:B\to S\cap W,
\qquad
\|x_n^G-\Pi_G\|_B\le\omega_n.
\tag{4.4}
\]

证明。每个 (4.3) 不等式都是有限轨道映射的闭条件。统一 Cauchy 判据给一致极限 \(\Pi_G\)，值在闭集 W 内。连续性使

\[
T_G\Pi_Gx=\lim_n T_Gx_n^G(x)=\lim_nx_{n+1}^G(x)=\Pi_Gx.
\]

再由 exact-S 得极限在 S。令 \(m\to\infty\) 得 (4.4)。证毕。

这里不必重复添加“到 S 的统一尾”条件，因为 (4.4) 已推出

\[
\sup_{x\in B}d(x_n^G(x),S)\le\omega_n.
\tag{4.5}
\]

**回缩措辞。** 一般 B 不是前向不变集，且不含全部 \(S\cap W\)，故 (4.4) 只称局部极限/相位映射。若另外固定 \(B=W\)，则 W 自动前向不变，\(\Pi_G\) 是到 \(S\cap W\) 的连续回缩，才可写 \(\Pi_GT_G=\Pi_G\)、\(\Pi_G^2=\Pi_G\)。

## 5. AW 与全时间拓扑的冻结桥梁

在留域层定义

\[
\rho_{\rm dyn}(G,G')=
\rho_{\mathfrak A}(G,G')+
\sup_{n\ge0}\min\{1,\|x_n^G-x_n^{G'}\|_B\}.
\tag{5.1}
\]

第一项不能删除，否则第 3 节两个不同原图之间会得到距离零。

**定理 5.1。** (5.1) 是留域层上的完备距离；在 \(\mathfrak D_\omega^\lambda(P)\) 上，它与 AW 子空间拓扑相同。

完备性证明：\(\rho_{\rm dyn}\)-Cauchy 首先给 \(\rho_{\mathfrak A}\) 的极限 G；留域层闭，所以 G 仍在该层。固定每个 n 用有限时连续性识别轨道极限，再把 Cauchy 的全时间一致控制传到极限，得到 (5.1) 下收敛。

拓扑等价的承重估计为：对 \(G,G'\in\mathfrak D_\omega^\lambda(P)\)，

\[
\sup_{n\ge N}\|x_n^G-x_n^{G'}\|_B
\le2\omega_N+\|x_N^G-x_N^{G'}\|_B.
\tag{5.2}
\]

给定 \(\varepsilon\)，先用共同的 \(\omega_N\to0\) 选 N，再用有限时间连续性控制 \(0\le n\le N\)。因此层内 AW 收敛蕴含全时间收敛；反向由基图项直接成立。并且

\[
\|\Pi_G-\Pi_{G'}\|_B
\le2\omega_N+\|x_N^G-x_N^{G'}\|_B,
\tag{5.3}
\]

所以 \(G\mapsto\Pi_G\) 在这同一拓扑下连续。

**类别桥梁的准确范围。** 在这个固定实际尾层里，可以在 AW 和 (5.1) 之间无损谈同一个第一纲/余稀结论。不能由此向所有收敛者、其他尾层、变量域或变量步长空间转移类别。

## 6. 直接写在原对象上的可认证类

以下先在中立留域层上定义理论谓词，最后才与 \(\mathfrak D_\omega^\lambda(P)\) 相交。这样定理认证本身不以“已知收敛”为前提；共同留域是两理论使用的同一个中立适用接口。

### 6.1 两个内生数据

令 \(R_G=2T_G-I\)。对 \(0<\gamma\le1\)，定义完整局部反射半范数

\[
\ell_\gamma(G)=
\sup_{\substack{x,y\in H,\ 0<\|x-y\|\le r_*}}
\frac{\|R_Gx-R_Gy\|}{\|x-y\|^\gamma}
\in[0,+\infty],
\tag{6.1}
\]

空上确界约定为 0。这里检验整个声明工作集上的 all-pairs，不只检验同分支或相对解点。

完整最小残差为

\[
r_G(u)=\min\{\|v\|:(u,v)\in G\},
\tag{6.2}
\]

空值集约定 \(+\infty\)。有限维闭纤维保证非空时最小值取得。对每个 \(u\in T_G(W)\)，它有限；若 \(u\notin S\)，它严格正。

两者都由整个原对象确定。特别是 (6.2) 的值集不局限于从 W 或 U 来的逆像。

### 6.2 RLEB-direct 的对象侧规范谓词

若 \(\ell_\gamma(G)<\infty\)，令

\[
h_{G,\gamma}(r)=\frac{r+\ell_\gamma(G)r^\gamma}{2\lambda},
\qquad r\ge0,
\tag{6.3}
\]

它为严格递增的全域同胚。定义

\[
K_\gamma(G)=
\sup_{u\in T_G(W)\setminus S}
\frac{d(u,S)}{h_{G,\gamma}^{-1}(r_G(u))},
\tag{6.4}
\]

空上确界为 0。冻结的 direct 谓词是

\[
\mathsf{Dir}_\lambda(G;P)
\iff\exists\gamma\in(0,1]:
\ell_\gamma(G)<\infty,\quad K_\gamma(G)<1.
\tag{6.5}
\]

等价地，存在 \(\gamma,L,\kappa\)，其中 \(L\ge\ell_\gamma(G)\)、\(0<\kappa<1\)，使

\[
\frac{d(T_Gx,S)/\kappa+L[d(T_Gx,S)/\kappa]^\gamma}{2\lambda}
\le r_G(T_Gx)\qquad(\forall x\in W).
\tag{6.6}
\]

这是“存在任意 direct gauge”的工作输出版本的精确规范化，不计证书标签。若有原 gauge \(\psi\) 且 \(\psi(h(r))\le\kappa r\)，就有 \(\psi(t)\le\kappa h^{-1}(t)\)；反之选规范 gauge \(\kappa h^{-1}\)。所有实际输出的真实残差都不超过 \(h(r_*)\)，因为与最近解比较 RL 给

\[
r_G(T_Gx)\le\|x-T_Gx\|/\lambda\le h(d(x,S))\le h(r_*).
\tag{6.7}
\]

因此规范化没有越过被调用的 gauge 尺度。原稿若还要求更大外部输出域上的 EB，那是更强的证书域规格，不能与本工作输出谓词混称。

### 6.3 RLEB-energy 保留原普通 gauge 口径

令 \(\mathcal H_+\) 表示 \([0,\infty)\) 上从 0 出发的连续严格增无界函数。定义

\[
\mathsf{Eng}_\lambda(G;P)
\iff \exists\gamma\in(0,1],\ \alpha\in\mathcal H_+,\ q\in(0,1)
\tag{6.8}
\]

使 \(\ell_\gamma(G)<\infty\)，且

\[
\alpha(d(u,S))\le r_G(u)\quad(\forall u\in T_G(W)),
\tag{6.9}
\]

\[
\frac{r^2+\ell_\gamma(G)^2r^{2\gamma}}2
\le q\{r^2+\lambda^2\alpha(r)^2\}
\quad(0\le r\le r_*).
\tag{6.10}
\]

这里 \(\alpha=\psi^{-1}\)；写成全域函数只是消除 inverse 越界歧义，工作尺度上的普通 gauge 可以严格递增地延拓。该谓词直接施加在 G 上，没有赋予证书参数另一个类别空间。

**不能自动移植的规范化。** 旧紧源图卡中 energy 的有限参数 running-maximum 规范化，在 \(\gamma=1,L<1\) 的退化支会重新利用全部输入纤维推导线性真实 EB。局部原图的域外纤维不受 (6.1) 控制，因此该分支不能无证移植。冻结的总类采用 (6.8)–(6.10)，不预先声称 \(F_\sigma\)。

若工作比较集里含两个距离不超过 \(r_*\) 的不同解点，则 \(\ell_1(G)\ge1\)，上述退化支被排除；非退化标量规范化可另作桥梁定理。无论是否满足这个条件，都不得以标准紧源图卡的 \(F_\sigma\) 结论直接替代这里的对象侧证明。

### 6.4 LT 2025 公共 all-pairs 收敛谓词

定义

\[
\rho_*(G)=
\sup_{u\in T_G(W)\setminus S}\frac{d(u,S)}{r_G(u)},
\qquad
\tau_*(G)=\frac{[\ell_1(G)^2-1]_+}{4},
\tag{6.11}
\]

空上确界为 0，\(\ell_1=\infty\) 时令 \(\tau_*=\infty\)。冻结谓词为

\[
\boxed{
\mathsf{LT}_\lambda(G;P)
\iff
\ell_1(G)<\infty,\ \rho_*(G)<\infty,
\quad2\tau_*(G)(\lambda+\rho_*(G))^2<\lambda^2.
}
\tag{6.12}
\]

它等价于存在有限 \(\tau,\rho\ge0\)，满足同一 H/r_* 上的

\[
\|R_Gx-R_Gy\|\le\sqrt{1+4\tau}\|x-y\|,
\quad d(u,S)\le\rho r_G(u)\ (u\in T_G(W)),
\quad2\tau(\lambda+\rho)^2<\lambda^2.
\tag{6.13}
\]

由于 (6.11) 是最小有效常数，(6.12) 与 (6.13) 的等价不使用证书投影。

几何部分正是完整近端图上的 scaled submonotonicity：若 \(x=u+\lambda v\)、\(y=u'+\lambda v'\)，则

\[
\langle u-u',v-v'\rangle
\ge-\frac\tau\lambda\|(u-u')+\lambda(v-v')\|^2.
\tag{6.14}
\]

完整存在性已由共同 \(\mathfrak A\) 接口解决；本谓词比较的是 LT 2025 公共 all-pairs 收敛条件，不等同于所有历史 LT/LTT pointwise 框架，也不偷偷附加一个未经编码的矩形 maximality 谓词。

### 6.5 对象侧最终分子

\[
\begin{aligned}
\mathcal C_{\rm RLEB}^{\rm dir}(P)
&=\{G\in\mathfrak D_\omega^\lambda(P):\mathsf{Dir}_\lambda(G;P)\},\\
\mathcal C_{\rm RLEB}^{\rm eng}(P)
&=\{G\in\mathfrak D_\omega^\lambda(P):\mathsf{Eng}_\lambda(G;P)\},\\
\mathcal C_{\rm RLEB}^{\rm fixed}(P)
&=\mathcal C_{\rm RLEB}^{\rm dir}(P)\cup\mathcal C_{\rm RLEB}^{\rm eng}(P),\\
\mathcal C_{\rm LT}^{\rm fixed}(P)
&=\{G\in\mathfrak D_\omega^\lambda(P):\mathsf{LT}_\lambda(G;P)\}.
\end{aligned}
\tag{6.15}
\]

它们是同一个已固定中立分母中的原图子集，每个 F 只统计一次。

## 7. 同一实际尾输出与保守证书尾输出必须分开

设 \(D_B=\max_Bd(x,S)\)。在共同留域接口上，三种谓词分别推出真正的 Cauchy 尾：

\[
e_n^D=
\frac12\left(
\frac{\kappa^nD_B}{1-\kappa}+
\frac{L\kappa^{\gamma n}D_B^\gamma}{1-\kappa^\gamma}
\right),
\tag{7.1}
\]

\[
e_n^E=
\frac{q^{(n+1)/2}\sqrt{V(D_B)}}{1-\sqrt q},
\qquad V(r)=r^2+\lambda^2\alpha(r)^2,
\tag{7.2}
\]

\[
e_n^{LT}=\frac{bD_B\sigma^n}{1-\sigma},\quad
b=\frac{1+\sqrt{1+4\tau}}2,\quad
\sigma^2=1+2\tau-\left(\frac\lambda{\lambda+\rho}\right)^2<1.
\tag{7.3}
\]

零因子情况用一次终止的直接解释，不作 \(0^0\) 的模糊调用。

证明接口：对 \(x\in W\)、\(s\in P_Sx\)，RL 比较合法，因为 \(s\in H\)、\(d(x,S)\le r_*\)。有

\[
\|Tx-s\|^2+\|x-Tx\|^2
\le\tfrac12\{d(x,S)^2+L^2d(x,S)^{2\gamma}\}.
\tag{7.4}
\]

direct 用 (6.6) 和 selected residual 的上界给 \(d(Tx,S)\le\kappa d(x,S)\)；energy 用完整 residual EB 给

\[
V(d(Tx,S))\le\|Tx-s\|^2+\|x-Tx\|^2
\le qV(d(x,S)).
\]

逐步应用依靠已固定的共同留域条件；对步长界求尾和得到 (7.1)–(7.3)。

**本报告主比较采用实际性能口径 (6.15)。** 即对象实际满足 \(\omega\)，并能被该理论认证；不要求理论给出的保守公式就是它的实际最坏尾。

若研究“哪套理论能以纸面常数保证这个性能”，另定义带帽类

\[
\widehat{\mathcal C}_C(P)
=\{G:\exists\text{有效 C 参数，其 }e_n^C\le\omega_n\ \forall n\}.
\tag{7.5}
\]

这种性能认证类可能严格小于 (6.15)。不能把两者用同一个符号混写。

**同步长包含。** 对 (6.13) 取 \(\gamma=1\)、\(L=\sqrt{1+4\tau}\)、\(\alpha(r)=r/\rho\)（\(\rho>0\)），有

\[
q_E=(1+2\tau)\frac{\rho^2}{\rho^2+\lambda^2}<1.
\tag{7.6}
\]

若 \(\rho=0\)，所有实际工作输出在 S，另取足够陡的正线性 inverse gauge 即可。故在主实际性能口径中，

\[
\boxed{\mathcal C_{\rm LT}^{\rm fixed}(P)
\subset\mathcal C_{\rm RLEB}^{\rm eng}(P).}
\tag{7.7}
\]

该转换一般不保持 (7.5) 中的同一个纸面尾上界；那需要另证性能支配。共同留域条件已经统一，所以这里也没有偷偷缩小 B。

## 8. “存在另一步长”的分子和禁止交换的量词

对每个 \(\mu>0\)，保持同一 \(E,U,S,B,W,r_*,\omega\)，只把完整算法步长换为 \(\mu\)，从同一个原图 G 定义 \(\mathfrak A_\mu\)、\(T_{G,\mu}\)、\(\mathfrak D_\omega^\mu\) 和相应理论谓词。

**同域、同实际输出预算的存在步长 LT 类：**

\[
\mathcal C_{\rm LT}^{\exists\mu}(P)
=\left\{G\in\mathfrak D_\omega^\lambda(P):
\exists\mu>0,
\ G\in\mathfrak D_\omega^\mu(P),\quad
\mathsf{LT}_\mu(G;P)\right\}.
\tag{8.1}
\]

这数的是原 F，不把不同步长重复计数。新步长仍须在整个 U 上为完整连续单值 resolvent；不能以旧 T 的一个公式分支代替完整新 resolvent。

可用的精确图恒等式为

\[
y\in J_{\mu F}(z)
\iff \exists x:\ y\in J_{\lambda F}(x),\quad
z=(\mu/\lambda)x+(1-\mu/\lambda)y.
\tag{8.2}
\]

在纯局部图表里，右侧 x 可能落在 U 外，所以不能仅用 \(T_{G,\lambda}|_U\) 恢复新步长关系。

若想公平比较两理论的“可选步长能力”，对 RLEB 同样定义 \(\mathcal C_{\rm RLEB}^{\exists\mu}\)。逐 \(\mu\) 使用 (7.7) 才有

\[
\mathcal C_{\rm LT}^{\exists\mu}
\subset\mathcal C_{\rm RLEB}^{\exists\mu}.
\tag{8.3}
\]

但一般不能断言

\[
\mathcal C_{\rm LT}^{\exists\mu}
\subset\mathcal C_{\rm RLEB}^{\rm fixed}.
\]

若要给 LT 额外的换步长机会，再研究固定步 RLEB 的优势，正确相对集合是

\[
\mathcal C_{\rm RLEB}^{\rm fixed}
\cap\mathcal C_{\rm LT}^{\exists\mu}
\quad\text{在}\quad
\mathcal C_{\rm RLEB}^{\rm fixed}\text{中的大小}.
\tag{8.4}
\]

禁止事项：未经局部完整覆盖的步长窗口定理，不把 \(\exists\mu>0\) 改成 \(\exists\mu\in\mathbb Q_+\)；不因不可数并的每个固定步长切片小就推其并小；不把本冻结域上的“不存在 LT 步长”说成任何更小/更大域都不存在。

## 9. 最终比较表、非真空性和下一阶段承重问题

主分母固定为 \(\mathfrak D=\mathfrak D_\omega^\lambda(P)\)，拓扑固定为 AW；按定理 5.1，用 (5.1) 叙述是同一件事。

首先比较

\[
\mathcal R=\mathcal C_{\rm RLEB}^{\rm fixed}(P),\qquad
\mathcal L=\mathcal C_{\rm LT}^{\rm fixed}(P)
\subset\mathcal R\subset\mathfrak D.
\tag{9.1}
\]

| 问题 | 固定在同一个分母里的精确对象 |
|---|---|
| 覆盖的稳定内区 | \(\operatorname{int}_{\mathfrak D}\mathcal R\)、\(\operatorname{int}_{\mathfrak D}\mathcal L\) |
| 可逼近的范围 | \(\overline{\mathcal R}^{\mathfrak D}\)、\(\overline{\mathcal L}^{\mathfrak D}\) |
| 总体相对纲 | 两类各自在 \(\mathfrak D\) 内是否第一纲/非第一纲/余稀 |
| 真正新增的覆盖 | \(\mathcal R\setminus\mathcal L\) 在 \(\mathfrak D\) 中的内部、闭包、纲 |
| 两者都未认证 | \(\mathfrak D\setminus\mathcal R\) |
| 给 LT 换步长后仍新增 | \(\mathcal R\setminus\mathcal C_{\rm LT}^{\exists\mu}(P)\) |
| 纸面性能优势 | 另用带帽类 (7.5)，不与上述实际覆盖比较混写 |

**相对 RLEB 的第二级比较要检查非真空性。** \(\mathfrak D\) 是 Baire，不意味着 \(\mathcal R\) 自身 Baire。即使某处知道 \(\mathcal R\) 为 \(F_\sigma\)，也不能推出它 Baire。若 \(\mathcal R\) 第一纲于自身，则“\(\mathcal L\) 第一纲于 \(\mathcal R\)”可能没有预期判别力。要把这种相对结论翻译为“典型 RLEB 系统不属于 LT”，应先证明所用 RLEB 分母为非空 Baire，或给出其他明确的非真空性保证。

这正是下一阶段需要构建的内容之一，不能靠一条特殊反例或证书空间投影补足。

### 冻结规格表

| 项目 | 本轮冻结口径 | 未证前禁止替换为 |
|---|---|---|
| 一个成员 | 完整闭图原算子 G，固定步实例 \((F,\lambda)\) | 局部 T、证书标签、某条分支 |
| 状态几何 | 固定有限维 E 的原欧氏范数 | 为该映射专造的压缩距离 |
| 解集 | 全局 \(\operatorname{zer}F=S\)，且 \(S\subset U\) | 仅 \(S\subset\operatorname{zer}F\) |
| 局部算法 | U 上完整、全输入、单值、连续 | 选中分支或只在一条轨道成立 |
| 初值/工作域 | 固定 B、W；只要求 B 轨道留 W | 自动宣称 W 对所有点不变 |
| all-pairs 比较域 | 固定 H、r_* | 更小测试集或只对解点比较 |
| 原图拓扑 | AW；局部坐标只是唯一内生坐标 | 遗忘外部图点后的商拓扑 |
| 收敛分母 | 实际 Cauchy 尾 \(\omega\) 的闭层 | 证书指数层或预设法向收缩律 |
| 残差 | 整个 F(u) 的最小范数 | 当前 proximal 分支残差 |
| 主性能口径 | 实际满足 \(\omega\) 且可认证 | 保守公式本身必须等于实际尾 |
| 先做的步长口径 | 同一固定 \(\lambda\) | 有的成员 fixed、有的成员 exists |
| 存在步长扩展 | 同一个 F，同一域/尾，显式 \(\exists\mu\) | 自动有理化或任意独立映射族 |
| 非空性 | 先有 \(F_\star\in\mathfrak D\) | 只写一个可能为空的形式集合 |
| 泛型含义 | 指明母空间及其 Baire 性 | “绝大多数”概率、百分比 |

### 当前可以交给后续证明组的唯一主任务

在任意一个已验证可实现、事先固定的 P 上，针对 (9.1) 证明真实的内部、闭包与纲关系；若定理只对某类 P 成立，先给该类不含理论标签的结构假设，并把量词写成“对所有此类 P”。

若最后发现两类都在 \(\mathfrak D\) 内第一纲，那也是这个中立体系的真实结论，不能通过改选有利 \(\omega\) 或尖点子族掩盖。届时应研究事先声明的内生结构分层及其类别桥梁，而不是把测试实例冒充总体系。

**本报告交付的是可直接进入证明工作的冻结规格及承重定理；并未将‘框架存在’宣称成‘类大小定理已完成’。**
