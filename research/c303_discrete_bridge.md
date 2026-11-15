# C303: a non-formal discrete inertial-PPA bridge for the HJ spiral

## Exact question

The HJ construction supplies a smooth potential
\[
\chi_a(x)=a f(x)-\tfrac12\|\nabla f(x)\|^2
\]
for which the damped second-order system
\[
 x''+a x'+\nabla\chi_a(x)=0
\]
has an open phase-space basin whose position omega-limit is a circle. The candidate below asks whether one can obtain the same open-basin nonconvergence from a **complete, explicitly defined, variable-step inertial PPA**, rather than by taking an exact flow map or writing a tautological inverse relation.

## Proposed discrete algorithm

Let (h_k=h_0(k+1)^{-\alpha}) with
\[
\frac23<\alpha<1,
\qquad t_k=\sum_{j<k}h_j\to\infty,
\]
and define
\[
\beta_k=\frac{h_k}{1+a h_k},
\qquad
\lambda_k=h_k\beta_k=\frac{h_k^2}{1+a h_k}.
\]
For the complete single-valued relation (F=\nabla\chi_a), set
\[
 y_k=J_{\lambda_kF}(x_k+\beta_k v_k),
 \qquad
 x_{k+1}=y_k,
 \qquad
 v_{k+1}=\frac{x_{k+1}-x_k}{h_k}.
\tag{D1}
\]
The resolvent equation is
\[
 x_{k+1}+\lambda_k\nabla\chi_a(x_{k+1})
 =x_k+\beta_kv_k,
\tag{D2}
\]
which is equivalent to the implicit inertial Euler step
\[
 v_{k+1}=v_k-h_k\bigl(a v_{k+1}+\nabla\chi_a(x_{k+1})\bigr),
 \qquad
 x_{k+1}=x_k+h_kv_{k+1}.
\tag{D3}
\]
Thus (D1) is a genuine proximal iteration with an explicit graph, step size, momentum input, and state update. It is not the exact time-(h_k) flow map.

### Complete graph and coverage gate

The HJ (f) is globally (C^\infty) after its cutoff extension. If the cutoff is compactly supported, then \(\nabla\chi_a\) is globally Lipschitz with some finite constant (L_\chi). For
\[
0<\lambda_k<1/L_\chi,
\]
the map (u\mapsto u+\lambda_k\nabla\chi_a(u)) is strongly monotone and coercive:
\[
\langle u-v, (u+\lambda_k\nabla\chi_a(u))-(v+\lambda_k\nabla\chi_a(v))\rangle
\ge (1-\lambda_kL_\chi)\|u-v\|^2.
\]
It is therefore a global homeomorphism of \(\mathbb R^2\), so every input in (D2) has exactly one output. This supplies full Minty coverage and avoids a hidden local-root selection. Verifying the compact-support/cutoff convention in the HJ source is a mandatory proof obligation; if only local boundedness is available, (D1) is merely a local branch and the bridge does not close.

## Why the schedule can preserve the shrinking spiral tube

The continuous proof has tail estimates
\[
Y_\vartheta\asymp \vartheta e^{-\vartheta^2},
\qquad
m(\vartheta)\asymp e^{-\vartheta^2+\vartheta},
\]
and the HJ tube dynamics gives (e^{\vartheta(t)^2}=\Theta(t)) up to subpolynomial factors. Hence both the angular drift and the inward boundary margin are polynomially small in (t), while (t_k\asymp k^{1-\alpha}). The one-step truncation error of (D3) is (O(h_k^2)). The crucial ratio is
\[
\frac{h_k^2}{h_km(\vartheta_k)}=\frac{h_k}{m(\vartheta_k)}
\asymp k^{-\alpha+(1-\alpha)+o(1)}\to0
\quad(\alpha>1/2).
\]
The stronger choice \(\alpha>2/3\) also makes the tail sum of local errors \(\sum_{j\ge k}h_j^2=O(k^{1-2\alpha})\) decay faster than the margin scale (k^{-(1-\alpha)+o(1)}), which is useful for a shadowing formulation.

## Discrete normal variable and the (w)-estimate

Let
\[
 w_k=v_k+\nabla f(x_k).
\]
Using (\nabla\chi_a=a\nabla f-\nabla^2f\,\nabla f), Taylor expansion of (\nabla f(x_{k+1})), and (D3), one obtains on the closed tail tube
\[
 w_{k+1}
 =\frac{(I+h_k\nabla^2f(x_k))w_k}{1+a h_k}+O(h_k^2)(1+\|w_k\|^2).
\tag{D4}
\]
If (a>\sup\lambda_{\max}(\nabla^2f)+\delta), then, for (h_k) small,
\[
 \|w_{k+1}\|
 \le (1-\tfrac\delta2h_k)\|w_k\|+C h_k^2.
\tag{D5}
\]
A discrete comparison gives \(\|w_k\|=O(h_k)\) after a finite prefix, uniformly for an open set of sufficiently small initial (w_0). This (O(h_k)) error is smaller than the shrinking boundary margin when \(\alpha>1/2\).

## First-exit bootstrap for the discrete tube

Let (s_1=r-b_1(\vartheta)), (s_2=b_2(\vartheta)-r). Taylor expansion of (D3) at a putative first boundary hit gives
\[
 s_i(x_{k+1})-s_i(x_k)
 \ge h_km(\vartheta_k)-C h_k\|w_k\|-C h_k^2.
\tag{D6}
\]
By (D5), (D6), and (h_k=o(m(\vartheta_k))), the right side is positive at every boundary contact after the finite initial prefix. Choose a compact initial subband with positive margin and then shrink the open (w_0)-ball to handle that prefix. A first-exit contradiction closes (s_i>0) for all (k).

The angular increment obeys
\[
\vartheta_{k+1}-\vartheta_k
 =h_k\bigl(Y_\vartheta/r+O(\|w_k\|)\bigr)+O(h_k^2).
\tag{D7}
\]
The same (h_k=o(\vartheta e^{-\vartheta^2})) comparison gives positive increments and excludes a finite angular limit. Since \(\sum_k h_k=\infty\), the unwrapped angle tends to (+\infty\). The tube width tends to zero, so (r_k\to1); the increments tend to zero, so the mod-\(2\pi\) phases are dense along the traversed circle. Therefore
\[
\omega(x_k)=S^1,
\qquad
\lim_{k\to\infty}x_k\ \text{does not exist}.
\tag{D8}
\]

## The decisive proof obligations

1. **Global graph identity:** verify from the HJ source that the cutoff extension makes (f) (and hence \(\nabla\chi_a\)) globally smooth with bounded Hessian, or construct an explicit global bounded-Hessian extension that agrees on the tail tube.
2. **Complete PPA coverage:** prove (I+\lambda_k\nabla\chi_a\) is onto and one-to-one for every (k), not merely locally invertible on the tube.
3. **Uniform discrete expansion:** derive (D4) with constants uniform in the unbounded angle coordinate and all states in the closed tail tube; keep the (h_k^2) terms that do not contain (w_k).
4. **Margin comparison:** prove (m(\vartheta_k)\) and (Y_\vartheta(\vartheta_k)) lower bounds along the discrete first-exit bootstrap, without assuming the tube before the bootstrap closes.
5. **Initial open set:** choose a finite angular band and a positive-width spatial subband, then an explicit open (w_0)-ball that survives the finite prefix. The quantifier must cover every initial state in this open phase-space set.
6. **No exact-flow shortcut:** (D1) must remain the actual implemented update; an exact-flow map or a relation defined by inverting that map would not answer the bridge question.

## Independent verdict

**Continue validation.** This is a plausible non-formal bridge: the variable-step inertial PPA has a complete explicit graph under a bounded-Hessian cutoff, and the schedule (h_k\asymp k^{-\alpha}), \(\alpha>2/3\), is tuned so that discretization errors decay faster than the HJ shrinking margin while total simulated time diverges. It could turn the ODE candidate into a genuine discrete PPA counterexample. The bridge is not proved here; the global cutoff/coverage check and the uniform estimates (D4)–(D7) are the single highest-value next task. If the HJ cutoff is not compactly supported or the uniform (O(h_k^2)) remainder fails, salvage only a local selected-branch result, which does not meet the project’s complete-graph requirement.
