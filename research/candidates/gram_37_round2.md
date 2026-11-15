# C270/C304 pure Gram two-column prox: second 3/7 attack

## Verdict

**Continue validation; no counterexample found, but the 3/7 upper bound is not proved.** The complete equations and exact Gram identities rule out the most obvious transverse and rank-two cancellations. All tested monomial arcs reduce to the collinear transition \(s^7\leftrightarrow s^3\), which produces \(3/7\). The remaining gap is a precise anisotropic inverse estimate for the conserved second-column equation, uniform across rank-one and rank-two strata. Finite arc searches do not certify it.

## Full object and exact identities

For \(Z=[a\ b]\) and \(Y=T_\lambda(Z)=[\alpha\ \beta]\),
\[
u(Z)=\|a\|^2a+\langle a,b\rangle b,\qquad
k(Z)=\langle a,b\rangle a+\|b\|^2b,
\]
and the complete unique prox solves
\[
u(Y)+\lambda\alpha=u(Z),\qquad k(Y)=k(Z).
\tag{G1}
\]
The identities
\[
\langle k(Z),b\rangle=\langle a,b\rangle^2+\|b\|^4\ge\|b\|^4,
\]
and, with \(S=\|a\|,R=\|b\|,c=\langle a,b\rangle/(SR)\),
\[
\|u(Z)\|^2=S^6+S^2R^2(2S^2+R^2)c^2,\quad
\|k(Z)\|^2=R^6+S^2R^2(S^2+2R^2)c^2
\tag{G2}
\]
show that angular changes cannot cancel both cubic signals. The output analogue is
\[
\langle k(Y),\beta\rangle=\langle\alpha,\beta\rangle^2+\|\beta\|^4.
\tag{G3}
\]
These are exact and hold in every \(m\ge2\).

## Rank-two and transverse attacks

For \(a=t e_1\), \(b=r e_2\), the output has \(\alpha=Ae_1,\beta=Ce_2\) and
\[
 (A^2+C^2+\lambda)A=t^3+tr^2,\qquad
 (A^2+C^2)C=r^3.
\tag{G4}
\]
Since \(A\sim t^3/\lambda\), the transverse output is \(C\sim r\) for \(r=t^B\) with \(B<3\), and \(C\sim r^3/t^6=t^{3B-6}\) for \(B>3\). Neither branch gives output/input exponent below one.

For \(a=t e_1\), \(b=s e_1+r e_2\), the input invariants are
\[
\begin{aligned}
u(Z)&=(t^3+ts^2)e_1+tsr\,e_2,\\
k(Z)&=(t^2s+s^3+sr^2)e_1+(s^2+r^2)r\,e_2.
\end{aligned}
\tag{G5}
\]
The only possible weak coefficient is the \(t^2s\) term aligned with the observed direction. The collinear transition is \(s=t^7\): it gives input separation \(t^7\), output separation \(t^3\). If \(s\gg t^7\), the cubic branch dominates and the output difference is smaller; if \(s\ll t^7\), the linearized branch gives output \(\asymp s/t^4\), and the constraint \(s\le t^7\) forces \(d\gtrsim h^{7/3}\).

More generally, write \(\|a\|=t^s,\|b\|=t^r\), with a small angle \(c=t^\ell\). The two leading orders of \(k(Z)\) are \(t^{2s+r+\ell}\) and \(t^{3r}\). The output equation has the order relation
\[
K=\min\{3B,\,6s+B\},
\]
where \(B\) is the order of the weak output column. The transition is \(r=7s\), again giving \(B=3s\). A rank-two angle can reduce a coefficient, but (G2) prevents an exact cancellation in the weak output direction. No tested arc gives \(H/D<3/7\).

These calculations are scaling evidence only. They do not rule out a non-monomial or angle-dependent arc, nor do they supply a uniform constant on a bounded set.

## Smallest hard lemma for a proof

Let \(Y=[\alpha,\beta]\), \(Y'=[\alpha',\beta']\) be the outputs of two inputs \(Z,Z'\) in a fixed bounded ball. Put
\[
h=\|Y-Y'\|,\quad d=\|Z-Z'\|,\quad
\sigma=\max\{\|\alpha\|,\|\alpha'\|\}^{1/3}.
\]
The missing statement can be reduced to an anisotropic estimate for
\[
B_\alpha(\beta)=\|\beta\|^2\beta+\langle\alpha,\beta\rangle\alpha,
\qquad B_\alpha(\beta)=k(Z).
\]
The desired dichotomy is a **uniform** version of
\[
\|\beta-\beta'\|
\lesssim
\begin{cases}
(\text{cross forcing})^{1/3},&\text{cubic branch},\\
\text{cross forcing}/\rho^2,&\text{linear branch},
\end{cases}
\]
together with the first equation \(u(Y)+\lambda\alpha=u(Z)\), which must force the coupling
\[
\sigma\gtrsim h^{1/3}\quad\text{whenever the linear branch is active}.
\]
Then \(d\gtrsim h\,\sigma^4\) in the linear branch and \(\sigma\gtrsim h^{1/3}\) yields \(d\gtrsim h^{7/3}\); the cubic branch gives the same lower bound after its own scale relation. The hard point is that \(\alpha,\alpha'\) need not be parallel and the weak eigendirection of \(D_\beta B_\alpha\) rotates with the pair.

Any proof must also stratify the singular locus of \(Dv\): full-rank outputs are locally regular, while rank-one outputs require a quantitative angle decomposition. A purely scalar estimate in \(\|\beta\|\) loses the alignment information and falls back to the known \(1/3\) exponent.

## Finite verification and what would change the verdict

The exact C270 \(t^7\) witness certifies that exponents \(>3/7\) fail. The transverse formulas (G4)–(G5) and the Gram positivity (G2) give no \(<3/7\) witness. This is not a proof of 3/7: exhaustive finite searches, floating-point fits, and a Newton polygon on one rank-one slice cannot exclude a transverse semialgebraic arc.

The candidate becomes a theorem only after either:

1. proving the anisotropic \(B_\alpha\) dichotomy plus the scale coupling uniformly on the bounded set; or
2. performing a complete semialgebraic Łojasiewicz/Newton analysis of the two-point graph, including all rank and angle strata, and proving that every admissible arc has quotient at least \(7/3\).

An explicit rank-two family with \(H/D<3/7\), especially one using near-cancellation of the two \(k\)-components while rotating the weak output eigendirection, would falsify the candidate. No such family is presently known.
