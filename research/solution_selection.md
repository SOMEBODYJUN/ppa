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

<a id="full"></a>
<a id="s02"></a>
## S02 · 对 RLEB 的有条件导入

图块全对 RL 给 \(T=J_{\mathcal G}\) 在同一图块的 \(H=(R^{1-\gamma}+L)/2\) Hölder 界。R02 的共同初值球和留域预算给统一尾界，才能应用 S01。若要以**完整** \(T=J_{\lambda F}\) 陈述，须另证它和 \(J_{\mathcal G}\) 在整条轨道可能经过的共同输入区域相等；只在初值处检查不够。SS2 §二 R1、B2。固定解点 \(s\in S\) 的 \(\|\Pi(x)-s\|\lesssim\|x-s\|^\gamma\) 只给 anchored calmness，不给邻域里**任意两个**初值的 Hölder 模。

<a id="sel-ex"></a>
<a id="sel-sharp"></a>
## S03 · 显式下界与价值边界

修订稿的两个闭图、至多二值完整 proximal 模型（SS1 §§2–4）分别给几何距离尾的匹配对数–对数劣化，以及点误差 Q-二次仍无正阶 Hölder 两点稳定性。其证明需要整图反演、负输入和 cap 接点的唯一性、跨支 all-pairs RL、全纤维最小残差 EB、实际局部半径中的严格兼容、首次切换时刻的匹配下界。几何模型固定示例的兼容必须把 \(R\) 缩到 SS2 R2 指定范围；二次模型的 all-pairs 常数还依赖输入对尺度 \(D\)（SS2 R3）。一般实参数族不自动半代数：该族的有理指数限制须保留。经典 AGM 已有“快速半代数迭代与非 Hölder 极限选择并存”的较宽泛机制，精确联合包的原创性仍未终审。SS2 §§三、四。

<a id="f03"></a>
## 反例 F03：不可省的全图一致性

令 \(F(u)=\{u,-u\}\)、\(\mathcal G=\{(u,u):u\in\mathbb R\}\)、\(\lambda=1\)、\(S=\{0\}\)。取 \(L=0,\gamma=1/2,R=1,\psi(t)=t,\kappa=1/2\)，局部 A1–A4 成立；但 \(J_{\mathcal G}(x)=x/2\)，而 \(J_F(0)=\mathbb R\)。因此 SS0 的“一般 A1–A4 自动得到完整单值 PPA”是假命题；S01、局部 S02 与两个逐项验算完整纤维的实例仍独立保留。相关失败卡见 [FAILED_ROUTES.md](../FAILED_ROUTES.md)。

## 超边

| ID | 合取先决条件 → 数学输出 | 审查状态 |
| --- | --- | --- |
| H-S01 | {共同迭代区域、局部 Hölder、统一几何／超几何尾} → S01 对应模 | 原稿证明，修订包内部审计 |
| H-S02 | {R02 的局部轨道、共同初值球、留域} → S02 的 \(J_{\mathcal G}\) 版本 | 局部版本；完整版本需再加纤维一致性 |
| H-S03 | {两个具体模型的完整反演、真 EB、跨支 RL、下界配对} → S03 中各对应锐性 | 修订包逐项审计；价值与先行性另判 |
| H-F03 | {局部图块 A1–A4、图块外额外输出} → 完整 \(J_F\) 可多值 | 明确反例，否定 SS0 的扩大版本 |
