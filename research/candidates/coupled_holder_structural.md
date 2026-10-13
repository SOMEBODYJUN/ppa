# Coupled Hölder cascade: self-contained structural verifier

This is a proposed theorem and proof for root review, not a registered canonical claim. It derives complete-fiber certificates from raw operator assumptions without computing the complete resolvent. The admissible class has a direct, stronger global convergence proof as well; the certificate threshold below must not be called a dynamical convergence threshold.

## Exact object and assumptions

Let the physical Euclidean space be X = R^r × R^s, r,s ≥ 1, with state y=(u,z). Fix λ>0, 0<γ<1, μ>ε≥0, and 0<c≤C<∞. Set

\[
m=\mu-\varepsilon>0,\qquad q=(1+\lambda m)^{-1},\qquad S=\{0\}\times\mathbb R^s.
\]

Let A:R^r ⇉ R^r be maximal μ-strongly monotone, with 0∈A(0). Here μ-strong monotonicity means its graph satisfies ⟨a−a',u−u'⟩≥μ||u−u'||²; maximality is a separate coverage assumption. The standard finite-dimensional Minty resolvent fact is used in exactly this form: J_{λA} is defined everywhere, single-valued and (1+λμ)^{-1}-Lipschitz, and J_{λA}(0)=0. Its Lipschitz estimate also follows directly by subtracting the two resolvent inclusions and taking their inner product with the output difference. For a version with no maximal-monotone import, assume A is continuous and μ-strongly monotone; existence then follows from the outward-pointing inequality on a sufficiently large ball and Brouwer's theorem.

Let K:R^r×R^s ⇉ R^r×R^s be upper semicontinuous with nonempty compact convex values, and impose, for every state (u,z) and every (e,b)∈K(u,z),

\[
\|e\|\le\varepsilon\|u\|,
\qquad c\|u\|^\gamma\le\|b\|\le C\|u\|^\gamma.
\tag{SC1}
\]

The uncertainty is joint: e and b need not be independently selectable, and may depend on the tangential state z. Define the complete operator

\[
F(u,z)=\{(a+e,b):a\in A(u),\ (e,b)\in K(u,z)\}.
\tag{SC2}
\]

Use its complete ordinary proximal relation J=(I+λF)^{-1}, physical kernel v=Id, and physical true residual r_F(y)=inf_{f∈F(y)}||f||, with empty values assigned +∞. All assumptions are global. No selected branch is substituted for J or for this infimum.

K(0,z)={(0,0)} by SC1 and nonemptiness. Thus 0∈F(0,z), while any zero at u≠0 would contradict ⟨a+e,u⟩≥m||u||². Consequently zer F=S, a nonempty closed nonisolated affine zero set, and d((u,z),S)=||u||.

## Complete global input coverage

Fix any input x=(α,β). Put t=||α|| and R_N=qt. For t>0 define compact convex sets

\[
D=\{(u,z):\|u\|\le R_N,\ \|z-\beta\|\le\lambda C R_N^\gamma\},
\qquad E=\{(e,b):\|e\|\le\varepsilon R_N,\ \|b\|\le C R_N^\gamma\}.
\]

On D×E use the correspondence

\[
(u,z,e,b)\longmapsto
\{J_{\lambda A}(\alpha-\lambda e)\}\times
\{\beta-\lambda b\}\times K(u,z).
\tag{SC3}
\]

Each value is nonempty compact convex, the graph is upper semicontinuous, and the map takes D×E into itself. Indeed,

\[
\|J_{\lambda A}(\alpha-\lambda e)\|
\le\frac{t+\lambda\varepsilon R_N}{1+\lambda\mu}=R_N,
\]

and the other three bounds follow directly from SC1. Kakutani gives a fixed point. Its equations are exactly α−u∈λ(A(u)+e), β−z=λb, (e,b)∈K(u,z), so it is an actual output of the full relation J. This proves global input coverage.

At t=0, SC1 and 0∈A(0) show directly that y=x is an output. The all-output estimate below proves it is the only output.

**Important correction:** the tempting state-only correspondence (u,z)↦{(J_{λA}(α−λe),β−λb):(e,b)∈K(u,z)} need not have convex values, because a nonlinear resolvent need not map convex e-sets to convex sets. SC3 uses the uncertainty variables as separate coordinates and avoids that error.

## Every fiber, including far outputs and zero inputs

Take an arbitrary full output y=(u,z)∈J(x); choose only for this inclusion a∈A(u) and (e,b)∈K(u,z) with α=u+λ(a+e), β=z+λb. Write s=||u||. Strong monotonicity relative to (0,0) gives

\[
\langle a+e,u\rangle\ge m s^2,
\qquad (1+\lambda m)s^2\le\langle\alpha,u\rangle\le ts.
\]

Hence s≤qt, including s=0. This bound was proved for every global root and never assumes that the output is already in a local tube. Moreover,

\[
\|z-\beta\|=\lambda\|b\|\le\lambda C q^\gamma t^\gamma.
\tag{SC4}
\]

If t=0, then s=0, b=0 and z=β, so every output is exactly x. The entire complete zero fiber is absorbing.

The unique physical nearest zero anchor to the input is p=(0,β). With this same p,

\[
\begin{aligned}
\|2y-x-p\|^2
&=\|2u-\alpha\|^2+4\lambda^2\|b\|^2,\\
\|2u-\alpha\|^2
&=t^2-4\lambda\langle a+e,u\rangle
\le t^2-4\lambda m s^2\le t^2.
\end{aligned}
\]

Thus, uniformly for every full output,

\[
\|2y-x-p\|\le\sqrt{t^2+4\lambda^2 C^2 q^{2\gamma}t^{2\gamma}}.
\tag{SC5}
\]

This is solution-anchored RL, not a claimed arbitrary-pair graph inequality. The input nearest anchor has not been changed to an output projection.

## True residual, including uncertainty correlations

For any f=(a+e,b)∈F(u,z), both ||a+e||≥m||u|| and ||b||≥c||u||^γ hold. Therefore the genuine infimum satisfies

\[
r_F(u,z)^2\ge m^2\|u\|^2+c^2\|u\|^{2\gamma},
\qquad d((u,z),S)\le\psi(r_F(u,z)),\quad
\psi(\tau)=(\tau/c)^{1/\gamma}.
\tag{SC6}
\]

If F is empty at a point, its residual is +∞ and the finite residual implication is vacuous. No attainment of the residual is needed. Joint correlations in K cannot invalidate the lower bound because it holds for every graph value. SC6 is global, so no output-neighborhood bootstrap is hidden in G4. The stronger inverse gauge of s↦sqrt(m²s²+c²s^{2γ}) is also available, but the simpler displayed ψ suffices.

## Explicit common physical-parent certificate

Assume

\[
\beta_*:=q(C/c)^{1/\gamma}<1.
\tag{SC7}
\]

Choose any κ with β_*<κ<1. Put M=cκ^γ and B=Cq^γ, so M>B. Choose any positive R satisfying

\[
R^{1-\gamma}\le\frac{\lambda(M^2-B^2)}M,
\tag{SC8}
\]

and define

\[
L_R=\sqrt{R^{2-2\gamma}+4\lambda^2 C^2q^{2\gamma}},
\quad a(t)=t,\quad\omega(\tau)=L_R\tau^\gamma,
\quad h(t,\tau)=\tau,\quad
K_R(t)=\frac{t+L_Rt^\gamma}{2}.
\tag{SC9}
\]

Take U=X, the complete allowed relation J, the global ψ in SC6, and any bar t≥K_R(R)/λ. These quantities have exactly the domains and monotonicity/continuity requirements of C249. Coverage G1 is SC3; G2 uses p=(0,β) and SC5; G3 is the identity-kernel equality ||y−x||=||v(y)−v(x)||; G4 is SC6 and the chosen residual evaluation window.

For 0<t≤R,

\[
\frac{\psi(K_R(t)/\lambda)}t
=\left(\frac{t^{1-\gamma}+L_R}{2\lambda c}\right)^{1/\gamma}
\le\left(\frac{R^{1-\gamma}+L_R}{2\lambda c}\right)^{1/\gamma}
\le\kappa.
\tag{SC10}
\]

The last inequality is exactly SC8 after squaring the positive inequality
R^{1−γ}+sqrt(R^{2−2γ}+4λ²B²)≤2λM. Thus G5 is verified with the same constants for the complete operator, all outputs and all admissible uncertainties. The length gauge is

\[
\Theta_R(t)=\frac{t}{2(1-\kappa)}+
\frac{L_Rt^\gamma}{2(1-\kappa^\gamma)}<\infty.
\tag{SC11}
\]

Since U=X, its complement distance is +∞ and the strict physical retention budget is automatic. C249 proves complete-fiber infinite continuation, retention in {d≤R}, finite physical length, convergence to S, d(x^k,S)≤κ^k d(x^0,S), and physical tail ≤Θ_R(κ^k d(x^0,S)). All zero-distance inputs are included by the exact absorption argument, not by an illicit strict inequality at zero.

## Sharper reflected envelope and optional radius improvement

Retaining the negative normal term gives the exact worst bound implied by the sector estimates:

\[
\omega_*(t)^2=t^2+
\max_{0\le s\le qt}\{4\lambda^2 C^2s^{2\gamma}-4\lambda m s^2\}.
\tag{SC12}
\]

It is nondecreasing because the t² term and the maximization domain both increase. Let

\[
s_*=\left(\frac{\gamma\lambda C^2}{m}\right)^{1/(2-2\gamma)},
\qquad D=1-4\lambda m q^2=
\left(\frac{1-\lambda m}{1+\lambda m}\right)^2\in[0,1).
\]

The maximand increases on [0,s_*] and decreases afterwards. If qR≤s_*, then

\[
\omega_*(t)^2=Dt^2+4\lambda^2C^2q^{2\gamma}t^{2\gamma},\quad0\le t\le R.
\]

Hence SC9 may replace L_R by sqrt(DR^{2−2γ}+4λ²B²), while SC8 may be enlarged to

\[
R^{1-\gamma}\le
\frac{2\lambda(M^2-B^2)}{
M+\sqrt{DM^2+(1-D)B^2}},
\qquad qR\le s_*.
\tag{SC13}
\]

This is the smaller positive root of the squared compatibility inequality; the rationalized expression remains well-conditioned near D=1. It improves the finite radius but does not change the critical asymptotic coefficient β_*.

## What is sharp and what is not

The normal damping margin m>0 is necessary for a uniform convergence theorem over the raw class. At μ=ε>0, choose scalar normal A(u)=μu and K(u,z)={(-μu,c|u|^γ)}. Then F(u,z)=(0,c|u|^γ), every full proximal output has u=α, z=β−λc|α|^γ, and every orbit with α≠0 drifts linearly along z. Global input coverage and zero-fiber absorption both hold, yet convergence fails.

In contrast, β_*<1 is only a sharp threshold for assembling this particular common direct G5 certificate from the worst upper/lower tangential bounds. It is not necessary for convergence. To see the certificate sharpness within the very same complete object, take scalar normal A(u)=μu and

\[
K(u,z)=\{(-\varepsilon u,b):b\in[c,C]|u|^\gamma\}.
\tag{SC14}
\]

The normal output is exactly u=qα, and the full uncertainty fiber has all tangent increments −λb. The true residual is sqrt(m²u²+c²|u|^{2γ}), while the maximal same-anchor reflection is sqrt(Dα²+4λ²C²q^{2γ}|α|^{2γ}). Thus every valid global/output-window EB gauge has asymptotic lower coefficient c^{-1/γ}, and every valid reflected gauge has asymptotic lower coefficient 2λCq^γ. For v=Id, a(t)≥t. Assembling K(t)=(a(t)+ω(a(t)))/2 therefore gives

\[
\liminf_{t\downarrow0}\frac{\psi(K(t)/\lambda)}t\ge\beta_*.
\]

If β_*≥1 no κ<1 can satisfy G5 on any positive radius for this full uncertainty example. If β_*<1 the explicit SC8 certificate works. This proves sharp common-gauge feasibility for the direct parent interface and distinguishes it from the algorithm's actual convergence.

Indeed, SC4 alone gives the stronger direct global all-output conclusion for every μ>ε, even if the lower forcing constant c is removed entirely. For all initial x^0 and all full choices,

\[
d(x^k,S)\le q^kd_0,
\qquad\|x^{k+1}-x^k\|
\le q^kd_0+\lambda Cq^{\gamma(k+1)}d_0^\gamma.
\tag{SC15}
\]

For the sharper normal step used here, the sector estimate gives ||α−u||²=t²−2⟨α,u⟩+||u||²≤t²−(1+2λm)||u||²≤t². This geometric sum is finite. It proves global finite length and convergence directly without RLEB or any energy. The structural certificate theorem's purpose is therefore a modular sufficient-condition verifier, not an assertion that the parent theorem is indispensable or that classical methods are excluded.

## Genuine feedback and uncertainty model

For a concrete subclass take A(u)=μu+∇φ(u)+Lu, where φ is differentiable convex with ∇φ(0)=0 and L is skew. Let Q(z) be any continuous matrix field with ||Q(z)||≤1, let v(z) be any continuous unit vector field in the tangent space, choose b_0>0 and 0<ρ<1, and set

\[
K(u,z)=\left\{\left(\varepsilon\theta Q(z)u,
b_0\|u\|^\gamma[e_1+\rho\theta v(z)]\right):\theta\in[-1,1]\right\}.
\tag{SC16}
\]

This is a continuous compact convex line segment of correlated normal and tangential uncertainty, with c=b_0(1−ρ) and C=b_0(1+ρ). The tangent state feeds into both channels; nonlinear Q and v leave the full coupled implicit equation unsolved. SC3 and the estimates nevertheless certify every root. Choosing Q=−I and v=e_1 gives a visibly genuine continuum of distinct outputs when ε>0 and the normal input is nonzero; Q and v can also vary with z to give genuinely state-dependent feedback.

A predetermined continuous state law θ_k(u,z)∈[-1,1] gives a singleton continuous K_k satisfying the same raw bounds, so each mode has its own global coverage and all its outputs lie in the original complete uncertainty relation. Arbitrary mode sequences share the common estimates. No coverage is claimed for discontinuous state laws merely because their pointwise values lie in the union.

This is an operator/control design class for robust normal regulation with a Hölder tangential command. It is not yet an identified external industrial system or a mapped published algorithm. No historical novelty or exclusion of all classical/KL/energy techniques follows from its proof.

## Optional exponent sharpness under an additional bounded normal slope

If A is single-valued near zero with ||A(u)||≤L_A||u||, then every sufficiently small normal input t and every full output satisfy

\[
\frac{t}{1+\lambda(L_A+\varepsilon)}\le\|u\|\le qt,
\qquad\|z-\beta\|\ge\lambda c\|u\|^\gamma.
\]

Thus the complete prox at each zero input has pointwise maximal Hölder exponent exactly γ: SC4 supplies the upper estimate, and the lower estimate excludes every η>γ. Similarly the true residual is bounded above by sqrt((L_A+ε)²s²+C²s^{2γ}) as well as below by SC6, so the true EB exponent 1/γ cannot be improved. To verify the latter sharpness on actual outputs, any state y with small s has a predecessor x=y+λf, f∈F(y), whose normal coordinate has norm at most [1+λ(L_A+ε)]s; hence it lies in the same input tube for small s. Without the additional bounded-slope hypothesis A may be much steeper than linear near zero, and these sharp exponent claims are not automatic.
