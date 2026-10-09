# Independent NFB v1 audit — ordinary PPA, arbitrary same-space splitting, and standard lift

Date: 2026-10-09. Reviewer: independent `gpt-6.1-sol` audit requested by the parent research task. This report modifies no central claims and makes no global priority verdict.

**Verdict.** I found no fatal objection to C201, C202, or C203 in their stated scopes. The August 24 NFB paper genuinely covers nonmonotone ordinary PPA examples and physical R-linear convergence; finite length follows immediately on those covered trajectories. Conversely, the paper's assumptions force a fixed bounded quadratic zero-anchor inequality for every qualifying same-space splitting and for its standard full-graph primal-dual lift. The repository's explicit nondegenerate natural, cap, superlinear, and logarithmic relations violate that necessary inequality locally. This is a valid noncoverage result for those precise representations, not a proof of global novelty or an exclusion of arbitrary lifts.

## Evidence and independence

The primary source is Pesquet–Roldán, *Nonlinear Forward-Backward Algorithm for Solving Non-monotone+Lipschitz Inclusions with Applications to Adjoint Mismatch Problems*, [arXiv:2608.22687v1](https://arxiv.org/abs/2608.22687v1). I directly opened the official version page, which lists submission on 24 August 2026, 00:58:01 UTC, and only v1 in its history. The audited local PDF has SHA-256 `14db75596189d898d97aa9389b3e1a50bbe2ed70e207a3257d681cb4d01077b9`, matching `sources/manifest.json`. Page numbers below are printed PDF pages.

I read the source's relevant definitions and proofs in §§2–4 and the application assumptions in §5.1–5.2. I visually inspected pp.6,8,13,24,25,30 where extraction can obscure formulas or the two chi constants. I first derived the zero-anchor square completion from the source, before reading `nfb_review.md` or `independent_attack.md`; C201's claim statement was supplied and read before this derivation, so this was an independent reconstruction, not a blind discovery. I then checked those reports against the derivation.

Repository reading covered the relevant Research Goal/Definition Map/Claim Map of `README.md`, the external comparison and open-scope statements of `RESEARCH_STATE.md`, C199–C203 in `CLAIMS.md`, F51–F53 in `FAILED_ROUTES.md`, comparison README/BASELINE/COMPARISON, the NFB review and NFB portions of the independent attack, and the canonical definitions/proofs for R02, C193/SN17, C137/GC1–6, C141/SF1–5, and C10/GM26–39. C199–C200 were read to prevent transferring GPPA-specific conclusions to NFB; this report does not independently certify their GPPA proofs.

The fresh reproducible arithmetic is in `sol61_nfb_check.py` and `sol61_nfb_results.json`. Exact checks passed: all scalar source gates and 24-step identities for three scalar examples, the rotation graph equation and norm contraction, 324 source cubic identities, and 36 square-completion identities in a non-diagonal positive metric. These are arithmetic checks. The universal splitting/lift exclusions below are proved symbolically, not established by a finite grid.

## 1. The exact source hypotheses

Use `F` for the original total relation, `C` for the source forward term, and `Delta` for the source's descent constant called `lambda` in (3.8). `Delta` is not the ordinary PPA step size.

Source (2.1), p.3, means

\[
\langle x-z,Cx-Cz\rangle\ge\beta\|Cx-Cz\|_{S^{-1}}^2
\quad\text{for all }x,z\in H.
\]

The source definition (2.3), p.4, of semimonotonicity **on a set of anchors** compares every specified anchor with every graph point. It does not require all-pairs semimonotonicity of two arbitrary nonzero graph points.

Assumption 3.1, p.6, and Problem 3.5, p.8, require all of the following:

- A fixed real Hilbert space and a fixed bounded, self-adjoint, strongly monotone linear `S`; hence `S^{-1}` is bounded and its norm is equivalent to the physical norm.
- `C:H->H` globally beta-cocoercive relative to `S`, with `beta>0`.
- `(M+A)^{-1}` single-valued with full domain, and the complete graph of `A+C` sequentially weak–strong closed.
- `A` rho `S^{-1}`-comonotone at **every** `(z,-Cz)` with `z in zer(A+C)`, where `rho>-beta`.
- `tau M-S` globally zeta-Lipschitz relative to `S`, with `0<=zeta<1/2` and `tau> -zeta*rhohat/(beta+rhohat)`, `rhohat=min(rho,0)`.
- A nonempty complete zero set. Algorithm 3.7 also requires `0<theta<2`; its arbitrary initial memory is allowed by the source but must be fixed correctly to establish PPA identity.

Algorithm 3.7, p.8, (3.6a–c), is

\[
p_{n+1}=(M+A)^{-1}(Mx_n-Cx_n+u_n/\tau),\quad
u_{n+1}=(\tau M-S)p_{n+1}-(\tau M-S)x_n,
\]
\[
x_{n+1}=(1-\theta)x_n+\theta p_{n+1}.
\]

Its fixed kernel can be nonlinear. The kernel restriction is nevertheless quantitative: the triangle inequality gives

\[
(1-\zeta)\|x-y\|_S\le
\tau\|Mx-My\|_{S^{-1}}
\le(1+\zeta)\|x-y\|_S.
\]

Thus one cannot import the unrestricted/noninjective GPPA kernel interpretation into this theorem. This lower bound follows directly from Assumption 3.1(iv), whether or not one calls `M` a kernel.

Theorem 3.10, pp.12–13, adds `Delta>0` in (3.8). Its (i) conclusion is physical weak convergence; its (ii) conclusion, under an additional positive anchored term `(mu S,rho S^{-1})` for `mu>0`, is physical R-linear convergence to the unique zero. Source Proposition 3.6, p.8, (3.3)–(3.5), already proves uniqueness. A negative rho term is permitted, so (ii) is not equivalent to requiring strong monotonicity of the original operator.

## 2. Independent reconstruction of C201

Assume the complete original relation is exactly `F=A+C` and only the cocoercivity and source anchored assumptions above hold. Fix **any** zero `z` and **any** `(x,f)` in `gph F`. Put `c=Cx-Cz`. Then `f-Cx in Ax` and `-Cz in Az`, so (2.3)/3.1(iii) and (2.1) yield

\[
\langle x-z,f-c\rangle\ge\rho\|f-c\|_{S^{-1}}^2,
\qquad
\langle x-z,c\rangle\ge\beta\|c\|_{S^{-1}}^2.
\]

Add these inequalities and use the exact identity

\[
\rho\|f-c\|_{S^{-1}}^2+\beta\|c\|_{S^{-1}}^2
=\frac{\beta\rho}{\beta+\rho}\|f\|_{S^{-1}}^2
 +(\beta+\rho)\left\|c-\frac{\rho}{\beta+\rho}f\right\|_{S^{-1}}^2.
\]

Because `beta+rho>0`,

\[
\boxed{\langle x-z,f\rangle\ge q\|f\|_{S^{-1}}^2,\qquad
q=\frac{\beta\rho}{\beta+\rho}.}
\tag{SOL-N1}
\]

In particular, `V=max(0,-q) S^{-1}` is a fixed bounded positive semidefinite operator with

\[
\langle x-z,f\rangle\ge-\langle f,Vf\rangle.
\tag{SOL-N2}
\]

This is C201. It needs neither the kernel nor the warped inverse nor the step-size descent estimate. It also does **not** invoke Proposition 3.3(ii), p.7, whose premise is stronger all-pairs comonotonicity. The source Lemma 2.1, p.5, (2.4), supplies the same quadratic algebra, but the anchored specialization above is enough.

The order of quantifiers is decisive. Each prospective decomposition can choose different `beta,rho,S,M,tau,theta`. Each valid choice still produces some bounded `V`. A single original relation for which SOL-N2 fails for every bounded `V` therefore defeats every such decomposition. This excludes arbitrary legal **fixed** metrics, including non-diagonal or ill-conditioned finite-dimensional SPD matrices, and every legal fixed nonlinear kernel. It is not limited to `C=0`.

The source has no variable `S_n` or `M_n` convergence theorem. C201 is therefore properly stated as a fixed-metric/kernel result. A sequence whose every individual stage retained the same global full-graph anchor hypotheses would already fail SOL-N2 at each stage. But this says nothing about different theorems that weaken geometry to actual orbit points, use unbounded/degenerate metrics, or transform the relation. At `rho=-beta` the completion does not yield a lower bound; that boundary is explicitly outside Assumption 3.1.

## 3. The repository's failure sequences are genuine complete-graph obstructions

A convenient sufficient witness against every bounded `V` is a sequence of nonzero graph values with

\[
(x_\epsilon,f_\epsilon)\to(z,0),\qquad
\frac{\langle x_\epsilon-z,f_\epsilon\rangle}{\|f_\epsilon\|^2}\to-\infty.
\tag{SOL-N3}
\]

Indeed `|<f,Vf>|<=||V|| ||f||^2`. This proves even local failure in every graph neighborhood of `(z,0)`.

| Complete relation and canonical definition | Independently checked local witness | Necessary nondegeneracy and implication |
| --- | --- | --- |
| C191–C192, SN6/SN13; C193, SN17 | Take the canonical external load `f_D` and projection separator `e=(f_D-P_D f_D)/d_D`, tangential displacement `epsilon^delta e`, `0<delta<alpha`, normal displacement `epsilon h` for nonzero `h` in the closed convex normal set (or `epsilon` in C192), and the legitimate normal-cone value `0`. Every support-face value satisfies `<e,v-f_D><=-d_D`. Pairing is at most `-c epsilon^(alpha+delta)+O(epsilon^2)`; graph-value squared norm is `O(epsilon^(2alpha))`. Since `alpha+delta<2alpha<2`, SOL-N3 follows. | C191 requires its normal set to be different from `{0}`; C192 uses the actual nondegenerate half-line data and local boundedness of `a(t)`. Both point and graph value tend to the zero anchor. Arbitrary support faces are permitted; no illegal deletion of normal-cone values occurs. |
| C137, GC1 | At any zero anchor choose `x=(xi_bar+epsilon^delta,eta_bar,epsilon)`, `0<delta<1/2`, and positive-branch value `(-2 sqrt(epsilon),-D_epsilon(eta_bar),3epsilon)`. Pairing equals `-2 epsilon^(delta+1/2)+3epsilon^2`; squared norm is at most `8epsilon+9epsilon^2`. | The full graph contains this legitimate value. The negative branch need not enter this particular NFB witness, but must remain in the original relation and ordinary PPA fiber. |
| C141, SF1 | Put `x=(xi_bar+epsilon^delta,eta_bar,epsilon)`, `0<delta<gamma/nu`, and choose the positive branch. Pairing equals `-A epsilon^(gamma/nu+delta)+epsilon^(1+1/nu)-epsilon^2`; squared norm is `O(epsilon^(2gamma/nu))`, because the second value has modulus at most `B epsilon^(gamma/nu)`. | All stated `0<gamma<1, nu>1, A,B>0` work. The inequalities `gamma/nu+delta<2gamma/nu<1+1/nu` prove domination. Holding the second physical coordinate fixed makes its pairing contribution zero even for a positive anchor `eta_bar`. No restriction to `eta_bar<=0` is needed, although C201's narrower witness is valid. |
| C10, GM26/GM29, every `a>0` | Write `h=ell_a(4y)`, choose `x=(xi_bar+sqrt(h),y)` and positive graph value `(-h,3y)`. Pairing is `-h^(3/2)+3y^2`, squared norm is `h^2+9y^2`, and `y^2=o(h^2)`. Thus the ratio tends to `-infinity`. | The logarithmic profile tends to zero more slowly than every positive power. This works for every `a>0`, including the divergent `a<=1` branch, which is not a positive R02/C09 finite-length example. |

For the noncoverage conclusion, one failing anchor is enough. The displayed constructions in fact work at every anchor for the stated relations. Full local R02 compatibility and complete ordinary fibers are separately present in GC1–6 and SF1–5, so C137/C141 are positive ordinary-PPA instances, not only graphs with formal negative pairings. For C191, the additional SN10 compatibility condition must accompany any R02 invocation. C192's global all-selection result must not be replaced by its local unique-fiber statement.

If C191's normal set is `{0}`, its complete relation is the normal cone of the tangential plane. The ordinary resolvent is the orthogonal projection `(p,xi)->(p,0)`. Its zero-anchor pairing is nonnegative, source 3.10(i) can apply, and the algorithm has finite length after one step. The repository correctly preserves this exception. Deleting it would be a fatal overclaim.

## 4. Independent reconstruction of C203 and its exact limit

Source Notation 4.1, p.17, (4.1)–(4.2), forms the total product relation

\[
\mathcal K(x,v)=\bigl((A_0+C_0+D)x+L^*v,\ B^{-1}v-Lx\bigr)
\]

for the primal relation

\[
F(x)=(A_0+C_0+D)x+L^*BLx.
\]

Suppose this is equality of the **complete original relation**, and this product relation meets the NFB geometric assumptions. Given every `f in F(x)`, choose its realizing `v in BLx`; then `((x,v),(f,0)) in gph K`. Given every `s in zer F`, choose a realizing dual value `v_*` so that `(s,v_*) in zer K`. Applying SOL-N1 on the product gives

\[
\langle x-s,f\rangle
=\langle(x-s,v-v_*),(f,0)\rangle
\ge q\langle f,Qf\rangle,
\qquad Q=I_H^* S_{\rm prod}^{-1} I_H,
\tag{SOL-N4}
\]

where `I_H f=(f,0)`. The compression is bounded and positive definite; in fact `Q>=||S_prod||^{-1} Id`. Consequently `V_H=max(0,-q) Q` is a fixed bounded PSD quadratic anchor on the original relation. Non-diagonal product cross blocks do not change this argument.

Theorem 4.10, pp.24–25, reduces Algorithm 4.9 to 3.7 through (4.24), with forward constant `beta*kappa`, negative modulus `rho=chi_upper*rhohat`, and `zeta=tau*vartheta/kappa`. Its positivity/descent hypotheses guarantee the required strict anchor margin. Hence it cannot cover the table's original full graphs through this standard product representation. Propositions 4.12 and 4.17 inherit the same obstruction; their specializations do not create a bypass.

There is **no requirement that `v` approach `v_*`** here: the source bound is global in the product graph. A new local lift theorem would need an independent near-anchor lifting condition. Arbitrary lifts remain open: a zero-set-only reformulation, an output `(f,r)` with nonzero dual residual, nonlinear coordinates, or altered pairings can destroy the exact compression in SOL-N4. Projection of product iterates onto the same ordinary PPA orbit also needs a separate algorithm identity. C203 is correct precisely because it states those limits.

## 5. Genuine PPA overlap: all source conditions checked

### Negative identity

For the complete graph `F=-Id` on `R^n`, ordinary step `lambda_PPA=3` gives

\[
J_{3F}=-\tfrac12 Id,\qquad x_n=(-\tfrac12)^n x_0.
\]

Choose source `A=F,C=0,S=Id,M=Id/3,tau=3,theta=1,u_0=0,zeta=0,zeta_M=1/3,beta=100,rho=-11/10,mu=1/10`.

Every source gate holds: the zero set is `{0}`; `M+A=-2 Id/3` has a single-valued full-domain inverse; the graph is closed, hence weak–strong closed in finite dimension; zero `C` is beta-cocoercive; `rho>-beta`; `tau M-S=0`, so `tau_zeta=0<3`. At every graph point, the strong anchored inequality is exact:

\[
\langle x,-x\rangle=-\|x\|^2
=(\mu+\rho)\|x\|^2.
\]

The exact full source (3.8), p.8, is

\[
\Delta=1-\frac{(3-11/5)^2}{6(100-11/10)}
      +2(-11/10)\,3\,(1/3)^2
=\boxed{\frac{788}{2967}}>0.
\]

The last negative term is essential; setting `zeta=0` does not remove it. Algorithm 3.7 has `u_n=0` and `p_{n+1}=-x_n/2`; hence this is complete ordinary PPA identity for every physical initial point with the specified memory. Arbitrary initial memory is source-legal but would change the first ordinary step; C202 does not claim that broader identity.

R02 simultaneously applies with `gamma=1,L=2,psi(s)=s`, full coverage/zero anchors, and compatibility `(t+2t)/(2*3)=t/2`. Thus the nonmonotone overlap with strict C02-v2 is genuine. Actual rate and length are

\[
\|x_n\|=2^{-n}\|x_0\|,\qquad
\sum_{n\ge k}\|x_{n+1}-x_n\|=3\,2^{-k}\|x_0\|.
\]

For this scalar relation, the exact ordinary contraction boundary is `lambda_PPA>2`; step `1` is noninvertible and step `2` oscillates without convergence. Source Corollary 3.12(ii), pp.15–16, for `C=0,zeta=0,theta=1`, has `tau>-2*rho`. Requiring `mu>0` for this graph permits `rho=-(1+mu)`, giving `tau>2(1+mu)`. Letting `mu` be small positive and taking a sufficiently large finite beta in 3.10(ii) can reach any strict `tau>2`. There is therefore no hidden boundary counterexample to this overlap.

### Rotation

Let `K(x_1,x_2)=(-x_2,x_1)` and `F=K`, ordinary step `1`. Source `A=K,C=0,S=M=Id,tau=theta=1,u_0=0,zeta=0,zeta_M=1,beta=1,mu=1/4,rho=-1/4` meets the same full-domain/closed-graph/positive-margin gates. The strong anchored inequality is again exact since `<x,Kx>=0` and `||Kx||=||x||`. Formula (3.8) gives

\[
\Delta=1-\frac{(1-1/2)^2}{2(1-1/4)}-\frac12
=\boxed{\frac13}>0.
\]

Algorithm 3.7 equals `(Id+K)^{-1}=(Id-K)/2`; its physical norm factor is `1/sqrt(2)`. The exact trajectory length from index `k` is

\[
\sum_{n\ge k}\|x_{n+1}-x_n\|
=(1+\sqrt2)\,2^{-k/2}\|x_0\|.
\]

This is genuine source 3.10(ii) coverage even though `K` is not strongly monotone. `K` is monotone in the usual sense (zero pairing), so this example should not be labelled an additional strictly nonmonotone relation. C202 correctly assigns the nonmonotone label to `-Id` and distinguishes rotation. With this repository's `gamma=1,L=1,psi(s)=s` parameters the R02 direct compatibility equals `1`, so it is C24 convergence overlap, not strict C02-v2 certificate overlap.

The two ancillary examples in `nfb_review.md` also pass the independent exact checks: `F=2 Id,C=Id/2,A=M=S=3 Id/2,tau=theta=1` gives `Delta=5/6` and the PPA factor `1/3`; `F=Id,C=Id/10,A=M=9 Id/10,S=Id,tau=theta=1,u_0=x_0/10` gives `Delta=3/4` and the invariant `u_n=x_n/10`, so the physical factor is `1/2`. Consequently `C=0`, zero memory, identity metric, or `tau M=S` are useful sufficient PPA-reduction choices, not universal necessary choices.

## 6. Theorem-by-theorem coverage and omission audit

Here “omission” means a condition or distinction a coverage/novelty summary must not omit, not a gap in the source's theorem.

| Source result; exact source location | Valid role and conditions that must stay | Consequence for repository claims |
| --- | --- | --- |
| Lemmas 2.1–2.2, p.5, (2.4) | Positive sum of the two residual-square coefficients is indispensable; the square identity tolerates a negative rho. The printed all-pairs sum result has an anchored specialization proved in §2 above. | C201 is sound without falsely strengthening Assumption 3.1 to full all-pairs semimonotonicity. |
| Lemma 2.3, pp.5–6, (2.5)–(2.6) | Positive sum, cocoercive first term, and weak continuity of the second give sequential weak–strong closure. | Source §5 linear mismatch examples have an actual closure route; “nonmonotone graphs lack closure” is not a difference. |
| Proposition 3.3, p.7, (3.1) | Global rho-comonotonicity is stronger than the standing anchored premise; (i)/(iii) also need the indicated range to be weakly sequentially closed and strict parameter bounds. | It is a sufficient closure tool, not a converse classification of every standing-assumption graph; C201 must not rely on its stronger premise. |
| Proposition 3.6, p.8, (3.3)–(3.5) | `mu>0`, all solution anchors, and `beta+rho>0` force a singleton solution set. | 3.10(ii) does not apply unchanged to entire nonisolated zero planes. But this alone does not exclude 3.10(i), which allows nonisolated zero sets. |
| Proposition 3.8, pp.8–12, (3.8)–(3.12) | All standing assumptions, the complete warped update, memory control, and positive denominator produce a nonnegative energy and a descent coefficient. Descent coefficient need not be positive in this proposition itself. | Keep the final `2 rhohat tau zeta_M^2` contribution even at `zeta=0`. Positivity is an extra convergence gate. |
| Theorem 3.10(i), pp.12–13, (3.33)–(3.36) | `Delta>0` gives square summability of actual steps, residual identification, and weak point convergence through complete-graph closure and Opial. | In finite dimension weak equals norm convergence. Square summability or norm convergence alone does not imply finite length. |
| Theorem 3.10(ii), pp.12–13, (3.37)–(3.40) | Positive anchored `mu` gives a Q-linear energy and physical R-linear point convergence to the unique zero via (3.12) and equivalent norms. | Real overlap with C202; physical finite length follows. The source conclusion is not merely residual or set-distance convergence. |
| Proposition 3.11, pp.14–15, (3.41)–(3.50) | Rewrites the same `Delta>0` as a cubic for fixed `zeta,xi,eta`; small-zeta feasible intervals are existence statements with all source assumptions retained. | No new operator class lacking the quadratic anchor appears. Exact cubic algebra matched in 324 rational samples. |
| Corollary 3.12, pp.15–16, (3.51)–(3.55) | FB, `C=0` comonotone, and monotone+cocoercive specializations retain Problem 3.5 and strict intervals. `C=0` allows beta to grow arbitrarily, not removal of anchor geometry. | Explicit ordinary PPA cases belong here; `C=0` is not the only possible identity mechanism. |
| Assumption 4.2 / Notation 4.1, p.17, (4.1)–(4.2) | Component semimonotonicity at all induced solution anchors; nonnegative sums with zero-sum restrictions; `nu_A,nu_B>=0`; full-domain single-valued component resolvents in nonempty step sets; complete product closure. | Merely sharing a primal zero set or a normal cone is insufficient; exact total-graph equality is the premise for C203. |
| Proposition 4.3, p.19, (4.3)–(4.4) | Gives component certificates for specific mismatched cocoercive maps or bounded linear `D`, with positive coefficient-sum/matrix monotonicity gates. The resulting `nu_A` still needs to be nonnegative to invoke 4.2. | Does not automatically include arbitrary cusp interactions or all native engineering models. |
| Proposition 4.5, pp.20–21, (4.5)–(4.9) | Stated signs give single-valuedness on range; full domain needs explicit range conditions or the specified maximal special cases. | “Maximally semimonotone” without the stated sign/range alternatives is not a free coverage certificate. |
| Propositions 4.6–4.7, pp.21–24, (4.10)–(4.18) | Global product anchors are derived by completion and block metric comparison; `sigma*tau*||L||^2<1`; the positive modulus uses lower chi and the negative one upper chi. | This is precisely the NFB product geometry compressed by C203. Extraction of both chi symbols as one value would be wrong. |
| Proposition 4.8 / Algorithm 4.9, p.24, (4.19)–(4.21) | Specific kernel yields triangular full inverse; algorithm retains reflected `D` terms, dual update, and relaxation. | Full original graph satisfaction and projected ordinary-PPA identity are distinct questions. |
| Theorem 4.10, pp.24–25, (4.22)–(4.25) | All 4.2, `kappa>0`, positive modified beta/rho margin, and (4.23). Its proof sets `u_0=(-tau Dp_0+tau Dz_{-1},0)` and reduces to 3.7. R-linear branch requires both `nu_A,nu_B>0`. | Already gives product physical R-linear point convergence and therefore finite length; standard complete-graph lift excluded by C203 for the failure table. |
| Proposition 4.12 / Corollary 4.14, pp.26–27, (4.28)–(4.33) | `D=0` CV/CP specialization retains product closure, component sign/maximality/resolvent gates and specified step intervals. 4.14 states weak convergence, not a new general R-linear statement. | These are included in the same standard product anchor obstruction; no theorem was omitted that removes it. |
| Assumption 4.16 / Proposition 4.17, pp.27–29, (4.34)–(4.38) | `B=L=0`, complete `A_0+D` anchored geometry, component resolvent coverage, total closure, (4.35) positive margin and (4.36) quadratic. `nu_A>0` for R-linear. | Replace the source `A` by `A_0+D` in SOL-N1; the same-space obstruction remains despite a reflected update. |
| §5.1–5.2, pp.29–30, (5.1)–(5.5) | Concrete `G+KT` with positive combined cocoercivity margin, linear mismatch matrix condition, and the specialized steps; two different splits are genuinely available. Huber scaling is `delta/lambda_H`, visually verified at p.30. | Source offers concrete nonmonotone applications; names like “inverse problem” or “normal cone” neither establish nor disprove identity with the repository's native models. Numerical PSNR is not a theorem assumption certificate. |

I found no omitted relevant theorem in this fixed source that bypasses SOL-N1 or SOL-N4 while preserving the same full relation under the source's own framework. References to earlier warped-resolvent, Spingarn, weak-Minty, or splitting work in the introduction are leads for separate priority work, not results proved in this paper. I did not independently re-prove all imported source references, especially the metric estimates cited from [48]. The exclusion argument itself needs no such import.

## 7. Implications for novelty language and remaining scope

A physical point estimate `||x_n-x_*||<=M r^n`, `0<r<1`, implies

\[
\sum_{j\ge n}\|x_{j+1}-x_j\|
\le\frac{M(1+r)}{1-r}r^n.
\]

Thus finite length is already a direct corollary of NFB 3.10(ii), 4.10(ii), and 4.17(ii), wherever those theorems cover the same physical trajectory. There is no novelty distinction based only on the authors not printing the phrase “finite length.” The source's weak branch gives less, even in finite dimension.

The repository's safe distinctions are the exact all-pairs RL plus complete true-residual EB and compatibility mechanism, its explicitly NFB-ineligible complete graphs, nonisolated solution-selection outputs, or the nongeometric Dini/logarithmic behavior. The positive C10 example is `a>1`; `a<=1` demonstrates the failure boundary rather than finite-length novelty. The source does not establish the same modulus–Dini chain, complete cap/superlinear fibers, or two-point selection modulus merely by proving convergence for another class.

C199's GPPA overlap and C200's ASM-kernel trajectory obstruction remain distinct from the NFB quadratic-anchor argument. In particular, C193's failed fixed quadratic anchor is not a GPPA-kernel exclusion: C199 expressly supplies a counterexample to that inference. NFB noncoverage does not establish absence of coverage by every earlier algorithm.

C03/C04/C18 and the finite-data structural results require a separate prior-art comparison. A nonmonotone PPA convergence overlap does not duplicate simultaneous shadows, complete-fiber classification, or sharp range/finite-data conclusions. Conversely, this audit does not certify those structural results' worldwide priority.

**Recommended editorial disposition:** retain the current limited verdict and C201–C203 scopes. No central mathematical correction is required by this NFB audit. Keep the words “fixed,” “complete original graph,” and “standard full-graph primal-dual lift” in any condensed exclusion statement; retain real `-Id` overlap and the natural-class degenerate projection exception. Do not convert this result into “all lifts impossible,” “no previous nonmonotone PPA convergence,” or “finite length is new.” Global novelty, arbitrary other faithful lifts, original-model certification, and imported-reference priority remain unresolved.
