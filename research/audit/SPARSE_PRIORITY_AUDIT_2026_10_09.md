# Sparse norm-difference structure: bounded priority audit

Audit date: 2026-10-09. Object audited: C224–C226 in
[`automatic_regularity.md`](../topics/sparse_recovery/automatic_regularity.md),
initially read at repository revision `8ff3ae1`.

## Verdict and scope

**The sharp active-Hessian threshold is a candidate contribution, not a certified first theorem.** The priority gate remains open because the complete bodies of Wang–Zhang (2017) and Huo–Chen–Ge–Ng (2023) have not been obtained. This audit improves the former from abstract-only to substantive, precisely identified Appendix proofs; it does not relabel either paper as fully read. Failed retrieval and unproductive keyword searches provide no evidence that a theorem is absent.

Two broader novelty claims should be withdrawn now. The norm-difference model family predates this project. Support-column independence at all local minima was explicitly proved for the least-squares `l1-l2` model in 2015, without a RIP condition. Moreover, the present proof extends that support conclusion to all finite `p>1`; it has no sharp `3/2` boundary. Strict complementarity follows here for all `1<p<2`. Only **automatic positive definiteness of the active Hessian** has the demonstrated sharp `3/2` boundary. The full local-structure package has that boundary only because it includes this strongest component.

No exact antecedent of the universal active-PD theorem or its sharpness counterexamples was identified in the source passages actually inspected. This statement is deliberately limited to those passages. It must not be promoted to “first,” “previously unknown,” or a statement about unread sections.

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

## Bounded paper-value assessment

If the sharp automatic-PD threshold survives the remaining audit, it is a coherent mathematical paper center: a parameter transition in the local-minimum geometry, proved for arbitrary least-squares data without RIP or genericity, including a delicate endpoint and genuine full-space degenerate minima above the threshold. This is stronger and more specific than renaming a standard local PPA convergence argument.

The support-rank extension, strict complementarity, explicit error-bound constants, and certified full proximal basin are useful supporting results. They should explain consequences and scope rather than inflate the novelty count. The manuscript must distinguish all local minima from arbitrary stationary points and recovery of a sparse ground-truth signal; these are different claims.

If an exact active-PD/threshold antecedent is found, retract the corresponding novelty claim immediately and map its assumptions and proof to C224–C225. A standalone contribution would then require an independently new theorem, such as a proved sharp basin-conditioning law or a genuinely new dynamical classification. Basic identification and local linear convergence alone do not justify a paper by rebranding them as PPA/RLEB. Publication suitability cannot be certified before the outstanding primary-text checks are completed.
