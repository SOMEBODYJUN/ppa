# 真实图值的非精确 RLEB：可计算停止准则与全部允许输出

- **ID / Version**：IRF-v1，候选正文；未分配总账编号。
- **Status**：`candidate`，保留较广推导身份。普通真实图停止规则已另以 [C275](../topics/inexact_ppa/real_graph_stopping.md) 独立写定、冷读并接收；本页其余物理 GPPA 和预算扩展不据此自动升级，外部先行性未定。不改 C02-v3、C213 或 C249 的身份。
- **Scope**：有限维物理空间、固定完整关系及其明定图块、完整闭零集、真实图值、局部残差窗。停止准则不调用解集距离，也不调用精确近端解。全部结论统一控制每个通过同一准则的输出。
- **Dependencies**：[C02-v3](../canonical/true_residual_selection_rleb.md)、[C249](../canonical/physical_rleb_gppa.md) 提供比较对象；本页证明自足。[C213](../canonical/gppa_inexact_modulus.md) 是不同的输出扰动模型。
- **Writing contract**：先说明算法实际计算的量，再证明非空性、吸收估计和有限前缀留域，随后给出幂次系数、核版本和失败边界。研究价值与文献新颖性分开判断。

## 1. 普通 PPA 的可计算残差准则

令 \(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，\(\lambda>0\)，并假设完整零集
\[
 S=F^{-1}(0)
\]
非空闭。完整真残差为
\(r_F(y)=\inf_{w\in F(y)}\|w\|\)，空纤维取 \(+\infty\)。
取开集 \(U\subset X\)、半径 \(R,\rho>0\)，定义
\(U_R=\{x\in U:d(x,S)\le R\}\)。
固定图块 \(\mathcal G\subset\operatorname{gph}F\)，并要求
\(S\times\{0\}\subset\mathcal G\)。取有限非减函数
\[
 \omega:[0,\rho]\to[0,\infty),\qquad
 \psi:[0,\bar t]\to[0,\infty),
\]
它们在零点连续且为零。定义 \(B(t)=(t+\omega(t))/2\)。

一个内层求解器返回真实图对 \((y,w)\in\mathcal G\)，然后计算
\[
 e=x-y-\lambda w,\qquad u=\lambda\|w\|.
 \tag{IRF1}
\]
给定 \(\eta\ge0\) 和 \(\bar u>0\)，接受当且仅当
\[
 \boxed{\quad u\le\bar u,\qquad
          \|e\|\le\eta\,\psi(\|w\|).\quad}
 \tag{IRF2}
\]
所有这种输出组成 \(\mathcal A(x)\)。\(\eta=0\) 恢复精确图块近端关系。
这里 \(\psi(\|w\|)\) 是可计算的所选图值范数的函数；它既不等于真实残差，也不等于未知输出距离。

### IRF-A · 一般模定理的全部前提

要求以下条件同时成立。

1. **真实图块与零锚比较。** 对每个 \((y,w)\in\mathcal G\) 和每个 \(p\in S\)，若
   \(\|y+\lambda w-p\|\le\rho\)，则
   \[
   \|y-\lambda w-p\|
       \le\omega(\|y+\lambda w-p\|).
   \tag{IRF3}
   \]
   这是局部零锚条件；不要求两个非零图点间比较，不强制同输入唯一。

2. **精确种子覆盖。** 每个 \(x\in U_R\) 至少有一个 \((y,w)\in\mathcal G\) 满足 \(x=y+\lambda w\)。不要求在扰动点 \(x-e\) 另有覆盖。

3. **完整真残差 EB。** 对每个 \(y\in\pi_X\mathcal G\)，若 \(r_F(y)\le\bar t\)，则
   \[
   d(y,S)\le\psi(r_F(y)).
   \tag{IRF4}
   \]
   该条件覆盖可能在 \(U\) 外的实际候选输出，不能先假设输出留域。

4. **共同窗与标量兼容。** 令
   \[
   \widehat B(t)=\min\{\bar u,B(t)\},\qquad 0\le t\le\rho.
   \]
   存在 \(0<\kappa_0<1\) 使
   \[
   \bar u/\lambda\le\bar t,\quad B(R)\le\bar u,\quad
   R+\eta\psi(\bar u/\lambda)\le\rho,
   \tag{IRF5}
   \]
   \[
   \psi(\widehat B(t)/\lambda)\le\kappa_0t
       \quad(0<t\le\rho),\qquad
   \kappa_0(1+\eta)<1.
   \tag{IRF6}
   \]
   IRF5 implies \(R\le\rho\), so \(B(R)\) is defined. The truncation in \(\widehat B\) keeps every evaluation of \(\psi\) inside \([0,\bar t]\).

5. **物理长度条件。** Put
   \[
   \kappa=\frac{\kappa_0}{1-\eta\kappa_0}\in(0,1),\qquad
   H(t)=\widehat B\!\left(\min\left\{\rho,
                   \frac{t}{1-\eta\kappa_0}\right\}\right)
                   +\eta\kappa t,
   \tag{IRF7}
   \]
   \[
   \Theta(t)=\sum_{j=0}^{\infty}H(\kappa^jt),
       \quad 0\le t\le R,
   \]
   and require \(\Theta(R)<\infty\). A sufficient condition is
   \(\int_0^\rho\omega(t)\,dt/t<\infty\).
   The minimum with \(\rho\) in IRF7 is necessary unless the stronger window \(R/(1-\eta\kappa_0)\le\rho\) is separately imposed.

### IRF-T · 全部接受输出的收敛定理

Under IRF-A, \(\mathcal A(x)\ne\varnothing\) for every \(x\in U_R\).
For every \(x^0\in U_R\) satisfying
\[
 \Theta(d_0)<d(x^0,X\setminus U),\qquad d_0=d(x^0,S),
 \tag{IRF8}
\]
every sequence \(x^{k+1}\in\mathcal A(x^k)\) can be continued indefinitely, stays in \(U_R\), has finite physical length, and converges to some \(x^\infty\in S\cap U\). Uniformly over all accepted witnesses and choices,
\[
 d(x^k,S)\le\kappa^k d_0,
 \tag{IRF9}
\]
\[
 \|x^{k+1}-x^k\|\le H(d(x^k,S))\le H(\kappa^k d_0),
 \qquad
 \sum_{k\ge0}\|x^{k+1}-x^k\|\le\Theta(d_0),
 \tag{IRF10}
\]
\[
 \|x^\infty-x^k\|\le\Theta(d(x^k,S))
       \le\Theta(\kappa^kd_0).
 \tag{IRF11}
\]
In particular, \(\mathcal A(x)=\{x\}\) for every \(x\in S\cap U_R\).

**Proof.** First take a legal input \(x\), an arbitrary accepted witness \((y,w)\), and a nearest point \(p\in P_S(x)\). Such \(p\) exists because \(S\) is nonempty closed in finite dimension. Set
\[
 d=d(x,S),\quad E=\|e\|,\quad
 z=\psi(u/\lambda),\quad
 \tau=\|y+\lambda w-p\|=\|x-e-p\|.
\]
The acceptance rule and IRF5 give
\[
 \tau\le d+E\le R+\eta\psi(\bar u/\lambda)\le\rho.
 \tag{IRF12}
\]
Consequently IRF3 applies to this actual graph point, even if \(y\notin U\). The identity
\(2\lambda w=(y+\lambda w-p)-(y-\lambda w-p)\) gives
\[
 u\le B(\tau)\le B(d+E),\qquad
 u\le\widehat B(d+E).
 \tag{IRF13}
\]
All gauge arguments in the following line belong to \([0,\bar t]\):
\[
 z=\psi(u/\lambda)
 \le\psi(\widehat B(d+E)/\lambda)
 \le\kappa_0(d+E)
 \le\kappa_0(d+\eta z).
 \tag{IRF14}
\]
At \(d+E=0\), the same inequality holds directly because \(B(0)=0\). Absorption therefore yields
\[
 z\le\kappa d,\qquad E\le\eta\kappa d,
 \qquad d+E\le\frac{d}{1-\eta\kappa_0}.
 \tag{IRF15}
\]
Since \(w\in F(y)\), the correct true-residual chain is
\[
 r_F(y)\le\|w\|\le\bar u/\lambda\le\bar t,
 \qquad d(y,S)\le\psi(r_F(y))\le z\le\kappa d.
 \tag{IRF16}
\]
No minimum-residual graph selection was used. Combining IRF12, IRF13 and IRF15 gives the bound for \(u\) in IRF7. Finally
\(\|x-y\|\le u+E\le H(d)\).

At \(d=0\), IRF15 gives \(z=E=0\), hence \(\tau=0\), \(u=0\) by IRF13, and \(y=x\). This proves zero absorption even if \(\psi\) is not strictly increasing.

For nonemptiness, take an exact seed \(x=y+\lambda w\) furnished by IRF-A.2. The same nearest point gives \(\tau=d\le R\), so IRF3 gives \(u\le B(d)\le B(R)\le\bar u\). Its defect vanishes and it passes IRF2. This argument invokes geometry before the cap, avoiding a circular assumption that the exact seed was already accepted.

The one-step inequalities now apply to every accepted output. If a trajectory has been constructed through \(x^k\in U_R\), then
\[
 d(x^{k+1},S)\le\kappa^{k+1}d_0,\qquad
 \|x^{k+1}-x^0\|\le\sum_{j=0}^kH(\kappa^jd_0)
 \le\Theta(d_0)<d(x^0,X\setminus U).
\]
Thus the new point lies in \(U_R\), and nonemptiness permits the next step. This finite-prefix induction proves retention and indefinite continuation. Summable steps give a Cauchy sequence; completeness, closedness of \(S\), and vanishing distances give its limit in \(S\). The same strict budget places the limit in \(U\). Summing from any index gives IRF11.

For the stated Dini sufficient condition, the finitely many indices where the argument in IRF7 is truncated cause no problem. For all remaining indices, monotonicity compares the geometric series of \(B(ct)\), \(c=(1-\eta\kappa_0)^{-1}\), with its Dini integral. The linear term is summable. This proves \(\Theta(R)<\infty\). \(\square\)

**Local basin.** Since \(H(0)=0\), \(H\) is nondecreasing and continuous at zero, and \(\Theta(R)<\infty\), dominated convergence for the series gives \(\Theta(t)\to0\). For any \(\bar x\in S\cap U\) and \(B_b(\bar x)\subset U\), choose \(0<\delta\le R\) with \(\delta+\Theta(\delta)<b\). Every initial point in \(B_\delta(\bar x)\) satisfies IRF8 and all accepted trajectories remain in the outer ball. No same-radius self-map claim is made.

**Full-fiber scope.** Taking \(\mathcal G=\operatorname{gph}F\) gives every real-graph output passing IRF2. For a proper graph block, the conclusion covers precisely the block's accepted outputs. Existence of an exact block seed never excludes accepted outputs of the complete graph outside that block.

### IRF-PHI · 统一可计算误差预算

The normalized gauge rule is one instance of a more general forcing budget. Fix a finite nondecreasing function
\(\phi:[0,\bar u]\to[0,\infty)\), continuous at zero with \(\phi(0)=0\), and accept every genuine graph pair satisfying
\[
 u\le\bar u,\qquad E\le\phi(u).
 \tag{IRF38}
\]
Retain IRF-A.1–3 and replace IRF5–7 by
\[
 \bar u/\lambda\le\bar t,\quad B(R)\le\bar u,\quad
 R+\phi(\bar u)\le\rho,
 \tag{IRF39}
\]
\[
 \psi(\widehat B(t)/\lambda)\le\kappa_0t,\qquad
 \phi(\widehat B(t))\le\theta t
 \quad(0\le t\le\rho),\qquad
 \kappa_0>0,\quad\theta\ge0,\quad\kappa_0+\theta<1.
 \tag{IRF40}
\]
Define
\[
 \kappa=\frac{\kappa_0}{1-\theta}<1,\qquad
 H_\phi(t)=\widehat B\!\left(\min\left\{\rho,
                         \frac{t}{1-\theta}\right\}\right)
                    +\frac{\theta t}{1-\theta},
 \quad
 \Theta_\phi(t)=\sum_{j\ge0}H_\phi(\kappa^jt).
 \tag{IRF41}
\]
Assume \(\Theta_\phi(R)<\infty\), for which the same Dini condition is sufficient. Then IRF-T holds verbatim with these quantities and the initial budget \(\Theta_\phi(d_0)<d(x^0,X\setminus U)\).

Indeed, the cap and IRF39 first give \(d+E\le\rho\), so the actual graph comparison yields \(u\le\widehat B(d+E)\). Both one-step estimates then follow from
\[
 E\le\phi(u)\le\theta(d+E),\qquad
 \psi(u/\lambda)\le\kappa_0(d+E).
\]
Absorbing the first gives \(E\le\theta d/(1-\theta)\), and the second gives distance contraction by \(\kappa\). These imply IRF41. When \(d=0\), the same absorption gives \(E=0\), and graph geometry forces \(u=0,y=x\). Exact seeds pass IRF38 since their defect is zero and the geometry proves their cap. The finite-prefix and tail proofs remain unchanged.

The original rule is recovered by
\[
 \phi(u)=\eta\psi(u/\lambda),\qquad\theta=\eta\kappa_0.
\]
Thus this is a single error-budget theorem with different computable choices of budget, not a new family of unrelated convergence principles.

For \(\omega(t)=Lt^\gamma\), \(\psi(r)=cr^p\), and \(\phi(u)=a u^q\), a simple sufficient small-scale test is
\[
 \kappa_0(\rho)=\frac{c}{\lambda^p2^p}
   \rho^{\gamma p-1}(\rho^{1-\gamma}+L)^p,
 \qquad
 \theta(\rho)=\frac{a}{2^q}
   \rho^{\gamma q-1}(\rho^{1-\gamma}+L)^q,
 \tag{IRF42}
\]
provided \(\gamma p\ge1\), \(\gamma q\ge1\), and \(\kappa_0(\rho)+\theta(\rho)<1\). These conditions make the displayed bounds nondecreasing as functions of the input scale; the cap only improves them. If both products exceed one, any fixed finite positive coefficients can be accommodated by shrinking the common window. If either product equals one, the corresponding coefficient survives in the limiting budget. The theorem separates the EB exponent \(p\) from the implementable forcing exponent \(q\). Section 4 and the independent sharp-family candidate provide necessity statements for their specified examples; IRF42 alone is only a sufficient general certificate.

## 2. 临界 Hölder 情形的显式系数

Let \(0<\gamma\le1\), \(p=1/\gamma\), \(L\ge0\), \(c>0\), and choose
\[
 \omega(t)=Lt^\gamma,\qquad \psi(r)=cr^p.
\]
Define
\[
 C_\rho=\frac{(\rho^{1-\gamma}+L)^p}{2^p},\qquad
 \kappa_0=\frac{cC_\rho}{\lambda^p}.
 \tag{IRF17}
\]
For \(0<t\le\rho\),
\[
 B(t)^p=t\frac{(t^{1-\gamma}+L)^p}{2^p}\le C_\rho t.
\]
Thus the scalar compatibility follows whenever
\[
 \boxed{\quad (1+\eta)cC_\rho<\lambda^p.\quad}
 \tag{IRF18}
\]
This argument evaluates only the polynomial upper bound and does not require an EB assertion beyond the true-residual window. IRF5 remains in force. The implementable stopping rule is
\[
 \|x-y-\lambda w\|\le\eta c\|w\|^p,
 \qquad\lambda\|w\|\le\bar u.
 \tag{IRF19}
\]
Writing
\[
 A_\rho=\frac{C_\rho}{1-\eta cC_\rho/\lambda^p},\qquad
 \kappa=\frac{cA_\rho}{\lambda^p},
\]
the direct absorption calculation yields the simpler uniform bounds
\[
 u^p\le A_\rho d(x,S),\qquad
 \|x-y\|\le A_\rho^{1/p}d(x,S)^{1/p}+\eta\kappa d(x,S),
 \tag{IRF20}
\]
and the explicit length budget
\[
 \Theta_p(t)=
 \frac{A_\rho^{1/p}t^{1/p}}{1-\kappa^{1/p}}
 +\frac{\eta\kappa t}{1-\kappa}.
 \tag{IRF21}
\]
Using \(\Theta_p\) instead of \(\Theta\) in the strict initial budget gives all conclusions. Point-error R-factor is at most \(\kappa^{1/p}=\kappa^\gamma\); no one-step point-error Q-factor is claimed.

For \(0<\gamma<1\), as \(\rho\downarrow0\) the sufficient coefficient becomes
\[
 (1+\eta)c(L/(2\lambda))^p<1.
 \tag{IRF22}
\]
The strict inequality is a sufficient certificate, not a universal necessary condition for each operator. Section 4 supplies a complete operator family where its normalized limiting error threshold is attained.

If the rule is instead parameterized as \(E\le\widetilde\eta u^p\), then \(\widetilde\eta=\eta c/\lambda^p\), and the critical condition is
\[
 C_\rho(\widetilde\eta+c/\lambda^p)<1.
\]
The two parameterizations must not be mixed when quoting an admissible error constant.

### IRF-INV · 利用反射逆模的较宽停止准则

The residual-gauge rule is particularly natural at the critical power balance. When \(\psi(u/\lambda)\) is much smaller than the input scale needed to produce \(u\), it asks for more inner accuracy than this proof needs. The following computable alternative separates the distance decrease from the control of physical length.

Retain IRF-A.1–3, the functions and \(\kappa_0\) in IRF6, but replace the acceptance rule and its windows as follows. Choose
\[
 0<\theta<1,\qquad \kappa_0<\kappa<1,\qquad
 0<\bar u\le\min\{\lambda\bar t,B(\rho)\}.
\]
Define the generalized inverse, on the full acceptance interval, by
\[
 Q(u)=\inf\{t\in[0,\rho]:u\le B(t)\},\qquad 0\le u\le\bar u.
 \tag{IRF33}
\]
This is a known scalar function of the reflection modulus, not a distance to \(S\). It is finite and nondecreasing, \(Q(0)=0\), and \(Q(u)>0\) for \(u>0\), by continuity of \(B\) at zero. Assume
\[
 B(R)\le\bar u,\qquad R+\theta Q(\bar u)\le\rho.
 \tag{IRF34}
\]
Accept all real graph pairs with \(u\le\bar u\) and
\[
 \boxed{\quad
 E\le\min\left\{\theta Q(u),\,
                 Q(u)-\frac{\psi(u/\lambda)}{\kappa}\right\}.
 \quad}
 \tag{IRF35}
\]
Then IRF9–11 hold with the prescribed \(\kappa\), the step bound
\[
 H_\theta(t)=\widehat B\!\left(\min\left\{\rho,
                           \frac{t}{1-\theta}\right\}\right)
                      +\frac{\theta t}{1-\theta},
 \tag{IRF36}
\]
and the corresponding summable length budget. Dini continuity of \(\omega\) again suffices.

To prove this, observe first that the compatibility already assumed implies
\[
 \psi(u/\lambda)\le\kappa_0 Q(u),\qquad 0\le u\le\bar u.
 \tag{IRF37}
\]
Indeed, for every \(t\) with \(u\le B(t)\), one has
\(u\le\widehat B(t)\) and \(\psi(u/\lambda)\le\kappa_0t\); take the infimum over such \(t\). No continuity of \(\omega\) away from zero or attainment in IRF33 is needed. Thus the right side of IRF35 is nonnegative, and all exact seeds pass it.

For an accepted pair, IRF34 ensures \(d+E\le\rho\), so the same graph geometry gives \(u\le B(d+E)\), hence \(Q(u)\le d+E\). The two parts of IRF35 then give separately
\[
 \psi(u/\lambda)\le\kappa[Q(u)-E]\le\kappa d,
 \qquad
 Q(u)\le\frac d{1-\theta},\quad
 E\le\frac{\theta d}{1-\theta}.
\]
These prove distance contraction and IRF36. At zero distance, they force \(E=Q(u)=0\), so \(u=0\) and \(y=x\). The rest of the proof is exactly the finite-prefix argument above.

A simpler special case accepts \(E\le\theta Q(u)\) with \(\theta<1-\kappa_0\), giving \(\kappa=\kappa_0/(1-\theta)\). IRF35 is wider because it permits a separate \(\theta\) close to one while using the measured residual to enforce the requested distance factor.

This simpler choice is precisely IRF-PHI with \(\phi(u)=\theta Q(u)\). To check its assumptions even when \(B\) has jumps, note that \(Q\) is nondecreasing, finite on \([0,\bar u]\), and \(Q(0)=0\). For each fixed \(t>0\), \(B(t)>0\); whenever \(0\le u\le\min\{\bar u,B(t)\}\), the definition gives \(Q(u)\le t\). Thus \(Q(u)\to0\) as \(u\downarrow0\). Finally \(\widehat B(t)\le B(t)\) implies directly \(Q(\widehat B(t))\le t\), whether or not the infimum defining \(Q\) is attained. These facts prove the forcing-budget condition in IRF40.

The original gauge rule is contained in this scalar acceptance rule on common windows: if \(E\le\eta\psi(u/\lambda)\), set \(\theta=\eta\kappa_0<1\) and \(\kappa=\kappa_0/(1-\eta\kappa_0)\). Equation IRF37 gives both inequalities in IRF35. For \(\eta=0\), the same conclusion holds with any positive \(\theta\) and any \(\kappa>\kappa_0\). This inclusion compares the tests under a shared certified window; it does not assert that the differing sufficient window inequalities automatically imply one another.

For \(B(t)\sim(L/2)t^\gamma\), \(Q(u)\sim(2u/L)^{1/\gamma}\). Thus its forcing exponent is still \(1/\gamma\), while in the supercritical regime it can allow substantially more error than the EB gauge \(\psi(u/\lambda)\). This is another candidate interface, not an independent novelty claim.

## 3. 物理 GPPA 的真实图缺陷版本

The same absorption works for a fixed everywhere-defined kernel \(v:X\to X\), without requiring that \(v(x)-e\) be in \(v(X)\). This is useful when a perturbed kernel input cannot be represented by a perturbed physical point.

Fix \(A>0\), \(\beta>0\), and retain the physical complete zero set \(S\), the graph block \(\mathcal G\), the residual gauge and the windows. Replace IRF1 by
\[
 e=v(x)-v(y)-\lambda w,\qquad u=\lambda\|w\|,
\]
and accept all real graph pairs satisfying
\[
 u\le\bar u,\qquad \|e\|\le\eta\psi(\|w\|)^\beta.
 \tag{IRF23}
\]
Assume the following conjunction.

- For each \(x\in U_R\), there is a nearest physical zero \(p\in P_S(x)\) with \(\|v(x)-v(p)\|\le A d(x,S)^\beta\).
- For every \(p\in S\) and \((y,w)\in\mathcal G\) such that \(\|v(y)+\lambda w-v(p)\|\le\rho\),
  \[
  \|v(y)-\lambda w-v(p)\|
    \le\omega(\|v(y)+\lambda w-v(p)\|).
  \tag{IRF24}
  \]
- Every \(x\in U_R\) has an exact graph seed \(v(x)=v(y)+\lambda w\), \((y,w)\in\mathcal G\).
- The same physical true-residual EB IRF4 holds. For all accepted transitions, including outputs not yet known to be in \(U\), there is a common physical transfer bound
  \[
  \|x-y\|\le h(d(x,S),\|v(x)-v(y)\|),
  \tag{IRF25}
  \]
  where \(h:[0,\infty)^2\to[0,\infty)\) is finite, nondecreasing in each argument, continuous at \((0,0)\), and \(h(0,0)=0\).
- For some \(C>0\),
  \[
  \psi(\widehat B(t)/\lambda)^\beta\le Ct\quad(0\le t\le\rho),
  \qquad C(A+\eta)<1,
  \tag{IRF26}
  \]
  \[
  \bar u/\lambda\le\bar t,\quad B(AR^\beta)\le\bar u,\quad
  AR^\beta+\eta\psi(\bar u/\lambda)^\beta\le\rho.
  \tag{IRF27}
  \]

Set
\[
 \kappa=\left(\frac{CA}{1-C\eta}\right)^{1/\beta}<1,
\]
\[
 V(t)=\widehat B\!\left(\min\left\{\rho,
                 \frac{At^\beta}{1-C\eta}\right\}\right)
           +\eta\kappa^\beta t^\beta,
 \qquad H_v(t)=h(t,V(t)),
\]
and assume \(\Theta_v(R)=\sum_{j\ge0}H_v(\kappa^jR)<\infty\). Then the theorem of Section 1 holds with this \(\kappa,H_v,\Theta_v\) for every accepted GPPA output.

**Proof.** Use the nearest physical zero in the first assumption. For an accepted pair,
\[
 \|v(y)+\lambda w-v(p)\|
 \le A d^\beta+E\le\rho.
\]
The zero-anchor geometry gives \(u\le\widehat B(A d^\beta+E)\). With \(z=\psi(u/\lambda)^\beta\), the crucial inequality is
\[
 z\le C(A d^\beta+E)\le C(A d^\beta+\eta z).
\]
Hence \(z\le\kappa^\beta d^\beta\), so true EB gives \(d(y,S)\le\kappa d\). Also
\[
 \|v(x)-v(y)\|\le u+E\le V(d),\qquad
 \|x-y\|\le H_v(d).
\]
At \(d=0\), absorption gives \(E=z=0\), geometry gives \(u=0\), and IRF25 forces \(y=x\), including invisible kernel directions. Exact seed coverage and IRF27 prove nonemptiness exactly as before. The finite-prefix retention, length and tail proof uses the same inequalities and the physical budget \(\Theta_v(d_0)<d(x^0,X\setminus U)\). \(\square\)

When \(v=I,A=\beta=1,h(t,s)=s\), this reduces exactly to the ordinary theorem with \(C=\kappa_0\). With \(\eta=0\), it is the power-anchor part of C249 under the stronger graph-level zero-anchor condition used here. The generic C249 condition only tests its exact allowed outputs; it cannot automatically control the new inexact outputs. That additional geometry must be proved.

Neither a noninjective kernel nor its true residual EB controls motion inside a kernel fiber. IRF25 remains essential, just as in C249. The theorem does not infer it from the kernel equation.

The unified budget IRF-PHI also transfers to this physical setting. Replace IRF23 by \(E\le\phi(u)\), and assume
\[
 \psi(\widehat B(t)/\lambda)^\beta\le Ct,\qquad
 \phi(\widehat B(t))\le\theta t,\qquad CA+\theta<1,
 \tag{IRF43}
\]
with the joint window \(AR^\beta+\phi(\bar u)\le\rho\), the same exact-seed and residual windows, and the same physical transfer. Then
\[
 E\le\theta(Ad^\beta+E),\qquad
 \kappa=\left(\frac{CA}{1-\theta}\right)^{1/\beta},
\]
\[
 V_\phi(t)=\widehat B\!\left(\min\left\{\rho,
                          \frac{At^\beta}{1-\theta}\right\}\right)
                      +\frac{\theta A t^\beta}{1-\theta}.
\]
Use \(H_v(t)=h(t,V_\phi(t))\) and its summable geometric budget. The same proof gives all conclusions. Taking \(\phi(u)=\eta\psi(u/\lambda)^\beta\), \(\theta=\eta C\), recovers IRF23–27 exactly. Thus forcing powers can be chosen independently of the physical EB power also for a nonlinear kernel.

## 4. 两个实际反例：相对误差与远端输出

Fix \(0<b<1\), \(0<\gamma<1\), \(p=1/\gamma\), \(\lambda=1\), and the complete single-valued continuous operator
\[
 F(u,v)=\left(-(|v|/b)^\gamma,\frac{1-b}{b}v\right)
       \quad\text{on }\mathbb R^2.
 \tag{IRF28}
\]
Its complete zero set is \(S=\mathbb R\times\{0\}\). Solving \(x=y+F(y)\) gives the complete, everywhere-defined exact proximal map
\[
 T(t,s)=(t+|s|^\gamma,bs).
 \tag{IRF29}
\]
The complete true residual satisfies
\[
 r_F(u,v)=\left((|v|/b)^{2\gamma}
              +((1-b)v/b)^2\right)^{1/2},\qquad
 |v|\le b\,r_F(u,v)^p.
 \tag{IRF30}
\]
For a graph point with Minty input \(z=(t,s)\) and an arbitrary zero \(p_0=(q,0)\),
\[
 2Tz-z-p_0=(t-q+2|s|^\gamma,(2b-1)s).
\]
Because \(|2b-1|\le1\), this has norm at most
\(\|z-p_0\|+2\|z-p_0\|^\gamma\). Thus the complete graph satisfies IRF3 with
\[
 \omega(t)=t+2t^\gamma,\quad B(t)=t+t^\gamma,\quad
 \psi(r)=br^p,
 \qquad\kappa_0=b(1+\rho^{1-\gamma})^p<1
 \tag{IRF31}
\]
for sufficiently small \(\rho\). In fact the same modulus also holds between arbitrary Minty input pairs, since \(||s|^\gamma-|s'|^\gamma|\le|s-s'|^\gamma\).

### IRF-REL · 固定相对残差或相对步长误差会失败

Fix \(s>0\) and choose the genuine graph witnesses and outputs
\[
 x^k=(k s^\gamma,bs),\quad y=x^{k+1},\quad
 w=(-s^\gamma,(1-b)s),\quad e=(0,-(1-b)s).
 \tag{IRF32}
\]
They satisfy \(e=x^k-y-w\) and \(w=F(y)\). Moreover
\[
 \frac{\|e\|}{\|w\|}
 =\frac{(1-b)s}{\sqrt{s^{2\gamma}+(1-b)^2s^2}}\to0,
 \qquad
 \frac{\|e\|}{\|x^k-y\|}=(1-b)s^{1-\gamma}\to0.
\]
For every fixed \(\sigma>0\), both familiar relative rules
\(\|e\|\le\sigma\|w\|\) and
\(\|e\|\le\sigma\|x^k-y\|\) therefore accept these trajectories once \(s\) is sufficiently small. Their residuals obey any prescribed positive cap when \(s\) is sufficiently small. Yet their distance is constantly \(bs>0\), and their physical tangent coordinate diverges. This counterexample already has exact complete input coverage, a closed continuous complete graph, true EB, and local whole-graph reflected Hölder control. The failure is not an empty-fiber or selected-residual artifact.

For the gauge rule of IRF2, these same trajectories are accepted whenever
\[
 \eta\ge\eta_*:=\frac{1-b}{b},
\]
including equality, since \(\psi(\|w\|)=b\|w\|^p\ge bs\). Conversely, for each \(\eta<\eta_*\), choose \(\rho\) so small that \(b(1+\rho^{1-\gamma})^p(1+\eta)<1\), then choose positive \(R,\bar u\) satisfying IRF5. IRF-T gives convergence of all accepted trajectories. Thus \(\eta_*\) is the exact asymptotic threshold for this normalized family: strict values below it can be certified on a sufficiently small common window; equality or larger values permit arbitrarily small nonconvergent accepted trajectories. This statement does not assert sharp finite-radius constants for IRF-T.

### IRF-FAR · 去掉残差上限会接受远端非零输出

Keep the same complete operator, start at the zero \(x=(0,0)\), and for \(s>0\) choose
\[
 y=(s^\gamma,bs),\quad w=(-s^\gamma,(1-b)s),\quad e=(0,-s).
\]
The untruncated gauge criterion asks
\[
 s\le\eta b\left(s^{2\gamma}+(1-b)^2s^2\right)^{p/2}.
\]
For every \(\eta>0\), this holds for all sufficiently large \(s\), because \(p>1\). Hence a local scalar compatibility theorem without a residual cap or an equivalent computable trust restriction cannot force even zero-input absorption. The cap in IRF2, together with the joint window in IRF5, removes these remote graph points before the local geometry is used.

## 5. 可实施性的准确含义

IRF2 uses an actual graph witness, a vector norm, the known EB gauge, and a prescribed residual cap. It never requires evaluating \(d(x,S)\), \(d(y,S)\), a projection onto \(S\), or the exact proximal solution during an iteration. Such quantities occur only in structural hypotheses and in the convergence analysis. As with ordinary EB-based local convergence, the theorem does not itself estimate unknown problem constants or locate the basin.

Exact seed coverage proves that the accepted set is nonempty. It does not by itself prove a particular inner solver terminates. There is, however, a precise finite-acceptance interface. Suppose \(\eta>0\), and an inner solver generates true graph pairs
\((y_j,w_j)\to(y_*,w_*)\) with \(x=y_*+\lambda w_*\),
\(\lambda\|w_*\|<\bar u\), and
\[
 \liminf_j\psi(\|w_j\|)>0.
\]
Then defects tend to zero, so IRF2 holds after finitely many inner iterations. The liminf condition follows if \(\psi\) is continuous and positive at \(\|w_*\|>0\), in particular for the power gauges. For \(x\notin S\), an exact ordinary seed necessarily has \(w_*\ne0\). Shrinking \(R\) so \(B(R)<\bar u\) makes every exact seed strictly inside the cap.

At a zero, the theorem forces exact stationarity, so an implementation needs its usual zero certificate or must return the known exact zero graph pair. There is no finite-precision zero-detection claim. An approximate graph-membership oracle is also outside the current theorem: \(w\in F(y)\) is an exact requirement, not an enlargement tolerance.

## 6. 与已有结果的关系及尚待裁决的研究价值

C213 assumes a perturbation of an exact output, \(z_{k+1}=Tz_k+a_k\), and estimates a convolution from an external bound on \(a_k\). The present acceptance test uses the computed equation defect at a real graph point. No exact proximal output appears in the algorithmic test or the proof. In a maximal-monotone setting, inverse stability can convert graph-equation residual into exact-output error; that classical conversion must be acknowledged rather than counted as new.

The direct scalar certificate does not recover every classical monotone parameter range. For example, with \(v=I\), \(\omega(t)=t\), and linear EB \(\psi(r)=Kr\), it uses \(\kappa_0=K/\lambda\). The gauge rule is then \(E\le\eta K\|w\|\), equivalently \(E\le\sigma\lambda\|w\|\) with \(\sigma=\eta K/\lambda\), and this proof requires \(K/\lambda+\sigma<1\). Hence this particular direct proof only yields a conservative \(\lambda>K\) subset. Classical monotone energy arguments allow broader parameter ranges. No full recovery of their rates or allowable errors is claimed.

For ordinary PPA, the proof is an input-defect absorption argument. Its strongest mathematical package is the conjunction of a nonlinear residual-gauge forcing rule, a local cap that excludes remote accepted roots, true residual EB, exact-seed nonemptiness, all accepted graph outputs, and physical finite length. For a noninjective or nonsurjective kernel, the physical version additionally avoids inventing a lift of the perturbed kernel input and keeps invisible fiber motion under an explicit physical transfer hypothesis.

The counterexample shows why a fixed relative equation residual can fail in the critical Hölder regime even at arbitrarily small residual levels; it also identifies an asymptotically sharp normalized error threshold for a complete operator family with a nonisolated zero set. The exponent rule alone resembles classical forcing terms in inexact Newton methods. Neither nonmonotonicity nor such a resemblance settles novelty. An external claim of priority requires comparison with the exact hypotheses and output models of inexact PPA, HPE, Hölder error-bound and inexact Newton literature; that task is separate from the proof above.

### Scoped handoff record

- **Meaning/evidence**：IRF12–16 explicitly check shifted-input radius, residual window, absorption, and the direction \(r_F\le\|w\|\). Exact seed coverage is proved before invoking an accepted trajectory. IRF7 and the kernel counterpart truncate their evaluation domains.
- **Reader progression**：Sections 1–2 identify the computable rule and its constants before the kernel migration; Section 4 attacks both the relative-rule substitution and removal of the cap; Section 5 separates nonempty accepted sets from inner solver termination.
- **Scope limits**：Only this candidate file is changed. No independent reviewer report, external novelty certification, formatted manuscript, figure, venue rule, or ledger registration is claimed here.
