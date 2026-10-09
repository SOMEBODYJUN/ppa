# 非线性 GPPA 的核坐标定理：完整残差、一般模、能量与物理提升

**Status:** `derived-checked` within the independently reconstructed and read scope recorded in [the reception audit](../../audit/GPPA_MODULUS_RECEPTION_2026_10_09.md). Global originality remains unchecked. Every mathematical claim below is proved from the displayed data; no source theorem supplies a missing existence or lifting hypothesis. The comparison concerns Le–Mordukhovich–Théra, arXiv:2608.01584v1, the archived [PDF](sources/gppa_2608.01584v1.pdf), SHA-256 `5f07147a258e441193dd918452909ddc2fec8781257d6005348f233016653e91`. The source was read directly, especially Definitions 1–6 (pp.4–6), Theorem 1 (p.6), Theorem 2 and its proof (pp.7–8), and Theorem 4 (pp.9–11). This file proves an exact-coordinate extension, not a claim of global novelty or dominance over every choice of kernel, subrelation or lift.

The main result has three independent scalar estimates. Keeping the residual square is essential: a direct compatibility test alone would omit source Theorem 2 when its adaptive constant is small. An optional dissipation estimate retains the source's useful quadratic geometry. A separate shell argument covers weak nonlinear error bounds even when no uniform geometric contraction is certified.

<a id="ngk-object"></a>
## NGK-1 · Full relation, graph block, and noninjective kernels

Let \(H\) be a real Hilbert space, \(F:H\rightrightarrows H\) any relation, \(v:H\to H\) any everywhere-defined mapping, and \(\lambda>0\). No continuity or injectivity of \(v\) is imposed here. Put

\[
S=F^{-1}(0),\qquad Q=\operatorname{ran}v,
\]
\[
A(z)=\bigcup_{x:v(x)=z}F(x),\qquad
r_A(z)=\inf_{f\in A(z)}\|f\|.
\tag{NGK1}
\]

An empty fiber has residual \(+\infty\). The full kernel-coordinate relation \(A\) is different from \(F\); in particular

\[
\operatorname{zer}A=v(S),\qquad r_A(v(x))\le r_F(x),
\quad r_F(x)=\inf_{f\in F(x)}\|f\|.
\tag{NGK2}
\]

The first equality follows in both directions directly from the union in (NGK1). The inequality need not be equality: another physical point with the same kernel coordinate may have a smaller graph value. Neither closedness of \(S\) nor continuity of \(v\) automatically makes \(v(S)\) closed.

For a physical graph block \(\mathcal G\subset\operatorname{gph}F\), define its exact image

\[
\Gamma=\{(v(x),f):(x,f)\in\mathcal G\}\subset\operatorname{gph}A.
\tag{NGK3}
\]

The block GPPA transition is

\[
(x^+,f)\in\mathcal G,\qquad v(x)=v(x^+)+\lambda f.
\tag{NGK4}
\]

Writing \(z=v(x)\), \(z^+=v(x^+)\), this is exactly a PPA step
\(z=z^++\lambda f\) on \(\Gamma\). Conversely, every such kernel step has a physical representative \((x^+,f)\in\mathcal G\) by the definition of \(\Gamma\), and that representative is a legal GPPA output for **any** preceding physical point with kernel coordinate \(z\). For the full graph \(\mathcal G=\operatorname{gph}F\), \(\Gamma=\operatorname{gph}A\) and this is the full warped-resolvent algorithm, with no deleted fiber.

The physical equivalence relation \(x\sim y\iff v(x)=v(y)\) has an exact metric identification with \(Q\), using \(d_v([x],[y])=\|v(x)-v(y)\|\). This is only a coordinate/metric quotient. No claim about its quotient topology or completeness follows. Our argument works in the ambient complete space \(H\); \(Q\) itself need not be open, closed or complete.

<a id="ngk-data"></a>
## NGK-2 · Exact local data

Fix a nonempty **closed** set \(Z\subset\operatorname{zer}A\), an open set \(U\subset H\), and \(R>0\). For the complete-zero-set version explicitly assume \(Z=v(S)\) is closed. Define

\[
E=\{z\in Q\cap U:d(z,Z)<R\},\qquad D_U(z)=d(z,H\setminus U).
\tag{NGK5}
\]

The distance to the empty set is \(+\infty\). All the following data refer to the **same** \(F,v,\mathcal G,\Gamma,\lambda,Z,U,R\).

1. **Coverage and zero anchors.** For every \(z\in E\), there is \((y,f)\in\Gamma\) with \(z=y+\lambda f\). For every \(p\in Z\), \((p,0)\in\Gamma\). Coverage is required only on \(Q\cap U\), not on all of \(H\). For the full graph, source coverage \(Q\subset\operatorname{ran}(v+\lambda F)\) supplies this condition.
2. **Kernel all-pairs RL.** A continuous nondecreasing \(\omega:[0,R]\to[0,\infty)\), with \(\omega(0)=0\), satisfies, for every two points \((y,f),(y',f')\in\Gamma\) whose kernel-input distance \(\delta=\|(y+\lambda f)-(y'+\lambda f')\|\le R\),
   \[
   \|(y-\lambda f)-(y'-\lambda f')\|\le\omega(\delta).
   \tag{NGK6}
   \]
3. **True kernel residual EB and evaluation window.** Let \(\bar t>0\), and let \(\psi:[0,\bar t]\to[0,\infty)\) be continuous and strictly increasing with \(\psi(0)=0\). On all actual outputs \(y\) of covered inputs \(z\in E\), whenever \(r_A(y)\le\bar t\), require
   \[
   d(y,Z)\le\psi(r_A(y)),\qquad
   B(R)/\lambda\le\bar t,\qquad
   B(t)=\frac{t+\omega(t)}2.
   \tag{NGK7}
   \]
   This is an EB for the full union \(A\), even if the algorithm uses a block \(\Gamma\). No residual minimum is assumed to be attained. Define \(M=\psi(\bar t)\) and \(g=\psi^{-1}:[0,M]\to[0,\bar t]\).
4. **Optional zero-anchor dissipation.** This extra condition may be omitted. If it is used, take a continuous nondecreasing \(a:[0,M]\to[0,\infty)\), \(a(0)=0\), and require for each actual output \((y,f)\) and every \(p\in Z\),
   \[
   \langle f,y-p\rangle\ge a(d(y,Z)).
   \tag{NGK8}
   \]
   Pair monotonicity supplies \(a=0\). Adaptive strong monotonicity with constant \(\varepsilon\) supplies \(a(t)=\varepsilon t^2\). The all-pairs condition (NGK6) can alternatively be replaced by its displayed comparison with **every zero anchor** for the convergence estimates below; all-pairs is needed for the uniqueness/continuity assertions.

The output EB is not required outside the residual window. Condition (NGK7) will certify every actual use of it. Strict monotonicity/continuity of \(\psi\) are only used for the inverse-energy branch. With merely nondecreasing, origin-continuous \(\psi\), the direct branch and its summable scalar-envelope theorem remain valid. Equivalently one can provide a continuous nondecreasing lower residual profile \(g\), positive at positive distances, with \(r_A(y)\ge g(d(y,Z))\), and use \(t^2+\lambda^2g(t)^2\) below without requiring an inverse gauge.

<a id="ngk-one-step"></a>
## NGK-3 · One-step estimates, uniqueness, and zero behavior

Under NGK-2, for an actual step from \(z\in E\), write

\[
d=d(z,Z),\qquad d^+=d(z^+,Z),\qquad s=\|z-z^+\|=\lambda\|f\|,
\quad C_\omega(t)=\frac{t^2+\omega(t)^2}{2}.
\]

Then

\[
(d^+)^2+s^2\le C_\omega(d),\qquad
s\le B(d),\qquad d^+\le B(d),
\tag{NGK9}
\]
\[
r_A(z^+)\le s/\lambda\le B(d)/\lambda\le\bar t,
\quad d^+\le\psi(s/\lambda)\le\psi(B(d)/\lambda),
\quad s\ge\lambda g(d^+).
\tag{NGK10}
\]

The optional condition (NGK8) also gives

\[
(d^+)^2+s^2+2\lambda a(d^+)\le d^2,
\quad s\le d.
\tag{NGK11}
\]

**Proof without nearest-point attainment.** Choose \(p_n\in Z\) with \(\|z-p_n\|\to d\). Since \(d<R\), the anchors can be chosen with \(\|z-p_n\|<R\). Put \(b=z-z^+=\lambda f\), \(h_n=z^+-p_n\). Comparison in (NGK6) with \((p_n,0)\) gives
\(\|h_n-b\|\le\omega(\|z-p_n\|)\), while \(h_n+b=z-p_n\). The parallelogram identity gives

\[
\|h_n\|^2+s^2\le\frac{\|z-p_n\|^2+\omega(\|z-p_n\|)^2}{2}.
\]

Both \(2b=(h_n+b)-(h_n-b)\) and \(2h_n=(h_n+b)+(h_n-b)\) have norm at most \(\|z-p_n\|+\omega(\|z-p_n\|)\). Use \(d^+\le\|h_n\|\), and pass to the limit by continuity of \(\omega\), proving (NGK9). The selected value belongs to the full \(A(z^+)\), so the residual chain in (NGK10) is valid; it both opens the EB window and keeps every gauge evaluation in its domain. From \(d^+\le\psi(s/\lambda)\), apply the increasing inverse to get its last inequality. If (NGK8) is available, polarization yields

\[
\|z-p_n\|^2=\|h_n\|^2+s^2+2\lambda\langle f,h_n\rangle
\ge(d^+)^2+s^2+2\lambda a(d^+),
\]

and the same limit proves (NGK11). These arguments work in arbitrary Hilbert spaces; closed nonconvex \(Z\) need not admit nearest points.

At \(d=0\), closedness of \(Z\) gives \(z\in Z\); comparison with the exact anchor \((z,0)\) in (NGK6) forces \(s=0\), \(z^+=z\), and \(f=0\). Thus kernel coordinates are absorbed at zero. Physical output points can still move inside the solution fiber \(S\cap v^{-1}(z)\).

For any two kernel outputs at the same kernel input, (NGK6) at \(\delta=0\), together with equality of inputs, forces both their kernel coordinates and their selected values to agree. Thus the kernel resolvent on \(\Gamma\) is single-valued; the physical warped resolvent can remain multivalued. For covered inputs at distance \(\delta\le R\), the same parallelogram argument gives

\[
\|Tz-Tz'\|^2+\|(z-Tz)-(z'-Tz')\|^2
\le C_\omega(\delta),
\tag{NGK12}
\]

so \(T\) is continuous in the relative domain \(E\), with modulus \(\sqrt{C_\omega}\). This supplies no extra coverage.

<a id="ngk-recurrence"></a>
## NGK-4 · Three scalar branches and the exact recurrence

On \([0,M]\), define continuous strictly increasing functions

\[
V(t)=t^2+\lambda^2g(t)^2,
\qquad W(t)=V(t)+2\lambda a(t)
\tag{NGK13}
\]

where \(W\) is used only when (NGK8) is imposed. The strict increase follows from the \(t^2\) term. For either \(J=V,W\), define its capped inverse

\[
J^{[-1]}(u)=
\begin{cases}J^{-1}(u),&0\le u\le J(M),\\M,&u>J(M).\end{cases}
\tag{NGK14}
\]

The cap is legitimate because (NGK10) already proves \(d^+\le M\); it does not silently extend an inverse past its domain. Define

\[
\tau_D(t)=\psi(B(t)/\lambda),\qquad
\tau_E(t)=V^{[-1]}(C_\omega(t)),
\quad\tau_A(t)=W^{[-1]}(t^2),
\tag{NGK15}
\]
\[
\tau(t)=\min\{\tau_D(t),\tau_E(t)\}
\quad\hbox{or}\quad
\tau(t)=\min\{\tau_D(t),\tau_E(t),\tau_A(t)\}
\tag{NGK16}
\]

according to whether the optional anchor branch is available. Every actual step satisfies

\[
V(d^+)\le C_\omega(d),\qquad
W(d^+)\le d^2\quad\hbox{when available},\qquad
d^+\le\tau(d).
\tag{NGK17}
\]

Indeed, substitute \(s\ge\lambda g(d^+)\) into (NGK9) and (NGK11); the direct estimate is (NGK10). The finite continuous \(\tau\) is nondecreasing and \(\tau(0)=0\). We do **not** suppose that arbitrary gauges automatically give contraction. Require the same-window scalar condition

\[
\tau(t)<t\quad(0<t\le R).
\tag{NGK18}
\]

If a uniform factor is desired, require \(\tau(t)\le\kappa t\) for some \(0<\kappa<1\). For \(t>0\), the sequence \(t_{j+1}=\tau(t_j)\) is strictly decreasing until it hits zero; continuity and (NGK18) show \(t_j\to0\). Failure of (NGK18) only means that these scalar upper bounds do not certify contraction.

<a id="ngk-length"></a>
## NGK-5 · Finite length and local retention from the exact scalar envelope

Assume (NGK18). Let

\[
\mathcal H_\tau(r)=\sum_{j=0}^{\infty} B(\tau^j(r)),\qquad 0\le r\le R.
\tag{NGK19}
\]

If the optional anchor branch is imposed, one may replace \(B(t)\) everywhere in this section by the smaller \(\min\{B(t),t\}\). Fix \(x_0\in H\) such that \(z_0=v(x_0)\in E\), and write \(d_0=d(z_0,Z)\). Require

\[
\mathcal H_\tau(d_0)<\infty,
\qquad \mathcal H_\tau(d_0)<D_U(z_0).
\tag{NGK20}
\]

Then every physical block-GPPA choice can be continued indefinitely. Its kernel coordinates are the same unique sequence and satisfy

\[
d(z_k,Z)\le\tau^k(d_0),\qquad
\sum_{k\ge0}\|z_{k+1}-z_k\|\le\mathcal H_\tau(d_0),
\tag{NGK21}
\]
\[
z_k\to z_\infty\in Z\cap U,\qquad
\|z_k-z_\infty\|\le\mathcal H_\tau(d(z_k,Z))
\le\mathcal H_\tau(\tau^k(d_0)).
\tag{NGK22}
\]

**Proof.** At each valid step NGK-3 and NGK-4 give the distance and step estimates. Monotonicity of \(\tau,B\) gives the bounds by induction. Every constructed finite prefix stays within distance \(\mathcal H_\tau(d_0)<D_U(z_0)\) of \(z_0\), and its distance to \(Z\) stays below \(R\). Its output belongs to \(Q\) by construction, so it lies in \(E\) and coverage can be invoked again. This proves existence without assuming in advance that the sequence remains in the window. Summable steps make \((z_k)\) Cauchy in \(H\), not in an assumed-complete \(Q\). The distance tends to zero; closed \(Z\) places the ambient limit in \(Z\subset Q\). The strict budget also keeps the limit in \(U\). Summing from an arbitrary index gives (NGK22). Since \(\mathcal H_\tau(\tau^k(d_0))\) is the tail of the convergent scalar series, it tends to zero. The physical choices need not be the same, although their kernel coordinates and selected values are. □

Two usable sufficient certificates for (NGK19) are:

* **Geometric distance plus Dini.** If \(\tau(t)\le\kappa t\), and
  \(\int_0^R\omega(t)\,dt/t<\infty\), then
  \[
  \mathcal H_\tau(r)\le\frac12\sum_{j\ge0}\{\kappa^jr+\omega(\kappa^jr)\}<\infty.
  \tag{NGK23}
  \]
  For a nondecreasing \(\omega\), its integral on \([\kappa^{j+1}r,\kappa^jr]\) is between \(\log(1/\kappa)\omega(\kappa^{j+1}r)\) and \(\log(1/\kappa)\omega(\kappa^jr)\), proving the geometric-sampling/Dini equivalence without concavity. This is the exact kernel-coordinate analogue of [GM1–18](../../canonical/general_modulus_dynamics.md#gm-data).
* **Geometric energy.** In this certificate additionally assume \(R\le M\), so \(V\) is defined on every input distance used. If \(C_\omega(t)\le qV(t)\) for all \(0<t<R\), with \(0<q<1\), then
  \[
  V(d_{k+1})\le qV(d_k),\qquad
  s_k^2\le C_\omega(d_k)\le q^{k+1}V(d_0).
  \tag{NGK24}
  \]
  Consequently the kernel-length budget is
  \(\sqrt{qV(d_0)}/(1-\sqrt q)\), and its tail after index \(k\) is at most
  \(q^{k/2}\sqrt{qV(d_0)}/(1-\sqrt q)\). The same retention induction applies with this budget. This certificate does not require a Dini modulus. It can be used instead of (NGK19). The later scalar argument [C221 TL10–11](../../canonical/gppa_tail_lyapunov_bridge.md#gtl-energy) proves that this same gate also makes the \(B\circ\tau^j\) series converge: \(B^2\le C_\omega\le qV\) and the inactive inverse cap give geometric decay of scalar \(V(\tau^j(d_0))\). This follows from the scalar data, not from already-known orbit length.

For \(\omega(t)=Lt^\gamma\), \(0<\gamma\le1\), the Dini condition is automatic. For arbitrary nonlinear \(\omega\), summability is an explicit additional gate; positivity and vanishing at zero alone do not supply it.

<a id="ngk-shell"></a>
## NGK-6 · Pair-monotone shell certificate beyond linear EB

Suppose \(\Gamma\) is pair-monotone in the kernel coordinates. This supplies (NGK6) with \(\omega(t)=t\). Conversely, that cutoff condition is equivalent to pair monotonicity only on the pairs tested within its input-distance window, because

\[
\|\Delta y+\lambda\Delta f\|^2-
\|\Delta y-\lambda\Delta f\|^2
=4\lambda\langle\Delta f,\Delta y\rangle.
\tag{NGK25}
\]

Assume coverage, closed \(Z\), zero anchors and the true EB from NGK-2. For this certificate additionally require \(d_0\le M\), so every inverse-gauge evaluation below is in its domain. Put \(r_j=2^{-j}d_0\), for \(d_0>0\). Define

\[
\mathcal L_{\rm sh}(d_0)=
\sum_{j\ge0}\left(r_j+\frac{r_j^2}{\lambda g(r_j/2)}\right).
\tag{NGK26}
\]

If this quantity is finite and smaller than \(D_U(z_0)\), then every block-GPPA choice is globally constructible in the local window, and its kernel sequence has total length at most \(\mathcal L_{\rm sh}(d_0)\) and converges to \(Z\cap U\). This can apply when no uniform \(\kappa<1\) exists and when the naive sum of distance bounds is divergent.

**Proof.** Pair monotonicity gives (NGK11) with \(a=0\):

\[
d_k^2-d_{k+1}^2\ge s_k^2,\qquad
s_k\ge\lambda g(d_{k+1}),\qquad s_k\le d_k.
\tag{NGK27}
\]

Assign every index with \(d_k>0\) to the unique shell \(r_j/2<d_k\le r_j\). Since \(d_k\) is nonincreasing, the indices in one shell form a consecutive block, possibly empty. Among its steps, all but at most one have \(d_{k+1}>r_j/2\). For these interior steps, \(s_k\ge\lambda g(r_j/2)\), hence

\[
\sum_{\rm interior}s_k
\le\frac{\sum_{\rm interior}s_k^2}{\lambda g(r_j/2)}
\le\frac{r_j^2}{\lambda g(r_j/2)}.
\tag{NGK28}
\]

The last inequality follows by telescoping (NGK27) over the shell's consecutive indices. The at-most-one crossing step has length \(s_k\le d_k\le r_j\). If it skips several smaller shells, it is counted just once, in its starting shell; no skipped shell acquires an extra crossing charge. Thus every finite valid prefix has length bounded by (NGK26). The strict initial budget proves retention and indefinite continuation exactly as in NGK-5.

Along the resulting infinite sequence \(d_k\) tends to a limit \(\ell\ge0\). If \(\ell>0\), (NGK27) would give \(s_k\ge\lambda g(\ell)>0\) indefinitely, contradicting \(\sum s_k^2\le d_0^2\). Therefore \(d_k\to0\). The finite shell sum gives Cauchy convergence in \(H\), and closed \(Z\) and the strict budget place the limit in \(Z\cap U\). At \(d_k=0\), kernel absorption was already proved. □

For \(\psi(s)=Ks^q\), the shell term is

\[
\frac{r_j^2}{\lambda g(r_j/2)}
=\frac{(2K)^{1/q}}\lambda r_j^{\,2-1/q}.
\tag{NGK29}
\]

Thus \(q>1/2\) is a sufficient finite-length condition for this certificate. No necessity claim is made at \(q\le1/2\). A proof failure at this scalar threshold does not prove that a particular GPPA trajectory has infinite length.

<a id="ngk-source-inclusion"></a>
## NGK-7 · Exact inclusion of source Theorem 2 and its rates

The source's complete assumptions are: \(S=\operatorname{zer}F\ne\varnothing\); for **all** physical graph-point pairs,

\[
\langle f-f',v(x)-v(x')\rangle
\ge\varepsilon\|v(x)-v(x')\|^2,
\quad\varepsilon>0;
\tag{NGK30}
\]

and \(Q\subset\operatorname{ran}(v+\lambda F)\). Source part (b) additionally assumes \(F^{-1}\) is R-Lipschitz at zero; this is a local set inclusion for all graph values near zero, with a positive residual radius. Its printed part (a) has kernel-distance factor \((1+2\lambda\varepsilon)^{-1/2}\), and part (b) concerns the **physical distance to the zero set**, not physical point convergence.

Take the full \(\mathcal G=\operatorname{gph}F\). Then (NGK30) passes exactly to all pairs in \(\operatorname{gph}A\). Applying it to two physical zeros shows that all their kernel coordinates agree. Hence

\[
Z=v(S)=\{z_*\}
\tag{NGK31}
\]

is nonempty and closed even for a discontinuous or noninjective kernel. All required zero anchors and the \(Q\)-coverage hold. The transformed relation is monotone, so \(\omega(t)=t\) is valid. Comparing any \((z,f)\in\operatorname{gph}A\) with \((z_*,0)\) gives

\[
\varepsilon\|z-z_*\|^2
\le\langle f,z-z_*\rangle
\le\|f\|\|z-z_*\|.
\]

Therefore \(\|z-z_*\|\le\|f\|/\varepsilon\) for **every** full graph value. Taking the infimum is valid here because the gauge is linear; it gives the true kernel EB

\[
d(z,Z)\le r_A(z)/\varepsilon.
\tag{NGK32}
\]

For any chosen \(R>d_0\), take \(\bar t\ge\max\{R/\lambda,\varepsilon R\}\); the linear EB is global, so this is allowed and gives \(M\ge R\). It follows that \(\psi(s)=s/\varepsilon\), \(g(t)=\varepsilon t\), \(B(t)=t\), and

\[
V(t)=(1+\lambda^2\varepsilon^2)t^2,
\qquad \tau_E(t)=\frac{t}{\sqrt{1+\lambda^2\varepsilon^2}}<t.
\tag{NGK33}
\]

Thus the RL+true-EB energy branch contains **every** source Theorem 2(a) instance, for every positive \(\lambda\varepsilon\). The direct branch alone would give \(\tau_D(t)=t/(\lambda\varepsilon)\) and require \(\lambda\varepsilon>1\), so it cannot justify an inclusion claim.

The source's positive anchor geometry also yields \(a(t)=\varepsilon t^2\), giving

\[
W(t)=(1+\lambda\varepsilon)^2t^2,
\qquad \tau_A(t)=\frac{t}{1+\lambda\varepsilon}.
\tag{NGK34}
\]

Consequently \(\|z_k-z_*\|\le(1+\lambda\varepsilon)^{-k}\|z_0-z_*\|\). This slightly stronger scalar bound is an elementary consequence of the same source hypotheses, not a separate novelty claim. Directly, \(\langle z_k-z_*,z_{k+1}-z_*\rangle\ge(1+\lambda\varepsilon)\|z_{k+1}-z_*\|^2\), and Cauchy–Schwarz proves it. The source's printed rate also follows from (NGK11) after discarding the residual square. Either geometric kernel-point rate already implies kernel finite length; it must not be advertised as an independent missing innovation.

If source part (b)'s R-Lipschitz condition holds with modulus \(L\) on a residual ball, the selected value \(f_{k+1}=(z_k-z_{k+1})/\lambda\) eventually lies in that ball, and

\[
d(x_{k+1},S)\le L\|f_{k+1}\|=Ls_k/\lambda.
\tag{NGK35}
\]

This gives the same physical set-distance conclusion and its geometric rate. More generally a physical R-continuity gauge \(\rho\) gives \(d(x_{k+1},S)\le\rho(s_k/\lambda)\) eventually within its stated local residual ball (at every step only for a global bound); a nonlinear \(\rho\) does not in general preserve a geometric rate, although it does preserve distance convergence. No physical point convergence follows from (NGK35) alone.

<a id="ngk-physical"></a>
## NGK-8 · Physical lifting and the fibers that remain uncontrolled

For all admissible physical transitions in the relevant window, suppose independently that

\[
\|x^+-x\|\le\sigma(\|v(x^+)-v(x)\|),
\qquad \sigma(0)=0,
\tag{NGK36}
\]

where \(\sigma\) is finite and nondecreasing. This may come from an inverse modulus of \(v\) on the selected physical set, or from a separately proved physical step estimate. It is not implied by pair monotonicity, ASM, kernel coverage or physical EB.

Under the scalar-envelope certificate of NGK-5, require

\[
\sum_{k\ge0}\sigma(B(\tau^k(d_0)))<\infty.
\tag{NGK37}
\]

Then the physical sequence has finite length and is Cauchy in \(H\). For the geometric-energy alternative, a sufficient condition is \(\sum_k\sigma(q^{k/2}\sqrt{qV(d_0)})<\infty\). For the shell alternative a Lipschitz bound \(\sigma(t)\le Ct\) suffices. If \(\tau(t)\le\kappa t\), Dini integrability of the nondecreasing composite \(\sigma\circ B\) suffices for (NGK37). Merely continuous inverse lifting is insufficient: a continuous modulus can be non-Dini. A Hölder inverse bound \(\sigma(t)=Ct^\beta\) is sufficient under geometric \(s_k\), for every \(\beta>0\).

To place the physical Cauchy limit \(x_\infty\) in the original zero set, add either:

* the norm–norm closed-graph implication \(x_k\to x,\ f_k\to0,\ f_k\in F(x_k)\Rightarrow0\in F(x)\); or
* a closed physical target \(S\) and a same-output bound \(d(x_{k+1},S)\le\rho(s_k/\lambda)\) with \(\rho(t)\to0\) as \(t\downarrow0\).

These conditions supply the final zero-set identity. Continuity of \(v\) at \(x_\infty\), or a closed graph of \(v\) along the sequence, additionally gives \(v(x_\infty)=z_\infty\). This last coordinate identity is not needed for physical membership in \(S\) when a zero-graph closure condition is already available.

The distinction is unavoidable. On \(H=\mathbb R^2\), let \(F(t,y)=\{(t,0)\}\) and \(v(t,y)=(t,0)\), with \(\lambda=1\). The pair is 1-ASM, \(Q\)-coverage holds, \(S=\{0\}\times\mathbb R\), and \(F^{-1}\) is globally R-Lipschitz at zero with modulus 1. Every step forces only \(t_{k+1}=t_k/2\); its \(y\)-coordinate is free. The valid sequence \(x_k=(2^{-k},(-1)^k)\) has a geometrically convergent kernel and geometrically vanishing physical distance to \(S\), but has no physical point limit and has infinite physical length. At zero kernel coordinate, arbitrary movement among points of \(S\) is also allowed. This is exactly the missing fiber direction that (NGK36) must control.

<a id="ngk-eb-bridge"></a>
## NGK-9 · An honest bridge from the original true residual EB

A true EB for \(F\) is not automatically the same EB for \(A\). One useful sufficient bridge is the following. Suppose that for **every** physical full graph point \((x,f)\) with \(\|f\|\le\bar t\),

\[
d(x,S)\le\rho(\|f\|),\qquad
d(v(x),Z)\le\eta(d(x,S)),
\tag{NGK38}
\]

where \(\rho,\eta\) are nondecreasing and the composite \(\eta\circ\rho\) is right-continuous at every residual value being minimized. Then

\[
d(z,Z)\le (\eta\circ\rho)(r_A(z))
\tag{NGK39}
\]

for \(r_A(z)<\bar t\). Indeed, take a sequence \(f_n\in A(z)\) with norms tending down to \(r_A(z)\), choose physical representatives \(x_n\) with \(v(x_n)=z\), and use (NGK38) on each. Right continuity lets the upper bounds pass to the residual infimum. At the upper endpoint \(r_A(z)=\bar t\), one additionally needs residual attainment, a bound on graph values just above \(\bar t\), or the EB itself at that endpoint. The full-fiber quantifier is essential: a bound only on selected/allowed physical values cannot be minimized over \(A(z)\).

A complete physical true EB \(d(x,S)\le\rho(r_F(x))\), together with evaluation of \(\rho\) on selected graph norms, supplies the first estimate in (NGK38) by monotonicity. If \(v\) is \(L_v\)-Lipschitz and \(v(S)\subset Z\), then \(\eta(t)=L_vt\) supplies the second estimate by approximate nearest physical zero points. This bridge changes the gauge to \(L_v\rho\); it does not identify the two true residuals. Residual nonattainment and positive-point jumps cannot be suppressed; compare [C166](../../canonical/operator_profile_tools.md#op-nonattainment).

<a id="ngk-strict-witness"></a>
## NGK-10 · A strict fixed-kernel inclusion witness, and its exact limitation

For \(1<p<2\), take the full scalar relation and the fixed identity kernel

\[
H=\mathbb R,\qquad F(x)=\{\operatorname{sgn}(x)|x|^p\},\qquad v(x)=x.
\tag{NGK40}
\]

The full graph is monotone; hence \(\omega(t)=t\) is a global kernel RL certificate. Its zero set is \(Z=S=\{0\}\), its true residual is \(r_A(x)=|x|^p\), and its exact EB is \(\psi(s)=s^{1/p}\). For every \(\lambda>0\), the scalar function \(x\mapsto x+\lambda\operatorname{sgn}(x)|x|^p\) is continuous strictly increasing and onto \(\mathbb R\), so full coverage and a unique physical output hold. The shell certificate applies because \(q=1/p>1/2\). Here physical lifting is the identity, so it gives finite physical length and convergence for every initial value.

No \(\varepsilon>0\) can make this **same** pair \((F,\mathrm{Id})\) adaptively strongly monotone on any neighborhood of zero: comparison of \(x>0\) with zero would require \(x^{p+1}\ge\varepsilon x^2\), that is \(x^{p-1}\ge\varepsilon\), which fails as \(x\downarrow0\). The physical inverse EB is nonlinear; no local linear EB holds either. Thus our fixed-coordinate theorem contains all source Theorem 2 hypotheses and genuinely includes additional fixed \((F,v,\lambda)\) data.

The rate cannot be linear for this witness. Starting at \(x_0>0\), the exact iteration satisfies

\[
x_k=x_{k+1}+\lambda x_{k+1}^p,
\qquad x_k\downarrow0.
\tag{NGK41}
\]

Its ratio \(x_{k+1}/x_k=(1+\lambda x_{k+1}^{p-1})^{-1}\to1\). More precisely, for \(b=p-1\), the mean-value theorem gives

\[
x_{k+1}^{-b}-x_k^{-b}
=b\lambda(x_{k+1}/\xi_k)^p\to b\lambda,
\quad x_{k+1}\le\xi_k\le x_k.
\]

Cesàro averaging yields \(x_k\sim[(p-1)\lambda k]^{-1/(p-1)}\). Its total physical length is exactly \(x_0\), by telescoping its positive decreasing scalar trajectory. Negative initial data are symmetric.

The strict comparison is **not** with the entirety of source Theorem 1 or arbitrary GPPA representations. The source's monotone-pair Theorem 1 already supplies distance convergence for this example, and in one dimension with a singleton zero that is point convergence. A different kernel can also restore ASM; for example \(\widetilde v=F\) makes the pair 1-ASM, while changing the warped algorithm. The witness therefore proves a strict relaxation of the source's *fixed-kernel quadratic Theorem 2 assumptions*, with polynomial rather than linear rates, and does not prove any exclusion for all kernels or any global novelty claim.

<a id="ngk-verdict"></a>
## NGK-11 · What has been absorbed, and what remains separate

The useful source machinery is its exact kernel update, full pair monotonicity/ASM in kernel coordinates, zero-anchor polarization, selected residual \((z_k-z_{k+1})/\lambda\), and the physical R-continuity bridge. This file retains those objects and embeds them in a full-kernel-union relation; it never assumes that a noninjective kernel controls its physical fibers.

The extension adds arbitrary same-scale reflected moduli, true kernel residual gauges, a three-branch scalar recurrence, exact nonlinear summability and Dini certificates, a weak-EB shell certificate, and explicit physical inverse/fiber gates. These are conditional theorem statements: arbitrary nonlinear exponents do not universally improve convergence, and weaker gauges can replace geometric rates by polynomial rates. Preserving the source energy/dissipation branch proves the required inclusion; NGK-10 proves strictness for the fixed-kernel Theorem 2 assumption class.

This does not settle whether every ordinary RLEB instance can be represented by a source-compatible GPPA with a different kernel or zero-preserving subrelation; the existing [branch-restriction constructions](sol61_branch_restriction.md) show why original-full-graph failure is insufficient for that claim. It does not settle arbitrary lifts, global prior literature, natural-mother-space size comparisons, structural shadow/fiber theorems, or physical convergence without a lifting gate. Inexact perturbations and regularization are deliberately not incorporated into this exact theorem; source Theorem 4 changes the relation to \(F+\epsilon v\) and needs its own existence, perturbation, and gauge-window analysis.
