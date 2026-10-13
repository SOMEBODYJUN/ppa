# Intrinsic zero geometry from uniform finite-length PPA tails

Scope: independent research note, not a registered claim or canonical edit. Read `AGENTS.md`, `RESEARCH_PROTOCOL.md`, the repository academic-writing skill (proof-review mode), C02-v3, C09/C11, C249/C250/C253, C242, and C244/C254. The existing canonical claims retain their exact identities.

## 1. What is already established and what needs an extra gate

C11 already proves, without a manifold hypothesis, that its **single continuous graph-block map** has an open basin and a continuous orbit-limit retraction onto `S∩U`. It explicitly proves the weak local-contractibility quantifier below and explicitly does not claim a deformation retraction. Its ENR conclusion is therefore an intrinsic conclusion, not a disguised regularity assumption.

C02-v3 and C249/C250 allow multiple complete outputs and only compare each output to a nearest zero anchor. Those hypotheses do **not** compare nearby inputs, so they do not supply continuity or single-valuedness. To carry the same geometric argument to a complete PPA, one must add or independently verify:

- the same complete resolvent is a single map `T` on the relevant neighborhood;
- `T` is continuous there;
- the actual target is the intended complete zero set, or an isolated zero cluster explicitly distinguished from the global zero set;
- uniform finite-length tails hold on an open neighborhood of that target.

All-pair RL on the same complete graph, together with input coverage, supplies the first two gates. A global reflected Hölder bound also supplies continuity. The anchor-only theorem by itself does not.

For ordinary and generalized complete resolvents, `Fix T = zer F` wherever the complete single map is defined: `x∈J^v_{λF}(x)` is exactly `0∈F(x)`. Noninjectivity of the kernel does not break that identity, though it can break single-valuedness and physical convergence. A selected map has `Fix T⊂zer F`; other complete zeros may fail to be fixed by the selection.

## 2. Exact C02 open-basin transfer

Assume C02-v3 applies to the complete single continuous map `T` and its same closed target `S`. Put

\[
B(t)=(t+Lt^\gamma)/2,\qquad
\mathcal L(t)=\sum_{j\ge0}B(\kappa^jt)
=\tfrac12\{t/(1-\kappa)+Lt^\gamma/(1-\kappa^\gamma)\}.
\]

Define

\[
O=\{x\in U:d(x,S)<R,\ \mathcal L(d(x,S))<D_U(x)\},
\qquad D_U(x)=d(x,\mathbb R^n\setminus U).
\]

This is open and contains `S∩U`. The theorem's one-step bounds give `d(Tx,S)≤κd(x,S)` and `||Tx−x||≤B(d(x,S))`. Since

\[
\mathcal L(t)-B(t)=\mathcal L(\kappa t),
\]

the global 1-Lipschitz estimate for distance to `U^c` gives

\[
D_U(Tx)\ge D_U(x)-\|Tx-x\|
>\mathcal L(d)-B(d)=\mathcal L(\kappa d)
\ge\mathcal L(d(Tx,S)).
\]

The positive right-hand side first proves `Tx∈U`, without assuming that fact. Therefore `T(O)⊂O`.

Define

\[
P(x)=\lim_{k\to\infty}T^kx\in S\cap U.
\]

Every finite iterate is continuous on `O`, and

\[
\sup_{x\in O}\|T^kx-Px\|\le\mathcal L(\kappa^kR)\to0.
\]

Thus `P` is continuous. The zero-distance anchor forces `Tp=p` for `p∈S∩U`, so `Pp=p`. This is an ENR proof directly from the definition: `S∩U` is a retract of its Euclidean open neighborhood `O`.

This transfer is a new candidate bridge from the continuous complete version of C02; C11 already carries the corresponding graph-block/general-modulus identity.

## 3. C249/C250 have a positive-radius discontinuity issue, and a repair

C249's `a,ω,h` are assumed continuous at zero, but not at every positive radius. Consequently its sum

\[
\Theta(t)=\sum_{j\ge0}H(\kappa^jt)
\]

need not be continuous for positive `t`. Copying the literal C11 formula `O={Θ(d)<D_U}` without checking openness is invalid.

There are two valid repairs.

**Simple compact-target repair.** If `S` is compact and `S⊂U`, choose `r>0` with `r<R` and

\[
r+\Theta(r)<d(S,U^c).
\]

The right side is positive (or infinite if `U=R^n`), and `Θ(r)→0`, so this is possible. Every input in the closed tube `N_r={d(x,S)≤r}` satisfies the strict initial budget. The one-step contraction makes the open tube `{d<r}` forward invariant. Its uniform tail bound proves a continuous retraction to `S` if the complete single `T` is continuous.

**Exact general open-basin repair.** For `0≤t<R`, set

\[
\Theta^+(t)=\lim_{s\downarrow t}\Theta(s),\qquad
H^+(t)=\lim_{s\downarrow t}H(s).
\]

The series is dominated by `ΣH(κ^jR)<∞`, and each summand tends to zero at zero. Hence `Θ(t)→0`, `Θ^+(0)=0`, and `Θ^+` is finite, monotone, right-continuous, and upper semicontinuous on `[0,R)`. The exact sum identity, with right limits, yields

\[
\Theta^+(t)=H^+(t)+\Theta^+(\kappa t).
\]

Now

\[
O^+=\{x\in U:d(x,S)<R,\ \Theta^+(d(x,S))<D_U(x)\}
\]

is open and contains `S∩U`. Each input already satisfies the theorem's original budget because `Θ≤Θ^+`. The step bound and recurrence imply

\[
D_U(Tx)>\Theta^+(d)-H(d)
\ge\Theta^+(\kappa d)\ge\Theta^+(d(Tx,S)),
\]

so `O^+` is forward invariant. Uniform tails `Θ(κ^kR)→0` again produce a continuous retraction.

The same argument applies to C250 once its scalar energy gate supplies the same distance contraction. None of these steps establishes continuity of `T`; that remains an explicit gate.

## 4. Intrinsic conclusions and forbidden overclaims

Let `A=S∩U` be the resulting retract. For every `p∈A` and every relative neighborhood `V` of `p` in `A`, continuity of `P` gives `ε>0` with

\[
B(p,\varepsilon)\subset O,\qquad P(B(p,\varepsilon))\subset V.
\]

For `W=A∩B(p,ε/2)`, the explicit map

\[
H(t,x)=P((1-t)x+tp)
\]

contracts the inclusion `W→V` to `p` and fixes `p`. This is the precise local-contractibility conclusion. It does not assert that `W` itself is contractible or that `O` deformation retracts to `A`.

The following implications are justified:

- `A` is a Euclidean neighborhood retract;
- `A` is locally contractible in the inclusion-into-a-larger-neighborhood sense;
- compact targets have finite-rank rational homology and only finitely many connected components (also follows from the finite-polyhedron domination constructed below);
- Cantor zero sets and Hawaiian-earring zero sets cannot satisfy the entire continuous complete uniform-tail package on a neighborhood.

For a perfect Cantor set, every continuous path is constant. A contraction of a neighborhood containing another point to `p` is therefore impossible. For the Hawaiian earring, every neighborhood of the common origin contains an entire sufficiently small circle. Collapsing all other circles to the origin gives a continuous retraction onto that circle, so a nullhomotopy of the inclusion would imply a nullhomotopy of the circle's identity, which is impossible. These are direct obstructions, not appeals to smoothness.

The package does **not** imply convexity, a `C^1` manifold, constant dimension, an embedded smooth stratum structure, or a positive-reach nearest-point projection. ENRs include finite polyhedra and branching complexes. To prove that such singular examples occur under a given RLEB certificate, one must actually build and certify the complete operator; citing the abstract ENR class only shows the topological conclusion itself is weaker.

## 5. A compact non-smooth complete example under the strongest global geometry

Let `K⊂R^n` be a nonempty compact convex set, e.g. a square, and put

\[
F(y)=y-P_Ky,\quad \lambda=1,\quad
T(x)=\tfrac12(x+P_Kx),\quad C(x)=2T(x)-x=P_Kx.
\]

Projection along the ray from `P_Kx` to `x` is constant, so `P_K(Tx)=P_Kx`. Thus `x−Tx=F(Tx)`. Uniqueness follows either from monotonicity of `F=Id−P_K` or directly from this projection-ray formula. The complete resolvent is exactly the displayed `T`, and `zer F=K`.

The true residual is `r_F(y)=d(y,K)`. The nearest zero anchor is `p=P_Kx`, and `C(x)=p`, giving the C02 anchor with `L=0`. Use `ψ(t)=t`, any `R>0`, `bart≥R/2`, and `κ=1/2`. Direct compatibility is `ψ(r/2)=r/2`; `U=R^n` makes the strict budget automatic. Every initial point has

\[
T^kx=P_Kx+2^{-k}(x-P_Kx),\qquad P=P_K.
\]

Since `P_K` is 1-Lipschitz and its range has diameter `D`, for every `0<γ_*<1` and `D>0`,

\[
\|C(x)-C(y)\|\le\min\{\|x-y\|,D\}
\le D^{1-\gamma_*}\|x-y\|^{\gamma_*}.
\]

This is a complete globally sublinear-Hölder reflection, a global RLEB-certified PPA, and all-initial global convergence, with the entire square as its zero set. Therefore a single-point conclusion requires the extra **closed manifold without boundary** hypothesis used in C244; compact ENR and contractibility alone do not yield a singleton. A square has corners and is not a `C^1` embedded manifold without boundary.

## 6. New compact ENR local-index bridge: no smooth tube is required

Assume `S` is a nonempty compact target, a continuous complete map `T` has a certified invariant open neighborhood containing `S`, and there are uniform finite-length tails and a strict distance contraction `d(Tx,S)≤κd(x,S)`, `κ<1`, in a full small tube. These properties follow from the complete continuous C02/C249/C250 package just explained. They imply the continuous retraction `P`.

Choose `0<a<b<c` with `κc<a` and the closed `c`-tube certified. For a sufficiently fine grid, the finite union `K` of closed cubes meeting the closed `b`-tube satisfies

\[
N_a\subset\operatorname{int}K\subset K\subset N_c,
\qquad T(K)\subset N_{\kappa c}\subset\operatorname{int}K.
\]

`K` is a compact finite cubical polyhedron, hence a compact ENR. It is not asserted to deformation retract onto `S`.

Let `A=T|K`, `j:S→K` be inclusion, and `p=P|K`. Uniform convergence gives some `m` with

\[
\sup_{x\in K}\|T^mx-Px\|
<d(S,\mathbb R^n\setminus\operatorname{int}K).
\]

The straight homotopy between `T^m|K` and `jp` consequently stays in `K`, because each segment stays inside a ball around `Px∈S` lying in `intK`. Therefore

\[
A_*^m=j_*p_*.
\]

We also have `pj=Id`, `Aj=j`, and `pA=p` (orbit limits are shift invariant). Over rational homology,

\[
H_q(K;\mathbb Q)=j_*H_q(S;\mathbb Q)\oplus\ker p_*.
\]

On the first summand `A_*` is the identity. On the second it is nilpotent, since its `m`th power is zero. Hence

\[
\operatorname{tr}(A_*|H_q(K;\mathbb Q))=\dim H_q(S;\mathbb Q),
\qquad L(A)=\chi(S).
\]

The same splitting establishes that `H_q(S;Q)` is finite dimensional and vanishes above the dimension of `K`; its Euler characteristic is therefore defined without importing a finite-CW-type theorem for compact ENRs.

Compact-ENR index normalization gives `i_K(A,K)=χ(S)`. For ambient transfer, the strict trapping and continuity give an open `W⊃K`, contained in the original certified region, with `T(W)⊂intK`. Apply index commutativity to `T:W→K` and the inclusion `K→R^n`. Both composites have exactly the fixed set `S`. Localization then gives

\[
\boxed{i_{\mathbb R^n}(T,V)=\chi(S)}
\]

for every sufficiently small isolating neighborhood `V` of `S` (or any such neighborhood contained in the certified region and containing all of this cluster).

This was independently checked by subagent `enr_index_attack`. It is an unregistered candidate extension of C254 from smooth closed zero manifolds to the intrinsically derived compact ENR zero cluster. It uses a trapping polyhedron and nilpotent complementary homology, not an unsupported deformation retraction.

**Broader finite-length version.** If an invariant open basin `O` has locally uniform tails of the actual total length, define

\[
\ell(x)=\sum_{k\ge0}\|T^{k+1}x-T^kx\|.
\]

Then `ℓ` is continuous, `d(x,S)≤ℓ(x)`, `ℓ|S=0`, and `ℓ(Tx)=ℓ(x)−||Tx−x||`. For small `a>0`, the compact sublevel `N={x∈O:ℓ(x)≤a}` contains `S` in its interior and satisfies `T(N)⊂intN`. Choose `U⊃N` with `T(U)⊂intN` and a finite cubical `K` with `N⊂intK⊂K⊂U`. The proof above then works without an explicit one-step distance contraction. The invariant-basin and local uniform **length-tail** assumptions are essential in this formulation; merely pointwise convergence does not make `ℓ` continuous.

The exact classical interfaces are Benjamin–Gottlieb, *Fixed Point Indices and Manifolds with Collars*, author PDF, §2.1.1 localization, §2.1.4 compact ENR normalization, and §2.1.6 commutativity. The author PDF was opened and these statements read in full:
https://www.math.purdue.edu/~gottlieb/Bibliography/62.pdf

## 7. Global completion and all-initial attraction have distinct consequences

If `C=2T−Id` is globally `γ_*`-Hölder with `0<γ_*<1`, then

\[
\|C(x)\|\le\|C(0)\|+L_*\|x\|^{\gamma_*}.
\]

It follows that `T` strictly maps a sufficiently large closed ball into its interior and has no fixed point outside it. Its entire fixed set is compact, and its ambient total index is `1` by ball normalization. Combining this with the preceding compact-cluster index gives

\[
i(T,\text{outside the local cluster})=1-\chi(S).
\]

If `S=zer F=Fix T` is the entire zero set, this yields `χ(S)=1`. If `S` is just a local cluster, it yields only the index balance. In particular, `χ(S)≠1` forces an additional complete zero, but `χ(S)=1` does not prove a zero-preserving completion exists.

This global conclusion needs the finite-length ENR package, but it does not need the prior smooth-manifold assumption. The existing C244/C254 claims remain restricted to their current smooth identities until this bridge is registered.

**All-initial attraction is stronger.** Suppose every initial point eventually enters the certified open basin `O` and the complete `T` is continuous globally. Define the global limit by the eventual tail. For each `x`, choose `m` with `T^mx∈O`; continuity provides a neighborhood `W` of `x` mapped into `O`. On `W`,

\[
P_{\rm glob}=P\circ T^m,
\]

so the global limit is continuous. It is a retraction `R^n→S`. For any `s_0∈S`,

\[
H(s,t)=P_{\rm glob}((1-t)s+ts_0)
\]

contracts `S`. Thus **contractibility**, not merely Euler characteristic `1`, is the intrinsic global-attraction obstruction.

If `S` is compact, the weaker assumption `d(T^kx,S)→0` for every `x` implies eventual basin entry, since `O` contains a whole uniform small tube. Compact initial sets have a common entry time by continuity, finite covering, and forward invariance; they consequently have uniform tails. Compactness is not needed when eventual basin entry is itself assumed.

For a noncompact target, `d(T^kx,S)→0` need not imply entry into a basin whose thickness shrinks at infinity. A full uniform distance tube, or an explicit eventual-entry condition, is then necessary. C242's zero line is noncompact and contractible, and its explicit global limit is a continuous retraction; its failure of global sublinear reflection means the compact index-balance argument cannot be imported.

## 8. Research interpretation

There is a useful conditional geometric hierarchy:

1. complete continuous local uniform finite-length PPA → local ENR / local contractibility;
2. compact cluster plus global sublinear reflection → local index `χ` and total index `1`;
3. entire compact zero set → necessary `χ=1`;
4. all-initial attraction plus local uniform tails → a global retraction, hence contractible zero set;
5. additionally a compact closed manifold without boundary → singleton.

None of these is a characterization of strict RLEB membership. Even the same singleton can support both a strict RLEB-certified map and a slow complete map with no possible fixed-factor strict contraction certificate. Zero geometry is an obstruction layer; operator dynamics and the true-residual/compatibility gates remain essential.


## 9. Sharpness of the continuity gate: arbitrary closed zero sets under anchor-only RLEB

For any nonempty closed `K⊂R^n`, fix `λ=1,v=Id` and define the entire relation

\[
\operatorname{gph}F_K=\{(y,x-y):x\in\mathbb R^n,\ y\in P_K(x)\}.
\]

The complete resolvent is **exactly** `J_FK(x)=P_K(x)`: the implicit input in a graph point is uniquely reconstructed as `x=y+w`, so there are no other proximal roots. Finite-dimensional nearest-point existence supplies all-input coverage. The graph is closed: it is the set of `(y,w)` satisfying `y∈K` and `||w||≤||y+w-z||` for every `z∈K`, an intersection of closed conditions. Domain `F_K` is precisely `K`; this does not prevent complete proximal coverage.

Every `y∈K` has `0∈F_K(y)` (take input `x=y`), while points outside `K` have an empty fiber. Consequently `zerF_K=K`, `r_FK=0` on `K` and `+∞` elsewhere. For every full output `y∈P_K(x)`, choose the nearest zero anchor `p=y`. Then `||2y-x-p||=d(x,K)`.

The complete C02-v3 certificate is

\[
U=\mathbb R^n,\quad R=\bar t=1,\quad L=\gamma=1,
\quad\psi(t)=t/4,\quad\kappa=1/2.
\]

The true output EB holds because all outputs lie in `K`, the residual evaluation window is exactly `1`, and the compatibility is `ψ((t+t)/2)=t/4≤κt`. The theorem's tail budget is `2t`, with no domain boundary obstruction. Every full trajectory enters `K` in one step and is then fixed; all choices, including tie outputs, are covered. Zero-distance inputs `x∈K` have only themselves as outputs; the coordinate input `x=0` can have multiple outputs if `0∉K` (e.g. both outputs for `K={-1,1}`). There is no truncation of remote `F_K` fibers. Distinct outputs at the same input directly violate all-pair RL; no full sublinear reflected-map certificate is asserted.

If `K` is the Cantor set, any continuous selection `s` of `P_K` on a neighborhood must fix all Cantor points there. A small interval containing two such points has a connected continuous image in a totally disconnected set, which is impossible. At each gap midpoint the complete fiber has its two endpoints. Hence neither full single-valuedness nor a continuous selection is available.

Thus **anchor-only complete RLEB admits arbitrary nonempty closed zero geometry**. The ENR theorem belongs to its continuous-single-physical-map subclass, not to the whole C02-v3/C249 selection framework. This is a mechanism relation induced by the global nearest-point algorithm; it is not asserted to equal the standard limiting or convex subdifferential of `δ_K`. The algorithm itself is the entire argmin of `δ_K(y)+||y-x||²/2` for this frozen step size.

An independent attack reconstructed the complete-fiber identity, graph closedness, zero and remote inputs, true-residual values, shared window and budget, and the no-continuous-selection obstruction. No fatal objection was found. Finite two-point inverse checks are in the classification verifier; the arbitrary-closed-set conclusion is analytic.

## Proof admission table

| Gate | Outcome | Exact scope |
|---|---|---|
| Complete input coverage / all fibers | Required extra gate | Must be verified for the same complete physical map; the abstract bridge does not construct a native operator |
| Single-valuedness / continuity | Required extra gate | Not supplied by C02-v3/C249 anchor-only data |
| True residual and common compatibility window | Imported only after verification | Exact same C02-v3 or C249/C250 object; no chosen-value replacement |
| Open invariant basin / physical summable tails | Passed conditionally | C02 continuous budget; compact-target shrink or right-envelope repair for C249 |
| ENR / local contractibility | Passed | Explicit continuous limit retraction and neighborhood inclusion homotopy |
| Compact local index equals Euler characteristic | Independently checked candidate | Finite trapping polyhedron, nilpotent complementary homology, classical ENR index interfaces |
| Global total index / all-initial attraction | Separate conditional gates | Sublinear complete reflection gives 1; eventual basin entry gives contractibility |
| Formal registration / external novelty | Not done | No canonical claim or manuscript numbering changed |

本轮总入口：[RLEB 零集几何分类研究](../../发表成果整理/本轮重构/RLEB零集几何分类研究.md)。此卡只存候选证明与内部检查，不改变规范命题身份。
