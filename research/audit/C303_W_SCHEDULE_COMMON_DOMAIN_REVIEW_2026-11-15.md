# C303: 接入 `W=e^{z^2}` 后的共同停止域核查

日期：2026-11-15  
状态：**continue validation / conditional schedule integration**

本页只核查一个接口：把 `c303_sharp_schedule_bootstrap.md` 的
\(W_k=e^{z_k^2}\) 比较接入 `c303_common_stopping_domain.md` 的 CS3--CS7。
它不把条件性的 \(W\) 超解、normal recursion、source gate 或 finite-prefix margin
升级为无条件 PPA 定理。

## 假设和量词

固定一个 \(\alpha\in(1/2,1)\)，而不是同时对所有 \(\alpha>1/2\) 取同一个误差
指数。设在最小出界步之前、从同一个首个 drop threshold \(K_*\) 开始，有

\[
 W_k=e^{z_k^2}\le K(1+t_k)\log(e+t_k),\qquad
 0\le \theta_k-z_k\le E,
 \tag{WS1}
\]

其中 \(E=C_1E_*\) 来自双侧角度余项和 transient normal tail，并且这些估计对
共同初始开集中的所有 pre-exit 轨道统一成立；同时要求 \(K\)、\(E_*\) 以及后续的
\(C_\varepsilon\) 在该有限前缀带上对同一开集和足够小的 \(h_0\) 统一有界。还假设

\[
 q_k:=\|w_k\|\le M h_k+Q_0e^{-\gamma(t_k-T_{\rm tr})},
 \qquad Q_0=O(h_0^2),
 \tag{WS2}
\]

以及同一首个 drop threshold 给出的有限前缀时间界
\(T_{\rm tr}=t_{K_*}\le T_*<\infty\)，其中对固定 \(\alpha\) 的 \(T_*\) 与 \(h_0\) 及初始 lifted angle 无关；还假设每条 pre-exit \(\tau\)-path 的物理位移、局部 lift 和半径界
\(\|y_\tau-x_j\|\le C h_j\)、\(r_\tau\in[1/2,3/2]\)。这些是接口的输入，不能由
本页的标量比较反向推出。

## WS1 给出的三组尾界

由 \(\theta_k=z_k+d_k\)、\(0\le d_k\le E\) 和 (WS1)，对任意固定
\(\varepsilon>0\) 都有

\[
 e^{\theta_k^2}\le C_\varepsilon(1+t_k)^{1+\varepsilon}.
 \tag{WS3}
\]

这里固定任意 \(0<\eta<\varepsilon/2\)，常数可吸收 \(\log(e+t_k)^{1+\eta}\) 和有界的
\(e^{d_k^2(1+1/\eta)}\)。因此在 \(\theta_k\ge\theta_*>0\) 时，C303 的实际
径向面余量和角漂移满足

\[
 m_{\rm face}(\theta_k)=m_0e^{-\theta_k^2+\theta_k}
   \ge c_\varepsilon(1+t_k)^{-(1+\varepsilon)},
\]

\[
 \phi(\theta_k)=\theta_ke^{-\theta_k^2}
   \ge c'_\varepsilon(1+t_k)^{-(1+\varepsilon)}.
 \tag{WS4}
\]

等价地，

\[
 m_{\rm face}(\theta_k)^{-1}+\phi(\theta_k)^{-1}
 \le C_\varepsilon(1+t_k)^{1+\varepsilon}.
 \tag{WS5}
\]

另一方面，(WS1) 只给出平方根对数角度。对任意固定 \(\delta>0\)，由
\(\sqrt{\log(e+t)}\le C_\delta+\delta\log(e+t)\) 可取

\[
 e^{\theta_k}\le C_\delta(1+t_k)^\delta.
 \tag{WS6}
\]

这个 \(\delta\) 可任意小，但常数依赖于 \(\delta\)；不能把 (WS6) 写成一个对
全部 \(\delta\) 或全部 \(\alpha\) 统一的常数。

## CS3 和 CS4

CS3 应改写为

\[
 \theta_\ell^2\le C+2\log(1+t_\ell),\qquad
 m_{\rm face}(\theta_\ell),\ \phi(\theta_\ell)
 \ge c_\varepsilon(1+t_\ell)^{-(1+\varepsilon)}.
 \tag{WS7}
\]

它不再使用旧的指数 2。对 normalized coordinate（为避免与 normal error
混淆记为 \(Q(r,\theta)\)），在 \(r\in[1/2,3/2]\)、\(|Q|\le\beta+\eta\) 上有
\(Q_r=O(e^\theta)\)、\(Q_\theta=O(1)\)。所以由 (WS6) 和位移界

\[
 |Q(y_\tau)-Q(x_j)|
 \le C h_j\bigl(1+e^{\theta_j}\bigr)
 \le C_\delta h_j(1+t_j)^\delta.
 \tag{WS8}
\]

由于 \(t_j\le C h_0(1+j)^{1-\alpha}\)，若
\(\delta<\alpha/(1-\alpha)\)，则

\[
 h_j(1+t_j)^\delta\to0.
 \tag{WS9}
\]

更强地，把 \(h_0(1+j)^{1-\alpha}\le1\) 与 \(\ge1\) 分开，可得
\(\sup_{j\ge K_*}h_j(1+t_j)^\delta\le C_\delta h_0\)（增大有限常数并固定
finite prefix 后）。于是 CS4 的 outer-strip 包含可在固定 \(\eta_{\rm strip}\) 下
由缩小 \(h_0\) 闭合，前提是 pre-exit 位移界本身已在同一停止域内成立。

## CS6/CS7 的 margin 比较

将 (WS2) 与 (WS5) 相乘，得到首接触误差的统一上界

\[
\begin{aligned}
 &(h_j+q_j)\bigl(m_{\rm face}(\theta_j)^{-1}
                 +\phi(\theta_j)^{-1}\bigr) \\
 &\quad\le C_\varepsilon(1+M)h_j(1+t_j)^{1+\varepsilon}
 +C_\varepsilon Q_0e^{-\gamma(t_j-T_{\rm tr})}(1+t_j)^{1+\varepsilon}.
\end{aligned}
\tag{WS10}
\]

The polynomial part has asymptotic exponent

\[
 h_j(1+t_j)^{1+\varepsilon}
 =O\!\left(j^{(1+\varepsilon)(1-\alpha)-\alpha}\right).
 \tag{WS11}
\]

Choose \(\varepsilon\) after fixing \(\alpha\) so that

\[
 0<\varepsilon<\frac{2\alpha-1}{1-\alpha},
 \qquad\text{equivalently}qquad
 \alpha>\frac{1+\varepsilon}{2+\varepsilon}.
 \tag{WS12}
\]

Then (WS11) tends to zero. The same two-range split as in CS4 gives a uniform
\(O(h_0)\) bound after the finite prefix. For the transient term, with
\(u=t_j-T_{\rm tr}\ge0\),

\[
 \sup_{u\ge0}e^{-\gamma u}(1+T_{\rm tr}+u)^{1+\varepsilon}<\infty,
 \tag{WS13}
\]

so its contribution in (WS10) is \(O(Q_0)=O(h_0^2)\). Thus, for each fixed
\(\alpha>1/2\), first choose \(\varepsilon\) as in (WS12), then choose \(h_0\) and the
finite-prefix margin so that the right side of (WS10) is below the strict margin
constant. This supplies the smallness needed in

\[
\dot s_i(y_{\tau_*})
 \ge \beta_j\bigl[m_{\rm face}(\theta(\tau_*))
       -C(h_j+q_j)\bigr],
\]

and

\[
\dot\theta(y_{\tau_*})
 \ge \beta_j\bigl[c\phi(\theta(\tau_*))-C(h_j+q_j)\bigr].
 \tag{WS14}
\]

The contact point may be compared to \(\theta_j\) because
\(|\theta(\tau_*)-\theta_j|\le C h_j\) and
\(|(\log m_{\rm face})'|+|(\log\phi)'|=O(1+\theta_j)\). Since
\(\theta_j=O(\sqrt{\log(e+t_j)})\),

\[
 h_j(1+\theta_j)\to0,
 \qquad
 \frac{m_{\rm face}(\theta(\tau_*))}{m_{\rm face}(\theta_j)}
 ,\ \frac{\phi(\theta(\tau_*))}{\phi(\theta_j)}\to1.
 \tag{WS15}
\]

The signs in (WS14) then follow for all sufficiently large \(j\), while the finite
prefix must still be covered by its independent uniform margin.

## Exact range and obstruction

Under (WS1)--(WS2), the CS3/CS4/CS6/CS7 estimates are conditionally compatible for
every fixed \(\alpha\in(1/2,1)\), with \(\varepsilon\) chosen by (WS12). This is not a
uniform statement as \(\alpha\downarrow1/2\): the permissible \(\varepsilon\) tends to zero
and the constants in (WS3)--(WS5) may blow up.

At \(\alpha=1/2\), every \(\varepsilon>0\) makes the exponent in (WS11) positive.
Even if one formally sets \(\varepsilon=0\), the sharper unshifted estimate gives
\(\phi(\theta_k)\asymp[(1+t_k)\sqrt{\log(e+t_k)}]^{-1}\), hence
\(h_k/\phi(\theta_k)\asymp\sqrt{\log k}\). The existing \(O(h_k)\) contact error
therefore cannot be absorbed at the critical endpoint. This is a genuine schedule
obstruction, not a notation issue.

## Remaining obligations and verdict

The companion independent ratio audit is recorded in
`C303_SHARP_SCHEDULE_COMMON_DOMAIN_REVIEW_2026-11-15.md`. The W schedule can replace the \(p=2\), \(\alpha>2/3\) exponents in CS3--CS7 only
conditionally. To turn the calculation into a theorem one still must prove, uniformly
on the same common initial open set and up to the same minimal first-exit index:

1. the two-sided angular estimate with the \(h_kq_k\) term and the summable transient
   error used to obtain (WS1);
2. the normal recursion (WS2) on the same outer strip before that first exit;
3. the pre-exit displacement/lift bounds used in (WS8), including a radial buffer for
   \(r\in[1/2,3/2]\);
4. the finite-prefix \(K_*\) margin, with no later threshold silently substituted;
5. HJ cutoff/source and physical-lift injectivity conditions;
6. the uniform finite-prefix time bound \(T_{\rm tr}=t_{K_*}\le T_*\), so the transient term is small on one common initial open set.

Consequently this page is a **conditional integration lemma / continue validation**.
It gives the exact admissible schedule range and the critical obstruction, but does not
upgrade C303 to a complete or major-contribution theorem.

