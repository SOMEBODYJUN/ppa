# DD2 在临界步长 Chambolle–Pock 与 Douglas–Rachford 中的应用

<a id="dd2-splitting-scope"></a>
## 原算法与恢复量词

设 \(X,Y\) 为有限维实 Hilbert 空间，\(A:X\rightrightarrows X\)、\(B:Y\rightrightarrows Y\)、\(L:X\to Y\) 为非零线性算子。记 \(D=B^{-1}\)，在 \(X\oplus Y\) 上固定

\[
T(u,v)=(Au+L^*v,\ Dv-Lu),\qquad
P=\begin{pmatrix}\gamma^{-1}I&-L^*\\-L&\tau^{-1}I\end{pmatrix},\qquad
\gamma\tau\|L\|^2\le1.
\]

令 \(\mathcal R=\operatorname{ran}P\)，取 \(P=CC^*\)，其中 \(C:\mathcal R\to X\oplus Y\) 单射，\(\operatorname{ran}C=\mathcal R\)。给定 \(z=C^*x\)，在 \(P+T\) 中消去第一行的 \(L^*\bar v\)，第二行保留 \(-2L\bar u\)。因此一次完整 Chambolle–Pock 更新 \(x^+=\bar x=(\bar u,\bar v)\in (P+T)^{-1}Cz\) 精确等价于

\[
\bar u\in J_{\gamma A}\bigl(\gamma(Cz)_1\bigr),\qquad
\bar v\in J_{\tau D}\bigl(\tau[(Cz)_2+2L\bar u]\bigr).
\tag{S1}
\]

于是 \(z^+=C^*\bar x\)、\(q=z-C^*\bar x\) 且 \(Cq\in T_{\mathcal R}(\bar x):=T(\bar x)\cap\mathcal R\)。有限维保证 \(P\) 的值域闭。无限维临界情形需要另查 \(\|L\|^2I-LL^*\) 的闭值域，证明来自 \(P\) 对 \(\operatorname{diag}(\gamma^{-1}I,\gamma(\|L\|^2 I-LL^*))\) 的可逆合同变换。[Alcantara arXiv:2611.20523v1 §5 (41)–(42)](https://arxiv.org/html/2611.20523v1#S5)

若 \(X=Y,\ L=I,\ \tau=1/\gamma\)，令 \(\zeta=u-\gamma v\)，采用尺度 \(Cz=(z/\sqrt{\gamma},-\sqrt{\gamma}z)\)，则 \(\zeta=\sqrt{\gamma}z\)。取 \(w=2\bar u-\zeta-\gamma\bar v\)，(S1) 等价于

\[
\bar u\in J_{\gamma A}(\zeta),\qquad w\in J_{\gamma B}(2\bar u-\zeta),\qquad
\zeta^+=\bar u-\gamma\bar v=\zeta-\bar u+w .
\]

这就是 Douglas–Rachford 的实际状态和两次分量取根。回代恒等式在集合值情形也逐选择成立。本文算法取固定松弛 \(\alpha=1\)，原迭代 \(x^{k+1}=\bar x^k\)。

Alcantara Theorem 5.1 的 \(V=V_1\oplus V_2\)、\(U\succeq-\sigma P\)、\(I_{\mathcal R}+C^*VC-\sigma I_{\mathcal R}\succeq\kappa I_{\mathcal R}\) 和全图 solution-relative semimonotonicity 给出

\[
\|\bar x-x_*\|\le K_{\rm PD}\|z-C^*x_*\|
\quad(x_*\in S^\star\subseteq \operatorname{zer}T).
\tag{S2}
\]

该估计比较 shadow 与零锚。证明使用 \((\bar u,v_*)\)、\((u_*,\bar v)\) 的混合图点，其图值一般会离开 \(\mathcal R\)。因此仅有 \(T_{\mathcal R}\) 图上的假设时不能援引该定理。从约化极限 \(p\in C^*S^\star\) 与 (S2) 可得到完整 shadow 的强收敛和到极限的尾界。若要以一般约化路径长度统一控制原空间路径长度，每一步须另有 \(K\)-Lipschitz 的跨输入比较或沿轨道长度估计。[Alcantara Theorem 5.1 (43)–(49)](https://arxiv.org/html/2611.20523v1#S5.Thmtheorem1)

在后续分量定理中，假设两个**完整**预解式全域单值且分别为 \(K_1,K_2\)-Lipschitz。由 (S1) 定义完整 shadow 映射 \(h(z)=(\bar u,\bar v)\)，输入差给

\[
\begin{aligned}
\|h(z)-h(z')\|&\le K_h\|z-z'\|,\\
K_h&=\|C\|\bigl[\gamma K_1+\tau K_2(1+2\gamma\|L\|K_1)\bigr].
\end{aligned}
\tag{S3}
\]

这个估计适用于任意两次约化输入。它可以由组件直接验证，例如 \(A\) 全域单值且 \(\gamma\operatorname{Lip}(A)<1\)，而 \(D\) 极大单调。另一充分条件是将 Theorem 5.1 的半单调性前件强化为**全对全图**，保留相同的谱余量与另证覆盖。对 \(J_{\gamma A}\) 的任意两个输出，固定任一 \((v_0,b_0)\in\operatorname{gra}D\) 构造两混合图点。其位置差为 \((\bar u-\bar u',0)\)，图值差为 \((\gamma^{-1}(s-s'-(\bar u-\bar u')),-L(\bar u-\bar u'))\)。代入全对不等式即得到 (47) 的任意输入比较。固定任一 \(\operatorname{gra}A\) 图点作对称操作得到 (48)。对任一分量令 \(a_i=\|V_i\|/\gamma_i\)，\((\gamma_1,\gamma_2)=(\gamma,\tau)\)，可取 \(K_i=[1+2a_i+\sqrt{(1+2a_i)^2+4\kappa a_i}]/(2\kappa)\)。

<a id="dd2-splitting-component"></a>
## 由分量假设得到实际步的耗散与误差界

以下给一组统一的局部充分条件。设 \(B\) 全域单值且为 \(b\)-Lipschitz，两个完整分量预解式满足 (S3)。令 \(G(u)=Au+L^*B(Lu)\)，取非空闭目标 \(Z\subseteq\operatorname{zer}G\) 并设 \(S^\star=\{(u_*,B(Lu_*)):u_*\in Z\}\)、\(\mathcal S=C^*S^\star\)。固定 \(1/2<\theta<1\)、\(p>0\)、\(K_G>0\) 和 \(M_A,M_D\ge0\)。在相应的统一正半径邻域内假设

\[
\begin{aligned}
d(u,Z)&\le K_G\,d(0,G(u))^\theta,\\
\langle u-u_*,a+L^*v_*\rangle &\ge-M_A\|u-u_*\|^p
\quad(a\in Au),\\
\langle v-v_*,b_0-Lu_*\rangle&\ge-M_D\|v-v_*\|^p
\quad(b_0\in Dv),
\end{aligned}
\tag{S4}
\]

其中第一式在 \(d(u,Z)\) 小时成立，后两式对每个 \((u_*,v_*)\in S^\star\) 及相应分量位置差足够小的全图点成立。令

\[
c_0=\sqrt{1+\|L\|^2 b^2},\qquad
M=(M_A+M_D)K_h^p,\qquad
K=\|C\|^{1+\theta}K_Gc_0^{1+\theta}.
\]

若 \(M=0\)，或 \(p>2/\theta\)，或 \(p=2/\theta\) 且 \(2M<K^{-2/\theta}\)，则每个约化初值距 \(\mathcal S\) 足够小的完整 \(\alpha=1\) 轨道全程留在相同小窗内。约化、完整 shadow 与原迭代均有有限长度，后两者收敛到同一个 \(x_\infty\in S^\star\)。写 \(t_k=d(z^k,\mathcal S)\)、\(\xi=2-1/\theta\)、\(\nu=2/\theta-2\)，则 \(t_k=O(k^{-1/\nu})\)，各自的尾长度从对应的第 \(k\) 个约化输入估计为 \(O(t_k^\xi)\)。原轨道从任意给定 \(x^0\) 起附加一次有限的初始位移 \(\|h(C^*x^0)-x^0\|\)。

**证明。** 对每个 \(x_*\in S^\star\)，完整覆盖及单值性给 \(h(C^*x_*)=x_*\)。故 \(\mathcal S\) 闭。若 \(C^*x_n\to p_0\) 且 \(x_n\in S^\star\)，由 (S3) 得 \(x_n=h(C^*x_n)\to h(p_0)\in S^\star\)，且 \(C^*h(p_0)=p_0\)。固定输入 \(z\) 及其最近锚 \(p_*=C^*x_*\in\mathcal S\)，取 \(t=d(z,\mathcal S)\)。令 \(\bar x=h(z)\)，则 \(\|\bar x-x_*\|\le K_ht\)，从而 (S4) 全部位置窗适用。任取 \(y=(r,s)\in T(\bar u,\bar v)\)，原图恒等式和交叉项抵消如下

\[
\begin{aligned}
\bar v&=B(L\bar u+s),\\
r-L^*(\bar v-B(L\bar u))&\in G(\bar u),&
\|r-L^*(\bar v-B(L\bar u))\|&\le c_0\|y\|,\\
\langle \bar x-x_*,y\rangle
&=\langle\bar u-u_*,a+L^*v_*\rangle
+\langle\bar v-v_*,b_0-Lu_*\rangle
\ge -Mt^p
\end{aligned}
\tag{S5}
\]

其中 \(a=r-L^*\bar v\in A\bar u\)、\(b_0=s+L\bar u\in D\bar v\)。由 \(Z\) 上最近点 \(u_0\) 的解 lift 估计得

\[
\begin{aligned}
d(C^*\bar x,\mathcal S)&\le \|C\|
\bigl[c_0d(\bar u,Z)+b\|s\|\bigr]\\
&\le\|C\|\bigl[K_Gc_0^{1+\theta}\|y\|^\theta+b\|y\|\bigr].
\end{aligned}
\tag{S6}
\]

(S6) 左边与 \(y\) 无关，因此可在完整 \(T(\bar x)\) 上取残差下确界。也可在 \(T_{\mathcal R}(\bar x)\) 上取下确界。这给的是真残差估计，允许多值且无需残差达到。对实际 \(y=Cq\) 有

\[
\langle q,C^*\bar x-p_*\rangle\ge-Mt^p,\qquad
d(C^*\bar x,\mathcal S)\le K\|q\|^\theta+b\|C\|^2\|q\|.
\tag{S7}
\]

最近锚和平方展开给 \(t^2-d(z^+,\mathcal S)^2\ge\|q\|^2-2Mt^p\)。由下文的实际步证明，约化轨道有限长度、幂次尾界，且极限 \(z_\infty\in\mathcal S\)。由 (S3) 可得从 \(j=k\) 起的完整 shadow 尾长至多 \(K_h\sum_{j\ge k}\|z^{j+1}-z^j\|\)。又 \(x^{k+1}=\bar x^k\) 且 \(h(z_\infty)\in S^\star\)。这个论证直接由强 Cauchy 极限与闭目标集识别零点。

**实际步证明。** 这一段也适用于后文的其他分裂。设工作窗内输入、输出高度为 \(t,a\ge0\)，实际步长为 \(s\ge0\)，且

\[
t^2-a^2\ge\chi s^2-2Mt^p,\qquad
t\le Hs^\theta+Js,\qquad \chi,H>0,\quad J\ge0 .
\tag{S8}
\]

第一式使 \(s\) 随 \(t\downarrow0\) 一致趋零。对每个 \(0<c<H^{-1/\theta}\)，缩窗后 \(s\ge ct^{1/\theta}\)。当 \(M=0\)、\(p>2/\theta\) 或 \(p=2/\theta,\ 2M<\chi H^{-2/\theta}\) 时，可选 \(c\)、\(\delta>0\) 和小窗使 \(t^2-a^2\ge\delta s^2\)。\(t>0\) 时，

\[
t-a\ge \frac{\delta c^2}{2}t^{2/\theta-1},\qquad
s\le\frac{2}{\delta c} t^{1-1/\theta}(t-a)
\le\frac{2}{\xi\delta c}(t^\xi-a^\xi),\qquad
\xi=2-\frac1\theta .
\]

最后一步用幂函数凹性。\(t=0\) 时 \(s=a=0\)。若每个小 \(t\) 都有一步并享有同一估计，则距离不增保证小窗归纳。对实际步求和得有限长度及尾界。设 \(\nu=2/\theta-2\)，对正距离用 \(t^{-\nu}\) 的凸性得到 \(t_{k+1}^{-\nu}-t_k^{-\nu}\ge\nu\delta c^2/2\)，故 \(t_k=O(k^{-1/\nu})\)。用在 (S7) 时 \(s=\|q\|,\ \chi=1,\ H=K,\ J=1+b\|C\|^2\)，第二式来自 \(t\le d(z^+,\mathcal S)+\|q\|\)。这是 C399 的同一步耗散证明。

<a id="dd2-splitting-anchored-threshold"></a>
## 点锚恢复的完整长度门槛

设约化轨道已由 (S8) 得到 \(t_{k+1}\le t_k-\gamma_0t_k^{1+\nu}\) 及约化尾长 \(O(t_k^\xi)\)，并假设 (S2) 对同一 \(S^\star\) 的全部零锚成立。取各步最近点 \(p_k\in\mathcal S\) 及 lift \(x_*^k\in S^\star\)。零点本身是自己约化输入的 shadow，故 (S2) 给

\[
\|x_*^{k+1}-x_*^k\|\le K_{\rm PD}\|p_{k+1}-p_k\|.
\]

由此

\[
\|\bar x^{k+1}-\bar x^k\|
\le K_{\rm PD}\bigl[2(t_{k+1}+t_k)+\|z^{k+1}-z^k\|\bigr].
\tag{S14}
\]

当 \(\theta>2/3\)，令 \(b_*=1-\nu=3-2/\theta>0\)。幂函数凹性给 \(t_k^{b_*}-t_{k+1}^{b_*}\ge b_*\gamma_0t_k\)，故 \(\sum_{j\ge k}t_j\le t_k^{b_*}/(b_*\gamma_0)\)。(S14) 给完整 shadow 和原迭代的有限长度，尾长 \(O(t_k^{b_*})\)。这适用于全图点锚恢复，允许完整 shadow 在非零输入处多值。以下临界 CP／DR 说明 \(\theta>2/3\) 是该组统一假设下的尖锐条件。

**反例。** 取 \(X=Y=\mathbb R^2,\ L=I,\ \gamma=\tau=1\) 及 \(Cz=(z,-z)\)。用 \(R_\alpha\) 表示平面旋转，设

\[
\vartheta(r)=2\arcsin\!\sqrt{\min(r,1/4)},\qquad
M_A z=R_{\phi(\|z\|)}z,\qquad M_B z=R_{\vartheta(\|z\|)-\phi(\|z\|)}z .
\]

两个 \(M_i\) 在零点取零，\(\phi\) 有界且在 \((0,\infty)\) 上连续，稍后选取。定义 \(J_i=(I+M_i)/2\)，并用 \(\{(J_i z,z-J_i z):z\in\mathbb R^2\}\) 分别定义 \(A,B\) 的完整图。任一图点的两分量和是原预解式输入，所以这确实给出全域单值的完整 \(J_A,J_B\)。连续性来自 \(\phi,\vartheta\) 的非零连续性和零点的幅值界，完整图也闭。由于 \(\|M_i z\|=\|z\|\)，各分量图点 \((u,a)\) 满足 \(\langle a,u\rangle=(\|z\|^2-\|M_i z\|^2)/4=0\)。逆图交换保留该等式，故 \(\langle x,y\rangle=0\) 对全图 \(y\in T(x)\) 成立，满足 \(U=V=0\) 的 Theorem 5.1 条件。

DR 的完整约化更新恰为

\[
R(z)=\tfrac12(I+M_BM_A)z
=\cos(\vartheta(r)/2) R_{\vartheta(r)/2}z,\qquad r=\|z\|.
\]

径向函数 \(r\sqrt{1-\min(r,1/4)}\) 严格增，从而 \(R\) 单射。其唯一固定点为零，完整 \(T\) 也只有零解，因为压缩零点必须固定 \(R\)，且两个分量的零输入输出唯一。任意 \(y'\in T_{\mathcal R}(x)\) 给出 \(y'=Cq'\) 及输入 \(C^*x+q'\)，因此 \(C^*x=R(C^*x+q')\)。由 \(R\) 单射，每个 \(T_{\mathcal R}(x)\) 的非空纤维都单值。对小输入，完整图的实际值域残差为 \(\|y'\|=\sqrt2\|z-R(z)\|=\sqrt2 r^{3/2}\)，而 \(d(C^*x,\{0\})\le r\)。这个计算验证了值域限制的真 Hölder 误差界 \(\theta=2/3\)，也适用于同窗内的每个 \(0<\theta<2/3\)。完整 shadow 满足 \(\|\bar u\|\le r,\ \|\bar v\|\le r\)，符合 (S2)。

固定 \(0<r_0<1/4\)，定义 \(r_{k+1}=r_k\sqrt{1-r_k}\)。这些半径严格降至零，由

\[
r_{k+1}^{-1}-r_k^{-1}
=\frac{(1-r_k)^{-1/2}-1}{r_k}\longrightarrow \frac12
\]

得到 \(r_k\sim 2/k\)。令 \(\phi(r_k)=(-1)^k\pi/3\)，逐区间 \([r_{k+1},r_k]\) 线性插值，并在 \(r\ge r_0\) 恒取 \(\pi/3\)。从任意 \(\|z^0\|=r_0\) 开始，约化步长为 \(r_k^{3/2}\)，故约化路径有限长。另一方面，

\[
\bar u^k=\cos(\pi/6)R_{(-1)^k\pi/6}z^k,\qquad
\frac{\|\bar u^{k+1}-\bar u^k\|}{r_k}\longrightarrow \sin(\pi/3)>0
\]

因为 \(z^{k+1}\) 相对 \(z^k\) 的角变化趋于零且半径比趋于一。由 \(\sum_k r_k=\infty\)，原空间完整 shadow 与完整 CP／DR 原迭代均无限长，仍强收敛到零。从任意后段切入给出同一算子任意小的坏初值。这个反例使用 \(T_{\mathcal R}\) 的真误差界，(S2) 及 \(U=V=0\) 则在完整图上成立。

<a id="dd2-splitting-nonzero-u"></a>
## 保留非零 \(U\) 的分量运算

给定零锚 \(x_*=(u_*,v_*)\in S^\star\)，对分量分别在 \((u_*,-L^*v_*)\in\operatorname{gra}A\) 和 \((v_*,Lu_*)\in\operatorname{gra}D\) 处取相对半单调模 \((M_A,N_A),(M_D,N_D)\)。本节的 \(M_A,M_D\) 为自伴算子。若直接掌握 \(B\) 的相对模，交换定义域与图值即可取得 \(D=B^{-1}\) 的两模。令

\[
\mathcal K=\begin{pmatrix}0&L^*\\-L&0\end{pmatrix},\quad
M=M_A\oplus M_D,\quad N=N_A\oplus N_D,\quad d=x-x_*,\quad y\in T(x).
\]

相对分量不等式与 \(\langle d,\mathcal Kd\rangle=0\) 给出

\[
\langle d,y\rangle\ge\langle d,Md\rangle+\langle y-\mathcal Kd,N(y-\mathcal Kd)\rangle.
\tag{S9}
\]

任取块对角自伴 \(W\succeq\varepsilon I\)，\(\varepsilon>0\)。下列块对角自伴算子是 \(T\) 同一全图、同一零锚的合法相对模

\[
V=N-W,\qquad
U=M+\mathcal K^*(N-NW^{-1}N)\mathcal K.
\tag{S10}
\]

事实上 (S9) 右端减去 \(\langle d,Ud\rangle+\langle y,Vy\rangle\) 恰等于 \(\|W^{1/2}y-W^{-1/2}N\mathcal Kd\|^2\)。因此固定 \(M,N,W\) 时，(S10) 是将 \(y\) 当作任意独立向量完成平方所得的最大位置模。真实图可能提供额外信息，允许更大的 \(U\)。若 \(N\succeq0\)，也可从 (S9) 直接取 \(U=M,V=0\)，涵盖 \(N=0\)。

将 (S10) 用入 Theorem 5.1 仍须逐例检验 \(U+\sigma P\succeq0\) 和 \(I_{\mathcal R}+C^*VC-\sigma I_{\mathcal R}\succeq\kappa I_{\mathcal R}\)。用于 DD2 耗散时，若在同一实际窗有

\[
\langle \bar x-x_*,U(\bar x-x_*)\rangle\ge D_+(x,\bar x,x_*)-Mt^p,\quad D_+\ge0,\qquad
C^*VC\succeq\eta I_{\mathcal R},\quad \eta>-1/2 ,
\]

则 \(t^2-a^2\ge(1+2\eta)\|q\|^2+2D_+-2Mt^p\)。伴随真 Hölder 残差界，(S8) 以 \(\chi=1+2\eta\) 使用。若缺陷按 (S8) 吸收，还得到 \(2\sum_k D_+(x^k,\bar x^k,x_*^k)\le t_0^2\)。仅有 \(U\succeq-\sigma P\) 时，负项一般量级为 \(t^2\)，不能自动按 \(p>2/\theta\) 吸收。另外，\(U\) 在 \(\ker P\) 上正定与 \(U\succeq cP\) 是不同的条件。

Evens–Latafat–Patrinos 的分量半单调计算用平行和给出 \(U=0\) 的斜弱 Minty 模。Alcantara §6 明确提出保留非零位置模的问题。(S10) 闭合一个显式充分方向，最优可行模、谱余量参数的比较和公开优先性仍需另查。[Evens–Latafat–Patrinos §4 Lemma 4.11、§5 Theorem 5.1](https://arxiv.org/pdf/2312.06540) · [Alcantara §6](https://arxiv.org/html/2611.20523v1#S6)

<a id="dd2-splitting-slow-example"></a>
## 完整非单调慢轨道与非零 \(U\)

取 \(X=Y=\mathbb R,\ L=I,\ \gamma=\tau=1,\ a_0=1/64\)，定义

\[
A(u)=-a_0\frac{u^3}{1+u^2},\qquad B(w)=w\sqrt{\frac{|w|}{1+|w|}},\qquad D=B^{-1}.
\tag{S11}
\]

\(P\) 的秩为 1，取 \(Cz=(z,-z)\)，约化状态 \(z=u-v\)。\(A\) 全域 Lipschitz 常数至多 \(3a_0/2<1\)，因为 \((u^3/(1+u^2))'=u^2/(1+u^2)+2u^2/(1+u^2)^2\)。故 \(J_A\) 全域唯一且 Lipschitz，由 \(u=z-A(u)\) 的收缩定点或 \(I+A\) 严格增且满射可见。\(B\) 奇、严格增、满射、全域 \(1\)-Lipschitz。对 \(w>0\)，设 \(b=\sqrt{w/(1+w)}\in(0,1)\)，则 \(B'(w)=(3b-b^3)/2\in(0,1)\)。于是 \(D\) 全域 \(1\)-强单调，\(J_D\) 全域唯一且 \(1/2\)-Lipschitz。整个 CP/DR 都是完整预解式更新。

若 \(r=|u|>0\)，则

\[
\frac{|A(u)|}{a_0|B(u)|}
=\frac{r^{3/2}\sqrt{1+r}}{1+r^2}\le\sqrt2 .
\]

当 \(r\le1\) 用分子不超过 \(\sqrt2\)。当 \(r\ge1\) 用分子不超过 \(\sqrt2 r^2\)。故 \(A+B\) 与 \(u\) 同号，唯一原始解及唯一原始–对偶解均为零。对 \(r\le1\)，\(|A(u)+B(u)|\ge(1-\sqrt2 a_0)r^{3/2}/\sqrt2\)，给原始真残差的 \(\theta=2/3\) 误差界。由 (S6) 得原始–对偶真残差及值域限制真残差的同指数估计。\(D\) 单调，且 \(uA(u)\ge-a_0|u|^4\)，所以 (S4) 以 \(p=4>2/\theta=3\) 成立。完整图 \(T\) 非单调，因 \(\langle (u,0),T(u,0)\rangle=-a_0u^4/(1+u^2)<0\) 对任意 \(u\ne0\)。

同一例另有一个具正半定非零 \(U\) 的全图证书。记 \(w=Dv\)，\(\phi(t)=t^4/(1+t^2)\)。由 \(\sqrt{\phi(t)}=t^2/\sqrt{1+t^2}\) 的导数可知其全域 \(2\)-Lipschitz，故 \(\phi(u)\le2\phi(w)+8|u-w|^2\)。上面的分子比界给 \(\phi(w)\le\sqrt2\,w B(w)\)。又由同号及 \(|B(w)|\le|w|\) 得 \(wB(w)\ge v^2\)。因此对原算子的完整图有

\[
\langle (u,v),T(u,v)\rangle
=wB(w)-a_0\phi(u)
\ge(1-2\sqrt2a_0)wB(w)-8a_0|Dv-u|^2
\ge \tfrac12v^2-\tfrac18|Dv-u|^2 .
\tag{S12}
\]

这里 \(U=\operatorname{diag}(0,1/2)\) 与 \(V=\operatorname{diag}(0,-1/8)\)，并有 \(I+C^*VC=(7/8)I\)、\(\sigma=0\)。\(U\) 在 \(\ker P=\{(t,t):t\in\mathbb R\}\) 上正定，而每个 \(\mu>0\) 均有 \(U\not\succeq\mu P\)，以 \((u,0)\) 即见。沿实际步，有 \(|z|^2-|z^+|^2\ge (3/4)|q|^2+|\bar v|^2\)。因此额外保持了 \(\sum_k|\bar v^k|^2\le |z^0|^2\)，且 (S8) 的 DD2 结论也可直接由这条耗散和真 Hölder 误差界取得。

**精确的慢速分离。** 由 (S1) 有 \(\bar u=J_A z=z+O(|z|^3)\)，\(\bar v=J_D(2\bar u-z)\)。写 \(t=2\bar u-z\)，\(w+D^{-1}(w)=t\)，则 \(\bar v=B(w)\)。因为 \(B(w)=\operatorname{sgn}(w)|w|^{3/2}(1+O(|w|))\)，有 \(w/t\to1\)，从而

\[
z^+=\bar u-\bar v=z-\operatorname{sgn}(z)|z|^{3/2}(1+o(1)).
\tag{S13}
\]

足够小的非零状态保号、绝对值严格下降、两分量均非零，并由唯一固定点与连续性收敛到零。令 \(t_k=|z^k|\)；(S13) 给 \(t_{k+1}^{-1/2}-t_k^{-1/2}\to1/2\)，所以 \(t_k\sim 4/k^2\)。\(\|h(z)\|/|z|\to1\)，完整 shadow 和原迭代同样是实际次线性。对任意足够小的正距离窗，\(\sup_{z\ne0}|z^+|/|z|=1\)，且任意固定 \(m\) 有 \(|z^m|/|z^0|\to1\) 当 \(z^0\to0\)。以 \(z\to0\) 的实际输出 \(\bar x=h(z)\) 检查真残差，完整 \(T(\bar x)=T_{\mathcal R}(\bar x)=\{Cq\}\)，其中 \(\|Cq\|\sim\sqrt2|z|^{3/2}\) 而 \(\|\bar x\|\sim|z|\)。由此排除 \(T\)、\(T_{\mathcal R}\) 的局部线性次正则，及约化位移 \(q=z-z^+\) 在零点的线性次正则。故该例在原算法内分离出有限长度与统一线性距离缩小和 R 线性率。

**与 DR 特例不同的临界 CP。** 取 \(X=Y=\mathbb R^2\)、\(L=\operatorname{diag}(1,1/2)\)、\(\gamma=\tau=1\)，令 \(A=(A_1,I)\)、\(B=(B_1,I)\)，第一分量为 (S11)，第二分量为单位线性算子。按两个通道重排，\(P\) 有秩 1 的首块及正定的次块，故 \(P\) 秩 3，且 \(L\) 的奇异值分别为 1、1/2。全图、覆盖、配对恢复及缺陷逐块成立。原始算子为 \((A_1+B_1,(5/4)I)\)，故 \(\theta=2/3\) 的局部真误差界成立。次块 \(\langle T_2d,d\rangle=\|d\|^2\)，沿实际步得到

\[
\|z_2\|^2-\|z_2^+\|^2\ge 2\|\bar x_2\|^2
\ge 2\|C_2\|^{-2}\|z_2^+\|^2 .
\]

第一通道保持 (S13)，所以约化初值首分量非零时，每个充分小完整 CP 轨道的约化距离仍等价于 \(4/k^2\)。正半定证书可取首块 (S12) 与次块 \(U_2=I,V_2=0\) 的直和。本例在非等距 \(L\) 上给出临界 CP，两个奇异通道在该构造中独立。

**不能省掉的前件。** 同样取标量 \(L=I,\gamma=\tau=1\)。若 \(A=-I,\ B=2I\)，则 \(A+B=I\) 有线性误差界，但 \(J_A(z)\) 对每个非零 \(z\) 为空。若 \(A=-3I/4,\ B=I/4\)，则两个完整分量预解式全域单值 Lipschitz，原始算子 \(A+B=-I/2\) 也有线性误差界。实际 DR 更新此时是 \(z^+=(13/5)z\)。所以复合误差界和两分量覆盖、Lipschitz 恢复均须与实际步锚定耗散配合。

<a id="dd2-splitting-others"></a>
## 其他分裂的实际步证书及边界

Alcantara §6 提出外梯度、前向–后向–前向、前向反射–后向及更一般分布式分裂的后续问题。下面给前三者的局部充分版本。它们各自使用原算法步与相应的图残差。分布式情形的同一步表述、值域闭性和物理量恢复条件需对具体方法验证。[Alcantara §6](https://arxiv.org/html/2611.20523v1#S6)

**前向–后向–前向。** 设 \(F=A+B\)，\(B\) 全域 \(L_B\)-Lipschitz，固定 \(\ell=\lambda L_B<1\)。更新 \(y=J_{\lambda A}(x-\lambda Bx)\)，\(x^+=y+e\)，\(e=\lambda(Bx-By)\)。令 \(d=x-y,\ q=d-e=x-x^+\)，则 \(q/\lambda\in F(y)\) 且 \(\|e\|\le\ell\|d\|\)。对最近零锚 \(p_*\) 有

\[
\|x-p_*\|^2-\|x^+-p_*\|^2
=2\langle q,y-p_*\rangle+\|d\|^2-\|e\|^2 .
\]

若实际配对满足 \(\langle q,y-p_*\rangle\ge-Md(x,S)^p\)，则 (S8) 的 \(\chi=(1-\ell)/(1+\ell)\) 足够。若 \(d(y,S)\le K_F d(0,F(y))^\theta\)，则

\[
d(x^+,S)\le K_F\lambda^{-\theta}\|q\|^\theta+\frac{\ell}{1-\ell}\|q\|.
\]

加上 \(d(x,S)\le d(x^+,S)+\|q\|\) 得 (S8)。例如 \(J_{\lambda A}\) 全域单值 Lipschitz 时，\(y\) 到零锚的距离至多 \(\operatorname{Lip}(J_{\lambda A})(1+\ell)d(x,S)\)，故分量图上的局部 Hölder 真误差界和 \(p\)-阶锚定缺陷可在同一小窗使用。零集闭、覆盖和 (S8) 的幂次门给有限长度与强收敛，\(y\) 的有限长度再由其输入 Lipschitz 性转移。[Tseng 2000](https://doi.org/10.1137/S0363012998338806)

**外梯度。** 设 \(K_0\) 是非空闭凸集，\(F=N_{K_0}+B\)，\(S\subseteq\operatorname{zer}F\) 非空闭，\(x\in K_0\)，采用真实的双投影

\[
y=\Pi_{K_0}(x-\lambda Bx),\qquad x^+=\Pi_{K_0}(x-\lambda By),\qquad
d=x-y,\quad e=x^+-y,\quad q=d-e .
\]

\(\|e\|\le\ell\|d\|\) 由投影非扩张性得出。两次投影不等式分别给 \(\langle q,x^+-p_*\rangle\ge\lambda\langle By,x^+-p_*\rangle\) 和 \(\langle d,e\rangle\le\lambda\langle Bx,e\rangle\)，故

\[
\|x-p_*\|^2-\|x^+-p_*\|^2
\ge 2\lambda\langle By,y-p_*\rangle+
\|d\|^2+\|e\|^2-2\ell\|d\|\|e\| .
\]

设 \(p_*\) 是最近零锚。若 \(\lambda\langle By,y-p_*\rangle\ge-Md(x,S)^p\)，则 \(\chi=(1-\ell)/2\) 足够。原图上 \(d/\lambda-Bx+By\in F(y)\)，范数至多 \((1+\ell)\|q\|/(\lambda(1-\ell))\)。同样由真误差界及 \(\|x^+-y\|\le\ell\|q\|/(1-\ell)\) 得 (S8)。例如输入窗内的 \(\langle By-Bp_*,y-p_*\rangle\ge-M_0\|y-p_*\|^p\) 可由 \(\langle Bp_*,y-p_*\rangle\ge0\) 及 \(\|y-p_*\|\le(1+\ell)d(x,S)\) 转移。前者是零锚的变分不等式条件。双投影的全域覆盖与 \(K_0\) 的不变性是显然的。

**前向反射–后向。** 在 \(F=A+B,\ \ell=\lambda L_B<1/2\) 下取固定步长，设 \(J_{\lambda A}\) 全域单值 Lipschitz。采用 \((x,w)\mapsto (y,x)\) 且 \(y=J_{\lambda A}(x-2\lambda Bx+\lambda Bw)\)。若直接使用增广欧氏距离，即使 \(A=0,B=I,0<\lambda<1/2\)，从 \((\varepsilon,0)\) 一步出发到 \(((1-2\lambda)\varepsilon,\varepsilon)\) 也严格增距。这里原线性迭代仍收敛，因特征根 \((1-2\lambda\pm\sqrt{1+4\lambda^2})/2\) 均在单位圆内。匹配的能量可从 Malitsky–Tam 的 (22) 得到。[Malitsky–Tam §2 Lemma 2.4 及 (22)](https://arxiv.org/html/1808.04162v4#S2)

令 \(d=y-x,\ e=x-w,\ V_x=Bx-Bw,\ V_y=By-Bx\)，则 \(r=-d/\lambda+V_y-V_x\in F(y)\)。对零锚 \(p_*\in S\) 记

\[
E_{p_*}(x,w)=\|x-p_*\|^2-2\lambda\langle V_x,x-p_*\rangle+\tfrac12\|e\|^2 .
\]

以 \(s=\sqrt{\|d\|^2+\|e\|^2}\) 表示实际增广步长，代数给

\[
E_{p_*}(x,w)-E_{p_*}(y,x)
=2\lambda\langle r,y-p_*\rangle+\tfrac12s^2+2\lambda\langle V_x,d\rangle
\ge2\lambda\langle r,y-p_*\rangle+(\tfrac12-\ell)s^2 .
\]

令 \(E(x,w)=\min_{p_*\in S}E_{p_*}(x,w)\)，有限维及闭非空 \(S\) 给极小锚。各能量满足

\[
(\tfrac12-\ell)(\|x-p_*\|^2+\|e\|^2)\le E_{p_*}(x,w)
\le (1+\ell)(\|x-p_*\|^2+\|e\|^2).
\]

令 \(t=\sqrt{E(x,w)},\ a=\sqrt{E(y,x)}\)。在达到 \(E(x,w)\) 的零锚处，\(p_*=J_{\lambda A}(p_*-\lambda Bp_*)\)，从而

\[
\|y-p_*\|\le\operatorname{Lip}(J_{\lambda A})
\bigl[(1+\ell)\|x-p_*\|+\ell\|e\|\bigr]\le K_yt .
\]

所以统一局部图缺陷 \(\lambda\langle r,y-p_*\rangle\ge-M_0\|y-p_*\|^p\) 给 (S8) 的第一式，其中 \(\chi=1/2-\ell,\ M=M_0K_y^p\)。真 Hölder 误差界和 \(\|r\|\le \lambda^{-1}\sqrt{(1+\ell)^2+\ell^2}\,s\) 得 \(d(y,S)\le H_0s^\theta\)。又 \(t\le\sqrt{1+\ell}(d(x,S)+\|e\|)\le\sqrt{1+\ell}(d(y,S)+\sqrt2 s)\)，故 (S8) 两式齐备。由相同幂次门，完整增广状态有限长度。能量下界给 \(d(x^k,S)\to0\) 与 \(x^k-x^{k-1}\to0\)，故闭性将极限识别为 \((p_*,p_*)\) 且 \(p_*\in S\)。变步长、一般多值及更宽的步长端点需各自核能量和实际状态量词。

<a id="dd2-splitting-open"></a>
## 适用边界

- 在固定 \(\alpha=1\) 的 CP／DR 中，可验证的分量前件给出 DD2、原空间实际长度及慢速严格例。只有 Alcantara 的点锚恢复时，强收敛与到极限的误差可直接传递，幂次族在 \(\theta>2/3\) 时还能由可求和的锚距离传递完整长度。临界 \(\theta=2/3\) 的完整 CP／DR 图排除同一统一推断延伸到端点。
- 非零 \(U\) 的显式分量传递及其可行实例已经给出。最优选择 \(W\)、不同原图子空间的谱余量、以及对没有全域 Lipschitz 分量预解式的真实非凸结构的应用，需要独立证明。接受更弱的负位置模时，必须核它在实际输出上的耗散尺度，不宜只引用 \(U\succeq-\sigma P\)。
- 闭值域只是退化 Hilbert 约化的入口。如果扩至任意闭目标集的无限维版本，还需最近锚存在或控制近似锚误差。变松弛时要额外控制实际更新而非近端 shadow 步长，方向相关上界和临界步长序列另行处理。
- 其他分裂这里闭合的是明确的固定步长实际步及幂次能量估计，分布式/一般多算子版与 Alcantara §3 的相对半单调前向表示仍应逐对象核对。
