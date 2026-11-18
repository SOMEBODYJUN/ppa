# Critical q=2, alpha=1: a positive theorem under a reach hypothesis

<a id="critical-q2-reach"></a>

This note isolates a proved subcase of the remaining C328 gate. It does not settle arbitrary closed zero sets.

Let `S` be a `C^{1,1}` embedded submanifold in a tubular neighborhood with reach at least `rho`. Let `x_k -> y_k=x_{k+1}` be a complete PPA orbit, with

`x_k = y_k + lambda v_k`, `v_k in F(y_k)`, `s_k=lambda ||v_k||`,
` t_k=d(x_k,S)`, `u_k=d(y_k,S)`.

Assume the all-pair value-weighted curvature inequality

`<v-w,y-z> >= -C (||v||+||w||)||y-z||^2`

for all local graph pairs, the complete residual bound

`d(y,S)^2 <= K_EB r_F(y)`,

and a strict square descent estimate

`t_k^2-u_k^2 >= c s_k^2`, `c>0`.

The strict descent is an explicit hypothesis in this note. It follows from the
curvature inequality and the residual bound under an additional common-anchor
or anchor-transport estimate, which controls `||y-P_S(x)||` by a multiple of
`d(y,S)`. Without that estimate, the curvature loss is evaluated at
`||y-P_S(x)||^2`, while the residual bound controls only `d(y,S)^2`.
Assume all roots and anchors remain in a sufficiently small common tube, with a uniform graph-value cap `||v_k|| <= v_bar`; the cap is chosen so the reach-error absorption factors stay positive.

## Tangential graph-value estimate

For `y` write `p=P_S(y)`, `n=y-p`, and split `v=a+b` into the normal and tangent spaces at `p`. The reach estimate gives, for a geodesic point `p_tau` in direction `xi=b/||b||`,

`p_tau-p=tau xi+e_tau`, `||e_tau|| <= tau^2/(2 rho)`.

Use the graph inequality with `(p_tau,0)`. Since
`A=<v,n> <= ||v|| u`,
`|<v,e_tau>| <= ||v|| tau^2/(2 rho)`, and
`||y-p_tau|| <= u+tau+tau^2/(2 rho)`, one obtains

`tau ||b|| <= ||v|| [u + c_0 tau^2]`

for a uniform `c_0` after shrinking the tube. Choose `tau=sqrt(u)` to get

`||b|| <= c_1 ||v|| sqrt(u)`.   (1)

This is the exact place where positive reach and a tangent chart are used.

## Projection displacement estimate

Let `p_k=P_S(x_k)`, `p_{k+1}=P_S(x_{k+1})`, and `h_k=p_k-p_{k+1}`. Write

`x_k=p_k+n_k`, `x_{k+1}=p_{k+1}+n_{k+1}`.

The reach inequalities imply

`|<n_k,h_k>| <= t_k ||h_k||^2/(2 rho)`,
`|<n_{k+1},h_k>| <= u_k ||h_k||^2/(2 rho)`.

The chord has normal component relative to `T_{p_{k+1}}S` bounded by
`O(||h_k||^2/rho)`. Since
`lambda v_k=h_k+n_k-n_{k+1}`, (1) and absorption in a sufficiently small graph-value/tube window give

`||h_k|| <= c_2 lambda ||b_k|| <= c_3 s_k sqrt(u_k)`.   (2)

## Dyadic summability

Set `a_k=u_k^2`. The strict descent gives
`Delta_k=t_k^2-u_k^2 >= c s_k^2`, while the EB gives
`a_k <= D s_k`, `D=K_EB/lambda`.

On the block `2^{-(j+1)} < a_k <= 2^{-j}`, each step satisfies
`s_k >= 2^{-(j+1)}/D` and hence
`Delta_k >= c 2^{-2j-2}/D^2`.  The sequence `a_k` is nonincreasing,
but one entering step can jump across arbitrarily many dyadic bands.  We
therefore split the block into interior steps, whose predecessor is in the
same band, and at most one entering step.  The interior steps consume a total
drop at most `2^{-j}`, so their number is bounded by
`N_j <= 4D^2 c^{-1}2^j` and
`sum_interior s_k^2 <= c^{-1}2^{-j}`.  Cauchy--Schwarz then gives
`sum_interior s_k <= c_4`, with `c_4` independent of `j`.

For the entering step, use the value cap `s_k <= lambda v_bar` and
`sqrt(u_k)=a_k^{1/4} <= 2^{-j/4}`.  The projection estimate (2) gives
`||h_k|| <= c_3 lambda v_bar 2^{-j/4}`.  For the interior steps, (2) and
`sqrt(u_k) <= 2^{-j/4}` give the same dyadic factor.  Consequently

`sum_{k in block} ||h_k|| <= c_5 2^{-j/4}`.

The dyadic series converges. Thus `(p_k)` is Cauchy. Since `||x_k-p_k||=t_k ->0`, the full PPA orbit converges to one point of `S`.

The result proves point convergence but does not supply finite length of the physical orbit. It only controls projection displacement. An additional estimate converting `||x_k-x_{k+1}||` to a summable quantity is required for finite length.

## Scope boundary

The proof uses two geometric facts unavailable for an arbitrary closed `S`: a tangent chart to create `p_tau` and a reach inequality to control projection displacement. The critical C328 hypotheses alone give square summability of `s_k`, but do not provide either fact. The general nonisolated closed-set point-convergence question therefore remains open. The existing rotation-platform counterexample does not satisfy the strict small-constant gate because its radial correction cancels the entire square descent.
