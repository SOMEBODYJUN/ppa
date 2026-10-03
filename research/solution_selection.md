# 初值到极限解：统一尾界与完整 resolvent 的边界

来源 SS0 为 9/18 research_note.md，SS1 为 9/19 修订包中的同名稿，SS2 为 solution_selection_final_audit.md；对应路径见 [SOURCES.md](SOURCES.md)。SS0 的一般完整 resolvent 推论有实际接口错误；下述版本按 SS1/SS2 收缩量词。审计 PASS 只陈述其审查范围，不能代替所有证明或全球先行性检索。

<a id="tail"></a>
<a id="s01"></a>
## S01 · 抽象模传递（与 proximal 表示分离）

设 \(T\) 的全部指定轨道在共同工作区域 \(V\) 中存在，且对 \(x,y\in V\)、\(\|x-y\|\le R\) 有 \(\|Tx-Ty\|\le H\|x-y\|^\gamma\)，其中 \(0<\gamma<1\)。在初值集 \(B\subset V\) 上令 \(\Pi(x)=\lim_{k\to\infty}T^kx\)。若统一尾界 \(\|T^kx-\Pi(x)\|\le M\sigma^k\)、\(0<\sigma<1\)，则足够小的 \(\delta=\|x-y\|>0\) 满足

\[
\|\Pi(x)-\Pi(y)\|\le C\left(\frac{\log\log(1/\delta)}{\log(1/\delta)}\right)^\beta,
\qquad \beta=\frac{\log(1/\sigma)}{\log(1/\gamma)}.
\tag{S01a}
\]

若尾界改为 \(M e^{-c_0\nu^k}\)、\(\nu>1\)，则上界为 \(C e^{-c[\log(1/\delta)]^\alpha}\)，\(\alpha=\log\nu/\log(\nu/\gamma)\)。证明在有限步敏感度 \(A\delta^{\gamma^k}\) 与统一尾界之间平衡，并检查每个中间输入对仍在尺度 \(R\) 内。SS1 §1；SS0 §1 的抽象部分同结论。

[SS-TRANSFER 独立证明](canonical/solution_selection_rates.md#ss-transfer) 给出两种截断步数及每一步局部尺度的闭合条件；本节是入口，引用精确常数和量词时读证明正文。

<a id="full"></a>
<a id="s02"></a>
## S02 · 对 RLEB 的有条件导入

图块全对 RL 给 \(T=J_{\mathcal G}\) 在同一图块的 \(H=(R^{1-\gamma}+L)/2\) Hölder 界。[C136 / SS-B1–B5](canonical/solution_selection_rates.md#ss-rleb-ball) 在 R01/R02 的**同一个**零锚、真残差、coverage、兼容和留域窗上，从 \(\varepsilon+\mathcal L(\varepsilon)<\rho\) 构造共同初值球、轨道区域和统一尾，才能应用 S01。若要以**完整** \(T=J_{\lambda F}\) 陈述，须另证它和 \(J_{\mathcal G}\) 在全部实际可达输入上逐纤维相等；在共同输入区域 \(W\) 上逐纤维相等是方便的充分门，只在初值处检查不够。SS2 §二 R1、B2。固定解点 \(s\in S\) 的 \(\|\Pi(x)-s\|\lesssim\|x-s\|^\gamma\) 只给 anchored calmness，不给邻域里**任意两个**初值的 Hölder 模。

<a id="sel-ex"></a>
<a id="sel-sharp"></a>
## S03 · 显式下界与价值边界

SS1 §§2–4 有两个不同的闭图、至多二值完整 proximal 模型。几何尾模型的反演、跨支 all-pairs RL、真 EB、固定兼容和共同尾在 C137；**同一图的首次切换匹配下界**在 [C138](canonical/selection_geometric_sharpness.md#gs-sharp) 独立重构。另一二次尾模型的无正阶 Hölder 两点稳定性由 C115/C116 单独证明。两模型的证书和下界不能混用；一般实参数族不自动半代数，旧稿的有理指数限制须保留。经典 AGM 的较宽泛机制提示新颖性门仍开放；这里不声称完成先行性判断。

**SS1 §2–§3** 的[完整几何尾二支图](canonical/selection_geometric_cap.md#gc-object)及[指定配对锐阶](canonical/selection_geometric_sharpness.md#gs-sharp)分别是 C137/C138：前者先给共同尾上界，后者在固定 \(r_0\) 的同一 \(T\) 上证匹配下界；若称两者属于同一严格 RLEB 证书，须固定 \(r_0\le R<R_*\)。**SS1 定理 4 的另一二次模型与 §5.1** 有[完整纤维、共同证书及坏选择的独立正文](canonical/solution_selection_rates.md#ss-quadratic-object)（C115/C116）：逐轨道 Q-二次比值与全部初值的共同超几何尾是不同断言；两点根对数下界固定另一个初始 collar。两模型的 \(F,T\)、法向率和最小残差不能互换；§5.2 仍未逐项重构。

<a id="f03"></a>
## 反例 F03：不可省的全图一致性

令 \(F(u)=\{u,-u\}\)、\(\mathcal G=\{(u,u):u\in\mathbb R\}\)、\(\lambda=1\)、\(S=\{0\}\)。取 \(L=0,\gamma=1/2,R=1,\psi(t)=t,\kappa=1/2\)，局部 A1–A4 成立；但 \(J_{\mathcal G}(x)=x/2\)，而 \(J_F(0)=\mathbb R\)。因此 SS0 的“一般 A1–A4 自动得到完整单值 PPA”是假命题；S01、局部 S02 与两个逐项验算完整纤维的实例仍独立保留。相关失败卡见 [FAILED_ROUTES.md](../FAILED_ROUTES.md)。

## 超边

| ID | 合取先决条件 → 数学输出 | 审查状态 |
| --- | --- | --- |
| H-S01 | {同一 T 的共同迭代区域 V、V 内同尺度局部 Hölder、全初值全时间统一几何／超几何尾} → S01 对应模 | [SS-TRANSFER](canonical/solution_selection_rates.md#ss-transfer) 独立证明；C08 抽象部分 `derived-checked`。图块 RL 转入此边须先核 T=J_G 与同域尺度 |
| H-S02 | {R02 的局部轨道、共同初值球、留域} → S02 的 \(J_{\mathcal G}\) 版本 | 局部版本；完整版本需再加纤维一致性 |
| H-S03 / E31 | {C137 的同一完整几何模型共同尾、C138 固定配对的首次切换与饱和尾} → \(\beta=1\) 上界的匹配阶 | `derived-checked`：GS-1–6 独立重算；二次模型的坏选择另用 E181/C116，先行性另核 |
| H-F03 | {局部图块 A1–A4、图块外额外输出} → 完整 \(J_F\) 可多值 | 明确反例，否定 SS0 的扩大版本 |
