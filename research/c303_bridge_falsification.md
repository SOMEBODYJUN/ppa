# C303 bridge: V11 and first-exit audit

状态：**candidate / continue validation**。本页只审查二阶 HJ 尾管的局部 Lipschitz 估计和离散首次越界量词；不把它升级为离散 PPA 定理。

## 1. Notation and the two different h's

The HJ profile is (H(\theta)=e^{-\theta^2}), while the discrete PPA step is (h_k=h_0(k+1)^{-\alpha}). Writing both as (h) hides the comparison in V11, so below (H) denotes the angular profile.

On the cutoff-free tube, with

\[
 q=\frac{2r-\gamma_1(\theta)-\gamma_2(\theta)}{\Delta(\theta)},
 \quad q_r=\frac2\Delta=O(e^\theta),
 \quad q_\theta=q+c_\mu=O(1),
\]

the field (Y=-\nabla f), (f=HF(q)), has orthonormal polar components

\[
 Y_r=-HF'(q)q_r=O(He^\theta),
 \qquad
 Y_\theta=\frac H r\bigl(2\theta F(q)-F'(q)q_\theta\bigr)=O(\theta H).
\]

For (s_1=r-b_1(\theta)), (s_2=b_2(\theta)-r), set (B_i=\nabla s_i\cdot Y). The boundary computation gives

\[
 B_i\big|_{s_i=0}\ge m(\theta):=m_0He^\theta. 
\tag{V11.1}
\]

## 2. Derivative/Lipschitz orders

The potentially largest derivative is radial:

\[
 \partial_rY_r=-H F''(q)q_r^2=O(He^{2\theta}).
\tag{V11.2}
\]

The remaining terms satisfy

\[
 \partial_rY_\theta=O(\theta He^\theta),
 \qquad
 r^{-1}\partial_\theta Y_r=O(\theta He^\theta),
 \qquad
 r^{-1}\partial_\theta Y_\theta=O((1+\theta^2)H),
\]

and differentiating (b_i'/r) contributes only (O(He^\theta)+O(\theta He^{-\theta})). Hence on a normalized-width strip (|q|le\beta+\eta), (	heta\ge\theta_0), (r\in[1/2,3/2]),

\[
 \operatorname{Lip}_x B_i\le L_b(\theta)
 \le C\bigl(He^{2\theta}+\theta He^\theta+(1+\theta^2)H\bigr).
\tag{V11.3}
\]

For (	heta\ge\max\{\theta_0,2\}), this is (L_b(\theta)=O(He^{2\theta})). This does **not** invalidate V11: (He^{2\theta}=e^{-\theta^2+2\theta}=e\,e^{-(\theta-1)^2}) has a finite supremum on every tail and decreases once (	heta_0>1). Thus a uniform (L_b<\infty) exists if the strip is the normalized tube on which (F,F',F'') are uniformly bounded. If “fixed width” means a physical radial width independent of (	heta), then (|q|) grows like (e^\theta) and the compact-(q) argument is unavailable; V11 must then be restated on a normalized-width strip or supplied with global bounds on (F'').

## 3. The variable bound repairs the local crossing estimate

At a first discrete exit through (s_i=0), write (\bar x_k) for a same-(	heta) boundary point. The endpoint displacement estimate (|x_{k+1}-x_k|\le Ch_k) implies (|x_k-\bar x_k|\le Ch_k). Taylor expansion of (s_i), with (B_i=\nabla s_i\cdot Y), gives

\[
 s_i(x_{k+1})-s_i(x_k)
 \ge h_k\left[m(\theta_k)-C h_k L_b(\theta_k)\right]
       -C h_k\|w_k\|-C h_k^2 .
\tag{V11.4}
\]

The ratio of the new Lipschitz error to the boundary margin is

\[
 \frac{h_kL_b(\theta_k)}{m(\theta_k)}=O(h_ke^{\theta_k}).
\tag{V11.5}
\]

Therefore a bootstrap hypothesis (	heta_k^2\le C_0+C_1\log(1+t_k)) gives (e^{\theta_k}=\exp O(\sqrt{\log(1+t_k)})=t_k^{o(1)}), and hence (h_ke^{\theta_k}\to0) for every (alpha>0), in particular for the proposed (alpha>2/3). Under this conditional upper bound and (w_k=O(h_k)), (V11.4) is positive for all sufficiently large (k). A finite prefix can be handled by an inner initial subband and a smaller initial (w_0)-ball.

This repairs the local Lipschitz step only. The angular upper bound and endpoint displacement must be established before invoking (V11.5), and the normalized strip/cutoff must contain the whole one-step segment.

## 4. Fatal issue that V11 does not repair: D6 has the wrong first-exit sign

If (k) is the first discrete exit and (x_k\in D), (x_{k+1}\notin D), then (s_i(x_k)>0) and (s_i(x_{k+1})\le0), hence (s_i(x_{k+1})-s_i(x_k)<0). The displayed C303 inequality

\[
 s_i(x_{k+1})-s_i(x_k)
 \ge h_km(\theta_k)-C h_k\|w_k\|-C h_k^2
\tag{D6}
\]

cannot be applied directly at this first exit: if its right side is positive, it contradicts the assumed exit rather than proving that the endpoint stays in the domain, and its derivation uses the inward boundary field at a point not yet known to lie on the boundary or in a tube where the formula is valid. V11's variable Lipschitz bound only controls (B_i(x_k)-B_i(\bar x_k)) after a separate (O(h_k)) endpoint/near-boundary lemma.

A sound repair needs an explicit buffer, for example an inner domain (D^-\Subset D) and an outer tail strip (D^+\supset D), together with:

1. a uniform displacement/inclusion lemma (G_{h_k}^{-1}(D^-)\subset D^+) for the implicit step (or an equivalent bound showing the whole segment (x_k\to x_{k+1}) remains in (D^+));
2. the lower bound (B_i\ge m(\theta)) on the relevant boundary of (D^+);
3. the variable-Lipschitz estimate (V11.3) and (h_ke^{\theta_k}\to0);
4. a finite-prefix argument for the chosen open initial set.

Without this buffered endpoint statement, D6 is a proof gap, independently of whether (L_b) is called uniform or variable.

## Verdict

**V11 is not a fatal obstruction.** On the actual HJ tail (H=e^{-\theta^2}), (He^{2\theta}) is bounded and decays for large (	heta); a variable (L_b(\theta)) yields the exact smallness ratio (h_ke^{\theta_k}\to0) once the angular bootstrap is non-circular. The candidate remains **continue validation**, because D6's first-exit quantifier/sign and the required buffered implicit-step inclusion are still unproved. If the intended “fixed-width strip” is physical radial width (so (|q|) is unbounded), V11 requires a new global (F'') estimate; absent such an estimate that version of V11 is unsubstantiated, but this is a local formulation failure rather than a counterexample to the HJ mechanism.

