# PPA 下一阶段研究状态与三方向启动报告

日期：2026-11-17  
仓库：SOMEBODYJUN/ppa，main，恢复的远端 HEAD：343790f

本报告把本轮工作分成五个层次：项目状态、LMZ/MOR 文献事实、三个独立目标、联合路线和启动结果。Paper fact、Interpretation、Hypothesis、derived-checked 和 refuted 分开使用。

## 1. 项目恢复与现有 PPA 状态

### 1.1 恢复证据

- 本地起始目录只有空 .git 目录和本轮上传文件，没有可用项目工作树。
- git ls-remote 得到 343790f；随后从该仓库恢复 main，git status 干净，remote 为项目给定的 GitHub 地址。
- 按项目要求先读了 README.md、RESEARCH_STATE.md、CLAIMS.md、FAILED_ROUTES.md、AGENTS.md、RESEARCH_PROTOCOL.md，再沿 File Map 读取 research/foundations.md、research/rleb_ppa.md、research/canonical/general_modulus_dynamics.md、research/canonical/generalized_ppa_modulus.md 以及历史 PPA 交接材料。
- 本轮上传的 PPA英语投稿.zip 已解包并读取 PPA_LaTeX/sections/theorem_spine.tex、preliminaries.tex、gppa_theory.tex、supplements/general_modulus.tex；它是 2026-11-12 的投稿源，不改变仓库既有 Claim 身份。

### 1.2 现有普通 PPA 主链

当前规范主链使用 \(X=\mathbb R^n\)、固定 \(\lambda>0\)、非空闭 \(S\subset\operatorname{zer}F\)，以及允许关系 \(\mathcal J(x)\subset J_{\lambda F}(x)\)。距离和真实残差为
\[
d(x)=\operatorname{dist}(x,S),\qquad r_F(y)=\operatorname{dist}(0,F(y)).
\]

在同一个最近零锚 \(p\in P_S(x)\) 上，RLEB 图几何给
\[
(d(y,S))^2+\|x-y\|^2
\le\frac{d(x)^2+\omega(d(x))^2}{2},
\qquad
\|x-y\|\le B(d(x)),
\]
其中 \(B(t)=(t+\omega(t))/2\)。真实全纤维误差界 \(d(y,S)\le\psi(r_F(y))\) 与 \(r_F(y)\le\|x-y\|/\lambda\) 结合后，得到 \(d(y,S)\le\psi(B(d(x))/\lambda)\)。

### 1.3 G1–G4 的准确含义

| 条件 | 数学内容 | 作用 |
| --- | --- | --- |
| G1 | 每个 \(x\in U_R\) 存在非空允许 \(\mathcal J_v(x)\subset J^v_{\lambda F}(x)\) | 覆盖和可迭代性 |
| G2 | 同一最近零锚 \(p\) 上，\(\delta_v=\|v(x)-v(p)\|\le a(d(x))\)，并有核空间 RL 能量不等式 | 产生核步界 \(K_v(d)\) |
| G3 | \(\|x-y\|\le h(d(x),\|v(y)-v(x)\|)\) | 把核步转成物理步 |
| G4 | 实际输出的真残差 EB、残差窗 \(K_v(R)/\lambda\le\bar t\)、直接兼容 \(\psi(K_v(t)/\lambda)\le\kappa t\)、物理尾 \(\Theta_v(R)<\infty\) | 距离收缩、有限长度、留域 |

普通 PPA 是 \(v=\operatorname{Id}\)、\(a(t)=t\)、\(h(t,q)=q\) 的退化情形；这时 \(K_v=H_v=B\)。

### 1.4 已经证明的结论

1. C02-v3/C09 在共同允许关系、最近零锚、真残差 EB、coverage、直接兼容和初值长度预算下，给出
   \[
   d_k\le\kappa^k d_0,\qquad
   s_k\le B(\kappa^k d_0),\qquad
   \sum_k s_k<\infty.
   \]
   C09 已把幂模替换为一般 \(\omega\)，并以 Dini 采样条件保证长度。
2. C10 对每个 \(a>0\) 给出完整双支关系。距离始终按 \(4^{-k}\) 收缩，但 \(a\le1\) 时切向步长级数发散、点列不收敛；\(a>1\) 时有限长度成立。这已经证明“距离趋零”和“点收敛/有限长度”不是同一命题。
3. 投稿稿的线性能量定理给出
   \[
   \rho_E=\sqrt{\frac{1+L^2}{2(1+\lambda^2/K^2)}},
   \]
   条件 \(\rho_E<1\) 时的距离收缩和步长估计，并保留旋转族边界见证。
4. GPPA 的物理提升先在核空间得到距离收缩，再以 \(h\) 和 \(\Theta_v\) 得到原空间有限长度。核空间收敛不能单独推出物理点列收敛；固定核或非单射核都必须逐项检查物理位移、真残差和 coverage。

### 1.5 已知过强处与未解决问题

- 固定 \(\kappa<1\) 把所有非线性距离递推压成几何率；C09 的一般模仍依赖这个固定率。
- Dini/采样可和是统一步长包络的充分门，不是所有单条轨道的必要条件；C10 已给出精确边界族。
- 局部 \(J_{\mathcal G}\) 的单值性不等于完整 \(J_{\lambda F}\) 单值；完整纤维和输入 coverage 仍是独立门。
- 真残差 \(r_F\) 是全纤维 inf，不能换成所选值的范数；GPPA 的核残差也不能自动替换原空间残差。
- 传统次单调性/MSR 的组合并不控制 \(\|x-y\|/d(y,S)\)；本轮 C310 给出最大单调反例。
- KL 可以替代某些次梯度 PPA 的有限长度证明，但需要 Lyapunov 函数、下降和相对误差；它不自动覆盖任意多值 \(F\)。

## 2. LMZ/MOR 精读报告

### 2.1 版本与可核对范围

正式版本（Paper fact）：INFORMS 正式页面确认题名、三位作者、DOI 10.1287/moor.2024.0570、接收日 2026-03-02、在线发表日 2026-04-07，以及 Article in Advance 状态和摘要。正式页面 PDF 入口在当前环境返回摘要/访问 HTML，未取得可逐页读取的刊本全文。

预印本（Paper fact）：arXiv:2406.13207v1，首页日期 2024-06-19，33 页。以下页码和定理编号只归属于 v1：

| 位置 | 读取内容 | 对 PPA 的意义 |
| --- | --- | --- |
| Definition 2.2, p.3 | KL 性质：\(\vartheta(0)=0\)、\(\vartheta'>0\)、\(\vartheta'(f(x)-f(\bar x))d(0,\partial f(x))\ge1\) | 把残差下界换成能量差的可积控制 |
| Definition 3.1, p.4 | pointwise/uniform generalized metric subregularity：\(\psi(d(x,\Xi))\le\kappa d(0,\partial f(x))\) | 广义误差界；可超出线性或幂型 |
| Theorem 4.3, pp.8–9 | H0–H3、surrogate \(e_k\)、\(\tau\)-迭代、下降差 \(\Lambda_{k,k+1}\)、有限长度 | 一般非线性迭代的抽象模板 |
| Theorem 4.4, p.10 | \(\tau(t)=\psi^{-1}(\gamma b\beta(\ell t))\)，\(\limsup\tau(t)/t<1\) 时的超线性/点收敛 | 对应 PPA 的 residual-to-distance 递推 |
| Theorem 5.1, pp.12–13 | KL 下的充分下降、相对误差与 \(\phi^{-1}(\beta(s)t)\) 混合条件 | 不用传统 MSR 的有限长度证明 |

版本差异记录：目前只能确认正式版与 v1 的出版身份、页码和在线状态不同。由于正式全文未能取得，不能负责任地声称定理编号、常数或假设完全相同。项目中的 C309/C311 只把 v1 作为已读来源，把正式版作为元数据/摘要来源。

### 2.2 广义度量次正则性的准确作用

LMZ 的 admissible 函数要求 \(\phi(0)=0\) 且 \(\phi(t)\to0\Rightarrow t\to0\)。其 generalized metric subregularity 是
\[
\psi(d(x,\Xi))\le\kappa\,d(0,\partial f(x)).
\]
\(\psi(t)=t\) 恢复普通 metric subregularity；\(\psi(t)=t^p\) 覆盖高阶或 Hölder 型误差界；Example 3.3 还展示了非幂函数可行而所有幂型都失败。

这与本项目的 \(\psi\) 记号方向相反：本项目写 \(d\le\psi(r_F)\)，LMZ 写 \(\psi(d)\le\kappa r\)。迁移时必须取逆或另命名，不能直接同名拼接。

### 2.3 非线性收缩 \(\tau\) 与可和性

LMZ Definition (4.3) 称 \(\tau\) 在零附近 asymptotically shrinking，当
\[
\tau(0)=0,\qquad
\limsup_{t\downarrow0}\frac1t\sum_{j=0}^\infty\tau^{\circ j}(t)<\infty.
\]
这是比单纯 \(\tau^{\circ j}(t)\to0\) 强的统一尾条件。Lemma 4.2 的易检验门
\[
\limsup_{t\downarrow0}\frac{\tau(t)}t<1
\]
只给出充分条件，并非 Theorem 4.3 的必要条件。

本轮 C309 证明了 PPA 所需的精确版本：
\[
\sum_j B(\Phi^{\circ j}(t))<\infty.
\]
当 \(B(t)\asymp t\) 时，它与 LMZ 的统一 \(\tau\)-尾同类；当 \(B\) 是非线性模时，C309 可接受 \(\Phi(t)/t\to1\) 而 LMZ 的简单比率门失败。

### 2.4 KL 有限长度机制

LMZ 的基本假设是 H0 下降、H1 步长 surrogate、H2 相对误差和 H3 上半连续性。KL Theorem 5.1 的核心把充分下降和 KL 导数转换成
\[
e_k\le \phi^{-1}\!\bigl((b/a)\beta(e_{k-1})\Lambda_{k,k+1}\bigr),
\]
再以
\[
\frac{\phi^{-1}(\beta(s)t)}{\mu_1s+\mu_2t}
\]
把它拆成前一步 surrogate 和可望远镜的 \(\Lambda\)。标准 exact prox 中取 \(\phi(t)=t^2,\beta(t)=t\)，AM–GM 就够了。

本项目 C311 已逐步重构这个 PPA 专化：\(e_k=\|x^{k+1}-x^k\|\)、\(a=1/(2\lambda)\)、\(w^{k+1}=(x^k-x^{k+1})/\lambda\)，从而
\[
\Lambda_{k,k+1}\ge \frac{e_k^2}{2e_{k-1}},
\qquad
e_k\le\frac{e_{k-1}+\Lambda_{k,k+1}}{\sqrt2}.
\]
这给出有限长度，不调用传统 MSR；但 KL 或等价 Lyapunov 结构仍是实质正则条件。

## 3. 三个目标的独立问题表

| 目标 | Exact mathematical question | 已知可调用结果 | 真正障碍 | 当前状态 |
| --- | --- | --- | --- | --- |
| 目标一 | 在 \(d_{k+1}\le\Phi(d_k)\) 下，以何种条件同时保证 \(\Phi^{\circ k}(t)\to0\)、\(\sum d_k\) 或 \(\sum B(d_k)\)、物理有限长度和点收敛？ | C09 的固定 \(\kappa\)+Dini；C10 的对数边界；C309 的一般 \(\Phi\) 定理 | 函数迭代趋零不等于步长可和；\(B\) 必须进入预算 | C309 derived-checked；原生 PPA/GPPA 实例仍 open |
| 目标二 | 能否在没有传统 MSR 时，用 KL/能量证明有限长度？ | LMZ v1 Theorems 4.3–5.1；C311 的 exact subgradient PPA 重构 | 一般 \(F\) 未必有目标函数、下降或相对误差；KL 不给自动距离率 | 次梯度 PPA 正面已闭；一般多值/GPPA 仍 open |
| 目标三 | 是否存在独立结构 \(\mathcal P\)，使旧假设推出 \(\mathcal P\Rightarrow(A)+(B)\)，并严格扩大适用类？ | (A)+(B) 本身足以给 \(\sum\|x^{k+1}-x^k\|\)；C310 反例；\(\mathcal P_{\rm TC}\) 的条件蕴含 | 旧“次单调性+MSR”不推出 (B)，故原逻辑链 fatal | 原始目标 refuted；修正版 \(\mathcal P_{\rm TC}\) 为 candidate |

## 4. 目标三的反例审查

### 4.1 传统前件不推出 (B)

\(F(y)=\operatorname{sgn}(y)|y|^\alpha\)、\(0<\alpha<1\) 是最大单调且满足线性 MSR。精确步为 \(x=y+\lambda\operatorname{sgn}(y)|y|^\alpha\)。当 \(y\downarrow0\)：
\[
\frac{d(y,S)}{d(x,S)}\to0,\qquad
\frac{\|x-y\|}{d(y,S)}=\lambda y^{\alpha-1}\to\infty.
\]
因此 (A) 可有任意严格因子，而 (B) 必然失败。这个反例直接阻断原始 传统条件 \(\Rightarrow\mathcal P\Rightarrow(A)+(B)\)。

### 4.2 各条件的独立性

- \(F(y)=\operatorname{sgn}(y)|y|^\alpha\)，\(0<\alpha<1\)：(A) 成立、(B) 失败。
- \(F(y)=\operatorname{sgn}(y)|y|^\beta\)，\(\beta>1\)：(B) 在有界窗成立、(A) 失败。
- 圆周旋转：集合距离为零但点列沿 \(S^1\) 不收敛，说明 A alone 不给点收敛。
- \(F(y)=\{y,y^2\}\)（\(y\ge0\)），允许分支 \(v=y\)：(A)+(B) 成立，但完整真残差 \(r_F(y)=y^2\) 破坏线性 MSR，且完整图不单调。

### 4.3 修正方向

\(\mathcal P_{\rm TC}\) 要求同一锚 \(p\in P_S(x)\cap P_S(y)\)、正扇区
\[
\langle y-p,x-y\rangle\ge\mu d(x,S)^2-\nu\|x-y\|^2,
\]
以及所选图值相对输出距离的 calmness
\[
\|(x-y)/\lambda\|\le c\,d(y,S).
\]
它严格推出
\[
d(y,S)\le\sqrt{1-2\mu}\,d(x,S),\qquad
\|x-y\|\le\lambda c\,d(y,S).
\]
这不是把 (A)+(B) 改名，而是投影锚、角度和纤维上界的三项结构；但旧前件不自动给它，必须单独研究可验证的算子类。

## 5. 联合路线图与优先级

真实依赖关系是：

\[
\text{RLEB 一步几何/真残差}
\longrightarrow
\text{复合距离模 }\Phi
\longrightarrow
\text{C309 函数迭代+步长预算}
\longrightarrow
\text{留域、有限长度、点收敛}.
\]

另一条独立链是：
\[
\text{Lyapunov 下降+相对误差}
\longrightarrow
\text{LMZ KL 机制}
\longrightarrow
\text{C311 次梯度 PPA 有限长度}.
\]

目标三修正版是另一条边：
\[
\mathcal P_{\rm TC}\Longrightarrow(A)+(B)
\Longrightarrow\sum_k\|x^{k+1}-x^k\|<\infty,
\]
但没有从传统次单调性/MSR 到 \(\mathcal P_{\rm TC}\) 的边。不能为了图形统一强行合并三条链。

优先顺序：

1. 先推进 C309 的原生模型实现和 \(\alpha=q\) 临界反例。
2. 并行把 C311 接到固定核 GPPA：先构造真实 Lyapunov 能量，再检查 G1–G4 与 H0–H3 的对象是否相同。
3. 最后研究 \(\mathcal P_{\rm TC}\) 的可验证算子类；在没有补充 calmness/锚持久性之前，不再沿原始目标三的逻辑链继续猜测。

## 6. 本轮启动结果与剩余 proof obligations

本轮已形成三个可独立复核的数学资产：

1. C309：任意非减函数迭代的 PPA 有限长度定理及 \(\sum B(\Phi^{\circ j}(t))\) 的精确预算；
2. C311：LMZ KL Theorem 5.1 到 exact subgradient PPA 的逐步证明，明确不使用传统 MSR 但需要 KL/下降/相对误差；
3. C310：最大单调+线性 MSR 仍不能推出 (B) 的反例，以及 \(\mathcal P_{\rm TC}\Rightarrow(A)+(B)\) 的修正版桥。

尚未完成的关键义务：

- C309 尚未给出一个同时满足原始完整 PPA 图量词、真残差和非线性临界 \(\Phi(t)=t-ct^{1+q}\) 的自然算子族；
- C311 尚未证明一般多值 \(F\) 存在与次梯度 PPA 同型的 Lyapunov/相对误差结构；
- \(\mathcal P_{\rm TC}\) 还没有一个已核、严格大于旧类的自然算子母类；
- 正式 LMZ 刊本全文的公式级版本差异仍未核对，不能将预印本编号转写为刊本编号；
- 所有新颖性判断仍独立于本轮内部证明，不因反例或定理成立而自动升级为全球首创。
