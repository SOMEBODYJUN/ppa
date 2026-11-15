# C303 finite-prefix extension for the W schedule

Date: 2026-11-15  
Status: **continue validation / source-conditional**

This audit checks whether the finite-prefix construction in
`research/c303_finite_prefix_margin.md` supplies the time and margin gate needed
by the W schedule for a fixed `alpha` in `(1/2,1)`. It does not certify the HJ
source, the global continuous tail invariance, or the discrete first-contact
barrier.

## Exact finite-prefix obligation

Take `h_k=h_0(k+1)^(-alpha)` and let `K_*` be the first index after which

    h_k-h_{k+1} <= (gamma/4) h_k^2

holds for every later index. Since

    (h_k-h_{k+1})/h_k^2 = (alpha/h_0)(k+1)^(alpha-1)(1+o(1)),

for every fixed `alpha<1` one may choose `K_*` with

    K_*^(1-alpha) >= 4 alpha/(gamma h_0)

up to a fixed finite-step factor. Summing the steps gives

    T_tr=t_{K_*} <= C_alpha,gamma + 1,

and the existing proof records the explicit choice

    T_* = 8 alpha/(gamma(1-alpha)) + 1.

Thus the time horizon is independent of `h_0` after `alpha` is fixed. The W
schedule only needs `alpha>1/2`, so its finite-prefix range is covered.

## Common initial set and what is uniform

The finite-prefix lemma starts from one compact interior subband around a fixed
reference point `x_bar0` and uses the continuous HJ trajectory on `[0,T_*]`.
Strict inward margin on this compact curve plus ODE continuous dependence gives a
single phase-space neighborhood for all initial states in that subband, provided

    ||v_0-Y(x_0)|| < epsilon_0,
    epsilon_0 <= c_init h_0^2.

The spatial subband and the margin constants can be chosen uniformly for the
fixed `alpha` and all sufficiently small `h_0`; the velocity radius itself is
allowed to shrink with `h_0`. This is the correct quantifier for a fixed-step
family. It does not claim one positive velocity radius for every `h_0` tending
to zero, nor uniformity over an unbounded set of initial lifted angles.

The intermediate `tau`-resolvent paths inherit the same margin from the
implicit-Euler error `O(h_0)` and the local displacement `O(h_k)`, once the
source-conditional global resolvent gate is available. Therefore the finite
prefix does not create a new circularity or a new alpha>2/3 restriction.

## Remaining obstruction

The argument is conditional on the continuous HJ reference trajectory staying
inside the lifted tail with a strict margin and on the global C-infinity/source
extension needed for the resolvent constants. It also leaves the later normal
recursion, W super-solution, outer-strip transfer, and common first-contact
argument untouched. Those obligations remain the reason for the overall verdict
**continue validation**.
