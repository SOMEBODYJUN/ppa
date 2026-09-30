# Sharp Hölder Error-Bound Certificates for Proximal Point Convergence near Nonisolated Zero Sets

## T5 core-manuscript draft

Project: RL-PPA-VERIFY  
Paper family: theoretical  
Stage: T5 — conceptual analysis and theoretical argument  
Version: 2026-09-07

This file is a proof-bearing core draft, not a submission-ready manuscript. Mathematical statements labeled as theorems are project derivations independently audited against the stated assumptions. Literature attributions are restricted to the source scope already verified in the research record; claims of priority, exhaustive coverage, and engineering-model identity remain excluded.

### Abstract

We give a quantitative interface for applying a nonlinear reflected-resolvent geometry and an independently verified ordinary set-distance error bound to the fixed-step Euclidean proximal point algorithm. The theorem is stated on an allowed-transition set, separates Minty injectivity from input coverage, and includes a summable localization budget yielding whole-orbit and point convergence near a possibly nonisolated zero set. For a reflection exponent \(0<\gamma<1\) and an error-bound exponent \(q\), the composed estimate has critical balance \(\gamma q=1\) and strict coefficient \(K(L/(2\lambda))^q<1\). We prove that the denominator \(2\) is non-improvable for this uniform asymptotic certificate, while a second example shows that the certificate is not necessary for actual contraction. Two independent verification modules are then applied to a support-function/normal-cone generalized equation. They yield a complete cross-active-face resolvent, the optimal Hölder exponent, an explicit higher-order ordinary error bound, and convergence to a point of a nonisolated zero set. A stronger direct normal argument is retained for the same class. Scoped forward and reverse examples establish complementarity, rather than dominance, with quadratic, anchored, and partial PPA certificates.

### Locked scope and notation

We work in a finite-dimensional Euclidean space \(X\), with a fixed stepsize \(\lambda>0\), a set-valued operator \(F:X\rightrightarrows X\), and a nonempty closed target set \(S\subset F^{-1}(0)\). The symbol \(q\) is reserved for the error-bound exponent; normal Minty inputs are denoted by \(\xi_N\); \(d_D=\operatorname{dist}(f,D)\) is a yield-set gap; \(\delta\) is an RL pair-distance scale; and \(r\) is a state-distance radius. “Independent certificates” means independently verifiable mathematical inputs, not probabilistic independence.

---
## 1. Introduction

Local convergence results for the proximal point algorithm often combine two logically different ingredients: a geometric condition on the operator or its resolvent, and a regularity estimate relating the residual to the solution set. In applications, however, these ingredients are rarely available in the same native form. One may know a Jacobian enclosure, a coderivative estimate, a normal-cone representation, or an active-set inverse on the geometric side, while a slope inequality, residual growth estimate, Hoffman bound, or higher-order subregularity estimate is available on the regularity side. The practical question is therefore not whether one universal differential test can recover every assumption, but whether independently produced certificates can be placed on the same proximal transition with compatible domains, selections, exponents, and constants.

We study this question for the graph condition
\[
\|(u-v)-\lambda(u^*-v^*)\|
\le L\|(u-v)+\lambda(u^*-v^*)\|^\gamma,
\qquad 0<\gamma\le1,
\tag{1.1}
\]
called RL on a specified graph patch. When \(\gamma=1\), (1.1) is a balanced quadratic semimonotonicity slice and includes the familiar monotone and Luke–Tam geometries after normalization. For \(0<\gamma<1\), the reflected localized resolvent may be genuinely non-Lipschitz. The latter assertion is not inferred from the mere existence of a subunit Hölder upper bound: throughout, “genuine” means that the reflected Minty map is not locally Lipschitz, and a best power exponent requires a separate matching lower-bound argument.

The central quantitative observation is that RL supplies a step bound that is stronger, for the present purpose, than using its energy inequality alone. If \(d=d(x,S)\), \(x^+\in J_{\lambda F}(x)\), and \(s=\|x-x^+\|\), then solution comparison gives
\[
s\le \frac{d+Ld^\gamma}{2}.
\tag{1.2}
\]
Combining (1.2) with an independently verified ordinary set-distance error bound
\[
d(y,S)\le K\,d(0,F(y))^q
\tag{1.3}
\]
at the actual output \(y=x^+\) yields
\[
d(x^+,S)\le
K\left(\frac{d+Ld^\gamma}{2\lambda}\right)^q.
\tag{1.4}
\]
Thus the nonlinear critical relation is \(\gamma q=1\), with strict critical margin \(K(L/(2\lambda))^q<1\). The constant \(2\) is sharp for the specified uniform asymptotic certificate: an explicit multivalued shear family attains the boundary. This does not make (1.4) a necessary condition for the algorithm, nor does it identify the optimal rate of every operator.

The paper develops four connected results. First, it formulates (1.4) on an allowed-transition set and closes the otherwise missing coverage, localization, finite-length, and point-convergence steps. Second, it separates the asymptotically sharp critical condition from the positive-radius constants needed in an actual theorem. Third, it derives RL and higher-order ordinary subregularity independently for a load-dependent support-function/normal-cone inclusion, including all active faces, a nonisolated zero set, and a genuine Hölder reflected resolvent. Fourth, it compares the resulting certificate with finite full-neighborhood quadratic and anchored tests in both directions. The comparison is deliberately limited: a tangentially degenerate normal/partial argument proves convergence of the same natural class under weaker parameter restrictions, while a reverse Minty-collision example satisfies anchored and partial properties but violates every all-pairs RL condition.

The main contribution is consequently not a new name for Hölder continuity, higher-order subregularity, or their logical conjunction. It is the proof-bearing quantitative interface, its attainable critical constant and positive-radius form, and a cross-active-set structural instance showing exactly what information each side consumes. Existing semimonotonicity, inverse, slope, coderivative, and partial-regularity tools remain legitimate certificate producers whenever their native quantifiers and constants match the proximal transition considered here.


---

## 2. Geometry and certificate scopes

Throughout, \(X\) is a finite-dimensional Euclidean space, \(F:X\rightrightarrows X\) is a possibly set-valued operator, and \(\lambda>0\) is fixed. Let \(S\subset F^{-1}(0)\) be nonempty and closed. We write
\[
d(x,S)=\inf_{p\in S}\|x-p\|,
\qquad
P_S(x)=\{p\in S:\|x-p\|=d(x,S)\}.
\tag{2.1}
\]
The projection set is nonempty, but it need not be a singleton. Unless stated otherwise, all distances and residuals use the same Euclidean norm. The target \(S\) need not be an isolated zero or the entire zero set; it must, however, remain the same target in every certificate used below.

### 2.1. Graph patches and admissible proximal transitions

A proximal point transition is a triple satisfying
\[
x=y+\lambda v,\qquad v\in F(y).
\tag{2.2}
\]
Its next iterate is \(y\), and its selected operator value is necessarily \(v=(x-y)/\lambda\). To record localizations and branch restrictions explicitly, fix an admissible transition set
\[
\mathcal A\subset
\{(x,y,v)\in X^3:x=y+\lambda v,\ v\in F(y)\},
\qquad
\mathcal A(x)=\{(y,v):(x,y,v)\in\mathcal A\}.
\tag{2.3}
\]
A conclusion for every \((y,v)\in\mathcal A(x)\) concerns every admissible choice, not necessarily every choice from the unrestricted resolvent \((I+\lambda F)^{-1}(x)\). In particular, proving a property of one selected branch does not prove it for the full resolvent.

For a nonempty graph patch \(\Gamma\subset\operatorname{gph}F\), introduce the coupled Minty coordinates
\[
M_+(u,v)=u+\lambda v,
\qquad
M_-(u,v)=u-\lambda v,
\qquad
D_\Gamma=M_+(\Gamma).
\tag{2.4}
\]
Here the same graph point \((u,v)\) is used in both coordinates. We say that \(\Gamma\) satisfies the all-pairs reflected Hölder condition, abbreviated AP-RL\((\gamma,L)\), if
\[
\|(u-u')-\lambda(v-v')\|
\le L\|(u-u')+\lambda(v-v')\|^\gamma
\quad
\text{for every }(u,v),(u',v')\in\Gamma,
\tag{2.5}
\]
where \(0<\gamma\le1\) and \(0\le L<\infty\).

**Lemma 2.1 (coupled Minty chart).** Condition (2.5) holds if and only if \(M_+|_\Gamma\) is injective and
\[
Q_\Gamma=M_-\circ(M_+|_\Gamma)^{-1}:D_\Gamma\to X
\tag{2.6}
\]
is \((\gamma,L)\)-Hölder. In that case the localized resolvent defined by the graph patch is the single-valued map
\[
J_\Gamma(x)=\frac{x+Q_\Gamma(x)}2,
\qquad x\in D_\Gamma.
\tag{2.7}
\]

*Proof.* Suppose (2.5) holds. If two graph points have the same \(M_+\)-coordinate, (2.5) gives equality of their \(M_-\)-coordinates. Adding and subtracting the two coordinate equalities, and using \(\lambda>0\), shows that both components of the graph points coincide. Thus \(M_+|_\Gamma\) is injective. Applying (2.5) to its inverse images yields the stated Hölder inequality for \(Q_\Gamma\). Conversely, injectivity makes those inverse images well defined, and the Hölder inequality for \(Q_\Gamma\), evaluated at \(M_+(u,v)\) and \(M_+(u',v')\), is exactly (2.5). Formula (2.7) follows from \(M_+(u,v)+M_-(u,v)=2u\). \(\square\)

Lemma 2.1 gives uniqueness within the specified graph patch, but it gives no input coverage. The separate statement \(V\subset D_\Gamma\) is required to define \(J_\Gamma\) throughout an input neighborhood \(V\). For example, given neighborhoods \(U,V\subset X\), the patch
\[
\Gamma_{U,V}
=\{(u,v)\in\operatorname{gph}F:u\in U,\ u+\lambda v\in V\}
\tag{2.8}
\]
defines a full localized inverse on \(V\) only when every input in \(V\) is represented and that representation is unique within this entire patch. This assertion does not exclude additional resolvent values outside \(U\). Any claim about unrestricted selections must account for them separately.

The coupling in (2.6) is also essential. For a set-valued \(F\), the ordinary relation composition \((I-\lambda F)\circ(I+\lambda F)^{-1}\) can choose a new operator value after finding the state \(u\); it therefore need not represent \(Q_\Gamma\). Likewise, separate estimates within individual active branches do not establish (2.5) between different branches.

### 2.2. Solution comparisons and genuinely nonlinear geometry

The convergence theorem will use only a solution-comparison consequence of AP-RL. For an admissible transition \((x,y,v)\), this consequence has the form
\[
\|(y-p)-\lambda v\|
\le Ld(x,S)^\gamma
\quad\text{for some }p\in P_S(x).
\tag{2.9}
\]
Indeed, if \((y,v),(p,0)\in\Gamma\), then the right-hand increment in (2.5) is \(y+\lambda v-p=x-p\), whose norm is \(d(x,S)\). AP-RL therefore implies (2.9) whenever the relevant solution graph point belongs to the controlled patch. The converse is not asserted.

The following quantifier distinctions will be maintained throughout.

| Scope | Comparison required | Scope of a valid conclusion |
| --- | --- | --- |
| All-pairs graph geometry | Every pair of graph points in \(\Gamma\) | A coupled reflected chart on \(D_\Gamma\); coverage remains separate. |
| Moving-projection solution comparison | For every admissible transition, at least one \(p\in P_S(x)\) satisfies the comparison | The set-distance and step estimates used in Theorem 3.1. |
| Fixed-solution comparison | Each relevant transition is compared with one fixed \(\bar p\in S\) | A bound in terms of \(\|x-\bar p\|\), not automatically \(d(x,S)\). |
| Along-trajectory comparison | The comparison is known only on one specified sequence of transitions | An estimate for that sequence; no general coverage or arbitrary-selection statement. |

A subunit Hölder exponent alone is not evidence of genuinely nonlinear behavior. On a bounded input domain of diameter at most \(\delta\), a Lipschitz map with constant \(C\) is also \(\gamma\)-Hölder with constant \(C\delta^{1-\gamma}\) for every \(0<\gamma<1\). We call the reflected geometry *genuinely non-Lipschitz at an input* if \(Q_\Gamma\) is not Lipschitz on any relative neighborhood of that input. A stronger, power-order property is that
\[
\alpha_*=
\sup\bigl\{\theta\in(0,1]:
Q_\Gamma\text{ is }\theta\text{-Hölder on some relative neighborhood}
\bigr\}<1,
\tag{2.10}
\]
whenever the displayed set is nonempty. To identify a sharp exponent \(\alpha\), one must establish an \(\alpha\)-Hölder upper bound and exclude every larger exponent by a matching obstruction. A verifier producing only an upper bound does not establish this property.

Pairwise input scales and distances to the solution set are different quantities. If an AP-RL estimate is known for Minty input pairs separated by at most \(\delta\), it applies to the pair \(x,p\) in (2.9) when \(d(x,S)\le\delta\), provided both associated graph points are covered. An all-pairs assertion on an input ball of radius \(r\), by contrast, must allow pair separations up to \(2r\).

### 2.3. Ordinary error bounds and certificate matching

Define the operator residual by
\[
r_F(y)=\operatorname{dist}(0,F(y))
=\inf_{w\in F(y)}\|w\|,
\qquad y\in\operatorname{dom}F.
\tag{2.11}
\]
An ordinary order-\(q\) set-distance error bound on an output set \(E\) is
\[
d(y,S)\le K r_F(y)^q
\quad\text{for every }y\in E\cap\operatorname{dom}F,
\qquad q>0,\quad K>0.
\tag{2.12}
\]
When \(S\) agrees locally with \(F^{-1}(0)\), this is ordinary order-\(q\) metric subregularity at the zero value, with the exponent convention fixed explicitly by (2.12). It permits nonisolated zero sets. A strong bound replacing \(d(y,S)\) by \(\|y-\bar p\|\) is a different assertion: if valid throughout a neighborhood, it forces every zero in that neighborhood to equal \(\bar p\).

More generally, we may use
\[
d(y,S)\le\psi(r_F(y)),
\tag{2.13}
\]
where \(\psi\) is nondecreasing and \(\psi(0)=0\). If \(v\in F(y)\), then \(r_F(y)\le\|v\|\), so (2.13) implies
\[
d(y,S)\le\psi(\|v\|).
\tag{2.14}
\]
No minimum-norm selection is required. Conversely, a bound checked only for the values admitted by \(\mathcal A\) is a transition-level certificate and is not automatically the ordinary error bound (2.13) on a full output neighborhood.

The reflected-geometry and error-bound certificates may be established from different information and by different arguments. Their combination requires agreement on the operator, target set, norm, proximal parameter, graph or selection scope, and effective input and output domains. A certificate expressed in a different residual or metric must first be converted with quantitative constants in the correct direction. Constants available only asymptotically must be replaced by valid constants on a positive common radius before applying a finite-radius conclusion.

## 3. Independent certificates and local trajectories

We first state the interface using general nondecreasing gauges. This separates the one-step algebra from the additional assumptions needed to construct a complete local trajectory.

**Theorem 3.1 (independent certificates and finite-length trajectories).** Let \(X,F,S,\lambda\), and \(\mathcal A\) be as in Section 2. Let \(V\subset X\) be open, let \(\eta>0\), and suppose
\[
\mathcal A(x)\ne\varnothing
\quad\text{for every }x\in V\text{ with }d(x,S)<\eta.
\tag{3.1}
\]
Let \(\omega:[0,\eta)\to[0,\infty)\) and \(\psi:[0,\infty)\to[0,\infty)\) be nondecreasing, with \(\omega(0)=\psi(0)=0\). Assume that for every input \(x\) covered by (3.1) and every \((y,v)\in\mathcal A(x)\), there exists \(p=p(x,y,v)\in P_S(x)\) such that
\[
\|(y-p)-\lambda v\|\le\omega(d(x,S)),
\qquad
d(y,S)\le\psi(\|v\|).
\tag{3.2}
\]
Define, for \(0\le t<\eta\),
\[
B(t)=\frac{t+\omega(t)}2,
\qquad
E(t)=\frac{t^2+\omega(t)^2}2,
\qquad
\Phi(t)=\psi\!\left(\frac{B(t)}\lambda\right).
\tag{3.3}
\]
Then every such transition, with \(d=d(x,S)\), \(d_+=d(y,S)\), and \(s=\|x-y\|\), satisfies
\[
s\le B(d),
\qquad
d_+\le\min\{B(d),\Phi(d)\},
\qquad
d_+^2+s^2\le E(d).
\tag{3.4}
\]

For the trajectory conclusion, suppose that there exist \(0<r<\eta\) and \(0<\kappa<1\) such that
\[
d(y,S)\le\kappa d(x,S)
\quad
\begin{array}{l}
\text{for every }x\in V\text{ with }d(x,S)\le r,\\
\text{and every }(y,v)\in\mathcal A(x).
\end{array}
\tag{3.5}
\]
Condition (3.5) follows, in particular, if \(\Phi(t)\le\kappa t\) for all \(0\le t\le r\), but it may instead come from a stronger independent estimate. For an initial point \(x^0\in V\), put \(d_0=d(x^0,S)\), and assume
\[
d_0\le r,
\qquad
H(d_0):=\sum_{j=0}^{\infty}B(\kappa^j d_0)<\infty,
\qquad
\operatorname{dist}(x^0,X\setminus V)>H(d_0).
\tag{3.6}
\]
We use \(\operatorname{dist}(x,\varnothing)=+\infty\) when \(V=X\). Then every successive admissible choice
\[
(x^{k+1},v^k)\in\mathcal A(x^k),\qquad k=0,1,\ldots,
\tag{3.7}
\]
can be continued indefinitely. The resulting trajectory stays in \(V\), has finite length, and converges to a point \(x^\infty\in S\). More precisely,
\[
\begin{aligned}
d(x^k,S)&\le\kappa^k d_0,\\
\|x^{k+1}-x^k\|&\le B(\kappa^k d_0),\\
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|&\le H(d_0),\\
\|x^k-x^\infty\|&\le\sum_{j=k}^{\infty}B(\kappa^j d_0).
\end{aligned}
\tag{3.8}
\]

*Proof.* Fix an admissible transition and a projection point supplied by (3.2). Set \(a=y-p\) and \(b=\lambda v=x-y\). Then \(a+b=x-p\), so \(\|a+b\|=d\), whereas \(\|a-b\|\le\omega(d)\). Consequently,
\[
2\|b\|\le\|a+b\|+\|a-b\|\le d+\omega(d),
\qquad
2\|a\|\le d+\omega(d).
\tag{3.9}
\]
The first inequality gives \(s\le B(d)\). Since \(p\in S\), the second gives \(d_+\le\|a\|\le B(d)\). By the parallelogram identity,
\[
d_+^2+s^2
\le\|a\|^2+\|b\|^2
=\frac{\|a+b\|^2+\|a-b\|^2}{2}
\le E(d).
\tag{3.10}
\]
Finally, the second certificate in (3.2), the equality \(\|v\|=s/\lambda\), and monotonicity of \(\psi\) imply
\[
d_+\le\psi(s/\lambda)
\le\psi(B(d)/\lambda)=\Phi(d).
\tag{3.11}
\]
This proves (3.4).

We next construct and control the trajectory without presupposing that future inputs stay in \(V\). Let \(m=\operatorname{dist}(x^0,X\setminus V)\). At the initial input, \(d_0\le r<\eta\), so (3.1) provides at least one admissible transition. Suppose a finite admissible prefix has been constructed through \(x^k\), and that \(x^i\in V\) and \(d(x^i,S)\le\kappa^i d_0\) for \(0\le i\le k\). Coverage (3.1) supplies a next transition at \(x^k\). Every such choice obeys (3.5) and (3.4). Because \(B\) is nondecreasing,
\[
d(x^{k+1},S)\le\kappa^{k+1}d_0\le r,
\qquad
\|x^{k+1}-x^k\|\le B(\kappa^k d_0).
\tag{3.12}
\]
The accumulated step bound then yields
\[
\|x^{k+1}-x^0\|
\le\sum_{j=0}^{k}B(\kappa^j d_0)
\le H(d_0)<m.
\tag{3.13}
\]
Thus \(x^{k+1}\notin X\setminus V\), and the next input lies in \(V\). Its distance is still less than \(\eta\), so coverage can be invoked again. This closes the induction for every admissible choice.

Summing the step bounds proves finite length. Their summable tails make \((x^k)\) Cauchy, and completeness of \(X\) gives a limit \(x^\infty\). Since the distance to a closed set is continuous,
\[
d(x^\infty,S)=\lim_{k\to\infty}d(x^k,S)=0,
\]
and hence \(x^\infty\in S\). Taking a limit in the finite tail bounds gives the last line of (3.8). If \(d_0=0\), (3.4) gives zero step length at every iteration, so the same conclusions hold for the stationary trajectory. \(\square\)

Neither all-pairs RL nor a common source for the two certificates is required by Theorem 3.1. AP-RL is one sufficient way to produce its first certificate, under the graph-scope conditions of Section 2. The theorem also does not infer resolvent existence from reflected geometry: existence is precisely the separate coverage assumption (3.1). Closedness of the chosen target \(S\), rather than an unstated closed-graph assumption on \(F\), justifies membership of the limit in \(S\).

If the error-bound gauge is available only on \([0,\zeta)\), the theorem applies after restricting the distance range so that
\[
B(r)/\lambda<\zeta.
\tag{3.14}
\]
For the one-step statement at a given distance, the corresponding requirement is \(B(d)/\lambda<\zeta\). Any output localization of the error bound must also contain the outputs of all admissible transitions under consideration. The inequalities in (3.4) are consequences of the geometric certificate, not an asserted equivalent reformulation of it.

### 3.1. Power certificates and positive radii

**Corollary 3.2 (power compatibility).** Under the one-step hypotheses of Theorem 3.1, suppose
\[
\omega(t)=Lt^\gamma,
\qquad
\psi(s)=Ks^q,
\qquad
0<\gamma<1,\quad L>0,\quad q>0,\quad K>0.
\tag{3.15}
\]
Then every admissible transition satisfies
\[
d_+
\le K\left(\frac{d+Ld^\gamma}{2\lambda}\right)^q
=\frac{K}{(2\lambda)^q}
d^{\gamma q}(d^{1-\gamma}+L)^q.
\tag{3.16}
\]
For \(\gamma q\ge1\), define at each positive radius \(r<\eta\)
\[
\beta(r)=\frac{K}{(2\lambda)^q}
r^{\gamma q-1}(r^{1-\gamma}+L)^q.
\tag{3.17}
\]
If \(\beta(r)<1\), every admissible transition from an input with \(d\le r\) satisfies \(d_+\le\kappa d\), with \(\kappa=\beta(r)\). The following cases hold.

1. If \(\gamma q>1\), such positive radii exist. Moreover, on every fixed valid radius,
   \[
   d_+\le C_r d^{\gamma q},
   \qquad
   C_r=\frac{K}{(2\lambda)^q}(r^{1-\gamma}+L)^q.
   \tag{3.18}
   \]
   Thus any complete trajectory supplied by Theorem 3.1 either reaches \(S\) in finitely many steps or has Q-superlinear convergence of its distance to \(S\), with the order bound (3.18).

2. If \(\gamma q=1\), the existence of a positive radius with \(\beta(r)<1\) is equivalent to
   \[
   \kappa_0:=K\left(\frac{L}{2\lambda}\right)^q<1.
   \tag{3.19}
   \]
   More explicitly, any common valid radius satisfying
   \[
   0<r<\eta,
   \qquad
   r^{1-\gamma}<2\lambda K^{-1/q}-L
   \tag{3.20}
   \]
   has \(\beta(r)<1\). The finite-radius factor is \(\beta(r)\), not the limiting value \(\kappa_0\).

3. If \(\gamma q<1\), the right-hand side of (3.16), divided by \(d\), tends to \(+\infty\) as \(d\downarrow0\). Therefore this composed upper bound does not certify a uniform strict contraction on any neighborhood of the target. It makes no assertion of divergence and does not exclude stronger certificates for the same operator.

Whenever a strict factor \(0<\kappa<1\) is certified on \([0,r]\), the summability budget in Theorem 3.1 is explicit:
\[
H(t)=\frac12\left(
\frac{t}{1-\kappa}
+\frac{Lt^\gamma}{1-\kappa^\gamma}
\right),\qquad 0\le t\le r.
\tag{3.21}
\]
Consequently, all its trajectory conclusions hold for every \(x^0\in V\) with \(d_0\le r\) and boundary margin greater than \(H(d_0)\). The pointwise tail estimate becomes
\[
\|x^k-x^\infty\|
\le\frac12\left(
\frac{\kappa^k d_0}{1-\kappa}
+\frac{L\kappa^{\gamma k}d_0^\gamma}{1-\kappa^\gamma}
\right).
\tag{3.22}
\]
In particular, \(\kappa\) is a certified Q-linear factor for the set distance, whereas (3.22) gives an R-linear bound for the point error with factor \(\kappa^\gamma\). It does not assert a Q-linear point-error factor.

*Proof.* Formula (3.16) is (3.11) with the gauges (3.15). For \(d>0\), its right-hand side divided by \(d\) is
\[
\frac{K}{(2\lambda)^q}
d^{\gamma q-1}(d^{1-\gamma}+L)^q.
\tag{3.23}
\]
When \(\gamma q\ge1\), this expression is nondecreasing in \(d\), giving the factor \(\beta(r)\) on \(0<d\le r\); at \(d=0\), the zero-step conclusion of Theorem 3.1 applies. If \(\gamma q>1\), expression (3.23) tends to zero, proving existence of a strict contraction radius. Bounding its last factor on \([0,r]\) gives (3.18). Along a nonterminating trajectory, division of (3.18) by \(d\), followed by \(d\to0\), proves the asserted Q-superlinear distance convergence.

If \(\gamma q=1\), (3.23) tends to \(\kappa_0\) and is strictly larger than \(\kappa_0\) at every positive distance. Solving \(\beta(r)<1\) gives exactly the second inequality in (3.20), whose right-hand side is positive if and only if (3.19) holds. This also shows why the critical equality \(\kappa_0=1\) does not produce a strict factor from (3.16). If \(\gamma q<1\), the negative power in (3.23) gives the stated divergence of this bound. Finally, summing \(B(\kappa^jt)=\tfrac12(\kappa^jt+L\kappa^{\gamma j}t^\gamma)\) proves (3.21), and summing from \(j=k\) proves (3.22). \(\square\)

The supercritical case also permits a directly computable, conservative radius. For a prescribed \(0<\kappa<1\), put \(a=\gamma q-1>0\). Any \(0<r<\eta\) satisfying
\[
r\le L^{1/(1-\gamma)},
\qquad
r\le\left(\frac{\kappa\lambda^q}{K L^q}\right)^{1/a}
\tag{3.24}
\]
has \(\beta(r)\le\kappa\). Indeed, the first inequality gives \(r^{1-\gamma}+L\le2L\), and the second controls the resulting bound \(\beta(r)\le K(L/\lambda)^q r^a\). All other graph, residual, and output-domain restrictions still apply. In either regime, an asymptotic modulus alone is not a substitute for valid constants and coverage at the selected radius.

### 3.2. The linear endpoint and the meaning of the coefficient

The case \(\gamma=1\) must retain both terms in \(B(d)=(1+L)d/2\). For the linear error bound \(d_+\le K\|v\|\), Theorem 3.1 gives the useful combined estimate
\[
d_+\le\widehat\kappa d,
\quad
\widehat\kappa=
\min\left\{
\sqrt{\frac{1+L^2}{2}}\,
\frac{K}{\sqrt{K^2+\lambda^2}},
\frac{K(1+L)}{2\lambda},
\frac{1+L}{2}
\right\}.
\tag{3.25}
\]
To verify the first term, combine \(d_+\le Ks/\lambda\) with
\(d_+^2+s^2\le(1+L^2)d^2/2\); the other two terms follow from the step and output bounds in (3.4). Whenever \(\widehat\kappa<1\), this factor can be used in the trajectory part of Theorem 3.1, with \(H(t)=(1+L)t/[2(1-\widehat\kappa)]\). Formula (3.25) is a certified bound, not a claim of the optimal rate for a given operator.

For \(0<\gamma<1\), the denominator \(2\lambda\) in (3.16) comes from the full step estimate (3.9); retaining only the energy inequality would discard this information. Corollary 3.2 establishes a sufficient compatibility test for the specified certificate data. It does not make that test necessary for actual convergence. The attainability question for its critical coefficient is addressed separately in Proposition 3.4.

---

### 3.3. Exact scalar relaxation

To describe exactly what is retained by a scalar reduction, take

\[
\omega(d)=Ld^\gamma,\qquad 0<\gamma<1,\quad L>0,
\]

and write
\[
A(d)=\frac{d^2+L^2d^{2\gamma}}2,
\qquad
B(d)=\frac{d+Ld^\gamma}2.
\] Retain the energy inequality, both individual \(B\)-bounds, and the error bound, but discard all remaining geometry. Their scalar envelope is

\[
\widehat R(d)
=\sup_{0\le t\le B(d)/\lambda}
\min\left\{B(d),\psi(t),\sqrt{A(d)-\lambda^2t^2}\right\}.
\tag{3.26}
\]

Here \(t=s/\lambda\) is the norm of the chosen output, not necessarily the minimal residual. In particular, (3.26) does not retain the reverse-triangle constraint \(|d-d_+|\le s\), and it does not enforce realizability by vectors or by an operator graph. Nevertheless, every allowed transition satisfies \(d_+\le\widehat R(d)\).

**Theorem 3.3 (exact nonlinear scalar asymptotics).** Suppose \(\psi:[0,\infty)\to[0,\infty)\) is nondecreasing, \(\psi(0)=0\), and \(\psi(t)\to0\) as \(t\downarrow0\). Set

\[
C_\gamma=\limsup_{t\downarrow0}\frac{\psi(t)}{t^{1/\gamma}}\in[0,\infty].
\]

Then, in the extended real sense,

\[
\boxed{\displaystyle
\limsup_{d\downarrow0}\frac{\widehat R(d)}{d}
=C_\gamma\left(\frac{L}{2\lambda}\right)^{1/\gamma}.}
\tag{3.27}
\]

*Proof.* First observe that

\[
A(d)-B(d)^2=\frac{(Ld^\gamma-d)^2}{4}\ge0,
\tag{3.28}
\]

so the square root in (3.26) is defined throughout its optimization interval. Monotonicity of \(\psi\) gives the upper bound

\[
\widehat R(d)\le\psi\!\left(\frac{B(d)}{\lambda}\right).
\tag{3.29}
\]

For the lower bound, use the endpoint \(t_d=B(d)/\lambda\):

\[
\frac{\widehat R(d)}{d}
\ge\min\left\{
\frac{B(d)}{d},
\frac{\psi(t_d)}{d},
\frac{|Ld^\gamma-d|}{2d}
\right\}.
\tag{3.30}
\]

Because \(0<\gamma<1\), the first and third quantities on the right tend to \(+\infty\). Furthermore,

\[
\frac{t_d^{1/\gamma}}{d}
=\left(\frac{d^{1-\gamma}+L}{2\lambda}\right)^{1/\gamma}
\longrightarrow\left(\frac{L}{2\lambda}\right)^{1/\gamma}.
\tag{3.31}
\]

The map \(d\mapsto t_d\) is continuous and strictly increasing from a small positive \(d\)-interval onto a small positive \(t\)-interval. Consequently,

\[
\limsup_{d\downarrow0}\frac{\psi(t_d)}{d}
=C_\gamma\left(\frac{L}{2\lambda}\right)^{1/\gamma}.
\]

If this limsup is finite, a realizing sequence combined with (3.30) gives the matching lower bound. If it is infinite, choose a sequence on which \(\psi(t_d)/d\to\infty\); all three terms in (3.30) then tend to infinity. The zero case follows directly from (3.29). No continuity of \(\psi\) away from zero is used. \(\square\)

The adjective *exact* in Theorem 3.3 refers to the scalar relaxation (3.26), not to the best convergence factor of every operator with these parameters. Retaining only energy and the error bound would instead produce the asymptotic coefficient \(C_\gamma(L/(\sqrt2\lambda))^{1/\gamma}\). Thus the step constraint genuinely strengthens the scalar conclusion.


### 3.4. A two-branch family attaining the asymptotic constant

**Proposition 3.4 (attainability and non-improvability of 2).** Fix once and for all \(\lambda_0>0\), \(0<\alpha<1\), \(b,c>0\), and a unit vector \(e\in\mathbb R^m\). Define an operator \(F_{\lambda_0}:\mathbb R^m\times\mathbb R\rightrightarrows\mathbb R^m\times\mathbb R\) by

\[
F_{\lambda_0}(t,y)=
\left\{
\left(-by^\alpha e,\frac{c-1}{\lambda_0}y\right),
\left(-by^\alpha e,-\frac{c+1}{\lambda_0}y\right)
\right\},\qquad y\ge0,
\tag{3.32}
\]

and \(F_{\lambda_0}(t,y)=\varnothing\) for \(y<0\). Apply the proximal algorithm with step size exactly \(\lambda_0\). Then the following statements hold.

**(i) Closed graph, genuine multivaluedness, and full input coverage.** The two branches are continuous on the closed half-space, so their finite union has closed graph. For \(y>0\) their normal outputs differ by \(2cy/\lambda_0>0\); hence the operator is genuinely two-valued. Its zero set is

\[
S=\mathbb R^m\times\{0\}.
\]

The two Minty input branches are

\[
(p,\xi_N)=\bigl(t-\lambda_0by^\alpha e,cy\bigr)
\quad\text{and}\quad
(p,\xi_N)=\bigl(t-\lambda_0by^\alpha e,-cy\bigr).
\tag{3.33}
\]

Every input \((p,\xi_N)\) therefore has the unique recovered base point

\[
J(p,\xi_N):=(I+\lambda_0F_{\lambda_0})^{-1}(p,\xi_N)
=\left(p+\lambda_0bc^{-\alpha}|\xi_N|^\alpha e,\frac{|\xi_N|}{c}\right).
\tag{3.34}
\]

At \(\xi_N=0\) the branch labels meet at the same graph point, so there is no collision of distinct graph points. This is an explicit all-branch coverage argument, not a branchwise regularity argument with coverage left implicit.

**(ii) Exact nonlinear order and limiting RL modulus.** The reflected map is

\[
Q(p,\xi_N)=2J(p,\xi_N)-(p,\xi_N)
=\left(p+2\lambda_0bc^{-\alpha}|\xi_N|^\alpha e,
\frac{2|\xi_N|}{c}-\xi_N\right).
\tag{3.35}
\]

The inequality

\[
\bigl||\xi_N|^\alpha-|\xi_N'|^\alpha\bigr|\le|\xi_N-\xi_N'|^\alpha
\]

and the \((1+2/c)\)-Lipschitz property of
\((p,\xi_N)\mapsto(p,2|\xi_N|/c-\xi_N)\) imply, whenever \(\|x-x'\|\le\delta\),

\[
\|Q(x)-Q(x')\|
\le L_\delta\|x-x'\|^\alpha,
\qquad
L_\delta=L_0+(1+2/c)\delta^{1-\alpha},
\tag{3.36}
\]

where

\[
L_0=2\lambda_0bc^{-\alpha}.
\tag{3.37}
\]

These estimates include opposite-sign inputs and therefore all cross-branch comparisons. Conversely, for \(h>0\),

\[
\frac{\|Q(p,h)-Q(p,0)\|}{h^\alpha}
=\sqrt{L_0^2+(2/c-1)^2h^{2-2\alpha}}
\longrightarrow L_0.
\tag{3.38}
\]

Thus \(L_0\) is the limiting smallest local all-pairs \(\alpha\)-Hölder modulus at every solution input. For any \(\theta>\alpha\), the tangential difference in (3.38), divided by \(h^\theta\), diverges. The best local Hölder exponent at a solution is therefore exactly \(\alpha\), rather than an artificially weakened Lipschitz estimate.

**(iii) Exact critical residual order.** Because \(|c-1|\le c+1\), the minimal residual is

\[
r_F(t,y)
=\sqrt{b^2y^{2\alpha}+\left(\frac{c-1}{\lambda_0}\right)^2y^2}
\ge by^\alpha.
\tag{3.39}
\]

Consequently,

\[
d((t,y),S)=y\le b^{-1/\alpha}r_F(t,y)^{1/\alpha}.
\tag{3.40}
\]

Moreover, \(r_F(t,y)/y^\alpha\to b\), and hence

\[
\frac{y}{r_F(t,y)^{1/\alpha}}\longrightarrow b^{-1/\alpha}.
\]

Thus \(b\) is the optimal asymptotic lower coefficient at order \(\alpha\), and \(K_0=b^{-1/\alpha}\) is the optimal asymptotic error-bound coefficient at exponent \(1/\alpha\). No larger error-bound exponent can hold on a neighborhood containing positive \(y\), since for \(q>1/\alpha\) the quotient \(y/r_F(t,y)^q\) diverges.

**(iv) Exact dynamics and attainable compatibility.** Formula (3.34) gives, for every input,

\[
d(J(p,\xi_N),S)=\frac1c\,d((p,\xi_N),S).
\tag{3.41}
\]

The critical asymptotic factor computed from the optimal limiting data is exactly

\[
K_0\left(\frac{L_0}{2\lambda_0}\right)^{1/\alpha}
=b^{-1/\alpha}\bigl(bc^{-\alpha}\bigr)^{1/\alpha}
=\frac1c.
\tag{3.42}
\]

The constant is therefore attainable by a closed-graph, genuinely two-valued operator with a nonisolated zero set. More precisely, if the genuine positive-radius constants \(L_\delta\) in (3.36) are used in (3.26), with \(\gamma=\alpha\), \(\lambda=\lambda_0\), and \(\psi(s)=b^{-1/\alpha}s^{1/\alpha}\), then

\[
\lim_{\delta\downarrow0}\limsup_{d\downarrow0}
\frac{\widehat R_{L_\delta}(d)}{d}
=\frac1c,
\tag{3.43}
\]

which equals the actual factor. Equation (3.43) makes the order of localization and asymptotic limits explicit; it does not claim that \(L_0\) is already a valid constant on a prescribed positive-radius neighborhood.

For \(c>1\), positive-radius compatibility is obtained by taking

\[
0<\delta<
\left[
\frac{2\lambda_0b(1-c^{-\alpha})}{1+2/c}
\right]^{1/(1-\alpha)}.
\tag{3.44}
\]

Then \(L_\delta<2\lambda_0b\). With this fixed verified constant, choose a positive distance radius \(r\) inside the same local domain such that

\[
r^{1-\alpha}+L_\delta<2\lambda_0b.
\tag{3.45}
\]

The power transfer certifies the factor

\[
\beta(r)=\left(\frac{r^{1-\alpha}+L_\delta}{2\lambda_0b}\right)^{1/\alpha}<1.
\tag{3.46}
\]

When (3.36) is invoked only for pairs at distance at most \(\delta\), also require \(r\le\delta\), so each input–projection pair is covered. A whole-orbit conclusion uses the coverage and displacement budget from Theorem 3.1; for this family coverage is global, and (3.41) independently gives the exact dynamics.

To see why 2 cannot be increased in a uniform critical certificate of the form \(K(L/(D\lambda))^{1/\alpha}<1\), take \(c=1\). Then \(L_0=2\lambda_0b\), yet (3.41) gives \(d_+=d\) for every nonsolution input. Every \(D>2\) would incorrectly certify this member using its limiting data. The defect persists with a true positive-radius constant: here \(L_\delta=2\lambda_0b+3\delta^{1-\alpha}\), and a sufficiently small \(\delta>0\) satisfies \(L_\delta<D\lambda_0b\). The false conclusion is therefore not attributable to replacing a positive-radius modulus by its limit. The coefficient 2 is non-improvable in this uniform asymptotic compatibility law. This statement neither makes the scalar relaxation operator-exact in general nor asserts that the strict condition is necessary for every operator. \(\square\)

**Step-size convention.** The subscript in \(F_{\lambda_0}\) is essential: the operator in (3.32) is fixed first, and the calculation uses algorithmic step size \(\lambda_0\). If the algorithmic step size is changed to \(\tau\), the operator is not redefined. Its normal Minty coefficients become

\[
1+\frac{\tau(c-1)}{\lambda_0}
\quad\text{and}\quad
1-\frac{\tau(c+1)}{\lambda_0},
\]

so coverage, injectivity, and the resolvent formula require fresh analysis. In particular, (3.34) and (3.41) are not step-size optimization formulas for a fixed operator.

**Set-distance and point rates.** For \(c>1\), let \(x^k=(t_k,y_k)\) with \(y_0\ge0\). Then

\[
y_k=c^{-k}y_0,\qquad
t_{k+1}-t_k=\lambda_0b\,y_{k+1}^\alpha e.
\]

Summing the geometric series yields

\[
t_\infty-t_k
=\frac{\lambda_0b\,y_0^\alpha}{c^\alpha-1}
c^{-\alpha k}e.
\tag{3.47}
\]

Thus the set-distance Q-factor is exactly \(c^{-1}\), while the nonzero tangential tail has factor \(c^{-\alpha}\). For a general orbit the step-sum argument supplies an R-linear point-error bound, not an automatic pointwise Q-factor equal to the set-distance factor.

### 3.5. Actual contraction without a compatible uniform scalar certificate

The preceding attainability result does not make power matching a necessary condition for convergence. The next example separates geometric irregularity, minimal-residual growth, and the actual normal dynamics.

**Proposition 3.5 (degenerate shear counterexample).** Fix \(0<\gamma<1\), \(b>0\), \(c>1\), and \(\lambda_0>0\). Define, for \(y\ge0\),

\[
G_{\lambda_0}(t,y)=
\left\{
\left(-b|t|y^\gamma,\frac{c-1}{\lambda_0}y\right),
\left(-b|t|y^\gamma,-\frac{c+1}{\lambda_0}y\right)
\right\},
\tag{3.48}
\]

and give it empty values for \(y<0\). This operator has closed graph, is two-valued for every \(y>0\), and has zero set \(S=\mathbb R\times\{0\}\). At algorithmic step size \(\lambda_0\), it has a locally single-valued resolvent with exact distance factor \(1/c\), but near \((0,0)\) its best all-pairs RL exponent is \(\gamma\), while no uniform error bound with exponent greater than 1 exists.

*Proof.* The normal Minty equation again gives \(y=|\xi_N|/c\). Put

\[
a(\xi_N)=\lambda_0b(|\xi_N|/c)^\gamma.
\]

When \(a(\xi_N)<1\), the tangential equation is \(p=t-a(\xi_N)|t|\). It is a continuous, strictly increasing bijection in \(t\), with slopes \(1+a(\xi_N)\) for \(t<0\) and \(1-a(\xi_N)\) for \(t>0\). Thus

\[
J_G(p,\xi_N)=
\left(
\frac{p}{1-\operatorname{sgn}(p)a(\xi_N)},\frac{|\xi_N|}{c}
\right),
\tag{3.49}
\]

where the first coordinate is zero when \(p=0\). In particular,

\[
d(J_G(p,\xi_N),S)=c^{-1}|\xi_N|=c^{-1}d((p,\xi_N),S).
\tag{3.50}
\]

For completeness, fix a box \(|p|\le P\), \(a(\xi_N)\le\eta<1\), and set \(f(p,a)=p/(1-\operatorname{sgn}(p)a)\). Its piecewise derivatives and continuity at \(p=0\) give

\[
|f(p,a)-f(p',a')|
\le\frac{|p-p'|}{1-\eta}
+\frac{P}{(1-\eta)^2}|a-a'|,
\tag{3.51}
\]

while

\[
|a(\xi_N)-a(\xi_N')|
\le\lambda_0bc^{-\gamma}|\xi_N-\xi_N'|^\gamma.
\]

The normal coordinate in (3.49) is Lipschitz. Therefore \(J_G\), and hence \(Q_G=2J_G-I\), is \(\gamma\)-Hölder on bounded input sets in this box. For example, for input differences at most \(\delta\), one valid reflected-map coefficient is

\[
L:=
\frac{2P\lambda_0bc^{-\gamma}}{(1-\eta)^2}
+\left[2\left((1-\eta)^{-1}+c^{-1}\right)+1\right]\delta^{1-\gamma}.
\tag{3.52}
\]

This intentionally conservative coefficient suffices for existence of a uniform local certificate.

Conversely, every open neighborhood of \((0,0)\) contains \((h,0)\) for some fixed \(h>0\). For all sufficiently small \(\xi_N>0\), the tangential reflected difference is

\[
\bigl[Q_G(h,\xi_N)-Q_G(h,0)\bigr]_t
=\frac{2h\,a(\xi_N)}{1-a(\xi_N)}
\sim2h\lambda_0bc^{-\gamma}\xi_N^\gamma.
\tag{3.53}
\]

Dividing by \(\xi_N^\theta\) proves failure of every full-neighborhood all-pairs Hölder estimate with \(\theta>\gamma\). Thus the irregularity is genuine even at the degenerate solution \((0,0)\); the proof uses nearby solution points, as is appropriate for a neighborhood all-pairs property.

On the other hand, along \(t=0\),

\[
r_G(0,y)=ky,\qquad k:=\frac{c-1}{\lambda_0}>0.
\tag{3.54}
\]

If a uniform error bound \(d((t,y),S)\le K r_G(t,y)^q\) held near \((0,0)\) with \(q>1\), then

\[
1\le Kk^q y^{q-1}
\]

would hold for all sufficiently small positive \(y\), a contradiction. In fact \(r_G(t,y)\ge ky\) everywhere on the domain, so a linear error bound does hold. No admissible full-neighborhood power pair can therefore satisfy \(\theta q\ge1\): necessarily \(\theta\le\gamma<1\) and \(q\le1\). The exact contraction (3.50) nevertheless persists. \(\square\)

This separation also applies to general gauges in the *uniform scalar composition* (3.11), not just to a selected power parametrization. Fix any full neighborhood of \((0,0)\), and choose the point \((h,0)\) used in (3.53) inside it. For the input \(x=(h,d)\), the nearest point in \(S\) is uniquely \(p=(h,0)\). The reflected solution-comparison vector is \(Q_G(h,d)-(h,0)\). Hence any uniform geometric gauge \(\omega\) valid for these transitions must obey, for sufficiently small \(d>0\),

\[
\omega(d)\ge2h\lambda_0bc^{-\gamma}d^\gamma.
\tag{3.55}
\]

For transitions whose output is \((0,y)\) on the positive normal branch, the input is \((0,cy)\) and the chosen output norm is \(ky\). Consequently any error-bound gauge \(\psi\) covering the same neighborhood must satisfy

\[
\psi(s)\ge s/k
\quad\text{for all sufficiently small }s>0.
\tag{3.56}
\]

If \(\omega(d)\to0\), (3.55)–(3.56) imply

\[
\frac{1}{d}\psi\!\left(\frac{d+\omega(d)}{2\lambda_0}\right)
\ge\frac{hb c^{-\gamma}}{k}\,d^{\gamma-1}
\longrightarrow+\infty.
\tag{3.57}
\]

If the nondecreasing gauge \(\omega\) has a positive right limit at zero, monotonicity of \(\psi\) and (3.56) instead give a positive lower bound on the composition, so it again cannot be bounded by \(\kappa d\). Thus no such uniform scalar composition certifies a fixed contraction on that neighborhood. For the stronger envelope (3.26), take \(\lambda=\lambda_0\) and any fixed valid positive \(\gamma\)-Hölder constant. At \(t_d=B(d)/\lambda_0\), (3.56) gives \(\psi(t_d)/d\ge B(d)/(k\lambda_0d)\to+\infty\). The two geometric terms in (3.30) also tend to infinity, so \(\widehat R(d)/d\to+\infty\). This argument does not require \(\psi(t)\to0\).

The obstruction is identifiable: the worst geometric shear is witnessed at a nonzero tangential coordinate, while the weakest residual growth is witnessed at \(t=0\). A uniform scalar aggregation combines these two pieces of information without retaining their different locations. Keeping the normal equation gives the exact factor \(1/c\) immediately. This counterexample does not rule out point-dependent gauges, blockwise estimates, or stronger native inequalities, and it does not claim absence of higher-order error bounds near solutions with \(t\ne0\).

Finally, contraction here does correspond to convergent local trajectories, not merely to a formal one-step calculation. Starting with \(y_0\ge0\) and \(a(y_0)<1\), the normal coordinates satisfy \(y_k=c^{-k}y_0\). The tangential sign is preserved and

\[
|t_{k+1}|=\frac{|t_k|}{1-\operatorname{sgn}(t_0)\lambda_0b\,y_{k+1}^\gamma}.
\]

Since \(\sum_{k\ge0}\lambda_0b\,y_{k+1}^\gamma<\infty\), these products have finite limits. More explicitly, if \(A=\lambda_0b y_0^\gamma\), \(r=c^{-\gamma}\), and \(Ar<1\), then for \(t_0>0\),

\[
0\le\log\frac{t_n}{t_0}
=\sum_{j=1}^n-\log(1-Ar^j)
\le\frac{Ar}{(1-r)(1-Ar)},
\]

using \(-\log(1-z)\le z/(1-z)\). For \(t_0<0\), the magnitude decreases and its product also converges; for \(t_0=0\) it stays zero. Therefore each sufficiently small initial point with \(y_0\ge0\) generates a convergent trajectory with exact set-distance Q-factor \(1/c\); the initial tangential coordinate can be chosen small enough that the displayed uniform bound keeps the entire trajectory inside a prescribed tangential box.

---

## 4. Independent verification modules

The two inputs to the convergence result are logically separate. A reflected-resolvent estimate is an upper bound on changes in the complete Minty inverse, whereas an error bound is a lower bound on the residual away from the zero set. The following elementary modules preserve this separation. All spaces in this section are finite-dimensional Euclidean spaces, and \(\lambda>0\) is fixed. For a set-valued map \(G\), write

\[
J_{\lambda G}=(I+\lambda G)^{-1},\qquad
Q_{\lambda G}=2J_{\lambda G}-I,\qquad
r_G(u)=\operatorname{dist}(0,G(u)).
\]

When the complete inverse is single-valued on its stated input domain, a bound
\(\|Q_{\lambda G}x-Q_{\lambda G}x'\|\le L\|x-x'\|^\gamma\)
is exactly the all-pairs RL inequality on the corresponding graph pairs. Indeed, if \(x=u+\lambda v\), \(v\in G(u)\), then \(Q_{\lambda G}x=u-\lambda v\). Existence and input coverage must therefore be established in addition to the modulus estimate.

### 4.1. A normal inverse with Hölder tangential feedback

**Proposition 4.1 (independent RL verifier).** Let \(A:\mathbb R^n\rightrightarrows\mathbb R^n\) have a complete, single-valued resolvent \(J_A=(I+\lambda A)^{-1}\) on \(\mathbb R^n\). Suppose that \(J_A\) is \(\eta\)-Lipschitz and \(2J_A-I\) is \(B_N\)-Lipschitz. Let \(h:\operatorname{ran}J_A\to\mathbb R^m\) satisfy

\[
\|h(z)-h(z')\|\le H\|z-z'\|^\alpha,
\qquad 0<\alpha<1.
\tag{4.1}
\]

Define

\[
G(t,z)=\{(-h(z),w):w\in A(z)\}.
\tag{4.2}
\]

Then its complete resolvent is single-valued on \(\mathbb R^{m+n}\) and equals

\[
J_{\lambda G}(p,v)=\bigl(p+\lambda h(J_Av),J_Av\bigr).
\tag{4.3}
\]

For every \(\delta>0\) and all inputs \(x,x'\) with \(\|x-x'\|\le\delta\), it satisfies

\[
\|Q_{\lambda G}x-Q_{\lambda G}x'\|
\le L_\delta\|x-x'\|^\alpha,
\qquad
L_\delta=2\lambda H\eta^\alpha+
\max\{1,B_N\}\delta^{1-\alpha}.
\tag{4.4}
\]

**Proof.** The inclusion \((p,v)\in(t,z)+\lambda G(t,z)\) is equivalent to

\[
v\in z+\lambda A(z),\qquad p=t-\lambda h(z).
\]

The first equation has exactly the solution \(z=J_Av\), and the second then determines \(t\), proving (4.3) for the complete inverse. For \(x=(p,v)\) and \(x'=(p',v')\), the reflected difference is the sum of

\[
\bigl(p-p',(2J_A-I)v-(2J_A-I)v'\bigr)
\]

and

\[
\bigl(2\lambda[h(J_Av)-h(J_Av')],0\bigr).
\]

Their norms are bounded by \(\max\{1,B_N\}\|x-x'\|\) and \(2\lambda H\eta^\alpha\|x-x'\|^\alpha\), respectively. Since \(\|x-x'\|\le\delta\), their sum gives (4.4). No error-bound exponent or constant has been used. \(\square\)

The same argument applies to a specified input domain if each stated Lipschitz or Hölder estimate holds on the corresponding inputs or outputs and the complete normal inverse covers that domain. Such a localized statement does not by itself establish invariance of a PPA orbit. The application in Section 5 will instead have global input coverage and constants uniform along the entire zero set.

### 4.2. Independent residual verifiers

**Proposition 4.2 (power transfer and stability of an ordinary error bound).** Let \(F\) be set-valued, and let \(q>0\). Define \(T_q(0)=0\) and

\[
T_q(v)=\|v\|^{q-1}v\quad(v\ne0),\qquad
H_q(u)=\{T_q(v):v\in F(u)\}.
\tag{4.5}
\]

With the convention \(\operatorname{dist}(0,\varnothing)=+\infty\), one has

\[
r_{H_q}(u)=r_F(u)^q,\qquad H_q^{-1}(0)=F^{-1}(0).
\tag{4.6}
\]

Consequently, the ordinary error bound

\[
\operatorname{dist}(u,F^{-1}(0))\le K r_F(u)^q
\tag{4.7}
\]

is equivalent to the linear error bound for \(H_q\) with the same constant and state domain.

For a separate perturbation statement, let \(S=F_0^{-1}(0)\) be closed, and suppose, on a specified neighborhood \(U\), that

\[
r_{F_0}(u)\ge m\operatorname{dist}(u,S)^\alpha,
\qquad
\|g(u)\|\le\ell\operatorname{dist}(u,S),
\quad m>0,\quad 0<\alpha<1.
\tag{4.8}
\]

Set \(F_g=F_0+g\). For each \(0<\theta<1\), at every \(u\in U\) satisfying

\[
\operatorname{dist}(u,S)^{1-\alpha}
\le\frac{(1-\theta)m}{\ell},
\tag{4.9}
\]

one has

\[
r_{F_g}(u)\ge\theta m\operatorname{dist}(u,S)^\alpha,
\qquad
\operatorname{dist}(u,S)
\le(\theta m)^{-1/\alpha}r_{F_g}(u)^{1/\alpha}.
\tag{4.10}
\]

If \(\ell=0\), condition (4.9) is unnecessary. Within the stated neighborhood and tube, \(F_g^{-1}(0)\) coincides with \(S\), so (4.10) is an error bound relative to the unchanged local zero set.

**Proof.** Since \(\|T_q(v)\|=\|v\|^q\), the continuity and monotonicity of \(s\mapsto s^q\) on \([0,+\infty)\) allow it to pass through the infimum defining the residual. Also, \(T_q(v)=0\) exactly when \(v=0\). This proves (4.6) and hence (4.7). For the perturbation assertion, the triangle inequality gives

\[
r_{F_g}(u)\ge r_{F_0}(u)-\|g(u)\|
\ge m d^\alpha-\ell d,
\qquad d=\operatorname{dist}(u,S).
\]

Condition (4.9) makes the last expression at least \(\theta m d^\alpha\). Moreover, \(g=0\) on \(S\cap U\), so those zeros are preserved; the positive lower bound excludes new zeros in the stated tube. \(\square\)

These are residual statements only: neither construction proves uniqueness or coverage of a Minty inverse. Conversely, Proposition 4.1 does not prove an error bound. The power transfer is an exact algebraic identity, not a license to apply a first-order chain rule without checking its hypotheses; in particular, \(DT_q(0)=0\) when \(q>1\). In the next section the error bound is obtained even more directly, from a separating gap in the native support-set geometry.

## 5. A support-function law coupled to a normal-cone inclusion

Consider a reduced generalized equation whose tangential response is a scaled support-function subdifferential and whose normal response is a strongly monotone variational inequality. The scaling depends on the normal state through a sublinear power. The formulation retains every active face of the support set. It is a mathematical support/yield structure; the results below do not identify it with an unchanged engineering model or a full contact PDE.

### 5.1. Complete resolvent and independent certificates

Let \(D\subset\mathbb R^m\) be nonempty, compact, and convex, and write

\[
\sigma_D(t)=\max_{v\in D}\langle v,t\rangle.
\]

Choose \(f\notin D\), and define two different geometric quantities,

\[
d_D=\operatorname{dist}(f,D)>0,
\qquad
R_D=\max_{v\in D}\|f-v\|.
\tag{5.1}
\]

Let \(C\subset\mathbb R^n\) be closed and convex with \(0\in C\). Let \(M\) be linear with \(\operatorname{sym}M\succeq aI\), where \(a>0\). Fix \(b>0\) and \(0<\alpha<1\). We use the normal-cone convention

\[
N_C(y)=\{n:\langle n,z-y\rangle\le0\text{ for every }z\in C\}
\quad(y\in C),
\]

and set \(N_C(y)=\varnothing\) otherwise. Define the full operator by

\[
F(t,y)=
\begin{cases}
\{(b\|y\|^\alpha(v-f),My+n):
v\in\partial\sigma_D(t),\ n\in N_C(y)\},&y\in C,\\
\varnothing,&y\notin C.
\end{cases}
\tag{5.2}
\]

**Theorem 5.1 (complete inverse and separate RL/EB certificates).** Put

\[
A=M+N_C,\qquad J_A=(I+\lambda A)^{-1},
\qquad\eta=(1+\lambda a)^{-1}.
\tag{5.3}
\]

Then \(F\) has a closed graph and

\[
S=F^{-1}(0)=\mathbb R^m\times\{0\}.
\tag{5.4}
\]

Its complete resolvent \(J=J_{\lambda F}\) exists and is single-valued on \(\mathbb R^{m+n}\). For an arbitrary input \((p,\xi_N)\), it is

\[
z=J_A\xi_N,\qquad s=b\|z\|^\alpha,
\qquad
J(p,\xi_N)=\bigl(T_s(p),z\bigr),
\tag{5.5}
\]

where

\[
T_s(p)=\operatorname{prox}_{\lambda s\sigma_D}(p+\lambda sf)
=\operatorname{prox}_{\lambda s(\sigma_D-\langle f,\cdot\rangle)}(p).
\tag{5.6}
\]

Here \(T_0=I\). For every \(\delta>0\), the reflected resolvent \(Q=2J-I\) satisfies, for all input pairs with \(\|x-x'\|\le\delta\),

\[
\|Qx-Qx'\|\le L_\delta\|x-x'\|^\alpha,
\qquad
L_\delta=\delta^{1-\alpha}+2\lambda bR_D\eta^\alpha.
\tag{5.7}
\]

Independently, on \(\operatorname{dom}F\) the ordinary error bound is

\[
\operatorname{dist}((t,y),S)
\le K r_F(t,y)^q,
\qquad
q=\frac1\alpha,\qquad K=(bd_D)^{-1/\alpha}.
\tag{5.8}
\]

**Proof.** We first establish the normal inverse without assuming an RL estimate. Set \(B=I+\lambda M\) and \(c=1+\lambda a\). For

\[
0<\omega<\frac{2c}{\|B\|^2},
\]

the map

\[
z\longmapsto P_C\bigl(z-\omega(Bz-\xi_N)\bigr)
\]

is a contraction on the complete space \(C\), with Lipschitz constant at most

\[
\sqrt{1-2\omega c+\omega^2\|B\|^2}<1.
\]

Its unique fixed point is characterized by \(\xi_N-Bz\in N_C(z)\). Since a normal cone is closed under nonnegative scaling, this is equivalent to

\[
\xi_N\in z+\lambda(Mz+N_C(z)).
\tag{5.9}
\]

Thus \(J_A\xi_N\) exists uniquely for every \(\xi_N\). If \(z=J_A\xi_N\) and \(z'=J_A\xi_N'\), monotonicity of \(N_C\) yields

\[
\langle \xi_N-\xi_N',z-z'\rangle
\ge(1+\lambda a)\|z-z'\|^2.
\tag{5.10}
\]

It follows that \(J_A\) is \(\eta\)-Lipschitz and \(J_A0=0\). The weaker inequality with coefficient one also gives

\[
\|(2J_A-I)\xi_N-(2J_A-I)\xi_N'\|^2
=\|\xi_N-\xi_N'\|^2+4\|z-z'\|^2
-4\langle \xi_N-\xi_N',z-z'\rangle
\le\|\xi_N-\xi_N'\|^2.
\tag{5.11}
\]

For the tangential equation, after \(z\) is determined, the complete inclusion becomes

\[
p\in t+\lambda s(\partial\sigma_D(t)-f).
\tag{5.12}
\]

This is the optimality condition of the strongly convex function

\[
t\longmapsto\frac12\|t-p\|^2+
\lambda s\bigl(\sigma_D(t)-\langle f,t\rangle\bigr).
\]

The quadratic term dominates its at-most-linear nonquadratic term, so a unique minimizer exists. Equations (5.5)–(5.6) follow. Conversely, that minimizer together with the normal solution satisfies the original inclusion. Hence the formula describes the complete inverse, not a branch selection. It also includes \(s=0\), when (5.12) is simply \(t=p\).

We next prove a parameter estimate that does not require a fixed active set. Let \(t=T_s(p)\) and \(t'=T_{s'}(p)\). Choose \(v\in\partial\sigma_D(t)\) and \(v'\in\partial\sigma_D(t')\) in the optimality conditions; if a parameter vanishes, any subgradient at the corresponding point may be chosen. Subtracting the equations gives

\[
0=t-t'+\lambda s(v-v')+
\lambda(s-s')(v'-f).
\]

Taking the inner product with \(t-t'\), using \(s\ge0\), the monotonicity of \(\partial\sigma_D\), and \(\|v'-f\|\le R_D\), yields

\[
\|T_s(p)-T_{s'}(p)\|
\le\lambda R_D|s-s'|.
\tag{5.13}
\]

For fixed \(s\), monotonicity in (5.12) similarly proves that \(T_s\) is firmly nonexpansive; therefore \(2T_s-I\) is nonexpansive. For two inputs \(x=(p,\xi_N)\) and \(x'=(p',\xi_N')\), put
\(s=b\|J_A\xi_N\|^\alpha\) and \(s'=b\|J_A\xi_N'\|^\alpha\). Split \(Qx-Qx'\) into the product difference at fixed parameter \(s\) and the parameter change at \(p'\). Equations (5.11) and (5.13) then give

\[
\begin{aligned}
\|Qx-Qx'\|
&\le\|x-x'\|+2\lambda R_D|s-s'|\\
&\le\|x-x'\|+
2\lambda bR_D\eta^\alpha\|\xi_N-\xi_N'\|^\alpha.
\end{aligned}
\tag{5.14}
\]

The last step uses
\(|\|z\|^\alpha-\|z'\|^\alpha|\le\|z-z'\|^\alpha\).
For \(\|x-x'\|\le\delta\), (5.14) proves (5.7). The argument concerns the full subdifferential and permits \(v\) and \(v'\) on different exposed faces, including transitions through \(t=0\). It uses \(R_D\), normal stability, and the load modulus, but not \(d_D\) or an error bound.

For the independent residual estimate, every \(v\in\partial\sigma_D(t)\) belongs to \(D\). Consequently, every graph value in (5.2) has norm at least

\[
b\|y\|^\alpha\|v-f\|
\ge bd_D\|y\|^\alpha,
\]

and hence

\[
r_F(t,y)\ge bd_D\|y\|^\alpha.
\tag{5.15}
\]

A zero therefore has \(y=0\), while \(0\in F(t,0)\) for every \(t\), proving (5.4). Since the distance to this set is \(\|y\|\), (5.15) gives (5.8). This proof uses neither the RL modulus nor the normal inverse estimates.

Finally, suppose graph points converge. Compactness of \(D\) permits a convergent subsequence of their subgradients; the closed graph of \(\partial\sigma_D\) identifies its limit. The normal vectors equal the convergent normal outputs minus \(My\), so they converge as well, and the closed graph of \(N_C\) applies. When \(y\to0\), boundedness of \(D\) makes the entire tangential output tend to zero. Thus the graph of \(F\) is closed. \(\square\)

The zero set is nonisolated when \(m\ge1\). Not every member of the class is genuinely multivalued: for example, a singleton \(D\) with \(C=\mathbb R^n\) gives a single-valued member. If \(D\) is not a singleton and \(C\ne\{0\}\), then \(\partial\sigma_D(0)=D\) supplies distinct tangential outputs at every state \((0,y)\) with nonzero \(y\in C\). Both the disk and nontrivial-polytope instances below have this property.

### 5.2. Genuine nonlinear order

**Proposition 5.2 (sharp exponents).** If \(C\ne\{0\}\), the largest local Hölder exponent of both \(J\) and \(Q\) at every solution input is \(\alpha\). In particular, neither map is calm there. No ordinary local error bound at a solution can hold with a finite constant and an exponent \(q'>1/\alpha\).

**Proof.** Fix an arbitrary solution input \(x_*=(p,0)\), and choose \(0\ne w\in C\). For \(0<\varepsilon\le1\), set

\[
y_\varepsilon=\varepsilon w,
\qquad \xi_{N,\varepsilon}=(I+\lambda M)y_\varepsilon,
\qquad x_\varepsilon=(p,\xi_{N,\varepsilon}).
\tag{5.16}
\]

Convexity and \(0\in C\) imply \(y_\varepsilon\in C\), and \(0\in N_C(y_\varepsilon)\) holds for every such point. Therefore \(J_A\xi_{N,\varepsilon}=y_\varepsilon\). Write
\(t_\varepsilon=T_{b\|y_\varepsilon\|^\alpha}(p)\).
The tangential optimality condition, together with (5.1), implies

\[
\|t_\varepsilon-p\|
=\lambda b\|y_\varepsilon\|^\alpha
\|v_\varepsilon-f\|
\ge\lambda bd_D\|w\|^\alpha\varepsilon^\alpha
\tag{5.17}
\]

for some \(v_\varepsilon\in\partial\sigma_D(t_\varepsilon)\). Meanwhile,
\(\|x_\varepsilon-x_*\|=\varepsilon\|(I+\lambda M)w\|\).
The tangential components of \(Jx_\varepsilon-Jx_*\) and \(Qx_\varepsilon-Qx_*\) are respectively \(t_\varepsilon-p\) and \(2(t_\varepsilon-p)\). For any exponent \(\theta>\alpha\), their ratios to \(\|x_\varepsilon-x_*\|^\theta\) diverge as \(\varepsilon\downarrow0\). The upper estimate (5.7), and the identity \(J=(I+Q)/2\), give exponent \(\alpha\). This proves the asserted sharp order and noncalmness. Estimate (5.13) also shows \(t_\varepsilon\to p\), so all the graph points and residuals used in the argument approach the solution graph point; ordinary localization does not remove them.

For the error-bound assertion, use the states \(u_\varepsilon=(p,\varepsilon w)\), fix \(v\in\partial\sigma_D(p)\), and choose the normal vector zero. This gives an admissible graph value and the residual upper bound

\[
r_F(u_\varepsilon)
\le bR_D\|w\|^\alpha\varepsilon^\alpha
+\|Mw\|\varepsilon
\le C_w\varepsilon^\alpha
\quad(0<\varepsilon\le1)
\tag{5.18}
\]

with \(C_w=bR_D\|w\|^\alpha+\|Mw\|\). If a local error bound with \(q'>1/\alpha\) held, then

\[
\varepsilon\|w\|\le K' C_w^{q'}\varepsilon^{\alpha q'},
\]

which is impossible as \(\varepsilon\downarrow0\). \(\square\)

The independently derived exponents therefore satisfy \(\gamma q=1\) for this class. This is a conclusion of the two verification arguments, not a restriction imposed on either argument in advance. The proposition establishes optimal exponents; it does not assert optimality of \(L_\delta\) or \(K\).

### 5.3. Two scales and the whole PPA orbit

**Corollary 5.3 (quantitative RL–EB certification).** Suppose

\[
\Delta=d_D-R_D\eta^\alpha>0.
\tag{5.19}
\]

First choose a pair-distance scale \(\delta>0\) satisfying

\[
\delta^{1-\alpha}<2\lambda b\Delta.
\tag{5.20}
\]

Then choose a state-distance threshold \(0<r\le\delta\) such that

\[
r^{1-\alpha}+L_\delta<2\lambda bd_D,
\quad\text{equivalently}\quad
r^{1-\alpha}<2\lambda b\Delta-\delta^{1-\alpha}.
\tag{5.21}
\]

Set

\[
\kappa_r=
\left(\frac{r^{1-\alpha}+L_\delta}{2\lambda bd_D}\right)^{1/\alpha}<1.
\tag{5.22}
\]

For every \(x_0\in\mathbb R^{m+n}\) with \(d_0=\operatorname{dist}(x_0,S)\le r\), the unmodified Euclidean PPA \(x_{j+1}=Jx_j\) exists for all \(j\), remains in the tube \(\operatorname{dist}(x,S)\le r\), and converges with finite length to a point \(x_\infty\in S\). More precisely,

\[
d_{j+1}\le\kappa_r d_j,
\qquad
\|x_{j+1}-x_j\|\le\frac12(d_j+L_\delta d_j^\alpha),
\tag{5.23}
\]

and

\[
\|x_j-x_\infty\|
\le\frac12\left(
\frac{\kappa_r^j d_0}{1-\kappa_r}
+\frac{L_\delta\kappa_r^{\alpha j}d_0^\alpha}
{1-\kappa_r^\alpha}
\right).
\tag{5.24}
\]

**Proof.** For \(x=(t,y)\), its nearest solution input is \(p_S=(t,0)\), and \(Jp_S=Qp_S=p_S\). If \(d=\operatorname{dist}(x,S)\le r\le\delta\), then (5.7) applies to the pair \((x,p_S)\). Thus

\[
\|x-Jx\|
=\tfrac12\|(x-p_S)-(Qx-p_S)\|
\le\tfrac12(d+L_\delta d^\alpha).
\tag{5.25}
\]

For \(z=Jx\), the actual PPA residual \(w=(x-z)/\lambda\) belongs to \(F(z)\). The error bound is evaluated at this output state, not at the input. Consequently,

\[
\begin{aligned}
\operatorname{dist}(z,S)
&\le (bd_D)^{-1/\alpha}\|w\|^{1/\alpha}\\
&\le\left(\frac{d^{1-\alpha}+L_\delta}{2\lambda bd_D}\right)^{1/\alpha}d
\le\kappa_r d.
\end{aligned}
\tag{5.26}
\]

At \(d=0\), the same conclusion holds because \(x\in S\) and \(Jx=x\). Global inverse coverage and (5.26) now give the whole sequence and tube invariance by induction. Summing (5.25) with \(d_j\le\kappa_r^j d_0\) proves finite length and (5.24). Since \(S\) is closed and \(d_j\to0\), the limit belongs to \(S\). \(\square\)

The two scales in this statement have different roles. The variable \(\delta\) bounds the distance between two Minty inputs; \(r\) bounds the distance of an iterate to \(S\). Condition (5.20) alone does not certify contraction on a prescribed state tube. If \(r=\delta\), the sufficient joint condition is

\[
r^{1-\alpha}<\lambda b\Delta.
\tag{5.27}
\]

If one instead advertises the all-pairs constant on a full input ball of radius \(r\), a safe choice is \(\delta=2r\); the corresponding contraction check is

\[
r^{1-\alpha}+(2r)^{1-\alpha}<2\lambda b\Delta.
\tag{5.28}
\]

For the solution comparisons in the proof, \(r\le\delta\) is sufficient. No finite tangential boundary or extra initial-point budget is needed here: the complete inverse is global and the near-pair estimates are uniform along all of \(S\). A merely local application would need its own coverage and finite-length stay-in-domain argument.

### 5.4. A successful direct partial proof

The preceding corollary certifies the orbit from two scalar summaries. The block structure contains additional information, and retaining it gives a stronger competing proof for the same algorithm.

**Proposition 5.4 (normal contraction and summable tangential motion).** Under the assumptions of Theorem 5.1, without condition (5.19), the same PPA converges to a point of \(S\) from every input \(x_0=(t_0,y_0)\in\mathbb R^{m+n}\). For every \(j\ge0\),

\[
\|y_{j+1}\|\le\eta\|y_j\|,
\qquad
\|t_{j+1}-t_j\|
\le\lambda bR_D\|y_{j+1}\|^\alpha,
\tag{5.29}
\]

and

\[
\|y_j\|\le\eta^j\|y_0\|,
\qquad
\|t_j-t_\infty\|
\le\frac{\lambda bR_D\eta^\alpha}{1-\eta^\alpha}\|y_j\|^\alpha.
\tag{5.30}
\]

In particular, \(\eta\) is a set-distance contraction bound, and \(\eta^\alpha\) is an R-linear point-convergence factor bound.

**Proof.** The normal recursion is \(y_{j+1}=J_Ay_j\), so (5.10) and \(J_A0=0\) imply the first inequality in (5.29), even when the initial normal input lies outside \(C\). The tangential optimality condition gives

\[
t_j-t_{j+1}=\lambda b\|y_{j+1}\|^\alpha(v_{j+1}-f),
\qquad v_{j+1}\in\partial\sigma_D(t_{j+1})\subset D,
\]

which proves the second. The normal increments are bounded by
\((1+\eta)\eta^j\|y_0\|\), and the tangential increments form a summable geometric majorant with ratio \(\eta^\alpha\). Thus the complete sequence has finite length and tends to \((t_\infty,0)\). Summing the tangential increments from \(j\) onward proves (5.30). For example,

\[
\|x_j-x_\infty\|
\le\eta^j\|y_0\|
+\frac{\lambda bR_D\eta^\alpha}{1-\eta^\alpha}
\eta^{\alpha j}\|y_0\|^\alpha,
\tag{5.31}
\]

which gives the stated R-linear bound. \(\square\)

The normal information in this proof is also expressible as a nontrivial degenerate quadratic certificate. Let \(P_T\) and \(P_N\) be the orthogonal projections onto the tangential and normal blocks. For any two graph points, write \(a_\Delta=u-u'\) and \(b_\Delta=v-v'\). Tangential Young's inequality and normal strong monotonicity give

\[
\langle a_\Delta,b_\Delta\rangle
\ge a_\Delta^TU a_\Delta+b_\Delta^TV b_\Delta,
\quad
U=-\frac1{2\lambda}P_T+aP_N,
\quad V=-\frac\lambda2P_T.
\tag{5.32}
\]

Its Cayley coefficient is

\[
I+\lambda U+V/\lambda=(1+\lambda a)P_N,
\tag{5.33}
\]

which is informative in the normal block and degenerate in the tangential block.

For completeness, define \(d_H(u,S)^2=\inf_{p\in S}(u-p)^TH(u-p)\), with \(H\succeq0\). The following partial inequality holds for every \((u,v)\in\operatorname{gph}F\):

\[
\inf_{p\in S}\left\{
\langle Nv,u-p\rangle+
(u-p)^T\operatorname{sym}(H-\Xi)(u-p)
\right\}\ge d_H(u,S)^2,
\tag{5.34}
\]

where

\[
N=2\lambda P_N,\qquad H=P_N,\qquad\Xi=2\lambda aP_N.
\tag{5.35}
\]

Indeed, \(0\in C\) implies \(\langle n,y\rangle\ge0\) for \(n\in N_C(y)\), so \(\langle v_N,y\rangle\ge a\|y\|^2\). The expression on the left of (5.34) is independent of the tangential coordinate of \(p\) and is at least
\(2\lambda a\|y\|^2+(1-2\lambda a)\|y\|^2=\|y\|^2=d_H(u,S)^2\).
Only the analysis tester has been changed; the actual PPA remains Euclidean and unmodified. The additional tangential summability estimate in (5.29) is essential for full point convergence and is not concealed in the partial-distance assertion.

Thus (5.19) is a sufficient condition for the displayed aggregated RL/EB certificate, not a necessary condition for convergence of this class, nor a proved optimal parameter domain for all possible certificates. Exclusions of full-space coercive or finite anchored conditions must therefore be stated alongside, not in place of, the successful partial proof.

### 5.5. Disk example and exact orbit

**Example 5.5.** Let \(D=\overline B_1(0)\subset\mathbb R^m\), with \(m=2\) for the disk, and set

\[
C=\mathbb R_+,\quad f=3e_1,\quad b=\lambda=1,
\quad\alpha=\tfrac23,\quad M=7.
\tag{5.36}
\]

Then \(\sigma_D(t)=\|t\|\), and the full operator is

\[
F(t,y)=\bigl(y^{2/3}(\partial\|t\|-3e_1),
7y+N_{\mathbb R_+}(y)\bigr),\qquad y\ge0,
\tag{5.37}
\]

with empty values for \(y<0\). At \(t=0\) and \(y>0\), its tangential value is a translated, nontrivial closed ball. The complete resolvent is

\[
z=\frac{\xi_N^+}{8},\qquad s=z^{2/3},\qquad
J(p,\xi_N)=\bigl(\operatorname{shrink}(p+3se_1,s),z\bigr),
\tag{5.38}
\]

where \(\xi_N^+=\max\{\xi_N,0\}\) and

\[
\operatorname{shrink}(u,s)=
\begin{cases}
(1-s/\|u\|)u,&\|u\|>s,\\
0,&\|u\|\le s.
\end{cases}
\]

The native constants are

\[
d_D=2,\qquad R_D=4,\qquad\eta=\tfrac18,
\qquad\eta^\alpha=\tfrac14.
\]

For \(\delta=r=1/8\), the two certificates and the finite-radius factor are

\[
(\gamma,L_\delta)=\left(\tfrac23,\tfrac52\right),
\quad
(q,K)=\left(\tfrac32,2^{-3/2}\right),
\quad
\kappa_r=\left(\tfrac34\right)^{3/2}.
\tag{5.39}
\]

This choice is valid for the solution comparisons in Corollary 5.3; it does not identify \(L_{1/8}\) with an all-pairs constant on an entire ball of radius \(1/8\).

An exact orbit is obtained from
\(t_0=\tau e_1\), \(\tau\ge0\), and \(y_0>0\).
The shrinkage input stays on the positive \(e_1\)-ray and has norm strictly larger than its threshold. Hence

\[
y_{j+1}=\tfrac18y_j,
\qquad t_{j+1}=t_j+2y_{j+1}^{2/3}e_1.
\]

Summing this recursion gives, for every \(j\ge0\),

\[
y_j=8^{-j}y_0,
\qquad
t_j=\left[\tau+\frac23y_0^{2/3}(1-4^{-j})\right]e_1,
\tag{5.40}
\]

and therefore

\[
t_\infty=\left(\tau+\frac23y_0^{2/3}\right)e_1,
\qquad
\|x_j-x_\infty\|^2
=\frac49y_0^{4/3}16^{-j}+y_0^2 64^{-j}.
\tag{5.41}
\]

The set-distance ratio is exactly \(1/8\), whereas the ratio of successive point errors tends to \(1/4\). In contrast, the aggregated certificate gives the safe factors \(\kappa_r\approx0.649519\) for set distance and \(\kappa_r^{2/3}=3/4\) for the point-error bound. These different numbers reflect different retained information, not conflicting convergence conclusions. If the same orbit is to be compared with the local certificate (5.39), take \(0<y_0\le1/8\). The restriction \(\tau\ge0\) is necessary for this displayed branch calculation; negative \(\tau\) can produce changes in the shrinkage regime and is not covered by (5.40).

For a polytope \(D=\operatorname{conv}\{v_1,\ldots,v_N\}\), the same theorem applies with

\[
\sigma_D(t)=\max_i\langle v_i,t\rangle,
\quad
\partial\sigma_D(t)=\operatorname{conv}\{v_i:i\in I(t)\},
\quad
R_D=\max_i\|f-v_i\|,
\tag{5.42}
\]

where \(I(t)\) is the active index set. The gap \(d_D\) is obtained from the convex projection problem \(\min_{v\in D}\|f-v\|^2\). The two certificates retain respectively the largest and the smallest distance to the same set; no common ball replacement or fixed-active-set reduction is required. A general compact-set representation need not make the farthest-point calculation computationally easy, and the structural formulas alone make no uniform complexity claim.

---

## 6. Relations to existing PPA geometries

The relevant distinction between convergence certificates is not simply whether the operator is monotone. For a fixed-step Euclidean PPA, available information may constrain arbitrary pairs of graph points, graph points relative to solutions, or an energy minimized over a solution set. We distinguish these quantifiers because they support different conclusions. An all-pairs reflected-resolvent bound (AP-RL) controls differences throughout the selected graph patch and, in particular, excludes distinct graph points with the same Minty input. A solution-anchored inequality need not have this property. Likewise, an inequality relative to one fixed solution cannot be evaluated at a moving nearest solution without an additional argument. Throughout the comparison, the stepsize, metric, graph localization, admissible selections, and local input domain are held fixed.

The closest linear graph-level comparison is the submonotonicity condition of Luke and Tam. Writing \(a=u-v\) and \(b=u^*-v^*\) for two graph points, their scaled inequality
\[
\langle a,\lambda b\rangle\ge-\tau\|a+\lambda b\|^2
\]
is equivalent to
\[
\|a-\lambda b\|^2\le(1+4\tau)\|a+\lambda b\|^2.
\]
Thus linear RL and this graph condition coincide under \(L^2=1+4\tau\). This is an equivalence of graph inequalities, not an identification of complete convergence theorems: local maximality, self-mapping, Minty coverage, stability, and the relevant error-bound and parameter assumptions must still be checked. Their framework already accommodates set-valued operators and nonisolated zero sets. The distinction investigated here is therefore the verification of genuinely non-Lipschitz reflected geometry, rather than multivaluedness or nonisolation alone. [Luke–Tam, Definition 2, Assumption 2, and Theorem 2](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)

Semimonotonicity provides a broader source of quadratic information. Its inequality \(\langle a,b\rangle\ge\mu\|a\|^2+\nu\|b\|^2\) can be converted into a linear RL bound when the corresponding Cayley conditions hold. The conversion must retain the source quantifier: an anchored inequality does not become all-pairs merely through algebra. It can also be preferable to keep the original quadratic terms, since their separate weights on the state error and the proximal step are lost when represented by a single RL constant. In particular, linear RL is a balanced slice of scalar semimonotonicity, not a replacement for its full parameter calculus or for matrix-valued information. The failure of an informative Cayley certificate should not be described as the absence of every semimonotonicity inequality; the universal negative-parameter Young region must be distinguished from parameters that actually certify the desired resolvent geometry. [Evens–Pas–Latafat–Patrinos, Definition 4.1 and Propositions 4.3, 4.7, and 4.12](https://arxiv.org/html/2305.03605v2#S4)

Weak- and oblique-Minty assumptions offer an anchored energy route rather than an all-pairs inverse estimate. An inequality of the form \(\langle u-p,v\rangle\ge v^{\mathsf T}Vv\) can directly control a PPA step when the permitted anchors include the comparison solution used in that step. If it is available only at a fixed solution, the corresponding Lyapunov argument must retain that fixed anchor. This distinction also matters when citing convergence rates: the general preconditioned PPA convergence results of Evens et al. and their linear-rate theorem do not have identical assumptions. The latter additionally requires the stated all-solution anchoring, closed convex zero set, resolvent continuity, and uniform subregularity conditions. None of these assumptions can be inferred solely from the displayed anchored inequality. [Evens–Pas–Latafat–Patrinos, Definition 2.1, Assumption I, and Theorems 2.4 and 2.13](https://arxiv.org/html/2305.03605v2#S2)

Partial subregularity and partial strong submonotonicity play two different roles. The former relates residual information to a selected test distance; the latter supplies a coupled energy inequality involving an infimum over the same zero set. Accordingly, a convergence argument based on partial strong submonotonicity should not be attributed to partial subregularity alone. Semidefinite tests are an intentional feature of this framework. They can retain normal contraction while assigning no weight to a tangential direction in which a full-space certificate fails. Their use does not, by itself, change the PPA being analyzed: a degenerate analysis metric and a degenerate preconditioner in the algorithm are different objects. Solvability, test-matrix evolution, the domain of validity, and orbit localization remain separate hypotheses. [Valkonen, Definitions 3.2 and 4.2 and Theorems 3.5 and 4.1](https://arxiv.org/pdf/1711.05123)

The error-bound side uses established ordinary higher-order metric subregularity. Our exponent convention is
\[
\operatorname{dist}(x,S)\le K\,r_F(x)^q,
\qquad r_F(x)=\operatorname{dist}(0,F(x)),\qquad S=F^{-1}(0),
\]
with the exponent on the residual. Mordukhovich and Ouyang define both ordinary and strong \(q\)-subregularity for \(q>0\), including \(q>1\). Ordinary subregularity measures distance to the inverse image and does not require an isolated zero; its strong counterpart measures distance to a specified point. These properties are inputs to the present analysis, not new definitions. The verification task is to obtain an applicable exponent, constant, and neighborhood for the actual residual and zero set. One exact transfer is the radial output transformation \(T_q(v)=\|v\|^{q-1}v\), with \(T_q(0)=0\): the transformed map \(H_q=T_q\circ F\) has the same zero set and residual \(r_{H_q}=r_F^q\). Ordinary linear subregularity tools may therefore be applied to \(H_q\), subject to their own assumptions. This does not authorize substituting \(q>1\) into a theorem proved only for a smaller exponent range, or using an unqualified chain rule at the degenerate point \(DT_q(0)=0\). [Mordukhovich–Ouyang, Definition 3.1](https://arxiv.org/html/1507.04825v1); [Li–Mordukhovich, Definitions 3.1–3.2 and Theorem 5.1](https://optimization-online.org/wp-content/uploads/2012/02/3340.pdf)

Identifiable-manifold results are another possible error-bound input, but their scope must be retained. The reviewed results of Wu and Xie transfer linear slope-type error bounds under local sublevel conditions, using identifiability or partial smoothness with nondegeneracy; their subdifferential-to-manifold-gradient result is stated in a convex setting. To apply such a transfer here, one must identify the relevant solution set, check the admissible sublevel and neighborhood, and compare the source slope or subdifferential residual quantitatively with \(r_F\). A higher-order conclusion additionally requires a proved transfer producing the claimed power. An identifiable active manifold is not generally the full zero set. These results do not by themselves establish Minty coverage, cross-branch RL, or a uniform higher-order estimate for an arbitrary multifunction. [Wu–Xie, Theorems 3.1, 3.3, and 4.2](https://arxiv.org/html/2605.02754v2)

The support-function/normal-cone class illustrates both separation and information loss. When its normal constraint set is nontrivial, its reflected resolvent is genuinely non-Lipschitz. It therefore lies outside finite linear RL certificates on a full neighborhood. The explicit scale-separation sequences also exclude the specified fixed finite weak/oblique-Minty inequalities, informative scalar semimonotonicity, and coercive full-space matrix certificates. These conclusions concern the specified certificates on the same local input domain; they do not exclude tangentially degenerate normal-projector tests or a different algorithm. Indeed, if \(\eta=(1+\lambda a)^{-1}<1\) is the normal resolvent contraction factor, the very same PPA satisfies
\[
\|y_{n+1}\|\le \eta\|y_n\|,
\qquad
\|t_{n+1}-t_n\|\le\lambda bR_D\|y_{n+1}\|^\alpha.
\]
The normal sequence contracts and the tangential increments are summable, which gives point convergence without the scalar compatibility condition \(R_D\eta^\alpha<d_D\). Thus the scalar RL–EB interface can certify a model while remaining less informative than a componentwise argument for that model. A failed scalar compatibility test is not a failed PPA.

The reverse obstruction is equally important. Consider
\[
F_0(x,y)=\{(0,y),(0,2y)\},\qquad S=\mathbb R\times\{0\}.
\]
This operator is monotone relative to every zero and has the exact ordinary error bound \(\operatorname{dist}((x,y),S)=r_{F_0}(x,y)=|y|\). For \(\lambda=1\),
\[
J_{F_0}(p,\xi_N)=\{(p,\xi_N/2),(p,\xi_N/3)\}.
\]
Every admissible selection converges, since the first coordinate is unchanged and the absolute second coordinate decreases by a factor at most \(1/2\). Nevertheless, for \(\xi_N\ne0\) the two resolvent outputs correspond to distinct graph points with the same Minty input. Their reflected outputs differ, so no AP-RL inequality with any positive exponent and finite constant can hold on a full local graph patch. Together with the forward separation, this rules out a general inclusion between AP-RL plus ordinary error bounds and the specified anchored convergence routes.

The resulting contribution is a quantitative verification interface with explicit scope, supplemented by a natural class and bounded separation results. Its two inputs may be proved independently and need not come from the same representation or derivative information. They must, however, apply to the same actual PPA transitions. At the nonlinear critical balance, the constant \(2\) belongs to the stated scalar information and its proximal-step consequence; it is not a claim that the resulting factor equals the best rate of every underlying operator. Retaining native quadratic, normal–tangential, or matrix information can give stronger conclusions. This is why the comparison supports complementary uses of existing theories, rather than universal dominance by RL.

### 6.1. Comparison by quantifier and retained information

AP means all graph pairs; AS means all relevant solution anchors; FS means a fixed solution anchor; INF means a coupled expression minimized over the same solution set. All imports below retain the source domain and quantifier.

| Theory or property | Exact role and source scope | What can enter the RL–PPA analysis | What does not follow | Evidence limits and fair comparison |
|---|---|---|---|---|
| Luke–Tam submonotonicity | A scaled quadratic graph property; [Definition 2, Assumption 2, Theorem 2](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863). | Exact graph-level linear RL with \(\gamma=1\), \(L^2=1+4\tau\). | The identity does not supply local maximality, self-mapping, stability, coverage, EB, or trajectory localization. | An existing multivalued/nonisolated baseline. Genuine non-Lipschitz reflection excludes finite linear certificates on the same full neighborhood; no global comparison of complete theorem families is asserted. |
| Scalar and matrix semimonotonicity | Quadratic increment or anchored information; source calculus includes shift, inversion, and composition operations; [Definition 4.1 and Propositions 4.3, 4.7, 4.12](https://arxiv.org/html/2305.03605v2#S4). | Scalar Cayley conversion to linear RL under the conditions in §6.2.1; alternatively retain native weighted energy or matrix constraints. | An anchored source does not imply AP-RL. Finite formal negative parameters need not yield a useful Cayley certificate. Scalarization does not preserve every matrix or componentwise advantage. | Project separation concerns informative scalar parameters and a specified coercive full-space matrix class. The universal Young region and successful degenerate tests remain available. |
| Weak/oblique-Minty | FS, a specified solution subset, or AS anchored energy; [Definition 2.1, Assumption I, Theorems 2.4, 2.13](https://arxiv.org/html/2305.03605v2#S2). | Native one-step energy, with AS sufficient for a moving nearest-solution comparison; FS gives a fixed-anchor Lyapunov route. | No AP-RL, Minty injectivity, or local resolvent existence follows from the anchored inequality alone. The linear-rate theorem needs its additional assumptions. | Forward exclusions require a fixed finite matrix and full local input coverage for the same Euclidean PPA. The reverse multivalued example excludes any blanket inclusion in AP-RL. |
| Partial subregularity (PSR) and partial strong submonotonicity (PSM) | Two distinct properties: PSR is residual-to-test-distance control; PSM is an INF-type coupled energy over the same zero set with test matrices. [Valkonen, Definitions 4.2 and 3.2; Theorems 3.5, 4.1](https://arxiv.org/pdf/1711.05123). | PSR supplies a partial EB after matching the test distance; PSM supplies native energy, including the specialization in §6.2.3. Normal energy can be combined with tangential reconstruction. | A partial EB alone gives neither descent nor full-space point convergence. INF is not AP/AS, and the comparison set cannot be changed. Rate, solvability, and orbit hypotheses remain necessary. | The natural-class direct proof shows that a tangentially degenerate normal-projector test may succeed even when a scalar aggregate is weaker. A degenerate test is not a degenerate algorithmic preconditioner. |
| Ordinary higher-order subregularity | A set-distance EB for \(q>0\), including \(q>1\); [Mordukhovich–Ouyang, Definition 3.1](https://arxiv.org/html/1507.04825v1). | The independent pair \((q,K)\), with its neighborhood and residual scope; linear tools on \(T_q\circ F\) give an exact transfer when their assumptions hold. | No RL, resolvent coverage, or prescribed relation \(q=1/\gamma\) follows. A strong/isolated estimate is not an ordinary uniform estimate along a nonisolated solution set. | Existing theory, not an exclusion target or claimed new definition. Do not extrapolate a source theorem beyond its exponent range; verify all relevant small outputs and actual positive-radius constants. |
| Identifiable-manifold transfer | Reviewed linear slope EB under sublevel conditions; convex subdifferential/manifold-gradient transfer in [Wu–Xie, Theorems 3.1, 3.3, 4.2](https://arxiv.org/html/2605.02754v2). | An optional EB-side transfer after proving target-set agreement and quantitative source-residual comparison. | No arbitrary-\(F\), arbitrary-\(q\) theorem; no automatic uniform constant along a full zero manifold; no RL or Minty coverage. | The active manifold need not be the zero set. A \(q>1\) application needs a separate power-producing argument. The main natural-class proof uses direct residual separation, not this transfer. |

### 6.2. Exact import formulas

These formulas make the comparison table self-contained for technical integration. They need not all appear in the short main text. They are project algebra from the supplied report, not newly attributed theorems of the linked authors.

#### 6.2.1. Scalar semimonotonicity

For \(\langle a,b\rangle\ge\mu\|a\|^2+\nu\|b\|^2\), assume
\[
1-4\mu\nu\ge0,\qquad D_\lambda=1+\lambda\mu+\nu/\lambda>0.
\]
Then the source inequality gives, with the same quantifier,
\[
\|a-\lambda b\|\le L_{\mu,\nu}(\lambda)\|a+\lambda b\|,
\quad
L_{\mu,\nu}(\lambda)=
\frac{|\lambda\mu-\nu/\lambda|+\sqrt{1-4\mu\nu}}
{1+\lambda\mu+\nu/\lambda}.
\]
Linear RL itself is the balanced slice
\[
\mu=\frac{1-L^2}{2\lambda(1+L^2)},\qquad \nu=\lambda^2\mu.
\]
For an actual PPA step, let \(d=\operatorname{dist}(x,S)\), \(d_+=\operatorname{dist}(x^+,S)\), and \(s=\|x-x^+\|\). If the semimonotonicity inequality is valid for the same nearest solution used by that step, and
\[
1+2\lambda\mu\ge0,\qquad1+2\nu/\lambda\ge0,
\]
retaining the native terms gives
\[
(1+2\lambda\mu)d_+^2+(1+2\nu/\lambda)s^2\le d^2.
\]
These sign conditions cannot be discarded in the nonisolated set-distance setting. With \(d_+\le\rho s/\lambda\), \(\rho>0\), a positive denominator gives the factor
\[
\kappa_{\mu,\nu}=
\frac{\rho}{\sqrt{(1+2\lambda\mu)\rho^2+\lambda^2+2\lambda\nu}},
\]
which is strictly below one precisely when \(2\lambda\mu\rho^2+\lambda^2+2\lambda\nu>0\). No unconditional dominance over separately simplified comparison factors is claimed.

#### 6.2.2. Solution-anchored weak-Minty

If the same nearest-solution comparison is allowed and
\[
\langle x^+-p,(x-x^+)/\lambda\rangle
\ge-\eta\|(x-x^+)/\lambda\|^2,
\]
then
\[
d_+^2+(1-2\eta/\lambda)s^2\le d^2.
\]
With the preceding linear EB and \(\lambda>2\eta\), this gives
\[
\kappa=\frac{\rho}{\sqrt{\rho^2+\lambda^2-2\eta\lambda}}<1.
\]
An FS-only condition does not justify replacing its fixed anchor with \(p\in P_S(x)\); it requires a separate fixed-anchor argument.

#### 6.2.3. Native PSM coupling

With \(M\succeq0\), \(d_M\) the associated test distance, and the convention \(\langle b,a\rangle_N=\langle Nb,a\rangle\), the relevant PSM property is
\[
\inf_{p\in S}\{
\langle b,u-p\rangle_N+\|u-p\|_{M-\Xi}^2
\}\ge d_M(u,S)^2.
\]
Here \(\|v\|_H^2\) denotes the quadratic form \(\langle Hv,v\rangle\); \(H=M-\Xi\) is not implicitly assumed positive semidefinite. In the isotropic specialization
\[
(\Xi,N,M)=(\theta I,2\lambda I,(1+\theta)I),\qquad\theta>-1,
\]
the same-set coupled identity yields
\[
(1+\theta)d_+^2+s^2\le d^2.
\]
With the same linear EB, the factor is \((1+\theta+\lambda^2/\rho^2)^{-1/2}\), and it is strictly below one if and only if \(\theta+\lambda^2/\rho^2>0\). This is an INF import, not a conversion into all-pairs RL.

### 6.3. Forward separation with a surviving degenerate certificate

**Proposition 6.1 (finite full-input tests fail while a degenerate test survives).**

Let \(X=\mathbb R^m\times\mathbb R^n\) with its Euclidean norm. Suppose that \(D\subset\mathbb R^m\) is nonempty, compact and convex, \(f\notin D\), \(C\subset\mathbb R^n\) is closed and convex with \(0\in C\ne\{0\}\), \(\operatorname{sym}M\succeq aI\) for \(a>0\), \(b>0\), and \(0<\alpha<1\). Define

\[
F(t,y)=\bigl(b\|y\|^\alpha(\partial\sigma_D(t)-f),My+N_C(y)\bigr),
\]

with empty values outside \(\mathbb R^m\times C\). Fix \(\lambda>0\), write \(S=\mathbb R^m\times\{0\}\), and let \(J=(I+\lambda F)^{-1}\), which is the complete single-valued map of Theorem 5.1. Fix any \(p_*\in S\). Then:

1. No fixed finite symmetric matrix \(V\) can make
   \[
   \langle u-p_*,v\rangle\ge v^TVv
   \tag{6.1}
   \]
   hold for every retained graph point \((u,v)\) near \((p_*,0)\), if the retained graph must cover a full neighborhood of the Minty input \(p_*\).

2. There is no finite \(C_0\) such that
   \[
   \|Jx-p_*\|\le C_0\|x-p_*\|
   \tag{6.2}
   \]
   on a full input neighborhood of \(p_*\). In particular, a fixed finite almost-nonexpansiveness inequality relative to this anchor cannot hold there. This only excludes almost-averaging uses for which (6.2) is a necessary consequence on that same relative input set.

3. No fixed finite symmetric matrices \(U,V\) can give the all-pairs inequality
   \[
   \langle\Delta u,\Delta v\rangle
   \ge\Delta u^TU\Delta u+\Delta v^TV\Delta v
   \tag{6.3}
   \]
   on such a graph patch while also satisfying
   \[
   \mathcal C:=I+\lambda U+\lambda^{-1}V\succ0.
   \tag{6.4}
   \]

4. The conclusion in part 3 does not extend to degenerate Cayley coefficients. Let \(P_T,P_N\) be the orthogonal tangential and normal projectors. The global inequality (6.3) does hold for
   \[
   U=-\frac1{2\lambda}P_T+aP_N,
   \qquad V=-\frac\lambda2P_T,
   \qquad \mathcal C=(1+\lambda a)P_N.
   \tag{6.5}
   \]
   Independently, the same Euclidean PPA has the normal contraction and summable tangential increments of Proposition 5.4. These statements do not require \(R_D\eta^\alpha<d_D\).

If additionally \(R_D\eta^\alpha<d_D\), where \(d_D=\operatorname{dist}(f,D)\), \(R_D=\max_{v\in D}\|f-v\|\), and \(\eta=(1+\lambda a)^{-1}\), Theorem 5.1, Proposition 5.2, and Corollary 5.3 also provide genuine AP-Hölder/ordinary-EB certification and convergence on positive scales. Thus the proposition gives a directed separation from the tests (6.1)–(6.4), accompanied by an explicit surviving degenerate certificate; it does not claim exclusive convergence capability.

**Proof.** Let \(v_0=P_Df\) and \(e=(f-v_0)/d_D\). Convex projection gives

\[
\langle e,v-f\rangle\le-d_D\qquad(v\in D).
\tag{6.6}
\]

Write \(p_*=(t_*,0)\), choose \(0\ne w\in C\), and let \(0<\beta<\alpha\). For sufficiently small \(r>0\), set

\[
u_r=(t_*+r^\beta e,rw),\qquad
v_r^*=(b\|rw\|^\alpha(v_r-f),Mrw),
\quad v_r\in\partial\sigma_D(t_*+r^\beta e).
\]

These are genuine graph points: convexity and \(0\in C\) imply \(rw\in C\) for \(0<r\le1\), and \(0\in N_C(rw)\). By (6.6),

\[
\langle u_r-p_*,v_r^*\rangle
\le-bd_D\|w\|^\alpha r^{\alpha+\beta}+O(r^2),
\qquad
\|v_r^*\|^2=O(r^{2\alpha}).
\]

Because \(\alpha+\beta<2\alpha<2\), the negative term dominates every fixed finite output quadratic form. Therefore (6.1) fails. Moreover, \(u_r\to p_*\), \(v_r^*\to0\), and \(u_r+\lambda v_r^*\to p_*\). Complete input coverage together with uniqueness of \(J\) forces the retained graph to contain the unique preimages of this sequence. Deleting these graph points would change the declared input scope.

For part 2 take instead the input

\[
x_r=(t_*,(I+\lambda M)rw).
\]

The normal resolvent returns \(rw\). If \(\widehat t_r\) is its tangential output and \(s_r=b\|rw\|^\alpha\), the proximal equation supplies \(\widehat v_r\in\partial\sigma_D(\widehat t_r)\subset D\) with

\[
\widehat t_r-t_*=-\lambda s_r(\widehat v_r-f).
\]

Thus

\[
\|Jx_r-p_*\|\ge\lambda bd_D\|w\|^\alpha r^\alpha,
\qquad
\|x_r-p_*\|=r\|(I+\lambda M)w\|.
\]

The latter coefficient is nonzero because \(I+\lambda M\) is strongly monotone. Their ratio diverges as \(r^{\alpha-1}\), proving part 2. Combined with the Hölder upper bound of Theorem 5.1, the same sequence also proves the best exponent \(\alpha\).

For part 3 put \(z=\Delta u+\lambda\Delta v\) and \(h=\Delta u-\lambda\Delta v\). Expanding (6.3) gives

\[
h^T\mathcal C h+2z^T\mathcal D h\le z^T\mathcal E z,
\quad
\mathcal D=\lambda U-\lambda^{-1}V,
\quad
\mathcal E=I-\lambda U-\lambda^{-1}V.
\]

If \(\mathcal C\succeq c_0I\) for \(c_0>0\), then

\[
c_0\|h\|^2-2\|\mathcal D\|\|z\|\|h\|
\le\|\mathcal E\|\|z\|^2.
\]

Solving this scalar quadratic inequality yields \(\|h\|\le L_0\|z\|\) for a finite constant \(L_0\). It therefore yields a Lipschitz reflection, and hence a Lipschitz \(J=(I+Q)/2\), contradicting part 2.

Finally, for two graph points the normal block satisfies

\[
\langle\Delta u_N,\Delta v_N\rangle\ge a\|\Delta u_N\|^2,
\]

whereas Young's inequality gives

\[
\langle\Delta u_T,\Delta v_T\rangle
\ge-\frac1{2\lambda}\|\Delta u_T\|^2
-\frac\lambda2\|\Delta v_T\|^2.
\]

Their sum is precisely (6.3) with (6.5). This proves the survival claim without changing the actual PPA preconditioner. The normal resolvent gives \(\|y_{j+1}\|\le \eta\|y_j\|\), and the tangential inclusion gives \(\|t_{j+1}-t_j\|\le\lambda bR_D\|y_{j+1}\|^\alpha\); both block increments are summable. The additional RL–EB assertion is exactly Theorem 5.1 with its positive-scale restrictions. \(\square\)

### 6.4. Reverse separation by a Minty collision

**Proposition 6.2 (anchored convergence without any AP-RL certificate).**

On \(\mathbb R^2\), define

\[
F_0(t,y)=\{(0,y),(0,2y)\},\qquad S=\mathbb R\times\{0\}.
\]

Then \(F_0\) is monotone relative to every zero, its ordinary residual error bound is exact,

\[
d((t,y),S)=r_{F_0}(t,y)=|y|,
\]

and at \(\lambda=1\) the complete inverse is

\[
J_0(p,\xi_N)=\{(p,\xi_N/2),(p,\xi_N/3)\}.
\]

Every PPA selection is globally defined and converges to \((p_0,0)\), with set distance and point error bounded by \(2^{-j}|\xi_{N,0}|\). Nevertheless no \(\gamma>0\) and finite \(L\) can satisfy AP-RL on the complete local inverse around any solution input.

In addition, the following concrete coupled partial inequality holds with \((\Xi,N,H)=(2I,2I,3I)\):

\[
\inf_{p\in S}
\bigl\{\langle Nv,u-p\rangle+(u-p)^T(H-\Xi)(u-p)\bigr\}
\ge d_H(u,S)^2
\qquad((u,v)\in\operatorname{gph}F_0).
\tag{6.7}
\]

Here \(d_H(u,S)^2=\inf_{p\in S}(u-p)^TH(u-p)\). This is an explicit valid partial test, not an assertion that AP-RL is needed by its source framework.

**Proof.** For \(u=(t,y)\), \(v=(0,ay)\) with \(a\in\{1,2\}\), and any \(p=(s,0)\),

\[
\langle u-p,v\rangle=ay^2\ge0.
\]

The residual is \(|y|\). Solving \((p,\xi_N)=u+v\) gives the two displayed inverse values, so any selection preserves the tangential coordinate and multiplies the normal coordinate by \(1/2\) or \(1/3\) at each step. For every \(\xi_N\ne0\), the two graph points

\[
\bigl((p,\xi_N/2),(0,\xi_N/2)\bigr),\qquad
\bigl((p,\xi_N/3),(0,2\xi_N/3)\bigr)
\]

have the same Minty input. Their reflected outputs are \((p,0)\) and \((p,-\xi_N/3)\), respectively. AP-RL would require their nonzero difference to be bounded by \(L\cdot0^\gamma=0\), a contradiction. Both graph points approach the same zero as \(\xi_N\to0\), so the complete local inverse retains the obstruction. Finally, minimizing the left side of (6.7) over \(s\) gives \((2a+1)y^2\ge3y^2=d_H(u,S)^2\). \(\square\)

### 6.5. Reviewer objections and bounded responses

| Objection | Bounded response |
|---|---|
| The interface is only substitution. | The substitution is elementary. The mathematical weight lies in the exact scalar relaxation, the non-improvable denominator \(2\), positive-radius localization, and the complete transition quantifiers. |
| AP-RL is stronger than convergence needs. | Correct. Theorem 3.1 needs only moving-projection comparisons on allowed transitions; AP-RL is a stronger producer that additionally controls cross-branch consistency and Minty injectivity. |
| The relation \(\gamma q=1\) is claimed necessary. | It is not. It is the critical balance for the displayed aggregate upper bound. Proposition 3.5 converges although no compatible uniform scalar certificate exists. |
| The natural class already has a stronger proof. | Correct. Proposition 5.4 gives global convergence without the aggregate margin. The class demonstrates hand-checkable cross-active-set certificates, not exclusive convergence capability. |
| Old theories are being weakened before comparison. | The comparison fixes the operator, step, metric, domain, selection scope, and finite parameters. Proposition 6.1 preserves the successful tangentially degenerate normal-projector certificate, and Proposition 6.2 supplies the reverse obstruction. |
| The structural class is engineered rather than natural. | It is stated only as a yield-inspired reduced generalized equation built from support-function and normal-cone components. No unchanged engineering-model identity is claimed. |
| A set-distance factor is being sold as a point rate. | It is not. The paper separates the aggregate certificate factor, the direct normal distance factor, and the point-error tail; only explicit trajectories receive exact point ratios. |
| Local contraction is circular without coverage. | Coverage is a separate hypothesis. Theorem 3.1 uses the summable boundary budget to prove continuation inductively; Theorem 5.1 proves global coverage directly. |

### 6.6. Contribution boundary

The theory provides a sharp, portable sufficient certificate for a fixed Euclidean PPA once separately derived geometric and residual data are matched on the same transitions. It is not a universal verifier for arbitrary multifunctions, and failure of its scalar composition is not evidence of divergence. The support-function/normal-cone class shows that genuine Hölder reflection, a nonisolated zero set, multivalued graph structure, and explicit higher-order ordinary subregularity can coexist with complete resolvent coverage. The same class also shows why retaining native block information may be stronger than scalar aggregation. The reverse collision example rules out inclusion of the specified anchored/partial classes in the AP-RL certificate class; it does not separate them from the weaker transition-level assumptions of Theorem 3.1. The defensible conclusion is complementarity with existing semimonotone, anchored, partial, and higher-order regularity tools, together with a quantitative interface that makes their independently obtained constants usable in one trajectory theorem.

---

## T5 stage dossier

### Concept distinctions fixed in the manuscript

| Distinction | Manuscript commitment |
|---|---|
| AP-RL vs trajectory geometry | AP-RL is an all-pairs producer; Theorem 3.1 uses only moving-projection solution comparison. |
| Injectivity vs coverage | The coupled Minty chart is single-valued on its image; input coverage is assumed or proved separately. |
| Ordinary vs strong subregularity | The error bound is to the set \(S\); nonisolated zeros are allowed. |
| Hölder upper bound vs genuine exponent | A lower-bound sequence is required to rule out every larger exponent and local Lipschitzness. |
| Pair scale vs state radius | \(\delta\) controls pair distances; \(r\) controls distance to \(S\); a full radius-\(r\) pair bound safely uses \(\delta=2r\). |
| Certificate vs instance rate | \(\kappa_{\mathrm{cert}}\), direct set-distance factor, and point-error tail are reported separately. |
| Degenerate analysis metric vs algorithm | A semidefinite test may analyze the same Euclidean PPA; it is not a change of preconditioner. |
| Sharp sufficient law vs necessity | Denominator \(2\) is non-improvable for the declared uniform information; the compatibility test is not necessary for actual convergence. |

### Evidence status

- **Project derivation, proof supplied:** Theorems 3.1, 3.3, and 5.1; Corollaries 3.2 and 5.3; Propositions 3.4, 3.5, 4.1–4.2, 5.2 and 5.4, and 6.1–6.2.
- **Exact trajectory/algebra checks:** the frozen-step shear family and disk example; the disk formulas were independently evaluated on multiple trajectories to machine precision in the specialist work record.
- **Verified literature role:** the cited sources are used only for their stated definitions, algebraic parameter routes, or scoped convergence frameworks; no exhaustive-priority claim is made.
- **Pending before submission:** final bibliography normalization, nearest-prior novelty verification for the exact sharp-interface theorem, and an independent line-by-line check of the final typeset manuscript.

### T5 acceptance decision

The core satisfies the T5 requirements: it contains proof-bearing theoretical chapters, an explicit concept ledger, a six-row theory comparison table, and reviewer objection–response text. Every new judgment is tied either to a displayed proof or to a scoped source attribution. Earlier theories are represented with their native AP/AS/FS/INF quantifiers, and successful degenerate/partial alternatives are retained rather than suppressed. T5 is therefore accepted as a conceptual-analysis and theoretical-argument stage. Submission readiness is not claimed.
