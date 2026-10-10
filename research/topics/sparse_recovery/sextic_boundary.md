# A sextic upper-side minimum: sharp true-residual exponent 1/5

**Status:** derived-checked. Two independent structural readers reconstructed the data, radial elimination and matching residual estimate. The exact finite coefficients have a separate reproducible check. This supporting example limits the scope of the quartic result; no published-priority or proximal-trajectory assertion is made here.

<a id="sx-data"></a>
## Exact data and statement (C229-v1)

Set \(p=3\), \(\eta=1\), \(R=2^{1/3}\), \(\bar x=(1,1)\), and

\[
Q=\frac R8\begin{pmatrix}5&-3\\-3&5\end{pmatrix},\qquad
A=\frac{\sqrt R}{4}\begin{pmatrix}3&-1\\-1&3\end{pmatrix},\qquad
c=(1-R/4)(1,1),\qquad b=\frac{2(1-R/4)}{\sqrt R}(1,1).
\]

Thus \(A^TA=Q\), \(A^Tb=c\), and \(A\) is invertible. Define the original global model

\[
\Phi(x)=\tfrac12\|Ax-b\|_2^2+\|x\|_1-\|x\|_3,\qquad
F=\partial_{\rm lim}\Phi,\quad S=F^{-1}(0),\quad r_F(x)=\operatorname{dist}(0,F(x)).
\]

Then \(\bar x\) is a strict local minimum with singular active Hessian, is locally stationary-isolated, and has **sharp strong true-residual exponent \(1/5\)**: some \(a,C>0\) satisfy

\[
\|x-\bar x\|\le C r_F(x)^{1/5}\quad(\|x-\bar x\|<a).
\]

For every \(q>1/5\) and every \(K,a>0\), some \(x\) with \(0<\|x-\bar x\|<a\) violates the corresponding exponent-\(q\) bound. After shrinking \(a\), the same statements hold with distance to the entire \(S\). In particular a matching \(1/3\) bound does not hold at every upper-side local minimum, even with invertible \(A\).

<a id="sx-proof"></a>
## Self-contained proof

At \(\bar x\), \(\nabla\|\bar x\|_3=(R/2)(1,1)\). Stationarity follows from \(Q\bar x-c=(R/2-1)(1,1)\). The active Hessian is

\[
H=\frac R8\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\operatorname{spec}H=\{R/4,0\}.
\]

Write \(x=(1+h+t,1+h-t)\), \(s=1+h\), and \(V(h,t)=\Phi(x)-\Phi(\bar x)\). In a positive-coordinate rectangle the exact analytic identity is

\[
\frac VR=\frac{h^2}{4}+t^2-s\left[\left(1+\frac{3t^2}{s^2}\right)^{1/3}-1\right]. \tag{S1}
\]

The binomial expansion \((1+3u^2)^{1/3}=1+u^2-u^4+5u^6/3+O(u^8)\), uniform with \(h\) in a small compact interval, gives

\[
\frac VR=\frac{h^2}{4}+\frac{ht^2}{1+h}+\frac{t^4}{(1+h)^3}
-\frac{5t^6}{3(1+h)^5}+O(t^8), \tag{S2}
\]
\[
\frac{V_h}R=\frac h2+\frac{t^2}{(1+h)^2}-\frac{3t^4}{(1+h)^4}
+\frac{25t^6}{3(1+h)^6}+O(t^8). \tag{S3}
\]

Since \(V_{hh}(0,0)=R/2>0\), the analytic implicit function theorem gives a unique even curve \(h=g(t)\) with \(V_h(g(t),t)=0\). Substitute \(g(t)=a_2t^2+a_4t^4+O(t^6)\) into (S3):

\[
a_2/2+1=0,\qquad a_4/2-2a_2-3=0.
\]

Hence

\[
g(t)=-2t^2-2t^4+O(t^6),\qquad
\psi(t):=V(g(t),t)=\frac R3t^6+O(t^8),\qquad
\psi'(t)=2Rt^5+O(t^7). \tag{S4}
\]

For transparency, the degree-four coefficient of \(V/R\) is \(a_2^2/4+a_2+1=0\); its degree-six coefficient is

\[
a_2a_4/2+a_4-a_2^2-3a_2-5/3=1/3.
\]

Shrink the rectangle so that \(V_{hh}\ge R/4\), \(g(t)\) and every segment from \(g(t)\) to \(h\) remain in it, and \(\psi(t)\ge Rt^6/6\). Taylor's integral formula gives

\[
V(h,t)\ge \frac R8|h-g(t)|^2+\frac R6t^6. \tag{S5}
\]

This proves full-space strict minimality. Every nearby stationary point first satisfies \(h=g(t)\); (S4) then forces \(t=0\). Thus \(\bar x\) is the sole stationary point in a neighborhood.

On this positive-coordinate neighborhood \(F(x)=\{\nabla\Phi(x)\}\), and the coordinate transformation gives

\[
\sqrt{V_h^2+V_t^2}=\sqrt2\,r_F(x). \tag{S6}
\]

On \(g\), \(V_h=0\), \(V_t=\psi'\), and

\[
\|x(t)-\bar x\|\sim\sqrt2|t|,\qquad r_F(x(t))\sim\sqrt2R|t|^5.
\]

Consequently \(\|x(t)-\bar x\|/r_F(x(t))^q\to\infty\) whenever \(q>1/5\), proving the failure quantifiers.

For the matching bound set \(u=h-g(t)\) and let \(L=\sup|V_{ht}|<\infty\) on a smaller rectangle. Radial curvature and the mean-value formula give

\[
|u|\le4|V_h(h,t)|/R,
\qquad
R|t|^5\le|\psi'(t)|\le|V_t(h,t)|+L|u|. \tag{S7}
\]

The lower bound for \(|\psi'|\) follows from (S4) after shrinking. Equations (S6)–(S7) give \(|u|\le C_1r_F\), \(|t|\le C_2r_F^{1/5}\). Since \(g(t)=O(t^2)\), further shrinking to \(r_F\le1\) proves the claimed point-distance bound. Stationary isolation provides a ball containing no other point of \(S\); on a ball of less than half that radius, distance to the entire \(S\) equals distance to \(\bar x\). This justifies the global-zero-set formulation without altering the residual.

## Scope and evidence

This is the equality parameter \(p=3,\alpha=\alpha_0=R/4,\beta=R\) of the family in [C225-v2](automatic_regularity.md#sr-sharpness-all-p); its theorem assumes \(\alpha>\alpha_0\) and remains unchanged. Here the fourth-order reduced coefficient vanishes and the positive sixth-order coefficient supplies strictness. This example strengthens the scope restriction on [C227](sharp_instance_dynamics.md#sd-theorem), without asserting an explicit complete-proximal window or any actual PPA law for this new instance. Local constants above are existential.

- [Exact coefficient verifier](../../code/sparse_regularity/sextic_boundary_verify.py) uses only standard-library Fraction arithmetic; it does not prove the analytic neighborhood statements.
- [Final independent reception](../../audit/SPARSE_FINAL_RECEPTION_2026_10_10.md) records two independent reconstructions and the final transcription checks. Acceptance is internal mathematical evidence, not external peer review or publication priority.
