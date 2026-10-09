# C221 · Scalar-tail Lyapunov and direct KL interfaces for GPPA

**Status:** `derived-checked`, independently reconstructed TL1–TL24 in the displayed scope; external priority remains unverified. Date: 2026-10-09. Independent reconstruction of TL1–TL24 found no fatal objection; the precise global identity is C221. This page supplies self-contained reductions; it does not change C208–C220 or claim a new abstract convergence principle. The initial frozen source was repository HEAD `94cbbbd9bacb61787eeee583e0282b890455849a`.

The finite scalar-tail part of C209 admits a continuous Caristi-type potential even when the actual resolvent is not calm. A substantial parameter subfamily of the complete noncalm SF example also satisfies the original-coordinate Attouch–Bolte–Svaiter (ABS) conditions. These positive reductions narrow the novelty claim: the remaining question concerns the complete RL/true-EB compilation and its quantified interfaces, not absence of Lyapunov or objective-function descriptions.

<a id="gtl-data"></a>
## TL1 · Exact local relation and finite scalar input

Let \(H\) be a real Hilbert space, \(Q\subset H\), \(U\subset H\) open, \(Z\subset Q\) nonempty and closed in \(H\), and \(R>0\). Put

\[
E=\{z\in Q\cap U:d(z,Z)<R\}.
\]

Let \(\mathscr T:E\rightrightarrows Q\) be a covered transition relation: \(\mathscr T(z)\ne\varnothing\) for every \(z\in E\). All its outputs, without a selected subrelation, must satisfy

\[
d(y,Z)\le\tau(d(z,Z)),\qquad
\|y-z\|\le b(d(z,Z)),\quad y\in\mathscr T(z).
\tag{TL1}
\]

Here \(b,\tau:[0,R]\to[0,\infty)\) are continuous nondecreasing, \(b(0)=\tau(0)=0\), and \(\tau(t)<t\) for \(0<t\le R\). Thus \(\tau\) maps \([0,R]\) into itself. Fix \(z_0\in E\), write \(r=d(z_0,Z)<R\), and assume the **scalar** input

\[
L(r):=\sum_{j=0}^{\infty}b(\tau^j(r))<D_U(z_0),
\quad D_U(z_0)=d(z_0,H\setminus U).
\tag{TL2}
\]

The left side is required finite, including when \(D_U(z_0)=+\infty\). It is defined from \(b,\tau,r\), before constructing any orbit. No actual-trajectory length or already-proved convergence is used to define the potential. Only this one scalar starting radius needs a finite tail; no uniform shrinking ratio such as \(L(t)/b(t)=O(1)\) is assumed.

For fixed-kernel GPPA, take \(Q=\operatorname{ran}v\), the exact kernel graph \(\Gamma\) of NGK1–4, and **fixed** \(\lambda>0\). The relation \(\mathscr T(z)\) contains every output of \(z=y+\lambda f\), \((y,f)\in\Gamma\). NGK9–17 compile TL1 with \(b=B\) and \(\tau\) the minimum of the available direct/energy/anchor bounds. When the anchor branch is certified, \(b=\min\{B,\operatorname{Id}\}\) is also valid. The EB is the full union residual \(r_A\), not the chosen value alone. No monotonicity of \(v\), injectivity, closedness of \(Q\), completeness of \(Q\), or unique physical output is added.

The abstract theorem also allows an indexed family \(\mathscr T_\lambda\), \(\lambda\in\Lambda\), and arbitrary sequences \(\lambda_k\in\Lambda\), **only if** coverage and the same TL1 functions hold for every \(\lambda\in\Lambda\) and every output. A theorem verified for one fixed \(\lambda\) does not supply those common data.

<a id="gtl-potential"></a>
## TL2 · Continuous potential without differentiability

On the finite interval \([0,r]\), define

\[
L(t)=\sum_{j=0}^{\infty}b(\tau^j(t)).
\tag{TL3}
\]

Then \(L\) is finite, continuous and nondecreasing, \(L(0)=0\), and

\[
L(t)=b(t)+L(\tau(t)),\qquad 0\le t\le r.
\tag{TL4}
\]

**Proof.** Each summand is continuous and nondecreasing. It is bounded uniformly on \([0,r]\) by \(b(\tau^j(r))\), whose series converges by TL2. The Weierstrass uniform-convergence argument proves continuity and finiteness, including at zero. Reindexing a convergent nonnegative series proves TL4. At \(r=0\), TL3 is simply the function zero on the singleton interval and all later conclusions are absorption. □

Define the potential only on \(\{z:d(z,Z)\le r\}\):

\[
\Phi(z)=L(d(z,Z)).
\tag{TL5}
\]

It is continuous there, bounded below by zero. For any covered input in this set and **every** allowed output, TL1 and TL4 give

\[
\Phi(z)-\Phi(y)
\ge L(d(z,Z))-L(\tau(d(z,Z)))
=b(d(z,Z))\ge\|z-y\|.
\tag{TL6}
\]

This is a first-power Caristi descent inequality in the original Hilbert metric. It requires neither a bounded subgradient nor KL regularity of \(\Phi\). In particular TL6 does not by itself verify ABS H2. If a globally defined continuous function is desired, \(z\mapsto L(\min\{d(z,Z),r\})\) is an extension, but TL6 is asserted only where TL1 and \(d(z,Z)\le r\) hold.

<a id="gtl-retention"></a>
## TL3 · All trajectories, retention and exact target

Define the explicit invariant set

\[
K=\{z\in Q: d(z,Z)\le r,
\ \|z-z_0\|+\Phi(z)\le L(r)\}.
\tag{TL7}
\]

It is nonempty because it contains \(z_0\). Every point of \(K\) lies in \(U\), since its distance to \(z_0\) is at most \(L(r)<D_U(z_0)\), and has \(d(z,Z)\le r<R\). Thus \(K\subset E\) and coverage is applicable. For every \(z\in K\), \(y\in\mathscr T(z)\), TL1 gives \(d(y,Z)\le r\), while TL6 and the triangle inequality give

\[
\|y-z_0\|+\Phi(y)
\le\|z-z_0\|+\|y-z\|+\Phi(y)
\le\|z-z_0\|+\Phi(z)\le L(r).
\]

The output belongs to \(Q\) by assumption, so \(y\in K\). Coverage and invariance therefore construct **every permitted trajectory** indefinitely, with no prior assumption of stay in the window. This works for arbitrary multivalued choices and, with the common-data gate in TL1, arbitrary permitted step parameters.

For any such trajectory, monotonicity of \(\tau\) gives \(d(z_k,Z)\le\tau^k(r)\). The scalar sequence \(\tau^k(r)\) tends to zero: it is nonincreasing, and any positive limit would contradict continuity and \(\tau(t)<t\). Telescoping TL6 from \(k\) to \(n-1\) gives

\[
\sum_{j=k}^{n-1}\|z_{j+1}-z_j\|
\le\Phi(z_k)-\Phi(z_n)\le L(d(z_k,Z)).
\tag{TL8}
\]

Hence the total length is at most \(L(r)\), and the orbit is Cauchy in complete \(H\). Its ambient limit lies in closed \(Z\), because the distance to \(Z\) tends to zero, and remains in \(U\) by the strict budget. Thus

\[
z_k\to z_\infty\in Z\cap U\subset Q,
\quad\|z_k-z_\infty\|\le L(d(z_k,Z))
\le L(\tau^k(r))=\sum_{j=k}^{\infty}b(\tau^j(r)).
\tag{TL9}
\]

Completeness of \(K\) or \(Q\) is unnecessary for this proof; the limit is recovered in \(Q\) through \(Z\subset Q\). The target is the prescribed \(Z\), not a silently changed \(\operatorname{Fix}\mathscr T\). At distance zero, TL1 forces \(y=z\), so the kernel transition absorbs. Physical points inside a zero fiber may still move unless a physical transition bound rules it out.

<a id="gtl-caristi"></a>
## TL4 · Exact complete-domain Caristi interface

The directly read older primary source is Kuhlmann–Kuhlmann–Paulsen, *The Caristi–Kirk Fixed Point Theorem from the point of view of ball spaces* (2018), [publisher full text](https://link.springer.com/article/10.1007/s11784-018-0576-8), §1 Theorem 1 and §2 Lemma 5. Its fixed-point theorem assumes a complete metric domain, a self-map, and a bounded-below lsc potential satisfying \(d(z,Tz)\le\Phi(z)-\Phi(Tz)\). The theorem guarantees existence of a fixed point, not the convergence of every unqualified Caristi orbit to a fixed point. TL8 is the elementary telescoping consequence; TL9 adds the certified distance contraction and target closedness.

For C209 with **all-pairs** RL, NGK12 makes its kernel map \(T\) unique and uniformly continuous at small input distances, with modulus \(\sqrt{C_\omega}\). This closes the complete-domain gate even when \(Q\) is not closed:

1. Form \(K\) in TL7, then \(\overline K\) in \(H\). Continuity of \(d\) and \(L\) gives \(d(z,Z)\le r\) and \(\|z-z_0\|+\Phi(z)\le L(r)\) on \(\overline K\). Therefore \(\overline K\subset U\) and the potential is finite there. \(\overline K\) is complete, though it can contain points outside \(Q\).
2. For \(z\in\overline K\), choose \(z_n\in K\) tending to \(z\). The NGK12 modulus shows \((Tz_n)\) is Cauchy, since the distances between sufficiently late \(z_n\)'s are below \(R\). Its limit is independent of the approximating sequence. This defines a continuous extension \(\overline T:\overline K\to\overline K\), since \(T(K)\subset K\).
3. Pass TL1 and TL6 to the limit. Then \(\overline T\) is a self-map of a complete metric space satisfying the cited Caristi condition. Moreover any fixed point satisfies \(d(z,Z)\le\tau(d(z,Z))\), hence lies in \(Z\); conversely every \(z\in Z\cap\overline K\) is fixed by the zero step bound.

This extension is solely a way of meeting the older theorem's complete-domain hypothesis. It is not new GPPA coverage at points outside \(Q\). The original all-trajectory conclusions concern the original relation on \(K\). With only zero-anchor RL, continuity/uniqueness may fail; TL1–TL9 still apply to all outputs, but this single-valued complete-domain extension is not claimed.

<a id="gtl-energy"></a>
## TL5 · C209 geometric-energy certificate also has a scalar-tail potential

NGK24 has \(R\le M\), \(C_\omega(t)\le qV(t)\), \(0<q<1\). Here

\[
B(t)^2\le C_\omega(t),\quad
C_\omega(t)-B(t)^2=(t-\omega(t))^2/4.
\tag{TL10}
\]

Since \(qV(t)<V(t)\le V(M)\), the inverse cap is inactive for \(t<R\), and \(V(\tau(t))\le V(\tau_E(t))=C_\omega(t)\le qV(t)\). Thus the scalar iterate itself obeys

\[
B(\tau^j(r))\le\sqrt{qV(\tau^j(r))}
\le q^{(j+1)/2}\sqrt{V(r)},
\quad
\sum_jB(\tau^j(r))\le\frac{\sqrt{qV(r)}}{1-\sqrt q}.
\tag{TL11}
\]

Therefore this independent energy certificate implies the finite scalar-tail gate with the same length budget. This conclusion follows from the scalar data, not from already-known convergence of a GPPA orbit. It refines NGK5's cautious statement that its energy proof does not itself assert convergence of the loose \(B\circ\tau^j\) series.

The NGK24 energy comparison is imposed for \(0<t<R\), whereas TL1's convenient abstract convention tests the endpoint too. For an initial \(r<R\), choose any \(R'\in(r,R)\) and restrict the scalar data/coverage to \([0,R']\); the energy comparison then holds at every positive point of that closed interval and supplies \(\tau(t)<t\) there. Thus this endpoint convention adds no assumption to the energy branch.

For C210 physical step moduli, the same algebra is available with \(b_\eta(t)=\eta(B(t))\), provided \(\eta\) is continuous nondecreasing with \(\eta(0)=0\), every allowed physical transition satisfies \(\|x^+-x\|\le\eta(\|v(x^+)-v(x)\|)\), and the scalar tail \(\sum_jb_\eta(\tau^j(r))\) is finite. Then \(L_\eta(d(vx,Z))\) drops by at least the physical step for every allowed choice. It need not be continuous/lsc as a function of \(x\) when \(v\) is discontinuous; the telescoping length statement needs no such regularity. Identification of the physical limit with a point of the exact solution set, and physical collar retention, retain C210's separate gates.

<a id="gtl-sf-kl"></a>
## TL6 · The complete noncalm SF map directly enters ABS for a parameter sector

Fix \(\nu>1\), \(0<\gamma<1\), \(A_0>0\), \(0<\rho<1\), \(\lambda=1\), and the **complete** relation on \(\mathbb R^2\)

\[
F(\xi,y)=\{(-A_0y^{\gamma/\nu},y^{1/\nu}-y),
(-A_0y^{\gamma/\nu},-y^{1/\nu}-y)\},\quad y\ge0;
\qquad F(\xi,y)=\varnothing\ (y<0).
\tag{TL12}
\]

Both branches at \(y=0\) coincide with zero. Solving \((\xi,r)=(\xi^+,y)+f\) shows that the complete resolvent, for **all signed inputs**, is uniquely

\[
T(\xi,r)=(\xi+A_0|r|^\gamma,|r|^\nu),
\quad S=\mathbb R\times\{0\}.
\tag{TL13}
\]

The branch sign is dictated by the sign of \(r\); none is deleted. At \(r=0\), \(T\) is the identity. For any fixed point \(p=(\xi,0)\), \(\|T(\xi,r)-p\|/|r|\ge A_0|r|^{\gamma-1}\to\infty\), so it remains an actual noncalm example.

Suppose

\[
\gamma\ge\frac{\nu}{2\nu-1},
\qquad
1+\frac\gamma\nu\le\beta\le2\gamma.
\tag{TL14}
\]

The interval is nonempty exactly under the displayed \(\gamma\) restriction, including equality. In particular \(1<\beta<2\). Define in the **same original coordinates**

\[
f(\xi,r)=|r|^\beta,\quad
\phi(s)=s^{1/\beta},\quad
a=\frac{1-\rho^{\beta(\nu-1)}}{A_0^2+4}>0,
\quad b=\frac\beta{A_0}>0.
\tag{TL15}
\]

The function \(f\) is proper, continuous, convex and \(C^1\), with \(\operatorname{argmin}f=S\). No Lipschitz gradient assumption is needed by ABS's abstract theorem.

For every \(\xi\in\mathbb R\), \(|r|\le\rho\), put \(u=|r|\), \(s=\|T(\xi,r)-(\xi,r)\|\). Then

\[
s^2=A_0^2u^{2\gamma}+(u^\nu-r)^2
\le(A_0^2+4)u^{2\gamma},
\tag{TL16}
\]

because \(|u^\nu-r|\le u^\nu+u\le2u\) and \(u^2\le u^{2\gamma}\). Moreover

\[
f(\xi,r)-f(T(\xi,r))
=u^\beta(1-u^{\beta(\nu-1)})
\ge (1-\rho^{\beta(\nu-1)})u^{2\gamma}\ge as^2.
\tag{TL17}
\]

This is ABS H1, uniformly over the entire signed collar and every tangential coordinate. At the actual output,

\[
\|\nabla f(T(\xi,r))\|=\beta u^{\nu(\beta-1)}
\le\beta u^\gamma\le bs,
\tag{TL18}
\]

so the unique subgradient satisfies ABS H2 with the same constants. The equality case \(\nu(\beta-1)=\gamma\) is allowed.

To verify H3 without assuming the desired convergence, note that \(u_{k+1}=u_k^\nu\le c_\rho u_k\), where \(c_\rho=\rho^{\nu-1}<1\). Thus \(u_k\le c_\rho^ku_0\), all iterates stay in the normal collar, and the tangential coordinate is bounded by

\[
|\xi_k-\xi_0|
\le A_0u_0^\gamma\sum_{j\ge0}c_\rho^{j\gamma}
=\frac{A_0u_0^\gamma}{1-c_\rho^\gamma}.
\tag{TL19}
\]

Finite-dimensional boundedness provides a convergent subsequence; its normal limit is zero and continuity of \(f\) gives function-attentive convergence, exactly H3. This boundedness estimate uses only TL13 and a geometric comparison, not C209 or ABS's convergence conclusion.

At every point of \(S\), \(\phi\) is continuous, concave, \(\phi(0)=0\), \(C^1\) on positive energies with positive derivative, and for \(r\ne0\)

\[
\phi'(f(\xi,r))\operatorname{dist}(0,\partial f(\xi,r))
=\frac1\beta(u^\beta)^{1/\beta-1}\beta u^{\beta-1}=1.
\tag{TL20}
\]

Thus the KL condition is verified explicitly, for every real \(\beta\) allowed by TL14; no definability claim is needed. ABS, *Convergence of descent methods for semi-algebraic and tame problems*, author manuscript dated 2010-12-15, [primary PDF](https://optimization-online.org/wp-content/uploads/2010/12/2864.pdf), Definition 2.4 (PDF7), H1–H3/Lemma 2.6 (PDF8–11), Theorem 2.9 (PDF12), now implies convergence to a point of \(S\) and finite length for **every** complete SF orbit starting at any \(\xi_0\in\mathbb R\), \(|r_0|\le\rho\). The original relation, both branches, Euclidean metric and all its uniquely determined outputs were retained.

This is witness-sector coverage, not a theorem that every C209 instance admits an ABS objective. When \(\gamma<\nu/(2\nu-1)\), this particular power objective cannot meet the two exponent inequalities; it does not follow that any lsc objective, another representation, or another abstract convergence theorem is impossible.

<a id="gtl-sf-c1-obstruction"></a>
## TL6b · The complementary full-collar C¹ obstruction

For the same complete SF map, suppose \(0<\gamma<\nu/(2\nu-1)\). There do not exist \(0<\rho<1\), a function \(f\in C^1(N_\rho)\) on \(N_\rho=\mathbb R\times(-\rho,\rho)\), and fixed constants \(a,b>0\), such that **every** positive input \(z=(\xi,r)\), \(\xi\in\mathbb R\), \(0<r<\rho\), satisfies

\[
f(Tz)+a\|Tz-z\|^2\le f(z),\qquad
\|\nabla f(Tz)\|\le b\|Tz-z\|.
\tag{TL21}
\]

This no-go is for any C¹ objective with these complete positive-collar fixed H1/H2 constants; it is stronger than failure of the particular power family. It is not a claim about general lsc objectives, other metrics/coordinates, trajectory-only certificates, or other abstract descent conditions.

**Proof.** Every \((\xi,y)\), \(\xi\in\mathbb R\), \(0<y<\rho^\nu\), is the output of the positive input \((\xi-A_0y^{\gamma/\nu},y^{1/\nu})\). Therefore the H2 part of TL21 gives

\[
\|\nabla f(\xi,y)\|
\le b\sqrt{A_0^2y^{2\gamma/\nu}+(y-y^{1/\nu})^2}
\le C y^{\gamma/\nu},\qquad C=b\sqrt{A_0^2+1},
\tag{TL22}
\]

using \(0<y<1\) and \(\gamma<1\). C¹ continuity gives \(\nabla f(\xi,0)=0\) for every \(\xi\). The function restricted to the connected zero line therefore has a single constant value \(c\). Integrating TL22 on a normal segment yields

\[
|f(\xi,r)-c|\le\frac{C}{1+\gamma/\nu}r^{1+\gamma/\nu},
\qquad0<r<\rho^\nu.
\tag{TL23}
\]

The explicit orbit TL13 from such an input stays in \(N_\rho\) and converges to the zero line: normal decay and the convergent tangential geometric comparison are TL19, proved independently of TL21. Continuity of \(f\) at that limit and telescoping H1 in TL21 give

\[
f(\xi,r)-c\ge a\sum_{k\ge0}\|Tz_k-z_k\|^2
\ge a A_0^2r^{2\gamma}.
\tag{TL24}
\]

Together TL23–24 force \(aA_0^2\le[C/(1+\gamma/\nu)]r^{1+\gamma/\nu-2\gamma}\). The exponent is strictly positive precisely in the stated sector, giving a contradiction as \(r\downarrow0\). All tangential quantifiers are used: they give output coverage at arbitrary \(\xi\), a connected constant zero-line objective, and no tangential domain boundary for the orbit. The proof does not assert a bounded tangential-collar version without separate output/retention gates. □

<a id="gtl-scope"></a>
## TL7 · What the reductions settle

* C209's summable-envelope convergence, finite length, target membership and local retention have an explicit continuous first-power descent encoding in the same kernel metric. Actual noncalmness does not obstruct this older Lyapunov mechanism.
* Its separate geometric-energy gate also implies a finite \(B\circ\tau^j\) scalar tail by TL10–11, so it enters the same encoding.
* The RL/full-union-EB/coverage hypotheses must still be compiled into TL1 and \(\tau\). Neither Caristi's theorem nor the SF ABS objective states that complete operator theorem for arbitrary \(F,v,\Gamma\). The compilation, domain and physical policies are the remaining exact comparison objects.
* The general tail potential need not have a certified subgradient relative-error inequality or KL property. The old ABS theorem was directly imported only for the explicit SF sector above.
* The SF sector is a positive older-framework reduction despite the surviving finite-violation almost-averaged obstruction of C218. Those conclusions are compatible because their hypotheses differ.

Deterministic finite arithmetic checks and parameter boundaries are in [noncalm_coverage_followup_check.py](../code/gppa_novelty/noncalm_coverage_followup_check.py). They do not replace any of the displayed infinite-series arguments. The literature/read-range record and C212 dyadic consequence are in [the follow-up report](../novelty/2026_10_09/noncalm_coverage_followup.md). Independent reception reconstructed TL1–TL20, reread the cited ABS H1–H3/T2.9 and Caristi T1, and found no fatal objection. A separate follow-up independently reconstructed TL21–24, including full output coverage, zero-line constancy and the strict exponent contradiction, with no fatal objection. These reviews verify the displayed scope and do not certify global priority.
