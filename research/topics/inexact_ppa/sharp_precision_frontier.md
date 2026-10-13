# 非精确 PPA 的完整精度边界：临界 Hölder 模型

本页 C276-v1 的注册结论为临界 \(\gamma p=1\) 的完整接受纤维、有限帽锐边界、误差幂次三分界与比较反例。非临界说明保留为自足扩展，不授予所有 RLEB 算子的必要性。公开首创尚未认证。这里的对象是 **inner graph residual**
\[
x=y+\lambda w+e,\qquad w\in F(y),\qquad
\|e\|\le\eta\|\lambda w\|^q. \tag{IF1}
\]
The parameters in IF1 satisfy \(\eta\ge0\) and \(q>0\). The actual next iterate is \(y\). This differs from C213's outer perturbation \(y=J_{\lambda F}(x)+e\). In IF1 the exact Minty input is \(u=x-e=y+\lambda w\); bounds on the exact resolvent must be applied at \(u\), not silently at \(x\).

The constructions below use the complete graph, all real signs, and a nonisolated complete zero set. They establish actual divergent trajectories, not merely failure to absorb an upper estimate. The basic translation model is a mechanism diagnostic, not a claim of a natural high-value application or a new general convergence principle.

<a id="isp-object"></a>
## 1. 完整算子与精确 RLEB 证书

Fix
\[
0<\gamma<1,\quad p\ge1/\gamma,\quad
\alpha=\gamma p\ge1,\quad a>0,\quad 0<b<1,\quad\lambda>0.
\]
Write \(h_\alpha(t)=\operatorname{sgn}(t)|t|^\alpha\), with \(\operatorname{sgn}(0)=0\). On \(\mathbb R^2\), define the complete resolvent
\[
J(s,t)=\bigl(s+a|t|^\gamma,\ b h_\alpha(t)\bigr). \tag{IF2}
\]
Its second coordinate is invertible. Thus the following is a globally defined, continuous, single-valued operator, with no discarded remote branch:
\[
\tau(z)=\operatorname{sgn}(z)(|z|/b)^{1/\alpha},\qquad
F(v,z)=\frac1\lambda\bigl(-a|\tau(z)|^\gamma,\ \tau(z)-z\bigr). \tag{IF3}
\]
Indeed,
\[
(v,z)+\lambda F(v,z)=
\bigl(v-a|\tau(z)|^\gamma,\tau(z)\bigr),
\]
whose global inverse is exactly IF2. Consequently \(J=J_{\lambda F}\), complete input coverage and uniqueness hold globally, and
\[
S=\operatorname{zer}F=\mathbb R\times\{0\}. \tag{IF4}
\]
For an exact input \(u=(s,t)\), set
\[
W_\alpha(t):=\|\lambda F(Ju)\|
=\sqrt{a^2|t|^{2\gamma}+(t-bh_\alpha(t))^2}. \tag{IF5}
\]
Because the fiber of \(F\) is a singleton, this is \(\lambda r_F(Ju)\), not merely a selected-value surrogate. For every physical point \(y=J(s,t)\),
\[
d(y,S)=b|t|^{\gamma p}
\le b(\lambda/a)^p r_F(y)^p. \tag{IF6}
\]
This true EB is global. Since \(W_\alpha(t)/(a|t|^\gamma)\to1\) as \(t\to0\), the ratio of the two sides of IF6 tends to one. No EB power strictly greater than \(p\) can hold with a finite coefficient in any neighborhood of a zero.

For \(|t|\le R\), the nearest zero to \(u\) is \((s,0)\), and
\[
2J(u)-u-(s,0)
=\bigl(2a|t|^\gamma,\ 2b h_\alpha(t)-t\bigr). \tag{IF7}
\]
This gives a local anchored Hölder RL estimate of exponent \(\gamma\). The exponent is sharp, since the first coordinate divided by \(|t|^\beta\) diverges for every \(\beta>\gamma\).

For general \(\alpha\ge1\), this can also be verified with all-pair quantifiers on the complete Minty-input strip \(|t|\le R\). The normal reflected coordinate has Lipschitz constant at most \(m_R=1+2b\alpha R^{\alpha-1}\); therefore, on input pairs of distance at most \(R\),
\[
\|C(u)-C(u')\|\le
\bigl(m_R R^{1-\gamma}+2a\bigr)\|u-u'\|^\gamma.
\]
The represented graph block contains every complete exact output of every input in that strip. With this coefficient and IF6, the C02 compatibility ratio is bounded by a constant times \(R^{\alpha-1}\) and hence tends to zero when \(\alpha>1\). Thus the supercritical exponent attacks below also satisfy the exact convergence conjunction on a sufficiently small positive window. The following critical-case estimate is sharper than this general-purpose bound.

In the critical case \(\alpha=1\), which is the main exact-frontier example below, the reflected map is
\[
C(s,t)=2J(s,t)-(s,t)
=\bigl(s+2a|t|^\gamma,(2b-1)t\bigr).
\]
The elementary inequality \(\big||t|^\gamma-|t'|^\gamma\big|\le|t-t'|^\gamma\) and \(|2b-1|\le1\) give the global all-pair modulus
\[
\|C(u)-C(u')\|
\le\|u-u'\|+2a\|u-u'\|^\gamma. \tag{IF8}
\]
Hence every pair with \(\|u-u'\|\le R\) satisfies the all-pair Hölder RL estimate with
\[
L_R=R^{1-\gamma}+2a. \tag{IF9}
\]
No same-sign restriction was used. The complete graph therefore admits the stronger C02-v2 full-pair certificate as well as C02-v3's anchored one. With the true EB \(\psi(r)=b(\lambda/a)^p r^p\) and \(\gamma p=1\), the standard C02 compatibility bound is
\[
\frac{\psi((d+L_R d^\gamma)/(2\lambda))}{d}
\le b\bigl(1+R^{1-\gamma}/a\bigr)^p. \tag{IF10}
\]
For every \(b<1\), a positive small \(R\) makes this less than a chosen \(\kappa\in(b,1)\). The output EB is global, and one may choose any \(\bar t\) at least \((R+L_R R^\gamma)/(2\lambda)\). On \(U=\mathbb R^2\), the strict localization budget is automatic. Thus the exact hypotheses really hold; their local convergence is not presumed from the model's name.

For the critical exact map, every orbit and limit are explicit:
\[
J^k(s_0,t_0)=\left(s_0+a|t_0|^\gamma
\frac{1-b^{k\gamma}}{1-b^\gamma},\ b^kt_0\right),\qquad
x^\infty=\left(s_0+\frac{a|t_0|^\gamma}{1-b^\gamma},0\right).
\tag{IF27}
\]
The homeomorphism \(H(s,t)=(s+a|t|^\gamma/(1-b^\gamma),t)\) conjugates \(J\) to \((\xi,t)\mapsto(\xi,bt)\). It is Hölder rather than locally bi-Lipschitz at the zero-line. This makes the exact model elementary, while preserving the question about errors measured in the original physical norm. It is a precision diagnostic, not a hard natural application.

<a id="isp-frontier"></a>
## 2. 临界情形的完整纤维与锐帽边界

From now through Section 4, set \(p=1/\gamma\), \(\alpha=1\), and \(c=1-b\). Then
\[
W(t)=\sqrt{a^2|t|^{2\gamma}+c^2t^2}
=A(|t|)|t|^\gamma,\qquad
A(T)=\sqrt{a^2+c^2T^{2-2\gamma}}. \tag{IF11}
\]
Fix \(T>0\). Define the **complete accepted relation** to be precisely the outputs admitting triples in IF1 satisfying the computable selected-residual cap
\[
\|\lambda w\|\le W(T). \tag{IF12}
\]
The function \(W\) is strictly increasing on \([0,\infty)\), so IF12 is equivalent to \(|t|\le T\) for the exact input \(u=x-e=(s,t)\). It does not select a favorable branch of an accepted relation.

For every physical input \(x=(s,r)\), the entire accepted output fiber has the closed description
\[
\mathcal A(s,r)=\bigcup_{\substack{|t|\le T\\ |r-t|\le\eta W(t)^q}}
[\,s+a|t|^\gamma-\ell(t,r),\ s+a|t|^\gamma+\ell(t,r)\,]\times\{bt\},
\quad\ell(t,r)=\sqrt{\eta^2 W(t)^{2q}-(r-t)^2}.
\tag{IF26}
\]
For each such output \(y\), the only graph witness is
\(w=(-a|t|^\gamma,(1-b)t)/\lambda\). Its first defect component satisfies \(e_1\in[-\ell(t,r),\ell(t,r)]\), while \(y_1\) lies in the displayed centered interval; its second equals \(r-t\), so IF26 is equivalent in both directions to IF1/IF12. At \(\eta=0\), only \(t=r\) and the exact output remain (when \(|r|\le T\)); for positive tolerance, all intervals and all normal parameters are retained.


For \(q\ge p\), define
\[
H_q(T)=T^{\gamma q-1}A(T)^q. \tag{IF13}
\]
The function \(W(t)^q/t=t^{\gamma q-1}A(t)^q\) is nondecreasing for \(t>0\). Therefore
\[
\sup_{0<t\le T}\frac{W(t)^q}{t}=H_q(T).
\]

**Exact frontier.** For every initial point with \(d(x^0,S)\le T\), every choice from the complete accepted relation IF1/IF12 has finite length and converges to \(S\) if and only if
\[
\boxed{\ \eta H_q(T)<1-b\ }. \tag{IF14}
\]
The assertion includes arbitrary tangential errors, both normal signs, and all accepted outputs.

**Sufficiency.** Put \(\delta=\eta H_q(T)<c\). An arbitrary accepted output has \(y=J(s,t)\), \(x=(s,t)+e\), and \(\|e\|\le\delta|t|\). Thus
\[
d(x,S)=|t+e_2|\ge(1-\delta)|t|,
\qquad d(y,S)=b|t|
\le\kappa d(x,S),\qquad
\kappa=\frac b{1-\delta}<1. \tag{IF15}
\]
For \(t\ne0\), the strict bound also proves that \(x_2,t,y_2\) have the same sign; cross-sign outputs have not been omitted from the proof. If \(d(x,S)=0\), IF15 forces \(t=0\); then \(w=e=0\) and \(y=x\). Every zero input is absorbing.

For an arbitrary input \(|x_2|\le T\), the exact output \(e=0\), \(u=x\) passes the cap and stopping test. Hence the complete accepted relation is nonempty on the whole input tube. IF15 keeps each actual output in that tube, so continuation follows by finite induction.

The physical displacement satisfies
\[
\|y-x\|\le W(t)+\|e\|
\le\frac{A(T)}{(1-\delta)^\gamma}d(x,S)^\gamma
 +\frac\delta{1-\delta}d(x,S). \tag{IF16}
\]
Summing along \(d(x^k,S)\le\kappa^k d_0\) proves the explicit length bound
\[
\sum_{k\ge0}\|x^{k+1}-x^k\|
\le\frac{A(T)d_0^\gamma}{(1-\delta)^\gamma(1-\kappa^\gamma)}
 +\frac{\delta d_0}{(1-\delta)(1-\kappa)}. \tag{IF17}
\]
Cauchy convergence and closedness of \(S\) finish the proof.

**Necessity, including equality.** If \(\eta H_q(T)\ge c\), use \(t=T\) and the policy
\[
x^k=(s_0+kaT^\gamma,bT),\quad
u^k=(s_0+kaT^\gamma,T),\quad
e^k=(0,-cT),\quad x^{k+1}=J(u^k). \tag{IF18}
\]
Here \(\|\lambda w^k\|=W(T)\), \(\|e^k\|=cT\le\eta W(T)^q\), and the initial distance is \(bT\le T\). The graph equation holds identically. The distance to \(S\) is constantly \(bT>0\), and the tangent coordinate tends to \(+\infty\) with step \(aT^\gamma\). This is an actual divergent full-graph accepted trajectory. It proves IF14 sharply, including the nonconvergent endpoint. □

For the requested stopping power \(q=p\), IF14 is the exact finite-cap threshold
\[
\boxed{\ \eta<\eta_{\rm conv}(T)
=\frac{1-b}{\bigl(a^2+(1-b)^2T^{2-2\gamma}\bigr)^{p/2}}\ }. \tag{IF19}
\]
As \(T\downarrow0\), the sharp local coefficient tends to
\[
\eta_*=(1-b)/a^p. \tag{IF20}
\]
Every \(\eta<\eta_*\) is locally admissible after shrinking the cap. Every \(\eta\ge\eta_*\) admits IF18 at **arbitrarily small nonzero normal distances**: at equality, \(W(t)^p>a^p|t|\) for every \(t\ne0\), since \(c>0\). This is why equality cannot be included.

Under the normalized true-EB stopping test
\[
\|e\|\le\widehat\eta\,\psi(\|w\|),\qquad
\psi(r)=b(\lambda/a)^p r^p,
\]
one has \(\eta=\widehat\eta b/a^p\). Thus the sharp asymptotic threshold is
\[
\boxed{\ \widehat\eta_*=(1-b)/b\ }. \tag{IF21}
\]
A general sufficient theorem using a finite-window certified \(\kappa_0>b\) may require \(\widehat\eta<(1-\kappa_0)/\kappa_0\). That is not the exact finite-cap frontier IF19; it reaches IF21 only as the certified window shrinks. The sharper model calculation must not silently be promoted to a universal constant.

<a id="isp-power"></a>
## 3. 误差幂次与必要性的准确范围

If \(q<p=1/\gamma\), then
\[
\frac{|t|}{W(t)^q}\sim a^{-q}|t|^{1-\gamma q}\longrightarrow0.
\]
For every \(\eta>0\) and every positive residual cap, a sufficiently small \(t\ne0\) passes the stopping test both for the zero-input escape \(e=(0,-t)\) and for the divergent policy IF18. Thus no smaller power supplies a local all-output result uniformly over this sharp Hölder-RLEB class.

If \(q>p\), then \(H_q(T)\to0\) as \(T\downarrow0\). Every finite \(\eta\ge0\) satisfies IF14 after choosing a sufficiently small positive cap. This proves a strict three-way power frontier:

| Forcing power | Local complete-output behavior of this critical model |
| --- | --- |
| \(\gamma q<1\) | Every \(\eta>0\) admits arbitrary-near-zero escape and divergent tangent drift. |
| \(\gamma q=1\) | Strict coefficient \(\eta<(1-b)/a^q\) is necessary and sufficient after shrinking the cap. The endpoint fails. |
| \(\gamma q>1\) | Every finite coefficient is locally admissible after shrinking the cap. |

The **universal exponent obstruction is \(q\ge1/\gamma\), not \(q\ge p\) when the supplied EB exponent obeys \(\gamma p>1\)**. In the more general IF2/IF3 model with \(\alpha=\gamma p>1\), the same zero-input calculation gives escape whenever \(\gamma q<1\). Conversely, for \(\gamma q>1\), \(W_\alpha(t)^q/|t|\to0\), and for \(\gamma q=1\) with \(\eta<a^{-q}\), this ratio times \(\eta\) is less than one on a small cap. Then
\[
|x_2|\ge(1-\delta)|t|,\qquad
d(y,S)=b|t|^\alpha
\le\frac{bT^{\alpha-1}}{1-\delta}d(x,S),
\]
which supplies contraction and summable displacement on a small cap. At the critical coefficient \(\eta=a^{-q}\), the constant-normal policy
\[
x^k=(s_0+ka|t|^\gamma,bh_\alpha(t)),\qquad
e^k=(0,-t+bh_\alpha(t))
\]
passes at every sufficiently small \(t>0\): its error is \(t-bt^\alpha<t\), whereas \(\eta W_\alpha(t)^q\ge t\). Thus the endpoint again fails. The requested rule \(q=p\) lies in the strict higher-power regime whenever \(\gamma p>1\), so a small-coefficient condition is then an optional finite-window certificate, not a necessary asymptotic condition.

For completeness, the cap used in this supercritical positive assertion can be fully computable without assuming \(W_\alpha\) is globally monotone. Choose a small \(T>0\) and impose \(\|\lambda w\|\le aT^\gamma\). Since \(W_\alpha(t)\ge a|t|^\gamma\), every accepted output has \(|t|\le T\). Choose a positive input radius \(R_0\le T\) with \(\sup_{|t|\le R_0}W_\alpha(t)\le aT^\gamma\), which exists by continuity at zero. Exact steps then supply coverage throughout \(|x_2|\le R_0\). On \(|t|\le T\), write
\[
A_\alpha(T)^2=a^2+
\sup_{0<|t|\le T}\frac{(t-bh_\alpha(t))^2}{|t|^{2\gamma}}.
\]
This is finite and tends to \(a^2\). The error-to-input ratio is at most \(\eta A_\alpha(T)^qT^{\gamma q-1}\) for \(\gamma q>1\), and at most \(\eta A_\alpha(T)^q\) for \(\gamma q=1\). The preceding strict conditions make this ratio less than one and the displayed normal contraction less than one for a sufficiently small \(T\). The actual normal distance then remains at most \(R_0\), so coverage is used by finite induction. The displacement bound and geometric summation are the same as IF16/IF17 with the appropriate constants. This closes the input-coverage and full-cap obligations in that assertion.

None of these necessity statements says that every individual RLEB operator requires the same power. An operator may have a stronger reflected modulus than the one supplied, or no tangent drift. The statements are sharp across the displayed complete-graph class with sharp \(\gamma\) and sharp true EB exponent \(p\).

<a id="isp-remote"></a>
## 4. 零吸收、远端残差与跨符号

For \(q\ge p\) under the cap IF12, the exact zero-absorption threshold is
\[
\boxed{\ \eta H_q(T)<1\ }. \tag{IF22}
\]
Indeed, an input on \(S\) requires \(e_2=-t\), so \(\|e\|\ge|t|\). IF22 forces \(t=0\). If \(\eta H_q(T)\ge1\), the choice \(t=T\), \(e=(0,-T)\) gives an accepted nonzero output from \(S\). Hence zero absorption is strictly weaker than all-output convergence: the interval
\[
1-b\le\eta H_q(T)<1
\]
has absorbing zero inputs and nevertheless contains the divergent constant-distance trajectory IF18.

For \(\eta H_q(T)>1\), opposite-sign outputs are also admitted: at \(t=T>0\), choose \(x_2=-\varepsilon\) and \(e_2=-T-\varepsilon\), with \(0<\varepsilon<T(\eta H_q(T)-1)\). The next normal coordinate is \(bT>0\). Thus a same-sign root calculation would omit actual accepted outputs once the absorption threshold fails.

Without any residual cap, **every \(q>0\) and every \(\eta>0\)** admit a divergent accepted trajectory starting on \(S\). If \(q<p\), choose a sufficiently small \(t>0\). If \(q\ge p>1\), use
\[
W(t)\sim(1-b)t\quad(t\to\infty),\qquad
\frac{t}{W(t)^q}\to0,
\]
and choose a sufficiently large \(t\). In either case \(t\le\eta W(t)^q\). Start at \(x^0=(s_0,0)\), take \(u^0=(s_0,t)\), \(e^0=(0,-t)\), and
\[
x^1=(s_0+a t^\gamma,bt).
\]
For every subsequent step use IF18 at that same \(t\). The first error passes by construction, and later errors \((1-b)t<t\) also pass. The tangent coordinate diverges and the normal distance remains \(bt\). This proves the necessity of some global exclusion of far accepted residuals for a purely local full-output theorem; a selected-residual cap is one concrete repair. No theorem can deduce that cap merely because the initial distance is small.

There is no output-window loophole in this counterexample: IF6 is a global true EB, the complete graph is explicit, and the exact graph has no remote additional root. For a general local theorem, however, the EB must cover the **accepted inexact outputs**, and the reflection estimate must cover the shifted exact inputs \(u=x-e\). Neither is automatic from an EB stated only on \(J(U_R)\). A cap alone does not keep shifted inputs in an arbitrary bounded open \(U\); that is a separate finite-prefix localization obligation.

The failed output-set inclusion is already concrete in this same harmless globally certified model. Fix \(0<R<T\), \(\eta>0\), \(q=p\), and choose
\[
0<\varepsilon<\min\{T-R,\eta a^pR\}.
\]
The input \(x=(s,R)\), shifted input \(u=(s,R+\varepsilon)\), and error \(e=(0,-\varepsilon)\) pass IF1/IF12, since
\(\varepsilon<\eta a^pR\le\eta W(R+\varepsilon)^p\).
Yet the output normal coordinate \(b(R+\varepsilon)\) lies outside the exact-output strip \(J(\{d\le R\})\), whose normal coordinates are bounded by \(bR\). Thus an EB certified only on the latter strip supplies no statement at this accepted output. This exhibits the missing inclusion itself; the global EB of the present example happens to repair it.

<a id="isp-classical-boundary"></a>
## 5. 有限局部亚单调与逆亚单调均失败

For the critical model, the raw operator IF3 is
\[
F(v,z)=(-A|z|^\gamma,Cz),\qquad
A=ab^{-\gamma}/\lambda>0,\quad
C=(1-b)/(b\lambda)>0. \tag{IF23}
\]
At the zero \((0,0)\), no finite local hypomonotonicity constant exists. With \(y_t=(t,t)\), \(t\downarrow0\),
\[
\frac{\langle F(y_t),y_t\rangle}{\|y_t\|^2}
=-\frac A2t^{\gamma-1}+\frac C2\longrightarrow-\infty. \tag{IF24}
\]
Therefore \(\langle F(y)-F(y'),y-y'\rangle\ge-\rho\|y-y'\|^2\) fails near zero for every finite \(\rho\), even with \(y'=(0,0)\).

No finite local cohypomonotonicity constant exists either. Use instead \(\widetilde y_t=(t^{\gamma/2},t)\), which also approaches \((0,0)\). Then
\[
\frac{\langle F(\widetilde y_t),\widetilde y_t\rangle}{\|F(\widetilde y_t)\|^2}
=\frac{-At^{3\gamma/2}+Ct^2}{A^2t^{2\gamma}+C^2t^2}
\sim-\frac1A t^{-\gamma/2}\longrightarrow-\infty. \tag{IF25}
\]
The graph inequality with a lower bound \(-\rho\|F(y)-F(y')\|^2\), as well as the corresponding zero-anchored weak-Minty inequality, fails for every finite \(\rho\). The two failures use different tangent scales; IF25 does not prove IF24 by itself. These are verified hypothesis exclusions, not a claim excluding every classical convergence result or every artificial energy construction.

The obstruction is not removed by choosing another zero anchor. For every \(p_0=(s_0,0)\in S\), replace the test points in IF24/IF25 by \(p_0+y_t\) and \(p_0+\widetilde y_t\); IF23 is translation invariant in the tangent coordinate. The same ratios apply to \(\langle F(y),y-p_0\rangle\). Thus there is no finite zero-anchored weak-Minty coefficient at any solution.

<a id="isp-checks"></a>
## 6. 可复算实例

Set \(\lambda=a=1\), \(\gamma=1/2\), \(p=q=2\), \(b=1/4\). Then
\[
F(v,z)=(-2\sqrt{|z|},3z),\quad
J(s,t)=(s+\sqrt{|t|},t/4),\quad
\psi(r)=r^2/4.
\]
For \(R=10^{-2}\), the full-pair Hölder constant \(L_R=2+\sqrt R=2.1\) gives C02's compatibility bound
\[
b(1+\sqrt R)^2=0.3025<1/2,
\]
and \(B(R)=0.11<\bar t=1\). All exact C02 gates thus hold on the complete graph with \(U=\mathbb R^2\).

The selected residual is
\[
W(t)^2=|t|+\frac9{16}t^2,
\qquad
\eta_{\rm conv}(T)=\frac{3/4}{1+9T/16},\quad
\eta_{\rm abs}(T)=\frac1{1+9T/16}.
\]
At \(\eta=3/4\), every sufficiently small \(t>0\) supplies the divergent policy
\[
x^k=(s_0+k\sqrt t,t/4),\qquad e^k=(0,-3t/4).
\]
For example, \(t=10^{-8}\) has constant distance \(2.5\times10^{-9}\) and positive constant physical step \(10^{-4}\).

Without a cap, even \(\eta=0.1\) admits escape from \(x^0=(0,0)\): choose \(t=16\), so \(W(16)^2=160\), \(e^0=(0,-16)\), and \(x^1=(4,4)\). The stopping inequality is equality in the first step. Thereafter use \(e=(0,-12)\), obtaining \(x^k=(4k,4)\) for \(k\ge1\); the inner error norm \(12\) is less than \(0.1W(16)^2=16\).

Run the supplementary verifier with
\[
\texttt{python3 research/code/inexact\_forcing\_attack/check\_frontier.py}.
\]
The script directly reconstructs graph equations, errors and selected residuals, including both signs; it checks threshold examples and the exact C02 constants. Its finite evaluations support those instances only. The full-graph frontier and exclusions above are analytic proofs.

## Scoped review outcome

The exact operator identity, complete coverage, true residual, sharp exponents, full-pair RL, finite-cap sufficient proof, endpoint divergent policy, zero/far/cross-sign behavior and local hypo/cohypomonotonicity exclusions have been reconstructed in this note. 一般停止合同见 [C275](real_graph_stopping.md#igs-theorem)，独立价值、自然模型筛选与先行性见[入口](README.md)。本页模型是诊断机制例，不能冒称难解自然应用；主稿、摘要和编号未改。
