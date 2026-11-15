# C303：核心管与 cutoff-free outer strip 的共同停止域

状态：**candidate / conditional merge**。本页把 `c303_outer_strip_gate.md`、`c303_transient_angular_error.md` 和 `c303_tau_common_tail_v5.md` 的停止域写成一个最小指标归纳，避免分别证明“核心管估计”和“outer-strip cutoff”而留下循环。

## 1. 共同停止域

取 HJ cutoff 尾部分离所需的 \(\theta_0\)，再取入口阈值
\(\theta_*\ge\max\{\theta_0,3/2\}\)、\(0<\eta_{\rm strip}<1-\beta\)，并令
\[
D=\{(r,\theta):\theta>\theta_*,\ b_1(\theta)<r<b_2(\theta)\}
 =\{(r,\theta):\theta>\theta_*,\ |q(r,\theta)|<\beta\},
\]
\[
S_{\eta_{\rm strip}}=\{(r,\theta):\theta\ge\theta_*,\ |q(r,\theta)|\le\beta+\eta_{\rm strip},
                         \tfrac12\le r\le\tfrac32\}.
\]
假设 HJ cutoff construction 给出
\[
\Pi_{\rm cut}=0\quad\text{on }\mathcal P(\overline{S_{\eta_{\rm strip}}})
\tag{CS1}
\]
并且 \(\mathcal P\) 在该闭 outer strip 上保持单射。定义共同停止域为 lifted core 的闭包连同
\(S_{\eta_{\rm strip}}\) 的局部坐标邻域；所有 \(F,Y,g,H\) 常数均取在此共同域或由 global-bounds 给出。

## 2. 最小指标归纳

令 \(K_*\) 为 finite-prefix 使用的首个 drop threshold，\(T_{\rm tr}=t_{K_*}\)，并取
\[
q_k=\|w_k\|\le M h_k+Q_0e^{-\gamma(t_k-T_{\rm tr})}
\tag{CS2}
\]
以及 transient angle estimate (TE2)--(TE10)。考虑第一个不属于核心管 \(D\) 的端点
\(x_K\)，并在导致它的步 \(j=K-1\) 的连续 \(\tau\)-path 上取第一个离开
\(D\) 的接触参数。若 \(K\le K_*\)，`c303_finite_prefix_margin.md` 直接给出所有
这些 \(\tau\)-paths 位于 \(S_{\eta_{\rm strip}}\) 的紧安全带内。

设 \(K>K_*\)，并假设所有 \(\ell<K\) 的端点在 \(D\)。则导致 \(x_K\) 的完整步索引
\(j=K-1\ge K_*\)。angle bootstrap 只对已完成的更新 \(\ell<j\) 使用，
并由此把端点估计传递到 \(x_j\)：
\[
\theta_\ell^2\le C+2\log(1+t_\ell),
\qquad
m(\theta_\ell),\ \phi(\theta_\ell)\ge c(1+t_\ell)^{-2}.
\tag{CS3}
\]
由 (CS2)、全局 \(g,F\) 界和 \(|y_\tau-x_j|\le C h_j\)，先控制极坐标位移。
在第一个接触之前，局部 lift 仍满足 \(r\in[1/2,3/2]\)；由
\(q_r=O(e^{\theta_j})\)、\(q_\theta=O(1)\) 得特别地
\[
|q(y_\tau)-q(x_j)|\le C h_j e^{\theta_j}.
\tag{CS4}
\]
由 (CS3) 可取 \(e^{\theta_\ell}\le C(1+t_\ell)\)。用
\(t_\ell\le C h_0(1+\ell)^{1-\alpha}\) 分裂
\(h_0(1+\ell)^{1-\alpha}\le1\) 与 \(\ge1\) 两段，得到
\[
\sup_{\ell\ge K_*}h_\ell e^{\theta_\ell}
 \le C h_0
 \quad(\alpha>2/3),
\]
由同一两项分裂
\(h_\ell(1+t_\ell)\le C[h_0(\ell+1)^{-\alpha}
 +h_0^2(\ell+1)^{1-2\alpha}]\).
缩小 \(h_0\) 后使 (CS4) 小于 \(\eta_{\rm strip}/2\)；\(r\)-带由
\(q\in[-\beta-\eta_{\rm strip},\beta+\eta_{\rm strip}]\) 与
\(\theta\ge\theta_*\ge\theta_0\) 的外条带估计给出，有限前缀由其紧安全带单独覆盖。
因此第一个 core 接触前的路径及接触点位于
\(S_{\eta_{\rm strip}}\) 的闭包内，并可调用 (CS1) 的 cutoff-free 显式 HJ 公式；
不对接触后的整条 \(\tau\)-path 作额外断言。

## 3. 排除核心管首接触

令 \(\tau_D=\inf\{\tau:y_\tau\notin D\}\)（若存在）。在
\([0,\tau_D]\) 上有 \(|q|\le\beta\)、\(r>1/2\)，故
\(q_r=O(e^{\theta_j})\)、\(q_\theta=O(1)\) 的积分估计不依赖于未知的
outer-strip 出界；若 outer strip 先假设出界，则从 \(|q|<\beta\) 出发必须
先穿过 \(q=\pm\beta\)，所以其首接触不早于 \(\tau_D\)。在 \(S_{\eta_{\rm strip}}\) 上，
导致 \(x_K\) 的步 \(j=K-1\) 的线性 \((\lambda_j,\beta_j)\)-resolvent path 的导数误差满足
\[
\sup_{0\le\tau\le1}\|\widetilde w_{j,\tau}\|
 \le q_j+C h_j.
\tag{CS5}
\]
若路径第一次接触径向面 \(s_i=0\)，则
\[
\frac d{d\tau}s_i(y_\tau)\bigg|_{\tau_*}
\ge\beta_j\left[m(\theta(\tau_*))
     -C\bigl(h_j+q_j\bigr)\right].
\tag{CS6}
\]
由 \(|\theta(\tau_*)-\theta_j|=O(h_j)\)、\(h_j(1+\theta_j)\to0\)，有
\(m(\theta(\tau_*))\asymp m(\theta_j)\)。TE9a--TE9b 和 (CS2) 使右侧严格为正。

若第一次接触是入口角面，则同理
\[
\frac d{d\tau}\theta(y_\tau)\bigg|_{\tau_*}
\ge\beta_j\left[c\,\phi(\theta(\tau_*))-C(h_j+q_j)\right]>0.
\tag{CS7}
\]
因此当前步不能离开 \(D\)，与 \(K\) 的定义矛盾。不存在最小出界步。

## 4. 量词边界

(CS1)--(CS7) 只是在以下条件同时成立时的合并证明：

1. cutoff support 的显式构造确实满足 HJ 原文全部未摘录条件；
2. TE2 的上下两侧极角估计、CS5 的线性同伦导数估计和 global normal recursion 在同一共同停止域上均匀成立；
3. finite-prefix 安全带覆盖与 \(K_*\)、\(T_{\rm tr}\) 使用同一首个 drop threshold；
4. \(\mathcal P\) 在闭 outer strip 上的 lift/injectivity 与有限局部角坐标已核验。
5. 本页 (CS3)--(CS4) 仍沿用 \(\theta^2\le C+2\log(1+t)\) 的 \(p=2\)、
   \(\alpha>2/3\) 分支；若要使用 `c303_sharp_schedule_bootstrap.md` 的
   \(W=e^{z^2}\) 候选并声称 \(1/2<\alpha<1\)，必须把共同停止域中的
   \(e^{\theta}\)、\(m^{-1}\)、\(\phi^{-1}\) 统一改用其
   \(C_\varepsilon(1+t)^{(1+\varepsilon)/2}\) 界，重新证明 CS4、首接触和
   \(q_k/\phi(\theta_k)\) 的一致性；两条 schedule 不能在同一行程中混用。

因此本页把 outer-strip first-contact 的合取量词明确化，但仍是 conditional merge；它不能单独把 C303 升级为无条件惯性 PPA 定理或主要贡献。
