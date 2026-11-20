# 非线性反射模、函数级补偿与 A/B 的线性边界

本页固定有限维 Euclidean 空间 \(X=\mathbb R^n\)、步长 \(\lambda>0\)、原关系 \(F:X\rightrightarrows X\)、非空闭集 \(S\subseteq\operatorname{zer}F\) 和开集 \(U\)。写
\[
 d(z)=\operatorname{dist}(z,S),\qquad
 r_F(y)=\inf_{v\in F(y)}\|v\|,
\]
其中空纤维的下确界为 \(+\infty\)。允许关系为
\[
 \varnothing\ne\mathcal J(x)\subseteq J_{\lambda F}(x),
 \qquad x^+\in\mathcal J(x).
\]
本页的正则性始终使用完整纤维的 \(r_F\)。所选近端值
\(v=(x-x^+)/\lambda\) 只给出 \(r_F(x^+)\le\|v\|\)，不能替代完整下确界。

<a id="nmc-definitions"></a>
## 1. 四个容易混淆的对象

**固定目标的广义度量次正则性。** 对非减函数
\(\psi:[0,\bar t]\to[0,\infty)\)、\(\psi(0)=0\)，定义
\[
 d(y)\le \psi(r_F(y))
 \tag{NMC-SR}
\]
于指定输出窗内。若 \(\psi(s)=Ks\)，这是固定目标的线性 metric subregularity。若 \(\psi(s)=Cs^p\)，则 \(p<1\) 是较弱的 Hölder 型误差界，\(p>1\) 是更强的局部界。

**两变量 metric regularity。** 它量化目标值扰动，典型形式为
\[
 \operatorname{dist}(y,F^{-1}(u))
 \le \psi\bigl(\operatorname{dist}(u,F(y))\bigr)
 \tag{NMC-MR}
\]
对 \(y,u\) 的共同邻域和全部目标 \(u\) 成立，并隐含相应逆纤维覆盖。令 \(u=0\) 且 \(S=F^{-1}(0)\) 才得到 (NMC-SR)。反向一般不成立。例 \(F(y)=y^2\) 在 \(S=\{0\}\) 上满足 \(d(y)=\sqrt{r_F(y)}\)，但任意包含负目标值的邻域都有 \(F^{-1}(u)=\varnothing\)，所以通常的两变量 metric regularity 失败。

**选定图值的误差界。** 对一个允许政策及其所选边，只要求
\[
 d(x^+)\le\psi(\|v\|),
 \qquad v=(x-x^+)/\lambda.
 \tag{NMC-SV}
\]
因为 \(r_F(x^+)\le\|v\|\)，(NMC-SR) 蕴含 (NMC-SV)，反向不成立。取
\[
 F(y)=\{y,y^3\},\quad S=\{0\},\quad \lambda=1,
\]
并只选 \(v=y\) 的近端分支 \(x=2y\)。在 \(|y|\le1\) 上 (NMC-SV) 以 \(\psi(s)=s\) 成立，但
\[
 r_F(y)=|y|^3,\qquad d(y)=|y|,
\]
故完整图不满足任何局部线性误差界。这里的另一个图值 \(y^3\) 不能被所选政策删除。

**完整残差下界。** 对非减函数 \(\chi\) 写
\[
 r_F(y)\ge\chi(d(y)).
 \tag{NMC-LB}
\]
它是完整纤维的陈述，即使最小范数值不达到也按下确界理解。若 \(\chi\) 连续严格递增，则 (NMC-LB) 与 (NMC-SR) 等价，\(\psi=\chi^{-1}\)。一般单调情形使用左右广义逆，只在相应输出窗内声明等价，不能把一个选定值的下界写成 (NMC-LB)。

<a id="nmc-function-theorem"></a>
## 2. 一般模补偿定理

令 \(U_R=\{x\in U:d(x)\le R\}\)。假设在同一 \(F,S,U_R,\lambda,\mathcal J\) 上：

1. **最近输入锚的非线性 RL。** 有限非减 \(\omega:[0,R]\to[0,\infty)\)，\(\omega(0)=0\)，并且每个 \(x\in U_R\) 和每个 \(y\in\mathcal J(x)\) 存在 \(p\in P_S(x)\) 使
   \[
   \|2y-x-p\|\le\omega(d(x)).
   \tag{NMC-RL}
   \]
2. **完整残差的 GMSR。** 有限非减 \(\psi:[0,\bar t]\to[0,\infty)\)，\(\psi(0)=0\)，且对输出 \(y\in\mathcal J(U_R)\) 的完整残差满足 (NMC-SR)，并且
   \[
   B(R)/\lambda\le\bar t,\qquad B(t):=\frac{t+\omega(t)}2.
   \tag{NMC-cap}
   \]
3. **函数级有效收缩与尾势。** 定义
   \[
   \Phi(t):=\psi\!\left(\frac{B(t)}\lambda\right),\qquad 0\le t\le R.
   \tag{NMC-profile}
   \]
   假设 \(\Phi:[0,R]\to[0,R]\) 非减，\(\Phi(0)=0\)，其迭代满足
   \[
   \Phi^{\circ k}(t)\to0,\qquad
   \Theta_{\omega,\psi}(t):=
   \sum_{j=0}^\infty B\!\left(\Phi^{\circ j}(t)\right)<\infty
   \tag{NMC-tail}
   \]
   对每个 \(t\in[0,R]\)，且 \(\Theta_{\omega,\psi}(t)\to0\) 当 \(t\downarrow0\)。

若 \(x^0\in U_R\) 满足
\[
 \Theta_{\omega,\psi}(d(x^0))
 <\operatorname{dist}(x^0,X\setminus U),
 \tag{NMC-budget}
\]
则每一条选择轨道均可无限续接，并且
\[
 d(x^k)\le \Phi^{\circ k}(d(x^0)),
 \tag{NMC-distance}
\]
\[
 \|x^{k+1}-x^k\|\le B\!\left(\Phi^{\circ k}(d(x^0))\right),\qquad
 \sum_{k=0}^\infty\|x^{k+1}-x^k\|
 \le\Theta_{\omega,\psi}(d(x^0)).
 \tag{NMC-length}
\]
轨道收敛到某个 \(x^\infty\in S\cap U\)，且尾界为
\[
 \|x^\infty-x^k\|
 \le \Theta_{\omega,\psi}(\Phi^{\circ k}(d(x^0))).
 \tag{NMC-tail-bound}
\]

**证明。** 置 \(d_k=d(x^k)\)、\(s_k=\|x^{k+1}-x^k\|\)。由 (NMC-RL)、\(p\in P_S(x^k)\) 和
\(2(x^k-x^{k+1})=(x^k-p)-(2x^{k+1}-x^k-p)\)，得
\[
 s_k\le B(d_k).
 \tag{NMC-step}
\]
近端包含给出 \(r_F(x^{k+1})\le s_k/\lambda\le B(R)/\lambda\)，所以完整 GMSR 和单调性给出
\[
 d_{k+1}\le\psi(s_k/\lambda)\le\psi(B(d_k)/\lambda)=\Phi(d_k).
 \tag{NMC-recursion}
\]
于是距离估计和步长估计按归纳成立。前 \(N\) 步的位移和不超过 \(\Theta_{\omega,\psi}(d_0)\)，预算条件保证每个有限前缀留在 \(U\)，而距离递推保证下一输入仍在 \(U_R\)，故 coverage 可重复使用。尾势可和使轨道 Cauchy，有限维完备性给出极限。\(d_k\to0\) 与 \(S\) 闭性给出极限属于 \(S\)，严格预算又给出极限在 \(U\)。从第 \(k\) 步重新求和得到 (NMC-tail-bound)。\(\square\)

这个定理只要求同一组合函数 \(\Phi=\psi\circ(B/\lambda)\) 的迭代和尾势。它不要求存在固定 \(\kappa<1\)，也不把 \(\Phi^{\circ k}(t)\to0\) 单独误作有限长度条件。

<a id="nmc-tau"></a>
## 3. 点态余量、可检验幂型门和标量锐边界

对 \(t>0\) 定义有效比率与点态补偿余量
\[
 \kappa_{\rm eff}(t):=\frac{\Phi(t)}t,\qquad
 \tau_{\rm eff}(t):=1-\kappa_{\rm eff}(t).
 \tag{NMC-ratio}
\]
固定线性门是 \(\sup_{0<t\le R}\kappa_{\rm eff}(t)\le\kappa<1\)。函数级门则允许 \(\tau_{\rm eff}(t)\downarrow0\)，只要迭代和尾势仍可和。

一个无需求逆的充分条件是：存在 \(c>0,q>0,C>0,\alpha>q\) 和 \(R_0>0\)，使
\[
 \tau_{\rm eff}(t)\ge c t^q,\qquad
 B(t)\le C t^\alpha,\qquad 0<t\le R_0,
 \tag{NMC-power}
\]
且 \(cR_0^q\le1/2\)。于是
\[
 \Phi(t)\le t-c t^{1+q},\qquad
 \Phi^{\circ j}(t)\le\left(t^{-q}+cqj\right)^{-1/q},
 \tag{NMC-rate}
\]
并且 \(\Theta_{\omega,\psi}(t)<\infty\)。因为
\(B(\Phi^{\circ j}(t))\le C(t^{-q}+cqj)^{-\alpha/q}\)，尾和在且仅在 \(\alpha>q\) 的该幂型充分条件下收敛。这里 \(B(t)\ge t/2\)，所以可行的 \(\alpha\) 不超过 1。证明不需要 \(\Phi(t)/t\) 在零点有统一小于 1 的上界。

**标量边界。** 对等式递推
\[
 t_{j+1}=t_j-c t_j^{1+q},\qquad B(t)=t^\alpha,
 \tag{NMC-sharp-rec}
\]
在足够小的窗内，有 \(t_j\asymp (j+1)^{-1/q}\)。因此 \(\sum_jB(t_j)\) 在 \(\alpha\le q\) 时发散，在 \(\alpha>q\) 时收敛。这个锐边界只针对标量补偿递推，不能把等式序列自动宣称为某个完整原图的实现。

<a id="nmc-a-profile"></a>
## 4. A 的函数级版本、残差下界与线性强制边界

把固定 A 换成函数级距离压缩
\[
 d(y)\le\Phi(d(x))
 \tag{A_\Phi}
\]
对全部受检原弦 \(x=y+\lambda v\) 成立。对 \(t>0\) 定义左阈值
\[
 u_\Phi(t):=\inf\{u\ge t:\Phi(u)\ge t\},\qquad
 \inf\varnothing:=+\infty,
\]
以及
\[
 \chi_\Phi(t):=\frac{u_\Phi(t)-t}{\lambda}.
 \tag{NMC-inverse}
\]
若每个 \(y\) 附近的所有完整图值在 \(x=y+\lambda v\) 上都落入 A_\Phi 的输入窗，则
\[
 r_F(y)\ge\chi_\Phi(d(y)).
 \tag{NMC-induced-LB}
\]
若仅能保证 \(\lambda\|v\|<\rho(y)\) 的短图值留在输入窗，则更精确地有
\[
 \lambda r_F(y)\ge
 \min\{u_\Phi(d(y))-d(y),\rho(y)\}.
 \tag{NMC-local-LB}
\]

**证明。** 令 \(t=d(y)\)、\(s=\lambda\|v\|\)。距离函数的 1-Lipschitz 性给
\[
 d(x)\le t+s.
\]
A_\Phi 和 \(\Phi\) 非减于是
\[
 t\le\Phi(d(x))\le\Phi(t+s).
\]
按 \(u_\Phi(t)\) 的定义，\(t+s\ge u_\Phi(t)\)，所以
\(s\ge u_\Phi(t)-t\)。对全部短图值取下确界即得。若完整残差的下确界不达到，使用任意逼近 \(r_F(y)\) 的图值序列，结论仍成立。\(\square\)

若 \(\Phi(t)=\kappa t\)，则
\[
 u_\Phi(t)=t/\kappa,\qquad
 r_F(y)\ge\frac{1-\kappa}{\kappa\lambda}d(y),\qquad
 d(y)\le\frac{\kappa\lambda}{1-\kappa}r_F(y).
 \tag{NMC-linear-forcing}
\]
因此，只要 A 使用固定 \(\kappa<1\) 且完整图值可反推为近端输入，线性真残差次正则性不是可选的额外表达，而是 A 的必要后果。B 单独没有这一后果。

若 \(\Phi(t)=t-c t^{1+q}\) 且取足够小的 \(t\)，则
\[
 u_\Phi(t)-t\asymp c t^{1+q},\qquad
 r_F(y)\gtrsim \frac c\lambda d(y)^{1+q}.
 \tag{NMC-nonlinear-forcing}
\]
对应的逆向 GMSR 只给
\(d(y)\lesssim (\lambda r_F(y)/c)^{1/(1+q)}\)。这正是保留函数级 A_\Phi 后出现的非线性次正则，而不是固定 A 的反例。

<a id="nmc-compatibility-boundary"></a>
## 5. RL--GMSR 兼容的硬边界和完整图量词

在第 2 节的 RL--GMSR 合取下，\(\Phi(t)=\psi(B(t)/\lambda)\)。若还要求固定 A 的 \(d(y)\le\kappa d(x)\)，必须有
\[
 \psi\!\left(\frac{B(t)}\lambda\right)\le\kappa t
 \qquad(0<t\le R).
 \tag{NMC-fixed-gate}
\]
由 \(B(t)\ge t/2\)，沿 RL 的实际尺度立即得到
\[
 \frac{\psi(B(t)/\lambda)}{B(t)/\lambda}
 \le 2\kappa\lambda .
 \tag{NMC-linear-envelope}
\]
若 \(B\) 连续且 \(B(0)=0\)，其像包含一个零邻域，所以固定 A 在完整图窗内强迫最小 GMSR 可以取线性模。特别是任何满足
\(\psi(s)/s\to\infty\) 的候选 gauge（例如 \(s^p\), \(0<p<1\)）不能在同一连续 RL 尺度和固定 \(\kappa<1\) 下承担全部非解尺度。\(\psi(s)/s\to0\) 的更强 gauge 可以共存，但它隐藏着由 A 已强制的线性界，不能据此声称 A 脱离线性次正则。

若只验证一个选定值的 (NMC-SV)，上述结论不成立。若输入覆盖只在局部窗口，必须保留 \(\rho(y)\) 的短值留域余量，不能把局部结论升级为全域 GMSR。若要讨论 (NMC-MR)，还必须把 \(0\) 换成所有附近目标 \(u\)，并对 \(F^{-1}(u)\) 给出共同覆盖，A 的零目标证明本身不提供这些逆纤维。

**结论。** 函数级 RL--GMSR 补偿由
\[
 \boxed{\Phi=\psi\circ(B/\lambda),\quad
        \tau_{\rm eff}(t)=1-\Phi(t)/t,\quad
        \Theta(t)=\sum_{j\ge0}B(\Phi^{\circ j}(t))}
\]
完全检验。它允许 \(\tau_{\rm eff}(t)\to0\) 并保留非线性有限长度。若坚持当前固定 A/B 结构及完整图量词，A 的常数收缩会通过 (NMC-linear-forcing) 强制线性真残差次正则，非线性 gauge 只能作为更强界、选定分支界或函数级 A_\Phi 的输入。\(\square\)
