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
4. There is a fixed integer K₀, chosen from the normal-error recursion, such that the finite prefix k<K₀ has a compact initial subband D₀⊂D̃ and h₀ small enough that the τ-path barrier has positive margins on this compact band.

Then there is a nonempty open set U of initial (x₀,v₀), with x₀ in Π(D₀) and ‖v₀+∇f(x₀)‖<ε, such that all resolvent steps stay in Π(D̃), the unwrapped lift has θₖ→∞, rₖ→1, and the physical ω-limit is S¹.

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

At the angular lower face, dθ/dτ ≥ βₖ[c₀θ*exp(−θ*²)−C hₖ]. Thus a first contact is impossible once the displayed error is smaller than the corresponding face margin. This is a genuine integer-step argument: the inward field is evaluated at the actual first boundary point, never at an unknown endpoint outside D.

## 2. The normal recursion gives one common open set

For α<1, hₖ₊₁/hₖ = 1−α/(k+1)+O(k⁻²), while γhₖ ≫ 1/(k+1). Therefore, after a finite K, choose M_w so that M_w hₖ is a supersolution of

qₖ₊₁ = (1−γhₖ)qₖ + C hₖ².

For all initial errors in a sufficiently small ball, the finite prefix remains bounded and qₖ=‖wₖ‖≤M_w hₖ for k≥K. The same ε-ball is used at every later step; no k-dependent shrinking of U is needed. The finite-prefix claim follows from continuity of the finitely many resolvent maps and the positive compact-band face margins. This is where openness is obtained; a pointwise orbit estimate alone would not supply it.

## 3. No-wrap and the physical lift

The HJ non-overlap condition gives Π-injectivity on the entire tail closure. Independently, ‖yτ−xₖ‖≤Chₖ and r≥1/2 imply |θ(τ)−θₖ|≤C hₖ. Choose h₀ so this is <π/4 for the finite prefix and use hₖ≤h₀ afterwards. Thus the local polar lift cannot jump by a 2π branch during one homotopy. Since every preceding step stays in D̃, the lifted path concatenates into one continuous unwrapped trajectory. The global Π-injectivity then excludes a later physical self-overlap with a different turn.

## 4. Non-circular angular upper bound

Let φ(s)=s exp(−s²), decreasing for s≥1. The τ estimate gives, while the stopping tube is valid,

Δθₖ ≤ C hₖ φ(θₖ) + C hₖ²,
Δθₖ ≥ c hₖ φ(θₖ) − C hₖ².

The O(hₖ²) term absorbs the O(hₖ) angular variation along yτ because φ′ and sφ(s) are bounded on [1,∞). Put Eₖ = Σⱼ≥ₖ hⱼ², choose h₀ so 2 C E₀ < θ₀−1, and set zₖ = θₖ − C(E₀−Eₖ), E=C E₀. Using the lower estimate in (T12), zₖ≥θ₀−2 C E₀>1, θₖ≤zₖ+E, and Δzₖ≤C hₖφ(zₖ).

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
