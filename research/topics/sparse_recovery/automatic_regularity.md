# Sharp automatic regularity of least-squares norm-difference minima

**Status:** `derived-checked` for C224–C226 as stated below. The mathematical proof, full-output exclusion, and explicit continuity bounds have been independently read and reconstructed by another project agent, then corrected and checked by the coordinating agent. This is internal mathematical reception, not external peer review or certification of publication novelty. Prior-art audit remains open.

**Identity:** finite-dimensional least squares with c=A^T b, not an arbitrary PSD quadratic with an unrelated linear term. Local minimizers, arbitrary stationary points, the full limiting-subdifferential resolvent, and the globally minimizing proximal map are distinct objects.

<a id="sr-object"></a>
## C224: Objects and automatic-regularity statement

Let 1<p<=3/2, eta>0, A in R^(m x n), b in R^m, and assume every column A_j is nonzero. Define

Phi_p(x)=1/2 ||Ax-b||_2^2 + eta (||x||_1-||x||_p), Q=A^T A, c=A^T b,
F=partial_lim Phi_p, S={x:0 in F(x)}.

**Theorem AR / C224:** Every nonzero local minimizer xbar of Phi_p has I=supp(xbar), satisfies

1. automatic strict complementarity: |(Q xbar-c)_j|<eta for every j outside I;
2. positive definite active Hessian H_I=Q_II-eta nabla^2 ||xbar_I||_p;
3. therefore the columns A_I are linearly independent and |I|<=rank A;
4. xbar is an isolated stationary point and a strict local minimizer; the local strong linear true-residual error bound is proved separately below;
5. C226 below gives a computable conservative ball and a small-step interval on which the FULL resolvent J_(lambda F), with all output points in R^n allowed initially, is a singleton, equals the global proximal argmin, maps the input ball into itself, identifies I and its signs in one step, and contracts linearly.

Only item 2 has the sharp 3/2 threshold: strict complementarity extends to 1<p<2 and support independence to every finite p>1, as C228 below proves. Support independence at p=2 is established prior art; exact active-PD publication priority remains open. Items 4-5 are classical consequences once the automatic margins have been proved, but item 5 requires full-fiber exclusion and not merely a localized graph argument. Quantitative constants below are conservative, not claimed optimal.

## Proof of automatic strict complementarity

Since xbar!=0, ||.||_p is C^1 near xbar (including zero coordinates). Exact smooth sum rule gives
F(x)=Qx-c+eta(partial ||x||_1-nabla||x||_p) for x!=0.
At a local minimizer Fermat gives 0 in F(xbar); for j outside I, gradient_p,j(xbar)=0 and |(Qxbar-c)_j|<=eta.

Suppose equality holds for one j. Choose sigma in {-1,+1} so sigma (Qxbar-c)_j=-eta, and move x(t)=xbar+sigma t e_j with t>0. Put R=||xbar||_p>0. The exact objective difference is

Phi(x(t))-Phi(xbar)=1/2 ||A_j||^2 t^2 -eta[(R^p+t^p)^(1/p)-R].

The norm difference is (1/p)R^(1-p)t^p+O(t^(2p)). Because p<2, the negative t^p term dominates the quadratic. This contradicts a local minimum. Thus every inactive inequality is strict. This argument excludes support-boundary degeneracy at local minima; it does not exclude such stationary saddles.

## Proof of active Hessian positive definiteness

On the fixed active support/sign face, Phi is real analytic around xbar. The local-minimum second-order necessary condition gives H_I positive semidefinite. Assume H_I is singular and choose nonzero z in ker H_I. Reorder/sign-change coordinates so x_i=|xbar_i|>0 and absorb signs into z. Put

R=(sum x_i^p)^(1/p), w_i=x_i^p/R^p, r_i=z_i/x_i,
a=sum w_i r_i, s_i=r_i-a, mu_k=sum w_i s_i^k.

Here w_i>0, sum w_i=1, mu_1=0. If mu_2=0, z=a xbar is radial. Norm homogeneity gives nabla^2||xbar_I||_p xbar_I=0, so H_I z=0 implies A_I xbar_I=0. Dotting active stationarity with xbar gives

0=||Axbar||^2-b^T Axbar + eta (||xbar||_1-||xbar||_p).

If |I|>=2, Axbar=0 leaves a strictly positive last term, contradiction. If |I|=1, Axbar=0 contradicts the nonzero-column assumption. Thus mu_2>0.

For small t, factor the radial part exactly:

||xbar+t z||_p/R=(1+a t) f(t/(1+a t)),
f(u)=(sum w_i(1+u s_i)^p)^(1/p).

Write f(u)=1+c_2 u^2+c_3 u^3+c_4 u^4+O(u^5). Binomial expansion gives

c_2=(p-1)mu_2/2,
c_3=(p-1)(p-2)mu_3/6,
c_4=(p-1)(p-2)(p-3)mu_4/24 -(p-1)^3 mu_2^2/8.

Thus the cubic coefficient along the original z is c_3-a c_2 and the quartic coefficient is c_4-2a c_3+a^2 c_2. Active stationarity kills the linear objective term; z in ker H kills its quadratic term. The data term is exactly quadratic and the l1 term is affine, so all objective coefficients from degree 3 onward are minus eta R times the corresponding norm coefficients. A local minimum therefore requires c_3-a c_2=0; equivalently a=c_3/c_2. Its norm quartic coefficient is

C_4=c_4-c_3^2/c_2.

**Pearson moment inequality, with equality conditions:**

mu_4-mu_2^2-mu_3^2/mu_2
 = sum w_i (s_i^2-mu_2-(mu_3/mu_2)s_i)^2 >=0.

Substitute this bound into C_4 to obtain

C_4 >= (p-1)[(3-2p)(p+1)mu_2^2/24 +(2-p)(p+1)mu_3^2/(72mu_2)].

For 1<p<3/2, this is strictly positive because mu_2>0. The objective has strictly negative quartic coefficient, impossible for a local minimum.

At p=3/2 the bound is (5/576)mu_3^2/mu_2. If C_4>0 the same contradiction applies. If C_4=0, all nonnegative pieces force mu_3=0 and mu_4=mu_2^2. The square identity forces s_i^2=mu_2 at every coordinate, so s_i takes exactly +d and -d, d=sqrt(mu_2)>0, with total weight 1/2 on each side. Also a=c_3/c_2=0. Consequently the norm along z is exactly

||xbar+t z||_p/R = [( (1+d t)^(3/2)+(1-d t)^(3/2))/2]^(2/3)
 =1+d^2 t^2/4+d^6 t^6/192+O(t^8).

The quadratic is already cancelled, cubic through fifth vanish, and the objective sixth coefficient is -eta R d^6/192<0. This again contradicts a local minimum. Hence H_I is positive definite, including the endpoint p=3/2.

Since the norm Hessian is positive semidefinite, Q_II=H_I+eta norm-Hessian is positive definite. This proves the support rank conclusion.

### Independent curved-path obstruction (same C224 statement)

The sixth-order endpoint proof above is retained. A second proof explains the role of radial relaxation and gives a useful necessary inequality at any singular active minimum, for every finite p>1.

Suppose z!=0 is an active Hessian-null direction at a nonzero local minimum. Put N(x)=||x||_p and write on the active face

N(xbar+t z)=N(xbar)+n1 t+n2 t^2+n3 t^3+n4 t^4+O(t^5).

The radial exclusion above gives q0=||A xbar||^2>0 and n2>0. Since H z=0 and Hess N(xbar) xbar=0, xbar^T Q z=0. Straight-line local minimality forces n3=0. For the actual two-variable perturbation x(s,t)=(1+s)xbar+t z, positive homogeneity, stationarity, and the exact quadratic data loss yield

\[
\Phi(x(s,t))-\Phi(xbar)
=\frac{q_0}{2}s^2+\eta n_2\frac{s t^2}{1+s}
-\eta n_4\frac{t^4}{(1+s)^3}+O(t^5),
\]

uniformly for small s. Set s=−eta n2 t^2/q0. Then

\[
\Phi(x(s,t))-\Phi(xbar)
=-\left(\eta n_4+\frac{\eta^2 n_2^2}{2q_0}\right)t^4+O(t^5).
\]

Consequently a singular active minimum must satisfy n4<=−eta n2^2/(2q0)<0. For 1<p<=3/2 the Pearson calculation above gives n4=R C4>=0, which contradicts this necessary inequality, including quartic equality at the endpoint. This alternative proof does not replace or modify the requested straight-line sixth-order certificate. For C225's symmetric construction, q0=2alpha, n2=beta and n4=R c4; the necessary inequality recovers the radial-relaxation threshold alpha>=beta^2/(−4R c4).

## Zero-column exception and origin

The nonzero-column assumption is material. Example A=[0,1], b=0, eta=1. Every xbar=(a,0), a!=0, is a local minimizer: the active ray has identically zero objective; for small y off the ray, |y| dominates the negative O(|y|^p) norm correction and the nonnegative data quadratic. The active Hessian is zero. No automatic isolation theorem applies to this example.

The theorem excludes xbar=0. For this homogeneous penalty, origin can be a local minimizer only if A^T b=0, by examining both directions of each coordinate axis. If A has no zero columns and A^T b=0 then Phi(x)-Phi(0)=1/2||Ax||^2+eta(||x||_1-||x||_p)>0 for every nonzero x (the penalty vanishes only on one-sparse vectors, whose data cost is positive). Thus origin is the unique global minimum and there are no nonzero stationary points. One must handle the limiting subdifferential at origin directly; the formula partial l1-minus-gradient norm is not valid there.

<a id="sr-full-resolvent"></a>
## C226: Conservative computable full-resolvent basin

For xbar!=0 define delta=min_(j outside I)[eta-|(Qxbar-c)_j|]>0 when I is not all coordinates. If I is full, omit all delta-dependent conditions. Choose rho>0 so B_rho(xbar) excludes origin, preserves signs of x_I, and the following hold:

(A) H_I(y_I)>=m Id for y supported on I in B_rho(xbar), with m>0;
(B) |(Qy-c)_j-eta nabla_j||y||_p|<=eta-delta/2 for every j outside I and every y in B_rho(xbar).

These conditions follow by continuity. Fully computable sufficient bounds are supplied below; their optimality is not claimed. Let

L_p=sqrt(n)+n^(1/p-1/2),
M=||Qxbar-c||+||Q|| rho/4+eta L_p.

The penalty g_p=||.||_1-||.||_p is globally L_p-Lipschitz in Euclidean norm. Every Frechet subgradient w satisfies ||w||<=L_p: test the defining lower first-order bound on a unit direction, and use the upper Lipschitz difference bound; limiting subgradients inherit the same norm bound by their defining limits. Globally, including at y=0, use the smooth sum rule F(y)=Qy-c+eta partial_lim g_p(y). The formula partial ||y||_1-minus-gradient norm is used only at nonzero points. For every FULL resolvent output y (even if not initially localized), p_in=y+lambda(Qy-c+eta w) and

||y-p_in|| <=lambda(||Q p_in-c||+eta L_p).

This follows by writing (I+lambda Q)(y-p_in)=lambda(c-Qp_in-eta w) and ||(I+lambda Q)^(-1)||<=1. Choose lambda M<rho/2 and 0<r<min(rho/4,lambda delta/2). Then every full output for p_in in B_r(xbar) lies in B_(3rho/4)(xbar). If y_j!=0 for an inactive j, the exact offsupport resolvent equation gives

sign(y_j)(p_in)_j >= |y_j|+lambda delta/2 >lambda delta/2,

contradicting |(p_in)_j|<=r. Thus every full output is supported on I with the correct active signs. Strong monotonicity from (A) then proves full-output uniqueness and

||J_(lambda F)(p_in)-xbar|| <=(1+lambda m)^(-1)||p_in-xbar||.

Existence does not follow from this uniqueness argument: it comes separately from the global proximal subproblem. Its objective Phi(y)+(1/(2lambda))||y-p_in||^2 is continuous and coercive because the penalty and data loss are nonnegative. Hence it has a global minimizer; Fermat places every minimizer in the full resolvent. Since the latter has at most one output, both maps equal the singleton above. This establishes full coverage, full-fiber exclusion, invariance, one-step identification and linear convergence for all initial points in the certified ball. No claim is made for larger lambda or arbitrary stationary points.

**True-residual EB in the same rho-window.** If x has any nonzero inactive coordinate, (B) implies r_F(x)>=delta/2. Thus ||x-xbar||<=rho<=(2rho/delta)r_F(x). If x is supported on I, all inactive intervals contain zero and the true residual equals the active gradient norm; (A) gives r_F(x)>=m||x-xbar||. Therefore a valid strong linear EB constant is max(1/m,2rho/delta), with the latter omitted for full support.


### Explicit conservative continuity radius (additional derived calculation)

The continuity gates (A)-(B) above can already be replaced by a fully explicit bound. Set C_n=n^(1/p-1/2), R=||xbar||_p and a_min=min_I|xbar_i|. For rho<=R/(2C_n), rho<=a_min/2, one has ||y||_p>=R/2 and preserved active signs. With B_Q=max_(j outside I)||Q_j||_2, the offsupport estimate is

|(Qy-c)_j-eta grad_p,j(y)| <= |(Qxbar-c)_j|+B_Q rho+eta (2rho/R)^(p-1).

Thus rho<=delta/(4B_Q) and rho<=(R/2)(delta/(4eta))^(1/(p-1)) imply (B), omitting the first bound when B_Q=0. At p=3/2 this explicit safe radius scales quadratically in the strict-complementarity gap delta; sharpness of that scaling for complete basins is not proved here.

To certify (A), put s=|I|, C_s=s^(1/p-1/2), r0=min(a_min/2,R/(2C_n)), d=a_min/2, N0=R/2, U=max_I|xbar_i|+r0 and V=sqrt(s) U^(p-1). On the active Euclidean ball B_r0(xbar_I) use the exact Hessian formula

nabla^2||u||_p=(p-1)[||u||_p^(1-p) diag(|u_i|^(p-2)) - ||u||_p^(1-2p) vv^T], v_i=sign(u_i)|u_i|^(p-1).

A conservative Euclidean Lipschitz constant for this Hessian is

L_H=(p-1)[N0^(1-p)(2-p)d^(p-3)
 +(p-1)N0^(-p) C_s d^(p-2)
 +2 N0^(1-2p) V (p-1)d^(p-2)
 +(2p-1)N0^(-2p) C_s V^2].

Each term follows from scalar mean value bounds for the two norm powers, the diagonal powers, and ||vv^T-ww^T||<=(||v||+||w||)||v-w||. The final rho is positive and chosen to satisfy rho<=r0 as well as every applicable bound above. If h_min=lambda_min(H_I)>0, also impose rho<=h_min/(2eta L_H), yielding m=h_min/2. The one-coordinate norm Hessian is identically zero, so when s=1 the sharper choice m=||A_I||^2 has no Hessian continuity restriction. These bounds remove the basic computability gap; optimizing them, proving asymptotically sharp basin laws, and handling full-resolvent folds remain separate research obligations.

<a id="sr-sharpness"></a>
## C225-v1: Original sharpness range 3/2<p<2

Take n=m=2, eta=1, xbar=(1,1), R=2^(1/p). Use radial/tangent coordinates x=(1+h+t,1+h-t). Set Q=A^T A to have eigenvalues alpha>0 on (1,1) and beta=R(p-1)/2 on (1,-1); Q is positive definite. Choose c=Qxbar+(1-R/2)(1,1), and choose A=Q^(1/2), b=A^(-T)c, so active stationarity is exact.

The active Hessian has eigenvalues alpha on the radial direction and zero on the tangent direction. For the symmetric norm expansion,

c_2=(p-1)/2,
c_4=-(p-1)(2p-3)(p+1)/24<0 for p>3/2.

The objective difference has local expansion

alpha h^2+beta h t^2-R c_4 t^4+O(h^2 t^2+|h|t^4+t^6).

The analytic IFT minimizes in h with h(t)= -beta t^2/(2alpha)+O(t^4). Its reduced objective is

K t^4+O(t^6), K=-R c_4-beta^2/(4alpha).

Choose alpha>beta^2/(-4R c_4), so K>0. Shrink the neighborhood so partial_hh Phi>=alpha>0 and the reduced objective is at least (K/2)t^4. Taylor's integral remainder in h gives

Phi(h,t)-Phi(h(t),t)>=(alpha/2)|h-h(t)|^2.

These two inequalities prove a strict full-space local minimum with singular active Hessian, rather than a minimum restricted to h=0. This makes p=3/2 a sharp universal automatic-nondegeneracy threshold in the range 1<p<2. The p=5/3, alpha=10 instance is additionally checked in the linked reproducible code, but the all-nearby-points claim is carried by this analytic proof.

For these examples the smooth true-residual EB cannot have exponent greater than 1/3. The radial critical curve is analytic and even, and along it partial_h Phi=0 while partial_t Phi=4Kt^3+O(t^5). All nearby stationary points must lie on this curve, and its reduced derivative has no zero except t=0 after shrinking. Thus xbar is an isolated stationary point. In a yet smaller ball, the distance to the entire stationary set S equals the distance to xbar. Along the curve this distance is asymptotic sqrt(2)|t| while r_F=O(|t|^3), excluding every exponent q>1/3. For the fixed p=7/4 instance, the matching lower EB and genuine complete-PPA tail are now proved in [C227](sharp_instance_dynamics.md#sd-theorem). No corresponding actual-trajectory theorem for every member of this family is asserted here. The radial minimization curve is not asserted to be invariant under PPA.



<a id="sr-sharpness-all-p"></a>
## C225-v2: Sharpness for every finite p>3/2

**Version identity.** This widens only C225's existence quantifier from 3/2<p<2 to every finite p>3/2. C225-v1 above remains the original restricted statement. It does not widen the p<=3/2 continuity constants in C226 or the fixed-instance trajectory theorem C227.

**Exact statement and construction.** For each real 3/2<p<infinity, put

\[
R=2^{1/p},\quad \beta=R(p-1)/2,\quad
c_4=-(p-1)(2p-3)(p+1)/24,\quad
\alpha_0=\frac{3R(p-1)}{2(2p-3)(p+1)}.
\]

Choose any alpha>alpha0; alpha=2alpha0 is one explicit choice. Let Q have radial/tangent eigenvalues alpha,beta, and set xbar=(1,1), eta=1, A=Q^(1/2), c=Q xbar+(1−R/2)(1,1), b=A^(−T)c. Then xbar is a strict full-space local minimum with singular active Hessian, is locally the sole stationary point, and every strong true-residual exponent q>1/3 fails there (also for distance to the full stationary set after shrinking the ball).

**Proof.** Q is positive definite and A is invertible. Stationarity and the tangent Hessian cancellation are exact as in v1. Every coordinate near xbar is positive, so the p-norm restricted to this neighborhood is real analytic for every finite real p>1; neither offsupport smoothness nor an assumption p<2 is needed. The symmetric binomial identity gives the displayed c4, which is negative for every p>3/2. The expansion and radial IFT therefore give

\[
V(h,t)=\alpha h^2+\beta ht^2-Rc_4t^4
+O(h^2t^2+|h|t^4+t^6),\qquad
h_*(t)=-\frac{\beta}{2\alpha}t^2+O(t^4),
\]
\[
V(h_*(t),t)=K t^4+O(t^6),\qquad
K=-Rc_4-\frac{\beta^2}{4\alpha}>0,
\]

because alpha0=beta^2/(−4R c4). For alpha=2alpha0,
K=R(p−1)(2p−3)(p+1)/48. On a sufficiently small neighborhood V_hh>=alpha, so Taylor integration around h_*(t) yields
V(h,t)>=alpha|h−h_*(t)|^2/2+K t^4/2. This proves strict full-space local minimality. Its nearby stationary points lie on the IFT curve; the reduced derivative 4K t^3+O(t^5) vanishes only at zero. On that curve the true gradient residual is |V_t|/sqrt(2)=O(|t|^3) and the Euclidean displacement is asymptotic to sqrt(2)|t|, proving every q>1/3 exclusion. Stationary isolation transfers it to distance to the entire stationary set in a smaller ball.

The neighborhood may depend on p, particularly as p approaches 3/2 or grows. No p=infinity theorem and no uniform exponent for all upper-side models is asserted. Together with C224 this establishes the exact universal active-PD threshold across all finite p>1.

**Independent evidence.** Two new readers independently checked the extension and the p=2/large-p boundaries; [reception](../../audit/SPARSE_THRESHOLD_RECEPTION_2026_10_09.md) records the proof mechanism. [Finite exact and 80-digit checks](../../code/sparse_regularity/upper_family_verify.py) include a parameter just above 3/2, p=2, and larger finite p; computation does not prove the all-real-p quantifier.

<a id="sr-uniform-steps"></a>
## C226 uniform positive step interval and scope

Given the computed rho, m, delta and M, choose 0<lambda_min<=lambda_max with lambda_max M<rho/2. Choose

0<r<min(rho/4,lambda_min delta/2),

omitting the second condition when the support is full. Every lambda in this interval has the same full coverage, full-output uniqueness, active identification and invariant input ball. For any sequence lambda_k in this interval and x_0 in B_r(xbar), the complete ordinary PPA has a unique trajectory and

||x_k-xbar|| <= (1+lambda_min m)^(-k)||x_0-xbar||.

This is a local statement at each specified nonzero local minimizer. No constants are uniform over all data or all minimizers. The residual EB also proves local stationarity isolation. To obtain strictness from the assumed local minimum, choose its nondecreasing neighborhood. Any other point with the same value in its interior is itself a local minimum, hence stationary by Fermat and therefore equal to xbar.

**Stationary points are not all minima, even at p=3/2.** An exact scope counterexample uses eta=1, xbar=(1,1), R=2^(2/3), d=R/8, alpha>0,

Q=[[d,-d],[-d,alpha+d]], c=(1-R/2,alpha+1-R/2).

Q is positive definite with determinant d alpha; take A=Q^(1/2), b=A^(-T)c. Active stationarity is exact, H=diag(0,alpha), and Phi(xbar+t e1)-Phi(xbar)=R t^3/32+O(t^4), so this is a stationary nonminimum. This qualitative example makes no assertion about the set of PPA initial points that converge to it. Automatic regularity at local minima is not a global minimizer-convergence theorem or a sparse-signal recovery guarantee.

<a id="sr-evidence"></a>
## Evidence and exact remaining mathematical gaps

- [Exact Fraction and high-precision checks](../../code/sparse_regularity/README.md) independently recompute Pearson's identity, the cubic/quartic algebra, the endpoint sixth coefficient, an upper-threshold strict-minimum instance and a complete small-step certificate. Finite computation is not the proof of universal quantifiers.
- Two mathematical readers checked the whole initial proof and full-fiber argument; the second reader additionally checked every term of the appended explicit L_H bound. The coordinating reader removed unsupported tilt-stability terminology, changed a misleading box to an Euclidean ball, supplied the global limiting-subgradient bound and full-space IFT inequality, and clarified isolation and full positive-step interval quantifiers.
- [Read primary literature and unclosed full-text gates](../../LITERATURE.md#lit-sparse-automatic-threshold). The model family and ordinary conditional local convergence are not asserted to be new. Exact published priority of the automatic PD threshold is open.
- C225 retains its all-3/2<p<2 sharpness family. [C227](sharp_instance_dynamics.md#sd-theorem) closes the fixed p=7/4 matching strong true-residual exponent 1/3 and complete-PPA slow tail, with an explicit invariant ball and exact norm constant. It separates the geometric radial axis and proves radial following; no general upper-side uniform exponent is asserted.
- The conservative basin is computable; no optimal conditioning law or maximal basin/fold classification has been proved. Those questions are separate from basic existence.


<a id="sr-wide-ranges"></a>
## C228: Separate ranges of strict complementarity and support rank

**Exact statement.** In the same least-squares model with eta>0 and no zero columns, every nonzero local minimum has independent support columns for every finite p>1. Its inactive inequalities are strict whenever 1<p<2. These conclusions do not have a sharp 3/2 threshold; that threshold belongs to automatic active-Hessian positive definiteness. This is a range refinement, not a change to the narrower C224-v1 identity or a standalone priority claim.

**Proof.** The inactive-coordinate descent proof above uses only p<2 and a nonzero base point, so it gives the stated wider strict-complementarity range. For support rank, the second-order necessary condition on the active orthant gives H=Q_II−eta Hess||xbar_I||_p positive semidefinite, without assuming it positive definite. For active u with no zero coordinates, R=||u||_p, w_i=|u_i|^p/R^p and r_i=z_i/u_i, direct differentiation gives

\[
z^T\nabla^2\|u\|_p z=(p-1)R\left[\sum_iw_ir_i^2-\left(\sum_iw_ir_i\right)^2\right].
\]

All weights are positive. Thus the norm Hessian is positive semidefinite with kernel exactly span{u}, for every finite p>1. If A_I z=0 for a nonzero z, then 0≤z^T H z=−eta z^T Hess||xbar_I||_p z≤0, forcing z=a xbar_I, a≠0. Hence A xbar=0. Dot active stationarity with xbar; because c=A^Tb it yields 0=eta(||xbar||_1−||xbar||_p). For at least two nonzero coordinates that difference is strictly positive; for one coordinate A xbar=0 contradicts its nonzero column. No such z exists, proving full column rank and |I|≤rank A.

**Scope and prior art.** The no-zero-column and least-squares compatibility gates remain material, with the examples above and in [the independent review](../../audit/SPARSE_THRESHOLD_REVIEW_2026_10_09.md). Yin–Lou–He–Xin (2015), Theorem 2.4 and Corollary 2.1(a), p.A543, provide the explicit p=2 support antecedent. The wider norm-curvature mechanism is credited as an extension, not confused with the novel-threshold candidate. Exact publication priority of the all-p range is not certified.

### Boundary counterexample: strict complementarity can fail for every finite p>=2

This counterexample fixes the upper boundary of C228's strict-complementarity range; it does not change C228-v1's sufficient-statement identity. Take eta=1, Q=diag(1,2), c=(1,1), A=diag(1,sqrt(2)), b=(1,1/sqrt(2)), and xbar=(1,0). For p=2 and r=||x||_2, direct completion of the square gives

\[
\Phi_2(x)-\Phi_2(xbar)
=\tfrac12(r-1)^2+\tfrac12x_2^2
+(|x_1|-x_1)+(|x_2|-x_2)\ge0.
\]

Equality holds only at xbar. For every finite p>=2, ||x||_p<=||x||_2 and ||xbar||_p=1, so

\[
\Phi_p(x)-\Phi_p(xbar)
=\Phi_2(x)-\Phi_2(xbar)+\|x\|_2-\|x\|_p.
\]

Hence the same xbar is the unique global minimizer for all these p, yet |(Q xbar−c)_2|=eta=1. Active-Hessian positivity and inactive strict complementarity are different structural properties: their automatic thresholds are 3/2 and 2, respectively. Support independence retains its whole finite p>1 range. These boundary claims do not assert publication priority.
