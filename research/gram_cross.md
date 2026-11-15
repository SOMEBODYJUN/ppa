# Cross attack on the C270 (3/7) Gram-prox candidate

## Scope and verdict

This note stress-tests the conjecture that the complete pure Gram map
\(T_\lambda=(v+\lambda P)^{-1}v\) has exact two-point exponent (3/7) on bounded sets.  I tried rank-two and nearly orthogonal arcs, where a second output direction might in principle be more singular than the collinear witness.  The order analysis below finds no exponent below (3/7).  The argument is a scaling obstruction and not a proof of the global Hölder bound; the remaining gap is to turn the strata calculation into a uniform inequality.

## 1. Equations and a positive identity

Write (Z=[a\ b]), (Y=[\alpha\ \beta]), and
\[
 u(Z)=\|a\|^2a+\langle a,b\rangle b,
 \qquad
 k(Z)=\langle a,b\rangle a+\|b\|^2b.
\]
The complete prox equations are
\[
 u(Y)+\lambda\alpha=u(Z),\qquad k(Y)=k(Z).
\tag{C1}
\]
The second column has an exact sign identity
\[
 \langle k(Z),b\rangle
   =\langle a,b\rangle^2+\|b\|^4\ge\|b\|^4.
\tag{C2}
\]
Thus (k(Z)=0) forces (b=0).  In particular, no choice of a transverse angle can cancel the cubic (b)-signal in all directions.  This is the main reason the rank-two search does not immediately produce a worse exponent.

For the output equation, taking the scalar product with (eta) gives
\[
 \langle k(Y),\beta\rangle
   =\langle\alpha,\beta\rangle^2+\|\beta\|^4,
\tag{C3}
\]
so (\|\beta\|^3\le\|k(Y)\|).  The inverse can only become singular when both the observed output scale (\|\alpha\|) and the unobserved output scale (\|\beta\|) are small.

## 2. Explicit transverse arcs

Take (a=t e_1) and perturb (b=r e_2), with (r=t^B), (B>0).  Then
\[
 u(Z)=(t^3+t r^2)e_1,
 \qquad k(Z)=r^3e_2.
\]
The unique output has \(\alpha=Ae_1\), \(\beta=Ce_2\), where
\[
 (A^2+C^2+\lambda)A=t^3+t r^2,
 \qquad (A^2+C^2)C=r^3.
\tag{C4}
\]
Since (A\sim t^3/\lambda), the second equation has two regimes:

* If (B<3), then (C\sim r=t^B); the transverse output is Lipschitz in the input perturbation.
* If (B>3), then (C\sim r^3/A^2=t^{3B-6}), which is smaller than (r=t^B) for (B>3).

At (B=3), both terms balance and (C\asymp t^3).  Therefore the pure transverse family cannot give an output/input quotient below one, let alone (3/7).

Now use a mixed perturbation
\[
 b=s e_1+r e_2,
 \qquad s=t^A,quad r=t^B.
\]
For (a=t e_1),
\[
\begin{aligned}
u(Z)&=(t^3+t s^2)e_1+t s r,e_2,\\
k(Z)&=(t^2s+s^3+s r^2)e_1+(s^2+r^2)r,e_2.
\end{aligned}
\tag{C5}
\]
The parallel component is the only one with the balance (s=t^7\): when (A=7), its forcing is (k_1\sim t^9), while (A_{\rm out}\sim t^3), so the output parallel coordinate is (t^3).  If (B<7), the input difference is already at least (t^B) and the transverse equation (C4) controls its output by a no-worse order.  If (B\ge7), the (s)-component gives input distance (t^7) and output distance (t^3), exactly the (3/7) quotient.  No mixed choice changes this balance because the transverse forcing in (C5) is a sum of nonnegative-order monomials and cannot cancel the parallel (t^2s) term in the direction of (a).

## 3. Nearly orthogonal base vectors

Let (\|a\|=t^s), \(\|b\|=t^r) with (s<r), and let the cosine of their angle be (t^c).  Then
\[
 k(Z)=(a\cdot b)a+\|b\|^2b
\]
has two geometrically distinct contributions of orders (t^{2s+r+c}) (the component along (a)) and (t^{3r}) (the component along (b)).  The observed output has order (\|\alpha\|\asymp t^{3s}).  If (K) denotes the order of (\|k(Z)\|), the unobserved output scale (B=\|\beta\|) is determined by
\[
 K=\min(3B,\,6s+B).
\tag{C6}
\]
Hence (B\le3s), with equality only at the transition (K=9s).  This is the same (A=7) balance after writing the parallel input order as (r=7s).

Could a perturbation be amplified by a weaker rank-two derivative?  A perturbation of (k) in the (\beta)-direction is controlled by the (\|b\|^2b) term and has coefficient at most (t^{2r}); a perturbation in the (a)-direction has coefficient (t^{2s}) but is aligned with the observed direction.  When (a\perp b), the (a)-direction and (\beta)-direction are orthogonal, so the large (t^{2s}) coefficient cannot feed the weak output direction.  When the angle tends to zero, the model approaches the collinear equations and the only singular transition is again (r=7s).  Thus a rank-two arc can lose conditioning, but the bad coefficient and the bad output direction do not align strongly enough to beat (3/7).

This paragraph is the principal unresolved uniform step: it needs a quantitative decomposition with angle-dependent constants rather than order notation.

## 4. Generic order table

Ignoring cancellations that are ruled out by (C2), let (p=\min\{s,r\}) be the input scale.  In the worst orientation (s\le r) (observed column larger),
\[
 \operatorname{ord}(\alpha)=3s,
 \qquad
 \operatorname{ord}(k)=r+2s.
\]
The output unobserved scale is
\[
 \operatorname{ord}(\beta)=
 \begin{cases}
 (r+2s)/3,&r\le7s,\\
 r-4s,&r\ge7s,
 \end{cases}
\tag{C7}
\]
with both branches equal to (3s) at (r=7s).  A perturbation of input order (D) sees a cubic coefficient (t^{2s}) and an output inverse coefficient at worst (t^{-6s}).  In the linearized branch the output difference has order (D-4s), but it remains below the base output scale only when (D\ge7s).  The smallest quotient is therefore
\[
 \frac{D-4s}{D}\ge\frac{7s-4s}{7s}=\frac37.
\]
In the cubic branch the quotient is larger and decreases to (3/7) as (r\uparrow7s).  If (r\le s) (unobserved column at least as large), then \(\beta\) is of input order and no sub-Lipschitz quotient appears.

## 5. Current independent verdict

* **No transverse counterexample found.** Pure orthogonal, mixed, and nearly orthogonal arcs either remain Lipschitz or reduce to the collinear (r=7s) balance.
* **The candidate survives a serious scaling attack but is not proved.** The main remaining obligation is a uniform angle/rank decomposition that upgrades (C7) from monomial orders to a bounded-set inequality.
* **What would falsify it.** A family with (\|Z_t-Z_t'\|\asymp t^D), (\|T(Z_t)-T(Z_t')\|\asymp t^H), and (H/D<3/7), most plausibly requiring near-cancellation of the (t^{2s+r+c}) and (t^{3r}) components of (k\) while aligning the residual with a weak output eigendirection. Identity (C2) rules out exact cancellation along (b), but a quantitative near-cancellation construction has not been excluded.
* **Evidence that would change the verdict.** Either (i) a symbolic elimination/Newton polygon computation over all rank strata proving the minimum Łojasiewicz quotient is (7/3), or (ii) an explicit rank-two arc violating (C7). Finite numerical sampling is insufficient.

