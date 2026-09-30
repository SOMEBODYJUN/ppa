# Characterization theory for attractive genuine Hölder RL geometry

## Scope and notation

This dossier treats only the converse/classification problem. The established sufficient theory—F-side tangent/normal jets, the effective normal balance with net coefficient \(-\tfrac12 II\), residual regularity, and the operator/curvature phase diagram—is used as baseline.

Let

\[
x=y+\lambda v,\qquad v\in F(y),\qquad p\in P_S(x),\qquad q\in P_S(y),
\]

and write

\[
d=d(x,S),\quad r=d(y,S),\quad n=x-p,\quad m=y-q,
\]

\[
R=R_p=(y-p)-\lambda v.
\]

When \(S\) is a manifold, put \(u=P_{T_qS}v\), \(w=P_{N_qS}v\), and \(a=\lambda u\). All asymptotic assertions are along the proximal branch under discussion. Uniform assertions over a branch family require a relatively compact chart and uniform remainders.

---

# A. Strongest converse theorem

## Theorem A (kinematic converse, exact normal defect, and inverse phase)

Assume first that \(S\) is a \(C^1\) embedded manifold on a relatively compact local patch, that the displayed nearest points remain in this patch, and that

\[
r=O(d),\qquad \|R\|\asymp \omega(d),\qquad d=o(\omega(d)).
\tag{A.1}
\]

Then the following conclusions are forced.

### (i) The selected residual and nearest-solution drift are forced

The exact identities

\[
2\lambda v=n-R,\qquad 2(y-p)=n+R
\tag{A.2}
\]

imply

\[
\|v\|\sim \frac{\|R\|}{2\lambda},
\qquad
q-p=\frac12R+O(d).
\tag{A.3}
\]

Consequently the selected residual has a leading tangential component:

\[
\lambda P_{T_qS}v=-(q-p)+o(\omega(d)),
\qquad
\|P_{T_qS}v\|\sim\frac{\omega(d)}{2\lambda},
\tag{A.4}
\]

while

\[
\|P_{N_qS}v\|=o(\omega(d)).
\tag{A.5}
\]

Thus genuine sublinear reflected motion necessarily determines a selected tangential residual scale in the input variable \(d\). It does not yet determine a scale depending only on \(r\).

### (ii) The effective normal object is forced exactly

Represent \(S\) at \(q\) as the orthogonal graph

\[
q+\tau+h_q(\tau),\qquad h_q(0)=Dh_q(0)=0.
\]

Define the normal defect

\[
E_\lambda:=m+\lambda w-h_q(a),\qquad a=\lambda u.
\tag{A.6}
\]

Then

\[
\boxed{d=(1+o(1))\|E_\lambda\|.}
\tag{A.7}
\]

This remains informative under arbitrarily deep cancellation; it is stronger than replacing geometry by an additive \(o(\|a\|^2)\) error.

If \(S\) is \(C^2\), with

\[
II_q(\xi,\eta)=P_{N_qS}D_\xi\widetilde\eta,
\]

then uniformly

\[
\boxed{
E_\lambda
=m+\lambda w-\frac12II_q(a,a)+o(\|a\|^2).
}
\tag{A.8}
\]

Hence algorithmic scaling recovers the *combined* effective normal defect, not its operator, output-error, and curvature summands separately.

### (iii) Scalar scale transport is conditional, not automatic

Suppose in addition that the branch is **radially synchronized**: there is an increasing profile \(C\) such that, uniformly on the branch,

\[
d\asymp C(r),
\tag{A.9}
\]

and the inverse is stable under constant dilation. Define

\[
A(r)\asymp \|P_{T_qS}v\|.
\]

Then (A.4) forces

\[
A(r)\asymp \lambda^{-1}\omega(C(r)),
\]

and therefore

\[
\boxed{
\omega(d)\asymp \lambda A(C^{-1}(d)).
}
\tag{A.10}
\]

Thus tangent–normal scale transport is necessary once a common radial calibration exists. Attraction and a sharp reflected scale alone do not force such a scalar calibration.

In particular, if

\[
\|R\|\asymp d^\gamma,\qquad r\asymp d^\beta,
\qquad 0<\gamma<1,
\tag{A.11}
\]

then necessarily, along the selected branch,

\[
C(r)\asymp r^{1/\beta},\qquad
A(r)\asymp r^{\gamma/\beta}.
\tag{A.12}
\]

### (iv) Inverse second-order phase, under superlinear normal attraction

Assume now that \(S\) is \(C^2\),

\[
r=o(d),\qquad \|R\|\asymp d^\gamma,qquad 0<\gamma<1.
\tag{A.13}
\]

Let \(s=\|a\|\) and \(e_a=a/s\). Then

\[
s\sim\frac{\|R\|}{2}\asymp d^\gamma,
\qquad
\lambda\|w\|=O(d+s^2),
\tag{A.14}
\]

and the following trichotomy is necessary.

1. If \(\gamma>\tfrac12\), then \(s^2=o(d)\) and

   \[
   \lambda w=P_{N_qS}n+o(d),\qquad
   \lambda\|w\|\sim d.
   \tag{A.15}
   \]

   The leading normal mechanism is necessarily operator-normal.

2. If \(\gamma=\tfrac12\), then \(s^2\asymp d\), \(w=O(d)\), and

   \[
   \frac{\lambda w}{s^2}-\frac12II_q(e_a,e_a)
   =\frac{P_{N_qS}n}{s^2}+o(1).
   \tag{A.16}
   \]

   Operator forcing, curvature, and nonresonant coupling are all possible. The exponent alone does not identify the mechanism.

3. If \(\gamma<\tfrac12\), then \(d=o(s^2)\) and

   \[
   \boxed{
   \frac{\lambda w}{s^2}-\frac12II_q(e_a,e_a)\longrightarrow0.
   }
   \tag{A.17}
   \]

   Hence, if \(\inf\|II_q(e_a,e_a)\|>0\), operator and curvature terms must undergo vectorial leading-order resonance and \(\|w\|\asymp s^2\). If \(w=o(s^2)\), the actual direction must instead satisfy \(II_q(e_a,e_a)\to0\).

Finally, in the half-exponent case the additional condition

\[
w=o(d)
\tag{A.18}
\]

does identify curvature:

\[
d=\frac{\lambda^2}{2}\|II_q(u,u)\|(1+o(1)),
\quad
\inf\|II_q(e_a,e_a)\|>0,
\tag{A.19}
\]

and

\[
\frac{\|R\|^2}{d}
=\frac{8}{\|II_q(e_a,e_a)\|}(1+o(1)).
\tag{A.20}
\]

## Proof

Equation (A.2) follows by eliminating \(y\) from \(x=y+\lambda v\) and the definition of \(R\). Since \(\|n\|=d=o(\|R\|)\), it yields the first asymptotic in (A.3). Also

\[
q-p=(y-p)-m=\frac12(n+R)-m=\frac12R+O(d).
\]

On a uniform \(C^1\) patch, a chord \(q-p\) is tangent to first order. Combining this fact with

\[
\lambda v=(p-q)+(n-m)
\]

gives (A.4)–(A.5).

For (A.7), write \(x=q+a+z\), where \(z=m+\lambda w\). For any graph point \(q+\tau+h_q(\tau)\), if \(L\) is the Lipschitz constant of \(h_q\) on the shrinking relevant ball, then

\[
\|E_\lambda\|
\le \|z-h_q(\tau)\|+L\|a-\tau\|
\le \sqrt{1+L^2}\,\|x-(q+\tau+h_q(\tau))\|.
\]

Choosing \(\tau=a\) gives the reverse upper bound

\[
d\le\|E_\lambda\|.
\]

Since \(L\to0\), (A.7) follows. Under \(C^2\), the uniform Peano expansion

\[
h_q(a)=\tfrac12II_q(a,a)+o(\|a\|^2)
\]

proves (A.8), including the net coefficient \(-\tfrac12\).

Equations (A.9)–(A.12) are monotone inversion of the already forced selected tangential scale. Without (A.9), the same output radius can correspond to incomparable input distances, so no scalar \(C(r)\) exists.

For the inverse phase, (A.4) gives \(s\sim\|R\|/2\). Projecting \(n\) to \(N_qS\) changes its norm only by \(1+o(1)\), and (A.8) gives

\[
P_{N_qS}n=m+\lambda w-\tfrac12II_q(a,a)+o(s^2).
\tag{A.21}
\]

Because \(m=o(d)\), comparison of \(s^2\) with \(d\) proves (A.15)–(A.17). Under (A.18), the half-exponent balance leaves curvature as the only possible leading term, proving (A.19). Since \(\|R\|\sim2s\), (A.20) follows.

---

# B. Necessary assumptions and their roles

| Assumption | What it buys | What fails without it |
|---|---|---|
| Existing nearest points along the branch | Definitions of \(p,q,n,m\) | At nonunique projections, different anchors can give different drifts. |
| Uniform \(C^1\) active manifold patch | Linear tangent space, chord tangency, exact graph defect | A general tangent cone need not supply a unique tangential direction. |
| \(r=O(d)\) | Removes output-normal error from the leading reflected scale | A large \(m\) can mask nearest-solution drift. |
| \(d=o(\|R\|)\) | Genuine sublinear motion and \(v\sim-R/(2\lambda)\) | No forced leading tangent motion at Lipschitz scale. |
| Radial synchronization \(d\asymp C(r)\) | A scalar \(A(r),C(r)\) transport law | The same \(r\) may carry incomparable algorithmic scales. |
| Uniform \(C^2\) Peano jet | Explicit \(-\tfrac12II\) and inverse phase | \(C^{1,1}\) gives only a quadratic bound, not a unique tensor coefficient. |
| \(r=o(d)\) | Separates operator/curvature from the output normal term | With merely \(r=O(d)\), \(m\) may be the leading normal mechanism. |
| Full-value residual lower bound | Recovers \(d(0,F(y))\) | Selected values never exclude hidden smaller values. |
| Two-sided common-branch scaling | Exact exponent identities | Supremal exponents may be realized on different subsequences. |

### Minimal geometric setting

- **\(C^1\) manifold:** sufficient for the first-order tangent necessity and the exact graph-defect formula along sequences for which the relevant nearest points are already available. It does not itself guarantee a uniform tubular projection.
- **\(C^{1,1}\) manifold:** locally supplies positive reach/uniform projections and \(h_q(a)=O(\|a\|^2)\). It supports an order-level operator-versus-geometric comparison, but not an intrinsic pointwise \(II\) coefficient everywhere.
- **\(C^2\) manifold:** the clean weakest standard hypothesis for the uniform tensorial inverse phase used here. An along-branch second Peano jet would suffice, but is less usable as a theorem hypothesis.
- **Prox-regular set:** projection and quadratic support estimates survive, but the tangent object may be a cone rather than a vector space. If the local reach is at least \(\rho>0\), the hypomonotonicity/support estimate gives

  \[
  \operatorname{dist}(q-p,T_S(p))
  \le \frac{\|q-p\|^2}{2\rho}.
  \]

  Hence the universal replacement is

  \[
  \operatorname{dist}(R,T_S(p))=o(\|R\|),
  \qquad
  \operatorname{dist}(v,T_S(q))=o(\|v\|).
  \]

  This is a tangent-cone statement, not an orthogonal decomposition relative to a linear active tangent space; no canonical \(-\tfrac12II\) exists in general.
- **Stratified/partly smooth set:** the theorem applies after a single \(C^1\) or \(C^2\) active stratum is identified and both projections remain on it. At stratum switching or singular intersections there is no single stable tangent/curvature field, so a manifold classification is false without identification.

---

# C. Counterexamples to failed converses

## C.1 Algorithmic scaling does not force scalar \(A(r),C(r)\)

Let \(S=\mathbb R\times\{0\}\), \(\lambda=1\), and choose

\[
0<\gamma<1,\qquad \delta(t)=\delta_0+ct\in[\delta_-,\delta_+]\Subset(0,1).
\]

For \(r>0\), define the single-valued continuous operator

\[
F(t,r)=\bigl(r^{\gamma\delta(t)},\ r^{\delta(t)}-r\bigr),
\qquad F(t,0)=0.
\tag{C.1}
\]

For input \(x=(s,d)\), the proximal equations give

\[
t=s-d^\gamma,qquad r=d^{1/\delta(t)}.
\]

Thus

\[
\|R\|\sim2d^\gamma,qquad r=o(d),
\]

uniformly. But for \(r_j=e^{-j^2}\) and \(t_j^\pm=\pm1/j\),

\[
d_j^\pm=r_j^{\delta(t_j^\pm)}
=e^{-\delta_0j^2\mp cj},
\]

whose ratio is unbounded. The same output radius therefore has incomparable \(d\), tangential residual, and reflected scales. Even flatness, single-valuedness, continuity, resolvent existence, sharp \(d^\gamma\), and superlinear attraction do not imply a scalar radial transport law.

## C.2 \(\gamma=\tfrac12\) need not mean curvature

On the same flat \(S\), let

\[
F(t,z)=\bigl(az^\alpha,bz^{2\alpha}\bigr),
\qquad 0<\alpha<\tfrac12,quad a,b>0.
\tag{C.2}
\]

For \(y=(t,r)\),

\[
d=r+\lambda br^{2\alpha}\sim\lambda br^{2\alpha},
\quad r\asymp d^{1/(2\alpha)}=o(d),
\]

and

\[
\|R\|\sim2\lambda ar^\alpha\asymp\sqrt d.
\]

Yet \(II\equiv0\); the mechanism is purely operator-normal. On a curved cylinder, taking the drift along the axial null-curvature direction gives the anisotropic analogue.

## C.3 Selected geometry does not determine minimum residual

On \(S=\mathbb S^1\), for outward points \(y=(1+r)q\), define

\[
F(y)=\{\sigma ar^\alpha Kq+br^\delta q:-1\le\sigma\le1\},
\qquad 0<\alpha<\delta<1.
\tag{C.3}
\]

The endpoint selections \(\sigma=\pm1\) have tangential scale \(r^\alpha\) and the established sharp tangent–normal RL geometry. Nevertheless

\[
d(0,F(y))=br^\delta,
\]

because the interior value \(\sigma=0\) removes the tangent component. Full multifunction regularity cannot be recovered from a selected branch.

## C.4 Sharp one-sided exponents do not obey a product calculus

Let \(S=\mathbb R\times\{0\}\), \(s=\log(1/r)\), and

\[
A(r)=r^{3/8+\sin(\log s)/8},\qquad
B(r)=r^{5/8+\sin(\log s)/8}.
\]

Both profiles are strictly increasing. Define the singleton operator

\[
F(t,z)=\bigl(A(|z|),\operatorname{sgn}(z)B(|z|)\bigr).
\tag{C.4}
\]

Then \(d=r+\lambda B(r)\), \(r=o(d)\), \(\|R\|\sim2\lambda A(r)\), and \(e(y)\sim A(r)\). Nevertheless the attained sharp uniform upper-bound exponents are

\[
\Gamma=\frac12,qquad Q=2,qquad \mathsf B=\frac43,
\]

so

\[
\Gamma Q=1<\frac43=\mathsf B.
\]

Different oscillatory subsequences determine the three extrema. This does not contradict the two-sided power theorem below.

---

# D. Power-law characterization and the law \(\gamma q=\beta\)

## Theorem D (residual compatibility law)

On one nonvacuous common family of proximal pairs, assume

\[
\|R\|\asymp d^\gamma,qquad
r\asymp d^\beta,qquad
r\asymp e(y)^q,
\tag{D.1}
\]

with \(0<\gamma<1\), \(\beta>1\), and \(q>0\). Then

\[
\boxed{\gamma q\le\beta.}
\tag{D.2}
\]

Moreover,

\[
\boxed{
\gamma q=\beta
\iff e(y)\asymp\|v\|
\iff e(y)\asymp\|R\|.
}
\tag{D.3}
\]

Indeed,

\[
\frac{e(y)}{\|v\|}\asymp d^{\beta/q-\gamma}.
\tag{D.4}
\]

This theorem is purely algebraic and needs no manifold regularity. It shows that \(\gamma q=\beta\) is a characterization of **minimum-residual compatibility on the same branch**, not a characterization of curvature.

Consequences for the proposed failure list are precise:

- **Minimum-residual mismatch:** exactly produces strict \(\gamma q<\beta\) under the three two-sided powers.
- **Branch mismatch:** invalidates the common-family hypothesis; separately optimized exponents cannot be multiplied.
- **Critical curvature cancellation:** changes \(\gamma\) and \(\beta\) together and does not by itself break equality when residuals match.
- **Non-power corrections:** require gauge-level identities; endpoint Hölder powers may fail.
- **Only one-sided or supremal exponents:** may violate the product relation even for a singleton operator with \(e\asymp\|v\|\), as in C.4.

An equivalent endpoint form is useful. If only the first two comparisons in (D.1) are known and \(q_0=\beta/\gamma\), then

\[
r\le C e(y)^{q_0}
\quad\Longleftrightarrow\quad
e(y)\asymp\|v\|.
\tag{D.5}
\]

No error-bound exponent larger than \(q_0\) is possible.

---

# E. When \(\gamma=\tfrac12\) signals curvature

The strongest valid identification is conditional:

> On a uniform \(C^2\) manifold patch, if \(r=o(d)\), \(\|R\|\asymp\sqrt d\), and \(P_{N_qS}v=o(d)\), then nondegenerate quadratic curvature in the actual drift direction is forced and is the leading normal mechanism, with (A.19)–(A.20).

Each clause is necessary.

- Without \(P_Nv=o(d)\), the flat model C.2 has operator-generated \(1/2\).
- Without \(r=o(d)\), the flat model

  \[
  F(t,z)=(a\sqrt z,bz^\eta),\qquad \eta>1,
  \]

  has \(r/d\to1\), \(P_Nv=o(d)\), and \(\|R\|\asymp\sqrt d\); the leading normal term is \(m\).
- Curvature elsewhere on \(S\) is irrelevant; \(II(e_a,e_a)\) must be tested in the actual leading drift direction.
- At \(\gamma=1/2\), a nonzero paired operator/curvature vector also gives the same exponent.

Thus \(1/2\) is the universal exponent of a nondegenerate quadratic leakage mechanism, but it is not a unique fingerprint of that mechanism.

---

# F. Stability and fragility map

| Feature | Stable under | Fragile under |
|---|---|---|
| Algebraic identities (A.2) | Any perturbation preserving the proximal equation | Not applicable; they are exact. |
| First-order tangent necessity | Uniform \(C^1\) active-manifold perturbations and preserved attraction margins | Loss of active-stratum identification or comparable output error. |
| Nonresonant power phase | Higher-order F perturbations; uniform relative perturbations smaller than the leading defect | Perturbations at the leading defect scale. |
| Curvature nondegeneracy | Small \(C^2\) perturbations of \(S\) with a positive directional margin | Drift toward a null-curvature direction. |
| Full residual matching | Full-value weighted Hausdorff perturbations \(o(A(r))\), or smaller than the residual gap | Adding one hidden value of smaller norm; selected-branch closeness is insufficient. |
| Radial synchronization | Relative defect perturbations \(o(C(r))\) and constant-dilation-stable \(C\) | Oscillatory direction/radius coupling such as C.1 or C.4. |
| Critical cancellation \(C\ll A^2\) | Paired perturbations satisfying \(\delta w=o(C)\) and \(\delta u=o(C/A)\) | Generic \(o(A)\) tangent or \(o(A^2)\) normal changes; these may exceed \(C\). |
| Dependence on \(\lambda\) | A uniform nonzero leading-vector margin persists for nearby \(\lambda\) | Exact resonance is normally destroyed by every fixed \(\lambda\ne\lambda_0\); preserving it needs \(|\Delta\lambda|A^2=o(C)\). |
| Flat operator phase | Stable within the class of affine solution manifolds | If \(A^2\gg B\), arbitrarily small nonzero curvature eventually changes the asymptotic phase. |

For fixed \(S,y\), the exact defect gives a useful perturbation test. If \(\tilde u=u+\delta u\), \(\tilde w=w+\delta w\), and \(\|u\|\asymp A\), then

\[
\|\widetilde E-E\|
\lesssim \lambda\|\delta w\|
+K\lambda^2\bigl(A\|\delta u\|+\|\delta u\|^2\bigr).
\tag{F.1}
\]

Therefore \(\delta w=o(C)\), \(\delta u=o(A)\), and \(A\|\delta u\|=o(C)\) preserve a defect scale \(C\). Away from resonance, \(C\gtrsim A^2\) makes the third condition automatic; deep resonance does not.

Invertible affine coordinate changes preserve the algebraic proximal relation after transforming \(F\), and preserve power exponents because norms are equivalent. A nonlinear diffeomorphism is not a naive covariance of Euclidean PPA: exact conjugacy adds a quadratic term

\[
\frac{\Phi(y+\lambda v)-\Phi(y)}{\lambda}
=D\Phi(y)v+\frac\lambda2D^2\Phi(y)[v,v]+o(\|v\|^2).
\]

That term is precisely at the curvature scale. Exact conjugacy preserves convergence exponents but may transfer what is called “curvature” into the transformed operator; a naive differential pushforward can change the mechanism.

---

# G. Final verdict and corrected classification map

The tangent–normal scale-transport mechanism is more than a sufficient construction, but less than an unconditional scalar classification principle.

What is universal is the following chain:

\[
\text{attractive genuine sublinear reflection}
\Longrightarrow
\text{selected residual of the same scale}
\Longrightarrow
\text{leading nearest-solution drift is tangent}
\Longrightarrow
\text{input distance is the exact normal defect }\|E_\lambda\|.
\]

With radial synchronization, this becomes the scalar transport law

\[
\omega\asymp \lambda A\circ C^{-1}.
\]

Without synchronization, no functions \(A(r),C(r)\) need exist, even for a continuous singleton operator on a flat solution manifold with a genuine superlinearly attractive resolvent.

Under \(C^2\) geometry and \(r=o(d)\), the converse becomes a genuine local phase classification:

\[
\gamma>\tfrac12\Rightarrow\text{operator-normal leading},
\]

\[
\gamma=\tfrac12\Rightarrow\text{operator/curvature/coupled ambiguity},
\]

\[
\gamma<\tfrac12\Rightarrow\text{quadratic resonance or directional curvature degeneration}.
\]

The half exponent identifies curvature only after operator-normal forcing and output normal error are proved lower order. The product law \(\gamma q=\beta\) identifies minimum-residual matching, not curvature.

Finally, the schematic “\(\gamma=1\Rightarrow\) isolated-type geometry” is too strong. A nonisolated flat solution manifold may have a branch with no leading tangent drift and sharp \(\gamma=1\). The correct statement is only that \(\gamma=1\) shows no genuine sublinear reflected amplification; it does not characterize isolation.

Accordingly, tangent–normal transport is close to a local classification principle precisely at the **parametric defect level**. Its scalar F-side form requires two independent model facts that algorithmic data cannot supply: radial synchronization and full-value residual separation. Critical resonance, anisotropic null directions, hidden multifunction values, and oscillatory scales are the exact obstructions—not defects of the proof.
