# 混合幂核的结构性验证与分层物理收敛阶

本页 C274-v1 给耦合块幂核的规范证明，允许一般强凸非光滑法向目标及真实集合值次微分。完整近端、同锚和物理预算已独立重构；锐物理阶须避开中心层。它属于经典凸 Bregman 理论，公开先行性未认证。

<a id="mixed-power-object"></a>
## 1. Exact raw model and claims

Let `X=R^m × R^d`, `m,d≥1`, with Euclidean product norm. Fix

\[
1<p<q,\qquad q>2,\qquad \lambda>0,\qquad \mu>0.
\]

Let `g:R^m→(-∞,+∞]` be proper lower semicontinuous and μ-strongly convex, with `0∈∂g(0)`. Set

\[
f(u,z)=g(u),\quad F(u,z)=\partial g(u)\times\{0\},\quad
S=\operatorname{zer}F=\{0\}\times\mathbb R^d,
\]
\[
h(u,z)=\frac1p(\|u\|^q+\|z\|^q)^{p/q},\qquad v=\nabla h.
\tag{1}
\]

Use the **complete** relation `J=(v+λF)^{-1}v`. No output selection or removal of nonglobal roots is made. The target is the full physical zero set; the true residual is `r_F(x)=inf{||w||:w∈F(x)}`, with empty value `+∞`.

The following conclusions hold.

1. `J` is a singleton on every input in `X`; it is exactly the complete Bregman argmin. Every orbit exists forever.
2. Every input and its complete output satisfy the same **physical nearest-zero** reflection with `ω=Id`.
3. The global true residual error bound is `d(x,S)≤r_F(x)/μ`.
4. The explicit local data in §4 verify **all** of C249 G1–G5, including physical lifting and the strict retention budget, from the raw parameters.
5. In fact every complete orbit globally has finite physical length and converges to the explicit point in §3. This stronger result comes from an elementary invariant argument.
6. At every initial point with nonzero tangential block, smooth normal objectives have sharp normal and full physical order `q−1`; for arbitrary positive-definite quadratic normal objectives the exact coefficient is in §5. No closed formula for the resolvent is used.
7. With `p=2`, the zero tangential stratum instead gives ordinary PPA. Thus `q−1` cannot hold uniformly near the entire zero set including the origin.

<a id="mixed-power-coverage"></a>
## 2. Complete coverage, true residual, and anchored reflection

Write `r=||u||`, `t=||z||`, `R_q=(r^q+t^q)^{1/q}`. Away from the origin,

\[
v(u,z)=R_q^{p-q}\bigl(r^{q-2}u,t^{q-2}z\bigr),
\tag{2}
\]

with continuous value zero at the origin. The block `ℓ_q` norm `R_q` is a strictly convex norm. Hence `h=R_q^p/p` is convex, strictly convex, `C^1`, and supercoercive because `p>1`. These facts also follow directly from norm convexity, strictness in its triangle inequality, and Euclidean equivalence of norms. For every input `x`,

\[
y\longmapsto h(y)+\lambda f(y)-\langle v(x),y\rangle
\]

is proper, lsc, strictly convex and coercive: `f≥g(0)`, and `h` is supercoercive. It therefore has exactly one global minimizer. The convex subgradient sum rule applies since `h` is finite and continuous everywhere, giving

\[
0\in v(y)+\lambda F(y)-v(x).
\]

Conversely every root of this inclusion is a global minimizer of the convex function. This proves complete coverage, complete uniqueness, and exact agreement with the complete Bregman argmin, including all remote outputs.

Strong monotonicity relative to `(0,0)∈gra ∂g` says

\[
\langle w,u\rangle\ge\mu\|u\|^2
\quad\text{for every }w\in\partial g(u).
\tag{3}
\]

For `u≠0`, Cauchy–Schwarz gives `||w||≥μ||u||`; taking the **infimum over all values** proves

\[
d((u,z),S)=\|u\|\le\mu^{-1}r_F(u,z).
\tag{4}
\]

The formula also holds when the subdifferential is empty, and at `u=0`. Equation (3) proves that no other zeros exist.

The physical nearest point is uniquely `p_x=(0,z)`. For the selected value `w∈∂g(u_+)` supplied by the complete inclusion, set `A=v(y)-v(p_x)` and `B=v(x)-v(y)=λ(w,0)`. The normal block of `v(p_x)` is zero, so

\[
\langle A,B\rangle
=\lambda R_{q,+}^{p-q}r_+^{q-2}\langle u_+,w\rangle\ge0.
\tag{5}
\]

The zero case uses the continuous formula. Thus

\[
\|2v(y)-v(x)-v(p_x)\|=\|A-B\|\le\|A+B\|
=\|v(x)-v(p_x)\|.
\tag{6}
\]

It is the same Euclidean nearest point throughout; no invariant limiting point has replaced it.

<a id="mixed-power-global"></a>
## 3. Global invariant, all-output retention, and physical length

For `t>0`, the tangent equation in the complete inclusion preserves its direction and the scalar

\[
k=K(r,t):=t^{q-1}(r^q+t^q)^{-(q-p)/q}>0.
\tag{7}
\]

For fixed `r≥0`, `K(r,t)` is continuous, strictly increasing in `t>0`, with range `(0,∞)`. Fixing `k` therefore defines a unique `t=t(r)>0` for all `r≥0`. Differentiation gives

\[
t'(r)=\frac{(q-p)t r^{q-1}}{(q-1)r^q+(p-1)t^q}\ge0,
\quad t(0)=k^{1/(p-1)}=:t_\infty.
\tag{8}
\]

The scalar normal gradient magnitude along this invariant curve is

\[
n(r)=(r^q+t(r)^q)^{-(q-p)/q}r^{q-1},
\quad \frac{n(r)}k=\left(\frac r{t(r)}\right)^{q-1}.
\tag{9}
\]

For `r>0`,

\[
\frac{r t'(r)}{t(r)}
=\frac{(q-p)r^q}{(q-1)r^q+(p-1)t^q}<1.
\]

Hence `r/t(r)`, and thus `n(r)`, are strictly increasing. For a nonzero output normal block, dot the normal proximal equation with `u_+/r_+` and use (3):

\[
n(r)\ge n(r_+)+\lambda\mu r_+.
\tag{10}
\]

If `r_+>0`, (10) and monotonicity imply `r_+<r`; if `r_+=0`, then `t_+=t_∞`. Thus normal and tangent radii decrease at each nonstationary step, and every output stays in the box `0≤r_+≤r`, `t_∞≤t_+≤t`. This assertion is proved before using any orbit or infinite sum.

For `t=0`, the tangent equation forces `t_+=0`. Then `n(r)=r^{p-1}`, which is strictly increasing, and the same argument applies. Set `t_∞=0` in this case, and define the normal gradient magnitude to be zero at the full origin. At `r=0`, (3) forces `r_+=0`, and the tangent equation forces `z_+=z`: every zero-input complete fiber is absorbing.

Telescoping (10) along finite prefixes gives

\[
\sum_{j=1}^{N}r_j\le\frac{n(r_0)}{\lambda\mu}.
\tag{11}
\]

Full coverage already gives arbitrary finite continuation. Letting `N→∞` proves `r_j→0`, and the tangent invariant yields

\[
x_\infty=(0,z_\infty),\quad
z_\infty=\begin{cases}
\displaystyle
\left[1+\left(\frac{r_0}{t_0}\right)^q\right]^{-(q-p)/(q(p-1))}z_0,&t_0>0,\\
0,&t_0=0.
\end{cases}
\tag{12}
\]

The actual normal variables may rotate; no radial-ray assumption is made for them. Their movement is bounded by `||u_{j+1}−u_j||≤r_j+r_{j+1}`. The tangent direction is fixed and its radius decreases, so its total variation equals `t_0−t_∞`. Consequently

\[
\boxed{\sum_{j\ge0}\|x_{j+1}-x_j\|
\le r_0+\frac{2n(r_0)}{\lambda\mu}+t_0-t_\infty<\infty.}
\tag{13}
\]

For every index `k`, the same proof gives the physical tail bound

\[
\sum_{j\ge k}\|x_{j+1}-x_j\|
\le r_k+\frac{2n(r_k)}{\lambda\mu}+t_k-t_\infty.
\tag{14}
\]

If `t_0>0`, (8) implies

\[
0\le t(r)-t_\infty
\le\frac{q-p}{q(p-1)}t_\infty^{1-q}r^q.
\tag{15}
\]

Since `n(r)=O(r^{q-1})` and `q>2`, whenever the orbit does not terminate,

\[
\frac{\|x_k-x_\infty\|}{r_k}\to1,
\qquad
\frac{\sum_{j\ge k}\|x_{j+1}-x_j\|}{r_k}\to1.
\tag{16}
\]

The lower bounds in (16) are the direct endpoint distance `≥r_k`; the upper bounds come from (14) and (15).

<a id="mixed-power-certificate"></a>
## 4. Explicit complete C249 certificate

Fix `b>0`, let `U={||z||>b}`, and choose `R>0` small enough that

\[
A_b=b^{p-q},\quad B_b=\frac{q-p}{q}b^{p-q-1},\quad
a(s)=A_b s^{q-1}+B_b s^q,
\quad\kappa=\frac{a(R)}{\lambda\mu R}<1.
\tag{17}
\]

All these constants depend only on raw model parameters and the declared physical window. Define

\[
\kappa_0=\frac{A_bR^{q-2}}{\lambda\mu}<\kappa,\quad
\beta=b\left[1+(R/b)^q\right]^{-(q-p)/(q(p-1))},
\quad C=\frac{q-p}{q(p-1)}\beta^{1-q},
\]
\[
L=1+\kappa_0+CR^{q-1},\quad
\omega(s)=s,\quad\psi(s)=s/\mu,
\quad\mathfrak h(s,t)=Ls.
\tag{18}
\]

Take `bar t≥a(R)/λ`. All C249 moduli satisfy their monotonicity, finiteness and zero-continuity requirements.

**G1**: complete existence and uniqueness were proved above, on all `X`.

**G2 forward**: for `x=(u,z)∈U_R`, write `r=||u||≤R`, `t=||z||>b`. The normal gradient norm is at most `b^{p-q}r^{q-1}`. The tangent gradient difference from `p_x=(0,z)` is

\[
t^{p-1}\left[1-\left(1+(r/t)^q\right)^{-(q-p)/q}\right]
\le\frac{q-p}{q}t^{p-q-1}r^q
\le B_b r^q,
\tag{19}
\]

using `1−(1+s)^{-α}≤αs` for `α,s≥0`. Triangle inequality between the two blocks gives `||v(x)−v(p_x)||≤a(r)`. Equation (6) gives the same-anchor reflection with `ω=Id`.

**G3 physical lifting before retention**: (10) gives

\[
r_+\le\frac{n(r)}{\lambda\mu}
\le\frac{A_b}{\lambda\mu}r^{q-1}\le\kappa_0r.
\tag{20}
\]

The input tangent invariant satisfies `k≥b^{p-1}[1+(R/b)^q]^{-(q-p)/q}`, so its entire invariant curve has `t(s)≥β`, including the complete output, whether or not it lies in `U`. Integrating (8) between `r_+` and `r` gives `||z−z_+||≤Cr^q`. Thus

\[
\|y-x\|\le r+r_++Cr^q\le Lr=\mathfrak h(r,\|v(y)-v(x)\|).
\tag{21}
\]

No output-domain assumption is used. This is a transition lifting bound, not an asserted Lipschitz inverse for the degenerate kernel.

**G4**: the infimum true residual error bound (4) is global, and `K(R)/λ=a(R)/λ≤bar t`.

**G5**: `K=a` and, for `0<s≤R`,

\[
\psi(K(s)/\lambda)=\frac{a(s)}{\lambda\mu}\le\kappa s,
\quad H(s)=Ls,\quad\Theta(s)=\frac{Ls}{1-\kappa}.
\tag{22}
\]

The strict physical initial budget is explicitly

\[
\frac{Lr_0}{1-\kappa}<t_0-b.
\tag{23}
\]

C249 therefore gives every stated retention, distance, physical length and tail conclusion for all such initial inputs. This is a real nonempty neighborhood of every `(0,z_*)` with `||z_*||>b`: choose `r_0` sufficiently small and `z_0` close enough to `z_*`. The stronger direct result §3 also gives the exact retention condition `t_∞>b`, but (23) is the unchanged C249 budget.

<a id="mixed-power-rate"></a>
## 5. Sharp rate, coupled quadratic case, and center obstruction

Assume additionally that `g` is finite and `C^2` on a neighborhood of `0`, with
`A=∇²g(0)≻0`. Let `t_0>0` and `u_0≠0`. A zero output normal block would force `v_N(x)=0`, hence `u=0`; thus this orbit never terminates. Write

\[
c_k=(r_k^q+t_k^q)^{(p-q)/q}r_k^{q-2}.
\]

The normal equation is

\[
c_k u_k=c_{k+1}u_{k+1}+\lambda\nabla g(u_{k+1}).
\tag{24}
\]

Since `r_k→0`, `t_k→t_∞>0`, and `q>2`, `c_k→0`. Taylor expansion at the actual output point yields

\[
u_{k+1}=\frac{t_\infty^{p-q}}{\lambda}
A^{-1}r_k^{q-2}u_k+o(r_k^{q-1}).
\tag{25}
\]

For completeness, inversion of (24) is legitimate asymptotically because
`∇g(u)=Au+o(||u||)` and the matrices `λA+c_{k+1}I` have uniform inverse bound. Also (20), with any eventual positive tangent lower bound, gives `r_{k+1}=O(r_k^{q-1})`; the Taylor error is consequently `o(r_k^{q-1})`. Formula (25) implies sharp two-sided order

\[
\frac{t_\infty^{p-q}}{\lambda\lambda_{\max}(A)}
\le\liminf\frac{r_{k+1}}{r_k^{q-1}}
\le\limsup\frac{r_{k+1}}{r_k^{q-1}}
\le\frac{t_\infty^{p-q}}{\lambda\lambda_{\min}(A)}.
\tag{26}
\]

By (16), the identical statement holds for full physical errors `||x_k−x_∞||`, not only distance to the zero set. It also holds for the remaining physical path length.

For the structurally coupled quadratic subclass `g(u)=1/2⟨Au,u⟩`, let `μ_*` be the smallest eigenvalue of `A` whose eigenspace has nonzero projection of `u_0`. Then exactly

\[
\boxed{\lim_{k\to\infty}\frac{r_{k+1}}{r_k^{q-1}}
=\frac{t_\infty^{p-q}}{\lambda\mu_*}.}
\tag{27}
\]

Indeed (24) gives `u_{k+1}=c_k(λA+c_{k+1}I)^{-1}u_k`. Each eigenspace remains invariant. Relative to the `μ_*` projection, a projection at eigenvalue `ν>μ_*` is multiplied each step by `(λμ_*+c_{k+1})/(λν+c_{k+1})→μ_*/ν<1`. Thus `u_k/r_k` tends to the normalized `μ_*` projection of `u_0`; substitution into (24) proves (27). The same exact limit holds for full physical errors and physical tail lengths by (16). This argument does not solve the nonlinear proximal equations.

The kernel is genuinely nonseparable between `u` and `z` when `p<q`: its mixed derivative is nonzero at nonzero blocks. At every `(0,z_*)` with `z_*≠0`, the normal Hessian vanishes because `q>2`, so no local positive strong convexity modulus for the kernel is available there. The tangential output normally moves, and the limit is the explicit biased point (12), independent of λ and of the normal objective within this class.

The localization `t_∞>0` is essential. Set `p=2`, `t_0=0`, and take the same quadratic `g`. All tangent outputs remain zero and `h(u,0)=||u||²/2`, so the complete normal algorithm is precisely

\[
u_{k+1}=(I+\lambda A)^{-1}u_k,
\tag{28}
\]

which has a nonzero linear rate for any nonzero input. In contrast, every nonzero tangent stratum has order `q−1>1`. Consequently no uniform bound `d(x_+,S)≤C d(x,S)^{q-1}` can hold on a neighborhood of the origin in the full physical space.

<a id="mixed-power-classical"></a>
## 6. Classical overlap and honest value assessment

Primary source consulted: Bauschke–Borwein–Combettes, *Bregman Monotone Optimization Algorithms*, author PDF https://pcombet.math.ncsu.edu/sicon2.pdf, Proposition 3.22 (PDF pp.13–14) and Corollary 3.25 (PDF pp.14–15). Their Proposition 3.22 identifies convex Bregman argmin with the kernel resolvent, gives its fixed set and D-firmness, and gives single-valuedness for a strictly convex kernel. Their Corollary 3.25 applies to a reflexive space, Legendre kernel, and bounded-below lsc convex objective. Our finite-dimensional full-domain `C^1` strictly convex supercoercive kernel is Legendre: gradient local boundedness is immediate and inverse-gradient local boundedness follows from supercoercivity/degree-p growth. Our objective is convex and bounded below. Hence this is inside classical Bregman proximal theory, not an escape from it.

What was independently derived here is an explicit raw-data-to-C249 certificate for a **set-valued normal strongly convex class**, together with a global all-input physical length estimate, explicit tangent drift/limit, sharp `q−1` full physical asymptotics for smooth normal objectives, an exact spectral coefficient for arbitrary SPD quadratic coupling, and a rigorous change-of-order obstruction on the central stratum. These quantitative statements are not claimed to be novel in the literature; their priority requires a targeted search. The global convergence mechanism has a shorter direct proof (§3), so the example cannot substantiate an assertion that the parent theorem is necessary or classical theory cannot handle it.

Hidden assumptions closed: nearest anchor fixed and physical; complete remote root coverage; zero-distance complete absorption; true residual infimum; subgradient sum rule; all output lifting before retention; q>2 for superlinear order and asymptotic tail equivalence; t0>0 for the q−1 stratum; C² only for sharp asymptotics, not the general structural certificate; SPD spectral coefficient only in the quadratic subclass.

Potential value: real structural verification progress beyond a separable scalar toy, with arbitrary nonsmooth coupled normal objectives and an explicit full physical rate mechanism. It is not by itself evidence of broad methodological superiority or publication-level novelty.


复算与精度见 [代码](../code/structural_verification/README.md)，实际正文的独立核查见 [接收记录](../audit/STRUCTURAL_VERIFICATION_REVIEW_2026_10_13.md)。
