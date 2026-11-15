# C303: exact endpoint identity and a direct first-contact barrier

状态：**continue validation / partial replacement lemma**。本页给出一个不使用

y(τ) 导数误差 `CS5` 或角度 Taylor 估计 `TE2` 的端点障碍。它仍需要

normal-error bound `q_k=||w_k||` and therefore does not close the whole bridge by

itself. The exact identity also gives a local obstruction: an arbitrary

`O(h_k)` normal defect can point outward, so no first-contact theorem can be

independent of `q_k`.

## Exact conditional claim

Let `g=∇f`, `H=∇²f`, `F=ag-Hg`, and `Y=-g` on a set where `f∈C³`,

`||H||≤L_H`, `D H` is bounded by `L_3`, and

`I-βH(y)` is uniformly invertible. For `h>0` put

    β=h/(1+ah),       λ=hβ.

Given `(x,v)` and a resolvent endpoint `y` satisfying

    y+λF(y)=x+βv,

set

    d=y-x,       w=v+g(x),
    R(x,y)=g(y)-g(x)-H(y)d,
    A_y=(I-βH(y))^{-1}.

Then the endpoint has the exact identities

    d = hY(y) + β A_y [ w+R(x,y) ],                 (EP1)

    w^+ := d/h+g(y)
       = (1/(1+ah)) A_y [ w+R(x,y) ].              (EP2)

If `||d||≤D h`, then

    ||R(x,y)|| ≤ (L_3 D²/2) h².                    (EP3)

Thus (EP2) is an alternative derivation of the normal recursion, while

(EP1) is a direct inward-field formula for the endpoint displacement.

## Proof of the identity

The resolvent equation gives

    d=β(v-hF(y)),

and define the secant defect

    w_bar=β^{-1}d-Y(y)=v-hF(y)+g(y).

Using `v=w-g(x)`, `F=ag-Hg`, and

    g(y)-g(x)=H(y)d+R(x,y),

one obtains

    w_bar=w+R+H(y)(d+h g(y))-ha g(y).

Since `d=β(-g(y)+w_bar)` and `h-β=ahβ`,

    (I-βH(y))(w_bar+ha g(y))=w+R.

Therefore `w_bar=ahY(y)+A_y(w+R)`, and

    d=β(Y(y)+w_bar)=hY(y)+βA_y(w+R),

which is (EP1). Dividing by `h` and adding `g(y)=-Y(y)` gives (EP2).

## Direct boundary barrier

Let a `C²` face `s` define the admissible side by `s>0`. Assume that at every

contact point in a compact tail patch

    ∇s(y)·Y(y) ≥ μ(y)>0,

and that the face has a uniform Hessian bound. If `q=||w||`, (EP1)--(EP3) and

a Taylor expansion at a boundary endpoint `s(y)=0` give

    s(x)
      = -h ∇s(y)·Y(y) + O(h²+h q)
      ≤ -h[ μ(y)-C(q+h) ].                              (EP4)

Consequently, whenever `q+h ≤ μ(y)/(2C)`, no endpoint on that face can have a
preimage `x` with `s(x)>0`. Applying the same identity to the scaled homotopy

    h_τ=τh,  β_τ=h_τ/(1+a h_τ),
    y_τ+ h_τβ_τF(y_τ)=x+β_τv,

at the first contact `τ_*>0` gives the same contradiction. The only estimates
needed for the homotopy are the endpoint identity and the bootstrap
`||y_τ-x||≤D h_τ`; the latter is itself a short consequence of (EP1). If
`u_τ=||y_τ-x||`, bounded `Y` and `A_y` give

    u_τ <= G h_τ + M h_τ(q + C_R u_τ²).

For `h_0` small, continuity from `u_0=0` and a first-exit argument imply
`u_τ≤D h_τ` uniformly; then `R_τ=O(h_τ²)` follows from (EP3). Thus no
 derivative estimate for `y_τ` or `w_tilde_τ` is used.

For C303, (EP4) applies to a radial face with `μ=m(θ)` and to the entrance
angle face with `μ=c φ(θ)`, `φ(θ)=θe^{-θ²}`. It replaces the derivative-based
`CS5`/`TE2` calculation by a direct endpoint first-contact argument, but still
requires

    q_k+h_k=o(m(θ_k)),       q_k+h_k=o(φ(θ_k)).          (EP5)

The normal recursion `q_k=O(h_k)` and the sharp schedule bootstrap therefore
remain necessary. No new source or outer-strip assumption is hidden in (EP4):
all constants are taken on the same compact pre-contact patch as the resolvent
coverage.

## Deriving the angular increment from the endpoint

The same calculation derives the two-sided angular recurrence instead of taking
`TE2` as an independent path estimate. Let `Theta` be the local lifted polar
angle on a patch with `r>=1/2`, and assume the HJ field bound

    c phi(theta) <= ∇Theta(y)·Y(y) <= C phi(theta),
    phi(s)=s exp(-s²),

on that patch. Taylor expansion of `Theta` at `y`, using (EP1), gives

    Theta(y)-Theta(x)
      = h ∇Theta(y)·Y(y)
        + β ∇Theta(y)·A_y[w+R(x,y)] + O(h²)
      = h ∇Theta(y)·Y(y) + O(h q+h²).                    (EP7)

The endpoint displacement bound gives `|Theta(y)-Theta(x)|<=C h`; since
`phi'` is bounded on `[1,infinity)`, replacing `phi(Theta(y))` by
`phi(Theta(x))` costs `O(h)` inside the leading `h` factor. Thus

    c h phi(Theta(x)) - C h q - C h²
      <= Theta(y)-Theta(x)
      <= C h phi(Theta(x)) + C h q + C h².                (EP8)

This is the required `TE2` form, derived from the endpoint equation and the
local HJ field bounds. It does not use `dot y_tau`, `w_tilde_tau`, or a
separate secant-velocity assumption. The `q` term remains exactly the one in
(EP4), so the normal recursion and schedule gate are not bypassed.

## The obstruction to removing the normal defect

The `q_k` term in (EP4) is not a proof artifact. Consider the flat local face

    s(z)=z_2,

with admissible side `z_2>0`, and the smooth potential

    f(z)=-μ z_2,

so `g=-μe_2`, `H=0`, `Y=μe_2`, and `F=ag=-aμe_2`. Take

    x=δe_2,       v=(μ-q)e_2,       w=-q e_2.

The exact resolvent endpoint is

    y_2=δ+hμ-βq.                                      (EP6)

If `q>μ(1+ah)` and `δ=(βq-hμ)/2>0`, then `x` is strictly inside while

    y_2=-(βq-hμ)/2<0.

Hence an `O(h)` defect whose outward component is comparable with the face
margin can force a one-step exit even though the endpoint identity is exact and
`H=0`. In the C303 tail the angular margin is `μ=cφ(θ)→0`; a generic
`q_k=O(h_k)` can therefore not be discarded. At the critical schedule
`α=1/2`, the unperturbed angle scale gives `h_k/φ(θ_k)≈√log k`, so (EP6)
explains why the endpoint identity alone cannot close that case.

## Why a convex variational shortcut is unavailable

The hypothesis `a>sup lambda_max(H)` does not imply convexity of
`chi_a=af-(1/2)||∇f||²`, because

    chi_a'' = a f'' - (f'')² - f' f'''

in one dimension. For

    f(x)=A x + epsilon sin(x),    A>epsilon>0,

we have `sup f''=epsilon`; choose any `a>epsilon`. At `x=pi`,
`f'=A-epsilon`, `f''=0`, and `f'''=epsilon`, hence

    chi_a''(pi)=-(A-epsilon)epsilon<0.

Therefore the C303 resolvent equation is not generally the optimality
condition of a convex proximal subproblem, and firm-nonexpansive or variational
inequalities cannot replace the endpoint/normal estimates without an additional
hypothesis controlling `f' f'''` (or directly assuming convexity of `chi_a`).
A smooth cutoff can localize this example: keep the displayed jet near
`x=pi`, enlarge `a` beyond the cutoff's global Hessian bound, and the negative
value of `chi_a''(pi)` is unchanged.

## Verdict and reusable content

**Continue validation.** (EP1)--(EP4) are a reusable algebraic lemma that can
replace the derivative-defined `CS5` and the one-step `TE2` estimate in a C303
proof, provided global coverage, a compact pre-contact patch, and the existing
normal bound are available. The local flat-face construction (EP6) is a precise
obstruction to any stronger claim that removes the `q_k` term or the scale gate.
It does not refute C303's conditional bridge; it identifies the minimum missing
quantity as a directional normal-error estimate, not a new variational
principle.
