# 非零原始数据的 Gram 回归：结构证书与锐解点指数

本页 C273-v1 是与 C270-v1 对象不同的规范证明：目标使用非零原始数据，核保持原中心。完整覆盖、真残差、共同物理证书及解点处锐的 $2/3$ 指数已独立重构；核仍单射。全域经典正面及每条轨道的 eventual ABS 正面必须并列。内部有效性不等于外部首创性。

<a id="native-gram-object"></a>
## Exact model and complete fibers

Fix an integer $m\ge2$, a nonzero data vector $c\in\mathbb R^m$, and a fixed $\lambda>0$. The physical space is $X=\mathbb R^{m\times2}$ with the Frobenius norm. Write $Z=[a\ b]$ and define

\[
f_c(Z)=\tfrac12\|a-c\|^2,\qquad F_c(Z)=\{[a-c\ 0]\},
\]
\[
h(Z)=\tfrac14\operatorname{tr}((Z^TZ)^2),\qquad
v(Z)=\nabla h(Z)=ZZ^TZ=[u(Z)\ k(Z)],
\]
\[
u(Z)=\|a\|^2a+\langle a,b\rangle b,
\qquad k(Z)=\langle a,b\rangle a+\|b\|^2b.
\tag{NG1}
\]

The raw-data target, complete zero set, physical nearest point, distance, and true residual are exactly

\[
S_c=F_c^{-1}(0)=\operatorname{argmin}f_c=\{[c\ b]:b\in\mathbb R^m\},\quad
p_Z=[c\ b],\quad d(Z,S_c)=r_{F_c}(Z)=\|a-c\|.
\tag{NG2}
\]

The kernel is applied to $[a\ b]$, not to $[a-c\ b]$. Thus (NG1) is not C270 with a change of coordinates.

Every input $Z\in X$ uses the complete relation

\[
J_{\lambda F_c}^v(Z)=(v+\lambda F_c)^{-1}(v(Z)).
\]

All its roots $Y=[\alpha\ \beta]$ satisfy, and are characterized by,

\[
(\|\alpha\|^2+\lambda)\alpha+\langle\alpha,\beta\rangle\beta
=u(Z)+\lambda c,
\]
\[
\langle\alpha,\beta\rangle\alpha+\|\beta\|^2\beta=k(Z).
\tag{NG3}
\]

For every $Z$, this complete fiber is a singleton. To prove this and all coverage claims, first note the global estimates

\[
h(Z)\ge\tfrac18\|Z\|_F^4,
\quad
\langle v(Z+H)-v(Z),H\rangle\ge\tfrac18\|H\|_F^4,
\]
\[
\|Z-Z'\|_F\le2\|v(Z)-v(Z')\|_F^{1/3},\qquad
D_h(Z+H,Z)\ge\tfrac1{32}\|H\|_F^4.
\tag{NG4}
\]

Here $D_h(Y,Z)=h(Y)-h(Z)-\langle v(Z),Y-Z\rangle$. For completeness, the Hessian identity is

\[
D^2h(Z)[H,H]=\tfrac12\|ZH^T+HZ^T\|_F^2+\|Z^TH\|_F^2.
\tag{NG5}
\]

Integrating this identity along $Z+tH$ and centering at $t=1/2$, the two quadratic-in-$t$ terms supply respectively $\|HH^T\|_F^2/6$ and $\|H^TH\|_F^2/12$. All remaining centered squares are nonnegative. Their sum is $\|H^TH\|_F^2/4\ge\|H\|_F^4/8$, because $H$ has two columns. This proves the monotonicity inequality in (NG4), hence strict convexity and the inverse estimate. Applying the same inequality with $tH$, dividing its inner product by $t$, and integrating $t^3/8$ from zero to one proves the displayed Bregman lower bound. The first estimate follows from the two singular values: $\sigma_1^4+\sigma_2^4\ge(\sigma_1^2+\sigma_2^2)^2/2$.

Consequently $h+\lambda f_c-\langle v(Z),\cdot\rangle$ is coercive, strictly convex, and $C^1$. It has exactly one global minimizer and exactly one stationary point. Its first-order equation is precisely (NG3). This proves full input coverage, uniqueness of the complete inverse fiber, and equivalence to the complete Bregman argmin without deleting any nonminimal or remote roots. At a zero input $Z\in S_c$, the comparator $Y=Z$ attains zero in $\lambda f_c(Y)+D_h(Y,Z)$, and strict convexity forces the unique output to be $Z$. Every point of the nonisolated target is therefore absorbing.

The kernel remains non-strongly-convex near $p=[c\ 0]$: for $H=[0\ w]$ with $w\perp c$, (NG5) vanishes at $p$. Thus a positive strong-convexity modulus cannot hold on any neighborhood of this solution.

<a id="native-gram-certificate"></a>
## Complete C249 certificate from primitive constants

Fix $B>0$ and $0<R<\|c\|$. Define the input region and primitive constants

\[
U=\{[a\ b]:\|b\|<B\},\qquad U_R=\{Z\in U:\|a-c\|\le R\},
\]
\[
M^2=(\|c\|+R)^2+B^2,\qquad L=3M^2,\qquad \eta=(\|c\|-R)^2>0.
\tag{NG6}
\]

Choose $\lambda>0$ and $0<\kappa<1$ such that

\[
q_\lambda:=\frac L\lambda+\frac L\eta\sqrt{\frac L\lambda}\le\kappa.
\tag{NG7}
\]

This is a nonempty parameter range because $q_\lambda\to0$ as $\lambda\to\infty$. No output localization is assumed. Every complete output is first obtained globally by (NG3).

For an input $Z\in U_R$, put $d=\|a-c\|$ and use its same physical nearest point $p=p_Z=[c\ b]$. The segment $p+t(Z-p)$ lies in the norm ball of radius $M$. From (NG5),

\[
0\preceq D^2h\preceq3M^2I=LI
\quad\hbox{on that segment},
\]

so

\[
\delta:=\|v(Z)-v(p)\|_F\le Ld,
\qquad D_h(p,Z)\le\tfrac L2d^2.
\tag{NG8}
\]

There is also a lower bound for this *same* kernel increment. Differentiating only the first block while holding $b$ fixed gives

\[
D_a u(a,b)=\|a\|^2I+2aa^T+bb^T.
\]

Every $a_t=c+t(a-c)$ has norm at least $\|c\|-R$. Therefore

\[
\langle v(Z)-v(p),Z-p\rangle
=\langle u(Z)-u(p),a-c\rangle\ge\eta d^2,
\quad\delta\ge\eta d.
\tag{NG9}
\]

For the complete output $Y$, compare its global Bregman objective with $p$. This comparison is legal before showing $Y\in U$ and yields

\[
\tfrac\lambda2\|\alpha-c\|^2+D_h(Y,Z)
\le D_h(p,Z)\le\tfrac L2d^2.
\tag{NG10}
\]

Combining (NG4) and (NG10),

\[
r_{F_c}(Y)=d(Y,S_c)=\|\alpha-c\|
\le\sqrt{L/\lambda}\,d,
\quad
\|Y-Z\|_F\le C_H\sqrt d,
\qquad C_H=(16L)^{1/4}.
\tag{NG11}
\]

These are physical estimates for every full output; neither the step nor the chosen graph value has been substituted for the true residual.

Set the C249 gauges to

\[
a_{\rm sc}(t)=Lt,\qquad
\omega(s)=\Omega s,\qquad
\Omega=1+\frac{2\sqrt{\lambda L}}\eta,
\]
\[
\psi(t)=t,\qquad
\mathfrak h(t,s)=C_H\sqrt t,
\qquad\bar t\ge q_\lambda R.
\tag{NG12}
\]

The physical lifting function $\mathfrak h$ is defined and finite on all $[0,\infty)^2$, nondecreasing in each variable, continuous at $(0,0)$, and zero there. It depends on distance because the objective comparator controls physical motion directly. It is not claimed to be a pure inverse-kernel modulus.

G1 follows from global unique coverage. For G2, (NG8) supplies its first estimate. By the full equation $v(Z)-v(Y)=\lambda F_c(Y)$, (NG9), and (NG11),

\[
\begin{aligned}
\|2v(Y)-v(Z)-v(p)\|_F
&=\|v(Z)-v(p)-2\lambda F_c(Y)\|_F\\
&\le\delta+2\sqrt{\lambda L}\,d
\le\Omega\delta.
\end{aligned}
\tag{NG13}
\]

Thus the *physical input nearest point* supplies both anchor estimates. G3 is (NG11). G4 is the global identity $d(Y,S_c)=r_{F_c}(Y)$ together with the output evaluation-window bound below. The C249 scalar quantities are

\[
K(t)=\tfrac{a_{\rm sc}(t)+\omega(a_{\rm sc}(t))}{2}
=L\left(1+\frac{\sqrt{\lambda L}}\eta\right)t,
\quad K(t)/\lambda=q_\lambda t,
\]
\[
H(t)=C_H\sqrt t,\qquad
\Theta(t)=\frac{C_H\sqrt t}{1-\sqrt\kappa}.
\tag{NG14}
\]

Hence $K(R)/\lambda=q_\lambda R\le\bar t$, $\psi(K(t)/\lambda)\le\kappa t$ for every $0<t\le R$, and $\Theta(R)<\infty$. G5 is proved, including its entire scalar domain.

The exact localization budget is

\[
\frac{C_H\sqrt{d_0}}{1-\sqrt\kappa}<B-\|b_0\|
=d(Z_0,X\setminus U).
\tag{NG15}
\]

For every input in $U_R$ satisfying (NG15), C249 proves every finite prefix stays in $U_R$, infinite continuation is available, and the complete trajectory converges with finite length to some $Z_\infty\in S_c\cap U$. It gives

\[
d(Z_k,S_c)\le\kappa^k d_0,
\qquad
\sum_{j\ge k}\|Z_{j+1}-Z_j\|_F
\le\frac{C_H\sqrt{d_0}\,\kappa^{k/2}}{1-\sqrt\kappa}.
\tag{NG16}
\]

No claim is made that every input near the boundary $\|b\|=B$ satisfies this budget.

A concrete group, common to every dimension $m\ge2$ and every unit data vector $c$, is

\[
B=1,\quad R=10^{-8},\quad \lambda=10^4,\quad
\kappa=\tfrac14,\quad\bar t=1,
\]
\[
L=3[(1+10^{-8})^2+1],\quad\eta=(1-10^{-8})^2,
\quad q_\lambda<0.148<\tfrac14,
\quad\Theta(R)<0.000627.
\tag{NG17}
\]

In particular, all initial states with $\|a_0-c\|\le10^{-8}$ and $\|b_0\|\le1/2$ satisfy the strict budget. The rate in (NG16) is a certified upper bound, not an exact asymptotic order of all trajectories.

<a id="native-gram-exponent"></a>
## Sharp pointwise exponent at every true solution $[c\ 0]$

Fix any $c\ne0$ and any $\lambda>0$, and let $p=[c\ 0]$. The complete map $T=J^v_{\lambda F_c}$ fixes $p$. There exist a radius $\varepsilon_0>0$ and a finite $C_0>0$, depending on $c,\lambda$, such that

\[
\boxed{\|T(Z)-p\|_F\le C_0\|Z-p\|_F^{2/3}
\quad(\|Z-p\|_F\le\varepsilon_0).}
\tag{NG18}
\]

This is an all-input bound with one fixed solution anchor. It is not asserted to be a two-input Hölder bound, a constant uniform over the noncompact target, or an optimal full-orbit rate.

To prove (NG18), put $\varepsilon=\|Z-p\|_F$, so $\|a-c\|,\|b\|\le\varepsilon$. Global uniform monotonicity of $v+\lambda F_c$ gives

\[
\|T(Z)-T(Z')\|_F\le2\|v(Z)-v(Z')\|_F^{1/3},
\]

by exactly the argument for (NG4), since $F_c$ is monotone. Thus $Y=T(Z)=[\alpha\ \beta]\to p$ as $Z\to p$. In particular, choose the input radius small enough that $\|\alpha\|\ge\|c\|/2$ and $\|\beta\|\le1$. The comparator (NG10), with a fixed finite bound on the input/comparator segments, proves $\|\alpha-c\|=O(\varepsilon)$ uniformly over every such input.

Write $n=c/\|c\|$ and use $w_\perp=(I-nn^T)w$. The conserved input block satisfies

\[
\|k(Z)\|=O(\varepsilon),\qquad
\|k(Z)_\perp\|=O(\varepsilon^2),
\]

because $k(Z)=\langle a,b\rangle a+\|b\|^2b$ and $a_\perp=(a-c)_\perp=O(\varepsilon)$. Let $s=\langle\alpha,\beta\rangle$. Taking the inner product of the second equation of (NG3) with $\alpha$ gives the exact identity

\[
s=\frac{\langle\alpha,k(Z)\rangle}{\|\alpha\|^2+\|\beta\|^2}
=O(\varepsilon).
\tag{NG19}
\]

Its perpendicular projection then gives

\[
\|\beta\|^2\|\beta_\perp\|
\le\|k(Z)_\perp\|+|s|\|\alpha_\perp\|
=O(\varepsilon^2),
\]

so $\|\beta_\perp\|\le O(\varepsilon^{2/3})$. Finally

\[
\langle n,\beta\rangle
=\frac{s-\langle\alpha_\perp,\beta_\perp\rangle}
{\langle n,\alpha\rangle}=O(\varepsilon),
\]

because $\langle n,\alpha\rangle\to\|c\|>0$. These uniform estimates prove (NG18), including $\varepsilon=0$ by zero-input absorption.

The exponent $2/3$ is optimal and calmness fails at this exact solution for every fixed $\lambda>0$. To see this, choose a unit $n=c/\|c\|$, a unit $w\perp n$, and put $C=\|c\|$ and

\[
Z_t=[C n+t w\quad t n],\qquad t\downarrow0.
\tag{NG20}
\]

Its two kernel blocks are

\[
u_t=(C^3+2Ct^2)n+(C^2t+t^3)w,
\qquad
k_t=(C^2t+t^3)n+Ct^2w.
\tag{NG21}
\]

The unique complete output stays in $\operatorname{span}\{n,w\}$: orthogonal transformations fixing this plane preserve the objective and input, so uniqueness forces invariance. Write

\[
\alpha=A n+E w,\qquad \beta=B n+D w,
\qquad s=AB+ED.
\]

Continuity gives $A\to C$, $E,B,D\to0$; the comparator gives $A-C,E=O(t)$. Formula (NG19) and (NG21) give $s/t\to C$. The identities

\[
B=(s-ED)/A,
\qquad E=(C^2t+t^3-sD)/(\|\alpha\|^2+\lambda)
\]

therefore imply $B/t\to1$ and $E/t\to C^2/(C^2+\lambda)$. The perpendicular conserved-block equation is

\[
(B^2+D^2)D=Ct^2-sE
=\left[\frac{C\lambda}{C^2+\lambda}+o(1)\right]t^2.
\tag{NG22}
\]

Its right side is positive for small $t$, so $D>0$ then. Since $B=O(t)$, (NG22) implies $D=O(t^{2/3})$ and $B^2D/t^2\to0$. Consequently

\[
\boxed{\frac D{t^{2/3}}\longrightarrow
\left(\frac{C\lambda}{C^2+\lambda}\right)^{1/3}>0.}
\tag{NG23}
\]

The first component of the first equation in (NG3) also gives

\[
A^3-C^3+\lambda(A-C)=2Ct^2-AE^2-sB=O(t^2),
\]

hence $A-C=O(t^2)$. Thus

\[
\|T(Z_t)-p\|_F\sim\|T(Z_t)-Z_t\|_F
\sim\left(\frac{C\lambda}{C^2+\lambda}\right)^{1/3}t^{2/3},
\qquad \|Z_t-p\|_F=\sqrt2t.
\tag{NG24}
\]

Every pointwise exponent greater than $2/3$ fails by (NG24). Together with (NG18), this proves the exact pointwise exponent $2/3$ and excludes solution-point calmness.

<a id="native-gram-h1"></a>
## Exact original-objective H1 obstruction

Along the same family,

\[
f_c(Z_t)-f_c(T(Z_t))
\sim\tfrac12\left[1-\left(\frac{C^2}{C^2+\lambda}\right)^2\right]t^2,
\]

while the physical step squared is asymptotic to

\[
\left(\frac{C\lambda}{C^2+\lambda}\right)^{2/3}t^{4/3}.
\]

Therefore

\[
\frac{f_c(Z_t)-f_c(T(Z_t))}{\|T(Z_t)-Z_t\|_F^2}\longrightarrow0.
\tag{NG25}
\]

For every neighborhood of $p$, there is no positive constant $a$ such that the original objective satisfies the uniform all-input Euclidean sufficient-decrease contract

\[
f_c(Z)-f_c(T(Z))\ge a\|T(Z)-Z\|_F^2
\]

throughout that neighborhood. This is exactly a failure of this particular natural H1 contract. It does not prove that a given individual orbit lacks an eventual orbit-dependent constant, does not exclude an alternative energy, and does not exclude all classical convergence analysis.

<a id="native-gram-classical"></a>
## Same-algorithm classical global positive: required comparison

In fact, the same native nonzero-data algorithm has a short global convergence proof for every $\lambda>0$. It is stronger in domain and parameter scope than the local C249 certificate. The second block $k_0=k(Z_0)$ is conserved. There is a unique $b_*$ solving

\[
cc^Tb_*+\|b_*\|^2b_*=k_0;
\tag{NG26}
\]

it is the unique minimizer of the coercive strictly convex function $\|b\|^4/4+\langle c,b\rangle^2/2-\langle k_0,b\rangle$. Define

\[
Z_*=[c\ b_*],\quad u_*=\|c\|^2c+\langle c,b_*\rangle b_*,
\quad D_0=\|u(Z_0)-u_*\|.
\]

For each complete step, monotonicity of $v$ between $Z_{k+1}$ and $Z_*$ and the common second block give

\[
\langle u_{k+1}-u_*,a_{k+1}-c\rangle\ge0,
\qquad u_k=u_{k+1}+\lambda(a_{k+1}-c).
\]

Expanding the square proves $\|u_k-u_*\|\le D_0$ for every prefix. Define

\[
Q=\sqrt{(\|u_*\|+D_0)^2+\|k_0\|^2},
\quad M_*=(2Q)^{1/3},\quad L_*=3M_*^2.
\]

The inequality $\|Z\|_F^3\le2\|v(Z)\|_F$ shows every $Z_k$ and $Z_*$ is in the ball of radius $M_*$. Here $Q>0$ since $c\ne0$. On every segment joining such points, the Hessian in (NG5) is PSD and bounded by $L_*I$. Its secant matrix $A=\int_0^1D^2h\,dt$ therefore satisfies $A^2\preceq L_*A$, proving the elementary cocoercivity estimate

\[
\|v(Z)-v(Z_*)\|_F^2
\le L_*\langle v(Z)-v(Z_*),Z-Z_*\rangle.
\]

Since the second kernel blocks agree, this gives

\[
\langle u_{k+1}-u_*,a_{k+1}-c\rangle
\ge\frac1{L_*}\|u_{k+1}-u_*\|^2.
\]

Taking the inner product of the update with $u_{k+1}-u_*$ and applying Cauchy yields

\[
\|u_{k+1}-u_*\|\le\rho\|u_k-u_*\|,
\quad\rho=\frac{L_*}{L_*+\lambda}<1.
\tag{NG27}
\]

Using the global physical inverse estimate (NG4),

\[
\|Z_k-Z_*\|_F\le2D_0^{1/3}\rho^{k/3},
\qquad
\sum_{k\ge0}\|Z_{k+1}-Z_k\|_F
\le\frac{2[(1+\rho)D_0]^{1/3}}{1-\rho^{1/3}}.
\tag{NG28}
\]

If $D_0=0$, the complete trajectory is already stationary. Thus every initial input and every fixed positive step size has a full finite-length trajectory converging to the explicit uniquely selected zero (NG26). Constants depend on the initial kernel slice; no global uniform factor on the noncompact target is claimed. This proof uses a fixed slice zero $Z_*$, never substitutes it for the *input physical nearest point* in the C249 proof.

<a id="native-gram-eventual"></a>
## Stronger ABS limitation: eventual constants exist on every individual orbit

The neighborhood obstruction (NG25) should not be promoted to an exclusion of orbit-specific original-objective ABS analysis. Indeed, every trajectory from (NG28) has eventual original-$f_c$ H1 and H2 constants, although they need not be uniform over all inputs near $[c\ 0]$.

First, $k(Z_0)=0$ if and only if $b_0=0$, because

\[
\langle k(Z_0),b_0\rangle=\langle a_0,b_0\rangle^2+\|b_0\|^4.
\]

Equation (NG26) shows that $b_*=0$ if and only if $k_0=0$. Thus a trajectory converging to $[c\ 0]$ starts with $b_0=0$ and stays in the invariant subspace $b=0$. On that subspace, the complete update is the smooth equation

\[
\|\alpha\|^2\alpha+\lambda(\alpha-c)=\|a\|^2a.
\]

Its normal derivative at $a=c$ is $(A+\lambda I)^{-1}A$, with $A=\|c\|^2I+2cc^T\succ0$, hence has norm strictly below one. Local original-objective quadratic H1 and relative-error H2 follow as below.

If $b_*\ne0$, write the Hessian of $h$ at $[c\ b_*]$ in blocks $H_{aa},H_{ab},H_{ba},H_{bb}$. The formula for its second diagonal block is

\[
H_{bb}=\|b_*\|^2I+2b_*b_*^T+cc^T\succ0.
\]

The Hessian of $h+\lambda f_c$ is positive definite: if its quadratic form is zero, the $\lambda\|\Delta a\|^2$ term forces $\Delta a=0$, and then $H_{bb}$ forces $\Delta b=0$. The implicit function theorem makes the complete update smooth near this stationary input. Its normal derivatives there are

\[
D_a\alpha=(S+\lambda I)^{-1}S,\qquad D_b\alpha=0,
\quad S=H_{aa}-H_{ab}H_{bb}^{-1}H_{ba}\succeq0.
\]

The Schur complement $S$ is symmetric PSD since $D^2h$ is PSD. Thus $\|D_a\alpha\|<1$. Continuity of the derivative and the identities $T([c\ b])=[c\ b]$ provide constants $r<1$, $K<\infty$, and a small neighborhood of $[c\ b_*]$ such that every input there obeys

\[
\|\alpha-c\|\le r\|a-c\|,\qquad
\|T(Z)-Z\|_F\le K\|a-c\|.
\]

These estimates hold on the invariant subspace near $[c\ 0]$ in the first case. For a nonzero physical step, they give

\[
f_c(Z)-f_c(T(Z))\ge\frac{1-r^2}{2K^2}\|T(Z)-Z\|_F^2,
\]
\[
\|\nabla f_c(T(Z))\|_F\le\frac r{1-r}\|T(Z)-Z\|_F.
\]

The second inequality uses $\|T(Z)-Z\|_F\ge\|a-\alpha\|\ge(1-r)\|a-c\|$. Zero steps satisfy both trivially. The global convergence proved in (NG28) puts every fixed trajectory eventually in its applicable neighborhood or invariant-subspace neighborhood. The original quadratic objective also has the usual exact KL exponent $1/2$. Thus the obstruction is a uniform *full-neighborhood* contract at the flat solution; eventual constants can depend on the individual limiting slice.

<a id="native-gram-scope"></a>
## Identity, novelty, and evidence limits

Compared with C270-v1, the objective and zero set change from $a=0$ to $a=c\ne0$ while the native kernel remains at its original center. This changes the sharp *fixed-solution* pointwise behavior: C270 is calm at its kernel-origin solution, whereas (NG18)–(NG24) give a true solution-point exponent $2/3$ here. Equation (NG25) also differs from the original-f ABS positive recorded for C270's specified window. The target is affine and nonisolated, the optimization source is a raw nonzero-data regression, all complete roots are retained, and the physical movement is analytically lifted from raw convexity estimates.

The valid contribution is a structural native-data extension and an exact failure boundary for solution calmness and original-objective uniform Euclidean H1. It is not evidence that RLEB is necessary for convergence or that every old analysis fails: (NG26)–(NG28) and the eventual orbit-specific ABS constants are explicit counterweights. Public priority has not been established by a literature search.

Primary papers inspected for comparison background are BSTV arXiv:1706.06461v1 and Bùi–Combettes's author PDF `https://pcombet.math.ncsu.edu/jmaa5.pdf`. No external theorem is imported into the above proof; all mathematical estimates are reconstructed from the model. The numerical constants in (NG17) were checked with Python only as arithmetic verification; all full-input, full-output, optimal-exponent, and localization quantifiers rest on the proofs above.


复算与精度见 [代码](../code/structural_verification/README.md)，实际正文的独立核查见 [接收记录](../audit/STRUCTURAL_VERIFICATION_REVIEW_2026_10_13.md)。本证明不把解点指数当作所有轨道的精确收敛率，也不替代零数据 C270 的对象。
