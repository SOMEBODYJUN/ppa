# HJ second-order open-basin candidate: final independent review

## Exact status

The current `second_order_open_basin_proof_v1.md` fixes the previously dangerous issues: (1<\mu<e^{2\pi}) gives an embedded unwrapped tube; the cutoff is required to be disjoint from the whole tail tube; the initial angle is a finite band; (u=\vartheta-W) is formed before the angular bootstrap; and the perturbation size is chosen only after the polynomial lower bound for the shrinking boundary margin.

The mathematical verdict is **continue validation**, not major-contribution status.

## Formula and sign check

The displayed HJ formula is the negative gradient (Y=-\nabla f), even where the article text calls the vector (X=\nabla f). In the cutoff-free tube,
[
q=\frac{2r-\gamma_1-\gamma_2}{\Delta},\quad
\Delta=(\mu-1)e^{-\vartheta},\quad h=e^{-\vartheta^2},
]
so
[
q_\vartheta=q+\frac{1+\mu}{\mu-1}=O(1),
\qquad
Y_\vartheta=\frac{h}{r}\bigl(2\vartheta F(q)-F'(q)q_\vartheta\bigr).
]
The HJ tube has (q\in[-\beta,\beta]Subset(-1,1)), (F_*>0) on that interval, and (|F'\|<\infty). Increasing (\vartheta_*) therefore gives constants (0<c_0<C_0) with
[
c_0\vartheta h\le Y_\vartheta\le C_0\vartheta h.
]
At (b_1) ((q=-\beta)), (F'(-\beta)<0) and (Y_r=+2h|F'(-\beta)|/\Delta); at (b_2) ((q=+\beta)), (F'(\beta)>0) and (Y_r=-2hF'(\beta)/\Delta). Since (b_i'=O(e^{-\vartheta})), tangential normal-correction terms are (O(\vartheta h e^{-\vartheta})), whereas the radial terms are (\asymp h/\Delta=e^{-\vartheta^2+\vartheta}). Thus the inward normal drifts are uniformly bounded below by (m_0e^{-\vartheta^2+\vartheta}).

The derivative orders are
[
f_{rr}=O(he^{2\vartheta}),\quad f_{r\vartheta}=O(\vartheta he^{\vartheta}),\quad f_{\vartheta\vartheta}=O(\vartheta^2h).
]
All tend to zero as (\vartheta\to\infty), and HJ's global (C^\infty) extension makes the Cartesian Hessian bounded on the compact physical closure of the tail tube. Hence (K=\sup\lambda_{\max}(\nabla^2f)<\infty).

## Bootstrap check

For (chi_a=af-rac12|\nabla f|^2), (w=v+\nabla f(x)) gives
[
x'=Y+w,\qquad w'=(\nabla^2f-aI)w,
]
and (|w(t)|\le e^{-\delta t}|w_0|), (delta=a-K>0), until the first exit.

Take (D_0) in a finite angular band and (|w_0|<\varepsilon). With (W=C\int_0^t|w(s)|ds), one first gets (\vartheta\ge\Theta_0-C\varepsilon/\delta>1). Since (u=\vartheta-W) and (s\mapsto se^{-s^2}) decreases for (s\ge1), (u'\le C_0ue^{-u^2}). Therefore (\vartheta^2\le C+p\log(1+t)) on the first-exit interval. Consequently
[
e^{-\vartheta^2+\vartheta}\ge c(1+t)^{-p}.
]
Choosing (arepsilon) after this estimate so that (Ce^{-\delta t}\varepsilon) is at most half the boundary margin gives (s_i'(\tau)>0) at any putative first boundary contact, a contradiction. The same polynomial comparison makes the angular error smaller than half (c_0\vartheta e^{-\vartheta^2}), so (\vartheta'>0); bounded (\vartheta) would then contradict a positive lower drift, hence (\vartheta\to\infty). The tube bounds imply (r\to1), and the unwrapped angle crosses every phase infinitely often, so (\omega(x)=S^1). Bounded (x,v) and global smoothness give continuation.

## Truth / value / novelty / ambition

* **Truth:** very likely correct once the HJ estimate lemma is written with explicit constants and the cutoff is shown to vanish on the entire tail tube. No remaining sign or first-exit quantifier defect was found.
* **Value:** high for finite-dimensional damped gradient dynamics: it would produce an open phase-space basin of nonconvergence with (omega=S^1), exactly the gap identified by HJ.
* **Novelty:** HJ's Remark 3 explicitly says the open phase-space basin problem was open. Searches found no later direct resolution; this is provisional priority evidence, not a completed survey.
* **Ambition:** it is an ODE result, not a PPA/GPPA discrete theorem. Without a precise discretization/GPPA bridge, it cannot be the requested PPA/GPPA major contribution.

## Minimum obligation changing the verdict

Write and independently audit one formal HJ lemma deriving the angular and boundary constants from the exact (F)-formula, prove the support choice gives (Pi=0) on the whole tail tube, and state the embedded-lift condition. After that, the ODE candidate is mathematically mature; a separate PPA/GPPA bridge is required before upgrading its status for this project.
