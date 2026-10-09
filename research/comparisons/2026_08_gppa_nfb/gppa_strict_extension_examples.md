# General-kernel RL + true-residual EB: strict full-graph witnesses and the ASM inclusion boundary

Independent derivation, 2026-10-09. This page supplies explicit witnesses for the general-kernel extension; it does not alter the existing C199–C207 identities. The comparison is with the fixed [GPPA 2608.01584v1](sources/gppa_2608.01584v1.pdf), Definition 1 p.4, Definitions 3–5 p.5, Theorem 1 p.6 and Theorem 2 pp.7–8. The source permits arbitrary single-valued full-domain kernels, including nonmonotone and noninjective ones. Requiring the kernel itself to be monotone is an additional restriction, not a source hypothesis.

The claims below concern the **same complete relation and the same specified generalized trajectory**. A kernel exclusion means that no source pair-monotone kernel can generate that trajectory on that complete relation. It does not mean that the relation has no admissible kernel: constant kernels remain possible. Nor does it exclude the proved zero-set-preserving branch restrictions in [sol61_branch_restriction.md](sol61_branch_restriction.md).

## 1. Exact conjugation, with graph values and true residual preserved

Let \(G:\mathbb R^n\rightrightarrows\mathbb R^n\), let \(V:\mathbb R^n\to\mathbb R^n\) be a homeomorphism, and set

\[
F^V(x)=G(Vx),\qquad S^V=V^{-1}(S_G),\qquad S_G=G^{-1}(0).
\tag{SE1}
\]

No Jacobian, transpose, or dual-coordinate transformation is applied to graph values. This choice is material: it makes the update equation exactly conjugate. For every \(h>0\), every input \(x\), and every output \(u\),

\[
Vx-Vu\in hF^V(u)
\quad\Longleftrightarrow\quad
Vx-Vu\in hG(Vu).
\]

Consequently the **complete fibers**, including every output on every graph branch, satisfy

\[
J^{V}_{hF^V}(x)=V^{-1}\bigl(J_{hG}(Vx)\bigr).
\tag{SE2}
\]

Thus full-domain coverage, uniqueness, and trajectory identity transfer without a selection argument. If \(z_{k+1}=J_{hG}z_k\), then the corresponding generalized trajectory is exactly \(x_k=V^{-1}z_k\).

For graph points \((x,f),(u,g)\), the kernel-input and kernel-reflection differences are

\[
\Delta_+=Vx-Vu+h(f-g),\qquad
\Delta_-=Vx-Vu-h(f-g).
\]

They are the ordinary Minty differences of \((Vx,f),(Vu,g)\in\operatorname{gph}G\). Therefore an all-pairs general modulus

\[
\|\Delta_-\|\le\omega(\|\Delta_+\|)
\tag{SE3}
\]

transfers with the **same** modulus and comparison scale, on the full graph or the exactly corresponding graph block. In particular, zero-input pairs and cross-branch pairs remain in the quantifier.

Define the kernel distance

\[
D_V(x)=d(Vx,S_G)=d(Vx,V(S^V)).
\]

The genuine complete residual is preserved exactly:

\[
r_{F^V}(x)=\inf_{f\in F^V(x)}\|f\|=r_G(Vx).
\tag{SE4}
\]

Hence \(d(z,S_G)\le\psi(r_G(z))\) gives \(D_V(x)\le\psi(r_{F^V}(x))\), with the same residual window. It is never necessary to replace the complete infimum by the selected graph value. The selected value gives only \(r_{F^V}(x_{k+1})\le\|Vx_k-Vx_{k+1}\|/h\).

If \(V^{-1}\) is \(L_-\)-Lipschitz, then

\[
d(x,S^V)\le L_-D_V(x),\qquad
\|x_{k+1}-x_k\|\le L_-\|z_{k+1}-z_k\|.
\tag{SE5}
\]

Kernel finite length and point convergence therefore give physical finite length and point convergence. A continuous general inverse modulus \(\rho\) can replace the Lipschitz bound, but the physical length conclusion then requires summability of the transformed step bounds, not merely \(\rho(t)\to0\).

The nearest zero anchor is chosen in the kernel image: if \(p\in P_{S_G}(Vx)\), use \(s=V^{-1}p\). It need not be a nearest zero in physical coordinates. Conflating these anchors changes the constants and can invalidate direct compatibility.

## 2. Explicit nonlinear kernels, both strongly monotone and nonmonotone

Fix

\[
b>0,\quad 0<c<1,\quad \sigma\in\{+1,-1\},\qquad
g_b(y)=y+b\tanh y,\quad \varphi_b=g_b^{-1}.
\]

The function \(g_b\) is odd, onto, smooth, and has derivative in \([1,1+b]\). Thus \(\varphi_b\) is globally 1-Lipschitz, odd, strictly increasing, and

\[
\varphi_b(t)\sim\frac{t}{1+b}\quad(t\to0).
\tag{SE6}
\]

In \(\mathbb R^3\), define

\[
V_{\sigma,b,c}(\xi,\eta,y)
=(\sigma\xi+c\sin y,\eta,g_b(y)).
\tag{SE7}
\]

For the two-dimensional log model omit \(\eta\). The explicit inverse is

\[
V_{\sigma,b,c}^{-1}(z_1,z_2,r)
=\bigl(\sigma[z_1-c\sin\varphi_b(r)],z_2,\varphi_b(r)\bigr).
\tag{SE8}
\]

The triangle inequality gives global Lipschitz constants

\[
\operatorname{Lip}(V)\le1+b+c,\qquad
\operatorname{Lip}(V^{-1})\le1+c.
\tag{SE9}
\]

For \(\sigma=+1\), writing physical differences as \((d_1,d_2,d_3)\),

\[
\langle\Delta V,\Delta x\rangle
=d_1^2+d_2^2+d_3\Delta g_b+c d_1\Delta\sin y
\ge(1-c/2)\|\Delta x\|^2.
\tag{SE10}
\]

Here \(d_3\Delta g_b\ge d_3^2\), \(|\Delta\sin y|\le|d_3|\), and \(|d_1d_3|\le(d_1^2+d_3^2)/2\). This is a globally strongly monotone, genuinely nonlinear, invertible kernel. For \(\sigma=-1\), two points differing only in their first coordinate have pairing \(-d_1^2<0\), so the equally nonlinear invertible kernel is nonmonotone. Both kernels satisfy the same exact conjugation proof. Thus the witnesses remain available if one voluntarily restricts to strongly monotone kernels, but monotonicity is not necessary for this extension.

For every model below, \(S_G=\mathbb R^{n-1}\times\{0\}\), and

\[
S^V=S_G,\quad V(S^V)=S_G,\quad
D_V(\xi,\eta,y)=|g_b(y)|,\quad
d((\xi,\eta,y),S^V)=\varphi_b(D_V(x)).
\tag{SE11}
\]

The exact kernel nearest zero is \((\sigma\xi+c\sin y,\eta,0)\). Its physical preimage is \((\xi+\sigma c\sin y,\eta,0)\). The physical EB gauge can be taken to be \(\varphi_b\circ\psi\), and also the larger \(\psi\), since \(\varphi_b(t)\le t\) for \(t\ge0\). The graph itself is genuinely transformed through its normal coordinate \(g_b(y)\), rather than merely changing a graph-invariant tangential coordinate.

In the team's [kernel theorem](gppa_nonlinear_kernel_theorem.md), the complete union relation is exactly \(A(z)=G(z)\), because \(V\) is bijective; hence its full-union residual equals the physical residual in (SE4). In the separate [physical-transfer theorem](gppa_physical_transfer.md), use the exact forward zero-distance modulus \(\sigma_0(t)=g_b(t)\), the physical gauge \(\psi_{\rm phys}=\varphi_b\circ\psi\), and inverse modulus \(\eta(t)=(1+c)t\). Then \(\sigma_0\circ\psi_{\rm phys}=\psi\) exactly. This mapping preserves the strict critical cap compatibility constant; replacing it by the coarser global forward Lipschitz constant would unnecessarily weaken that certificate.

## 3. Full cap graph: a critical-exponent witness with strict compatibility

Let \(G\) be the complete [C137 cap graph](../../canonical/selection_geometric_cap.md#gc-object). To make the transformed relation explicit, put \(t=g_b(y)\) and, for \(t\ge0\),

\[
D_t(\eta)=\min\left\{2\sqrt t,
\frac{\sqrt{1+4\eta_+}-1}{2}\right\}.
\]

Then, for either sign \(\sigma\),

\[
F^V(\xi,\eta,y)=
\begin{cases}
\{(-2\sqrt t,-D_t(\eta),3t),
(-2\sqrt t,-D_t(\eta),-5t)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}
\tag{SE12}
\]

It is a closed complete two-branch relation; its whole zero set is the plane in (SE11). Choose generalized step \(h=1\). For an arbitrary physical input \((\xi,\eta,y)\), put \(r=g_b(y)\) and

\[
y^+=\varphi_b(|r|/4),\quad
\eta^+=\eta+\sqrt{\min\{\eta_+,|r|\}},
\]
\[
\xi^+=\xi+\sigma\left[\sqrt{|r|}
+c(\sin y-\sin y^+)\right].
\tag{SE13}
\]

These are the **only** generalized outputs, by (SE2) and the complete cap inversion. Negative inputs select the complete negative normal branch; zero inputs have the stationary output. No branch is deleted.

On every fixed kernel-input comparison scale \(R>0\), the all-pairs modulus is

\[
\omega_R(s)=L_R\sqrt s,\qquad L_R=2\sqrt2+\tfrac32\sqrt R.
\tag{SE14}
\]

This includes both graph branches. The exact full residual at a graph point is

\[
r_{F^V}(\xi,\eta,y)^2
=4t+D_t(\eta)^2+9t^2,
\quad D_V(x)=t\le\frac14 r_{F^V}(x)^2.
\tag{SE15}
\]

Although a negative input selects the graph value with normal coordinate \(-5t\), the complete residual uses the smaller \(3t\) branch. The formula retains this distinction.

Take \(U=\mathbb R^3\), \(0<R<[2(4-2\sqrt2)/5]^2\), and \(\bar t\ge(R+L_R\sqrt R)/2\). All input fibers and all zero anchors are covered, the EB is global, every gauge evaluation lies in its declared window, and the kernel collar \(D_V\le R\) is invariant. Direct compatibility is

\[
\sup_{0<s\le R}\frac{\psi((s+\omega_R(s))/2)}s
=\frac{(\sqrt R+L_R)^2}{16}<1,
\quad\psi(t)=t^2/4.
\tag{SE16}
\]

The Dini condition is immediate. Thus the exact generalized general-modulus hypotheses hold. Here the EB exponent is \(q=2\), the RL exponent is \(\gamma=1/2\), and \(q\gamma=1\): supercriticality is not necessary when the critical coefficient is strictly favorable.

For \(\eta_0\le0,r_0=g_b(y_0)>0\), the kernel normal coordinate is \(r_k=4^{-k}r_0\), the second coordinate is constant, and the kernel tangential tail is \(2\sqrt{r_k}\). From (SE8), the physical error is exactly

\[
e_k^2=
\left[2\sqrt{r_k}+c\sin\varphi_b(r_k)\right]^2
+\varphi_b(r_k)^2.
\]

It follows that \(e_k\sim2\sqrt{r_k}\) and \(e_{k+1}/e_k\to1/2\). This positive convergence witness has geometric, rather than superlinear, physical convergence.

## 4. Full superlinear family: every exact physical order \(\nu>1\), including \(\nu>2\)

Fix \(0<\gamma<1\), \(\nu>1\), and \(A,B>0\). For \(a\ge0\), define

\[
H_a(p)=p+B\min\{p_+,a\}^{\gamma},\qquad \tau_a=H_a^{-1}.
\]

Use the complete [C141 relation](../../canonical/selection_superlinear_family.md#sf-object). Its transformed form, with \(t=g_b(y)\), \(a=t^{1/\nu}\), is

\[
F^V(\xi,\eta,y)=
\begin{cases}
\{(-Aa^\gamma,\tau_a(\eta)-\eta,a-t),
(-Aa^\gamma,\tau_a(\eta)-\eta,-a-t)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}
\tag{SE17}
\]

Both values remain present at every positive height. The complete generalized output at step 1 is

\[
r=g_b(y),\quad y^+=\varphi_b(|r|^\nu),\quad
\eta^+=\eta+B\min\{\eta_+,|r|\}^\gamma,
\]
\[
\xi^+=\xi+\sigma\left[A|r|^\gamma
+c(\sin y-\sin y^+)\right].
\tag{SE18}
\]

Fix \(0<R_0<1\) and the full output graph block \(0\le g_b(y)\le R_0^\nu\), including both branches and all tangential coordinates. Its kernel-input domain is exactly \(\mathbb R^2\times[-R_0,R_0]\). On this collar and comparison scale \(R\le R_0\), the transferred all-pairs modulus is

\[
\omega_R(s)=L_Rs^\gamma,
\quad L_R=2\sqrt{A^2+B^2}
+(1+2\nu R_0^{\nu-1})R^{1-\gamma}.
\tag{SE19}
\]

On the graph domain \(y\ge0\), the complete residual satisfies

\[
r_{F^V}(x)^2
=A^2a^{2\gamma}+(\tau_a(\eta)-\eta)^2+(a-t)^2,
\]
\[
D_V(x)=t\le(r_{F^V}(x)/A)^{\nu/\gamma}.
\tag{SE20}
\]

The identity uses the minimum normal absolute value \(|a-t|\); it is not restricted to the chosen branch. Put \(\psi(s)=(s/A)^{\nu/\gamma}\). For \(0<s\le R\), direct compatibility has the uniform bound

\[
\frac{\psi((s+\omega_R(s))/2)}s
\le R^{\nu-1}
\left(\frac{R^{1-\gamma}+L_R}{2A}\right)^{\nu/\gamma}
\longrightarrow0\quad(R\downarrow0).
\tag{SE21}
\]

Choose a fixed sufficiently small \(R\), a fixed \(\kappa\in(0,1)\) above that bound, and \(\bar t\ge(R+L_RR^\gamma)/2\). Coverage, zero anchors, full-fiber equality on the input collar, residual window, compatibility and Dini all hold on this same object. The whole-space open-domain budget is automatic, and (SE18) independently verifies forward invariance. Here \(q=\nu/\gamma\), so \(q\gamma=\nu>1\).

The exact physical order requires a separate calculation; it is not obtained by changing the name of a distance estimate. Choose \(\eta_0\le0\) and \(0<r_0=g_b(y_0)<1\). Then \(\eta_k=\eta_0\), \(r_k=r_0^{\nu^k}\). Define

\[
E(r)=\sum_{j\ge0}r^{\gamma\nu^j},\qquad 0\le r<1.
\]

Since \(\nu^j\ge1+j(\nu-1)\),

\[
r^\gamma\le E(r)
\le\frac{r^\gamma}{1-r^{\gamma(\nu-1)}};
\quad E(r)\sim r^\gamma\quad(r\downarrow0).
\tag{SE22}
\]

The kernel tangential error is \(A E(r_k)\). In physical coordinates,

\[
e_k^2=
\left[A E(r_k)+c\sin\varphi_b(r_k)\right]^2
+\varphi_b(r_k)^2.
\tag{SE23}
\]

By \(0<\gamma<1\) and (SE6), the sine and normal terms are \(o(r_k^\gamma)\). Thus

\[
e_k\sim A r_k^\gamma,
\qquad
\boxed{\lim_{k\to\infty}\frac{e_{k+1}}{e_k^\nu}=A^{1-\nu}.}
\tag{SE24}
\]

This is exact Q-\(\nu\) convergence for every \(\nu>1\); taking \(\nu>2\) gives an actual order above quadratic. It is an existential family with the indicated parameters and initialization. It does not imply that every operator satisfying general-modulus RL + EB has arbitrarily large order, that order is independent of EB growth, or that the source framework cannot prove convergence of a suitable restriction. For instance \(\nu=3,\gamma=1/2,A=B=1\) gives a cubic physical witness and EB exponent \(q=6\).

## 5. Full logarithmic family: nonpower Dini convergence and its exact failure boundary

Fix \(a>0\), let \(r_a=e^{-a}\), and use the complete concave profile from [GM26](../../canonical/general_modulus_dynamics.md#gm-log-object):

\[
\ell_a(0)=0,\quad
\ell_a(t)=[\log(e/t)]^{-a}\ (0<t\le r_a),
\quad
\ell_a(t)=\frac{1+a e^a t}{(a+1)^{a+1}}\ (t\ge r_a).
\tag{SE25}
\]

The second formula is the tangent continuation and is essential to global concavity and subadditivity. In two dimensions, with \(t=g_b(y)\), the transformed complete graph is

\[
F^V(\xi,y)=
\begin{cases}
\{(-\ell_a(4t),3t),(-\ell_a(4t),-5t)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}
\tag{SE26}
\]

Its unique complete generalized output is

\[
r=g_b(y),\quad y^+=\varphi_b(|r|/4),\quad
\xi^+=\xi+\sigma\left[\ell_a(|r|)
+c(\sin y-\sin y^+)\right].
\tag{SE27}
\]

The global all-pairs kernel modulus is the displayed \(\Omega_a\). On the graph domain \(y\ge0\), the true residual and exact kernel EB are

\[
\Omega_a(s)=\sqrt{(s+2\ell_a(s))^2+\tfrac94s^2},
\]
\[
r_{F^V}(\xi,y)=\chi_a(t)
:=\sqrt{\ell_a(4t)^2+9t^2},
\quad \psi_a=\chi_a^{-1},
\quad D_V(x)=\psi_a(r_{F^V}(x)).
\tag{SE28}
\]

For \(y<0\), the full physical fiber is empty and its residual is \(+\infty\); \(\chi_a\) is not evaluated at negative \(t\), and the finite gauge \(\psi_a\) is not evaluated at \(+\infty\).

The physical exact gauge is \(\varphi_b\circ\psi_a\). The negative selected branch again has a larger normal graph value without changing the true infimum. Since \(\Omega_a(s)\sim2\ell_a(s)\), it has no positive-power upper bound at zero. Moreover input pairs \((0,s),(0,0)\) in kernel coordinates have reflected tangential difference \(2\ell_a(s)\), so this failure is intrinsic to the full graph, not just a loose proposed modulus.

The Dini calculation gives

\[
\int_0^{r_a}\frac{\ell_a(s)}s\,ds
=\int_{a+1}^{\infty}u^{-a}\,du<\infty
\quad\Longleftrightarrow\quad a>1.
\tag{SE29}
\]

For completeness, direct compatibility is genuinely valid on a fixed small interval: for any \(\kappa\in(1/4,1)\), put \(d=4\kappa>1\). For small \(s\), with \(L=\log(e/s)\),

\[
\ell_a(ds)-\ell_a(s)
=a\int_{L-\log d}^{L}u^{-a-1}\,du
\ge a\log d\,L^{-a-1}.
\tag{SE30}
\]

On the other hand \(\sqrt{A^2+B^2}\le A+B^2/(2A)\) for \(A>0\) gives

\[
\frac{s+\Omega_a(s)}2
\le\ell_a(s)+s+\frac{9s^2}{16[s+2\ell_a(s)]}.
\tag{SE31}
\]

The excess on the right over \(\ell_a(s)\) is \(O(s)\), hence smaller than the lower bound in (SE30) for all sufficiently small \(s\). Therefore

\[
\frac{s+\Omega_a(s)}2\le\ell_a(4\kappa s)
\le\chi_a(\kappa s),\qquad
\psi_a((s+\Omega_a(s))/2)\le\kappa s.
\tag{SE32}
\]

Choose one such fixed radius \(R\), and \(\bar t\ge(R+\Omega_a(R))/2\). All coverage, zero-anchor and evaluation-window gates hold globally; for \(a>1\), Dini closes the exact extended hypotheses and (SE5) transfers finite length to physical coordinates.

For \(r_0=g_b(y_0)>0\), \(r_k=4^{-k}r_0\). After the finite tangent-continuation prefix, the increments are \([\log(e/r_0)+k\log4]^{-a}\). For \(a>1\), integral comparison yields the kernel tail

\[
E_a(r_k)=\sum_{j\ge0}\ell_a(4^{-j}r_k)
\sim\frac{[\log(e/r_0)+k\log4]^{1-a}}{(a-1)\log4}.
\tag{SE33}
\]

The physical error has squared form \([E_a(r_k)+c\sin\varphi_b(r_k)]^2+\varphi_b(r_k)^2\), so it has the same asymptotic. This is a nongeometric point tail with summable **steps**. The point tail itself is not summable when \(1<a\le2\). For \(0<a\le1\), the positive tangential series diverges; the bounded sine correction cannot prevent physical divergence, although \(d(x_k,S^V)=\varphi_b(r_k)\to0\) geometrically. Those parameters fail the Dini hypothesis and are not positive strict-extension convergence witnesses.

## 6. Why every source pair-monotone kernel fails for these complete generalized trajectories

Let \(K:\mathbb R^n\to\mathbb R^n\) be any single-valued kernel, with no continuity, measurability, boundedness or injectivity assumption. Suppose \((F^V,K)\) is pair monotone on the **entire complete graph**. Define

\[
Q(z)=K(V^{-1}z).
\tag{SE34}
\]

For all \((z,f),(w,g)\in\operatorname{gph}G\), (SE1) gives

\[
\langle f-g,Q(z)-Q(w)\rangle\ge0.
\tag{SE35}
\]

Thus \((G,Q)\) is pair monotone with exactly the source's all-pairs quantifier. If the conjugated physical sequence also satisfied a GPPA update with \(K\), arbitrary positive steps \(h_k\), and arbitrary branch choices, then

\[
Q(z_k)-Q(z_{k+1})\in h_kG(z_{k+1}).
\tag{SE36}
\]

The no-regularity scalar dual-branch proof is included here to make the exclusion self-contained. On a tangential product slice \(W\times I\), suppose the complete graph values are

\[
(-C\phi(y),0,a_+(y)),\qquad
(-C\phi(y),0,a_-(y)),
\tag{SE37}
\]

where \(C>0\), \(I\) is a connected positive interval, \(\phi\) is strictly increasing and locally Lipschitz, and \(a_+>0>a_-\) are continuous. In dimension two omit the middle coordinate. Two cross-branch comparisons at the same height force \(Q_n\) to be independent of all tangential coordinates; write it \(q_n(y)\). Fix one tangential coordinate and write \(q_1(y)\) for the first component. At heights \(y,z\), put \(D=q_1(y)-q_1(z)\), \(d=q_n(y)-q_n(z)\), and

\[
A=a_+(y)-a_-(z)>0,\qquad
B=a_+(z)-a_-(y)>0.
\]

The cross-branch inequalities are

\[
Ad\ge C[\phi(y)-\phi(z)]D,\qquad
-Bd\ge C[\phi(y)-\phi(z)]D.
\tag{SE38}
\]

Multiplying them by \(B,A\) and adding gives \([\phi(y)-\phi(z)]D\le0\). Hence \(q_1\) is nonincreasing. It has finite total variation on every compact \([\alpha,\beta]\subset I\), because its endpoint values are finite real numbers. On that interval, \(A,B\) have a positive common lower bound \(m\), while \(\phi\) has Lipschitz constant \(L\). Selecting the unfavorable inequality according to the sign of \(d\) gives

\[
|q_n(y)-q_n(z)|
\le\frac{CL}{m}|y-z|\,|q_1(y)-q_1(z)|.
\tag{SE39}
\]

Apply this to an \(N\)-part equal partition, use the triangle inequality, and telescope the nonincreasing \(q_1\) differences:

\[
|q_n(\beta)-q_n(\alpha)|
\le\frac{CL}{m}\frac{\beta-\alpha}{N}
[q_1(\alpha)-q_1(\beta)]\longrightarrow0.
\tag{SE40}
\]

This includes jumps and does not assume continuity of \(Q\). Thus \(Q_n\) is constant on the whole slice.

Apply the lemma to the full original graphs in the kernel coordinates:

| Full model and positive slice | \(C\phi(y)\) | \(a_+(y),a_-(y)\) | Nonstationary trajectory |
| --- | --- | --- | --- |
| Cap, \(\eta\le0,y>0\) | \(2\sqrt y\) | \(3y,-5y\) | \(\eta_0\le0,r_0>0\) |
| Superlinear, \(\eta\le0,0<y<1\) | \(Ay^{\gamma/\nu}\) | \(y^{1/\nu}-y,-y^{1/\nu}-y\) | \(\eta_0\le0,0<r_0<1\) |
| Log, \(y>0\) | \(\ell_a(4y)\) | \(3y,-5y\) | \(r_0>0\) |

Every selected trajectory stays in its slice and has adjacent distinct positive normal coordinates. Equation (SE36) has left normal coordinate zero by the lemma; its right normal coordinate is one of two nonzero numbers times \(h_k>0\). This is impossible. It excludes every source pair-monotone kernel and hence every ASM kernel on the **same full transformed graph preserving that specified generalized sequence**, for both \(\sigma=+1\) and \(\sigma=-1\).

The proof is local if one retains both complete branches, a connected interval containing an adjacent pair, and the entire relevant tangential product slice. It is not a proof from discrete trajectory pairs alone. It does not use, and therefore cannot be repaired by, warped coverage or inverse R-continuity.

## 7. Exact power ranges; what “arbitrary order above quadratic” can mean

Let \(h>0\), \(0<\gamma<1\), \(L,C,q>0\), \(\omega(t)=Lt^\gamma\), and \(\psi(s)=Cs^q\). The direct scalar compatibility ratio is

\[
\frac{\psi((t+\omega(t))/(2h))}{t}
=C\left(\frac{L+t^{1-\gamma}}{2h}\right)^q
t^{q\gamma-1}.
\tag{SE41}
\]

Therefore:

| Exponent regime | Precise small-radius direct certificate |
| --- | --- |
| \(q\gamma>1\) | Ratio tends to zero; every fixed positive parameter set has a sufficiently small strict radius. |
| \(q\gamma=1\), \(C(L/(2h))^q<1\) | Ratio tends to a number below one; a sufficiently small fixed strict radius exists. |
| \(q\gamma=1\), \(C(L/(2h))^q\ge1\) | This exact direct test fails. At coefficient equality it is greater than one for every \(t>0\), because the added \(t^{1-\gamma}\) is strictly positive. |
| \(q\gamma<1\) | Ratio diverges; this scalar certificate fails, without implying divergence of a particular trajectory. |

When \(\gamma=1\), the coefficient is \(C[(1+L)/(2h)]^q\) and the exponent is \(q-1\); omitting the “1” is incorrect. Changing or sharpening the actual modulus or EB gauge can change the certificate, so a failed displayed test is not a necessity theorem for convergence.

The general inequality gives \(D_{V,k+1}\le A D_{V,k}^{q\gamma}\) on a small collar for suitable \(A\). It is a kernel distance-to-set estimate. Exact physical point Q-order, its nonzero asymptotic factor, and any sharpness claim require more. The explicit tail calculation (SE22)–(SE24) supplies those extra facts for the superlinear family. The cap and log families prevent a universal claim of arbitrary high physical order from the general hypotheses alone.

## 8. ASM inclusion through the energy route, and the noninjective-fiber limit

Suppose the complete pair \((F,v)\) is \(\varepsilon\)-ASM, \(\varepsilon>0\), with nonempty zero set and global warped coverage at fixed \(h>0\). No monotonicity, continuity or injectivity of \(v\) is assumed. Two zero graph points immediately give \(v(s)=v(s')\) for all zeros. Let their common image be \(w_*\), and put \(D_v(x)=\|v(x)-w_*\|\).

First, pair monotonicity gives the full graph RL modulus \(\omega(t)=t\), since

\[
\|\Delta v-h\Delta f\|^2
\le\|\Delta v+h\Delta f\|^2.
\tag{SE42}
\]

Second, comparison of any complete graph value with a zero gives

\[
\varepsilon D_v(x)^2
\le\langle f,v(x)-w_*\rangle
\le\|f\|D_v(x),
\qquad D_v(x)\le r_F(x)/\varepsilon.
\tag{SE43}
\]

The last inequality follows by taking the complete infimum; no minimum attainment is required. Thus ASM itself supplies the kernel true-residual gauge \(\psi_v(t)=t/\varepsilon\), globally.

For an actual step write \(a=v(x_{k+1})-w_*\), \(b=v(x_k)-v(x_{k+1})\). The generic zero-anchor RL inequality with \(\omega(t)=t\) yields

\[
\|a\|^2+\|b\|^2\le D_v(x_k)^2.
\]

By (SE43), \(\|b\|\ge h\varepsilon\|a\|\). Therefore the general RL+EB **energy** certificate has

\[
E(r)=(1+h^2\varepsilon^2)r^2,
\quad A(r)=r^2,
\quad q_E=\frac1{1+h^2\varepsilon^2}<1,
\]
\[
E(D_v(x_{k+1}))\le q_E E(D_v(x_k)).
\tag{SE44}
\]

This holds for every \(h\varepsilon>0\), rather than just the \(h\varepsilon>1\) range admitted by the direct test with \(\omega=t\), \(\psi_v=t/\varepsilon\). It gives geometric kernel error and summable kernel steps, all with the full source quantifier. The source's stronger ASM anchor identity gives the printed estimate

\[
(1+2h\varepsilon)D_v(x_{k+1})^2+\|b\|^2
\le D_v(x_k)^2,
\]

and Cauchy even gives \(D_v(x_{k+1})\le(1+h\varepsilon)^{-1}D_v(x_k)\). These sharpenings must not be attributed to the weaker generic energy calculation.

Thus an extension with direct **or energy** certificates contains every source Theorem 2 kernel-convergence case at the kernel level. Source Theorem 2(b)'s physical distance assertion follows separately from its complete inverse R-Lipschitz assumption, exactly as printed. An extension that additionally requires a physical inverse/fiber modulus is a theorem for the corresponding controlled subclass; it does not literally contain every arbitrary-kernel source case with a physical-point conclusion.

The direct-only failure is not merely an artifact of choosing the loose modulus \(\omega=t\). On \(\mathbb R\), take \(F(x)=\varepsilon x\), \(v(x)=x\), and \(a=h\varepsilon\in(0,1)\). All source Theorem 2 hypotheses hold globally, while every valid all-pairs RL modulus is at least \((1-a)t/(1+a)\), and every valid true-residual EB gauge is at least \(t/\varepsilon\). Thus the direct compatibility ratio is at least

\[
\frac1{a(1+a)}.
\tag{SE44a}
\]

For \(a=1/4\), this lower bound is \(16/5>1\) at every positive scale; even the sharp modulus and exact gauge cannot supply a direct certificate for this specified pair. Their energy quotient is exactly \((1+a)^{-2}<1\). Therefore direct-only hypotheses and ASM hypotheses are incomparable on fixed pairs; adding the energy alternative repairs the source-to-extension direction at the kernel level.

The reason is concrete. For \(F(x_1,x_2)=v(x_1,x_2)=(x_1,0)\), \(h=\varepsilon=1\), the pair is ASM, coverage holds, and \(F^{-1}\) is globally R-Lipschitz at zero with modulus 1. Nevertheless

\[
x_k=(2^{-k},(-1)^k)
\tag{SE45}
\]

is a legal complete generalized trajectory, with geometric kernel convergence and physical distance to \(S=\{0\}\times\mathbb R\), but no physical point convergence or finite physical length. A vanishing kernel-step modulus \(\|x-u\|\le\rho(\|v(x)-v(u)\|)\) cannot hold on its fibers: equal kernel values can have different second coordinates. This is an exclusion of an unjustified conclusion, not a flaw in the source theorem.

Noninjective kernels can nevertheless support physical finite length when the control is imposed on **allowed transitions**, rather than on every pair of physical points. For the more general \(F(x_1,x_2)=(\varepsilon x_1,0)\), \(v(x_1,x_2)=(x_1,0)\), the complete warped fiber is

\[
J^v_{hF}(x)=\{x_1/(1+h\varepsilon)\}\times\mathbb R.
\]

The allowed selection

\[
\mathcal A(x)=\{(x_1/(1+h\varepsilon),x_2)\}
\tag{SE45a}
\]

has coverage for every input, is a genuine subset of the complete fiber, fixes every physical zero, and satisfies

\[
\|u-x\|=\|v(u)-v(x)\|\qquad(u\in\mathcal A(x)).
\]

Thus its physical trajectory converges with finite length to \((0,x_{2,0})\), even though \(v\) is noninjective on every neighborhood. This does not control every selection in the complete warped fiber, as (SE45) already demonstrates. A theorem using transition control must state its allowed-output coverage separately; ordinary source warped coverage does not supply it. In contrast, a bound \(\|x-u\|\le\rho(\|v(x)-v(u)\|)\), \(\rho(0)=0\), quantified over **all** point pairs necessarily makes \(v\) injective on that set. Calling that bound a general noninjective-kernel assumption would be misleading.

Consequently the meaningful strictness comparison is: source ASM cases are covered for their actual kernel/physical-distance conclusions; with an explicit physical control one obtains the stronger physical result; (SE12), (SE17), and (SE26) with \(a>1\) satisfy the extended controlled hypotheses but are outside every same-full-graph source pair-monotone representation preserving their specified generalized trajectories. For the **direct-only** certificate class, there is no general ASM inclusion; (SE44) is why the energy branch must be retained.

## 9. R-continuity and restriction imports remain useful, without erasing the comparison

In these finite-dimensional closed models the residual minima are attained, zeros are closed planes and nearest zeros exist. Their global true-residual EB therefore gives the source inverse R-continuity inclusion directly: every \(x\in(F^V)^{-1}(f)\) obeys

\[
d(x,S^V)\le\varphi_b(\psi(\|f\|))
\]

with an attained nearest zero. On a bounded small residual interval the power gauges with exponent \(q>1\), and the log inverse gauge, also admit linear upper bounds. Thus inverse R-continuity/R-Lipschitz is not the separating failed source hypothesis; the complete pair-monotone representation of the same trajectory is.

For general mappings, an output-only EB is weaker than source Definition 5's inclusion for every complete inverse fiber. Conversely, if an infimum is not attained and the source modulus has jumps at positive arguments, source R-continuity need not give an EB with exactly the same modulus evaluated at the infimum. One safe gauge is \(\widehat\rho(t)=\rho(2t)\) for \(t>0\), \(\widehat\rho(0)=0\); right continuity at zero and closed zeros handle residual zero. These model calculations avoid that issue by computing the complete minima explicitly.

Finally, the existing branch-restriction imports conjugate just as exactly as (SE2). If \(G_+\) is a zero-set-preserving positive-branch restriction and \(K_+\) its proved source kernel, set

\[
F_+^V(x)=G_+(Vx),\qquad \widetilde K_+(x)=K_+(Vx).
\tag{SE46}
\]

All-pairs pair monotonicity/ASM, full warped coverage and complete fibers transfer. The zero set remains the whole original plane. On the proved invariant basin or after the proved finite prefix, the same conjugated generalized sequence is a source-GPPA sequence for this **different complete relation**. The inverse Lipschitz bound (SE9) transfers the already established physical convergence and finite-length bridge. This includes cap T2, the fixed-collar superlinear T2 import, and log \(a>1\) T1 plus its independently established Dini tail/length bridge.

Therefore none of the witnesses proves that their physical convergence cannot be obtained through a legitimate GPPA restriction argument. What is rigorously strict is the full-graph, same-algorithm representation and the availability of the displayed general-modulus certificates and exact quantitative tails. Global novelty, arbitrary lifts/reformulations and precise prior attribution of those quantitative results remain separate questions.

## Reading and verification scope

Read the four root state files (`README.md`, `RESEARCH_STATE.md`, `CLAIMS.md`, `FAILED_ROUTES.md`) in their relevant convergence/comparison ranges, `RESEARCH_PROTOCOL.md`, the complete general-modulus and RLEB local theorem pages, complete cap and superlinear object cards, fixed GPPA PDF Definitions 1–5 and Theorems 1/2/4, the all-kernel pair-monotone proof, the branch-restriction report, and the corresponding independent sol61 audits. No `AGENTS.md` was found in the workspace/repository search. No central file, claim ledger or graph registration is changed by this page; no commit/push is performed.

The proofs above carry the universal quantifiers. Finite arithmetic checks, when run by the integrating team, can corroborate selected updates and constants but cannot replace the complete-fiber inversion, no-regularity partition argument, Dini integrals or infinite-tail asymptotics.
