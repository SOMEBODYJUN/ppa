# C303 v5: common-tail invariant theorem audit

状态：**candidate / conditional theorem**。本页审查 resolvent τ-path、误差递推和角度超解能否给出同一个相空间开集 U，使全部离散步留在同一条 HJ 物理尾管。结论是：在明确列出的全局覆盖和 HJ tail gates 下可以闭合；这些 gates 未由本页自行证明，因此不能升级为已完成的 PPA 定理。

## Exact conditional theorem

Let F = ∇χₐ, χₐ = a f − |∇f|²/2, Y = −∇f. Let hₖ = h₀(k+1)^−α with 2/3 < α < 1, βₖ = hₖ/(1+a hₖ), λₖ = hₖβₖ, and

xₖ₊₁ + λₖF(xₖ₊₁) = xₖ + βₖvₖ,   vₖ₊₁ = (xₖ₊₁−xₖ)/hₖ.

Assume:

1. F is globally C¹ and L_F-Lipschitz, λ₀L_F < 1/2. Hence every resolvent homotopy
   y(τ)+τλₖF(y(τ)) = xₖ+τβₖvₖ, 0≤τ≤1,
   is a unique C¹ path.
2. The lifted HJ tail D̃ = {(r,θ): θ>θ*, b₁(θ)<r<b₂(θ)} has r∈[1/2,3/2], physical projection Π(r,θ)=r(cos θ,sin θ) is injective on its closure, and on both radial faces
   ∇sᵢ·Y ≥ m₀ exp(−θ²+θ), while Yθ/r ≥ c₀ θ exp(−θ²) for θ≥θ* > 1.
3. ∇f is Lipschitz on a fixed physical outer strip containing every pre-contact τ-path, and F,Y are bounded there. The normal recurrence holds while the path is in the strip:
   ‖wₖ₊₁‖ ≤ (1−γhₖ)‖wₖ‖ + C hₖ²,
   where wₖ = vₖ+∇f(xₖ), γ>0.
4. Fix a finite prefix index K₀ after which
   hₖ−hₖ₊₁ <= (γ/4) hₖ². Choose η,ρ,σ>0 and the open subband
       D₀°={θ∈(θ*+η,θ*+2η),
             b₁(θ)+ρ<r<b₂(θ)−ρ}.
   Its closure \overline{D₀°} is compact and lies strictly inside the tail.
   Assume the reference finite prefix has τ-path face margin at least σ
   uniformly for every (x₀,v₀) with x₀∈Π(\overline{D₀°}) and
   ‖v₀+∇f(x₀)‖≤ε₀. The finite-prefix update maps are continuous, so this is
   one common margin condition, not a state-dependent selection.

Then there is a nonempty open set
    U={ (x₀,v₀): x₀∈Π(D₀°),
                    ‖v₀+∇f(x₀)‖<ε₀ },
where 0<ε₀ <= c_init h₀² for a fixed c_init>0,

such that all resolvent steps stay in Π(D̃), the unwrapped lift has
θₖ→∞, rₖ→1, and the physical ω-limit is S¹. The h₀² radius handles the
first rapidly decreasing ratio h₁/h₀≈2^(−α); any smaller positive radius is
still an open phase-space condition.

The theorem is conditional because items 1–3 are genuine coverage, cutoff, and recurrence obligations.

## 1. One τ-path closes one integer step

For fixed k define yτ by the homotopy above. The Jacobian I+τλₖDF is invertible with inverse norm at most 2, and strong monotonicity gives a uniform bound on yτ for bounded xₖ,vₖ. Differentiation gives

ẏτ = βₖ (I+τλₖDF(yτ))⁻¹ (vₖ − hₖF(yτ)),   ‖ẏτ‖ ≤ C hₖ.

Define w̃τ = βₖ⁻¹ẏτ + ∇f(yτ). Since λₖ = hₖβₖ, the Lipschitz bounds imply

‖w̃τ − wₖ‖ ≤ C hₖ,   ẏτ = βₖ(Y(yτ)+w̃τ).

The estimate uses only the bounded input and the global/outer-strip bounds; it is not inferred from the endpoint being in D.

Suppose y₁ were outside D̃. Since ‖yτ−xₖ‖≤Chₖ and r≥1/2, the path has a continuous local polar lift. Injectivity of Π on the closed tail fixes the unwrapped branch. Let τ* be its first contact with a boundary face. At a radial face, θ* in the following display means the contact angle θ(τ*), not the fixed lower cutoff θ_*:

(d/dτ)sᵢ(yτ)|τ* = βₖ[∇sᵢ·Y(yτ*) + ∇sᵢ·w̃τ*]
                 ≥ βₖ[m(θ(τ*)) − L_s(C hₖ+‖wₖ‖)].

The displacement bound also gives |θ(τ*)−θₖ|≤C hₖ. Since
hₖ(1+θₖ)→0 and m(s)=exp(−s²+s), the tail estimate gives
m(θ(τ*))/m(θₖ)→1 uniformly along first-contact sequences. Hence
hₖ=o(m(θ(τ*))) and the displayed error is eventually smaller than half
the actual face margin. At the angular lower face,
dθ/dτ ≥ βₖ[c₀θ(τ*)exp(−θ(τ*)²)−C hₖ]. The logarithmic derivative of
φ(s)=s exp(−s²) is O(1+s) on the tail, so the same displacement estimate
gives φ(θ(τ*))/φ(θₖ)→1. Hence hₖ=o(θₖexp(−θₖ²)) makes the angular error
smaller than half the actual entrance-face drift. Thus a first contact is
impossible. This is a genuine integer-step argument: the inward field is
evaluated at the actual first boundary point, never at an unknown endpoint
outside D.

## 2. The normal recursion gives one common open set

For α<1, choose K₀ so that
hₖ−hₖ₊₁ <= (γ/4)hₖ² for every k>=K₀. Let
qₖ₊₁=(1−γhₖ)qₖ+C hₖ² be the scalar majorant from the normal recursion.
Choose ε₀<=c_init h₀² and define the finite-prefix numbers

    B₀=ε₀,
    Bₖ₊₁=(1−γhₖ)Bₖ+C hₖ²,
    M₀=max_{0<=k<=K₀}(Bₖ/hₖ).

The finite maximum M₀ is common to every initial state in the ε₀-ball.
Choose M_w>=max{M₀,4C/γ}. For k>=K₀, the drop hₖ−hₖ₊₁ is absorbed by
the γhₖ² contraction term, so qₖ<=M_w hₖ follows inductively. The h₀²
radius is exactly what prevents the first rapidly decreasing ratio h₁/h₀
from being hidden inside a false all-k invariant argument.

The finite-prefix maps are continuous by complete resolvent coverage. The
uniform margin hypothesis on \overline{D₀°}×{‖w₀‖≤ε₀}, together with the
strict inequalities defining D₀°, makes U above a genuine common open
neighborhood; no k-dependent shrinking of U or state-dependent M_w is used.
This is where openness is obtained; a pointwise orbit estimate alone would
not supply it.

## 3. No-wrap and the physical lift

The HJ non-overlap condition gives Π-injectivity on the entire tail closure. Independently, ‖yτ−xₖ‖≤Chₖ and r≥1/2 imply |θ(τ)−θₖ|≤C hₖ. Choose h₀ so this is <π/4 for the finite prefix and use hₖ≤h₀ afterwards. Thus the local polar lift cannot jump by a 2π branch during one homotopy. Since every preceding step stays in D̃, the lifted path concatenates into one continuous unwrapped trajectory. The global Π-injectivity then excludes a later physical self-overlap with a different turn.

At τ=1 the endpoint equation itself gives
    vₖ₊₁=(y₁−xₖ)/hₖ=(1+a hₖ)⁻¹(vₖ−hₖF(y₁)).
The global F bound and the pre-step velocity bound therefore control the
last-step velocity and provide the local lifted-angle chart for the next
homotopy. If y₁ is known to lie in D̃, this can equivalently be written
vₖ₊₁=Y(y₁)+wₖ₊₁; it cannot be replaced by the derivative-defined
\widetilde w₁ before the first-contact contradiction has been established.

## 4. Non-circular angular upper bound

Let φ(s)=s exp(−s²), decreasing for s≥1. The τ estimate gives, while the stopping tube is valid,

Δθₖ ≤ C hₖ φ(θₖ) + C hₖ²,
Δθₖ ≥ c hₖ φ(θₖ) − C hₖ².

The O(hₖ²) term absorbs the O(hₖ) angular variation along yτ because φ′ and sφ(s) are bounded on [1,∞). Put Eₖ = Σⱼ≥ₖ hⱼ², choose h₀ so 2 C E₀ < θ₀−1, and set zₖ = θₖ − C(E₀−Eₖ), E=C E₀. Using the lower side of the angular estimate above, zₖ≥θ₀−2 C E₀>1, θₖ≤zₖ+E, and Δzₖ≤C hₖφ(zₖ).

For Uₖ = exp((zₖ+E)²/2), negative Δz decreases U. For positive Δz, the mean-value theorem yields

ΔUₖ ≤ C hₖ (zₖ+E) zₖ exp(−zₖ²/2 + E zₖ + E²/2) ≤ C′hₖ.

Hence exp(θₖ²/2) ≤ Uₖ ≤ U₀+C′tₖ and θₖ² ≤ C+2 log(1+tₖ). Consequently

m(θₖ) = exp(−θₖ²+θₖ) ≥ c(1+tₖ)⁻²,
φ(θₖ) ≥ c(1+tₖ)⁻²,

and, since tₖ ≍ k^(1−α),

hₖ/m(θₖ),  hₖ/φ(θₖ) = O(k^(2−3α)) → 0.

This is the exact reason for α>2/3. The bound also makes hₖ exp(θₖ)→0, so the normalized q-coordinate changes by o(1) in one step and the outer-strip gate is preserved.

## 5. Angle divergence and omega-limit

The lower increment is eventually positive. If θₖ had a finite upper limit, φ(θₖ) would be bounded below by a positive constant on that compact interval, while Σhₖ=∞; contradiction. Therefore θₖ→∞. Since bᵢ(θ)=1+O(exp(−θ)), the tube squeezes rₖ→1. The increments Δθₖ→0, so for every phase ϑ and every large turn n, the first index crossing 2πn+ϑ overshoots by at most Δθₖ→0. Thus phases are dense and, with rₖ→1, ω(xₖ)=S¹.

## Remaining fatal obligations / verdict

The τ-path, common-U, no-wrap, and α>2/3 angle bootstrap are internally compatible. I found no counterexample once the stated gates hold. The candidate remains **continue validation**, because the following are still independent proof obligations; the normal-error algebra is separately recorded in `research/c303_normal_error_recursion.md`:

* complete global Lipschitz/coverage for F=∇χₐ, including the actual HJ cutoff extension;
* a uniform outer strip (or global ∇f bound) through which every pre-contact τ-path can be controlled;
* a fully derived D4–D5 normal recursion with constants independent of the unbounded lift angle;
* a finite-prefix compact band whose τ-path margins are explicitly positive.

If any one of these gates fails, the result is only a local branch or a finite numerical observation, not a complete PPA bridge.
