# Zero-set-preserving branch restrictions: actual GPPA imports of original trajectories

Independent reverse audit, 2026-10-09. This file is an essential qualification to complete-original-graph exclusions C200/C201/C203/C204. Those exclusions remain valid. However, deleting an inactive graph branch can leave the original ordinary PPA unchanged on its relevant invariant input basin, retain the entire original zero set, and permit the archived GPPA theorem to prove convergence of the **same physical sequence**. A claim of convergence nonderivability from GPPA is therefore stronger than the established full-graph noninclusion and is false for the cap witness below.

The external interfaces are `sources/gppa_2608.01584v1.pdf`: Definitions 1/3/4/5 pp.4–6, Theorem 1 p.6 and Theorem 2 pp.7–8. The source requires a kernel on all H, nonempty zeros, all-pairs pair monotonicity (Theorem 1) or ASM (Theorem 2), and warped range coverage. Theorem 2(a) controls kernel point distances to a fixed zero; Theorem 1(c) controls ordinary distance to the zero set when the inverse is R-continuous at zero. Physical bridges below are independently proved and cannot be omitted.

<a id="br-cap"></a>
## 1. Complete positive cap branch: global ASM, global coverage, original positive trajectories

Use exactly C137's D_y and delete only its negative normal branch:

`F_+(xi,eta,y)={(-2sqrt(y),−D_y(eta),3y)}` for y>=0, and the empty set for y<0.

This is a complete, closed single-valued graph on the same closed half-space. Its zero set remains **the original entire sheet** S=R²×{0}; at y=0 D_0 is zero for every eta. For any original input x=(z,p,r) with r>=0, the complete ordinary resolvent is exactly the original cap T:

`J_{F_+}(z,p,r)=(z+sqrt(r), p+sqrt(min(p_+,r)), r/4)=J_F(z,p,r)`.

The original normal equation for this branch is r=4y. The first and second coordinate inversions are the same original C137 inversions, and hence no additional outputs appear. For r<0 this restricted ordinary resolvent is empty; it is not the original complete algorithm on all R³.

Define a globally single-valued kernel

`v(xi,eta,y)=(-2sqrt(y_+),0,y_+)`, and choose GPPA step h=1.

For original restricted graph points y,z>=0,

`<f_+(x)−f_+(x'),v(x)−v(x')>`

`=4(sqrt(y)−sqrt(z))²+3(y−z)² >= ||v(x)−v(x')||²`.

Thus the full `(F_+,v)` pair is 1-ASM, independent of the variation of D or the tangential positions. The second kernel component is zero, not −D; this deliberately allows arbitrary tangential input positions without an extra sign condition in the all-pairs proof.

**All-input warped coverage.** For any input x=(xi,eta,r), put a=r_+. The complete equation `v(x) in v(u)+F_+(u)` forces output y=a/4 from its third component. Its first component is then automatic: −2sqrt(a)=−4sqrt(a/4). The second component forces D_y(eta')=0. For y>0, this means eta'<=0; for y=0 every eta' is allowed. The first output coordinate is arbitrary. Therefore

`J^v_{F_+}(x)=R×(−infinity,0]×{a/4}` if a>0,

and `J^v_{F_+}(x)=S` if a=0.

Every input in R³ has a warped output, so the source range-coverage gate is genuinely closed. No ordinary full-domain gate is needed for GPPA; it is the warped coverage that matters.

**Complete inverse R-Lipschitz continuity.** Every restricted graph value at positive y has third component 3y, hence `d(u,S)=y<=||f||/3`; at y=0 the distance is zero. Thus for every right-hand side w, `F_+^{-1}(w) subset S+(||w||/3)B`. This is source Definition 5 with global radius and linear modulus 1/3, not a selected-residual substitution.

**Physical bridge and import.** For initial eta0<=0 and r0>0, the original complete cap trajectory stays in eta=eta0 and r>=0. Its first-coordinate invariant is

`I=xi_k+2sqrt(r_k)=xi0+2sqrt(r0)`.

The point x_*=(I,eta0,0) is an original and restricted zero, fixed from initial data before convergence is assumed. Along every such original trajectory,

`v(x_k)−v(x_*)=(xi_k−I,0,r_k)=x_k−x_*`.

Each original ordinary step satisfies the full F_+ GPPA equation; Theorem 2(a), applied to this complete restricted graph and kernel, therefore proves physical point R-linear convergence to x_* (the printed bound has factor 1/sqrt(3)). A geometric physical point tail implies finite physical length. The direct cap formula has sharper factor 1/2; the external theorem's bound need not be sharp to constitute a genuine convergence import.

**Negative normal initial value.** If eta0<=0 and r0<0, the original complete F uses its negative branch only for its first step:

`x1=(xi0+sqrt(|r0|),eta0,|r0|/4)`.

Apply the restricted GPPA theorem from x1 onward; one finite original prefix does not affect convergence or finite length. The same eventual zero is I=xi0+2sqrt(|r0|). This is a tail import, not an equality of algorithms at the negative first input. At r0=0 the original trajectory is stationary. Initial eta0>0 generally fails this kernel's physical GPPA selection/bridge and is not covered by this argument.

<a id="br-log"></a>
## 2. Positive logarithmic branch: mere-monotone GPPA with a Dini tail bridge

Fix a>1 and use the exact canonical GM26 profile, including its positive-slope tangent continuation. Define the complete positive branch

`F_{a,+}(t,y)={(-ell_a(4y),3y)}` for y>=0, empty otherwise.

It is closed and retains the entire original zero line R×{0}. Its complete ordinary resolvent agrees with the original complete log resolvent on every input r>=0:

`J_{F_{a,+}}(t,r)=(t+ell_a(r),r/4)`.

Set

`E_a(y)=Σ_{j=0}^infinity ell_a(4^(−j)y)` for y>0, `E_a(0)=0`,

and `v(t,y)=(-E_a(y_+),y_+)`, h=1.

**Finiteness, monotonicity and continuity at zero.** For sufficiently small y, put A=log(e/y) and b=log4; every term is `(A+jb)^(−a)`. The positive decreasing summands satisfy the integral bounds

`A^(1−a)/(b(a−1)) <= E_a(y) <= A^(−a)+A^(1−a)/(b(a−1))`.

Therefore E_a(y) is finite and tends to zero at y=0 when a>1. For arbitrary positive y, only finitely many terms precede the canonical logarithmic region; the remaining tail obeys these bounds. E_a is strictly increasing, since every ell term is. No convergence of a physical orbit was assumed to establish these properties.

**All-pairs monotonicity.** For restricted graph points at y,z>=0,

`<f(y)−f(z),v(y)−v(z)>`

`=[ell_a(4y)−ell_a(4z)][E_a(y)−E_a(z)]+3(y−z)² >=0`.

Thus the pair meets source Definition 1 globally on the complete restricted graph. It need not meet ASM. In fact this explicit kernel cannot have a positive global ASM constant: comparing y with zero, the ratio of that inner product to ||v(y)||² tends to zero. The tail estimate gives E_a(y) asymptotic to A^(1−a)/(b(a−1)), while ell_a(4y) is asymptotic to A^(−a), and y is negligible compared with either. Hence the ratio is asymptotic to b(a−1)/A.

**All-input warped coverage.** The tail identity is

`E_a(y)−E_a(y/4)=ell_a(y)`.

For any input r, let output z=r_+/4. The normal equation is r_+=4z. Its tangential equation is automatic because

`E_a(r_+)=E_a(z)+ell_a(4z)`.

The output tangential coordinate is arbitrary, so the warped fiber is `R×{r_+/4}` for every real input. The source coverage gate is satisfied on the whole space. Complete inverse R-Lipschitz continuity at zero has constant 1/3 by the positive normal graph value 3y; the graph is closed as well.

**Physical conclusion and what actually supplies it.** For an original positive trajectory define I=t0+E_a(r0). One-step algebra gives `t_k+E_a(r_k)=I` and

`v(x_k)−v(I,0)=x_k−(I,0)`.

Theorem 1(c) gives r_k=d(x_k,S) tending to zero; continuity E_a(y)->0 gives physical point convergence by this explicit bridge. The total tangential displacement is E_a(r0), by the tail identity, and the total positive normal displacement is r0. Consequently the physical path length is at most E_a(r0)+r0. This length assertion uses the extra tail identity and monotone coordinate geometry; it is **not** a consequence of printed Theorem 1 alone. The kernel construction encodes the Dini summability condition rather than replacing it with a weaker unrelated assumption.

For r0<0, use the original first step `(t0+ell_a(|r0|),|r0|/4)` and import the positive tail; the invariant is I=t0+E_a(|r0|). At r0=0 the orbit is stationary. For 0<a<=1, the defining tail E_a(y) diverges for every y>0; this construction is unavailable, and the original divergent physical trajectories are not claimed covered. Their failure of convergence is not evidence for novelty of a positive finite-length theorem.

<a id="br-superlinear"></a>
## 3. Positive superlinear branch on a fixed small collar: ASM import

Use exact C141 data gamma∈(0,1), nu>1, A,B>0 and its original positive branch. Choose a fixed

`0<R<min{1,nu^(−1/(nu−1))}`,

and define a new complete subrelation G by retaining that positive branch only for output heights 0<=y<=R^nu, with **all** original tangential coordinates and values on that branch. Thus

`G(xi,eta,y)={(-A y^(gamma/nu), tau_{y^(1/nu)}(eta)−eta, y^(1/nu)−y)}`

on this collar, empty outside. It is closed and retains the entire original zero sheet S=R²×{0}. For every ordinary input normal r∈[0,R], its complete ordinary resolvent agrees with the original full F resolvent, for all tangential input coordinates. The ordinary normal equation is r=y^(1/nu); thus y=r^nu.

Put

`E(y)=Σ_{j=0}^infinity y^(gamma nu^j)` for 0<=y<1,

`b(y)=min{R,max{y,0}}`,

`v(xi,eta,y)=(-h A E(b(y)),0,h b(y))`, h>0 arbitrary.

The series is finite for y<1, positive and increasing, and E(y)->0 at zero. On y<=R it is bounded by `y^gamma/[1−R^(gamma(nu−1))]`, since nu^j>=1+j(nu−1). Its exact identity is `E(y)−E(y^nu)=y^gamma`. Clipping defines a finite single-valued kernel on **all** R³, which is essential for the source coverage contract.

**Full ASM on G.** Let phi(y)=y^(gamma/nu). On the output collar y<=R^nu, write t=phi(y)<=R^gamma. Then

`E(y)=Σ_{j=1}^infinity t^(nu^j)`.

As a function of t it has a finite Lipschitz constant

`K_R=Σ_{j=1}^infinity nu^j R^(gamma(nu^j−1))`.

The derivative series converges uniformly on 0<=t<=R^gamma, because its consecutive upper-bound ratios tend to zero. Hence `|Delta E|<=K_R |Delta phi|`; the differences have the same sign. Also g(y)=y^(1/nu)−y has derivative at least

`m_R=R^(1−nu)/nu−1>0`

on the positive output collar, so `Delta g Delta y>=m_R(Delta y)²`, including comparisons to zero by integration. The second kernel component is constant. Therefore

`<Delta f,Delta v>=h A² Delta phi Delta E+h Delta g Delta y`

`>= [1/(h K_R)] (h A Delta E)² + [m_R/h](h Delta y)²`

`>= epsilon ||Delta v||²`,

where epsilon=min{1/(h K_R),m_R/h}>0. This is global all-pairs ASM on the **complete truncated G**, not a condition merely along the selected trajectory. No monotonicity of the original positive normal branch outside this collar is required.

**All-input warped coverage.** For any input normal r let c=b(r). A graph output y belongs to [0,R^nu], so b(y)=y. Its normal warped equation is

`h c=h y+h(y^(1/nu)−y)=h y^(1/nu)`,

forcing y=c^nu. The tangential first equation follows from `E(c)=c^gamma+E(c^nu)`. The second equation requires `tau_c(eta')−eta'=0`, which allows every eta'<=0 when c>0 and every eta' when c=0. The output first coordinate is arbitrary. Thus every input in R³ has a warped output. Clipping does not remove coverage: it directs all large positive inputs to the collar's endpoint, and negative inputs to the zero sheet.

Complete inverse R-Lipschitz continuity follows from `g(y)>=m_R y`: every graph value has norm at least m_R y, so its inverse obeys the global modulus 1/m_R to S. At zero this is again a complete-fiber inequality.

**Original physical trajectories and their bridge.** For eta0<=0 and 0<r0<=R, the original full F ordinary trajectory stays in this basin and has r_{k+1}=r_k^nu. The invariant is

`I=xi_k+A E(r_k)=xi0+A E(r0)`.

With x_*=(I,eta0,0), one has `v(x_k)−v(x_*)=h(x_k−x_*)`. Every original ordinary step is a G-GPPA step, and all source Theorem 2 gates have just been checked. Hence source Theorem 2(a) imports physical point R-linear convergence and finite length for this same original trajectory. It does not by itself deliver the exact Q-nu factor, common supergeometric tail, two-point selection modulus, or sharp lower bound; those remain additional results.

For any original eta0<=0 and 0<|r0|<1, the ordinary normal trajectory eventually enters the chosen fixed collar. A negative normal input becomes positive after its first original step. Apply the same theorem to the remaining tail and retain the finite original prefix. This yields an eventual restriction import for the full stated convergent normal range, not a source representation of every original step from arbitrary initial input. Initial eta0>0 is not controlled by this kernel's zero second component and is outside this bridge.

<a id="br-scope"></a>
## 4. What the reverse audit changes

All three constructions preserve the original whole zero set and the original ordinary trajectories on their stated invariant basin (or after a finite prefix). They use a different complete graph. The original double-branch graph is still incapable of the corresponding source all-pairs kernel representation; C200/C204 are untouched. NFB's necessary original-graph quadratic anchor also continues to fail for these positive subgraphs because the unfavorable tangential zero anchors remain; this file does not claim same-space NFB coverage of them.

The cap construction is particularly decisive: no infinite series, unknown limit, or tail existence premise is needed. Its simple explicit ASM kernel and ordinary invariant allow the GPPA theorem to prove the exact original witness's physical convergence. Thus a manuscript should not say that cap convergence cannot be obtained from that paper under any legitimate reformulation. It may say that the original **complete two-branch relationship** cannot satisfy the theorem with a kernel preserving the ordinary trajectory, and explain why preserving complete graph structure is mathematically material.

For logarithmic and superlinear examples the tailored kernels encode ordinary tail geometry. That substantially weakens a broad claim of convergence-framework separation, while leaving quantitative mechanism/identity results to be evaluated on their own terms. The restriction must be stated as a proved basin/tail transfer, not dismissed merely because a new complete graph appears. Conversely a restriction import is not a theorem about the original full algorithm on all starts, all branches, or all tangential states.

These are explicit verified reformulations, not a classification of arbitrary lifts. Global novelty of the convergence mechanisms, exact selection moduli, or the separate structure/approximation manuscripts remains open.

## Finite corroboration

`sol61_branch_checks.py` passed on 2026-10-09. The JSON results record 24 exact cap ordinary/warped steps, 36 exact cap ASM pairs with arbitrary second residual components, eight finite all-input coverage witnesses including negative and large inputs, the exact negative-prefix identity, nine finite truncated-series C141 ASM/phi-Lipschitz pairs, a rigorous safe constant bound K_R<=11/7<2 at nu=2,gamma=1/2,R=1/4, two exact finite-series telescoping identities, and five log tail intervals with integral remainder bounds. The script checks arithmetic and examples; the full series, universal all-pairs, coverage and physical-transfer claims are proved above.
