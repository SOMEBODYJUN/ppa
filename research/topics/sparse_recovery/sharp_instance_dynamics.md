# A sharp quartic least-squares instance: true residual and complete PPA

**Status:** `derived-checked`. Two independent mathematical readers reconstructed the complete-fiber, quantitative remainder, residual, and actual-trajectory arguments below and found no mathematical blocker; their checks are recorded in the reception audits linked under Evidence. The finite checks corroborate the displayed arithmetic and trajectories; they do not prove any universal quantifier. This is a fixed explicit example, not a theorem for every degenerate minimum or every least-squares instance. Its precise published priority has not been determined.

**Objects and dependencies:** This file is self-contained apart from elementary smooth calculus, the analytic implicit function theorem, the Cauchy coefficient estimate, and the defining Fermat/smooth-sum rules for the limiting subdifferential. It closes the matching-residual and actual-trajectory obligations left open for one instance in [C225](automatic_regularity.md#sr-sharpness). It does not apply the positive-active-Hessian theorem C226 to a singular Hessian.

<a id="sd-theorem"></a>
## Exact statement

Fix

\[
p=7/4,\quad \eta=1,\quad R=2^{4/7},\quad
Q=\frac R{16}\begin{pmatrix}19&13\\13&19\end{pmatrix},\quad
\bar x=(1,1),\quad c=(1+3R/2)(1,1),
\]

and take \(A=Q^{1/2}\), \(b=A^{-T}c\). In particular \(A^TA=Q\), \(A^Tb=c\), and both columns of \(A\) are nonzero. Define on all of \(\mathbb R^2\)

\[
\Phi(x)=\tfrac12\|Ax-b\|_2^2+\|x\|_1-\|x\|_{7/4},\quad
F=\partial_{\rm lim}\Phi,\quad S=F^{-1}(0),\quad
r_F(x)=\inf_{v\in F(x)}\|v\|_2.
\]

The complete resolvent is \(J_{\lambda F}(z)=\{y:z-y\in\lambda F(y)\}\), with every output \(y\in\mathbb R^2\) initially allowed. Put

\[
\mathcal B=\{x=(1+h+t,1+h-t): |h|,|t|\le 1/32\},\qquad
\mathcal U=\overline B_{1/64}(\bar x).
\]

The following assertions hold.

1. \(\bar x\) is a strict local minimum and is the sole stationary point in \(\mathcal B\). The active Hessian at \(\bar x\) has eigenvalues \(2R\) and \(0\).
2. On \(\mathcal B\) the **strong true-residual error bound** is
   \[
   \|x-\bar x\|_2\le (512/R)^{1/3}r_F(x)^{1/3}.
   \]
   The exponent \(1/3\) is optimal: no exponent greater than \(1/3\), with any finite constant and any neighborhood of \(\bar x\), satisfies this bound. On \(\mathcal U\), \(d(x,S)=\|x-\bar x\|_2\), so the same statement also gives the ordinary error bound to the entire stationary set.
3. For **every** \(0<\lambda\le 1/128\) and **every** \(z\in\mathcal U\), the complete \(J_{\lambda F}(z)\) is a singleton, equals the global minimizing proximal map
   \[
   \mathop{\rm argmin}_{y\in\mathbb R^2}
   \left\{\Phi(y)+\frac{\|y-z\|_2^2}{2\lambda}\right\},
   \]
   and belongs to \(\mathcal U\). Thus this is an invariant nonempty input ball for the same original complete graph, not just a local inverse or a selected stationary branch.
4. Fix any one \(\lambda\in(0,1/128]\), and run the ordinary complete PPA from **any** \(x_0\in\mathcal U\): \(x_{k+1}\in J_{\lambda F}(x_k)\). This trajectory is unique and converges to \(\bar x\). Writing \(x_k=(1+h_k+t_k,1+h_k-t_k)\), if \(t_0\ne0\), then \(t_k\) keeps its initial sign, and
   \[
   \frac{h_k}{t_k^2}\longrightarrow-\frac3{32},\qquad
   \sqrt{k}|t_k|\longrightarrow\sqrt{\frac{128}{13\lambda R}},\qquad
   \boxed{\sqrt{k}\|x_k-\bar x\|_2\longrightarrow
   \frac{16}{\sqrt{13\lambda R}}.}
   \]
   Consequently every off-axis input in this ball produces a genuine \(\Theta(k^{-1/2})\) complete-PPA tail. If \(t_0=0\), the exact separate formula is \(t_k=0\), \(h_k=(1+2\lambda R)^{-k}h_0\). The origin of the \((h,t)\) coordinates is the stationary trajectory.

The constants \(1/64\) and \(1/128\) below are certified sufficient values, not maximal basin or step bounds. The asymptotic assertions fix \(\lambda\); they do not assert this particular constant for an arbitrary variable-step sequence.

<a id="sd-scalar-certificate"></a>
## Exact scalar formula and analytic remainder certificate

Throughout \(\mathcal B\), the two coordinates of \(x\) are positive. Put \(s=1+h\), \(u=t/s\), and

\[
f(u)=\left(\frac{(1+u)^{7/4}+(1-u)^{7/4}}2\right)^{4/7},\qquad
\varphi(h,t)=\Phi(1+h+t,1+h-t)-\Phi(\bar x).
\]

The eigenvalues of \(Q\) are \(2R\) in the radial direction \((1,1)\) and \(3R/8\) in the tangent direction \((1,-1)\). Substitution, including \(c=A^Tb\), gives the exact identity

\[
\frac{\varphi(h,t)}R=2h^2+\frac38t^2-s(f(u)-1). \tag{1}
\]

In particular \(\nabla\Phi(\bar x)=0\). The symmetric binomial expansion gives

\[
f(u)=1+\frac38u^2-\frac{11}{256}u^4+E(u). \tag{2}
\]

Here, for **all real** \(|u|\le1/16\),

\[
|E(u)|\le5|u|^6,\quad |E'(u)|\le28|u|^5,\quad
|E''(u)|\le140|u|^4. \tag{3}
\]

For completeness these bounds have an analytic certificate, rather than a sampled verification. Let \(G(u)=((1+u)^{7/4}+(1-u)^{7/4})/2\). Its even binomial coefficients from degree two onward are positive; after degree four their absolute values decrease. For complex \(|u|\le r=7/8\),

\[
|G(u)-1|\le \frac{21}{32}r^2+
\frac{35}{2048}\frac{r^4}{1-r^2}
=\frac{214375}{393216}<1.
\]

Therefore the analytic branch \(G^{4/7}\) with value one at zero is defined on a neighborhood of this closed disk and has modulus at most \(2\). If \(f=\sum a_{2j}u^{2j}\), the Cauchy coefficient estimate is \(|a_{2j}|\le2r^{-2j}\). After removal of the displayed terms through degree four, put \(v=(u/r)^2\le1/196\). Summing the majorant series and its two derivatives gives

\[
\begin{aligned}
|E|/|u|^6&\le 2r^{-6}/(1-v)<5,\\
|E'|/|u|^5&\le 2r^{-6}\left[6/(1-v)+2v/(1-v)^2\right]<28,\\
|E''|/|u|^4&\le 2r^{-6}\left[30/(1-v)+26v/(1-v)^2
                         +8v^2/(1-v)^3\right]<140.
\end{aligned}
\]

The inequalities at zero are interpreted by continuity. This proves (3) on the full interval. Direct expansion of (1) consequently gives

\[
\frac{\varphi}R=2h^2+\frac38ht^2+\frac{11}{256}t^4
+O(h^2t^2+|h|t^4+t^6). \tag{4}
\]

<a id="sd-star-eb"></a>
## Star inequality, strictness, and the sharp residual exponent

The quantity needed for invariance is the gradient inner product with the displacement, not the objective in (4). Exactly,

\[
D(h,t):=\langle x-\bar x,\nabla\Phi(x)\rangle
=h\varphi_h+t\varphi_t.
\]

Differentiating (1) and using (2) gives

\[
\frac DR=4h^2+\frac98hu^2+\frac34h^2u^2
+\left(\frac{11}{64}+\frac{11h}{256}\right)u^4-hE(u)-uE'(u).
\tag{5}
\]

On \(\mathcal B\), \(|u|\le1/31<1/16\), so (3) applies. Complete the first square in (5), discard the nonnegative term \(3h^2u^2/4\), and bound the remaining terms:

\[
\frac DR\ge4\left(h+\frac9{64}u^2\right)^2+
\left[\frac{95}{1024}-\frac{11}{8192}
-\frac{28+5/32}{961}\right]u^4
\ge4\left(h+\frac9{64}u^2\right)^2+\frac1{32}u^4.
\tag{6}
\]

The last rational bracket exceeds \(1/32\). Also \((33/32)^4<2\), so

\[
h^2+t^4\le2\left(h+\frac9{64}u^2\right)^2+
\left(2\left(\frac9{64}\right)^2+2\right)u^4.
\]

Comparison with (6) yields the conservative full-box bound

\[
\boxed{D(h,t)\ge\frac R{128}(h^2+t^4).} \tag{7}
\]

One can sharpen (7) to \(R(h^2+t^4)/64\) by keeping \((33/32)^4\) rather than replacing it by two: the required rational check is
\((2(9/64)^2+(33/32)^4)/64<1/32\). We use this certified sharper bound below:

\[
D(h,t)\ge\frac R{64}(h^2+t^4). \tag{8}
\]

Every ray segment from \(\bar x\) to a point of \(\mathcal B\) stays in \(\mathcal B\). Integrating (8) along that segment gives

\[
\varphi(h,t)\ge \frac R{128}h^2+\frac R{256}t^4>0
\quad\text{when }(h,t)\ne(0,0).
\]

This proves strict local minimality. A stationary point in the box has \(D=0\), so (8) proves stationarity isolation there. The Hessian eigenvalues stated in the theorem follow from (1) or from cancellation of the tangent norm Hessian against \(3R/8\).

Since \(\mathcal B\) has positive coordinates, \(F(x)=\{\nabla\Phi(x)\}\) there: this is the actual complete residual. Put \(d=\|x-\bar x\|_2=\sqrt{2(h^2+t^2)}\). Since \(|h|<1\),

\[
h^2+t^4\ge h^4+t^4\ge\tfrac12(h^2+t^2)^2=d^4/8.
\]

Consequently \(d\,r_F(x)\ge D(h,t)\ge Rd^4/512\), proving the strong exponent-\(1/3\) error bound, including \(d=0\). Every other stationary point is outside \(\mathcal B\), hence at distance greater than \(\sqrt2/32\) from \(\bar x\). For \(x\in\mathcal U\), its distance to such a point exceeds \(\sqrt2/32-1/64>1/64\ge d\), proving the asserted equality with distance to the entire \(S\).

To prove optimality, \(\varphi_{hh}(0,0)=4R>0\), and the analytic implicit function theorem gives the unique even radial critical curve near zero:

\[
\varphi_h(h_*(t),t)=0,\qquad
h_*(t)=-\frac3{32}t^2+O(t^4).
\]

Substitution into (4) gives

\[
\varphi(h_*(t),t)=\frac{13R}{512}t^4+O(t^6),\qquad
\varphi_t(h_*(t),t)=\frac{13R}{128}t^3+O(t^5).
\]

The exact gradient-coordinate transformation is
\(\|\nabla\Phi\|_2=\sqrt{\varphi_h^2+\varphi_t^2}/\sqrt2\).
Thus on this curve \(d\sim\sqrt2|t|\) whereas
\(r_F\sim13R|t|^3/(128\sqrt2)\). For any \(q>1/3\), \(d/r_F^q\) tends to infinity. The critical curve is used only to test sharpness; it is not declared invariant under PPA.

<a id="sd-complete-prox"></a>
## Complete-fiber exclusion, global proximal equality, and invariance

Let \(g(x)=\|x\|_1-\|x\|_{7/4}\). It is globally Euclidean-Lipschitz with constant
\(L_p=\sqrt2+2^{1/14}\). Every Fréchet subgradient has norm at most \(L_p\), by testing the subgradient inequality in unit directions against the Lipschitz upper bound; every limiting subgradient inherits this bound. The exact smooth-sum rule, valid including at zero, is

\[
F(y)=Qy-c+\partial_{\rm lim}g(y).
\]

This does not assert the invalid norm-gradient formula at zero. Given **any** complete resolvent output \(y\) at \(z\), choose \(w\in\partial_{\rm lim}g(y)\) with \(z-y=\lambda(Qy-c+w)\). Then

\[
(I+\lambda Q)(y-z)=\lambda(c-Qz-w),\qquad
\|y-z\|_2\le\lambda(\|Qz-c\|_2+L_p), \tag{9}
\]

because \(Q\succ0\). The elementary bounds

\[
7/5<R<3/2,\quad \sqrt2<10/7,\quad 2^{1/14}<15/14
\]

give, for \(z\in\mathcal U\),

\[
\|Qz-c\|_2+L_p
\le\sqrt2(1-R/2)+2R/64+L_p
<\frac37+\frac3{64}+\frac52<3. \tag{10}
\]

Therefore **every** complete output satisfies

\[
\|y-\bar x\|_2<1/64+3/128=5/128,
\quad |h_y|,|t_y|<5/(128\sqrt2)<1/32. \tag{11}
\]

No localization of outputs was assumed in deriving (9). In particular remote nonsmooth outputs and zero are excluded before using any smooth formula.

On the convex box \(\mathcal B\), both individual coordinates are at least \(15/16\). The usual norm Hessian formula gives

\[
0\preceq\nabla^2\|y\|_{7/4}
\preceq\tfrac34\|y\|_{7/4}^{-3/4}
\operatorname{diag}(y_i^{-1/4}).
\]

Here \(\|y\|_{7/4}\ge(15/16)R>1\) and
\((3/4)(16/15)^{1/4}<1\). Thus
\(\nabla^2\Phi(y)=Q-\nabla^2\|y\|_{7/4}\succ-I\).
The map \(y\mapsto y+\lambda\nabla\Phi(y)\) is strictly monotone on this convex box, because its Jacobian is at least \((1-\lambda)I\succ0\). All complete outputs from (11) lie in this box, so two such outputs at the same input must coincide.

For existence, \(\Phi\) is continuous and nonnegative; hence its proximal objective is continuous and coercive for every input and every positive step. A global minimizer exists, and Fermat places every global minimizer in the complete \(J_{\lambda F}\). The proved at-most-one output therefore gives exactly one complete output and exactly one global minimizer, and the two maps coincide.

Finally, write \(z=y+\lambda\nabla\Phi(y)\). By (8),

\[
\|z-\bar x\|_2^2
=\|y-\bar x\|_2^2+2\lambda D(h_y,t_y)
+\lambda^2\|\nabla\Phi(y)\|_2^2
\ge\|y-\bar x\|_2^2. \tag{12}
\]

Thus \(y\in\mathcal U\), establishing the stated invariant ball for the complete resolvent and global proximal map.

<a id="sd-actual-tail"></a>
## Actual PPA tracking and the exact slow-tail constant

Fix \(0<\lambda\le1/128\). By complete coverage, uniqueness, and (12), the trajectory starting at any \(x_0\in\mathcal U\) is defined uniquely for every integer \(k\ge0\) and stays in that ball. Summing (12) and using (8) gives

\[
\sum_{k=0}^{\infty}(h_{k+1}^2+t_{k+1}^4)<\infty.
\]

Therefore \(h_k,t_k\to0\), and \(x_k\to\bar x\). This argument uses the ordinary proximal equations, not a reduced scalar minimization algorithm.

The exact coordinate form of those equations is

\[
h_k=h_{k+1}+\frac\lambda2\varphi_h(h_{k+1},t_{k+1}),\qquad
t_k=t_{k+1}+\frac\lambda2\varphi_t(h_{k+1},t_{k+1}). \tag{13}
\]

The factor \(1/2\) comes from the Euclidean metric
\(\|x-x_k\|_2^2=2[(h-h_k)^2+(t-t_k)^2]\).
From (1)–(3), on the box,

\[
\begin{aligned}
\varphi_h/R&=4h+\tfrac38t^2+O(|h|t^2+t^4),\\
\varphi_t/R&=\tfrac34ht+\tfrac{11}{64}t^3
 +O(h^2|t|+|h||t|^3+|t|^5). \tag{14}
\end{aligned}
\]

All remainders here are analytic with uniform bounds on the box; these are local asymptotic estimates derived from the explicit certificate, not assumptions about the trajectory.

If \(t\ne0\), its exact tangent derivative is

\[
\frac{\varphi_t}{Rt}=\frac34\frac h{s}
+\frac{11}{64}\frac{t^2}{s^3}-\frac{E'(t/s)}t.
\]

By (3), \(|h|,|t|\le1/32\), and \(s\ge31/32\), the absolute value is at most

\[
\frac3{124}+\frac{11}{64\cdot32^2}(32/31)^3
+\frac{28}{32^4}(32/31)^5<\frac1{32}. \tag{15}
\]

The bound extends continuously to \(t=0\). Since \(\lambda R/64<1\), the factor in the second equation of (13),
\(1+(\lambda/2)(\varphi_t/t)\), is positive everywhere in the box. Consequently \(t_{k+1}=0\) if and only if \(t_k=0\), and nonzero tangent coordinates keep their sign. On the axis \(t=0\), (1) gives \(\varphi=2Rh^2\), so (13) gives exactly the geometric formula in the theorem.

Now suppose \(t_0\ne0\). The tangent multiplier tends to one as \(h_k,t_k\to0\), and therefore

\[
\frac{t_k}{t_{k+1}}\longrightarrow1. \tag{16}
\]

Set \(a=1+2\lambda R>1\), \(b_0=3\lambda R/16\), and \(q=1/a<1\). Introduce the analytic even function

\[
\kappa(u)=\frac{1-f(u)+u f'(u)}{u^2},\qquad \kappa(0)=3/8.
\]

The value at zero is its removable analytic extension. Exact differentiation of (1) gives
\(\varphi_h/R=4h+u^2\kappa(u)\). Thus, for the actual output with \(s_{k+1}=1+h_{k+1}\), the first equation of (13) yields the exact tracking recurrence

\[
w_{k+1}=q\left(\frac{t_k}{t_{k+1}}\right)^2w_k
-q\frac{\lambda R}{2}\frac{\kappa(t_{k+1}/s_{k+1})}{s_{k+1}^2},
\qquad w_k=\frac{h_k}{t_k^2}. \tag{17}
\]

No boundedness of \(w_k\) is presumed. By (16) and convergence to the origin, the multiplier tends to \(q<1\), and the forcing tends to \(-qb_0\). Choose any \(\theta\in(q,1)\); eventually the multiplier has absolute value below \(\theta\) and the forcing is bounded. Iterating this scalar inequality first proves \(w_k\) bounded. Subtract the fixed point \(-qb_0/(1-q)\): the new forcing tends to zero, and the same contraction then proves convergence. Hence

\[
\frac{h_k}{t_k^2}\to-\frac{qb_0}{1-q}=-\frac3{32}. \tag{18}
\]

This is the required radial-following proof. It is valid for all off-axis initial points in the certified ball; it neither assumes nor requires invariance of the radial critical curve.

Substitute (18) into the second equation of (13), using (14) at the actual output. The remainders become \(o(t_{k+1}^2)\) after division by \(t_{k+1}\), and

\[
t_k=t_{k+1}\left[1+
\frac{13\lambda R}{256}t_{k+1}^2+o(t_{k+1}^2)\right]. \tag{19}
\]

Writing \(\tau_k=|t_k|>0\), expansion of the reciprocal square gives

\[
\tau_{k+1}^{-2}-\tau_k^{-2}\longrightarrow
\frac{13\lambda R}{128}.
\]

Telescoping and taking Cesàro means yields
\(\tau_k^{-2}/k\to13\lambda R/128\), proving the tangent limit. Finally (18) implies \(h_k/t_k\to0\), and
\(\|x_k-\bar x\|_2=\sqrt2\sqrt{h_k^2+t_k^2}\sim\sqrt2\tau_k\).
This proves the stated exact distance limit.


<a id="sd-critical-not-invariant"></a>
## The critical curve is not a PPA invariant curve

For small t>0 the radial critical curve has h_*'(t)=−3t/16+O(t^3)<0, while varphi_t(h_*(t),t)=13R t^3/128+O(t^5)>0. If both a positive-t input and its complete-PPA output lay on this curve, the radial equation would force their h coordinates equal, whereas the tangent equation and sign preservation force t_input>t_output>0. Strict monotonicity of h_* on this interval makes those statements inconsistent. The negative-t case is symmetric. Thus sufficiently small nonzero points of the critical curve leave it under the actual proximal update. Radial following in (18) preserves only the leading profile, not exact curve invariance.

Equivalently, for a curve output with tangent t, its actual inverse-proximal input has the same h and tangent t+13lambda R t^3/256+O(t^5). Its difference from the critical h at that input tangent is

\[
h_*(t+13\lambda R t^3/256+O(t^5))-h_*(t)
=-39\lambda R t^4/4096+O(t^6)\ne0.
\]

This gives an exact leading-order obstruction and explains why reduction to the critical curve would have been an invalid algorithmic proof.

<a id="sd-kl"></a>
## Sharp classical KL exponent and its order bounds (C230-v1)

For the same fixed instance, there are a smaller neighborhood \(N\) of \(\bar x\) and \(c_*>0\) such that, with \(e(x)=\Phi(x)-\Phi(\bar x)\),

\[
r_F(x)\ge c_* e(x)^{3/4}\quad(x\in N).
\tag{K1}
\]

The exponent \(3/4\) is sharp: for each \(\theta<3/4\), every positive proposed constant fails arbitrarily close to \(\bar x\). These constants are local existence constants, not new explicit bounds on the whole certified box \(\mathcal B\).

Here is a self-contained proof, without importing a KL convergence theorem. Let \(H(t)=h_*(t)\), \(K=13R/512\), and \(V(t)=\varphi(H(t),t)=Kt^4+O(t^6)\). With \(d=h-H(t)\), Taylor integration gives the exact analytic splitting

\[
\varphi(H(t)+d,t)=V(t)+a(d,t)d^2,\qquad
a(d,t)=\int_0^1(1-s)\varphi_{hh}(H(t)+sd,t)\,ds,\quad a(0,0)=2R>0.
\tag{K2}
\]

The coordinate change \(v=d\sqrt{a(d,t)}\), with \(t\) unchanged, is an analytic local diffeomorphism. After shrinking \(N\), both its Jacobian and inverse Jacobian are bounded and \(a\) is bounded above and below by positive constants. The objective is exactly \(v^2+V(t)\). Since \(V'(t)=4Kt^3+O(t^5)\), the true residual is comparable to \(|v|+|t|^3\) and the energy to \(v^2+t^4\). For \(|v|\le1\),

\[
e(x)^{3/4}\le C(|v|^{3/2}+|t|^3)
\le C(|v|+|t|^3)\le C' r_F(x).
\tag{K3}
\]

All original coordinates are positive here, so this gradient calculation is for the original limiting-subdifferential residual. On \(d=0\), the energy is asymptotic to \(Kt^4\) and the residual to \(4K|t|^3/\sqrt2\). Thus \(r_F/e^\theta\to0\) if \(\theta<3/4\). The usual desingularizing function for (K1) is \((4/c_*)s^{1/4}\).

For any fixed \(0<\lambda\le1/128\) and any \(x_0\in\mathcal U\), the already proved complete PPA converges to \(\bar x\), hence eventually enters \(N\). Independent global-proximal equality gives the descent estimate

\[
e_k-e_{k+1}\ge\frac{\|x_k-x_{k+1}\|^2}{2\lambda}
=\frac{\lambda}{2}r_F(x_{k+1})^2
\ge a_\lambda e_{k+1}^{3/2},\qquad a_\lambda=\lambda c_*^2/2>0.
\tag{K4}
\]

This implies \(e_k=O(k^{-2})\) by an elementary comparison: reindex at entry to \(N\), choose \(B\ge\max\{e_0,36/a_\lambda^2\}\), and set \(s_n=B/(n+1)^2\). The increasing map \(T(s)=s+a_\lambda s^{3/2}\) satisfies \(T(s_{n+1})\ge s_n\), because

\[
a_\lambda\sqrt B\ge6\ge
\frac{(2n+3)(n+2)}{(n+1)^2}.
\]

Induction using \(T(e_{n+1})\le e_n\) proves \(e_n\le s_n\). The local energy comparison and \(H(t)=O(t^2)\) also give \(\|x-\bar x\|\le C e(x)^{1/4}\); therefore \(\|x_k-\bar x\|=O(k^{-1/2})\).

This explicitly confirms that classic KL tools apply. For example, the actual complete-global-proximal sequence satisfies the sufficient-decrease and relative-error conditions of Attouch–Bolte–Svaiter, author report dated 15 December 2010, p.8 (H1–H3), Theorem 2.9 p.12: take \(a=1/(2\lambda)\), \(w_{k+1}=(x_k-x_{k+1})/\lambda\in F(x_{k+1})\), \(b=1/\lambda\); compactness and continuity give H3. The KL condition holds at its already identified limit. This classical comparison is not needed for the self-contained order proof above. It supplies no exact slow-tail constant and does not exclude remote complete outputs. Those assertions remain the separate full-fiber and actual two-variable arguments. See the [primary-source comparison](../../audit/SPARSE_PRIORITY_AUDIT_2026_10_09.md#final-submission-source-check).

<a id="sd-evidence"></a>
## Evidence and scope

- [Reproducible exact arithmetic and numerical trajectories](../../code/sparse_regularity/sharp_dynamics_verify.py) and [recorded output](../../code/sparse_regularity/sharp_dynamics_results.json) check the rational majorants, coefficients, the two-dimensional implicit equations, radial tracking, and the slow versus radial distinction. Run `python3 research/code/sparse_regularity/sharp_dynamics_verify.py` from the repository root; only Python's standard library is used, there is no random seed, and the script records the Python version and its exact parameters. The checked run passed all exact Fraction inequalities, three genuine 100,000-step two-variable float trajectories, independent 50/80-digit Decimal repetitions, and the geometric-axis formula. The finite raw distances scaled by the square root of the iteration count remain far from the proved limit at this conservative small step; the record expressly reports that long transient. The post-transient reciprocal-square slope agrees with its proved limit to about five parts in 100,000. The complete-fiber and global-minimizer identification are carried by the analytic proof above.
- [Independent complete-dynamics reception](../../audit/SPARSE_COMPLETE_DYNAMICS_REVIEW_2026_10_09.md) reconstructs the full-output exclusion, exact Cauchy/star gates, proximal existence/uniqueness, actual radial tracking, exceptional axis, and tail normalization. A [second threshold and cross-proof reception](../../audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md#sr-cross-dynamics) independently recomputes the same quantitative and tracking steps. The sole reported correction was a mathematical-rendering typo in the symbol `\epsilon_k`, which has been fixed. These are internal mathematical receptions, not external peer review or published-priority certification.
- No external convergence or center-manifold theorem is imported. The full-output displacement bound uses the original globally defined limiting subdifferential, and existence is obtained from the global proximal subproblem separately from uniqueness.
- This example does not prove that all stationary points are minima, that arbitrary initial points enter this local ball, that a matching quartic tail holds for every \(3/2<p<2\) example, or that the certified ball and step bound are optimal.
