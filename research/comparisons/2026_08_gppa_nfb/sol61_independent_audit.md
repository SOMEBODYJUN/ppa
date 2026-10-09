# Independent hostile audit: August GPPA/NFB versus PPA

Audit author: independent reviewer in the sol61 review round, 2026-10-09. This file is a scoped audit, not an external-priority certificate. Archived PDFs are the fixed source versions. Existing comparison proofs were not read before the independent derivations below (the comparison README and repository navigation necessarily exposed their claimed conclusions).

## Blind derivations recorded before reading comparison proofs

For an ordinary step `p -> u`, `p-u=lambda*f` with `f in F(u)`, using the *same selected graph value* in GPPA gives `v(p)-v(u)=gamma*f`. Thus `h=v-(gamma/lambda)Id` is invariant along the prescribed ordinary trajectory. This is a restriction on a kernel for a fixed relationship, not an exclusion of changing the relationship, restricting its graph, or lifting the problem.

If `(F,v)` is ASM with constant epsilon, a graph value shared at two output points forces equality of the two kernel values. In particular the complete cap graph is independent of its first tangential coordinate, so any ASM kernel is independent of that coordinate. The two normal branches differ at each positive normal height; comparing the branches at neighboring heights in both orders should force the kernel's normal derivative to vanish. ASM also gives `||v(u)-v(w)|| <= ||f(u)-f(w)||/epsilon` along each locally smooth selected branch, so local absolute continuity is available without assuming kernel continuity. Ordinary positive-normal cap transitions require a nonzero normal kernel increment. This is the expected same-F obstruction and must be checked against the existing proof. It does not prohibit another relationship with the same single orbit.

For NFB write the complete original graph as `F=A+C`. For `s in zer F`, `f in F(u)`, put `h=u-s`, `d=C(u)-C(s)`. The anchored comonotonicity and cocoercivity inequalities imply

`<h,f> >= beta ||d||^2_{S^-1} + rho ||f-d||^2_{S^-1}`.

When `rho<0` and `beta+rho>0`, completing the square gives the necessary fixed quadratic original-graph anchor with coefficient `beta*rho/(beta+rho)`. When `rho>=0`, the coefficient zero is safe. The statement covers arbitrary same-space decompositions satisfying those assumptions, not merely `A=F,C=0`; the metric must be one fixed bounded coercive operator.

For the natural support/normal graph, any nonzero tangential graph value of size `y^alpha`, paired with a zero point displaced by a fixed small amount in the unfavorable tangential direction, yields `<u-s,f>/||f||^2 -> -infinity` as `y -> 0`. This defeats every fixed quadratic anchor. It remains a local obstruction if the fixed displacement and all shrinking graph points lie in the same open neighborhood. The complete zero sheet and the complete graph, rather than only an individual orbit and its limit, matter.

A potential loophole must remain visible: restricting the original graph to a prescribed orbit plus its limit, or changing the relationship by monotone extension, can preserve that orbit while removing the adverse zero anchors and branches. A full-graph theorem exclusion alone therefore does not establish that the convergence behavior, viewed without the original problem identity, cannot be imported from an older framework. Arbitrary lifts require a separate fidelity definition and theorem.

## Audit verdict and actual reading scope

No fatal objection was found to the *scoped* statements of C199-v1–C203-v1. They establish genuine intersection and genuine failure of inclusion for the fixed original relationships and the explicitly specified fidelity contracts. They do not establish global novelty, failure of every possible reformulation, or novelty of the attached structure manuscripts. One previously open comparison gap can be closed: the cap trajectory is excluded even by merely pair-monotone GPPA, without regularity of the kernel. The new result should receive its own identity rather than silently changing C200-v1. **A decisive reverse audit also succeeded:** deleting the inactive negative cap branch preserves the complete original zero sheet and the ordinary algorithm on positive inputs, and an explicit ASM kernel imports GPPA Theorem 2 for the same original cap trajectory. Similar zero-set-preserving restrictions import GPPA for the positive C141 and Dini-log basins with precisely stated tail bridges. Thus complete-graph noninclusion must not be described as convergence nonderivability. Full proofs are in [sol61_branch_restriction.md](sol61_branch_restriction.md).

This audit inspected the canonical R01/R02 proof and the complete C137 object/coverage/RL/residual calculation; the relevant natural-class definitions and C193 near-zero argument; the C199–C203 Claim register; comparison README, BASELINE, COMPARISON, and the relevant sections of all three existing reports. Primary-source inspection was concentrated on GPPA Definitions 1–6 and Theorems 1/2/4, including their printed proofs, and NFB (2.1)/(2.3), Assumption 3.1, Algorithm 3.7, Proposition 3.8 and Theorem 3.10, plus Notation 4.1, Assumption 4.2, Algorithm 4.9 and Theorem 4.10's reduction. The attached manuscript introductions, theorem statements, hypothesis contracts, local solvability section, and discussion were inspected. This is not a reproof of every structure theorem, every external cited lemma, or every numerical application in either archived paper.

Exact archived source files:

- `sources/gppa_2608.01584v1.pdf`: pair definitions pp.4–5, warped/inverse-continuity definitions pp.5–6, Theorem 1 p.6, Theorem 2 pp.7–8, regularization and Theorem 4 pp.8–11.
- `sources/nfb_2608.22687v1.pdf`: (2.1) p.3 and (2.3) p.4, Assumption 3.1 p.6, Algorithm 3.7 p.8, estimate/proof pp.8–12, Theorem 3.10 pp.12–13, product definitions/assumptions p.17, product algorithm/reduction pp.24–25.
- `/workspace/scratch/428311e7cc3f/project_sources/02-2026_09_25_siopt_combined_candidate.pdf`: introduction pp.2–4; structural Theorems 3.3/3.5/3.6 pp.6–8, 4.1/4.4/4.5 pp.9–12, 5.2/5.3 pp.13–14, 6.1/6.2 pp.15–17; separate Theorem 8.1 pp.20–21; discussion p.22.
- `/workspace/scratch/428311e7cc3f/project_sources/04-Holder_RL_Formal_Manuscript.tex`: assumptions/introduction lines 49–202, main shadow theorem 375–472, sharpness 506–552, anchored shadow 561–617, geometry 624–686, fixed-set realization 738–836, fiber classification 840–873, coverage 1000–1063, QP 1134–1213, covered estimates 1227–1293, information boundary 1394–1437, discussion 1573–1613. Line locations refer to the supplied file, not a reconstructed draft.

## Claim-by-claim hostile review

| Claim | Independent result | Quantifiers that must remain visible |
| --- | --- | --- |
| C199 | Pass. The complete original nonmonotone graph, including every boundary normal value, admits the explicit nonlinear noninjective ASM kernel. Every ordinary trajectory is an admissible warped selection. The invariant gives a noncircular physical point-rate bridge. | This is one explicit kernel, not every kernel. Ordinary outputs are contained in warped outputs; the two complete algorithms differ. The physical bridge belongs to the ordinary selection and does not control arbitrary warped tangential choices. |
| C200-v1 | Pass as written. The ASM estimate derives local Lipschitz regularity, and both complete branches force the normal kernel to be constant on the positive-height interval. No initial continuity hypothesis is smuggled in. | Fixed original complete graph and physical sequence, arbitrary positive GPPA step, arbitrary single-valued kernel, and permission to reselect either original branch at each step. Local versions need complete two-branch product neighborhoods, not just a sequence of graph points. |
| C201 | Pass. The fixed original-graph quadratic anchor follows from arbitrary qualifying same-space decompositions by completing a square. The original-graph local sequences contradict every fixed bounded quadratic form. | Equality of the original full graph with A+C; all solution anchors and all original graph values; beta>0 and rho>−beta; one bounded coercive metric. Degenerate natural C={0} is excluded from the failure witness. |
| C202 | Pass. The negative identity example is genuinely nonmonotone, satisfies the source's strong *anchored semimonotonicity* with negative rho, and has the same complete PPA step under the stated memory initialization. | u0=0 for the negative identity reduction; full inverse and closed graph; the last negative-rho term in source (3.8) must be retained. Rotation is a C24 overlap, not a strict C02 direct-compatibility overlap at the parameters shown. |
| C203 | Pass. The complete standard product lift maps each original graph output to (f,0), and every original zero to a product zero. The product necessary anchor compresses to the original graph. | One and the same full product relationship must satisfy source Assumption 3.1. Full graph-value fidelity, zero lifting, and fixed bounded coercive product metric are essential. Equality of zero sets alone or a nonzero auxiliary output does not suffice. |

C199's inverse-continuity assertion has a particularly simple complete-fiber proof: for y>0 every normal graph value is ay, hence distance to the zero sheet is at most ||f||/a; at y=0 distance is zero despite the entire negative normal half-line. Thus it is not relying on a selected residual. The kernel is deliberately non-Lipschitz at zero; Theorem 2 does not forbid that, while Theorem 4 has a different Lipschitz hypothesis and changes the graph to F+epsilon v.

C201 does not assume full pairwise comonotonicity of A. Source (2.3) explicitly quantifies every graph point against every member of its anchor set; Assumption 3.1(iii) chooses all solution anchors. That exact source quantifier is already sufficient. The square identity holds also for rho>=0; replacing the resulting positive bound by a nonnegative or PSD lower-bound formulation only weakens it. Each candidate splitting may choose different constants and metric: each still yields *some fixed bounded quadratic form*, and the near-zero witness defeats all such forms.

The local failure witness is stronger than using a distant zero: C137 admits u_epsilon=(bar_xi+epsilon^eta,bar_eta,epsilon), 0<eta<1/2, with its actual positive-branch f_epsilon. Its graph point and graph value both tend to (s,0), but pairing/residual-square tends to minus infinity. C193 uses 0<eta<alpha and a normal ray in the nontrivial closed convex C; 0 is an allowed normal value at every point of C. Consequently shrinking an open graph neighborhood cannot restore the NFB anchor. A sparse orbit-only subgraph is a different object.

For C203, large auxiliary *base* displacement is harmless because the auxiliary component of the output is exactly zero. If I_H f=(f,0), then Q=I_H^* S_prod^{-1} I_H is bounded and coercive: Q>=||S_prod||^{-1} Id. The conclusion does not depend on finite auxiliary dimension. Infinite-dimensional auxiliaries alone cannot bypass this argument. An arbitrary lift might instead change the output embedding or pairing, or carry nonzero auxiliary residual; that is precisely where the current proof stops.

## Strengthening independently checked: pair-monotone cap obstruction

The following proof does not use ASM, kernel continuity, measurability, or a preexisting bounded-variation assumption.

On the complete cap region eta<=0 and y>0, write f_+(y)=(-2sqrt(y),0,3y) and f_-(y)=(-2sqrt(y),0,−5y). Assume only

`<f−g,v(x)−v(z)> >= 0` for every two complete original graph points.

At one fixed height y, opposite branch values differ by 8y e3. Comparing arbitrary tangential base points with the branches in both orders forces equality of their third kernel components. Thus v3(xi,eta,y)=q3(y), although v1 and v2 need not be independent of tangent.

Fix any tangential base c with eta<0 and define q1(y)=v1(c,y). For y,z>0 put Delta r=sqrt(y)−sqrt(z), Delta y=y−z and Delta qi=qi(y)−qi(z). The two same-branch inequalities are

`−2 Delta r Delta q1 + 3 Delta y Delta q3 >= 0`,

`−2 Delta r Delta q1 − 5 Delta y Delta q3 >= 0`.

Five times the first plus three times the second gives `Delta r Delta q1 <= 0`. Since sqrt is strictly increasing, q1 is decreasing. It is finite-valued on [a,b], so its total variation is exactly q1(a)−q1(b), a finite number. This is a conclusion, not an extra regularity assumption.

The cross-branch inequalities give, on any 0<a<=y,z<=b,

`|Delta q3| <= 2 |Delta r| |Delta q1| / (8a)`

`<= |y−z| |Delta q1| / (8a sqrt(a))`.

Partition [a,b] with mesh d. By the triangle inequality and telescoping monotonicity,

`|q3(b)−q3(a)| <= d [q1(a)−q1(b)] / (8a sqrt(a))`.

Letting d tend to zero proves q3 constant. Applying the argument to any interval between two positive heights proves constancy on the whole positive axis. The actual ordinary cap trajectory varies tangentially, but the same-height opposite-branch comparison already makes its third kernel component q3(y). Each GPPA update would therefore require

`0 in h {3y_{k+1},−5y_{k+1}}`,

which is impossible for h>0 and y_{k+1}>0. Range coverage is unnecessary for the contradiction. Source Theorem 1's merely pair-monotone hypothesis cannot represent this same-F trajectory, even without kernel regularity.

An open local version holds on a tangential product patch and a connected positive-height interval containing adjacent tail points, with both complete branches present. A neighborhood of the limiting cap zero contains such a tail patch. A discrete orbit subgraph lacks these comparisons.

The scalar-profile extension in `pair_monotone_barrier.md#pm-profile` was independently checked after the cap argument. It avoids any monotonicity assumption on the normal branches. For common tangential value −c phi(y), put A=a_+(y)−a_−(z)>0, B=a_+(z)−a_−(y)>0, and P=c Delta phi Delta q1. The two cross inequalities are A d>=P and −B d>=P. Multiplying by B and A and adding gives 0>=(A+B)P, so q1 is nonincreasing whenever phi is strictly increasing. Continuity and opposite signs of the normal branches give a positive lower bound for A,B on every compact interval. Local Lipschitz regularity of phi then gives the same mesh-times-total-variation estimate. Thus the lemma also excludes the specified C141 trajectory for 0<y<1, without any derivative-sign gate on y^(1/nu)−y. Canonical GM26–27 gives the log profile a strictly positive derivative and a positive-slope tangent continuation; it is strictly increasing and locally Lipschitz on the full positive axis. The same lemma excludes the specified C10 trajectory for every a>0. This remains a scalar common-tangent lemma; it is not permissible simply to delete epsilon from C200's general vector-H ASM lemma.

## Concrete changed-graph counter-representation

The chosen cap trajectory is not intrinsically beyond classical PPA. Put

`I=xi0+2sqrt(y0)`, `x_*=(I,−1,0)`,

and define the affine strongly monotone relationship

`G(xi,eta,y)=(xi−I,eta+1,3y)`.

Its complete resolvent at step 1 is

`J_G(xi,eta,y)=((xi+I)/2,(eta−1)/2,y/4)`.

On the cap orbit eta=−1, y_k=4^(−k)y0, the algebraic invariant is xi_k−I=−2sqrt(y_k). Substitution shows J_G x_k equals the next cap point exactly. G is globally strongly monotone with modulus 1 and globally Lipschitz with constant 3; its unique zero is the cap orbit's limit. Therefore that identical physical sequence is an ordinary, ASM-GPPA sequence for G. It also lies in an ordinary NFB reduction: A=G,C=0,S=M=Id,tau=theta=1,u0=0,zeta=rho=0,mu=1,beta=1 yields source descent coefficient 1/2>0.

This is a fatal counterexample to an *unqualified* claim that this physical trajectory cannot be represented by GPPA or NFB under any relationship. It is not a counterexample to C200/C201/C203, which preserve the original full F. The invariant determines I from the initial point before convergence is invoked, so the counter-representation is not circular. Different initial tangential families would generally need different I and hence a different G; it does not reproduce the full cap algorithm on an open domain. It changes the original zero sheet and all other fibers.

Restricting or extending an orbit graph can likewise import older theorems for an individual sequence. To count that as an algorithmic coverage result for the original problem one must establish the declared fidelity contract, uniformity over starts/choices, and a usable transformation, including what original data it needs. The present noninclusion results intentionally do not classify such reformulations.

## Manuscript-level comparison: actual attachments versus project convergence line

The filenames are potentially misleading. The combined candidate is **not** a combined C02 convergence paper. Its title and principal claims are *Sharp Simultaneous Shadows and Fiber Realization for Hölder–RL Relations*. Sections 1–7 concern structure and approximation; its addition is a separate original local *solvability/range* theorem in Section 8, not a PPA trajectory convergence theorem. The formal TeX ends with the structure/approximation discussion and contains no corresponding Section 8 local solvability theorem.

| Manuscript result | Actual mathematical identity | What the August comparison establishes |
| --- | --- | --- |
| 02/04 shadow theorem | Full graph/all-scale sublinear Hölder–RL; one common strongly monotone bi-Lipschitz map controls every nonempty forward and inverse fiber at the same original base; universal sharp factor 1/sqrt(2). | The compared GPPA/NFB convergence theorems do not establish this paired structural conclusion. C199–C204 neither prove its novelty nor show it is redundant. |
| 02/04 realization/classification | Finite-dimensional fixed-parameter graph maximality; exact complete fibers are all nonempty compact sets within the diameter threshold; optimal Hölder modulus in the construction. | Different output from convergence to a zero. NFB's unique-solution rate branch cannot supply arbitrary compact zero fibers; its weak branch cannot be dismissed merely because its rate branch is unique. No complete structural priority search was done here. |
| 02/04 sharp coverage | Full-fiber range localization, including relatively maximal fixed windows, with an exact scalar threshold. | Neither a warped coverage assumption nor an external algorithm's existence proves these original-fiber localization estimates. Coverage is an assumption in GPPA, not the same quantitative conclusion. |
| 02/04 finite QP | One coherent invertible proxy, sample cross inequalities, parameter-space coverage, and numerical evaluation terms. | This is not a newly discovered generic extension algorithm: the manuscripts themselves identify constructive Kirszbraun antecedents. The paired RL specialization and sharp constants need a separate antecedent comparison. |
| 02 Section 8 only | Actual proximal subrelation T, selected-step inequalities on the complete input window, usc/compact rational-acyclic values, certified shell margin, cohomology surjectivity, nonzero Euler/Lefschetz certificate; original value ball and state-dependent forcing. | GPPA/NFB trajectory convergence does not assert this range theorem. Its topology and complete-window premises are independent of the global structure hypothesis and of finite observations. It is not a C02 convergence conclusion. |
| Project C02/C09 | Ordinary local graph-block PPA, true infimal residual EB, same-window compatibility/coverage, stay-in-domain budget; geometric or Dini physical tails. | C199/C202 are real covered subclasses; C200/C201/C203/C204 are real fixed-original-graph noninclusion witnesses. This is the direct subject of the August comparison. |

There is an elementary input-class mismatch, not just a difference in output. For the attachments' full-graph, all-scale condition with 0<gamma<1, comparing two zero graph points gives `||s−s'|| <= L||s−s'||^gamma`; thus every complete zero fiber has diameter at most R=L^(1/(1−gamma)). In contrast C199, C137, C141, C191 and C192 have an unbounded zero sheet. They cannot satisfy the attachments' global sublinear condition with a fixed finite L. Their bounded-input-scale RL certificates are different hypotheses. The nonmonotone negative-identity overlap uses gamma=1 and is likewise outside the formal manuscript's sublinear class. Consequently the convergence witnesses do not test the principal attached structure theorem on its own hypothesis class.

The formal manuscript explicitly says at lines 200–202 that it does not infer convergence for the original relationship from a shadow and a residual error bound. The combined candidate says the same on p.4, and separates its Section 8 hypotheses. It would therefore be incorrect to reject either manuscript as a duplicate solely because an August paper proves some nonmonotone convergence results. It would be equally incorrect to award either manuscript novelty solely because cap trajectories violate August hypotheses.

The Section 8 printed bound deserves precise terminology. Equation (8.2) assumes `d(y,S)<=c||p−y||^q` for every permitted y in T(p). This is a uniform *selected-step/output* bound. A complete infimal-residual bound `d(y,S)<=kappa r_F(y)^q` would imply it, but the selected bound does not imply the complete true EB. Theorem 8.1 only needs what (8.2) prints, so this distinction is not a fatal proof objection. It prevents silently identifying the added local theorem with C02's complete true-residual hypothesis. Finite observations do not establish the inequalities everywhere on A or the topology/regularity of T; the printed theorem acknowledges those independent gates.

## Novelty audit: what survives and what is not certified

The defensible comparison claim is about different sufficient conditions for the *same ordinary algorithm on the same complete original relationship*, together with quantitative physical tails, completeness of graph fibers, and the specific complete examples. On covered subclasses, existing physical R-linear point estimates automatically imply finite length by a geometric series; the fact that an external paper did not give that consequence its own heading is not novelty. A kernel-coordinate rate alone has no such implication without a physical bridge, but C199 supplies an explicit bridge and must be acknowledged.

A complete-graph obstruction is mathematically useful and stronger than failure of one proposed kernel or the C=0 splitting. It is still not a priority theorem. It excludes the named source theorem on the named fidelity contract; it does not show that its conclusion has no earlier proof, that another selected relation cannot import it, or that an entire natural operator class is new. The affine counter-representation above is a concrete reason that the fidelity contract must be present in the same sentence as the exclusion.

The structure manuscripts already disclaim novelty of Kirszbraun/Hölder extension, generic Lipschitz approximation, and generic finite extension algorithms. Their remaining candidate contributions are the paired same-original-base estimate and optimal factor, anchored optimum, exact complete-fiber realization with least modulus, and their quantitative original-fiber consequences. Those claims need direct comparison to the relevant approximation/extension/fixed-set literature. The combined PDF p.3 says Levy–Rice and Ajiev do not supply the paired sharp conclusion. This audit did not retrieve and theorem-by-theorem verify those works or the Ciosmak 2024/2026 references; the August comparison cannot substantiate that negative antecedent assertion. The primary-paper references that support the construction are not thereby exhausted as novelty threats.

No assurance is justified about arbitrary graph-preserving nonlinear lifts, transformed residuals, alternate metrics outside the source class, all possible local subrelations, all earlier Dini/selection results, or global structural priority. A general lift exclusion would need an explicitly frozen fidelity contract and a new invariant/necessary condition covering it. A global novelty statement would need broader primary-source literature review, not more finite experiments on these witnesses.

## Independent finite checks and proof boundary

`sol61_independent_checks.py` uses only the Python standard library and passed on 2026-10-09. `sol61_independent_results.json` records 12 exact ordinary/warped C199 steps and the invariant physical bridge, the exact NFB negative-identity descent coefficient 788/2967, 16 exact cap/changed-affine-graph steps, a legal near-zero cap anchor sequence, and a non-diagonal product compression example with arbitrarily large auxiliary base displacement.

These checks are arithmetic corroboration. They do not prove any arbitrary-kernel, arbitrary-splitting, infinite-interval, complete-source-priority, or arbitrary-lift assertion. The universal pair-monotone exclusion is the partition/BV proof; the universal same-space NFB exclusion is the source anchored square identity plus the analytic near-zero asymptotics. Parent integration owns any changes to central Claims, navigation, graphs, or publication; this audit did not edit them or commit/push.

## Reverse audit integration: stronger import than a changed affine graph

The [branch restriction audit](sol61_branch_restriction.md) is an essential part of this verdict. Its cap restriction deletes only the negative normal value, keeps S=R²×{0}, and agrees with the original complete ordinary resolvent on every positive normal input. Kernel v=(-2sqrt(y_+),0,y_+) is globally 1-ASM on that restricted complete graph, has global warped coverage, and the complete inverse is R-Lipschitz with constant 1/3. For eta0<=0 it has an exact original physical bridge; negative normal initial data use one original step and the positive tail. This imports source Theorem 2 point convergence and finite length for the very trajectory used as the complete-graph exclusion witness. It is therefore a fatal objection to broad claims that the external framework cannot prove that original trajectory converges through any valid reduction. It does not contradict the correctly scoped C200/C204 full-original-graph kernel exclusion.

C141 admits an analogous source Theorem 2 import after a finite prefix, by retaining its positive branch on a sufficiently small fixed output collar and using a clipped tail-series kernel. The source result supplies physical R-linear convergence and finite length; exact superlinear factors and selection regularity need the original additional analysis. For log a>1, the positive branch and a Dini-tail kernel satisfy source Theorem 1. Inverse R-continuity plus the tail bridge gives physical point convergence, while finite length uses the extra telescoping tail identity. The series is unavailable for a<=1. These different theorem/hypothesis identities warrant separate Claim registrations (planned C205 cap, C206 superlinear, C207 log). The proofs close their explicit coverage/inverse/physical gates; they do not classify arbitrary kernels, restrictions or lifts.

`sol61_branch_checks.py` passed and wrote `sol61_branch_results.json`. Its finite arithmetic corroboration does not prove the infinite-series or universal assertions. Those are carried by the independently reconstructed proofs in the linked report.
