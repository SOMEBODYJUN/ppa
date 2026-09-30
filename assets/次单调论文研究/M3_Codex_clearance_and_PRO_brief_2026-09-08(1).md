# M3：数学背景与文献清场

日期：2026-09-08  
项目：RL–PPA–VERIFY  
主题：非孤立解集上的 ordinary \(q>1\) 误差界及其扰动传递

---

## 1. 问题本身

设

\[
F:X\rightrightarrows X,
\qquad
S\subseteq F^{-1}(0)
\]

且 \(S\) 非空闭。M3 关心的是 ordinary 集合距离误差界

\[
d(x,S)
\le K\,d(0,F(x))^q,
\qquad q>1,
\tag{M3.1}
\]

而不是 strong subregularity

\[
\|x-\bar x\|
\le K\,d(0,F(x))^q
\]

或孤立解结论。

原问题关注：当算子经过加法、扰动、复合、活动分支变化或其他原生结构变换后，能否从可检查信息定量得到新的 ordinary 数据

\[
(q,K,r),
\]

并保持明确的目标集、作用域和正邻域半径。

这里的 \(q\) 是残差的幂指数。\(q>1\) 表示高阶 ordinary metric subregularity。

---

## 2. 与 RL–PPA/T5 的接口

T5 对同一个实际算子 \(F\)、同一个闭目标集 \(S\) 和同一输出域使用

\[
d(y,S)\le K\,r_F(y)^q,
\qquad
r_F(y):=d(0,F(y)).
\tag{M3.2}
\]

该误差界与 RL 几何是两个独立证书。二者可以由不同的数学工具得到，但必须匹配到同一个 PPA 转移。

对于 genuine \(0<\gamma<1\)，T5 的幂次兼容需要

\[
\gamma q>1,
\]

或处于临界情形

\[
\gamma q=1,
\qquad
K\left(\frac{L}{2\lambda}\right)^q<1.
\tag{M3.3}
\]

因此，只有 \(q>1\) 并不足以调用非线性 T5；指数、常数和共同有效半径都必须匹配。

以下对象不能直接替代式 (M3.2)：

- 针对单个孤立点的 strong subregularity；
- 只沿一条预选轨道成立的残差估计；
- 针对另一个算子或另一个目标集的误差界；
- 没有共同正状态半径的纯渐近模量；
- 只保持部分旧零点、但允许附近产生新零点的结论。

---

## 3. 已核验的已有范围

| 来源 | 已核范围 | 与 M3 的关系 |
|---|---|---|
| Li–Mordukhovich (2012), *Hölder Metric Subregularity…* | ordinary 集合距离允许非孤立目标；主要指数范围为 \(0<q\le1\) | 是普通 Hölder subregularity 的基础工具；尚未从该文核实到 ordinary \(q>1\) 的完整扰动演算 |
| Mordukhovich–Ouyang (2015), *Higher-Order Metric Subregularity…* | 定义覆盖任意 \(q>0\)，包括 \(q>1\)；ordinary 与 strong 分开 | 说明 ordinary \(q>1\) 不是新概念；其扰动部分的 strong 结论不能直接改写成非孤立 ordinary 结论 |
| Cibulka–Dontchev–Kruger (2018) | strong \(q\)-subregularity 的 calm perturbation stability，含定量新常数 | 仍属于 strong/孤立范围 |
| Gfrerer–Kruger (2023) | ordinary \(q=1\) 的 perturbation radius；包含多值且非 strong 的例子 | “ordinary + 多值 + 非孤立 + 扰动”作为宽泛组合并不新；其扰动大小半径不是 T5 的状态邻域半径 |
| T5 Proposition 4.2 | 一个保旧目标、具有显式常数和正管半径的单值小扰动 \(q>1\) 结论 | 已覆盖一类具体高阶扰动传递 |
| Li–Mordukhovich–Zhu (2026) | subdifferential/stationary target 的一般 gauge 与部分复合、目标距离转移；包含非孤立例子 | 可提供特定 subdifferential 类的误差界，但不是任意 multifunction 的 target-preserving calculus |
| Wei–Théra–Yao (2024) | 凸函数 \(q=1\) 的 ordinary 扰动证书 | 是定量的线性阶近邻结果，不是 \(q>1\) |
| Ouyang–Zhang–Zhu (2025) | 出版信息表明研究 \(F+f\) 的 ordinary metric subregularity 与模量估计 | 全文假设、指数、目标和半径尚未完成定理级核验 |
| Gao–Ouyang–Zhang–Zhu (2025) | 出版信息表明研究 generalized-subsmooth multifunction 的充分条件 | 全文范围尚未完成定理级核验 |
| Huang–Liu–Zhou–Zhu (2025) | 出版信息表明研究 generalized metric subregularity 的点式刻画 | 全文范围尚未完成定理级核验 |

主要来源：

- [Li–Mordukhovich 2012](https://epubs.siam.org/doi/10.1137/120864660)
- [Mordukhovich–Ouyang 2015](https://arxiv.org/html/1507.04825v1)
- [Cibulka–Dontchev–Kruger 2018](https://arxiv.org/abs/1701.02078)
- [Gfrerer–Kruger 2023](https://arxiv.org/html/2206.10347v2)
- [Li–Mordukhovich–Zhu 2026](https://arxiv.org/abs/2406.13207)
- [Ouyang–Zhang–Zhu 2025](https://doi.org/10.1080/00036811.2025.2505614)
- [Gao–Ouyang–Zhang–Zhu 2025](https://doi.org/10.1007/s11228-025-00753-7)
- [Huang–Liu–Zhou–Zhu 2025](https://doi.org/10.1080/02331934.2025.2588424)

三篇 2025 年论文尚缺全文定理级核验。因此，目前不能把它们的摘要信息升级为“已覆盖”或“未覆盖”结论。

---

## 4. 必须区分的目标关系

对

\[
G=F+H,
\]

以下三个命题不同：

\[
S\subseteq G^{-1}(0),
\tag{M3.4}
\]

\[
G^{-1}(0)\cap U=S\cap U,
\tag{M3.5}
\]

以及

\[
d(x,S)\le K\,d(0,G(x))^q.
\tag{M3.6}
\]

式 (M3.4) 只表示旧解仍是新解；式 (M3.5) 表示局部零集完全保持；式 (M3.6) 才是相对于给定旧目标的误差界。前两者都不自动推出第三者。

对非孤立 \(S\)，逐点存在常数和半径也不自动给出沿整个目标片统一的 \((K,r)\)。

---

## 5. 已知的逻辑障碍

### 5.1 完全保持零集仍不足以保持 \(q>1\)

令

\[
F(s,t)=\operatorname{sgn}(t)|t|^{1/q},
\qquad
S=\mathbb R\times\{0\}.
\]

则

\[
d((s,t),S)=|F(s,t)|^q.
\]

定义

\[
h(s,t)=t-F(s,t),
\qquad
G=F+h=t.
\]

此时

\[
G^{-1}(0)=S,
\]

但

\[
\frac{d((s,t),S)}{|G(s,t)|^q}
=|t|^{1-q}\longrightarrow\infty.
\]

因此，即使零集完全不变，\(q>1\) 误差界仍可能被扰动破坏。

### 5.2 多值扰动的最小残差不足以控制抵消

令

\[
H(s,t)=\{0,\,t-F(s,t)\}.
\]

虽然

\[
d(0,H(s,t))=0,
\]

但

\[
(F+H)(s,t)=\{F(s,t),t\},
\]

其最小残差在 \(t\to0\) 时由 \(|t|\) 主导，仍会破坏原有的 \(q>1\) 误差界。

因此，只控制 \(d(0,H(x))\) 不能代表对全部多值分支的非抵消控制。

### 5.3 Ordinary 与 strong 的差别不可通过换记号消除

Strong subregularity 估计的是到单个参考点的距离；ordinary subregularity 估计的是到整个逆像或目标集的距离。对非孤立零集，沿切向方向的运动可被集合距离消除，而在 strong 估计中不会消失。两类定理的扰动结论不能相互替换。

---

## 6. 截至本次核验的剩余边界

已确认不是剩余空白的内容包括：

- ordinary 或 higher-order metric subregularity 的定义本身；
- strong \(q\)-subregularity 的一般扰动稳定性；
- ordinary \(q=1\) 的一般扰动半径理论；
- T5 Proposition 4.2 已处理的单值、距离小扰动类；
- 只证明旧零点继续存在；
- 只对孤立解或预选轨道成立的估计。

在三篇决定性 2025 文献完成全文核验以前，尚不能确认一个一般的“多值、非孤立、ordinary \(q>1\)、保目标、显式常数与共同正状态半径”的扰动演算是否仍为空白。

目前能够保守提出的数学问题是：

> 对一个自然的多值算子类，能否从扰动前算子及扰动的直接结构，定量推出扰动后算子相对于明确非孤立目标集的 ordinary 高阶误差界
> \[
> d(x,S)\le K\,d(0,G(x))^q,
> \qquad q>1,
> \]
> 并给出指数、常数和共同正状态半径，使其能够与同一实际 PPA 转移的 RL 数据匹配？

这是项目强化问题，不应在决定性全文核验完成以前宣称为已认证公开问题。

---

## 7. 证据状态

| 主张 | 状态 |
|---|---|
| Ordinary \(q>1\) subregularity 已有定义和基础理论 | VERIFIED_SOURCE |
| Strong \(q\)-subregularity 的扰动稳定性已有定量结果 | VERIFIED_SOURCE |
| Ordinary \(q=1\) 的 perturbation-radius 理论已有 | VERIFIED_SOURCE |
| T5 Proposition 4.2 已覆盖一个具体 \(q>1\) 扰动类 | VERIFIED_PROJECT_MATERIAL |
| 零集保持不足以保持 \(q>1\) 误差界 | PROVED_PROJECT_OBSTRUCTION |
| 最小扰动残差不足以控制完整多值抵消 | PROVED_PROJECT_OBSTRUCTION |
| 三篇 2025 论文的决定性定理范围 | PENDING_FULLTEXT_VERIFICATION |
| 一般多值、非孤立、ordinary \(q>1\) 扰动演算仍为空白 | PENDING_GLOBAL_VERIFICATION |

本文件只记录问题、已有文献范围、逻辑障碍和 T5 接口；不包含研究流程、证明建议或面向任何模型的任务指令。
