# C303 v3: resolvent-τ path barrier

状态：**candidate / conditional lemma**。本页给出一个可以修补 D6 首次越界量词的正式 τ-path 引理，并列出其不可省略的全局假设。它不宣称 C303 离散桥已经闭合。

## 1. Setting

Let

\[
 F=\nabla\chi_a,\qquad
 \chi_a=a f-\tfrac12|\nabla f|^2,
 \qquad
 Y=-\nabla f,
\]

and let (h_k=h_0(k+1)^{-\alpha}), (2/3<\alpha<1),

\[
 \beta_k=\frac{h_k}{1+a h_k},
 \qquad
 \lambda_k=h_k\beta_k.
\]

The discrete step is

\[
 x_{k+1}+\lambda_kF(x_{k+1})=x_k+\beta_kv_k,
 \qquad
 v_{k+1}=\frac{x_{k+1}-x_k}{h_k}.
\tag{T1}
\]

Use the lifted HJ tube

\[
 \widetilde D=\{(r,\theta):\theta>\theta_*,\ b_1(\theta)<r<b_2(\theta)\},
\]

with (H(\theta)=e^{-\theta^2}), (Delta(\theta)\asymp e^{-\theta}), and physical projection (Pi(r,\theta)=r(\cos\theta,\sin\theta)). Assume the HJ non-overlap condition makes (Pi|_{\overline{\widetilde D}}) injective; this is the physical-lift gate.

For (s_1=r-b_1(\theta)), (s_2=b_2(\theta)-r), assume on the closed tail tube

\[
 \nabla s_i\cdot Y\ge m_0H(\theta)e^\theta,
 \qquad
 \frac{Y_\theta}{r}\ge c_0\theta H(\theta),
 \qquad
 |\nabla s_i|\le L_s .
\tag{T2}
\]

The proof also needs the following global gates:

* (F) is globally (C^1) and (L_F)-Lipschitz, with (lambda_0L_F<1/2);
* (\nabla f) is globally (K_f)-Lipschitz (or has the same bound on a fixed outer strip);
* on that outer strip, (|Y|+|F|\le M) and (|DY|\le C H(\theta)e^{2\theta});
* the normal error (w_k:=v_k+\nabla f(x_k)) obeys (|w_k|\le M_w h_k) after a finite prefix.

The last estimate is the D4--D5 obligation; it is not supplied by the τ-path argument.

## 2. Resolvent homotopy is (C^1)

For a fixed step (k), define

\[
 y_\tau+\tau\lambda_kF(y_\tau)=x_k+\tau\beta_kv_k,
 \qquad
 0\le\tau\le1.
\tag{T3}
\]

Since (\tau\lambda_kL_F<1/2), (I+\tau\lambda_kF) is a global (C^1) diffeomorphism. Thus (y_\tau) is a unique (C^1) path, with (y_0=x_k), (y_1=x_{k+1}). Differentiating (T3),

\[
 \dot y_\tau
 =\beta_k(I+\tau\lambda_kDF(y_\tau))^{-1}
       \bigl(v_k-h_kF(y_\tau)\bigr).
\tag{T4}
\]

The input (x_k+\tau\beta_kv_k) is bounded whenever (x_k) lies in the tube and (w_k=O(h_k)). Strong monotonicity then bounds (y_\tau) uniformly:

\[
 |y_\tau|
 \le \frac{|x_k+\tau\beta_kv_k|+\tau\lambda_k|F(0)|}
              {1-\tau\lambda_kL_F}.
\tag{T5}
\]

Consequently

\[
 |\dot y_\tau|\le C h_k,
 \qquad
 |y_\tau-x_k|\le C h_k.
\tag{T6}
\]

This endpoint estimate is obtained before any tube invariance claim; it is not inferred from D6.

## 3. The τ-normal error

Define the rescaled path error

\[
 \widetilde w_\tau:=\beta_k^{-1}\dot y_\tau+\nabla f(y_\tau).
\tag{T7}
\]

Because (Y=-\nabla f), (T4) gives the exact representation

\[
 \beta_k^{-1}\dot y_\tau
 = (I+\tau\lambda_kDF(y_\tau))^{-1}
   \bigl(v_k-h_kF(y_\tau)\bigr).
\]

Using (w_k=v_k+\nabla f(x_k)), (T5)--(T6), and the global (K_f,L_F,M) bounds,

\[
 |\widetilde w_\tau-w_k|\le C h_k .
\tag{T8}
\]

Hence

\[
 |\widetilde w_\tau|\le |w_k|+C h_k=O(h_k),
 \qquad
 \dot y_\tau=\beta_k\bigl(Y(y_\tau)+\widetilde w_\tau\bigr).
\tag{T9}
\]

If only local bounds are available, (T8) is valid up to the first contact provided the whole pre-contact path lies in the declared outer strip.

## 4. First-contact barrier

Assume (x_k\inPi(\widetilde D)), and suppose (y_1\notin\Pi(\widetilde D)). By (T3), (T6), and (r\ge1/2), the physical path has a continuous local polar lift ((r_\tau,\theta_\tau)) starting at the lift of (x_k). Injectivity of (Pi|_{\overline{\widetilde D}}) fixes the unwrapped branch. Let (\tau_*) be the first contact with the boundary of (widetilde D).

At a radial face (s_i=0), first contact requires

\[
 \frac{d}{d\tau}s_i(y_\tau)\big|_{\tau=\tau_*}\le0.
\tag{T10}
\]

On the other hand, (T2) and (T9) give

\[
 \frac{d}{d\tau}s_i(y_\tau)\big|_{\tau_*}
 \ge\beta_k\bigl(m_0H(\theta_{\tau_*})e^{\theta_{\tau_*}}
       -L_s(|w_k|+C h_k)\bigr).
\tag{T11}
\]

The angular bootstrap below implies (h_k/[H(\theta_*)e^{\theta_*}]\to0) uniformly on the first-contact stopping interval. Since (|w_k|=O(h_k)), the right side of (T11) is positive for all sufficiently large (k). A finite prefix is handled by choosing the initial spatial subband and (w_0)-ball with positive margin. This contradicts (T10).

At the lower angular face (\theta=\theta_*),

\[
 \frac{d\theta_\tau}{d\tau}
 \ge\beta_k(c_0\theta_*H(\theta_*)-C h_k)>0
\]

for all sufficiently large (k), so it cannot be the first contact either. Therefore (y_1\in\Pi(\widetilde D)). The argument closes an entire integer step; it never applies an inward estimate to an unknown out-of-domain endpoint.

## 5. Non-circular angular bootstrap

Let (\varphi(s)=s e^{-s^2}), decreasing for (s\ge1). While the tube is not exited, the τ-path estimates imply

\[
 \theta_{k+1}-\theta_k
 \le C h_k\varphi(\theta_k)+C h_k^2,
 \qquad
 \theta_{k+1}-\theta_k
 \ge c h_k\varphi(\theta_k)-C h_k^2.
\tag{T12}
\]

The (O(h_k^2)) terms include the (O(h_k)) change of (\varphi) along the path; this uses boundedness of (\varphi') and (\theta\varphi(\theta)) on ([1,\infty)).

Set (E_k=\sum_{j\ge k}h_j^2), (E=CE_0), and (z_k=\theta_k-C(E_0-E_k)). Choose (h_0) so (z_k\ge1). Then

\[
 z_{k+1}-z_k\le C h_k\varphi(\theta_k)\le C h_k\varphi(z_k),
 \qquad
 \theta_k\le z_k+E.
\]

For (U_k=\exp((z_k+E)^2/2)), negative (z)-increments only decrease (U); for a positive increment, the mean value theorem and (\varphi(z)=z e^{-z^2}) give

\[
 U_{k+1}-U_k
 \le C h_k(z_k+E)z_k
       \exp\left(-\frac{z_k^2}{2}+Ez_k+\frac{E^2}{2}\right)
 \le C' h_k.
\tag{T13}
\]

Thus (U_k\le U_0+C't_k), and therefore

\[
 e^{\theta_k^2/2}\le C(1+t_k),
 \qquad
 \theta_k^2\le C+2\log(1+t_k).
\tag{T14}
\]

Since (m(\theta)=H(\theta)e^\theta\ge c(1+t_k)^{-2}) and (\varphi(\theta_k)\ge c(1+t_k)^{-2}),

\[
 \frac{h_k}{m(\theta_k)},\ \frac{h_k}{\varphi(\theta_k)}
 \le C k^{2-3\alpha}\to0
 \qquad(\alpha>2/3),
\tag{T15}
\]

using (t_k\asymp k^{1-\alpha}). This closes the positivity estimates in (T11) and (T12) without circularly assuming a logarithmic angular bound.

## 6. Angle divergence and physical omega-limit

After the integer-step barrier is closed, the lower estimate in (T12) and (T15) give strict angle increase. If θ were bounded, φ(θ) would have a positive lower bound on the resulting compact interval, whereas Σh_k=∞; contradiction. Hence θ_k→∞. Since (b_i(\theta)=1+O(e^{-\theta})), (r_k\to1). Injectivity of the physical lift and unbounded unwrapped angle imply the physical omega-limit is (S^1).

## 7. Verdict and remaining obligations

The τ-path lemma closes the **integer-step crossing** under explicit gates: global resolvent coverage, bounded endpoint displacement, a global or outer-strip Lipschitz bound for ∇f, the D4--D5 estimate (w_k=O(h_k)), and the HJ boundary signs. It does not prove those gates. In particular:

1. if (F=\nabla\chi_a) is not globally Lipschitz, (T3) may fail to be a complete single-valued path;
2. if the HJ cutoff does not leave a whole outer strip around the tail tube, (T8) cannot be invoked at first contact;
3. if (w_k=O(h_k)) is not established uniformly, the boundary error in (T11) can dominate the shrinking margin;
4. if (T13)--(T14) is replaced by the informal (e^{\theta^2}=\Theta(t)) claim, the bootstrap is circular.

Thus the v3 τ-path is a valid conditional repair, not a fatal counterexample and not yet a complete C303 theorem.
