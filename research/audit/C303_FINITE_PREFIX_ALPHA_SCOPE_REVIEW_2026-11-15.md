# C303 finite-prefix scope audit for the W schedule

Date: 2026-11-15
Status: **continue validation**

This is an independent audit of the finite-prefix obligation needed to move the conditional W_k = exp(z_k^2) schedule from alpha > 2/3 to a fixed alpha in (1/2,1). It audits the threshold algebra and the initial-set quantifiers; it does not certify the full C303 bridge.

## Threshold and physical-time calculation

For h_k = h_0 (k+1)^(-alpha), the normal supersolution starts once

    h_k - h_{k+1} <= (gamma/4) h_k^2.

Since h_k-h_{k+1} is asymptotic to alpha h_0 (k+1)^(-alpha-1), this is reached when

    (k+1)^(1-alpha) >= 4 alpha/(gamma h_0)

up to a fixed small-h_0 constant. The corresponding physical time satisfies, for each fixed alpha < 1,

    t_{K_*} = sum_{j<K_*} h_j <= C_(alpha,gamma) < infinity

for all sufficiently small h_0. Thus the bound T_tr=t_{K_*} <= T_* is compatible with every fixed alpha in (1/2,1), provided the same threshold is used in the finite-prefix lemma and the tail recursion.

This calculation does not give a single T_* uniform as alpha approaches 1, and it does not control arbitrary unbounded lifted initial angles. The finite-prefix construction in c303_finite_prefix_margin.md is centered at one fixed compact interior subband around x_bar0; that bounded initial lift is part of its quantifier.

## Discrete prefix margin

The existing finite-prefix argument compares implicit Euler with the continuous second-order flow on the compact time interval [0,T_*]. Under the source-conditional continuous HJ invariance, a compact reference segment has a positive minimum distance from the radial and entrance faces. The implicit-Euler error is O(h_0), uniformly for initial data in a fixed small phase-space neighborhood, so choosing h_0 small preserves the finite prefix and all intermediate tau-paths.

The same proof uses no inequality special to alpha > 2/3 after the displayed threshold calculation. It therefore supplies a plausible conditional extension to fixed alpha > 1/2, but the repository statement still records only alpha > 2/3; the extension must be written into that lemma before it can be used as a theorem hypothesis.

## Quantifier issue that remains open

The prefix note imposes

    ||v_0 + grad f(x_0)|| < epsilon_0,
    0 < epsilon_0 <= c_init h_0^2.

For every fixed h_0 > 0 this is a nonempty open phase-space set. It is not one fixed open set uniform over all h_0 down to zero, because the normal thickness shrinks like h_0^2. Therefore the phrase "one common initial open set" in the W interface must mean one set for each fixed schedule parameter h_0, with constants uniform over that set. A stronger claim of a single h_0-independent open set is not supported by the current proof.

The transient estimate also needs the finite-prefix time bound T_tr <= T_* to be uniform over that same fixed-alpha family. If T_tr were allowed to grow with h_0^{-1} or with the lifted initial angle, the factor Q_0 (1+T_tr)^(1+epsilon) could destroy the O(h_0^2) absorption.

## Verdict

For each fixed alpha in (1/2,1), a bounded initial subband, and a common finite-prefix threshold satisfying T_tr <= T_*, no finite-prefix counterexample appears in the current argument. The exact remaining obligations are:

1. rewrite c303_finite_prefix_margin.md with the fixed-alpha > 1/2 quantifier;
2. state whether the theorem uses an h_0-dependent open set or prove a stronger uniform-set claim;
3. propagate the same K_*, T_*, and source/lift conditions into the W interface.

The independent verdict is **continue validation**. The W candidate remains a conditional schedule improvement and does not meet the major-contribution or four-star standard.
