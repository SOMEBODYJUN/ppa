# RL foundations: moving anchors, isolated-zero flatness, and local PPA order

> Task: RL-FND-ANCHOR-03  
> Scope: independent algebraic reconstruction; no literature or novelty claim.  
> Status: theorem/proof package for merger after orchestrator review.

## 0. Setting and quantifiers

Let $H$ be a real Hilbert space, let $F:H\rightrightarrows H$, fix
$\lambda>0$, and set

\[
S:=F^{-1}(0),\qquad r_F(y):=d(0,F(y)).
\]

For $(y,w)\in\operatorname{gph}F$, use the Minty coordinates

\[
x:=y+\lambda w,\qquad \widehat x:=y-\lambda w. \tag{0.1}
\]

Thus $y\in J_{\lambda F}(x)$ and
$\widehat x\in(2J_{\lambda F}-I)(x)$, relation-wise.
For a graph localization $\Gamma\subset\operatorname{gph}F$, put

\[
M_\lambda(y,w):=y+\lambda w,\qquad D_\Gamma:=M_\lambda(\Gamma).
\]

Only when $M_\lambda|_\Gamma$ is injective does $\Gamma$ induce

\[
J_\Gamma:=\pi_1\circ(M_\lambda|_\Gamma)^{-1},\qquad
R_\Gamma:=2J_\Gamma-I
\quad\text{on }D_\Gamma. \tag{0.2}
\]

Nothing below, by itself, proves neighborhood coverage
$B(p,\delta)\subset D_\Gamma$, exclusion of remote full-resolvent
branches, or validity for arbitrary full-resolvent selections. The
algebraic proofs use only the normed-linear-space structure.

---

## 1. Moving-anchor asymptotic reflection

### Theorem 1.1 (superlinear-gauge moving anchor)

Let $\psi:[0,\eta)\to[0,+\infty)$ be finite and nondecreasing, with

\[
\psi(t)=o(t)\qquad(t\downarrow0). \tag{1.1}
\]

Suppose, at the graph points being considered,

\[
d(y,S)\le \psi(r_F(y)). \tag{1.2}
\]

Let $e:[0,\eta)\to[0,+\infty)$ satisfy $e(t)=o(t)$. For
$w\in F(y)$ with $0<\|w\|<\eta$, choose $p\in S$ so that

\[
\|y-p\|\le d(y,S)+e(\|w\|). \tag{1.3}
\]

Define

\[
\vartheta(t):=\psi(t)+e(t),\qquad
\delta_w:=\frac{\vartheta(\|w\|)}{\lambda\|w\|}. \tag{1.4}
\]

Then $\|y-p\|\le\vartheta(\|w\|)$. Whenever $\delta_w<1$,

\[
\frac{1-\delta_w}{1+\delta_w}
\le
\frac{\|\widehat x-p\|}{\|x-p\|}
\le
\frac{1+\delta_w}{1-\delta_w}, \tag{1.5}
\]

and

\[
\frac{\|\widehat x-(2p-x)\|}{\|x-p\|}
\le \frac{2\delta_w}{1-\delta_w}. \tag{1.6}
\]

Consequently, along every such sequence with $w_n\to0$, $w_n\ne0$,

\[
\frac{\|\widehat x_n-p_n\|}{\|x_n-p_n\|}\to1,\qquad
\widehat x_n-p_n
=-(x_n-p_n)+o(\|x_n-p_n\|). \tag{1.7}
\]

#### Proof

Since $r_F(y)\le\|w\|$, monotonicity of $\psi$ and (1.2)--(1.3) give
$\|y-p\|\le\vartheta(\|w\|)$. Write

\[
a:=y-p,\qquad t:=\lambda w.
\]

Then $x-p=a+t$, $\widehat x-p=a-t$, and
$\|a\|\le\delta_w\|t\|$. Direct and reverse triangle inequalities give
(1.5). Moreover,

\[
\widehat x-(2p-x)=2a,\qquad
\|x-p\|\ge(1-\delta_w)\|t\|,
\]

which gives (1.6). Finally $\delta_{w_n}\to0$, proving (1.7).
$\square$

### Projection clause

No proximinality is hidden here. If $e(\|w\|)>0$, a point satisfying
(1.3) exists by the definition of distance. The choice $e\equiv0$ is
legitimate only when $p\in P_S(y)$ exists at every relevant output; a
uniform zero-error anchor rule therefore requires proximinality of $S$
on those outputs (global proximinality is sufficient, but not necessary).

### Corollary 1.2 (power case and constants)

Let $q>1$, $\rho>0$, $c\ge0$, and assume

\[
d(y,S)\le\rho r_F(y)^q,\qquad
\|y-p\|\le d(y,S)+c\|w\|^q, \tag{1.8}
\]

where $c=0$ denotes an exact projection. With $A:=\rho+c$,

\[
\|y-p\|\le A\|w\|^q,\qquad
\delta_w=\frac A\lambda\|w\|^{q-1}. \tag{1.9}
\]

Thus (1.5)--(1.7) apply. If $\delta_w\le\frac12$, then

\[
\|y-p\|
\le A\left(\frac2\lambda\right)^q\|x-p\|^q, \tag{1.10}
\]

\[
\boxed{
\|\widehat x-(2p-x)\|
\le\frac{2^{q+1}A}{\lambda^q}\|x-p\|^q.} \tag{1.11}
\]

Indeed, $\|x-p\|\ge\lambda\|w\|/2$.

### Exact scope

The anchor is an output-nearest, or $o(\|w\|)$-accurate output-near,
zero. The theorem does not imply:

1. all-pairs Lipschitz continuity of $R_{\lambda F}$;
2. the same limit with $p_x\in P_S(x)$;
3. the same limit with a fixed zero when $S$ is nonisolated;
4. $d(\widehat x,S)/d(x,S)\to1$;
5. existence or uniqueness of a resolvent branch.

If $(p,0)\notin\Gamma$, (1.7) remains a vector statement but is not a
comparison with $R_\Gamma(p)$.

---

## 2. Fixed-anchor flatness

The algebraic equivalence below does not need isolation. Isolation is
needed only to turn a full mapping error bound into a fixed-zero bound.

### Theorem 2.1 (power equivalence on a graph germ)

Fix $p\in S$, $q>1$, and a graph germ
$\Gamma\subset\operatorname{gph}F$ at $(p,0)$. With (0.1), the following
are equivalent after possibly shrinking the germ:

\[
\begin{aligned}
\mathrm{(B_q)}\quad&\|y-p\|\le C_B\|w\|^q,\\
\mathrm{(J_q)}\quad&\|y-p\|\le C_J\|x-p\|^q,\\
\mathrm{(R_q)}\quad&
\|\widehat x-(2p-x)\|\le C_R\|x-p\|^q.
\end{aligned} \tag{2.1}
\]

Safe transferred constants are

\[
C_J=C_B\left(\frac2\lambda\right)^q,\qquad
C_B=C_J(2\lambda)^q,\qquad C_R=2C_J. \tag{2.2}
\]

These are not asserted to be optimal moduli.

#### Proof

Under $\mathrm{(B_q)}$, shrink so that
$C_B\|w\|^{q-1}\le\lambda/2$. Then

\[
\|x-p\|\ge\lambda\|w\|-\|y-p\|
\ge\frac\lambda2\|w\|,
\]

which proves $\mathrm{(J_q)}$. Conversely, under $\mathrm{(J_q)}$,
shrink so that $C_J\|x-p\|^{q-1}\le1/2$. Since
$\lambda w=(x-p)-(y-p)$,

\[
\lambda\|w\|\ge\|x-p\|-\|y-p\|
\ge\frac12\|x-p\|,
\]

which proves $\mathrm{(B_q)}$. Finally,

\[
\widehat x-(2p-x)=2(y-p), \tag{2.3}
\]

so $\mathrm{(J_q)}\Longleftrightarrow\mathrm{(R_q)}$ exactly.
$\square$

### Theorem 2.2 (general superlinear controls)

Let $\alpha,\beta$ be finite, nondecreasing near zero, with
$\alpha(t)=o(t)$ and $\beta(t)=o(t)$.

- If
  \[
  \|y-p\|\le\beta(\|w\|), \tag{2.4}
  \]
  then, on a smaller germ,
  \[
  \|y-p\|\le
  \beta\!\left(\frac2\lambda\|x-p\|\right). \tag{2.5}
  \]

- If
  \[
  \|y-p\|\le\alpha(\|x-p\|), \tag{2.6}
  \]
  then, on a smaller germ,
  \[
  \|y-p\|\le\alpha(2\lambda\|w\|). \tag{2.7}
  \]

- Reflection-defect control is exactly twice the corresponding
  $J$-control, by (2.3).

#### Proof

In (2.4), $\beta(\|w\|)\le\lambda\|w\|/2$ locally, so
$\|w\|\le2\|x-p\|/\lambda$; monotonicity yields (2.5). In (2.6),
$\alpha(\|x-p\|)\le\|x-p\|/2$ locally, so
$\|x-p\|\le2\lambda\|w\|$; monotonicity yields (2.7).
$\square$

### Same-gauge form: the missing hypothesis

The three properties may use the same $\psi=o(t)$ up to multiplicative
constants if $\psi$ is stable under fixed dilations:

\[
\forall c>0,\qquad \psi(ct)=O(\psi(t))\quad(t\downarrow0). \tag{2.8}
\]

For fixed $\lambda$, only the dilation factors $2/\lambda$ and
$2\lambda$ that exceed one are needed. Power and regularly varying
power-type gauges satisfy (2.8). Without it, the correct theorem is the
rescaled pair (2.5), (2.7).

#### Counterexample 2.3 (arbitrary $o(t)$ gauge cannot be reused verbatim)

Choose $t_0\in(0,1/2)$, let $t_{n+1}=t_n^2$, and, for $n\ge1$, define

\[
\psi(0)=0,\qquad
\psi(t)=t_n^2=t_{n+1}
\quad\text{for }t\in[t_n,t_{n-1}). \tag{2.9}
\]

This $\psi$ is nondecreasing and $\psi(t)/t\le t_n\to0$, but

\[
\frac{\psi(t_n)}{\psi(t_n-t_n^2)}
=\frac{t_{n+1}}{t_{n+2}}\to+\infty. \tag{2.10}
\]

Let $\lambda=1$, $p=0$, and take the graph germ formed by $(0,0)$ and

\[
(y_n,w_n)=(-t_n^2,t_n).
\]

Because $t_n<1/2$,

\[
t_{n+1}=t_n^2\le t_n-t_n^2<t_n,
\]

so $x_n:=t_n-t_n^2\in[t_{n+1},t_n)$ and
$\psi(x_n)=t_{n+1}^2=t_{n+2}$. Hence
$|y_n|=\psi(|w_n|)$, while
$|y_n|/\psi(|x_n|)\to+\infty$. Hence no fixed constant gives the
identical-gauge $J$-bound.

---

## 3. Full mapping versus branchwise residual

### Proposition 3.1 (full mapping implies every branchwise bound)

Let $p\in S$ be locally isolated. Then, on a neighborhood $U$ of $p$,

\[
d(y,S)=\|y-p\|. \tag{3.1}
\]

Hence

\[
d(y,S)\le\rho r_F(y)^q
\quad\Longrightarrow\quad
\|y-p\|\le\rho\|w\|^q
\quad
\forall (y,w)\in\operatorname{gph}F,\ y\in U, \tag{3.2}
\]

and, for a nondecreasing gauge,

\[
d(y,S)\le\psi(r_F(y))
\quad\Longrightarrow\quad
\|y-p\|\le\psi(\|w\|). \tag{3.3}
\]

#### Proof

Choose $R>0$ with $S\cap B(p,R)=\{p\}$. Sufficiently near $p$, every
other zero is farther from $y$ than $p$, proving (3.1). Now use
$r_F(y)\le\|w\|$. $\square$

### Proposition 3.2 (a sufficient converse)

Call $\Gamma$ residual-complete near $(p,0)$ if some neighborhood $U$
of $p$ and some $\eta>0$ satisfy

\[
\{(y,w):y\in U,\ w\in F(y),\ \|w\|<\eta\}\subset\Gamma. \tag{3.4}
\]

If, uniformly on $\Gamma$,

\[
\|y-p\|\le C\|w\|^q, \tag{3.5}
\]

then, after shrinking $U$,

\[
\|y-p\|\le C' r_F(y)^q. \tag{3.6}
\]

Thus the full mapping is $q$-strongly subregular at $(p,0)$.

Moreover, (3.4)--(3.5) automatically exclude every other zero in $U$:
if $0\in F(y)$, then $(y,0)\in\Gamma$ and (3.5) gives $y=p$. Thus the
word “strong” is a conclusion here, not an extra isolation assumption.

#### Proof

Restrict to $\|y-p\|<d_0$. If $r_F(y)<\eta$, choose
$w_n\in F(y)$ with $\|w_n\|\downarrow r_F(y)$; eventually
$(y,w_n)\in\Gamma$, and (3.5) gives
$\|y-p\|\le C r_F(y)^q$. If $r_F(y)\ge\eta$, use
$\|y-p\|<d_0\le(d_0/\eta^q)r_F(y)^q$. Take
$C'=\max\{C,d_0/\eta^q\}$. Empty values are harmless under
$r_F(y)=+\infty$. $\square$

Residual completeness is sufficient, not claimed minimal.

### Counterexample 3.3 (one good branch is not full MSR)

On $\mathbb R$, for $y>0$ small, set

\[
F(y):=\{y^{1/q},y^2\},\qquad F(0):=\{0\}. \tag{3.7}
\]

Set $F(y)=\varnothing$ at the remaining nearby points.

The branch $w=y^{1/q}$ satisfies $y=|w|^q$. But

\[
r_F(y)=y^2,\qquad
\frac{d(y,S)}{r_F(y)^q}=y^{1-2q}\to+\infty.
\]

So a selected-residual law cannot be relabeled as full-mapping MSR.

---

## 4. Isolated-zero reflection and local PPA

### Theorem 4.1 (isolated-zero $q$-flatness and named PPA)

Let $p\in S$ be locally isolated, let $q>1$, $\rho>0$, and suppose

\[
d(y,S)\le\rho r_F(y)^q \tag{4.1}
\]

on a neighborhood $U$ where (3.1) holds. Let $T$ be a named
single-valued resolvent branch on an input neighborhood $V$ of $p$:

\[
T(x)\in J_{\lambda F}(x),\qquad
w(x):=\frac{x-T(x)}{\lambda}\in F(T(x)), \tag{4.2}
\]

with $T(p)=p$, $T(x)\in U$, and $\|w(x)\|<\eta$, where

\[
\rho\eta^{q-1}\le\frac\lambda2. \tag{4.3}
\]

Then

\[
\boxed{
\|T(x)-p\|
\le C_q\|x-p\|^q,\qquad
C_q:=\rho\left(\frac2\lambda\right)^q.} \tag{4.4}
\]

For $R_T:=2T-I$,

\[
R_Tx-p=-(x-p)+2(T(x)-p), \tag{4.5}
\]

\[
\|R_Tx-(2p-x)\|\le2C_q\|x-p\|^q. \tag{4.6}
\]

If $p$ is an accumulation point of $V\setminus\{p\}$, then

\[
\lim_{\substack{x\to p\\x\in V,\ x\ne p}}
\frac{\|R_Tx-p\|}{\|x-p\|}=1. \tag{4.7}
\]

If $\overline{B}(p,\delta_0)\subset V$, choose
$0<\delta\le\delta_0$ and $0<\theta<1$ with

\[
C_q\delta^{q-1}\le\theta. \tag{4.8}
\]

Then $T(\overline{B}(p,\delta))\subset B(p,\delta)$. Every orbit

\[
x^{k+1}=T(x^k),\qquad x^0\in\overline{B}(p,\delta), \tag{4.9}
\]

is well-defined, converges to $p$, and satisfies

\[
r_{k+1}\le C_qr_k^q,\qquad r_k:=\|x^k-p\|, \tag{4.10}
\]

\[
r_k\le
C_q^{(q^k-1)/(q-1)}r_0^{q^k}. \tag{4.11}
\]

This is a $q$-order upper recurrence. No RL hypothesis is used.

#### Proof

Proposition 3.1 gives
$\|T(x)-p\|\le\rho\|w(x)\|^q$. By (4.3),

\[
\|x-p\|
\ge\lambda\|w(x)\|-\|T(x)-p\|
\ge\frac\lambda2\|w(x)\|.
\]

This proves (4.4). Equations (4.5)--(4.7) are immediate. From
(4.4) and (4.8),
$\|T(x)-p\|\le\theta\|x-p\|\le\theta\delta$, proving invariance and
convergence. Induction in (4.10) gives (4.11). $\square$

### Branch interpretation

Once a named branch covers an input ball, (4.4) itself yields invariance.
What must still be supplied is:

1. input-ball coverage;
2. return to the graph window where (4.1) and isolation hold;
3. iteration of this named $T$;
4. branch exclusion, only if (4.9) is replaced by arbitrary
   $x^{k+1}\in J_{\lambda F}(x^k)$.

If $T$ is defined only on a thin set $D$, one must instead prove
$T(D)\subset D$.

### Theorem 4.2 (superlinear-gauge PPA)

Replace (4.1) by

\[
d(y,S)\le\psi(r_F(y)),\qquad \psi(t)=o(t), \tag{4.12}
\]

where $\psi$ is finite and nondecreasing. Keep (4.2), and shrink the
residual window so that

\[
\psi(t)\le\frac\lambda2t\qquad(0\le t\le\eta). \tag{4.13}
\]

Then

\[
\boxed{
\|T(x)-p\|
\le\Phi(\|x-p\|),\qquad
\Phi(r):=\psi\!\left(\frac{2r}{\lambda}\right)=o(r).} \tag{4.14}
\]

Hence a sufficiently small input ball is invariant and, unless finite
termination occurs,

\[
\frac{\|x^{k+1}-p\|}{\|x^k-p\|}\to0. \tag{4.15}
\]

#### Proof

Proposition 3.1 gives
$\|T(x)-p\|\le\psi(\|w(x)\|)$. By (4.13),

\[
\|x-p\|\ge\lambda\|w(x)\|-\psi(\|w(x)\|)
\ge\frac\lambda2\|w(x)\|.
\]

Monotonicity of $\psi$ gives (4.14). Since $\Phi(r)/r\to0$, shrink the
input ball until $\Phi(r)\le\theta r$ for some $\theta<1$, and repeat the
invariance proof above. $\square$

### Proposition 4.3 (exact $Q$-order criterion)

The upper bound (4.10) is not an exact-order theorem. If a nonterminating
orbit additionally satisfies

\[
\frac{\|x^{k+1}-p\|}{\|w_k\|^q}\to\mu\in(0,+\infty),\qquad
w_k:=\frac{x^k-x^{k+1}}{\lambda}, \tag{4.16}
\]

then

\[
\boxed{
\frac{\|x^{k+1}-p\|}{\|x^k-p\|^q}
\to\frac{\mu}{\lambda^q}.} \tag{4.17}
\]

Two-sided comparability in (4.16) gives positive finite liminf and limsup
in (4.17).

#### Proof

Equation (4.16) gives
$\|x^{k+1}-p\|=o(\|w_k\|)$. Since

\[
x^k-p=(x^{k+1}-p)+\lambda w_k,
\]

$\|x^k-p\|/(\lambda\|w_k\|)\to1$, which proves (4.17).
$\square$

---

## 5. Counterexample stress tests

### 5.1 Superlinearity is necessary

Take $F(y)=y$ on $\mathbb R$, $\lambda=1$, $S=\{0\}$, and
$\psi(t)=t$. Then $x=2y$, $\widehat x=0$, so
$|\widehat x|/|x|=0$, not one. An $O(t)$ error bound does not force
asymptotic reflection.

### 5.2 The output anchor cannot be replaced

Let $H=\mathbb R^2$, $q>1$, $\lambda=1$, and

\[
F(s,z)=\big(\operatorname{sgn}(z)|z|^{1/q},z\big). \tag{5.1}
\]

Then $S=\mathbb R\times\{0\}$ and
$d((s,z),S)=|z|\le\|F(s,z)\|^q$. For $u\downarrow0$, take

\[
y=(u,u^q),\quad w=(u,u^q),\quad
x=(2u,2u^q),\quad\widehat x=(0,0).
\]

For $p_y=(u,0)$, the ratio in (1.7) tends to one. For the fixed zero
$p=(0,0)$ it is zero. For $p_x=(2u,0)$ it tends to $+\infty$, and
$d(\widehat x,S)/d(x,S)=0$. Thus fixed-anchor, input-anchor, and
set-distance substitutions all fail.

### 5.3 Full $q$-MSR does not imply resolvent coverage

On $\mathbb R$, define the closed-graph, full-domain multifunction

\[
F(y)=
\begin{cases}
\{1\},&y>0,\\
\{-1,0,1\},&y=0,\\
\{-1\},&y<0.
\end{cases} \tag{5.2}
\]

Here $S=\{0\}$ and, for $0<|y|<1$, $|y|\le r_F(y)^q=1$ for every
$q>0$. Yet

\[
\operatorname{rge}(I+\lambda F)
=(-\infty,-\lambda]\cup\{0\}\cup[\lambda,+\infty),
\]

which contains no neighborhood of zero.

### 5.4 A named branch does not control the full resolvent

Let $\lambda=1$, $q>1$, and
$T(x):=\operatorname{sgn}(x)|x|^q$ for small $|x|$. Define a relation
from the union of

\[
(T(x),x-T(x))
\quad\text{and}\quad
(1+x,-1). \tag{5.3}
\]

Both graph pairs have Minty input $x$. The first branch has an isolated
zero, local $q$-MSR, and update $T(x)$. The second changes no mapping
property near $y=0$, but makes $1+x$ another full-resolvent value at the
same small input. Arbitrary selections therefore need branch exclusion.

### 5.5 Even a sharp full exponent need not be the exact orbit order

Fix $r>q>1$ and define, for small nonzero $y$,

\[
F(y)=
\left\{
\operatorname{sgn}(y)|y|^{1/q},
\operatorname{sgn}(y)|y|^{1/r}
\right\},\qquad F(0)=\{0\}. \tag{5.4}
\]

The full residual is $r_F(y)=|y|^{1/q}$, so $q$ is its largest power
exponent. The resolvent branch using the second value satisfies

\[
|x|=|y|+\lambda|y|^{1/r}
\sim\lambda|y|^{1/r},\qquad
|y|\sim\lambda^{-r}|x|^r.
\]

Its exact order is $r>q$. Thus exactness needs a branchwise lower
asymptotic such as (4.16).

### 5.6 Moving-anchor flatness does not imply all-pairs Lipschitzness

Fix $0<\gamma<1<q$, set $\beta=q/\gamma-1$, and define

\[
h(t):=|t|^q\sin(|t|^{-\beta}),\quad h(0):=0,
\]

\[
\operatorname{gph}F
=\{(h(t),t-h(t)):|t|\le\varepsilon\},\qquad\lambda=1. \tag{5.5}
\]

Then $J(t)=h(t)$, $R(t)=2h(t)-t$, and $S=\{0\}$. Full $q$-MSR holds
because every representing parameter satisfies
$|h(t)|\le|t|^q$ and $|t-h(t)|\ge|t|/2$ locally; taking the infimum
over all representations preserves the same bound. A two-scale estimate gives

\[
|h(t)-h(s)|\le C|t-s|^{q/(\beta+1)}
=C|t-s|^\gamma.
\]

On scales $|t-s|\gtrsim|t|^{\beta+1}$ use the amplitude
$O(|t|^q)$; on smaller scales use
$|h'(\xi)|=O(|\xi|^{q-\beta-1})$. Adjacent opposite phase extrema satisfy

\[
|t_n-s_n|\asymp t_n^{\beta+1},\qquad
|h(t_n)-h(s_n)|\asymp t_n^q.
\]

Because $q<\beta+1$, the identity term cannot cancel this difference in
$R$. Hence $R$ has sharp all-pairs exponent $\gamma<1$, although
$J(t)=O(|t|^q)$ and $R(t)=-t+O(|t|^q)$ at the zero.

---

## 6. Claim-safe merger summary

1. A superlinear full residual gauge forces asymptotic reflection only
   around an output-nearest or $o(\|w\|)$-accurate output-near zero.
2. Fixed-anchor branchwise residual flatness, resolvent flatness, and
   centered reflection-defect flatness are equivalent. Arbitrary gauges
   are rescaled; literal same-gauge equivalence requires dilation
   stability.
3. At an isolated zero, full $q>1$ subregularity gives
   $J_\Gamma x-p=O(\|x-p\|^q)$ on every existing small-residual Minty
   branch; RL is unnecessary.
4. Once a named branch covers an input ball, $q$-flatness makes a smaller
   ball invariant. Arbitrary full-resolvent PPA still needs branch
   exclusion.
5. One-sided MSR proves a $q$-order upper recurrence, not exact order.
   Exact $q$ needs a two-sided branchwise asymptotic.

No statement above claims literature novelty, optimal global constants,
full-resolvent maximality, or a universal all-pairs RL exponent.

---

## 7. Independent review ledger

### Fact base and three lenses

- Paper family: theoretical.
- Bounded package: moving-anchor reflection, gauge extension,
  fixed-anchor flatness, and isolated-zero local PPA.
- Evidence boundary: internal derivation only; no prior-art or journal
  verification.

| Lens | Finding | Severity | Repair embodied here |
|---|---|---:|---|
| Contribution | The separation of all-pairs roughness, moving-anchor reflection, and branchwise PPA survives. | — | Claim-safe decomposition retained. |
| Methods | Power proofs survive after quantifiers are printed. Arbitrary same-gauge equivalence and exact-$q$ wording do not. | Major | Rescaled gauges, explicit branch hypotheses, and an exact-order criterion added. |
| Communication | Full residual, selected residual, named branch, and arbitrary full-resolvent selection were conflated. | Major | Separate propositions and counterexamples added. |

Bounded-package readiness: **CONDITIONALLY_READY** for merger after one
independent line-by-line orchestrator audit. This is not a readiness
judgment on the full RL manuscript or stage.

## Expert contract

~~~yaml
contract_version: "1.0"
expert_skill: independent-proof-analysis
project_id: monotonicity-regularity-seesaw-2026-09
paper_family: T
stage_id: T2
task_id: RL-FND-ANCHOR-03
task_status: COMPLETE
inputs_reviewed:
  - work/rl_genuine_exponent.md
  - work/rl_proof_referee.md
  - research/theory_atlas.md
  - work/b_algorithm_anchored.md
  - upload/01-RL_Submonotonicity-.md
outputs:
  - work/rl_foundations_anchor_theorems.md
evidence_status:
  - VERIFIED_USER_MATERIAL: source definitions, draft claims, and project examples were inspected locally
  - AI_INFERENCE: theorem proofs, minimal hypotheses, constants, and counterexamples were independently derived
  - EXECUTED_LOCAL: file searches, cross-checks, and artifact validation were run in the shared workspace
assumptions:
  - lambda is fixed and strictly positive
  - local mapping error bounds use the printed residual and solution set
  - named branches return graph points inside the printed localization
  - no literature novelty is inferred from algebraic correctness
author_input_needed: []
manual_actions: []
quality_checks:
  - rederived moving-anchor ratio and defect constants from a=y-p and t=lambda*w
  - separated approximate from exact projections
  - proved power equivalence in both directions with explicit shrinking
  - replaced false arbitrary same-gauge equivalence by rescaled gauges plus dilation stability
  - separated full-mapping from selected branchwise residuals
  - separated named-branch PPA from arbitrary full-resolvent selections
  - derived ball invariance once coverage is available
  - distinguished q-order upper recurrence from exact Q-order
  - stress-tested all identified overstrong variants
  - made no literature, novelty, maximality, or journal-placement claim
conflicts:
  - conflict_id: RL-FND-GAUGE-SAME
    conflict_type: theorem_scope
    claim: every nondecreasing psi=o(t) yields same-gauge branchwise equivalence up to constants
    source_or_locator: work/rl_genuine_exponent.md, section 9.3 proposal
    competing_interpretations:
      - literal same-gauge equivalence for arbitrary superlinear gauges
      - rescaled-gauge equivalence, with same-gauge form only under dilation stability
    recommended_resolution: adopt Theorem 2.2 and Counterexample 2.3
  - conflict_id: RL-FND-EXACT-Q
    conflict_type: claim_strength
    claim: full q-subregularity alone gives exact PPA Q-order q
    source_or_locator: informal wording around work/rl_genuine_exponent.md, Corollary 3.2
    competing_interpretations:
      - exact order q
      - q-order upper recurrence, exact only with a two-sided branchwise asymptotic
    recommended_resolution: adopt Theorem 4.1 and Proposition 4.3
  - conflict_id: RL-FND-BRANCH-FULL
    conflict_type: quantifier_scope
    claim: a named local branch automatically governs arbitrary full-resolvent selections
    source_or_locator: original PPA inclusion wording audited in work/rl_proof_referee.md
    competing_interpretations:
      - arbitrary full-resolvent PPA
      - named localized branch unless branch exclusion is proved
    recommended_resolution: retain named-branch wording and print branch exclusion separately
conflict_resolution_status: UNRESOLVED
merge_permission: orchestrator_only
recommended_next_action: have the orchestrator perform one independent line-by-line proof audit and then merge this package into the RL foundations document
stage_acceptance_recommendation: NOT_ASSESSED
~~~
