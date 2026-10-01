# RLEB–PPA：局部轨道的精确合取条件

来源以 S19 `sections/theorem_spine.tex` 为主；S18 是较早的投稿稿。源文件索引在 [SOURCES.md](SOURCES.md)。以下是稿件命题的可检索重构，不代表先行性审查完成。D01–D04 的定义见 [foundations.md](foundations.md)。

## R01 · 一步估计：图几何与真实残差在这里相遇

令 \(X=\mathbb R^n\)，\(S\subset F^{-1}(0)\) 非空闭，\(U\subset X\) 开，\(U_R=\{x\in U:d(x,S)\le R\}\)。固定 \(\lambda>0\)、\(L\ge0\)、\(0<\gamma\le1\)、\(\bar t>0\) 与非减原点连续 gauge \(\psi\)。假设每个 \(x\in U_R\) 在图块 \(\mathcal G\subset\operatorname{gph}F\) 上有 proximal 输出，并有一个 \(p\in P_S(x)\) 满足 \((p,0)\in\mathcal G\)；该图块在输入对尺度 \(R\) 满足全对 RL。对**实际输出** \(x^+=J_{\mathcal G}x\) 假设真残差界 \(d(x^+,S)\le\psi(r_F(x^+))\)，且 \((R+LR^\gamma)/(2\lambda)\le\bar t\)。

置 \(d=d(x,S),d^+=d(x^+,S),s=\|x-x^+\|\)，则

\[
(d^+)^2+s^2\le\tfrac12(d^2+L^2d^{2\gamma}),\qquad
(2s-d)^2\le L^2d^{2\gamma},\qquad
d^+\le\psi(s/\lambda)\le\psi((d+Ld^\gamma)/(2\lambda)).
\tag{R01}
\]

第一式用同一图块的 \((p,0)\) 和 proximal 图点作成对比较；第二式用反三角不等式；末式用 \(r_F(x^+)\le s/\lambda\)，不假设 \(s/\lambda=r_F(x^+)\)。同输入唯一只保证图块内 \(J_{\mathcal G}\) 单值。S19 `lem:solution-comparison`。

## R02 · 局部直接收敛定理

保留 R01 的全部域、量词与 gauge 条件，另假设存在 \(0<\kappa<1\) 使
\(\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t\) 对**每个** \(0<t\le R\) 成立。若 \(x^0\in U\)，\(d_0=d(x^0,S)\le R\)，且

\[
\mathcal L(d_0)=\tfrac12\left(\frac{d_0}{1-\kappa}
 +\frac{Ld_0^\gamma}{1-\kappa^\gamma}\right)
 <\operatorname{dist}(x^0,X\setminus U),
\tag{R02-budget}
\]

则唯一**局部图块**轨道 \(x^{k+1}=J_{\mathcal G}x^k\) 全程存在、留在 \(U_R\)、有限长，极限在 \(S\)。精确上界为
\(d(x^k,S)\le\kappa^kd_0\)，
\(\|x^{k+1}-x^k\|\le[\kappa^kd_0+L\kappa^{\gamma k}d_0^\gamma]/2\)，
尾界 \(\mathcal L(\kappa^kd_0)\)。这是 S19 `thm:two-branch-RLEB` 的命题身份；固定 \(F\) 的完整 resolvent 轨道还需 \(J_{\lambda F}=J_{\mathcal G}\) 在共同轨道区域成立。

**允许多选择的另一版本**（S19 `cor:selection-extension`）以每个合法 \(x^+\in\mathcal J(x)\subset J_{\lambda F}(x)\) 的统一 anchored 比较、输出 EB、coverage 取代图块 A1–A3；它不声称全对 RL 自动使完整 \(J_{\lambda F}\) 单值。每条合法轨道有同一上界，极限可随选择变化。

## R03 · 竞争的充分证书与临界边界

若真残差增长 \(r_F(y)\ge m d(y,S)^a\)，\(0<\gamma<1,L>0\)，选择 \(\psi(t)=(t/m)^{1/a}\)。R02 的小尺度直接兼容在 \(a<\gamma\) 成立；\(a=\gamma\) 时恰当 \(\lambda m>L/2\)；\(a>\gamma\) 时这个**标量测试**失败。失败不证明某条轨道发散。S19 `cor:residual-growth`。

同一稿件有另一个能量证书：当 \(\psi\) 连续严格递增且 \(R\le\psi(\bar t)\)，置 \(V(r)=r^2+\lambda^2[\psi^{-1}(r)]^2\)，\(A(r)=(r^2+L^2r^{2\gamma})/2\)。若 \(q_E(R)=\sup_{0<r\le R}A(r)/V(r)\le q<1\) 且 \(\sqrt{qV(d_0)}/(1-\sqrt q)<\operatorname{dist}(x^0,X\setminus U)\)，则 \(V(d_k)\le q^kV(d_0)\) 并有有限长和尾界。\(a=\gamma\) 的小尺度能量阈值 \(\lambda m>L/\sqrt2\) 比直接阈值更强；两者是**证明证书的阈值**，不宣称个别轨道收敛的必要条件。S19 `prop:energy-certificate`, `rem:sharpness-boundary`。

## R04 · 可检验图块、实例与条件拓展

- S19 `thm:square-root-seam` 反演一个闭图、正法向处二值的完整 proximal 关系；反射在接缝呈平方根阶，完整图跨支满足 RL，真实最小残差与覆盖各自验算。`prop:seam-quadratic-separation` 排除的是**指定**二次 \(J\)-side 证书，不是所有可能的 LT 定理。
- S19 `thm:signed-schur-growth` 的双支参数化先作切向反演，再要求两侧 Schur 导数有相反定向与定量增长，另加 complete-fiber 条件；得到覆盖、同输入唯一、跨支 Hölder 指数 \(1/p\)。仅有每支光滑或每支 Hölder 不足够，见 `prop:schur-collision-counterexample`。真残差 EB 仍要另证。
- S19 `thm:modulus-dini` 用非减 \(\omega\) 代替 \(Lt^\gamma\)，保留 coverage、输出 EB、兼容、留域，并加 \(\int_0^R\omega(t)dt/t<\infty\) 得有限长度。`thm:logarithmic-seam` 以完整对数二支图显示 \(a\le1\) 时距离以 \(1/4\) 收缩而切向坐标发散，\(a>1\) 才有限长；门槛对该族精确。拓扑后果和随机措辞异议见 [holder_structure.md](holder_structure.md)。

## 依赖超边与证据等级

| 超边 | 合取输入 → 输出 | 状态 |
| --- | --- | --- |
| H-R01 | {同图块全对 RL、coverage、解点图、实际输出真 EB} → R01 | 稿内代数，可逐项复核 |
| H-R02 | {R01、统一兼容 \(\kappa<1\)、初值留域预算、闭 \(S\)} → R02 | 稿内证明；不扩大完整 resolvent 量词 |
| H-R03 | {R01、\(\psi^{-1}\) 存在、\(q_E<1\)、另一留域预算} → 能量分支 | 稿内证明；与 H-R02 平行 |
| H-R04 | {signed-Schur 定向、全纤维排他、跨支估计} → RL 图块与 coverage | 条件验证器；EB 独立 |
| H-R05 | {R01 的 \(\omega\) 版、Dini、兼容、留域} → 点收敛 | 9/19 稿内证明；对数接缝攻击 Dini 边界 |

先行性与外部定理适用条件仍是独立审查门；旧 9/14 核心稿中的 fixed-anchor 与沿轨道条件不能无标签地合并到 R02。失败机制见 [FAILED_ROUTES.md](../FAILED_ROUTES.md)。
