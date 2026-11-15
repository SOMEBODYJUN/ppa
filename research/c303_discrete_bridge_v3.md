# C303 discrete bridge v2: derivation, coverage, and the schedule gate

## Status

This is an independent proof attack on `c303_discrete_bridge.md`. The bridge remains a candidate. The main correction is that the schedule exponent cannot be fixed at `alpha>2/3` before the first-exit bootstrap produces a quantitative polynomial exponent. The safe statement chooses `alpha` after that exponent is known.

## 1. Complete proximal update

Let (g=\nabla f), (H=\nabla^2f), and
\[
\chi_a=a f-\tfrac12\|g\|^2,
\qquad
\nabla\chi_a=a g-Hg.
\]
For a step (h>0), put
\[
\beta=\frac{h}{1+ah},qquad \lambda=h\beta=\frac{h^2}{1+ah}.
\]
The update
\[
 y=J_{\lambda\nabla\chi_a}(x+\beta v),qquad
 x^+=y,qquad v^+=\frac{x^+-x}{h}
\tag{V1}
\]
is equivalent to
\[
(1+ah)v^+=v-h\nabla\chi_a(x^+),qquad x^+=x+hv^+.
\tag{V2}
\]
This is an implicit Euler step for the damped second-order system, with the damping term implicit. It is a genuine inertial PPA update; it is not the exact flow map.

Assume the HJ cutoff extension gives (f\in C^3(\mathbb R^2)) with bounded (g,H,D^3f). Then (\nabla\chi_a\) is globally Lipschitz. Indeed
\[
D(\nabla\chi_a)=aH-D(Hg),
\]
and (D(Hg)[\xi]=D^3f[\xi,\cdot]g+H^2\xi), so
\[
L_\chi:=\sup_x\|aH(x)-D(Hg)(x)\|<\infty.
\]
For (0<\lambda<1/L_\chi),
\[
\langle u-v,(u+\lambda\nabla\chi_a(u))-(v+\lambda\nabla\chi_a(v))\rangle
\ge (1-\lambda L_\chi)\|u-v\|^2.
\tag{V3}
\]
The map (u\mapsto u+\lambda\nabla\chi_a(u)) is strongly monotone and coercive, hence a global bijection of (mathbb R^2). Thus (V1) has complete all-input coverage and a unique output. If the original HJ cutoff is not globally bounded-derivative, this paragraph is an additional extension obligation; a local IFT branch would not satisfy the complete-graph requirement.

## 2. Exact Taylor expansion for the normal error

Define
\[
 w=v+g(x),\qquad w^+=v^++g(x^+),\qquad \delta=x^+-x=hv^+.
\]
Let (M_2=\sup\|H\|), (M_3=\sup\|D^3f\|), and (G=\sup\|g\|) on the closed tail tube. Taylor's theorem gives
\[
 g(x^+)-g(x)=H(x)\delta+R_g,
\qquad
\|R_g\|\le \tfrac12M_3\|\delta\|^2.
\tag{V4}
\]
From (V2),
\[
 w^+(1+ah)=v+g(x^+)+hH(x^+)g(x^+).
\tag{V5}
\]
Use (v=w-g(x)), (V4), and
\[
H(x^+)g(x^+)=H(x)g(x)+R_H,
\qquad
\|R_H\|\le C_1\|\delta\|+C_2\|\delta\|^2,
\tag{V6}
\]
where (C_1=M_3G+M_2^2) on the tube. Since (v^+=v+O(h)) for bounded (v,g), one has
\[
H(x)\delta+hH(x)g(x)=hH(x)w+O(h^2)(1+\|w\|),
\]
and therefore
\[
 w^+=\frac{(I+hH(x))w}{1+ah}+R_w,
\qquad
\|R_w\|\le C h^2(1+\|w\|^2).
\tag{V7}
\]
The constants are uniform on the closed tail tube. If (a\ge\sup\lambda_{\max}H+\delta), then for sufficiently small (h\),
\[
\|w^+\|\le (1-\delta h/2)\|w\|+Ch^2.
\tag{V8}
\]
For (h_k=h_0(k+1)^{-\alpha}), the discrete comparison has the invariant bound
\[
\|w_k\|\le M h_k
\tag{V9}
\]
after a finite prefix, provided (M\ge 2C/\delta) and (h_0) is small enough. The reason is that (h_k-h_{k+1}=O(h_k/k)), while (\delta h_k^2\gg h_k/k) for every (alpha<1); enlarge (M) to cover the finite prefix.

## 3. Correct first-exit argument (implicit shifted-boundary path)

The endpoint x_{k+1} can jump across a radial boundary in one step, so an estimate of the signed endpoint difference s_i(x_{k+1})-s_i(x_k) is not valid by itself. The right barrier uses the continuous inverse-resolvent path inside the same complete graph.

Fix an input (x_k,v_k) in the tail tube and write h=h_k. For tau in [0,1], set

    h_tau = tau h,
    beta_tau = h_tau/(1+a h_tau),
    lambda_tau = h_tau^2/(1+a h_tau),
    y_tau = J_{lambda_tau nabla chi_a}(x_k + beta_tau v_k).        (D6.1)

Strong monotonicity in (V3), uniformly for 0<=tau<=1, gives a unique output and continuity of tau -> y_tau; y_0=x_k and y_1=x_{k+1}. Put v_tau=(y_tau-x_k)/h_tau for tau>0, with v_0=v_k by the implicit equation. Then

    (1+a h_tau) v_tau = v_k - h_tau nabla chi_a(y_tau),
    y_tau = x_k + h_tau v_tau.                                    (D6.2)

Thus w_tau=v_tau+g(y_tau) obeys the same expansion as (V7), with h replaced by h_tau and initial error w_k=v_k+g(x_k). Uniformly in 0<=tau<=1,

    w_tau = (I+h_tau H(x_k)) w_k/(1+a h_tau) + R_tau,
    ||R_tau|| <= C h_tau^2 (1+||w_k||^2).                         (D6.3)

Therefore, once the induction bound ||w_k||=O(h_k) is available,

    sup_{0<=tau<=1} ||w_tau||
       <= ||w_k|| + C h_k ||w_k|| + C h_k^2 = O(h_k).               (D6.4)

Assume y_tau has a first contact with a radial boundary s_i=0 at tau_* in (0,1], while y_tau is in D for tau<tau_*. At y_*=y_{tau_*}, (D6.2) and v_{tau_*}=Y(y_*)+w_{tau_*} give

    x_k = y_* - tau_* h (Y(y_*) + w_{tau_*}).

Taylor expansion of s_i at y_*, using the inward estimate (V10), yields

    s_i(x_k)
      = -tau_* h grad(s_i)(y_*) dot Y(y_*)
        -tau_* h grad(s_i)(y_*) dot w_{tau_*} + O(h^2)
      <= -tau_* h m(theta_*) + C tau_* h ||w_{tau_*}|| + C h^2.   (D6.5)

The tail condition h_k=o(m(theta_k)), together with (D6.4), makes the right side strictly negative, contradicting x_k in D. This contradiction is quantified for every k and either i=1,2, so no first radial contact is possible. If first contact occurs at the entrance boundary theta=theta_0, then Y_theta>0 on the tail and the same Taylor calculation in the angular coordinate gives theta(x_k)<theta_0, again contradicting x_k in D. Thus the implicit branch preserves D without assuming that an integer endpoint lies on the boundary.

A finite initial prefix is handled by shrinking the initial compact tube and choosing h_0 below the finitely many local constants. The remaining obligations are the global bounded-derivative cutoff and the uniform constants in (D6.3); neither can be replaced by the continuous-time first-contact sentence.

## 4. Discrete angular bootstrap and the schedule correction

On the tail tube,
\[
 c_0\vartheta e^{-\vartheta^2}\le Y_\vartheta\le C_0\vartheta e^{-\vartheta^2}.
\]
The discrete angular increment is
\[
\vartheta_{k+1}-\vartheta_k
 =h_k\frac{Y_\vartheta(x_k)}{r_k}+O(h_k\|w_k\|)+O(h_k^2).
\tag{V14}
\]
For an upper bound before first exit, the summable (O(h_k^2)) term contributes only a finite angle shift because (alpha>1/2). After absorbing this shift, the same scalar comparison as in the ODE gives a finite (p) and (C_p) with
\[
\vartheta_k^2\le C_p+p\log(1+t_k),
\qquad t_k=\sum_{j<k}h_j.
\tag{V15}
\]
The exact value of (p) depends on the constants in the HJ tube estimate; it should not be silently fixed to (2) without a separate sharp comparison. From (V15),
\[
 m(\vartheta_k)\ge c_p(1+t_k)^{-p}.
\tag{V16}
\]
Since (t_k\asymp k^{1-\alpha}), (V13) follows whenever
\[
\alpha>p(1-\alpha),qquad	ext{i.e.}qquad
\alpha>\frac{p}{p+1}.
\tag{V17}
\]
There is always such an (alpha<1) once (p<\infty). The earlier universal claim “any \(\alpha>2/3) suffices” is therefore too strong unless one proves (p\le2). A safe construction first proves (V15), then chooses
\[
\alpha\in\left(\max\left\{\frac23,\frac{p}{p+1}\right\},1\right).
\]
For this choice h_k=o(m(theta_k)). The same upper bound (V15) also gives
    theta_k exp(-theta_k^2) >= c_p theta_k (1+t_k)^(-p),
after increasing the finite-prefix threshold if necessary. Hence h_k=o(theta_k exp(-theta_k^2)) follows from the same inequality alpha>p/(p+1), with the extra factor theta_k only helping. Therefore (D6.5) and (V14) imply positive angular increments after a finite prefix.

If (\vartheta_k\) had a finite limit, the positive lower bound in (V14) together with \(\sum h_k=\infty\) would be impossible. Hence \(\vartheta_k\to\infty), (r_k\to1), and the phase increments tend to zero. Every phase modulo (2\pi) is approached along a subsequence, so (\omega(x_k)=S^1).

## 5. Independent verdict

**Continue validation.** No fatal obstruction was found after the correction (V17), but the bridge is not yet a theorem. The decisive obligations are: verify the HJ cutoff really gives globally bounded (D^3f) (hence complete PPA coverage), derive the uniform remainder in (V7) from the exact implicit step, and write the strip version (V11) into the first-exit proof. If any of these fail, the salvage is only a local selected-root inertial discretization, which does not meet the complete-graph requirement.
