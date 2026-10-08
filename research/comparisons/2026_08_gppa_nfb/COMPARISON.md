# 8 月两篇论文与本项目的逐项比较

**裁决：两篇都有实质重合，但都不能涵盖本库全部明定收敛对象。** 这要求收紧收敛稿的创新表述；现有证据没有支持“完全重复”，也没有完成全球先行性认证。本文件综合逐篇原文审查和独立攻击，完整证明在 [GPPA 报告](gppa_review.md)、[NFB 报告](nfb_review.md) 与 [独立审计](independent_attack.md)。

比较的数学状态、附件身份和四层判别契约见 [BASELINE](BASELINE.md)。本库的完整原图、局部图块、普通 PPA、warped PPA 与升维算法保持各自身份，不因有相同零集而混合。

<a id="papers"></a>
## 1. 固定的是哪些论文

| 首发日 | 作者与固定版本 | 本次实读位置 |
| --- | --- | --- |
| 2026-08-03 | Le–Mordukhovich–Théra，*Convergence and Stability Analysis of a Generalized Proximal Point Algorithm and Its Inexact Version*，[2608.01584v1](https://arxiv.org/abs/2608.01584v1)；PDF 首页另印 August 4 | Definition 1/3/4/5/6；Theorem 1 p.6，Theorem 2 pp.7–8，Lemma 3 pp.8–9，Theorem 4 pp.9–11；关键原式另渲染核对 |
| 2026-08-24 | Pesquet–Roldán，*Nonlinear Forward-Backward Algorithm for Solving Non-monotone+Lipschitz Inclusions with Applications to Adjoint Mismatch Problems*，[2608.22687v1](https://arxiv.org/abs/2608.22687v1) | §3 的 Assumption 3.1、Algorithm 3.7、Theorem 3.10；§4 标准 primal–dual lift 与 rate 门；§5 例子；关键指标原式另渲染核对 |

两份版本原文均已存入 [sources](sources/manifest.json)，字节哈希和下载来源可复核。截至 2026-10-08 的 arXiv 页面均只列 v1。本轮不推测未列出的修订。

<a id="verdict-table"></a>
## 2. 先按数学主张分开判断

| 本库主张 | GPPA v1 | NFB v1 | 应如何表述 |
| --- | --- | --- | --- |
| C02-v2 的 RL + 真 EB + 严格兼容 + 留域，得到普通物理点几何尾 | 有真实重合子类；非单调非 calm 的 C191 子类也能覆盖 | 有真实非单调重合，例如完整 F=−Id、普通步长3 | 不能笼统声称此前没有非单调 PPA 点线性收敛 |
| 几何物理点尾下的有限长度 | 点范数率已有时直接随附；非单射核的率本身则不够 | Theorem 3.10(ii) 已给物理范数 R-linear，因而有限长 | 有限长度不能在这些子类单独充当创新 |
| C137 的严格 RLEB 完整 cap 原图及指定普通轨道 | 任意正步长、任意非线性/非单射 ε-ASM 核都不能保留该轨道 | 任意合格同空间拆分及固定合法度量都被必要二次锚阻断 | 是两个指定框架均未涵盖的明确完整实例；不是全球新颖性证明 |
| C141 完整双支超线性族 | 指定正法向轨道受同一任意 ASM 核障碍；单有某个较慢线性上界不等于表示成功 | 指定非退化图也违反固定二次锚 | 同时讨论完整算法身份和精确物理尾，不只比“线性/超线性”字样 |
| C09/C10 一般模、Dini 长度及完整对数门槛 | C10 正法向轨道受完整双支障碍；核率不自动恢复其物理 Dini 尾 | C10 完整图违反必要二次锚；Theorem 3.10(i) 在本库有限维不能只因写 weak 而被排除 | a>1 的有限长度与 a≤1 的切向发散分开；后者不是 C09 的正面实例 |
| C191/C192 自然类全部原数据 | 一个 C191 子类已真实重合；一般数据的核分类仍开放 | 非退化 C193 二次锚失败排除同空间全部合格拆分 | 不能从“非 calm”推出 GPPA 总排除，也不能宣称整个自然类只可用本库机制证明 |
| C11/C137/C141 的极限回缩、两点模和同图锐阶 | 原文未给同一组输出 | 原文未给同一组输出 | 原文未给不等于全球首创；应逐结果核先行性 |
| C03/C04/C18/C19/C20-v2 的影子、完整纤维、覆盖、有限 QP | 主要收敛结果没有给这些同身份结构结论 | 主要分裂/收敛结果没有给这些同身份结构结论 | 此为另一条结构线，须单独核 Ciosmak 等相关文献 |

<a id="gppa-overlap"></a>
## 3. 8 月 3 日：不能回避的真实重合

原算法的核心是

\[
v(x_k)-v(x_{k+1})\in hF(x_{k+1}),\qquad h>0,
\]

不是一般的 \(x_k-x_{k+1}\in hF(x_{k+1})\)。其 Theorem 2 允许任意单值、非线性、非单射核，只要求完整 all-pairs 条件

\[
\langle f-g,v(x)-v(y)\rangle\ge\varepsilon\|v(x)-v(y)\|^2
\quad((x,f),(y,g)\in\operatorname{gph}F),\quad\varepsilon>0,
\]

以及非空零集、warped 输入 coverage；距离率另要求 \(F^{-1}\) 在0 R-Lipschitz。把它说成只许 \(v=Id\)、只处理普通单调图，是错误的。

**C199 的具体非平凡重合。** 取同一完整法锥关系

\[
F(t,y)=\{(-2y^{2/3},7y+n):n\in N_{\mathbb R_+}(y)\}
\quad(y\ge0),\qquad F(t,y)=\varnothing\ (y<0).
\]

其完整零集为 \(\mathbb R\times\{0\}\)，完整边界图值 \(F(t,0)=\{0\}\times(-\infty,0]\) 全部保留。普通步长1的完整近端为

\[
T(t,y)=\bigl(t+2(y_+/8)^{2/3},y_+/8\bigr).
\]

在输入对尺度 \(R=1/8\)，本库严格 RLEB 可取 \(L_R=3/2\)、真 gauge \(\psi(s)=(s/2)^{3/2}\)、兼容因子 \(\kappa=1/(2\sqrt2)<1\)；完整纤维、零锚、coverage 和全空间留域均已核。

现在取 GPPA 步长 \(h=3/10\) 和

\[
v(t,y)=\left(-\frac15(y_+)^{2/3},\frac3{10}y_+\right).
\]

完整 all-pairs 的 adaptive 常数可取 \(\varepsilon=10\)，\(F^{-1}\) 全局 R-Lipschitz 常数 \(1/7\)，完整 warped 纤维恰为

\[
J^v_{hF}(t,y)=\mathbb R\times\{y_+/8\}.
\]

所以每一条普通 PPA 轨道都是 GPPA 的合法选择。对非负初值，\(I=t_k+(2/3)y_k^{2/3}\) 是一步代数不变量；取预先确定的解 \(x^*=(I,0)\)，沿普通选择有

\[
v(x_k)-v(x^*)=\frac3{10}(x_k-x^*).
\]

因此 source Theorem 2 的核率可直接转成这条同一物理轨道的点 R-linear 率及有限长度，不必循环地先假设它已经收敛。负法向初值一步到零法向，随后驻定。该例普通图不单调、近端在零点非 calm；这些标签不足以区分两种方法。

这个重合属于**同原图、全部普通轨道包含**。warped 纤维的切向输出自由，普通纤维唯一，故完整算法并不相等。反之 \(F=aId\) 的适当普通子类连完整算法都相等。

<a id="gppa-barrier"></a>
## 4. 8 月 3 日：完整双支给出的任意核排除

**C200 固定 C137 完整 cap。** 在 \(\eta\le0,y\ge0\) 的区域，两条完整图值是

\[
f_+(y)=(-2\sqrt y,0,3y),\qquad
f_-(y)=(-2\sqrt y,0,-5y).
\]

原 cap 在区域外的完整定义和所有近端纤维见 [C137](../../canonical/selection_geometric_cap.md#gc-object)，不作删支。普通步长1、初值 \(x_0=(0,-1,1/64)\) 的轨道满足

\[
\eta_k=-1,\qquad y_k=4^{-k}/64>0,\qquad
\xi_{k+1}-\xi_k=\sqrt{y_k}.
\]

本库全部严格 RLEB 门在 \(R=1/16\) 成立：\(\psi(s)=s^2/4\)、\(L_R=2\sqrt2+3/8\)、\(\kappa=(2\sqrt2+5/8)^2/16<1\)，完整普通近端全输入唯一，轨道物理有限长。

任意 \(\varepsilon\)-ASM 核若作用于这张完整图，则：

1. 同法向、同支的图值相同，ASM 强迫核折叠切向变量，即 \(v(\xi,\eta,y)=q(y)\)。
2. 同支比较经 Cauchy 给 \(q\) 在每个正法向紧区间局部 Lipschitz；这是由前件推出，没有预设核连续性。
3. 两个方向的跨支比较共同强迫 \(|q_3(y)-q_3(z)|\le K|y-z|^2\)。把区间细分并求和，得 \(q_3\) 在正法向区间恒定。
4. 保持普通轨道时 GPPA 正常分量必须满足 \(0\in h\{3y_{k+1},-5y_{k+1}\}\)，但 \(h>0,y_{k+1}>0\)，矛盾。

这排除了**任何非线性或非单射 ASM 核、任何正步长、甚至允许重新选择另一图值**来保留该轨道，不只是证明 \(v=Id\) 不行。相同正轴光滑双支论证适用于 C141 与 C10 的指定非驻定正法向轨道，详见逐篇报告。

量词边界必须保留：常量核总可能满足 ASM 并一步跳入零集，排除的是它保留上述普通轨道；mere pair-monotone 且无核正则性的 Theorem 1 表示未被本证明排除；删支、换图和任意 lift 仍需新身份。局部证明须保留切向开片、连通正法向区间及完整两支，不能只保留离散轨道采样。

<a id="nfb-overlap"></a>
## 5. 8 月 24 日：已有物理点线性率，且确有非单调重合

Theorem 3.10(i) 给 weak convergence；在本库的有限维空间中 weak 与 strong 一致，不能用这个词制造差异。(ii) 在解锚半单调强化 \(\mu>0\) 和正下降系数下给唯一物理解及范数 R-linear。物理 R-linear 尾界 \(\|x_k-x^*\|\le Mq^k\) 自动给

\[
\sum_{j\ge k}\|x_{j+1}-x_j\|
\le\frac{M(1+q)}{1-q}q^k.
\]

**C202 真实重合。** 完整 \(F=-Id\)、普通步长3有 \(J_{3F}=-Id/2\)、反射 \(-2Id\)、真 gauge \(\psi(s)=s\)；本库 \(\gamma=1,L=2,\kappa=1/2\) 严格兼容且全空间 coverage。外部取 \(A=F,C=0,S=Id,M=Id/3,\tau=3,\theta=1,\zeta=0,\rho=-11/10,\mu=1/10,\beta=100,u_0=0\)，所有 source 门和正下降系数成立，Algorithm 3.7 恰成为同一完整普通 PPA。它不是仅限强单调图的重合。

纯旋转例 \(F=K\) 也可由其半单调率门覆盖；它在本库 C24 已收敛，但该例原参数不满足 C02 的严格兼容，因此只作 C24 结论的先例，不能误称 C02 重合。相关精确系数复算及非零 forward 项吸收实例见 NFB 报告。

<a id="nfb-necessary"></a>
## 6. 8 月 24 日：任意同空间拆分都须满足的门

**C201 的必要条件不只测试 \(C=0\)。** 假设同一完整 \(F=A+C\) 存在 NFB Assumption 3.1 合格拆分。\(S\) 是固定有界自伴强单调度量，\(C\) 是 \(\beta\)-cocoercive，\(A\) 在解图对满足 \(\rho S^{-1}\)-comonotonicity，\(\rho>-\beta\)。

任意零锚 \((z,0)\in\operatorname{gph}F\)、任意完整图点 \((x,f)\)，令 \(c=Cx-Cz\)。两个 source 前件给

\[
\begin{aligned}
\langle x-z,f\rangle
&\ge\rho\|f-c\|_{S^{-1}}^2+\beta\|c\|_{S^{-1}}^2\\
&=(\beta+\rho)\left\|c-\frac{\rho}{\beta+\rho}f\right\|_{S^{-1}}^2
 +\frac{\beta\rho}{\beta+\rho}\|f\|_{S^{-1}}^2\\
&\ge\frac{\beta\rho}{\beta+\rho}\|f\|_{S^{-1}}^2.
\end{aligned}
\]

这是一条对**原完整 F 本身**的固定二次零锚下界，和 \(M\) 如何选择无关。因此任意合法同空间 \(A+C\) 拆分、任意合法固定 \(S\) 与 kernel \(M\)，都绕不过它。

非退化 C193 对每个固定有限矩阵二次锚都有局部失败序列。其核心是选 \(0<\eta<\alpha\) 使

\[
\langle x_\epsilon-z,f_\epsilon\rangle
\le-c\epsilon^{\alpha+\eta}+O(\epsilon^2),\qquad
\|f_\epsilon\|^2=O(\epsilon^{2\alpha}),
\]

而 \(\alpha+\eta<2\alpha\)。图点和残差都趋向同一零锚，故缩邻域、改变有限矩阵也无法补救。退化 \(C=\{0\}\) 的自然类例外另保留。C137、C141、C10 的完整图也有同样的固定二次锚失败，详见 NFB 报告中的显式序列。

<a id="nfb-lift"></a>
## 7. 标准 primal–dual lift 的边界也核了

**C203** 针对该文 §4 的标准完整 product 关系

\[
\mathcal K(z,v)=((A+C+D)z+L^*v,\ B^{-1}v-Lz).
\]

要求同一 \(\mathcal K\) 在 product 空间满足 NFB Assumption 3.1，特别是 product 前向的 \(\beta\)-cocoercivity、\(\rho>-\beta\)、全部 product 解图锚的 comonotonicity 与固定有界正定度量。若它还逐图值保持原图 \(F=A+C+D+L^*BL\)，则每个 \(f\in F(z)\) 都有 lift \(((z,v),(f,0))\in\operatorname{gph}\mathcal K\)，并且原零点有 product 零点。对这两个 product 图点应用上一节必要条件，得到

\[
\langle z-s,f\rangle\ge
\frac{\beta\rho}{\beta+\rho}
\langle(f,0),S_{\rm prod}^{-1}(f,0)\rangle.
\]

把固定 product 矩阵压缩到原空间，仍是原图的固定二次锚，与 C193 等失败序列矛盾。原文全图条件不要求所选辅助 \(v\) 靠近零点辅助变量。若另立局部 lift 定理，则还需局部全图保真门，不能默用此全局结论。

因此这里已排除这个指定标准 lift，不是只说“还没核升维”。结论仍不覆盖任意自创高维关系、改变算法或只保留零集的表示；那些需逐一证明全图、算法及物理回代。

<a id="positioning"></a>
## 8. 稿件定位应如何改

不宜再用这些表述承担创新：一般非单调 PPA 首次点线性收敛；已有物理点几何尾之外单独强调有限长度；“我们的例非 calm，所以 GPPA 不适用”；“NFB 只弱收敛或只强单调”；仅核 \(C=0\) 后宣布 NFB 任意拆分不适用。

更准确的收敛稿定位应落在已证明的接口：同一普通 PPA 的全对反射模与真实残差如何匹配；完整双支保留下的 coverage、唯一纤维和局部留域；指定完整图无法被这两个框架保持的证明；一般模/Dini 的物理尾、完整对数门槛，以及同图极限回缩与两点锐阶。自然类还应承认已有独立法向—切向收敛机制，不能把 RLEB 证书说成唯一证明路径。

可据本轮证据使用的比较文字为：

> GPPA 与半单调 NFB 已为若干非单调问题给出线性收敛保证，本工作的部分子类亦落入这些框架。本文关注固定完整原关系的普通 PPA，按全对反射模、真实残差及统一兼容给出局部物理尾和留域证书。完整双支实例显示，这些证书可用于无法由 GPPA 的 adaptive 强核保持原轨道、且不满足 NFB 任意同空间拆分及指定标准 primal–dual lift 必要二次锚的图。一般模结果另给出 Dini 长度门及完整对数边界。上述比较针对明确版本与保真范围，不宣称对一切表示的总排除。

本轮附件正式稿主要是 **C03/C04/C18/C19/C20 的结构与纤维线**，并非 C02 收敛稿。两篇主要收敛论文没有给出该稿同一组影子、全纤维实现和有限 QP 定理；本轮子类重合不能据此裁定整份正式稿重复。结构线的先行性，特别 Ciosmak 2024/2026 等扩张结果，仍需独立逐定理审核。

<a id="remaining"></a>
## 9. 审查闭合范围与剩余任务

本轮闭合：固定 v1 的相关原文身份；真实重合的合法实例；C137 任意 ASM 核同轨道障碍及指定双支推广；NFB 任意同空间拆分的必要条件；指定标准 full-graph primal–dual lift 的压缩障碍；有限长度定位修正。逐篇报告和独立报告记录实际阅读与计算范围，互审按证明而非人数表决。

仍未闭：一般 C191/C192 的全部核分类；无正则性 mere-monotone GPPA 表示；任意保真自定义 lift/改变算法；连续回缩与锐阶的全球先行性；Ciosmak/Spingarn 等其它论文的逐定理比较；总体参数中立母空间与规模量尺。这些不能由本轮不涵盖见证、有限 PASS 或文件归档替代。

GPPA Theorem 4 的正则化误差稳定性另有本库列举的精确算法所不含的范围；其原证明的两个技术门已给严格裕度修补，不作为否定它的论据。外部工具有其独立价值；“它没有涵盖我们这个完整对象”也不表示我们的每个结果都比它更强。
