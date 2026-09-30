# Local gauge–PPA theorem on a named Minty branch

> Scope. This note closes only the local PPA theorem package. It makes no
> literature, novelty, necessity, or optimality claim. Its purpose is to
> separate resolvent existence, the anchored Cayley estimate used in one
> step, the output-point error bound, and the finite localization budget.

## 1. Local data

Let \(H\) be a real Hilbert space, let \(F:H\rightrightarrows H\), let
\(\lambda>0\), and set

\[
S:=F^{-1}(0)\neq\varnothing,
\qquad
M_\lambda(u,u^*):=u+\lambda u^*.
\]

Fix \(\bar x\in S\), \(R>0\), and

\[
U:=B(\bar x,R).
\]

Fix \(0<\gamma\leq 1\), \(L\geq0\), and \(\delta>0\). The assumptions
below are required only for the active inputs

\[
\mathcal A_\delta:=\{x\in U:d(x,S)\leq\delta\}.
\]

### B. Named Minty branch and range coverage

There exist \(G\subset\operatorname{gph}F\) and a specified map

\[
\sigma:U\to G,
\qquad
M_\lambda(\sigma(x))=x
\quad(x\in U).
\tag{B}
\]

Write \(\sigma(x)=(Tx,Vx)\). Then

\[
x=Tx+\lambda Vx,
\qquad
Vx=\frac{x-Tx}{\lambda}\in F(Tx),
\qquad
Tx\in J_{\lambda F}(x).
\tag{1.1}
\]

Thus (B) is explicit Minty range coverage of the input ball, and \(T\) is
the named local resolvent branch to be iterated. It does not yet say that
the full resolvent has no remote selection.

### A. Epsilon-nearest solution anchors

For every \(x\in\mathcal A_\delta\), with \(r=d(x,S)\), there exists a
sequence \((p_n)\subset S\), allowed to depend on \(x\), such that

\[
\|x-p_n\|\longrightarrow r
\tag{A1}
\]

and

\[
\|2Tx-x-p_n\|
\leq L\|x-p_n\|^\gamma
\quad(n\in\mathbb N).
\tag{A2}
\]

Because \((p_n,0)\in\operatorname{gph}F\), (A2) is exactly the anchored
RL/Cayley inequality

\[
\|(Tx-p_n)-\lambda(Vx-0)\|
\leq
L\|(Tx-p_n)+\lambda(Vx-0)\|^\gamma .
\]

This formulation never assumes that \(S\) is proximinal or that \(P_Sx\)
exists.

### E. Gauge error bound at the resolvent output

Let \(\psi:[0,+\infty)\to[0,+\infty)\) be finite and nondecreasing, with
\(\psi(0)=0\). Assume that the following inequality is valid at the
specific point \(u=Tx\), for every \(x\in\mathcal A_\delta\):

\[
d(Tx,S)
\leq
\psi\bigl(d(0,F(Tx))\bigr).
\tag{E}
\]

Only these output points are used. A gauge defined originally on a small
residual interval causes no loss: first shrink \(\delta\) so that the
upper residuals below lie below an interior cutoff, and then extend the
gauge constantly beyond that cutoff.

## 2. One-step lemma

For \(r\geq0\), define

\[
b_\gamma(r):=\frac12(r+Lr^\gamma),
\qquad
\Phi_\gamma(r):=
\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right).
\tag{2.1}
\]

### Lemma 2.1

Under B, A, and E, every \(x\in\mathcal A_\delta\), with
\(x^+:=Tx\) and \(r=d(x,S)\), satisfies

\[
\boxed{\|x-x^+\|\leq b_\gamma(r),}
\tag{2.2}
\]

\[
\boxed{
d(0,F(x^+))
\leq
\frac{b_\gamma(r)}{\lambda}
=
\frac{r+Lr^\gamma}{2\lambda},
}
\tag{2.3}
\]

and

\[
\boxed{d(x^+,S)\leq\Phi_\gamma(r).}
\tag{2.4}
\]

#### Proof

Fix \(x\in\mathcal A_\delta\) and take \((p_n)\) from A. The identity

\[
2(x-Tx)=(x-p_n)-(2Tx-x-p_n)
\tag{2.5}
\]

gives

\[
\begin{aligned}
2\|x-Tx\|
&\leq \|x-p_n\|+\|2Tx-x-p_n\|\\
&\leq \|x-p_n\|+L\|x-p_n\|^\gamma .
\end{aligned}
\tag{2.6}
\]

Letting \(n\to\infty\) proves (2.2). No distance infimum is assumed to be
attained.

By (1.1), \((x-Tx)/\lambda\in F(Tx)\), and hence

\[
d(0,F(Tx))
\leq
\frac{\|x-Tx\|}{\lambda}.
\tag{2.7}
\]

Combining (2.7) with (2.2) proves (2.3). Finally, E, (2.3), and
monotonicity of \(\psi\) give

\[
\begin{aligned}
d(Tx,S)
&\leq \psi\bigl(d(0,F(Tx))\bigr)\\
&\leq \psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right)
=\Phi_\gamma(r),
\end{aligned}
\]

which is (2.4). \(\square\)

The proof uses no all-pairs inequality. It needs the anchored inequality
only along one epsilon-nearest sequence for each active input.

## 3. Local gauge–PPA theorem

### Theorem 3.1

Assume B, A, and E, and suppose

\[
c_\gamma:=
\limsup_{r\downarrow0}
\frac{\Phi_\gamma(r)}{r}
<1.
\tag{3.1}
\]

Choose \(c_\gamma<\theta<1\). Then there exists
\(0<\delta_\theta\leq\delta\) such that

\[
\Phi_\gamma(r)\leq\theta r
\qquad(0<r\leq\delta_\theta).
\tag{3.2}
\]

Let \(x^0\in U\), set \(r_0=d(x^0,S)\), and assume

\[
r_0\leq\delta_\theta
\tag{3.3}
\]

and the strict outer-radius margin

\[
\boxed{
\|x^0-\bar x\|+B_\gamma(r_0,\theta)<R,
}
\tag{3.4}
\]

where

\[
B_\gamma(r,\theta):=
\frac12\left(
\frac{r}{1-\theta}
+
\frac{Lr^\gamma}{1-\theta^\gamma}
\right).
\tag{3.5}
\]

Then the named local PPA iteration

\[
x^{k+1}=T(x^k)
\tag{3.6}
\]

is well-defined for every \(k\), stays in \(U\), has finite length, and
converges in norm to a point \(x^\infty\in S\). More precisely, with
\(r_k=d(x^k,S)\),

\[
r_k\leq\theta^k r_0,
\tag{3.7}
\]

\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|
\leq B_\gamma(r_0,\theta),
\tag{3.8}
\]

and

\[
\|x^k-x^\infty\|
\leq B_\gamma(r_k,\theta).
\tag{3.9}
\]

No closedness of \(S\) and no continuity of \(T\) is needed. The endpoint
anchored estimate itself puts the interior limit in \(S\).

#### Proof

If \(r_0=0\), (2.2) gives \(Tx^0=x^0\); then (1.1) gives
\(0\in F(x^0)\). The orbit is constant. Hence assume \(r_0>0\).

We prove by induction that

\[
x^k\in U,
\qquad
r_k\leq\theta^k r_0\leq\delta_\theta.
\tag{3.10}
\]

This is true at \(k=0\). Suppose it is true at \(k\). If \(r_k=0\),
(2.2) makes \(x^k\) a fixed point and the orbit is constant thereafter.
If \(r_k>0\), then \(x^k\in\mathcal A_\delta\), and (2.4), (3.2) give

\[
r_{k+1}
\leq\Phi_\gamma(r_k)
\leq\theta r_k
\leq\theta^{k+1}r_0.
\tag{3.11}
\]

For every preceding index \(j\), (2.2) and (3.10) give

\[
\begin{aligned}
\|x^{j+1}-x^j\|
&\leq\frac12(r_j+Lr_j^\gamma)\\
&\leq\frac12\bigl(\theta^j r_0
+L\theta^{\gamma j}r_0^\gamma\bigr).
\end{aligned}
\tag{3.12}
\]

Therefore

\[
\begin{aligned}
\|x^{k+1}-\bar x\|
&\leq \|x^0-\bar x\|
+\sum_{j=0}^{k}\|x^{j+1}-x^j\|\\
&\leq \|x^0-\bar x\|+B_\gamma(r_0,\theta)\\
&<R.
\end{aligned}
\tag{3.13}
\]

Thus \(x^{k+1}\in U\), closing the induction. Notice that no global
self-map condition \(T(U)\subset U\) was assumed.

Summing (3.12) proves (3.8); hence \((x^k)\) is Cauchy. Let
\(x^k\to x^\infty\). From (3.4) and (3.13),

\[
\|x^\infty-\bar x\|
\leq
\|x^0-\bar x\|+B_\gamma(r_0,\theta)
<R,
\tag{3.14}
\]

so \(x^\infty\in U\). The distance to any nonempty set is 1-Lipschitz.
Together with (3.7), this yields

\[
d(x^\infty,S)=0.
\tag{3.15}
\]

Apply (2.2) at the active input \(x^\infty\). Equation (3.15) gives

\[
\|x^\infty-Tx^\infty\|
\leq b_\gamma(0)=0.
\tag{3.16}
\]

Thus \(Tx^\infty=x^\infty\), and (1.1) yields

\[
0=\frac{x^\infty-Tx^\infty}{\lambda}\in F(x^\infty).
\]

Therefore \(x^\infty\in S\). Applying (3.12) from index \(k\) onward,
with \(r_k\) in place of \(r_0\), proves (3.9). \(\square\)

The endpoint quantifier in A is doing real work here. If A is assumed only
at the generated iterates, rather than at every active input, then the last
step must instead be closed by either local closedness of \(S\), or
continuity of \(T\) at \(x^\infty\) together with (1.1).

### The two values of \(\gamma\)

For \(0<\gamma<1\),

\[
B_\gamma(r_0,\theta)
=
\frac12\left(
\frac{r_0}{1-\theta}
+
\frac{Lr_0^\gamma}{1-\theta^\gamma}
\right).
\tag{3.17}
\]

The second term pays for the potentially larger tangential/Hölder step
scale \(r_k^\gamma\).

For \(\gamma=1\),

\[
B_1(r_0,\theta)
=
\frac{(1+L)r_0}{2(1-\theta)},
\tag{3.18}
\]

and

\[
\Phi_1(r)
=
\psi\!\left(\frac{1+L}{2\lambda}r\right).
\tag{3.19}
\]

The coefficient is \(1+L\), not \(L\), because \(r\) and
\(Lr^\gamma\) have the same order at \(\gamma=1\).

### Convenient gauge-envelope tests

Condition (3.1) is the primary scalar condition. If
\(0<\gamma<1\) and \(L>0\), the sufficient condition

\[
\limsup_{t\downarrow0}
\frac{\psi(t)}{t^{1/\gamma}}
<
\left(\frac{2\lambda}{L}\right)^{1/\gamma}
\tag{3.20}
\]

implies (3.1), since for
\(t(r)=(r+Lr^\gamma)/(2\lambda)\),

\[
\frac{\psi(t(r))}{r}
=
\frac{\psi(t(r))}{t(r)^{1/\gamma}}
\left(
\frac{r^{1-\gamma}+L}{2\lambda}
\right)^{1/\gamma}.
\tag{3.21}
\]

For \(\gamma=1\), the corresponding sufficient condition is

\[
\limsup_{t\downarrow0}\frac{\psi(t)}{t}
<
\frac{2\lambda}{1+L}.
\tag{3.22}
\]

Neither (3.20) nor (3.22) is asserted to be necessary.

## 4. All-pairs RL as a branch-verification device

### Proposition 4.1

Let \(G\subset\operatorname{gph}F\) satisfy

\[
\|(u-v)-\lambda(u^*-v^*)\|
\leq
L\|(u-v)+\lambda(u^*-v^*)\|^\gamma
\tag{4.1}
\]

for every \((u,u^*),(v,v^*)\in G\). Then \(M_\lambda|_G\) is injective.
If also

\[
U\subset M_\lambda(G),
\tag{4.2}
\]

the restricted inverse

\[
\sigma=(M_\lambda|_G)^{-1}:U\to G
\]

is well-defined and gives B with \(T=\pi_1\circ\sigma\).

Let

\[
S_G:=\{p\in S:(p,0)\in G\}.
\]

If

\[
d(x,S_G)=d(x,S)
\quad(x\in\mathcal A_\delta),
\tag{4.3}
\]

then A holds. Moreover, the restricted reflected map \(R_G:=2T-I\)
satisfies

\[
\|R_Gx-R_Gy\|
\leq L\|x-y\|^\gamma
\quad(x,y\in U),
\tag{4.4}
\]

and consequently

\[
\|Tx-Ty\|
\leq
\frac12\bigl(\|x-y\|+L\|x-y\|^\gamma\bigr).
\tag{4.5}
\]

#### Proof

If two points of \(G\) have the same Minty input, then the right side of
(4.1) is zero, so its left side is zero. Adding and subtracting the two
zero difference equations shows equality of both graph coordinates.
This proves injectivity and, with (4.2), defines \(\sigma\).

For active \(x\), (4.3) supplies \(p_n\in S_G\) with
\(\|x-p_n\|\leq d(x,S)+1/n\). Apply (4.1) to
\(\sigma(x)=(Tx,Vx)\) and \((p_n,0)\). Since
\(Tx+\lambda Vx=x\), this is exactly (A2), while (A1) follows from the
choice of \(p_n\). Applying (4.1) to \(\sigma(x)\) and \(\sigma(y)\)
gives (4.4), and \(T=(I+R_G)/2\) gives (4.5). \(\square\)

All-pairs RL is therefore sufficient for restricted Minty injectivity,
anchor verification, and continuity. The convergence proof itself uses
only B and A.

### Full-resolvent branch exclusion

All-pairs RL on \(G\) does not control graph points outside \(G\). To make
the named branch equal to the full resolvent on \(U\), one must additionally
assume

\[
M_\lambda^{-1}(U)\cap\operatorname{gph}F
\subset G.
\tag{4.6}
\]

Then \(J_{\lambda F}(x)=\{Tx\}\) for \(x\in U\). Without (4.6), the
proved algorithm is the named iteration \(x^{k+1}=Tx^k\), not an arbitrary
selection \(x^{k+1}\in J_{\lambda F}(x^k)\).

## 5. Power error bounds

Assume E with

\[
\psi(t)=\rho t^q,
\qquad
\rho>0,
\qquad
q>0.
\tag{5.1}
\]

Lemma 2.1 gives the certified one-step bound

\[
\boxed{
r_+
\leq
\frac{\rho}{(2\lambda)^q}
(r+Lr^\gamma)^q,
}
\tag{5.2}
\]

where \(r=d(x,S)\) and \(r_+=d(Tx,S)\).

### Corollary 5.1: \(0<\gamma<1\)

Assume \(0<\gamma<1\), \(L>0\), and put \(p:=\gamma q\). For every
\(0<\delta_0\leq\delta\) and every active input with
\(0\leq r\leq\delta_0\),

\[
r_+\leq C_{\delta_0}r^p,
\qquad
C_{\delta_0}
:=
\frac{\rho}{(2\lambda)^q}
(\delta_0^{1-\gamma}+L)^q.
\tag{5.3}
\]

#### (i) Supercritical case \(p>1\)

Choose \(0<\delta_0\leq\delta\) small enough that

\[
\theta_{\delta_0}
:=
C_{\delta_0}\delta_0^{p-1}
<1.
\tag{5.4}
\]

Then \(r_+\leq\theta_{\delta_0}r\) on the active radius. Theorem 3.1
applies whenever \(r_0\leq\delta_0\) and

\[
\|x^0-\bar x\|
+B_\gamma(r_0,\theta_{\delta_0})
<R.
\tag{5.5}
\]

Along the resulting orbit,

\[
r_{k+1}=O(r_k^{\gamma q}).
\tag{5.6}
\]

Unless the orbit terminates finitely,
\(r_{k+1}/r_k\to0\).

#### (ii) Critical case \(p=1\)

Here \(q=1/\gamma\). Define

\[
\boxed{
\kappa_\gamma
:=
\rho\left(\frac{L}{2\lambda}\right)^q.
}
\tag{5.7}
\]

If \(\kappa_\gamma<1\), choose \(0<\delta_0\leq\delta\) so that

\[
\theta_{\delta_0}
:=
\frac{\rho}{(2\lambda)^q}
(\delta_0^{1-\gamma}+L)^q
<1.
\tag{5.8}
\]

Theorem 3.1 applies when \(r_0\leq\delta_0\) and (5.5) holds, and

\[
\limsup_{\substack{k\to\infty\\r_k>0}}
\frac{r_{k+1}}{r_k}
\leq
\kappa_\gamma
<1.
\tag{5.9}
\]

The ratio assertion is read for a nonterminating orbit (equivalently, one
with infinitely many positive \(r_k\)); finite termination is already a
stronger conclusion.

#### (iii) Subcritical case \(p<1\)

Bound (5.2) alone does not imply (3.1). This theorem gives no convergence
or divergence conclusion in that region.

The factorization

\[
r+Lr^\gamma
=
r^\gamma(r^{1-\gamma}+L)
\]

proves all three assertions above.

### Corollary 5.2: \(\gamma=1\)

For \(\gamma=1\), (5.2) becomes

\[
\boxed{
r_+\leq A_1r^q,
\qquad
A_1:=\rho\left(\frac{1+L}{2\lambda}\right)^q.
}
\tag{5.10}
\]

#### (i) \(q>1\)

Choose \(0<\delta_0\leq\delta\) so that

\[
\theta_{\delta_0}
:=
A_1\delta_0^{q-1}
<1.
\tag{5.11}
\]

If \(r_0\leq\delta_0\) and

\[
\|x^0-\bar x\|
+
\frac{(1+L)r_0}{2(1-\theta_{\delta_0})}
<R,
\tag{5.12}
\]

then the orbit converges and
\(r_{k+1}=O(r_k^q)\).

#### (ii) \(q=1\)

Define

\[
\boxed{
\kappa_1
:=
\rho\frac{1+L}{2\lambda}.
}
\tag{5.13}
\]

If \(\kappa_1<1\), choose any
\(\kappa_1<\theta<1\). The direct bound
\(r_+\leq\kappa_1r\leq\theta r\), together with

\[
r_0\leq\delta
\]

and

\[
\|x^0-\bar x\|
+
\frac{(1+L)r_0}{2(1-\theta)}
<R,
\tag{5.14}
\]

gives convergence. Moreover,

\[
\limsup_{\substack{k\to\infty\\r_k>0}}
\frac{r_{k+1}}{r_k}
\leq\kappa_1<1.
\tag{5.15}
\]

Again, the ratio assertion concerns a nonterminating orbit.

#### (iii) \(q<1\)

Bound (5.10) alone supplies no local contraction theorem.

### Upper order is not exact order

Equations (5.6) and (5.10) are one-step upper-order bounds. Exact
Q-order \(p\) would require a matching positive lower bound, for example

\[
0<
\liminf_{\substack{k\to\infty\\r_k>0}}
\frac{r_{k+1}}{r_k^p}
\leq
\limsup_{\substack{k\to\infty\\r_k>0}}
\frac{r_{k+1}}{r_k^p}
<+\infty.
\tag{5.16}
\]

Neither anchored/all-pairs RL nor E supplies the first inequality. Finite
termination also precludes a positive exact-order constant.

The coefficients \(\kappa_\gamma\) and \(\kappa_1\) are strict sufficient
coefficients produced by Lemma 2.1. They are not proved necessary or
optimal. Equality to one, or a value above one, means only that this
contraction proof is inconclusive.

## 6. Assumption ledger and example stress tests

| Assumption | Exact role | Not implied |
|---|---|---|
| Named Minty chart B | Defines the iterate and supplies a graph point for every input in \(U\). | RL does not imply range coverage. |
| All-pairs RL on \(G\) | Sufficient for restricted Minty injectivity, A, and continuity. | It does not exclude remote branches outside \(G\). |
| Epsilon-nearest anchored RL A | Gives (2.2) without a projection. | Distance closeness does not control tangential location. |
| Error bound E at \(Tx\) | Converts the selected residual into (2.4). | It neither creates a resolvent step nor excludes vacuity off \(\operatorname{dom}F\). |
| Strict scalar condition (3.1) | Gives geometric decay of \(r_k\). | A one-step scaling law alone is not convergence. |
| Margin (3.4) | Pays for all motion and keeps the orbit in \(U\). | Small \(d(x^0,S)\) alone is not an invariant localization. |
| Endpoint use of A | Forces \(Tx^\infty=x^\infty\), hence \(x^\infty\in S\). | Closedness of \(S\) is unnecessary under the stated endpoint quantifier. |

The four requested catalog examples test distinct gaps:

- GX-074: all-pairs RL on the natural domain and vacuous fixed-target error
  bounds do not put an input ball in the Minty range. This necessitates
  B/(4.2).
- GX-071: \(r_{k+1}=r_k^{\gamma q}\) can coexist with tangential motion
  of size \(r_k^\gamma\). Thus a theorem of this form needs an explicit
  tangential localization mechanism; the whole rectangle need not be a
  self-map.
- GX-072: the all-pairs upper exponent \(\gamma q\) can be strictly below
  the actual orbit order \(q\). Exact \(\gamma q\)-order is not a universal
  conclusion.
- GX-073: an anchored one-step power law can expand every sufficiently
  small nonzero point and leave the window. One-step scale is not a
  convergence rate without scalar contraction and localization.

## 7. Final logical chain

\[
\begin{gathered}
\text{named Minty branch on an input ball}
+\text{epsilon-nearest anchored RL}\\
\Longrightarrow
\|x-Tx\|\leq\tfrac12(r+Lr^\gamma)\\
+\quad
\text{gauge error bound evaluated at }Tx\\
\Longrightarrow
d(Tx,S)
\leq
\psi\!\left(\frac{r+Lr^\gamma}{2\lambda}\right)\\
+\quad
\limsup_{r\downarrow0}
\frac{\psi((r+Lr^\gamma)/(2\lambda))}{r}<1\\
+\quad
\text{strict finite-length margin}\\
\Longrightarrow
x^{k+1}=Tx^k\to x^\infty\in S.
\end{gathered}
\]

All-pairs RL belongs one level earlier: it is a clean sufficient condition
for constructing the unique restricted Minty chart and verifying the
anchored estimate. It is not the weakest convergence assumption.

## Expert contract

- task_id: RL-FND-PPA-02
- project: monotonicity-regularity-seesaw-2026-09
- role: strict mathematical proof specialist; localized gauge–PPA theorem only
- stage: RL foundations theorem closure and proof gate
- inputs_reviewed: upload/01-RL_Submonotonicity-.md; work/rl_proof_referee.md; research/example_properties.md (GX-071–GX-074); work/c_gx066_077.md (only detailed GX-071–GX-074 algebra used to stress-test margin/rate claims)
- methods: quantifier audit; graph/Minty-domain separation; epsilon-nearest-point proof; scalar recurrence; explicit geometric step-sum; endpoint fixed-point argument; GX-071–GX-074 stress tests
- primary_output: work/rl_foundations_ppa_theorem.md
- proved_results: one-step step/residual/gauge recurrence; finite-length convergence of a named branch; explicit invariant margin and tail bound; limit membership in S without proximinality, closedness of S, or continuity of T; all-pairs graph-to-branch verification; separate power corollaries for \(0<\gamma<1\) and \(\gamma=1\)
- minimality_findings: the convergence proof needs only epsilon-nearest anchored RL; all-pairs RL is sufficient for restricted Minty injectivity but unnecessary after a branch is named; E is needed only at \(T(x)\); full-resolvent branch exclusion is separate
- negative_results: RL does not imply Minty range coverage; local all-pairs RL does not control remote selections; distance closeness alone is not invariant; \(\gamma q\) is an upper exponent, not a universal exact rate; the critical coefficients are sufficient but not proved necessary or sharp
- unresolved_questions: joint optimality of the step and critical coefficients; necessity in narrower structural classes; natural versus reverse-calibrated exact-order realizations
- consistency_checks: factor \(1/2\) retained; \(\gamma=1\) uses \(1+L\); E evaluated at the resolvent output; strict radius margin places the limit inside \(U\); \(r=0\) handled; no projection onto \(S\)
- literature_search: not performed, by task instruction
- main_files_modified: none
- confidence: high (0.96) for the stated theorem and proof; medium-high (0.88) that A is the cleanest readable form of the weakest anchored requirement
- recommended_next_action: independent line-by-line referee pass, then integrate only Theorem 3.1, Proposition 4.1, and Corollaries 5.1–5.2 into the optimized RL foundations manuscript

```yaml
contract_version: "1.0"
expert_skill: "independent-proof-analysis"
project_id: "monotonicity-regularity-seesaw-2026-09"
paper_family: "T"
stage_id: "T2"
task_id: "RL-FND-PPA-02"
task_status: "COMPLETE"
inputs_reviewed:
  - "upload/01-RL_Submonotonicity-.md"
  - "work/rl_proof_referee.md"
  - "research/example_properties.md (GX-071--GX-074)"
  - "work/c_gx066_077.md (GX-071--GX-074 detailed algebra only)"
outputs:
  - "work/rl_foundations_ppa_theorem.md"
evidence_status:
  - label: "VERIFIED_USER_MATERIAL"
    item: "The uploaded RL draft, the prior proof-referee report, and the catalogued GX-071--GX-074 statements were reviewed locally."
  - label: "VERIFIED_ALG"
    item: "The one-step bound, residual recurrence, scalar contraction, invariant-margin estimate, finite-length bound, endpoint membership argument, Minty injectivity, and power corollaries were independently rederived line by line."
  - label: "EXECUTED_LOCAL"
    item: "Equation delimiters, control characters, required sections, and Markdown parsing were checked in the shared workspace."
  - label: "AI_INFERENCE"
    item: "Assumption-minimality judgments and integration recommendations are mathematical assessments, not external novelty evidence."
assumptions:
  - "H is a real Hilbert space, lambda is fixed and strictly positive, and S=F^{-1}(0) is nonempty."
  - "The named Minty branch is defined on the stated open input ball and returns graph points of F."
  - "The epsilon-nearest anchored inequality and output-point error bound hold for every active input, including any interior limit with distance zero."
  - "The gauge is finite and nondecreasing on the residual range used by the proof, with psi(0)=0."
  - "Arbitrary selections of the full resolvent are covered only when the separate branch-exclusion condition is imposed."
author_input_needed: []
manual_actions: []
quality_checks:
  - "Printed complete quantifiers for the named branch, Minty range coverage, active input set, epsilon-nearest anchors, and output-point error bound."
  - "Used epsilon-nearest zero points and never assumed that S is proximinal."
  - "Proved the factor-one-half step estimate directly from the anchored Cayley inequality."
  - "Proved the explicit invariant budget, finite length, geometric distance decay, tail bound, and limit membership in S."
  - "Separated anchored assumptions from the stronger all-pairs condition and separated the restricted branch from the full resolvent."
  - "Handled 0<gamma<1 and gamma=1 separately; verified that the gamma=1 critical coefficient contains 1+L."
  - "Separated one-step upper order from exact Q-order and preserved the nonsharp status of the critical coefficients."
  - "Stress-tested coverage, invariance, and rate language against GX-071--GX-074."
  - "Performed no literature search and modified no RL main manuscript."
conflicts:
  - conflict_id: "RL-PPA-C01"
    conflict_type: "domain_and_existence"
    claim: "Local RL and an error bound alone make the PPA available from every sufficiently close input."
    source_or_locator: "upload/01-RL_Submonotonicity-.md, Theorems 1--3; work/rl_proof_referee.md, Sections 4.1 and 5"
    competing_interpretations:
      - "RL supplies Minty injectivity but not range coverage."
      - "A named branch on an explicitly covered input ball is required."
    recommended_resolution: "Adopt Assumption B and Proposition 4.1 from this output."
  - conflict_id: "RL-PPA-C02"
    conflict_type: "branch_quantifier"
    claim: "A theorem for a local RL graph controls arbitrary selections of the full resolvent."
    source_or_locator: "upload/01-RL_Submonotonicity-.md, PPA inclusion notation; work/rl_proof_referee.md, Section 4.2"
    competing_interpretations:
      - "Iterate the named restricted branch."
      - "Claim arbitrary full-resolvent PPA only after branch exclusion."
    recommended_resolution: "Use the named iteration and print condition (4.6) whenever a full-resolvent conclusion is intended."
  - conflict_id: "RL-PPA-C03"
    conflict_type: "localization"
    claim: "Small distance to S is by itself an invariant local hypothesis."
    source_or_locator: "upload/01-RL_Submonotonicity-.md, localization paragraph; GX-071"
    competing_interpretations:
      - "Distance controls only the normal coordinate for a nonisolated solution set."
      - "The total step budget must fit strictly inside an outer input ball."
    recommended_resolution: "Adopt the explicit margin (3.4)."
  - conflict_id: "RL-PPA-C04"
    conflict_type: "claim_strength"
    claim: "The exponent gamma*q and the displayed critical coefficient are universally exact or sharp."
    source_or_locator: "upload/01-RL_Submonotonicity-.md, Theorems 1--2; GX-071--GX-072"
    competing_interpretations:
      - "A one-step upper-order guarantee and sufficient critical coefficient."
      - "Exact Q-order or a necessary sharp threshold."
    recommended_resolution: "Retain the upper-order language and require a separate two-sided asymptotic theorem for exact order."
conflict_resolution_status: "RESOLVED_IN_OUTPUT_PENDING_MERGE"
merge_permission: "orchestrator_only"
recommended_next_action: "Run one independent line-by-line proof-referee pass; if it finds no defect, merge Theorem 3.1, Proposition 4.1, and Corollaries 5.1--5.2 into the optimized RL foundations manuscript."
stage_acceptance_recommendation: "PASS_CANDIDATE"
```
