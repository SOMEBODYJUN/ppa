# C303 common stopping domain: independent review

日期：2026-11-15  
审查对象：`research/c303_common_stopping_domain.md`

## 裁决

当前页保持 **continue validation**。它正确地把 core、outer-strip、transient angle bootstrap 和 τ-path 放进了同一候选框架，但 CS1--CS7 仍是 conditional merge，不能作为已闭的惯性 PPA 证明。最关键的潜在致命缺口是 CS4 的 outer-strip containment 量词仍有循环：它在尚未定义 outer-strip 首次接触或证明路径留在该 strip 之前，直接使用只在该 strip 内有界的 (q_r,q_\theta) 和 HJ cutoff-free 公式来推出路径属于该 strip。

## 最小首次出界步重构

令
\[
K=\inf\{k\ge1:x_k\notin D\}.
\]
若 (K<\infty)，则 (x_{K-1}\in D)。固定这一整数步的连续 resolvent 路径 (y_\tau), (0\le\tau\le1)，并定义
\[
\tau_D=\inf\{\tau:y_\tau\notin D\}.
\]
在 ([0,\tau_D)) 上路径自动位于 (D\subset S_\eta)，所以只有在这个区间内，才可使用 cutoff-free HJ 公式、角度展开和径向/入口面估计。由 global resolvent bounds 和 (x_{K-1}\in D) 可先得
\[
\|y_\tau-x_{K-1}\|\le C h_{K-1},
\qquad
|\theta(y_\tau)-\theta_{K-1}|\le C h_{K-1}
\]
直到 (	au_D)。结合前面已经独立证明的 angle bootstrap、(h_k(1+t_k)^2\le Ch_0) 和 transient bound，可在 (	au_D) 处把 (m(\theta(\tau_D))) 与 (m(\theta_{K-1})) 比较。若 (	au_D) 是径向首接触，需逐式得到
\[
\frac d{d\tau}s_i(y_\tau)\bigg|_{\tau_D}
\ge \beta_{K-1}\bigl[m(\theta(\tau_D))-C(q_{K-1}+h_{K-1})\bigr]>0.
\]
若是入口角首接触，则同样需要
\[
\frac d{d\tau}\theta(y_\tau)\bigg|_{\tau_D}
\ge \beta_{K-1}\bigl[c\phi(\theta(\tau_D))-C(q_{K-1}+h_{K-1})\bigr]>0.
\]
这才与从 (D) 内部首次达到边界所需的非正左导数矛盾。

这个最小重构实际上不需要先证明整条路径属于 (S_\eta)：在首个 core-face 接触之前，路径已经在 (D\subset S_\eta)。若要按 CS4 的路线先证明整条 τ-path 在 (S_\eta)，则必须另定义
\[
\tau_S=\inf\{\tau:y_\tau\notin S_\eta\}
\]
并只在 ([0,\tau_S)) 上使用 (q_r=O(e^\theta)), (q_\theta=O(1))。随后在 (	au_S) 处证明 (q)-边界、半径边界和入口角边界的首接触导数具有严格正确符号，从而排除 (	au_S)。当前 CS4 没有这个 (	au_S) 量词，也没有给出 (q)-边界的首接触估计。

## 为什么这是 source gate，而非已完成的细节

CS1 假设 (Pi_{\rm cut}=0) 在整个 (mathcal P(\overline{S_\eta})) 上，并假设 (mathcal P) 在闭 outer strip 上单射。这两个条件尚未从 HJ 原始 cutoff 的全部定义逐字推出。global-bounds 可给全局 resolvent coverage 和导数上界，但不能替代 cutoff-free HJ 公式在每个首次接触点的来源证明。

此外，CS5 的 (sup_\tau\|\widetilde w_{k,\tau}\|\le q_k+Ch_k) 必须明确说明其常数由 global normal recursion 的 (c_\delta)-到-(\gamma) 选择得到，且对所有 (	au\in[0,1]) 和所有共同初值统一；不能把端点已经在 (D) 当成该估计的前提。

## 最小改变裁决的证据

要改变当前裁决，至少需要一份逐步合并的证明，完成以下任一等价方案：

1. 以 (	au_D) 为最小首接触参数，证明在 ([0,\tau_D)) 上的 global displacement、normal-error、角度比较和 CS6/CS7 严格正导数；或
2. 继续使用 outer-strip 路线，但显式定义 (	au_S)，在 ([0,\tau_S)) 上建立 (q)-坐标微分不等式，并在 (	au_S) 处排除 normalized-strip、物理半径和入口角三类首接触。

同时必须给出 CS1 的可复核 HJ cutoff 构造、闭 outer strip 的 lift/injectivity 证明和共同初始开集量词。仅把 CS4--CS7 并列写在同一页，或继续声明这些条件为 assumptions，不能把 C303 升级为主要贡献。
