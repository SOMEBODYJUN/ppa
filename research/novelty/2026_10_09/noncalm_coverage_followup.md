# 非 calm 核 PPA 的 Lyapunov/KL 反查：新增正面导入与 C212 早期推论

日期：2026-10-09 UTC。任务基线：`94cbbbd9bacb61787eeee583e0282b890455849a`。仅核 C209–C212、C218 限制和下列一级源接口；不改全局 Claim/图、不 commit。仓库实际通读 `RESEARCH_PROTOCOL.md`、`generalized_ppa_modulus.md`、`gppa_almost_averaged_bridge.md`、`gppa_nonlinear_kernel_theorem.md` NGK1–7、当日 `core_prior_art.md` / `independent_review.md`。外源阅读范围逐项在末表列明。

## 本轮新增裁决

**C218 的实际非 calm 障碍不能支撑“没有旧 Lyapunov/目标函数框架可处理”这一宽结论。** 本轮完成了两个正面桥，不再只是搜索未命中的免责声明：

1. **全部 C209 有限标量尾分支**：直接用先验标量数据构造连续势 \(L(d(z,Z))\)，对原核关系的全部允许输出满足 first-power Caristi 下降。不换坐标、不删支、不使用已经知道的轨道长度定义势。留域、未闭 \(Q\)、目标 \(Z\) 与所有物理输出量词已经完整处理。几何能量分支也满足该尾门，见下述新增代数。
2. **完整非 calm SF 的参数扇区**：当 \(\gamma\ge\nu/(2\nu-1)\)，同原坐标、同 Euclidean 度量、同完整双支关系，\(f(\xi,r)=|r|^\beta\) 满足 ABS H1–H3 和显式 KL，直接导入其 2010 作者稿 T2.9。边界等号有效。这是全 signed collar 的全轨道覆盖，不只是单条轨道。
3. **C212 的 \(q>1/2\) 长度阈值机制**：2012 Li–Mordukhovich T7.3(i) 的距离率，加其证明的平方下降，经过 dyadic-time Cauchy–Schwarz 已推出同一阈值的有限长度。前轮仅对距离逐项求和得到 \(q>2/3\)，漏掉了这条决定性的旧结果推论。因此不能把这个阈值或从弱 Hölder EB 得有限长度单列为首创。

它们不把旧抽象源自动变成“逐字覆盖任意 C209 完整 GPPA 合同”的定理。剩余精确比较对象是完整 union 真残差与 RL 如何编译为同窗 \(b,\tau\)、三分支逆端点/局部 coverage 与物理政策，而不是抽象尾和/下降收敛本身。

## 1. 全 C209 尾分支的完整 Lyapunov 归约

完整正文为 [C221 候选 TL1–TL11](../../canonical/gppa_tail_lyapunov_bridge.md)。以下重列承重合同，便于先行性判断。

从同一完整核图/图块、固定 \(\lambda>0\)、实际全 union residual EB 与已开启的评价域，NGK9–17 给每个允许核输出 \(y\)

\[
\|y-z\|\le B(d(z,Z)),\qquad d(y,Z)\le\tau(d(z,Z)).
\]

\(B,\tau\) 连续非降，\(\tau(0)=B(0)=0\)，\(\tau(t)<t\)。只需在初值 \(r=d(z_0,Z)<R\) 有

\[
L(r)=\sum_{j\ge0}B(\tau^j(r))<\infty,
\qquad L(r)<d(z_0,H\setminus U).
\]

对 \(0\le t\le r\)，每项由 \(B(\tau^j(r))\) 支配，故 M-test 给 \(L\) 连续且非降；没有额外的 \(L(t)/B(t)\) 统一缩小比率门。移项恒等式

\[
L(t)-L(\tau(t))=B(t)
\]

给 \(\Phi(z)=L(d(z,Z))\) 对**每个**允许输出满足

\[
\Phi(z)-\Phi(y)\ge B(d(z,Z))\ge\|y-z\|.
\]

这是原 Hilbert 度量中的 Caristi 条件。\(L\) 只由先验 scalar envelope 形成；没有用 actual tail 或未知极限编码结论。连续性仅在 \(d\le r\) 的有限定义域断言，若要全域函数可用 \(L(\min\{d,r\})\) 连续扩张，下降仍只在认证域。

显式 invariant set

\[
K=\{z\in Q:d(z,Z)\le r,
\ \|z-z_0\|+L(d(z,Z))\le L(r)\}
\]

包含初值且落在 \(E=Q\cap U\cap\{d<R\}\)。三角不等式加 Caristi drop 保证每个输出留在 \(K\)，因此局部 coverage 不循环。每条轨道的步长望远镜可和；在环境 Hilbert 空间完备性下收敛；\(d_k\le\tau^k(r)\to0\) 与闭 \(Z\) 给原目标 \(Z\cap U\)。不假定 \(Q\) 完备；\(Z\subset Q\) 恢复实际极限的核身份。

如果严格要求逐项满足旧 Caristi fixed-point theorem 的 complete self-map 门，all-pairs RL 给 NGK12 的唯一且 uniform-continuous 核 map，因而把 \(T:K\to K\) 延拓到完备 \(\overline K\)。下降和距离递推连续传递。延拓不是 \(Q\) 外新 GPPA coverage，原轨道保持原算法。只有 anchor RL 时不声称单值延拓，但全输出的直接望远镜结论仍成立。

**先行范围判定。** 本次实际读到 Kuhlmann–Kuhlmann–Paulsen 2018 T1 / L5 的旧 Caristi 定义与 complete-domain theorem。这条旧 theorem 本身只给固定点存在；every-orbit length 是直接 telescoping，加 \(d\)-contracting 与目标闭性才给本库精确 limit 身份。它们都是该较早下降骨架的明确数学后果。不能因此声称“1976 原文已经印出 C209”；1976 原文入口本轮未成功取到。

### 新增的几何能量包含

\[
B(t)^2\le C_\omega(t),
\qquad C_\omega(t)-B(t)^2=(t-\omega(t))^2/4.
\]

在 NGK24 的 \(R\le M\)、\(C_\omega(t)\le qV(t)\)、\(0<q<1\) 下，\(qV(t)<V(t)\le V(M)\) 保证能量 inverse cap 不触发，故

\[
V(\tau(t))\le qV(t),\quad
B(\tau^j(r))\le q^{(j+1)/2}\sqrt{V(r)},
\quad
L(r)\le\frac{\sqrt{qV(r)}}{1-\sqrt q}.
\]

这是从 scalar iteration 自身的证明，改进旧正文“energy proof 不声称 loose B-tail 一定可和”的保守描述；不是从已经得出的 actual finite length 反推 scalar summability。也将独立几何能量门接入同一势下降。

### 尚未关闭的 KL 门

该一般 \(\Phi\) 连续且 nonnegative，但没有从 C209 给出 \(\operatorname{dist}(0,\partial\Phi(y))\le c\|y-z\|\) 或 KL。Caristi 不需要这些数据。不能以 TL6 的一级下降代替 ABS 的平方下降与 subgradient relative-error 两门。Ochs 的泛距离/参数 Lyapunov 框架也仍有真正的 subgradient、KL、参数和 Euclidean step domination 门；本次读到其 Assumption H / T10 后，没有删除这些门以冒称全 C209 已导入。

## 2. 完整 signed SF 的直接 ABS 导入

原关系和 resolvent 为

\[
F(\xi,y)=\{(-A_0y^{\gamma/\nu},y^{1/\nu}-y),
(-A_0y^{\gamma/\nu},-y^{1/\nu}-y)\}\ (y\ge0),
\quad F(\xi,y)=\varnothing\ (y<0),
\]
\[
T(\xi,r)=(\xi+A_0|r|^\gamma,|r|^\nu),\quad
S=\mathbb R\times\{0\},\quad \lambda=1.
\]

Complete graph 中 \(r=\pm y^{1/\nu}\) 决定分支；输出唯一，负输入没有删去。实际 noncalm ratio \(A_0|r|^{\gamma-1}\) 仍发散。

若 \(\nu>1\)、\(\gamma\in[\nu/(2\nu-1),1)\)，取

\[
\beta\in[1+\gamma/\nu,2\gamma],\quad
f(\xi,r)=|r|^\beta,\quad \phi(s)=s^{1/\beta}.
\]

对任意 \(0<\rho<1\)、全 \(\xi\in\mathbb R\)、全 \(|r|\le\rho\)，统一常数

\[
a=\frac{1-\rho^{\beta(\nu-1)}}{A_0^2+4},\qquad b=\beta/A_0
\]

给 ABS H1/H2：设 \(u=|r|\)、\(s=\|Tz-z\|\)，则

\[
s^2\le(A_0^2+4)u^{2\gamma},\quad
f(z)-f(Tz)\ge(1-\rho^{\beta(\nu-1)})u^{2\gamma}\ge as^2,
\]
\[
\|\nabla f(Tz)\|=\beta u^{\nu(\beta-1)}
\le\beta u^\gamma\le bs.
\]

不需要 Lipschitz gradient；T2.9 的 abstract regularity 是 proper lsc。这里甚至得到 convex C¹ objective。\(u_{k+1}\le\rho^{\nu-1}u_k\) 保持 full normal collar，tangential coordinates 由几何上界 \(A_0u_0^\gamma/(1-\rho^{\gamma(\nu-1)})\) 有界；有限维产生 cluster subsequence，\(f\) 连续给 H3。这一步不引用 C209 的收敛。最后

\[
\phi'(f(z))\operatorname{dist}(0,\partial f(z))=1\quad(r\ne0),
\]

给 exact KL。该源 T2.9 对每条从任意 \(\xi_0\)、\(|r_0|\le\rho\) 起步的 complete SF 轨道给有限长度和点收敛，零集等于 \(\operatorname{argmin}f\)。边界 \(\gamma=\nu/(2\nu-1)\) 唯一可选 \(\beta=2\nu/(2\nu-1)\)，两指数门均取等，仍成立。例 \(\nu=3,\gamma=3/4,\beta=3/2\) 具有 noncalm 比率 \(r^{-1/4}\)，却有此原坐标导入。

**Fatal 外推。** 非 calm 排除 finite almost-averaged 并不排除 ABS；此完整参数扇区已经是反例。另一方面，较低 \(\gamma\) 时该 power candidate 的区间为空，不是“任何 lsc objective 均不存在”的证明。全 C209、log witness、无限维空间、随步长变化、任意 physical inverse 政策没有被这个二维特例覆盖。

另已完成真正的 C¹ complementary-sector 证明，见候选 TL21–24：若 \(\gamma<\nu/(2\nu-1)\)，在 \(\mathbb R\times(-\rho,\rho)\) 不可能有任何 C¹ 目标满足所有正输入的固定 H1/H2。全正输出 coverage 把 H2 转成 \(\|\nabla f(\xi,y)\|\le Cy^{\gamma/\nu}\)；C¹ 强迫零线梯度零及同一常值 \(c\)；正常积分给 \(|f(\xi,r)-c|\le C' r^{1+\gamma/\nu}\)。独立的显式 SF 轨道收敛和 H1 给 \(f(\xi,r)-c\ge aA_0^2r^{2\gamma}\)，低 sector 的指数矛盾。故这里得到**同原坐标全正 collar C¹ H1/H2 可行性**的确切参数分界，等号属于正面 sector；它仍不排除 nonsmooth/lsc 目标，且不自动适用于 bounded tangential collar。

## 3. C212 长度阈值是 2012 距离率的可写明推论

### 一级源的严格覆盖角

Li–Mordukhovich 修订稿 2012-10-12 T7.2/T7.3：\(A:H\rightrightarrows H\) 极大单调，\(p\in A^{-1}(0)=S\)，Hilbert 空间；在 \(B(p,\delta)\) 有 full true residual EB \(d(z,S)\le K r_A(z)^q\)。从 \(z_0\in B(p,\delta)\) 起步的 exact PPA，固定 \(\lambda>0\)，其 T7.3(i) 给

\[
d_k=d(z_k,S)=O(k^{-\alpha}),\qquad
\alpha=\frac{q}{2(1-q)},\qquad0<q<1.
\tag{NC1}
\]

其 T7.2 证明 (7.7) 保证留在同一个 \(p\)-ball，并给相同轨道的平方下降

\[
d_k^2-d_{k+1}^2\ge s_k^2,
\qquad s_k=\|z_{k+1}-z_k\|.
\tag{NC2}
\]

源正文没有在 T7.3 陈述 finite length；以下是本轮完整推论，不假称源印出同一表述。

### 完整 dyadic-time 归约

选 \(N_0\ge1\) 和 \(C\) 使 \(d_N\le CN^{-\alpha}\) 对 \(N\ge N_0\) 成立。Cauchy–Schwarz 加 NC2 在每个时间块给

\[
\sum_{k=N}^{2N-1}s_k
\le\sqrt N\left(\sum_{k=N}^{2N-1}s_k^2\right)^{1/2}
\le\sqrt N\,d_N
\le C N^{1/2-\alpha}.
\tag{NC3}
\]

把 \(N=2^jN_0\) 代入并对 \(j\ge0\) 求和。因为

\[
\frac12-\alpha=\frac{1-2q}{2(1-q)}<0
\quad\Longleftrightarrow\quad q>\frac12,
\]

所以 tail length

\[
\sum_{k=N_0}^{\infty}s_k
\le\frac{C N_0^{1/2-\alpha}}{1-2^{1/2-\alpha}}<\infty.
\tag{NC4}
\]

有限前缀单独加入，得到 finite length；完备与闭 \(S\) 给原零集点收敛。更一般 \(N\ge N_0\) 的尾不超过同式把 \(N_0\) 换成 \(N\)，故 \(\|z_N-z_\infty\|=O(N^{-(2q-1)/[2(1-q)]})\)。\(q=1\) 使用源 T7.3(iv) 的几何距离率及 \(s_k\le d_k\) 直接可和；不把含 \(1-q\) 的式子代入 \(q=1\)。\(q=1/2\) 时该 time-block 上界只是常数量级，无必要性结论。

例 \(q=3/5\)：source distance exponent \(3/4\)，逐项求和发散；time-block length exponent 是 \(-1/4\)，dyadic block series 可和。这正是前轮 \(2/3\) 比较的遗漏。NC3 不需要步长大小单调，亦不需要 nearest point attainment。

### 全 C212 与源极大性的边界

源 T7.3 使用全 \(S=\operatorname{zer}A\)、极大单调、全 Hilbert coverage、一个 reference-ball 的 local EB。C212 允许局部 pair-monotone 图块、\(Q\)-coverage、指定闭 \(Z\subset\operatorname{zer}A\)、完整 union EB 和初值领圈预算。不能用标题/阈值相同，把这些前件默认为源前件。

在 C212 合同内，NGK27 已给 NC2 和

\[
d_k^2\ge d_{k+1}^2+\lambda^2K^{-2/q}d_{k+1}^{2/q}.
\tag{NC5}
\]

因此同一旧 scalar-rate machinery 在合法有限前缀上可直接重建，随后 NC3–4 提供另一种长度机制。具体自足 rate 常数：\(a_k=d_k^2\)、\(p=(1-q)/q>0\)、\(c=\lambda^2K^{-2/q}\)，若 \(a_0>0\)，令

\[
\Delta=\min\{pc/2^{p+1},(2^p-1)a_0^{-p}\}>0.
\]

若 \(a_{k+1}\ge a_k/2\)，积分 \(p\int_{a_{k+1}}^{a_k}t^{-p-1}dt\) 给 \(a_{k+1}^{-p}-a_k^{-p}\ge pc/2^{p+1}\)；若 \(a_{k+1}<a_k/2\)，则差至少 \((2^p-1)a_k^{-p}\ge(2^p-1)a_0^{-p}\)。归纳得

\[
a_k\le(a_0^{-p}+k\Delta)^{-1/p}.
\tag{NC6}
\]

到零之后由 absorption 停住，退化 \(a_0=0\) 也直接停住。该证明只用 NC5，故不假借极大性。无穷 coverage 和留域仍需 C212 的严格长度预算；NC6+NC4 形成的粗 budget 不一定等于原 shell 最优 budget。故：**threshold finite-length mechanism 已有 2012 结果的显式推论；C212 的完整局部量词/常数 theorem 没有被源逐字直接包含。**

不能通过任意 maximal monotone extension 偷掉这些门：扩张图可能引入新零点，改变 target distance，亦可能给原输出加入更小图值，使 old-target full residual EB 失效。具体合格反例：原单调图 \(\{(0,0),(1,1)\}\) 的指定目标 \(Z=\{0\}\)，原输出 1 有 \(d(1,Z)=r_A(1)=1\)；极大单调扩张 \(M=\partial h\)，\(h(x)=\frac12(x-1)_+^2+(x-1)_+\)，在 \(x=1\) 有 \(M(1)=[0,1]\)，包含原图且 \(r_M(1)=0\)，于是任何零消失 gauge 的同 \(Z\)-EB 失败。它还有新增零点 \(( -\infty,1]\)。不把 extension 的新目标当成旧 \(Z\)。

## 4. Wang–Li–Ng 2023 全文的实际结果

子任务由独立代理定向搜索 SIAM full/pdf、CUHK institutional record、作者 HZNU 页面、SWUFE 官方 talk 和作者/题名 preprint 路线。SIAM full/pdf 均 redirect 到 abstract + get-access wall；没有取得 main-theorem 正文。可读 publisher preview 只有印刷 p1996。SWUFE 2025-04-08 官方 talk 也只有摘要，无 slides/附件。

因此本轮仍不能把 finite length、任何具体 \(q\) 门、inexact 条件或 theorem 编号归给 Wang–Li–Ng。此处开放的是**该文的精确 attribution**，而不是 C212 阈值机制的先行可能性：上一节的 2012 全文归约已经给出实际覆盖事实。

## 5. 实际一级源读取范围、URLs 与 web 路由

页码为 PDF 一基物理页；括号给印刷页或 crawler 的零基 P 索引。没有把 search snippet 当 theorem proof。

| 一级源 | 完整 URL；本轮 web refs | 实际读范围 | 使用门/仍未审范围 |
|---|---|---|---|
| ABS，作者稿 2010-12-15 | https://optimization-online.org/wp-content/uploads/2010/12/2864.pdf ; `turn38view0`, `turn61view0`–`turn61view2`, `turn44view0`–`turn44view1` | PDF5 定义 limiting subgradient；PDF7 D2.4；PDF8 H1–H3；PDF8–11 L2.6、C2.7–2.8；PDF12 T2.9/完整证明入口 | finite-dimensional proper lsc、fixed H1/H2、function-attentive cluster、KL。只对显式 SF 原对象做全门归约；§3–6应用未复审。 |
| Kuhlmann–Kuhlmann–Paulsen 2018 | https://link.springer.com/article/10.1007/s11784-018-0576-8 ; `turn52view0` | §1 T1 crawler L73–89；§2 L5/proof L145–195；§3部分 proof L199–249 | complete metric self-map、lsc bounded-below、Caristi inequality；T1原输出只是存在固定点。一般ballspace其它应用未重审。 |
| Caristi 1976/ Kirk 1976 原入口 | https://www.ams.org/tran/1976-215-00/S0002-9947-1976-0394329-4/S0002-9947-1976-0394329-4.pdf ; https://www.impan.pl/en/publishing-house/journals-and-series/colloquium-mathematicum/all/36/1/101485/caristi-s-fixed-point-theorem-and-metric-convexity | AMS403；IMPAN官方 bibliographic 页面可读，download403；EU DML timeout | 不声称读原1976 theorem；可读2018 primary paper的 theorem足够给较早覆盖骨架。 |
| Ochs，作者稿 2017-11-21 | https://optimization-online.org/wp-content/uploads/2017/11/6333.pdf ; `turn106view0` | PDF3 finite-dimensional standing space；PDF4 D2/limiting subgradient；PDF6 Assumption H、H1–H5；PDF10–12 T10 statement/proof | generic distance不删除KL/relative-error，Euclidean length另需实际步被generic distance统一控制。参数/应用§4–6未逐条重审。 |
| Li–Mordukhovich，修订稿2012-10-12 | https://web.maths.unsw.edu.au/~gyli/papers/lm-subreg12final.pdf ; `turn63view0`,`turn66view0`–`turn66view1`,`turn68view0`–`turn68view1` | PDF5 D3.1；PDF26–27 T7.2 完整平方残差证明(7.7)–(7.10)；PDF28 T7.3(i)/(iv)与(i) proof引用；§7相邻 L7.1 proof显示 scalar split | 固定步长/source maximal case已经足够 NC1–4；不调用 T7.3(ii)/(iii) varying-step部分，其写成 O lower-bound使用也未独立认可；§3–6 calculus未复审。 |
| Wang–Li–Ng，SIAM2023 | https://epubs.siam.org/doi/full/10.1137/22M152147X ; https://epubs.siam.org/doi/pdf/10.1137/22M152147X ; `turn64view0`（独立子代理 `turn9view0`） | publisher摘要 crawler L53–86；metadata L514–538：submitted2022-09-12, accepted2023-02-27, published2023-08-04 | main theorem全文被access wall阻断；不作finite-length attribution。 |
| Wang–Li–Ng官方机构线索 | https://research.cuhk.edu.hk/en/publications/convergence-rate-of-inexact-proximal-point-algorithms-for-operato-2/ ; https://math.swufe.edu.cn/info/1089/23331.htm ; `turn64view1`（子代理 `turn35view0`） | CUHK abstract/access links；SWUFE L80–100 talk abstract；作者 https://sxxy.hznu.edu.cn/c/2021-08-11/2574019.shtml 无publication列表 | 无公开deposited manuscript/slides。RG p1996 publisher preview https://www.researchgate.net/publication/372932490_Convergence_Rate_of_Inexact_Proximal_Point_Algorithms_for_Operator_with_Holder_Metric_Subregularity 仅作为publisher preview定位，不作为主 theorem证据。 |

## 6. 验证、fatal objections 与可用措辞

运行：`python3 research/code/gppa_novelty/noncalm_coverage_followup_check.py`。Python标准库；Fraction exact 441 energy identities；Decimal70位 132 nonlinear scalar tail identity/inequality；4参数 sectors含两个 threshold equality，1280 signed SF tests；180步 energy scalar iterates；4096步隐式 scalar recurrence；12个 dyadic blocks。全部 PASS。最大 SF H1 ratio 0.59175，H2 ratio 1.0000000000000102（浮点等号误差），KL error \(1.03\times10^{-14}\)。有限算术只检查公式/边界，不证明 infinite statements。

独立代理已完整重构 TL1–TL20，实际重读 ABS H1–H3/T2.9 和 Caristi T1，运行上述脚本，未发现 fatal；另一代理已独立核 LM2012 NC1–4、目标/局部预算和 TL11。后加的 TL21–24 又单独收到完整独立重构，gradient output coverage、zero-line常值、normal积分与 strict低sector指数均无 fatal。本文不自行升状态；最终身份接收由主代理归档。

| Fatal 外推 | 明确关闭理由 |
|---|---|
| 非 calm SF不能由任何 old objective theorem处理 | TL14–20 是原坐标完整图的显式ABS正面归约。 |
| 无objective是假设特色，所以不存在Lyapunov表示 | \(L(d)\) 势直接由scalar data形成；不要求原算子是subgradient。 |
| Caristi theorem直接印出全C209 | source只提供抽象complete-domain固定点骨架；RL/true EB→scalar编译仍需本库证明。 |
| tail potential自动KL、自动满足ABS H2 | 没有gradient/slope界；只对explicit SF sector证明了ABS门。 |
| q>1/2 shell finite length可列主首创候选 | 2012已读rate + square descent经NC3–4完整推出该阈值。 |
| maximal extension自动使旧结果涵盖全C212 | extension可改变zero target与full residual；上节有具体合格图反例。 |
| 未取得Wang正文意味着monotone finite length gate仍全开放 | attribution开放；2012已读结果足以关闭阈值机制首创主张。 |

可用的新措辞：**固定核完整 GPPA 的 RL/真残差编译和三分支同窗合同已经形成条件统一定理；其有限长度部分有显式先验尾和 Lyapunov 表示，实际非 calm 例中的一扇区还可在原坐标直接导入经典 KL 抽象收敛。C212 的 \(q>1/2\) 阈值机制是早期距离率与平方下降的显式推论。剩余候选只应保留精确完整对象/域/物理接口的组合，不再把无目标、非 calm 或该长度阈值单列为首创证据。**
