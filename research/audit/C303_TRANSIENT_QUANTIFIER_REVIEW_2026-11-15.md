# C303 transient bootstrap: independent quantifier review

日期：2026-11-15  
审查对象：`c303_transient_angular_error.md`、`c303_finite_prefix_margin.md`、`c303_tau_common_tail_v5.md`、`c303_outer_strip_gate.md`

## 裁决

C303 保持 **continue validation**。瞬态 normal-error 项的正确求和确实保留了 (p=2) 的角度超解和 (alpha>2/3) 的步长门；但这只是在共同首出界停止域、统一的 (K_\star/T_\star) 选择以及上下两侧角度估计均已给出的条件下成立。当前四页尚未把这些条件合并为一个已闭的 source-to-PPA 证明，因此不能升级为主要贡献。

## 独立重构：瞬态项与 (p=2)

设在同一首出界前停止区间，对所有合法轨道有
\[
q_k=\lVert w_k\rVert\le M h_k+Q_0e^{-\gamma(t_k-T_\star)},
\qquad Q_0\le C_qh_0^2,
\]
以及极角上界
\[
\Delta\theta_k\le A h_k\phi(\theta_k)+B h_kq_k+C_0h_k^2,
\qquad \phi(s)=se^{-s^2}.
\]
则
\[
\Delta\theta_k
\le A h_k\phi(\theta_k)+C_e e_k,
\quad
 e_k=h_k^2+h_kh_0^2e^{-\gamma(t_k-T_\star)},
\]
其中 (C_e) 与 lifted angle 和轨道无关。由于 (t_{j+1}-t_j=h_j)、(h_j) 单调递减，
\[
\sum_{j\ge k}h_je^{-\gamma(t_j-T_\star)}
\le C_\gamma e^{-\gamma(t_k-T_\star)}.
\]
因此 (E_k=\sum_{j\ge k}e_j) 满足 (E_\star=E_{K_\star}=O(h_0^2))。令
\[
z_k=\theta_k-C_e(E_\star-E_k),
\qquad E=C_eE_\star.
\]
在 (z_k\ge1) 时，
\[
\Delta z_k\le A h_k\phi(\theta_k)\le A h_k\phi(z_k).
\]
对 (U_k=\exp((z_k+E)^2/2)) 使用均值定理，正增量满足 (Delta U_k\le C_Uh_k)，负增量使 (U_k) 下降；且 (	heta_k\le z_k+E)，故
\[
 e^{\theta_k^2/2}\le U_k\le U_{K_\star}+C_U(t_k-t_{K_\star}),
\qquad
\theta_k^2\le C+2\log(1+t_k).
\]
从而 (m(\theta_k),\phi(\theta_k)\gtrsim(1+t_k)^{-2})。对于 (h_k=h_0(k+1)^{-\alpha})，
\[
\frac{h_k}{m(\theta_k)},\frac{h_k}{\phi(\theta_k)}=O(k^{2-3\alpha}),
\]
所以渐近门仍准确地是 (alpha>2/3)。更强的统一首接触版本需要分两区估计 (u=h_0(k+1)^{1-\alpha})：
\[
\sup_{k\ge K_\star}h_k(1+t_k)^2\le C h_0
\quad(2-3\alpha<0),
\]
以及
\[
\sup_{k\ge K_\star}h_0^2e^{-\gamma(t_k-T_\star)}(1+t_k)^2\le C h_0^2.
\]
这两条说明瞬态项不改变指数，只改变有限常数。

## 尚未闭合的量词

### 1. (z_k\ge1) 不能只由上角度界推出

当前瞬态页从上界直接写出“(	heta_{K_\star}\ge3/2) 且 (C_eE_\star\le1/2)，故 (z_k\ge1)”。这一步缺少 (	heta_k) 的下界。必须在同一停止域补上例如
\[
\Delta\theta_k\ge c h_k\phi(\theta_k)-C_e e_k
\]
（或至少 (Delta\theta_k\ge-C_e e_k)），再用尾和控制累计下损，并把常数/初始角选到
\[
\text{累计下损}+C_eE_\star<\theta_{K_\star}-1.
\]
原 v4 的纯 (h_k^2) lower estimate 不能不加修改地覆盖瞬态 (h_kq_k) 项。

### 2. (K_\star)、(t_{K_\star}) 和有限前缀 horizon 的合并

有限前缀页证明的是首个 drop-threshold (K_0) 的有限步和 τ-path margin；瞬态页要求 (K_\star) 同时位于 drop threshold 之后且 (t_{K_\star}\ge T_\star)。若 (K_\star) 是首次满足 (t_k\ge T_\star) 的扩展索引，则必须把 FP1--FP5 的连续参考和所有 τ-path margin 明确延长到 (t_{K_\star})（例如证明 (t_{K_\star}-T_\star\le h_0)，并覆盖 ([0,T_\star+h_0])）。若只覆盖 (K_0)，则不能直接调用该 (K_\star) 的初始角度和 (Q_0=O(h_0^2)) 结论。

较干净的修补是分离两个时间常数：取固定 (T_{\rm pref}) 作为有限前缀参考上界，令 (K_\star=K_{\rm drop}) 并以 (t_{K_\star}) 为瞬态指数基准，或显式证明扩展后的 prefix margin；不要把固定参考 horizon 与瞬态指数中的 (T_\star) 复用而不说明其关系。

### 3. outer-strip 的 first-contact 合取尚未写成共同停止域

`c303_outer_strip_gate.md` 的 cutoff-free 结论依赖 (p=2) 角度包络和 
(lVert y_\tau-x_k\rVert=O(h_k))，并把路径限制到 (|q|\le\beta+\eta)。正式合并时，停止域必须同时包含核心管、normalized outer strip、物理半径界和入口角界；先在这个共同域内证明角度包络，再排除 (|q|=\beta+\eta) 的首接触。仅分别写“核心管内的角度估计”和“outer-strip 内的 cutoff 分离”会留下循环。

此外，outer-strip 页的 cutoff 分离是在“可自由选择 Π”的 HJ 约定下成立。HJ 来源页没有单独给出整个闭尾管与 π 的支撑分离构造，也没有在该页把 θ 截止、初始 band 和有限前缀 horizon 绑定。因此该 gate 仍是 source obligation，而非由条件性引理自动升级的事实。

## 最小改变裁决的证据

要把裁决从 continue validation 改变为已闭主要贡献，至少需要一份可复核合并证明，明确给出：

1. 同一共同开集和首出界停止域上的上下角度估计，特别是带瞬态项的 lower estimate 与 (z_k\ge1)；
2. (K_\star)、固定 finite-prefix horizon、(t_{K_\star}) 的统一选择，并将所有有限步端点与 τ-path margin 覆盖至该索引；
3. Π 的紧支撑构造，证明闭尾管与支撑分离且保留 HJ 的全局 (C^\infty) source identity；
4. outer-strip 首接触的共同停止域、离散留域和后续角度发散量词。

在这些证据出现前，TE、FP、OS 各自的条件性正确性不能被合取为 C303 的完整惯性 PPA 定理。
