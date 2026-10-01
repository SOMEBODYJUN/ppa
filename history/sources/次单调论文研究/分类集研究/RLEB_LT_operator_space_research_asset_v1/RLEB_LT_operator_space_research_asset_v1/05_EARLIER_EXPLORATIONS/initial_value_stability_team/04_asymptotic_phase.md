# 第 4 组：初值到极限点映射的动力系统与回缩文献核查

核查日期：2026-09-19。范围：固定算法的初值 → 极限点/渐近相位；不把参数扰动、单轨道收敛率或到解集的距离界替代两初值稳定性。仅核对本次新稿所用接口，不重新审查原 RLEB。

## 结论先行

**有人直接研究过，而且正向结果很强。** 1993 年 Beyn 已研究 Gauss–Newton 把初值送到最终解的映射；现代稳定叶/渐近相位理论和 2026 年交替投影回缩论文也给出正向条件。因此，“加条件获得稳定的解选择”不是全新问题。值得推进的是：把这些条件降到 RLEB 特有的非光滑、接缝、多值图背景下，找到无需全环境光滑性的可核查切向条件。

不能将下列三类命题混同：

1. 各初值轨道均快速收敛；
2. 每个固定解点处的 calmness；
3. 同一工作邻域内任意两初值之间的 Hölder/Lipschitz/C^k 极限选择。

本组核得的真正直接基线是 Beyn Theorem 2.2、Eldering–Kvalheim–Revzen Corollary 2，以及 Zheng–Chen **v3** Theorems B.1–B.2。Chen–He–Huang 的主定理需特别标明其切丛参数域。

## 1. 原始文献定理级对应

### 1.1 Beyn 1993：离散 Gauss–Newton 的平滑极限选择

- 作者、题名：Wolf-Jürgen Beyn, *On smoothness and invariance properties of the Gauss-Newton method*.
- 刊物：Numerical Functional Analysis and Optimization 14(5–6), 503–514 (1993)。[DOI: 10.1080/01630569308816536](https://doi.org/10.1080/01630569308816536)。[原始 12 页扫描件](https://noah.nrw/ubbihs/download/pdf/5114560)。本轮已逐页读完。
- **Theorems 2.1–2.2，p.505**：设 \(F:\mathbb R^{m+p}\to\mathbb R^m\) 为 \(C^{k+1}\)，\(k\ge1\)，且 \(F(\bar v)=0\)、\(\operatorname{rank}DF(\bar v)=m\)。对 \(T(v)=v-DF(v)^\dagger F(v)\)，在一个共同小初值邻域中迭代收敛，且 \(\Pi(v)=\lim_nT^n(v)\in C^k\)。**Theorem 3.1，p.510** 给出 \(C^k\) 稳定叶，叶与解流形正交。
- 覆盖：非唯一解、真正初值→极限点、二次轨道收敛与稳定选择共存。
- 不覆盖：一般 Hölder resolvent、多值图接缝、秩退化、RLEB 全类别。不能把“Gauss–Newton”换名成任意 proximal 方法。作者明确注意到 GN 不必为微分同胚。

### 1.2 Kvalheim–Revzen 2016：渐近相位及其设计

- Matthew Kvalheim, Shai Revzen, *Reverse-engineering invariant manifolds with asymptotic phase*, [arXiv:1608.08442](https://arxiv.org/abs/1608.08442)，[原文](https://arxiv.org/pdf/1608.08442)。本轮读取 §2、§3.2、§4 与 Appendix F/G 的相关定理。
- **Proposition 1，§2.1，Appendix F 精确重述**：紧 \(C^r\) 正常吸引不变流形有连续相位投影；再加定义中的速率条件 \(\tau(q)<1/m\)，\(1\le m\le r-1\)，相位映射为 \(C^m\)。这是连续时间结果。
- **重要边界**：Theorem 1 已假设 \(C^r\) 相位；§3.2.2 的逆向设计也预先输入一个 \(C^r\) 相位映射。它们不能被当成“从很弱算子条件自动导出相位光滑”的证据。
- RLEB 对应：当流形上全部为平衡点，相位就是最终解；一般周期/流形内运动的相位并非静态极限解。

### 1.3 Eldering–Kvalheim–Revzen 2018：可直接检查的谱速率条件

- Jaap Eldering, Matthew Kvalheim, Shai Revzen, *Global linearization and fiber bundle structure of invariant manifolds*, Nonlinearity 31(9), 4202–4245 (2018)。[DOI: 10.1088/1361-6544/aaca8d](https://doi.org/10.1088/1361-6544/aaca8d)，[arXiv:1711.03646v3](https://arxiv.org/pdf/1711.03646v3)。已读 Theorem 1、Corollaries 1–2 及条件 (11)。
- 连续时间；紧正常吸引流形 \(M\)，\(C^r\) 流。**Theorem 1**：局部相位投影 \(C^k\) 则全稳定域投影 \(C^k\)。**Corollary 2** 用下式保证局部到全局 \(C^k\)，\(k<r\)：
  \[
  \|D\Phi^t|_{TM}\|^i\|D\Phi^t|_{E^s}\|
  \le K e^{\alpha t}\,m(D\Phi^t|_{TM}),\quad 0\le i\le k,\quad\alpha<0.
  \]
- 推论性解释：若 \(M\) 全是不动点，切向导数为恒等，条件简化为法向指数收缩。
- 限制：流的稳定叶定理不能直接套在可能不可逆、法向导数为零的离散 proximal 映射上；需要离散版或直接证明。

### 1.4 Chen–He–Huang 2026：交替投影极限的光滑回缩

- Shixiang Chen, Yixiao He, Wen Huang, *Retractions by Alternating Projections*, [arXiv:2605.17384v2](https://arxiv.org/html/2605.17384v2)。已读 Assumptions 1–3、Lemma 4.6、Theorems 2–4。
- **Theorem 2**：clean intersection、近投影逼近条件及 Assumption 3（含 \(\varphi\in C^{1,1}\)）给出 \(\psi(x,\eta)=\lim_k\varphi^k(x+\eta)\) 为 \(C^1\) 回缩；**Theorem 3** 加相应二阶切向/法向余项与 \(C^{2,1}\) 条件给 \(C^2\) 二阶回缩。精确投影由 \(C^{2,1}\)/\(C^{3,1}\) 流形验证。
- **域限制**：主陈述在 \((x,\eta)\in TM\) 的零截面邻域，不应不加说明扩张成整个环境空间的初值两点定理。
- **Lemma 4.6** 的核心是：切向恒等、双向交叉导数为零、法向统一收缩。clean intersection 比 transversality 弱，但仍假设解流形和较强光滑性。

### 1.5 Zheng–Chen 2026：固定正则化 RN-SLRA 的邻域极限映射

- Dengyu Zheng, Shixiang Chen, **v3 题名** *A Regularized Newton-Type Method for Manifold--Affine Intersection Problems under Intrinsic Transversality*, [arXiv:2606.31738v3](https://arxiv.org/abs/2606.31738v3)，2026-09-17 更新。[v3 原文](https://arxiv.org/pdf/2606.31738v3)。旧 v1/v2 题名为 *A Geometry-Adaptive Regularized Newton-Type Method for Manifold-Affine Intersection Problems*。
- **Theorem B.1**：固定正则化 \(\rho=0\)，\(M\in C^3\)，仿射集 \(E\) 与 \(M\) clean intersection，得到共同邻域 \(z\in E\) 上 \(\Psi_c(z)=\lim_k\Phi_c^k(z)\in C^1\)。**B.2**：\(M\in C^4\) 给 \(C^2\) 极限映射及二阶回缩。
- 正向机制见 (B.1)：切向特征值 1，法向特征值 \((1-\lambda)/(1+\lambda/c)<1\)；导数尾级数一致可和。
- **Remark B.3** 还指出可分别降为 \(C^{2,1}\)、\(C^{3,1}\)；这是作者给出的放宽说明，本组没有把其省略细节的推广冒充已独立重证。
- **不能外推**：B.1/B.2 仅处理 \(\rho=0\)；主文 \(\rho>0\) 的超线性/二次轨道结论不自动附带同样光滑的极限选择。Theorem 4.8 的近投影距离界也不能单独替代两初值 Lipschitz 性。

## 2. 经典稳定叶来源：已核与未核的界线

本轮直接读取的原始研究 EKR 2018，明确把上述 center-bunching→局部光滑投影归给 **Neil Fenichel, *Asymptotic Stability with Rate Conditions, II*, Indiana University Mathematics Journal 26(1), 81–93 (1977), Theorem 5**。[DOI: 10.1512/iumj.1977.26.26006](https://doi.org/10.1512/iumj.1977.26.26006)。此外有 Hirsch–Pugh–Shub, *Invariant Manifolds*, Lecture Notes in Mathematics 583 (1977), Theorem 4.1 的稳定叶传统。

本轮 Fenichel 出版站返回 502，JSTOR 未提供正文，HPS 原始书页未取得。因此 **不把 Fenichel Theorem 5 或 HPS 4.1 标成原页独立复核**；可执行的精确条件以已直接读到的 EKR Corollary 2 为准。这不妨碍回答“有人研究过”，但后续投稿若细论最早优先权，应补核经典原页。

## 3. 对 RLEB 的翻译：应保留什么，避免什么

以下是本组综合判断，不是上述任一论文已经证明的 RLEB 推广定理。

### 3.1 最有用的结构不是“再快一点”，而是“误差不持续放大”

RLEB 的统一尾界控制单条轨道余程。稳定选择还需控制两条轨道之间的切向差。若迭代每一步的两点放大因子为 \(1+a_k\)，并有统一的 \(\sum_k a_k<\infty\)，则

\[
\prod_k(1+a_k)\le\exp\!\left(\sum_k a_k\right)<\infty.
\]

这是标准乘积/Gronwall机制，并不是新发现。其优点是允许有限扩张，不强求每一步非扩张。若施加到所有方向，可能排除 RLEB 希望保留的法向 Hölder 尖点；因此宜尝试只控制切向放大，同时单独估算法向差的输入。

### 3.2 原新稿 §5.2 已经是一个正确的弱正向起点

原附加命题处理

\[
T(a,r)=(a+B(a,r),qr),\qquad
\|B(a,r)-B(b,r)\|\le Cr^\eta\|a-b\|,
\]

再加 \(B\) 关于 \(r\) 的 \(\gamma\)-Hölder 性，得到两初值 Hölder 选择。这里不要求整个映射 \(C^1\)，比上述光滑回缩路线保留了更多非光滑特征；但三角解耦限制很强。

作为**标准估计的直接放宽**，可将 \(Cr^\eta\) 换为非减模 \(\omega(r)\)，仅要求

\[
\sum_{k=0}^\infty\omega(Rq^k)<\infty.
\]

相同递推给

\[
\|\Pi_a(a,r)-\Pi_a(b,s)\|
\le e^{\sum_k\omega(Rq^k)}
\left(\|a-b\|+\frac H{1-q^\gamma}|r-s|^\gamma\right).
\]

对非减 \(\omega\)，Dini 条件 \(\int_0^R\omega(t)\,dt/t<\infty\) 是自然可核查形式。这允许例如 \(\omega(r)=[\log(e/r)]^{-1-\epsilon}\)，远弱于正幂衰减。**但这一放宽仍只在上述三角结构内，不能宣称是一般 RLEB 新定理，亦不能宣称必要。**

### 3.3 不应把“光滑解流形”当作单独充分条件

用户新反例的解集已很规则。问题在固定 \(r>0\) 时切向分量 \(p\mapsto\sqrt{\min\{p_+,r\}}\) 的尖点：两条很近的轨道会反复被放大。故仅加“零集是流形”“半代数”“距离收缩更快”并未针对致坏机制。

同样，\(DT|_{TS}=I\) 只是固定点流形上的必然一阶关系；还需邻域里的交叉项/切向误差的定量控制。不能把流形上导数式当完整邻域两点结论。

### 3.4 谱条件是强基线，不宜直接宣称“最弱自然条件”

假定解流形 \(S\)、足够光滑的 \(T\)、切向恒等与法向统一收缩，是恢复光滑选择的成熟路线。它能清楚定位 RLEB 反例何处不满足要求，但可能直接放弃 RLEB 的非光滑特色。

此外，“完全没有法向→切向的一阶耦合”不是逻辑上必要。最小线性例

\[
T(a,r)=(a+br,qr),\qquad 0<q<1,
\qquad \Pi(a,r)=(a+br/(1-q),0)
\]

具有非零交叉项 \(b\) 而 \(\Pi\) 仍线性。应研究可控/可和耦合，而不是不加思考地一律要求交叉块为零。

## 4. 条件梯度与研究优先级

下表是“所要求结构逐渐增加”的工作梯度，**不是所有行两两存在逻辑包含的总序**。

| 层级 | 候选条件 | 可望/已知结果 | 本轮定位 |
|---|---|---|---|
| 0 | 共同初值邻域上的统一尾界 + 连续单步映射 | 极限连续；有单步模可传递定量模 | 已有新稿主线，不自动 Hölder |
| 1 | 三角结构 + 切向放大沿轨道可和 + 法向差 Hölder 输入 | 混合 Lipschitz/Hölder 极限选择 | 标准 Gronwall，最接近新稿的轻量证书 |
| 2 | 全空间或适配度量中迭代的统一 Lipschitz 界，或足以推出它的可和扩张条件 | Lipschitz 极限选择 | 很可靠，但可能过强或难核查 |
| 3 | 非三角法/切向两点递推闭合，切向放大及耦合的累积预算有限 | 目标为 Hölder/Lipschitz | **值得继续研究的接口；本轮未证明一般定理** |
| 4 | 光滑固定点流形 + 正常吸引/谱隙 + 足够高阶正则性 | 稳定叶、C^k 相位/极限映射 | 成熟强基线；离散非可逆情形需专门处理 |
| 5 | 正则 Gauss–Newton、光滑 clean-intersection 投影/RN-SLRA | 特定算法的 C^k/C^1/C^2 回缩 | 原定理已有，不能重新包装成 RLEB 创新 |

最建议：先把第 1 层写成明确的“已有基线”，然后攻击第 3 层。创新门应设为：**能否从算子图/次单调性可实际核查的条件推出累积切向稳定性，且允许新稿希望保留的法向非 Lipschitz、接缝或多值性；同时确实覆盖三角情形之外的新实例。**

## 5. 本轮交付与待补

- 已独立核到：Beyn 原文全部 12 页；Kvalheim–Revzen 所需原定理和假设；EKR Corollary 2 的精确谱条件；两篇 2026 原文的实际结论域。
- 已发现的重要引用风险：2026 RN-SLRA v3 与旧版题名及结论变化；切丛回缩不等于全邻域结论；固定正则化光滑性不等于超线性参数情形光滑性；预设光滑 phase 不能拿来证明 phase 自然光滑。
- 未完成且不虚报：Fenichel/HPS 的原始定理页；最弱性/必要性；把候选切向条件翻译到所有 signed-Schur 图块；非三角一般定理及原创性审核。
- 未修改用户稿件。本文件为团队中间核查报告。
