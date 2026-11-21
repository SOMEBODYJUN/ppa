# PPA 非线性收缩、KL 有限长度与耦合条件障碍

本页固定三个方向的规范对象。它只使用有限维 Euclidean 空间、局部允许转移和完整真残差；不把历史稿中的图块 resolvent 自动升级为完整 \(J_{\lambda F}\)。

<a id="ng-object"></a>
## 1. 共同对象与现有一步估计

令 \(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，\(\lambda>0\)，\(S\subset F^{-1}(0)\) 非空闭，\(U\subset X\) 开。写

\[
d(x)=\operatorname{dist}(x,S),\qquad r_F(y)=\operatorname{dist}(0,F(y)).
\]

在 \(U_R=\{x\in U:d(x)\le R\}\) 上给定一个允许转移关系
\[
\mathcal J(x)\subset J_{\lambda F}(x),
\qquad x^+\in\mathcal J(x).
\]
现有 RLEB 一步证明（C02-v3/C09）在同一个最近零锚 \(p\in P_S(x)\) 上给出
\[
\begin{aligned}
 d(x^+,S)^2+\|x^+-x\|^2
 &\le \frac{d(x)^2+\omega(d(x))^2}{2},\\
 \|x^+-x\|&\le B(d(x)),
 \qquad B(t):=\frac{t+\omega(t)}2.
\end{aligned}
\tag{NG1}
\]
若真实全纤维残差满足
\[
d(y,S)\le\psi(r_F(y)),
\tag{NG2}
\]
且评价窗包含 \(B(R)/\lambda\)，则
\[
d(x^+,S)\le \psi\!\left(\frac{B(d(x))}{\lambda}\right).
\tag{NG3}
\]

### 1.1 C09 与本页新方向的分界

C09 另外假设一个常数 \(\kappa<1\)，使右端在整个窗口满足
\[
\psi(B(t)/\lambda)\le \kappa t.
\]
因此 C09 的长度预算是 \(\sum_jB(\kappa^jt)\)。本页不再要求一个固定线性因子；只要求存在一个非减函数 \(\Phi\) 使
\[
d(x^+,S)\le\Phi(d(x)),
\qquad 0\le t\le R.
\tag{NG4}
\]
在 RLEB 直接证书中可以取
\[
\Phi(t):=\psi(B(t)/\lambda),
\tag{NG5}
\]
但定理本身只使用 (NG4)，所以也适用于由其它几何估计直接得到的 \(\Phi\)。

<a id="c309-theorem"></a>
## 2. C309：一般函数迭代的 PPA 有限长度定理

**Exact Statement。** 设 \(B,\Phi:[0,R]\to[0,R]\) 非减、\(B(0)=\Phi(0)=0\)，且 \(B\) 在零连续。假设：

1. 对每个 \(x\in U_R\)，\(\mathcal J(x)\ne\varnothing\)；
2. 每个允许转移 \(x^+\in\mathcal J(x)\) 满足
   \[
   d(x^+,S)\le\Phi(d(x)),
   \qquad \|x^+-x\|\le B(d(x));
   \tag{NG6}
   \]
3. 对每个 \(t\in(0,R]\)，
   \[
   \Phi^{\circ k}(t)\longrightarrow0,
   \qquad
   \Theta_\Phi(t):=\sum_{j=0}^{\infty}B(\Phi^{\circ j}(t))<\infty;
   \tag{NG7}
   \]
4. \(\Theta_\Phi(t)\to0\) 当 \(t\downarrow0\)。

若 \(x^0\in U_R\) 且
\[
\Theta_\Phi(d(x^0))<\operatorname{dist}(x^0,X\setminus U),
\tag{NG8}
\]
则每条允许轨道 \(x^{k+1}\in\mathcal J(x^k)\) 都可无限构造，满足
\[
d(x^k,S)\le \Phi^{\circ k}(d(x^0,S)),
\tag{NG9}
\]
\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|
\le \Theta_\Phi(d(x^0,S))<\infty,
\tag{NG10}
\]
并收敛到某个 \(x^\infty\in S\cap U\)。尾界为
\[
\|x^\infty-x^k\|
\le \Theta_\Phi(\Phi^{\circ k}(d(x^0,S))).
\tag{NG11}
\]

**Proof。** 记 \(t_k=d(x^k,S)\)。由 (NG6) 归纳得 \(t_k\le\Phi^{\circ k}(t_0)\)。于是
\[
\|x^{k+1}-x^k\|\le B(t_k)
\le B(\Phi^{\circ k}(t_0)).
\]
对前 \(N\) 步求和，(NG8) 保证所有有限前缀留在 \(U\)，而 \(t_k\le R\) 保证下一步 coverage 继续适用。令 \(N\to\infty\) 得 (NG10)，所以轨道是 Cauchy；有限维完备性给出极限。由 (NG9) 和 \(\Phi^{\circ k}(t_0)\to0\)，闭性给 \(x^\infty\in S\)。从第 \(k\) 步重新求尾和即得 (NG11)。最后，\(\Theta_\Phi(t)\to0\) 可由有限前缀逐项趋零及
\[
B(\Phi^{\circ j}(t))\le B(\Phi^{\circ j}(R))
\]
的可和尾控制得到。证毕。

**状态。** derived-checked，范围严格是 (NG6) 的允许转移定理。它不声称 (NG6) 自动来自任意完整图，也不把 \(\Phi^{\circ k}(t)\to0\) 单独当作有限长度条件。

<a id="c309-sharpness"></a>
## 3. 非线性迭代的可检验充分条件与锐边界

### 3.1 低于固定线性比率的渐近收缩

若存在 \(q>0,c>0,\alpha>0\) 和 \(R_0>0\)，使
\[
\Phi(t)\le t-c t^{1+q},
\qquad B(t)\le C t^\alpha,
\qquad 0<t\le R_0,
\tag{NG12}
\]
且 \(ct^q\le1/2\) 在该区间成立，则
\[
\Phi^{\circ j}(t)
\le (t^{-q}+cqj)^{-1/q}
\tag{NG13}
\]
（把 \(cq\) 换成更小的正常数也足够）。因此当
\[
\alpha>q
\tag{NG14}
\]
时 \(\Theta_\Phi(t)<\infty\)。这里 \(\Phi(t)/t\to1\)，所以这类收缩一般不满足 C09 的固定 \(\kappa<1\) 门，也不满足 MOR 论文中用 \(\limsup\tau(t)/t<1\) 的简化门。

证明只用
\[
(1-cu)^{-q}\ge1+qcu,
\qquad u=t_j^q,
\]
对 \(t_{j+1}\le t_j-ct_j^{1+q}\) 反复取倒数。于是
\[
t_{j+1}^{-q}\ge t_j^{-q}+cq.
\]
对 \(B(t_j)\le Ct_j^\alpha\) 求和，右端被 \(\sum_j(j+1)^{-\alpha/q}\) 控制。

### 3.2 尖锐性

取等式递推
\[
t_{j+1}=t_j-c t_j^{1+q}
\tag{NG15}
\]
在足够小的窗口内。对 \(ct_j^q\le1/2\)，还有
\[
(1-ct_j^q)^{-q}\le1+C_qct_j^q,
\]
故 \(t_j\ge (t_0^{-q}+C_qcj)^{-1/q}\)。所以 \(B(t)=t^\alpha\) 时，
\[
\sum_jB(t_j)=\infty\quad\text{若 }\alpha\le q.
\tag{NG16}
\]
这说明 (NG14) 是该标量机制的真实阈值，而非证明中的粗糙几何级数。

### 3.3 与现有完整对数例的关系

规范例 C10（见 [general_modulus_dynamics](general_modulus_dynamics.md#gm-log-object)）给出更强的动力学见证：
\[
d_k=4^{-k}d_0\to0
\]
但切向步长 \(\ell_a(4^{-k}d_0)\) 的级数在 \(a\le1\) 时发散，轨道切向坐标趋于 \(+\infty\)。因此即使距离以固定几何因子收缩，点列也可能不收敛；缺失的是 (NG7) 的步长可和门，而不是距离趋零。

<a id="c311-kl"></a>
## 4. C311：KL 机制可在次梯度 PPA 中替代传统度量次正则

**Exact Statement。** 按 LMZ v1 的有限值函数约定，或在轨道有限值且 limiting-subgradient/Fermat 桥已另证的 proper-l.s.c. 扩展，令 \(f:\mathbb R^n\to(-\infty,+\infty]\) 有下界。设每一步精确近端点存在：
\[
x^{k+1}\in\operatorname*{argmin}_y
\left\{f(y)+\frac1{2\lambda}\|y-x^k\|^2\right\},
\qquad \lambda>0.
\tag{KL1}
\]
假设某个聚点 \(\bar x\) 满足：

- 相关子水平集有界；
- 对每个趋于 \(\bar x\) 的迭代子序列，\(\limsup f(x^{k_j})\le f(\bar x)\)；
- \(f\) 在 \(\bar x\) 满足 KL 性质，使用 \(\vartheta\)；
- 近端最优性给出限制子梯度
  \[
  w^{k+1}:=\frac{x^k-x^{k+1}}\lambda\in\partial f(x^{k+1}).
  \tag{KL2}
  \]

则
\[
\sum_{k=0}^{\infty}\|x^{k+1}-x^k\|<\infty,
\qquad x^k\to\bar x,
\tag{KL3}
\]
而整个论证不使用传统 metric subregularity。这里的结论是对次梯度 PPA；对一般 \(F\) 必须另行构造 Lyapunov 函数和相对误差桥。

**Proof reconstruction from LMZ v1 Theorem 5.1.** 令
\[
e_k=\|x^{k+1}-x^k\|,
\quad a=\frac1{2\lambda},
\quad \phi(t)=t^2,
\quad \beta(t)=t,
\quad b=\frac1\lambda.
\]
近端最小性给
\[
f(x^{k+1})+\frac1{2\lambda}e_k^2\le f(x^k),
\tag{KL4}
\]
即 LMZ 的充分下降 (H11)；(KL2) 是相对误差 (H2)，\(e_k\) 就是 surrogate。若 \(e_{k-1}>0\)，KL 不等式在 \(x^k\) 给
\[
\vartheta'(f(x^k)-f(\bar x))\,\|w^k\|\ge1,
\qquad \|w^k\|=e_{k-1}/\lambda.
\]
凹性和 (KL4) 因而给
\[
\begin{aligned}
\Lambda_{k,k+1}
&:=\vartheta(f(x^k)-f(\bar x))-\vartheta(f(x^{k+1})-f(\bar x))\\
&\ge \vartheta'(f(x^k)-f(\bar x))\,[f(x^k)-f(x^{k+1})]\\
&\ge \frac{e_k^2}{2e_{k-1}}.
\end{aligned}
\tag{KL5}
\]
于是
\[
e_k\le\sqrt{2e_{k-1}\Lambda_{k,k+1}}
\le \frac{e_{k-1}+\Lambda_{k,k+1}}{\sqrt2}.
\tag{KL6}
\]
系数 \(1/\sqrt2<1\)，对 (KL6) 求和并望远镜消去 \(\Lambda\)，得到 \(\sum e_k<\infty\)。这正是 LMZ v1 (5.6)–(5.7) 的 PPA 专化；其一般表述用
\[
\frac{\phi^{-1}(\beta(s)t)}{\mu_1s+\mu_2t}
\]
控制一个下降差和前一步 surrogate 的混合项。标准 PPA 的 (KL6) 直接由 AM--GM 得到；若按 LMZ 的 K1 代入 \(t=(b/a)\Lambda=2\Lambda\)，取 \(\mu_1=\mu_2=1/2\) 得另一递推 \(e_k\le e_{k-1}/2+\Lambda\)，两者不混写。

**Scope。** KL 证明给出有限长度和点收敛，但不自动给 \(d(x^k,S)\) 的先验线性或非线性速率；也不自动覆盖非次梯度、非 Lyapunov 的原始多值 \(F\)。因此它可以去掉的是“为了有限长度而使用传统 metric subregularity”的一个证明接口，不能写成“去掉一切正则性”。KL 本身是新的正则结构。

<a id="exact-prox-kl-value-bridge"></a>
### C464：精确全局近端的 KL 转接，不另假设聚点值连续性

本段是独立的充分版本，不更改 C311 原卡的前件。
已经三席实际终稿复核，状态 derived-checked；这是经典 KL 机制的明确转接，不作新颖性声明。
[Attouch–Bolte–Svaiter 作者稿](https://bolte.perso.math.cnrs.fr/MPA.pdf)
（2010-12-15，2011-07-21 修订）§2.2 Definition 2.4（PDF第7页）、
§2.3 H1–H3（PDF第8页）、Theorem 2.9（PDF第12页，均从1计）是比较依据。
该定理使用充分下降、输出 limiting 子梯度的相对误差及一个函数值相容聚点，
并在该点假设 KL；它不要求先有全序列有界性。
以下先证明这些桥，再直接重构邻域锁定和长度求和。

**EK1 · Exact statement。** 令 \(f:\mathbb R^n\to(-\infty,+\infty]\)
proper、lsc、全局下有界，\(\lambda>0\) 固定，\(x^0\in\operatorname{dom}f\)。
每一步允许全部全局近端极小解
\[
x^{k+1}\in T_\lambda(x^k):=
\operatorname*{argmin}_y\{f(y)+\|y-x^k\|^2/(2\lambda)\}.
\tag{EK1}
\]
对每条这样生成的轨道，若它有一个聚点 z 且 f 在 z 具有上述 ABS Definition2.4 的凹型 limiting
子梯度 KL 性质，则
\[
\sum_{k\ge0}\|x^{k+1}-x^k\|<\infty,\qquad
x^k\to z,\qquad z\in T_\lambda(z),\quad0\in\widehat\partial f(z)\subseteq\partial f(z).
\tag{EK2}
\]
有界轨道是得到聚点的充分条件，不是额外必需的前件。
全局极小集非空、f 在域上连续、传统误差界及 DD2 的距离积分都未假定；
KL 和全局极小化结构则确实增加了信息。

**EK2 · 完整极小解、H1 与 H2。** 每个近端目标 proper、lsc、强制，
所以 \(T_\lambda(x)\) 非空紧；它在非凸时不必单值。
任意选择都留在 \(\operatorname{dom}f\)。记 \(s_k=\|x^{k+1}-x^k\|\)，
与 \(x^k\) 比较得
\[
f(x^{k+1})+\frac{s_k^2}{2\lambda}\le f(x^k).
\tag{EK3}
\]
故 \(f(x^k)\downarrow f_\infty\in\mathbb R\)、\(\sum s_k^2<\infty\)、\(s_k\to0\)。
对任意 w 的全局比较还给
\[
f(w)\ge f(x^{k+1})+
 \left\langle\frac{x^k-x^{k+1}}{\lambda},w-x^{k+1}\right\rangle
 -\frac{\|w-x^{k+1}\|^2}{2\lambda}.
\tag{EK4}
\]
因此选中方向 \(v_{k+1}=(x^k-x^{k+1})/\lambda\)
属于 Fréchet 子梯度，因而属于 limiting 子梯度。
这精确给 H1 的 \(1/(2\lambda)\) 和 H2 的 \(1/\lambda\)，
并对完整输出纤维保 \(r_{\partial f}(x^{k+1})\le s_k/\lambda\)。
没有将完整真残差反过来认作选中方向的范数。

**EK3 · H3 自动桥。** 设 \(x^{k_j}\to z\)，取下标正且趋无穷。
lsc 给 \(f(z)\le f_\infty<\infty\)。
因为 \(s_{k_j-1}\to0\)，前驱 \(x^{k_j-1}\to z\)。
在该前驱的全局子问题中比较 z，
\[
f(x^{k_j})+\frac{s_{k_j-1}^2}{2\lambda}
 \le f(z)+\frac{\|z-x^{k_j-1}\|^2}{2\lambda},
\]
于是 \(f_\infty\le f(z)\)。故 \(f(x^k)\to f(z)\)，
尤其这个聚点满足 H3；没有偷加 f 的连续性。
该桥使用全局比较，不能只由一般驻点 inclusion 推出。

**EK4 · KL 邻域和有限尾。** 记 \(r_k=f(x^k)-f(z)\ge0\)。
取 KL 邻域中的球 \(B(z,\delta)\)、能级窗 \(0<r<\eta\)，以及连续凹
\(\vartheta:[0,\eta)\to[0,\infty)\)，
\(\vartheta(0)=0\)、正尺度 C¹、\(\vartheta'>0\)，满足
\(\vartheta'(f(x)-f(z))\,d(0,\partial f(x))\ge1\)。
若某个 \(r_k=0\)，下降式 EK3 及下界 \(f(z)=f_\infty\) 迫所有之后的步为零；
否则在邻域内的 \(x^k\)，\(k\ge1\)，KL 及 EK4 给
\(\vartheta'(r_k)\ge\lambda/s_{k-1}\)，其中 \(s_{k-1}>0\)。
用凹性和 EK3，
\[
\Delta_k:=\vartheta(r_k)-\vartheta(r_{k+1})
 \ge\frac{s_k^2}{2s_{k-1}},\qquad
s_k\le\tfrac12s_{k-1}+\Delta_k.
\tag{EK5}
\]
沿上述聚点子列选 N 足够大，使 \(0<r_N<\eta\) 且
\[
\|x^N-z\|+s_{N-1}+2\vartheta(r_N)<\delta .
\tag{EK6}
\]
若从 N 到 M 的点已在球内，对 EK5 求和便有
\[
\sum_{k=N}^{M}s_k
 \le s_{N-1}+2\vartheta(r_N)-s_M-2\vartheta(r_{M+1})
 \le s_{N-1}+2\vartheta(r_N).
\tag{EK7}
\]
这又使 \(x^{M+1}\) 留在同一个球内；函数值下降保能级窗。
从 N 开始归纳，即无循环地锁定全部尾部，并得到可和长度。
有限头部不影响结论，且已有聚点 z 迫唯一点极限就是 z。
之后同一求和还给
\(\sum_{k\ge N}s_k\le s_{N-1}+2\vartheta(r_N)\)。
这是函数值势和前一步信息，不是只看 \(t_k=d(x^k,S)\) 的势。

在原全局近端比较中固定任意 w，再令 k 趋无穷，由函数值与点收敛得
\[
f(z)\le f(w)+\|w-z\|^2/(2\lambda).
\tag{EK8}
\]
所以 \(z\in T_\lambda(z)\)，并由这个二次支持得
\(0\in\widehat\partial f(z)\)。事实上只用 EK3 的聚点子列，
此近端固定点结论就已成立，不依赖 KL。
它不宣称 z 为 f 的全局极小点：例如 \(f(u)=(u^2-1)^2\)、\(\lambda=1/4\)
在 z=0 的近端目标为 \(u^4+1\)，故0是唯一近端固定输出，
却是 f 的严格局部极大点。若 DD2 另指定某个闭
\(S\subseteq\operatorname{zer}\partial f\)，
仍须另证 \(d(x^k,S)\to0\) 或 z 属于 S，不能只凭临界性识别指定目标。

**EK5 · 不是全部驻点 resolvent 的定理。** 即使 \(f(u)=(u^2-1)^2\)
光滑多项式、\(\lambda=1\)，输入 x=1 与输出 y=-1/2 也满足
\(x-y=f'(y)=3/2\)，故是完整 \(J_{\partial f}\) 的真实一条边；
但
\[
f(y)+\tfrac12|x-y|^2=\tfrac{27}{16}>f(x)=0 .
\tag{EK9}
\]
它违反 H1，且不是全局近端极小解，所以不能据此边套用上述证明。
要严格否定全部驻点选择的有限长度，还可在同一个 f、λ1 上取
\[
r=1/\sqrt2,\qquad
r\longmapsto-r\longmapsto r,\qquad
f'(\pm r)=\mp2r .
\tag{EK10}
\]
两条边都满足原完整 inclusion，形成实际二周期；每步长度 \(2r>0\)。
两个聚点的导数均非零，在各自小邻域有 \(|f'|\ge c>0\)，
取线性解奇函数 \(\vartheta(u)=u/c\) 即直接验证那里的 KL 性质。
所以即使轨道有 KL 聚点，完整驻点选择仍可无限长且不收敛，
失败前件正是全局极小化及其下降桥，而非文献定理本身。
对一般 F 需要另有同一函数的下降、相对误差和聚点值桥；
不能把 EK1 的允许关系偷换成完整驻点 resolvent。
多值极小解也不因偶遇一个零步就强制永久驻定；
上面的驻定论证明确使用已到达该轨道的极限能级。

<a id="c310-nogo"></a>
## 5. C310：旧条件不自动生产输出相对步长界

曾经尝试证明的辅助蕴含是
\[
\text{传统次单调性+度量次正则性}
\Longrightarrow\mathcal P
\Longrightarrow (A)+(B).
\tag{T0}
\]
其中
\[
(A)\ d(y,S)\le\kappa d(x,S),\qquad
(B)\ \|x-y\|\le B d(y,S).
\]
这个辅助蕴含在当前对象层面是错误的。它只否定“从旧条件自动推出 (B)”这条路线，不否定目标三真正需要的严格扩张构造。

### 5.1 最大单调且有线性 MSR，但 (B) 失败

固定 \(0<\alpha<1\)，在 \(X=\mathbb R\) 取
\[
F(y)=\operatorname{sgn}(y)|y|^\alpha,
\qquad S=\{0\}.
\tag{NG17}
\]
它是凸函数 \(f(y)=|y|^{1+\alpha}/(1+\alpha)\) 的梯度，故最大单调，尤其满足传统次单调性。且在 \(|y|\le R\le1\) 上
\[
d(y,S)=|y|\le |y|^\alpha=r_F(y),
\]
所以线性 metric subregularity 成立。

精确 PPA 方程为 \(x=y+\lambda\operatorname{sgn}(y)|y|^\alpha\)。对 \(y>0\)，
\[
d(x,S)=y+\lambda y^\alpha,
\quad d(y,S)=y,
\quad \|x-y\|=\lambda y^\alpha.
\tag{NG18}
\]
第一式给
\[
\frac{d(y,S)}{d(x,S)}=\frac1{1+\lambda y^{\alpha-1}}
\longrightarrow0,
\]
所以在足够小的窗口内 (A) 对任意预定的 \(\kappa\in(0,1)\) 成立；但
\[
\frac{\|x-y\|}{d(y,S)}=\lambda y^{\alpha-1}
\longrightarrow+\infty,
\]
故不存在有限 \(B\) 使 (B) 成立。

这不是非单调或多值病理，而是最大单调、完整 resolvent 和线性 MSR 都成立的例子。它证明旧条件不能自动生成输出相对步长界，但不回答“存在满足 (A)+(B) 且脱离旧结构的对象”这一严格扩张问题。

### 5.2 (A) 与 (B) 各自不足

- (NG17) 同时给出“(A) 可成立而 (B) 失败”。
- 取 \(F(y)=\operatorname{sgn}(y)|y|^\beta\) 且 \(\beta>1\)。则
  \(\|x-y\|=\lambda|y|^\beta\le\lambda R^{\beta-1}d(y,S)\)，所以局部 (B) 成立；但 \(d(y,S)/d(x,S)\to1\)，不存在严格的 \(\kappa<1\)，故 (A) 失败，且线性 MSR 也失败。
- 取 \(S=S^1\) 且 \(T\) 为圆周上的非平凡旋转。对所有点 \(d(Tx,S)=0\)，所以 (A) 对 \(d(x,S)=0\) 是真空成立；轨道沿圆周不收敛，而 (B) 立即失败。这说明集合距离收缩不等于点收敛。

### 5.3 (A)+(B) 可以脱离传统 MSR 与单调性

在 \(X=\mathbb R\) 取
\[
F(y)=\{y,y^2\}\quad(y\ge0),\qquad F(y)=\varnothing\quad(y<0),
\tag{NG19}
\]
并令允许关系只选取 \(v=y\) 的分支。于是 \(x=(1+\lambda)y\)，所以
\[
d(y,S)=\frac1{1+\lambda}d(x,S),\qquad
\|x-y\|=\lambda d(y,S).
\tag{NG20}
\]
这给出 (A)+(B)，但真残差为
\[
r_F(y)=\min\{y,y^2\}=y^2\quad(0<y<1),
\]
所以线性 MSR 失败。图也不单调：例如图点 \((0.5,0.5)\) 与 \((0.7,0.49)\) 的差满足
\[
(0.5-0.7)(0.5-0.49)<0.
\]
它说明 (A)+(B) 确实可能来自一个允许分支的独立几何机制，而不是传统假设的同义改写。

<a id="c312-fullgraph"></a>
## 6. C312：完整单值 PPA 中满足 (A)+(B) 但不满足传统次单调性的例子

取 \(X=\mathbb R\)、\(\lambda=1\)，定义
\[
G(y)=\frac32(y+\sin y),\qquad
F(y)=G(y)-y=\frac12y+\frac32\sin y.
\tag{SG1}
\]
有 \(G'(y)=\frac32(1+\cos y)\ge0\)。虽然导数在奇数倍 \(\pi\) 处为零，但 \(G\) 在每个非退化区间上严格递增，且 \(G(y)\to\pm\infty\)，所以 \(G\) 是全局同胚，完整 resolvent 是 \(J_F=G^{-1}\)。

零集为 \(S=\{0\}\)：当 \(|y|\le\pi\) 时 \(\sin y\) 与 \(y\) 同号；当 \(|y|>\pi\) 时 \(\frac12|y|>\frac32\ge\frac32|\sin y|\)，故 \(F(y)=0\) 只发生在 \(0\)。

对任意图点 \(x=G(y)\)，有
\[
\frac{G(y)}y=\frac32\left(1+\frac{\sin y}{y}\right)
\ge m:=\frac32\left(1-\frac1\pi\right)>1.
\]
因此完整 resolvent 的每一步满足
\[
d(J_Fx,S)=|y|\le m^{-1}|x|,
\]
即 (A) 对所有输入和唯一完整输出成立。另一方面
\[
\|x-y\|=|F(y)|\le\frac12|y|+\frac32|\sin y|\le2|y|,
\]
所以 (B) 对所有完整输出成立，可取 \(B=2\)。

但 \(F\) 不满足传统次单调性，甚至不存在有限的 Luke–Tam 型 violation 常数 \(\tau\)。令 \(y_n=(2n+1)\pi\)，\(u_n=y_n-\varepsilon\)、\(v_n=y_n+\varepsilon\)。则
\[
\Delta y=2\varepsilon,\qquad
\Delta F=\varepsilon-3\sin\varepsilon,\qquad
\Delta G=3(\varepsilon-\sin\varepsilon).
\]
当 \(\varepsilon\downarrow0\) 时，\(\Delta y\,\Delta F\sim-4\varepsilon^2\)，而 \((\Delta G)^2\sim\varepsilon^6/4\)。任何不等式
\[
\Delta y\,\Delta F\ge-\tau(\Delta y+\Delta F)^2
\]
都要求 \(\tau\gtrsim16\varepsilon^{-4}\)，矛盾。

因此 C312 给出 full-graph/full-resolvent 的严格扩张：完整 PPA 同时满足 (A)+(B)，但脱离传统次单调性。它仍满足线性 MSR；若要求同时否定完整 MSR，则由 full-graph 的 (A) 自动推出线性 MSR，这是量词边界。

<a id="ptc"></a>
## 7. 修正后的候选结构：锚定扇区—相对平静性

一个有独立几何意义的候选是对**允许转移**加入以下性质 \(\mathcal P_{\rm TC}\)：存在同一锚
\[
p\in P_S(x)\cap P_S(y),
\tag{TC1}
\]
常数 \(0<\mu<1/2\)、\(0\le\nu<1/2\)、\(c<\infty\)，使
\[
\langle y-p,x-y\rangle
\ge \mu d(x,S)^2-\nu\|x-y\|^2,
\tag{TC2}
\]
\[
\left\|\frac{x-y}{\lambda}\right\|
\le c\,d(y,S).
\tag{TC3}
\]
这里 (TC1) 是零集投影的锚持久性，(TC2) 是图增量的正扇区条件，(TC3) 是所选图值相对输出距离的 calmness；三者分别具有投影、角度和图纤维解释，不是把 (A)+(B) 改名。

由 \(p\in P_S(y)\) 有 \(\|y-p\|=d(y,S)\)。恒等式
\[
d(x,S)^2=\|y-p\|^2+\|x-y\|^2+2\langle y-p,x-y\rangle
\]
与 (TC2) 给出
\[
(1-2\mu)d(x,S)^2
\ge d(y,S)^2+(1-2\nu)\|x-y\|^2.
\tag{TC4}
\]
因此
\[
d(y,S)\le\sqrt{1-2\mu}\,d(x,S),
\qquad
\|x-y\|\le \lambda c\,d(y,S).
\tag{TC5}
\]
即 \(\mathcal P_{\rm TC}\Rightarrow(A)+(B)\)，其中 \(\kappa=\sqrt{1-2\mu}<1\)、\(B=\lambda c\)。

**严格范围。** C310 只否定“传统次单调性+MSR 自动推出 \(\mathcal P_{\rm TC}\)”这一辅助路线；C312 已给出 full-graph 非单调的严格扩张例。PTD/TC 仍需研究自然算子类和允许关系量词，不能把选择子关系的例子自动升级为完整 resolvent 结论。

<a id="next-obligations"></a>
## 7. Proof obligations 与下一步

1. 对 C309，寻找原生 PPA/GPPA 模型使 \(\Phi(t)=t-ct^{1+q}+o(t^{1+q})\) 且 \(B(t)\asymp t^\alpha\)，验证 \(\alpha>q\) 与 \(\alpha\le q\) 两侧都能在同一图块和真残差约定下实现。
2. 对 C311，先在 \(F=\partial f\) 且 exact prox 的范围内完成；再判断一个 Lyapunov 结构 \(E\) 能否对固定核 GPPA 提供 (KL4)–(KL6) 的同一替代。没有 \(E\) 时不能把 KL 结论迁移到任意 \(F\)。
3. 对 C312，进一步核对更高维、非孤立零集和 full-graph violation 的严格常数；对 \(\mathcal P_{\rm TC}\)，研究单值局部图和凸/光滑零集的锚持久性。
4. 先行性只登记已逐条读取的 LMZ v1 和正式版元数据。正式版全文当前只能取得 INFORMS 摘要页，不能负责任地声称其与 v1 在定理编号或假设上完全相同。
