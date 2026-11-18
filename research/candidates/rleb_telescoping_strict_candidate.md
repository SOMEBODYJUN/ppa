# Candidate: replacing the Dini budget by a telescoping displacement potential

## Status

candidate. This is the result of the supervised Astra Ultra round. The construction gives a full-graph strict-separation example after the definitions below are fixed. External novelty and a publication-level comparison remain open.

## The comparison target

Fix a finite-dimensional Euclidean space, a closed target \(S\subset\operatorname{zer}F\), a step \(\lambda>0\), an input window \(U_R\), and the complete resolvent relation. Retain the original nonlinear RL anchor condition, input coverage, and the true-residual error bound.

The old RLEB package also requires a nondecreasing RL modulus \(\omega\) with
\[
\int_0^R\frac{\omega(t)}t\,dt<\infty,
\]
and uses
\[
B_\omega(t)=\frac{t+\omega(t)}2,
\qquad
\Theta_\omega(t)=\sum_{j\ge0}B_\omega(\kappa^jt).
\]
The direct compatibility condition is
\[
\psi(B_\omega(t)/\lambda)\le \kappa t.
\]

The candidate package \(M_{\mathrm{tel}}\) keeps the nonlinear RL and true-residual ingredients, replaces the global Dini requirement by two directly checkable conditions, and does not define them as A+B.

There is a nondecreasing residual envelope \(\bar r\) and a nondecreasing potential \(W\), with \(\bar r(0)=W(0)=0\), such that every complete step \(x\mapsto y\) satisfies
\[
r_F(y)\le \bar r(d(x,S)),
\qquad
\psi(\bar r(t))\le \kappa t,
\tag{M1}
\]
and
\[
\|x-y\|\le W(d(x,S))-W(d(y,S)).
\tag{M2}
\]
The same complete-input coverage, RL anchor, residual window, and strict initial budget are retained. M2 is a pathwise energy-payment condition. Summing it gives finite physical length, while M1 gives A through the true-residual error bound. It also gives the physical displacement bound \(\|x-y\|\le W(d(x,S))\).

## Why old RLEB implies the candidate

Under old RLEB, the one-step RL estimate gives
\[
\|x-y\|\le B_\omega(d(x,S)),
\qquad
r_F(y)\le B_\omega(d(x,S))/\lambda.
\]
The old direct compatibility gives M1 with
\[
\bar r(t)=B_\omega(t)/\lambda.
\]
The old distance recursion gives \(d(y,S)\le\kappa d(x,S)\). Set \(W=\Theta_\omega\). Since
\[
\Theta_\omega(t)-\Theta_\omega(\kappa t)=B_\omega(t)
\]
and \(W\) is nondecreasing,
\[
W(d(x,S))-W(d(y,S))
\ge W(d(x,S))-W(\kappa d(x,S))
 =B_\omega(d(x,S))
\ge\|x-y\|.
\]
Thus old RLEB implies \(M_{\mathrm{tel}}\). Under M1, the true-residual error bound gives
\[
d(y,S)\le\psi(r_F(y))\le\psi(\bar r(d(x,S)))\le\kappa d(x,S).
\]
Summing M2 over a finite prefix gives
\[
\sum_{j=0}^{N-1}\|x^{j+1}-x^j\|
\le W(d(x^0,S))-W(d(x^N,S))
\le W(d(x^0,S)).
\]
The strict initial budget and coverage then give the usual local extension and convergence argument.

## Strict full-graph construction

Choose \(0<\alpha<1\), \(p>1/\alpha\), and \(t_n=2^{-n}\). Let
\[
A_n=t_n^\alpha,
\qquad
\delta_n=t_n^{p+1}\exp(-1/A_n).
\]
Choose a triangular bump \(\beta\) supported in \([-1,1]\), with \(0\le\beta\le1\) and \(\beta(0)=1\), and define on a sufficiently small positive window
\[
h(t)=\sum_{n\ge n_0}A_n\beta\!\left(\frac{t-t_n}{\delta_n}\right),
\qquad h(t)=0\quad(t\le0).
\]
The supports are disjoint. Extend \(h\) continuously outside the window with a bounded modulus. On the window,
\[
|h(t)|\le C_h|t|^\alpha.
\]

Let
\[
\phi(t)=\operatorname{sgn}(t)\frac{|t|^p}{1+|t|^{p-1}}.
\]
Then \(\phi\) is a strictly increasing homeomorphism, \(|\phi(t)|<|t|\) for \(t\ne0\), and \(|\phi(t)|\asymp |t|^p\) near zero. Define
\[
J(u,t)=(u+h(t),\phi(t)),
\qquad
F=J^{-1}-\operatorname{Id}.
\]
The full resolvent is exactly \(J_F=J\), it is globally single-valued and onto, and
\[
S=\mathbb R\times\{0\}=\operatorname{zer}F.
\]

For \(x=(u,t)\), write \(y=Jx\). Then
\[
d(x,S)=|t|,
\qquad d(y,S)=|\phi(t)|\le |t|^p,
\]
and
\[
\|x-y\|^2=h(t)^2+(t-\phi(t))^2
\le C_s^2|t|^{2\alpha}
\]
after shrinking the window. Hence the candidate residual envelope can be taken as
\[
\bar r(t)=C_s t^\alpha.
\]
The exact inverse formula gives, for \(y=(a,b)\) and \(t=\phi^{-1}(b)\),
\[
F(y)=(-h(t),t-\phi(t)),
\qquad
r_F(y)=\|F(y)\|.
\]
Since \(|t-\phi(t)|\ge(1-R^{p-1})|t|\) on the window,
\[
d(y,S)=|\phi(t)|\le |t|^p
\le (1-R^{p-1})^{-p}r_F(y)^p.
\]
Thus M1 holds with
\[
\psi(s)=(1-R^{p-1})^{-p}s^p.
\]
Because \(\alpha p>1\), shrinking \(R\) gives
\[
\psi(\bar r(t))\le\kappa t
\]
for some \(\kappa<1\). This is the distance contraction A.

For M2 choose
\[
W(t)=C_Wt^\alpha+t,
\qquad
C_W\ge\frac{C_s}{1-R^{\alpha(p-1)}}.
\]
Since \(d(y,S)\le R^{p-1}d(x,S)\),
\[
W(d(x,S))-W(d(y,S))\ge C_s d(x,S)^\alpha\ge\|x-y\|.
\]
Therefore M2 holds and the physical length is finite.

## Why the old RLEB package fails

The reflected resolvent is
\[
2J(u,t)-(u,t)=(u+2h(t),\,2\phi(t)-t).
\]
Let \(\eta_h\) be the least nondecreasing modulus of \(h\). The center and an edge of the \(n\)-th bump are separated by \(\delta_n\) and have height difference \(A_n\). Hence any full-graph RL modulus \(\widetilde\omega\) satisfies
\[
\widetilde\omega(\delta_n)\ge cA_n.
\]
Since
\[
\log\frac{\delta_{n-1}}{\delta_n}
\ge \frac{1-2^{-\alpha}}{A_n}+O(1),
\]
the disjoint intervals \([\delta_n,\delta_{n-1}]\) give
\[
\int_0^R\frac{\widetilde\omega(t)}t\,dt
\ge c\sum_n A_n\log\frac{\delta_{n-1}}{\delta_n}=+\infty.
\]
Thus no alternative full-graph RL modulus can satisfy the old Dini requirement. The strict separation is caused by narrow cross-input oscillations, while the actual PPA steps are controlled by the height envelope \(C_st^\alpha\) and the superlinear normal contraction \(t\mapsto t^p\).

## Current status

The implication \(H_{\mathrm{RLEB}}\Rightarrow M_{\mathrm{tel}}\Rightarrow(A)+B_{\mathrm{phys}}\) is algebraically closed under the stated common quantifiers. The bump construction is a candidate strict example. The remaining audit obligations are the exact global extension of \(h\), the least-modulus estimate with the chosen bump profile, and a line-by-line check that the old residual window and complete-fiber conventions use the same object. No claim of publication novelty is made.
