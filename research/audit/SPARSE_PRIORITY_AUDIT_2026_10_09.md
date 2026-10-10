# Sparse norm-difference structure: bounded priority audit

Initial audit: 2026-10-09; renewed primary-source check: 2026-10-10.
Object audited: C224–C228 in
[`automatic_regularity.md`](../topics/sparse_recovery/automatic_regularity.md)
and [`sharp_instance_dynamics.md`](../topics/sparse_recovery/sharp_instance_dynamics.md).
The initial C224–C226 reading used revision `8ff3ae1`; the renewed priority-only
check started from revision `b051868`.

## Verdict and scope

**The sharp active-Hessian threshold is a candidate contribution, not a certified first theorem.** The priority gate remains open because the complete bodies of Wang–Zhang (2017) and Huo–Chen–Ge–Ng (2023) have not been obtained. Zhao–He–Huang–Huang (2018) is an additional relevant unread-body lead. The renewed check adds a complete 2026 fractional-regularization theorem comparison and closes two title-based false leads; it does not relabel the missing papers as fully read. Failed retrieval and unproductive keyword searches provide no evidence that a theorem is absent.

Two broader novelty claims should be withdrawn now. The norm-difference model family predates this project. Support-column independence at all local minima was explicitly proved for the least-squares `l1-l2` model in 2015, without a RIP condition. Moreover, the present proof extends that support conclusion to all finite `p>1`; it has no sharp `3/2` boundary. Strict complementarity follows here for all `1<p<2`. Only **automatic positive definiteness of the active Hessian** has the demonstrated sharp `3/2` boundary. The full local-structure package has that boundary only because it includes this strongest component.

No exact antecedent of the universal active-PD theorem or its sharpness counterexamples was identified in the source passages actually inspected. This statement is deliberately limited to those passages. It must not be promoted to “first,” “previously unknown,” or a statement about unread sections.

### Certification decision

| Proposed claim | Decision as of 2026-10-10 |
|---|---|
| First norm-difference sparse-recovery model | Withdrawn: explicit older models have been read. |
| First support-column independence principle | Withdrawn: the published 2015 `p=2` theorem is an exact predecessor. |
| First automatic strict-complementarity theorem | Not certified; the project proves the wider range `1<p<2`, not a sharp `3/2` threshold. |
| First universal automatic active-PD theorem with sharp `3/2` endpoint | Open. No match in the inspected corpus; two prioritized original bodies and one relevant secondary body remain unread. |
| New mathematics established within the project | C224–C228 have independent proof reception. This is a mathematical evidence classification, not external publication priority. |

The priority target is fixed to the **penalized least-squares model with coefficient one on the negative norm**, every nonzero local minimum, arbitrary no-zero-column `A`, and no RIP, genericity, assumed strict complementarity or assumed second-order sufficiency. A precursor expressed as automatic nondegeneracy, strict second-order sufficiency, local strong convexity or an equivalent active-face curvature conclusion must be checked even if it never says “Hessian” or “3/2”. Conversely, recovery of a global constrained solution, support rank, smoothed Hessian bounds, a conditional positive-Hessian theorem, and a conditional KL rate are not logically interchangeable with this target. Stronger prior hypotheses may give a genuine partial predecessor without proving the full target.

Git revisions identify project versions, not independent publication dates. Author-controlled commit timestamps alone do not certify public availability, global precedence or a journal publication. This audit issues no priority certificate on that basis.

## Evidence ledger

| Source and version | Actual access and precise locator | Consequence for this project |
|---|---|---|
| Yingnan Wang, *New Improved Penalty Methods for Sparse Reconstruction Based on Difference of Two Norms*, [Optimization Online PDF](https://optimization-online.org/wp-content/uploads/2015/03/4849.pdf). Cover dates: March 2013; revisions August 2013 and August 2014; server upload path March 2015. | Complete 11-page author report obtained; model, algorithm, convergence proof and reference passages read. Equation (5), p.2, constrained `l1-epsilon lr`, `r>1`, `0<epsilon<=1`; §III, equation (14), p.4, least-squares variant with **`0<epsilon<1`**; Theorem 3.3, p.5, and its appendix proof: descent, boundedness and stationary cluster points. | Model-family priority is closed against the present project. The displayed least-squares algorithm theorem excludes `epsilon=1`; it is not a theorem about all nonsmoothed local minima or the full limiting-subdifferential resolvent. Do not silently enlarge its parameter range. |
| Yin–Lou–He–Xin, *Minimization of l1-2 for Compressed Sensing*, SISC 37(1), A536–A563 (2015), DOI [10.1137/140952363](https://epubs.siam.org/doi/10.1137/140952363). [Author-hosted published PDF](https://www.math.uci.edu/~jxin/DL12_sisc_2015.pdf). | Complete 28-page journal PDF obtained. Model (1.4), p.A537; §2.3, Theorem 2.3, pp.A542–A543: constrained support independence. Theorem 2.4 and Corollary 2.1(a), p.A543: least-squares support independence and support size at most `m`. Model setup assumes underdetermined full-row-rank `A` and `b!=0`. The [June 24, 2014 author manuscript](https://www.math.uci.edu/~jxin/cam14-01.pdf), pp.7–8, has the same theorem numbers. | Explicit antecedent to the support conclusion; it is not active-Hessian positive definiteness. Theorem **4.1**, p.A550, concerns simulated annealing convergence in probability, not support rank. The proof uses equal-fit perturbations and strict convexity of the Euclidean norm. |
| Dan Wang–Zhuhong Zhang, *Generalized Sparse Recovery Model and Its Neural Dynamical Optimization Method for Compressed Sensing*, CSSP 36, 4326–4353 (2017), [DOI 10.1007/s00034-017-0532-7](https://link.springer.com/article/10.1007/s00034-017-0532-7); online 15 March 2017. | **Partial body:** publisher HTML exposes the Appendix. Proof of Theorem 1, equations (27)–(32): constrained `l1-lp` RIP uniqueness. Proof of Lemma 3, equations (40)–(48): generalized Hessian norm boundedness for a fixed **positive smoothing parameter**. Proofs of Theorems 2–3: neural trajectory existence/uniqueness. Proof of Theorem 4, equation (55) and following: velocity decay and stationary accumulation points. Full main sections/statements remain unavailable. | These accessible results do not establish the claimed automatic active-PD threshold. Smoothed-Hessian boundedness is not unsmoothed active-Hessian positivity. This is **not** an absence conclusion for the full article. |
| Lou–Yan, *Fast L1-L2 Minimization via a Proximal Operator*, JSC 74, 767–785 (2018), [arXiv v4 PDF](https://arxiv.org/pdf/1609.09530v4). | Complete 21-page v4 author manuscript obtained. Proximal characterization: Lemma 1, §2. FBS: Theorem 1, pp.7–8. Global-minimum necessary conditions: Lemma 3, pp.8–9. ADMM: Theorem 2, §4. | The neighboring `p=2` proximal theory and distinction between stationary points and global minima are prior art. This article does not itself establish a parameter-varying `3/2` theorem. A conditional local rate is not an independent novelty claim. |
| Huo–Chen–Ge–Ng, *L1-beta Lq Minimization for Signal and Image Recovery*, SIIMS 16(4), 1886–1928 (2023), [DOI 10.1137/22M1525363](https://epubs.siam.org/doi/10.1137/22M1525363), online 11 October 2023. | **Abstract, metadata and reference list only.** [Official full URL](https://epubs.siam.org/doi/full/10.1137/22M1525363) redirects to a subscription abstract; publisher PDF retrieval did not return a PDF. [HKBU record](https://scholars.hkbu.edu.hk/en/publications/lsub1sub-%CE%B2lsubqsub-minimization-for-signal-and-image-recovery/) provides the DOI but no full-text file. Abstract covers `(beta,q) in [0,1] x [1,infinity)` except `(1,1)`, convex-hull decomposition and RIP recovery. | This remains the most important full-body gap. No theorem number, hypothesis comparison, or absence claim is assigned from its abstract. Its displayed parameter family contains the current penalty. |

Downloaded originals and fingerprints are in
[`sparse_regularity/manifest.json`](../literature/sparse_regularity/manifest.json).
The 2015 journal PDF supplies publication-page locators directly; no manuscript-to-journal theorem renumbering is inferred.

## Mathematical comparison, separate from publication priority

For `Phi_p(x)=||Ax-b||²/2+eta(||x||_1-||x||_p)`, with no zero columns and `eta>0`, the following distinctions are required.

| Claim | Mathematical range established by this project | Priority classification |
|---|---|---|
| Support columns are independent at every nonzero local minimum | Every finite `p>1` | Published `p=2` antecedent exists. The extension follows the same strict-convexity mechanism; do not advertise it as the sharp `3/2` discovery. |
| Every inactive first-order inequality is strict | `1<p<2` | Elementary inactive-coordinate expansion here. Exact prior publication unclosed. It neither needs nor detects the `3/2` threshold. |
| Every active Hessian is positive definite | `1<p<=3/2` | Candidate core result. Requires fourth-order moment inequality and a sixth-order endpoint argument, beyond support independence or a second-order necessary condition. Exact priority open. |
| Strict local minima with singular active Hessian exist | Every finite `p>3/2`, under [C225-v2](../topics/sparse_recovery/automatic_regularity.md#sr-sharpness-all-p) | Candidate sharpness result. The full-space radial minimization argument is essential; a restriction to a tangent line does not prove local minimality. Exact priority open. |
| Isolation, linear residual EB and local linear proximal convergence | At the automatic nondegenerate minima, with stated small-step/basin conditions | Primarily standard local consequences. The complete-resolvent output exclusion is a useful explicit certification, not proof that a new general PPA principle is necessary. |

The direct support proof is short. On the active orthant, a nonzero `z` with `A_I z=0` keeps the data term constant and the `l1` term affine. For all finite `p>1`, strict convexity of `||.||_p` makes the average of `Phi(x+tz)` and `Phi(x-tz)` strictly smaller unless `z` is radial. If `z` is radial, then `Ax=0`. Active stationarity dotted with `x` forces `||x||_1-||x||_p=0`, hence one-sparsity; the no-zero-column assumption excludes this last case. This is a project derivation using an established proof mechanism, not a claim that the 2015 authors stated the all-`p` version.

There is a small scope issue in directly importing the 2015 unconstrained proof: it reduces to the fiber `Ax=Ax*`, whereas strict noncollinearity in the preceding constrained proof used a nonzero right-hand side. The radial exclusion just given closes that issue under the current assumptions. The project should credit the antecedent while retaining its own explicit hypothesis handling. The zero-column counterexample in C224 explains why one cannot discard that handling.

**Versioned mathematical range update.** The original C225-v1 covers
`3/2<p<2`. C225-v2 retains its symmetric two-dimensional construction and checks
the same radial reduction for every finite `p>3/2`, including `p=2` and `p>2`.
This broadens the mathematical sharpness range, not the certified novelty range.
Strict complementarity still has only the stated `1<p<2` automatic range;
support independence still holds for all finite `p>1`.

## Citation chain and acquisition boundary

Wang–Zhang's accessible Theorem 1 proof explicitly cites [10] Candès–Rudelson–Tao–Vershynin (2005), *Error correction via linear programming*, and [52] Yin–Lou–He–Xin (2015). Its [institutional author profile](https://eie.gzu.edu.cn/2022/0819/c19157a226651/pagem.htm) lists the 2017 paper without a download and identifies a later lead: Wang–Zhang, *KKT condition-based smoothing recurrent neural network for nonsmooth nonconvex optimization in compressed sensing*, NC&A 31, 2905–2920 (2019). This lead has not been imported as theorem evidence.

Huo's official bibliography supplies the following exact links in the chain: [27] Lou–Yan (2018), [28] Lou–Yin–He–Xin (2015), [53] Yin–Esser–Xin (2014), [54] Yin–Lou–He–Xin (2015), and [58] Zhou–Yu (2021), *Minimization of the q-ratio sparsity with 1<q<=infinity for signal recovery*. Bibliographic citation does not establish how a result is used in Huo's unread body. The companion [Lou–Yin–He–Xin published paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/473/11409-Jack_Xin_15.pdf), §2.2, explicitly directs proofs of its listed theoretical properties to its reference [26].

Acquisition attempts included both search engines; exact DOI and title variants; author/institution searches; official PDF and full-HTML routes; and available institutional records. Huo's official PDF returned Cloudflare HTML locally; its full HTML redirected to the abstract. Wang's PDF route returned HTML subscription content, despite an HTTP success code. ResearchGate offered no full text for Huo and no complete main body for Wang. OpenAlex's public metadata reported no OA location for Huo; that is an acquisition clue, never theorem evidence. No access control was bypassed and no author was contacted. The title/abstract of a citing paper was not substituted for the requested originals.

The remaining priority work is specific: obtain the complete Wang 2017 and Huo 2023 bodies and inspect every lemma/theorem/proof concerning minimizer structure, norm curvature, sparsity and local optimality; then follow any relevant cited original. Searching only for “Hessian” or “3/2” is insufficient because an equivalent theorem could be differently phrased. Full-text access through an authorized supplied copy or legitimate institutional route is needed to close those two gates.

<a id="primary-citation-chain-follow-up"></a>
### Primary citation-chain follow-up

The following additional texts were inspected starting from revision `338367f`.
Access to a complete PDF is distinguished from the sections actually read. These
comparisons add evidence about the citation chain; they do not close the two
unread-body gates above.

| Primary source and actual read scope | Exact result and comparison |
|---|---|
| Yin–Esser–Xin, *Ratio and Difference of l1 and l2 Norms and Sparse Representation with Coherent Dictionaries*, [complete UCLA CAM13-21 author manuscript](https://ww3.math.ucla.edu/camreport/cam13-21.pdf), 14 pages. Read §III definitions and proofs, §IV model and algorithms. Huo cites the 2014 journal article as [53]. | §III, pp.7–8, defines the nonnegative feasible set `Ax=b`, explicitly excludes `b=0`, and defines “locally sparse” by absence of another feasible vector with contained support. Theorem III.1 states that **global solutions** of the constrained ratio/difference models have this property. Its proof uses strict convexity of the Euclidean norm. §IV, equation (4.5), pp.10–12, considers least squares on `x>=0, sum(x)>=r>0`; Algorithm 3 is a scaled-gradient scheme. This is an earlier sparsity mechanism, not a theorem about every unrestricted local minimum or a varying-exponent Hessian threshold. Manuscript pagination is used; journal theorem numbering is not inferred. |
| Zhou–Yu, *Minimization of the q-ratio sparsity with 1<q<=infinity for signal recovery*, [complete arXiv:2010.03402v1](https://arxiv.org/pdf/2010.03402v1), 21 pages. Read model, §4 theorem statements, §5 derivations/algorithms and references. Huo cites its 2021 publication as [58]. | §4, p.7, explicitly separates its global recovery results from local-optimality results, whose extension from `l1/l2` to `l1/lq` it leaves conjectural. §5.1, equation (22), Theorem 3 and Algorithm 2, pp.12–14, uses the constrained subproblem `min lambda||z||_1-||z||_q` with `||Az-y||_2<=eta`; Theorem 3 relates its optimal value to the fractional optimum, and Algorithm 2 linearizes the negative norm by DCA. These are prior norm-difference subproblems and algorithms. The theorem read does not concern the active Hessian of the penalized least-squares model. The occurrence of `q=1.5` in its plots is not a sharp automatic-regularity theorem. |
| Lou–Osher–Xin, *Computational Aspects of Constrained L1-L2 Minimization for Compressive Sensing*, [complete UCLA CAM15-08 author report](https://ww3.math.ucla.edu/camreport/cam15-08.pdf), 12 pages. Read §2 lemmas/proofs, §5 weighted-model discussion and §6 comparison. Wang–Zhang lists this computational work as [36]. | Equation (4), p.2, is constrained `l1-l2`. Lemma 3, pp.3–4, proves bounded DCA iterates under **no zero column**; Theorem 1, p.4, states stationarity of each nonzero limit point. §6, equation (22), p.9, directs the unconstrained least-squares convergence theory to its [19], Yin–Lou–He–Xin. Thus this branch leads back to an already identified primary source. Stationarity of algorithmic limit points and its no-zero-column hypothesis do not establish automatic active-Hessian positivity. |
| Tran–Webster, *A class of null space conditions for sparse recovery via nonconvex, non-separable minimizations*, [complete arXiv:1710.07348v2, 14 February 2019](https://arxiv.org/pdf/1710.07348v2), 16 pages. Read §§1–2 and the full Theorem 3.1 statement; its complete proof has not been audited. | §1.1, p.3, expressly studies **global** sparse recovery and distinguishes algorithm-dependent local recovery. Theorem 3.1, pp.6–7, applies to nonnegative-valued, sign-invariant symmetric penalties concave on the positive orthant, with additional strict conditions (R1)/(R2) and NSP/iNSP hypotheses. Its conclusion is uniform constrained exact recovery, with the displayed equal-height exception in the iNSP branch. General nonseparable-penalty theory therefore cannot be cited as an unconditional local-Hessian theorem without a new logical bridge. |

Two similarly named leads require different treatment. The complete
[Zhao–He–Huang–Huang–Li 2020 author PDF](https://web.ece.ucsb.edu/~lip/publications/SmoothingNN-NeuralNetworks2020.pdf),
*A smoothing neural network for minimization l1-lp in sparse signal reconstruction
with measurement noises*, was inspected at its introduction, model and smoothing
convergence passages. Journal p.41, equation (3), is `min ||x||_1` subject to
`||Ax-b||_p^p<=epsilon`: here `p` describes the **residual**, not a negative
regularizer norm. In contrast, the official
[Zhao–He–Huang–Huang 2018 record](https://www.sciencedirect.com/science/article/abs/pii/S0893608017302939),
*Smoothing inertial projection neural network for minimization Lp-q in sparse
signal reconstruction*, describes the genuinely relevant difference family
`0<p<=1<q<=2` and extends Wang–Zhang. Only its abstract/introduction preview was
available; its full body is an additional acquisition lead, with no absence
judgment assigned.

The renewed official Wang PDF opening again yielded subscription HTML or a
retrieval error despite search-index PDF metadata. Huo's official article still
exposed only abstract, bibliography and metadata, and the inspected author
homepages supplied no copy. This follow-up has not found an exact antecedent in
the **passages read**; it neither upgrades novelty nor makes the priority search
exhaustive. Temporary reading copies were kept outside the repository; the
copyrighted texts were not added to git.

<a id="renewed-priority-check"></a>
## Renewed primary-source check, 2026-10-10

Two independent readers pursued the Wang and Huo acquisition branches; the coordinating reader checked the new primary statements and the comparison below. They did not obtain either prioritized complete body. The following are positive reading results, rather than an inference from unsuccessful searches.

### Complete 2026 fractional-regularization comparison

**Paper facts.** Zhao–He–Ma–Wang, *A Unified Fractional Regularization Framework for Sparse Recovery*, [arXiv:2604.23184v2 PDF](https://arxiv.org/pdf/2604.23184v2), dated 27 May 2026 (v1: 25 April 2026), is an 18-page complete manuscript. An independent reader read the full paper, including every proof and Appendix. The coordinating reader checked the statements, model and algorithm, convergence arguments, Appendix and references on pp.1–12 and 16–18. The HTML rendering renumbers results; all locators below use the **PDF** numbering.

| PDF locator | Actual hypothesis and conclusion | Comparison with the target |
|---|---|---|
| Theorem 3.1, pp.5–6 | Closed convex constraint set `Omega`, nonzero `x*`, `p>1`, `0<q<=1`, a `C1` increasing transform `phi` with positive derivative. First-order stationarity of `phi(||x||_1/||x||_p^q)` is equivalent to stationarity of constrained `||x||_1-alpha||x||_p`, with **point-dependent** `alpha=q||x*||_1/||x*||_p`. | Relevant norm-difference equivalence, but a first-order constrained assertion, not automatic second-order structure of the penalized least-squares model. The coefficient `alpha=1` is **not excluded**: choose `q=||x*||_p/||x*||_1`. |
| Theorem 4.1, p.6; Lemmas 4.2–4.3, p.7; proofs pp.16–17 | RIP-based noisy global recovery and supporting norm inequalities. | Different hypothesis and conclusion from geometry at every local minimum. |
| Algorithm 5.1, pp.8–9; Theorems 6.1–6.2, pp.10–11 | Proximal MM for a log-ratio objective, descent and stationary cluster points. | An MM surrogate update does not identify the complete resolvent of the original least-squares norm-difference objective. |
| Lemma 6.3, pp.11–12; Theorem 6.4, p.12 | Relative error in the stated composite/Lipschitz setting; the MM theorem assumes a lower-bounded objective, the KL property and `beta>L`. Its rate is **conditional** on the KL exponent: linear for `theta in (0,1/2]`, sublinear for `theta>1/2`. | No automatic value of the KL exponent or active-Hessian positivity is derived here. A conditional rate cannot supply the threshold theorem. |

The full theorem/proof comparison found no automatic active-PD result or sharp `3/2` statement in this version. Its reference [15] is Huo et al. (2023), and [26] is Xie–Su–Ge (2023), a RIP recovery paper. Neither reference's title transfers an unread-body theorem to this audit; in particular the complete 2026 paper cannot stand in for Huo's missing original.

**Project derivation: why the first-order bridge is insufficient.** On a fixed nonzero active orthant let `a(x)=||x||_1`, `r(x)=||x||_p`,
`U(x)=a(x)r(x)^(-q)`, and `V(x)=a(x)-alpha r(x)`, with `alpha=q a*/r*` held fixed. On an affine feasible tangent direction `d`, first-order stationarity gives `a'[d]=alpha r'[d]`. Direct differentiation then gives

\[
 U''[d,d]=r_*^{-q}V''[d,d]
   +q(1-q)a_*r_*^{-q-2}(r'[d])^2.
\]

Indeed, use `a''[d,d]=0` in
`U''=-2q r^(-q-1)a'[d]r'[d]-q a r^(-q-1)r''[d,d]+q(q+1)a r^(-q-2)(r'[d])^2`, and substitute the stationary identity. For `q<1` the additional term is generally nonzero. This is an explicit nonidentity of second-order forms, not a claim that the cited authors asserted such an identity, nor a counterexample to every possible local-minimum transfer theorem. Even when `q=1`, the comparison is for constrained norm-difference models; an additional argument would be needed for the Gram term and the universal least-squares curvature threshold. No fourth/sixth-order automatic-positivity proof is supplied by the cited first-order equivalence.

### Two title-based false leads

| Source, version and actual reading | Resolved distinction |
|---|---|
| Qu–Yang–Liu–Zhao–Wei, *L1-Lp Minimization via a Distributed Smoothing Neurodynamic Approach for Robust Multi-View Three-Dimensional Space Localization*, Applied Sciences 16(1), 403, issue 2026; published **30 December 2025**, [DOI 10.3390/app16010403](https://www.mdpi.com/2076-3417/16/1/403). Complete 21-page publisher PDF obtained. Read pp.1–11 and references pp.19–21, including both theorem proofs; numerical sections pp.12–18 were not audited. | Equation (7), p.6, is `min ||v||_1` subject to `||Av-b||_p^p<=epsilon`, with `1<=p<=2`. The exponent belongs to the residual constraint, not to a negative regularizer. Theorem 1 and its proof, pp.7–8, concern KKT/equilibrium; Theorem 2, pp.8–11, concerns the smoothed neural system. Its positive Lyapunov function is not a positive active Hessian. Reference [31], p.20, cites Wang–Zhang; [32] cites the analogous residual-norm model in 2020. This title is not an exact model match. |
| Xiu–Kong–Li–Qi, *Iterative Reweighted Methods for l1-lp Minimization*, COAP 70, 201–219 (2018), online 5 January 2018, [DOI 10.1007/s10589-017-9977-7](https://link.springer.com/article/10.1007/s10589-017-9977-7). Official abstract and indexed model excerpt read; the author-hosted complete PDF was **not** obtained. | The official abstract fixes `0<p<1`; the indexed equation (5) uses `||Ax-b||_1+lambda||x||_p^p`. This is not subtraction of the two decision-variable norms for `p>1`. The model/parameter mismatch closes this title-based lead; no whole-paper absence claim is made from a preview. |

The two obtained 2026 PDFs have pinned URLs, sizes, SHA-256 fingerprints and explicit reading scopes in [the manifest](../literature/sparse_regularity/manifest.json). Temporary reading copies remain outside git. No priority conclusion depends on the excluded numerical sections.

### Refined Appendix interpretation and remaining acquisition gates

All seven exposed Wang–Zhang Appendix proof blocks were checked again: Lemma 1 (24)–(26), Theorem 1 (27)–(32), Lemma 2 (33)–(39), Theorem 2, Lemma 3 (40)–(48), Theorem 3 (49)–(51), and Theorem 4 (52)–(55) and its closing argument. **Theorem 2's `B(x)=||Ax-b||^2/2` is a constraint-feasibility auxiliary:** along its neural trajectory `dot B=-2B/epsilon`. The appearance of a squared residual there is not a theorem about local minima of the penalized least-squares objective. Locators are proof headings and formula numbers, not invented journal page numbers.

Having all exposed Appendix proofs still does not establish the complete main-body result inventory. Inline proofs, corollaries or differently phrased structural remarks in the missing main sections remain unexamined. Thus this check supports a seven-block comparison, not a full-article absence certificate.

The following official routes were actually checked:

- Wang's [official institutional profile](https://math.sgmtu.edu.cn/info/1096/1069.htm), reached through the institution's staff directory, has no manuscript attachment or personal-homepage link. Zhang's [institutional profile](https://eie.gzu.edu.cn/2022/0819/c21642a226651/page.htm) lists the 2017 article at item 15 and the later KKT-smoothing article at item 8, without manuscript downloads. The ResearchGate preview only exposed the journal's first page, p.4326, not the 28-page body.
- Huo's [current institutional profile](https://math.haust.edu.cn/info/2197/10843.htm) confirms a 2023 doctorate at CAEP. The [official CAEP literature navigation](https://site.gscaep.ac.cn/) explicitly marks its literature system as intranet-only. That access boundary was respected; no intranet resource was accessed. No public corresponding thesis chapter was obtained. The HKBU paper record and checked author pages supplied no downloadable body.
- Zhao–He–Huang–Huang (2018), *Smoothing inertial projection neural network for minimization Lp-q in sparse signal reconstruction*, Neural Networks 99, 31–41, [DOI 10.1016/j.neunet.2017.12.008](https://doi.org/10.1016/j.neunet.2017.12.008), is still a relevant secondary gate. Its [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29306802/) confirms online publication **20 December 2017**, with issue date March 2018. The [official author profile](https://ceie.swu.edu.cn/info/1114/5898.htm) lists it without a manuscript attachment. Its preview does not support a claim about all body theorems.

Acquisition metadata for Wang and Zhao supplied no additional OA location; that is only a search boundary. Equivalent phrases such as nondegeneracy, strict second-order sufficiency and local strong convexity were also searched. None of these unsuccessful routes count as evidence of theorem absence. No email was sent, no access control was bypassed, and no unread source was used as a mathematical dependency.

### Manuscript-safe contribution statement and next decisive evidence

The current admissible statement is: **“We prove a sharp automatic active-Hessian positivity threshold at `p=3/2` for every nonzero local minimum of the stated least-squares norm-difference model, and derive certified complete proximal dynamics. No exact predecessor was identified in the primary passages reviewed; publication priority remains unverified.”** The mathematical assertion is backed by the project proofs. Its first-publication status is not asserted.

The next decisive evidence is the complete legally available Wang 2017 and Huo 2023 bodies, together with any relevant structural theorem they cite; the relevant Zhao 2018 body must also be resolved. Check exact model coefficients, all-local-minimum versus stationary/global quantifiers, matrix assumptions, exponent ranges, active-face curvature and upper-side degenerate strict minima. If only one side of the threshold is prior, credit that theorem and reassess the endpoint/sharpness contribution separately. If the complete sharp theorem is prior, retract that novelty claim; the ordinary proximal consequences cannot rescue it by changing the algorithm name. Resolving these gates would permit a stronger **bounded literature assessment**, not a proof that every publication worldwide has been searched.

**Independent reception of this revision.** The Wang reader accepted the seven Appendix locators, feasibility-auxiliary interpretation, Zhao2018 metadata and preview boundary, and the bounded certification wording. The Huo/fractional reader accepted the PDF theorem locators, `alpha=1` inclusion, affine-active-face second-order calculation, conditional KL interpretation and remaining body gates. Their reception covers source comparison and wording; it does not re-certify C224–C228 or turn an acquisition failure into a priority proof.

## Bounded paper-value assessment

If the sharp automatic-PD threshold survives the remaining audit, it is a coherent mathematical paper center: a parameter transition in the local-minimum geometry, proved for arbitrary least-squares data without RIP or genericity, including a delicate endpoint and genuine full-space degenerate minima above the threshold. This is stronger and more specific than renaming a standard local PPA convergence argument.

The support-rank extension, strict complementarity, explicit error-bound constants, and certified full proximal basin are useful supporting results. They should explain consequences and scope rather than inflate the novelty count. The manuscript must distinguish all local minima from arbitrary stationary points and recovery of a sparse ground-truth signal; these are different claims.

If an exact active-PD/threshold antecedent is found, retract the corresponding novelty claim immediately and map its assumptions and proof to C224–C225. A standalone contribution would then require an independently new theorem, such as a proved sharp basin-conditioning law or a genuinely new dynamical classification. Basic identification and local linear convergence alone do not justify a paper by rebranding them as PPA/RLEB. Publication suitability cannot be certified before the outstanding primary-text checks are completed.
