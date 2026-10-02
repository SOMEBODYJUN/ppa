# 两种条件刷新残差：二进制守恒边缘与 Gaussian Gibbs

本页的两个定理使用**不同的状态空间、距离与残差**。二进制的
\(\mathsf W_\nu,\mathcal R\) 不能代入 Gaussian 的
\(W_{2,Q},\mathcal R_Q\)；二者也不是同步最优运输残差 \(\Psi\)。
证明从各自核和全部概率律重新组织，不把原稿编号或程序 PASS 当作证据。

<a id="cr-binary-object"></a>
## C129-v1：固定边缘的二进制对象

取标准 Borel 空间 \(U\) 上固定概率律 \(\nu\)，有限
\(X=\{0,1\}^m\)，\(m\ge1\)。律类
\(\mathscr M_\nu=\{\mu(du,dx)=\nu(du)\mu_u(dx)\}\)，其条件距离为
\[
\mathsf W_\nu(\mu,\eta)^2
=\int W_2(\mu_u,\eta_u)^2\,\nu(du),
\tag{CR1}
\]
其中纤维平方欧氏成本为 Hamming 距离，耦合必须保持 \(u\)。
给可测 \(b_i(u)\in(0,1),p_i(u)>0\) 且
\(\sum_i p_i(u)\le1\) 几乎处处；余概率作恒等更新。选坐标 \(i\)
时以独立 \(\operatorname{Bern}(b_i(u))\) 替换该位，其余位不变。
\(\beta_u=\bigotimes_i\operatorname{Bern}(b_i(u))\)，
\(\pi_\nu(du,dx)=\nu(du)\beta_u(dx)\)。记
\[
E(\mu)=\mathsf W_\nu(\mu,\pi_\nu),\quad
d_i(u;\mu)^2=\sum_{x_{-i}}\mu_u(x_{-i})
\left|\mu_u(X_i=1\mid x_{-i})-b_i(u)\right|,
\quad \mathcal R(\mu)^2=\int\sum_i p_i(u)d_i(u;\mu)^2\,\nu(du).
\tag{CR2}
\]
零概率条件事件的任意条件版本不改变和式。设
\(a_*={\rm ess\,inf}_{u\sim\nu}\min_i p_i(u)\in[0,1]\)。

<a id="cr-binary-theorem"></a>
## C129-v1：精确零、统一误差界与锐速率

\(\pi_\nu\) 是 \(\mathscr M_\nu\) 中唯一不变律，且对每个该律
\(\mathcal R(\mu)=0\iff\mu=\pi_\nu\)。以下五项等价：

1. \(a_*>0\)；
2. 存在统一有限 \(K\)，对全部 \(\mu\) 有 \(E(\mu)\le K\mathcal R(\mu)\)；
3. 存在 \(c<1\)，对全部 \(\mu\) 有 \(E(\mu P)\le cE(\mu)\)；
4. 某个固定 \(N\ge1\) 和 \(c_N<1\) 对全部 \(\mu\) 满足 \(E(\mu P^N)\le c_NE(\mu)\)；
5. 统一 \(C<\infty,c<1\) 对全部 \(\mu,k\ge0\) 满足 \(E(\mu P^k)\le Cc^kE(\mu)\)。

若 \(a_*>0\)，最佳统一 EB 系数是 \(a_*^{-1/2}\)，对每个固定
\(k\ge1\) 的最佳相对距离因子是 \((1-a_*)^{k/2}\)。若 \(a_*=0\)，
每条律仍有 \(E(\mu P^k)\to0\)，但每个固定 \(k\) 的最坏相对因子为 1，
没有统一有限线性 EB。上述最佳系数在围绕 \(\pi_\nu\) 的任何固定正半径
**完整条件距离球**上仍相同；这里的收缩是**到目标距离**，不是任意
两律间的统一 Lipschitz 收缩声明。

**证明。** 对任一纤维律 \(\gamma\) 与乘积 Bernoulli \(\beta\)，
依次按过去坐标 \(X_{<i}\) 耦合 \(X_i\) 和目标第 \(i\) 位：
前者保留 \(\gamma(X_i=1\mid X_{<i})\)，后者条件于已构造的全部
配对历史仍为 Bernoulli\((b_i)\)。最优二值耦合的错位概率为两参数差的
绝对值，故 \(Y\) 保持乘积律，\(X\) 保持 \(\gamma\)。因为
\(X_{<i}\) 的信息包含于 \(X_{-i}\) 的信息，用条件期望的 Jensen 不等式得到
\[
W_2(\gamma,\beta)^2\le
\sum_i\mathbb E_\gamma
|\gamma(X_i=1\mid X_{<i})-b_i|
\le\sum_i\mathbb E_\gamma
|\gamma(X_i=1\mid X_{-i})-b_i|.
\tag{CR3}
\]
逐纤维积分给 \(E^2\le\int\sum_i d_i^2\,d\nu\)。若 \(a_*>0\)，
这不超过 \(\mathcal R^2/a_*\)；若 \(\mathcal R=0\)，即使
\(a_*=0\)，正权 \(p_i(u)>0\) 与 (CR3) 仍给 \(E=0\)。

对 \(\mu_u\) 与 \(\beta_u\) 取最优纤维耦合，同步选择更新坐标并
共用新 Bernoulli 位；旧耦合的一次 Hamming 错位中，第 \(i\) 位以
概率 \(p_i(u)\) 消去。因此纤维成本每步至多乘
\(1-\min_i p_i(u)\)，从而
\[
E(\mu P^k)^2\le\int(1-\min_i p_i(u))^k
W_2(\mu_u,\beta_u)^2\,\nu(du)
\le(1-a_*)^k E(\mu)^2.
\tag{CR4}
\]
每个纤维的 \(\min_i p_i(u)>0\)；支配收敛证明即使 \(a_*=0\)
每条律也趋于目标。因 \(\pi_\nu P=\pi_\nu\)，这又证明唯一不变律。

为核最佳常数，取 \(\epsilon>0\)。有限个坐标中有某个 \(i\)
及正 \(\nu\)-测度集合 \(A\)，在其上 \(p_i<a_*+\epsilon\)。
只在 \(A\) 内把目标第 \(i\) 位的 Bernoulli 参数朝离它较远的端点
按同一小比例 \(s>0\) 扰动，记差 \(h(u)>0\)。此时其它位仍与目标独立，
纤维 Hamming 运输的该边缘差既是下界又可由只搬动该位取到，故
\[
E^2=\int_Ah\,d\nu,\quad
\mathcal R^2=\int_Ap_i h\,d\nu,\quad
E(\mu P^k)^2=\int_A(1-p_i)^k h\,d\nu.
\tag{CR5}
\]
令 \(\epsilon\downarrow0\) 给 EB 和各固定 \(k\) 的锐性，
包括 \(a_*=0\) 的无限 EB 系数/最坏因子 1；令 \(s\downarrow0\)
使同一见证落进任意正半径完整球。五项中 (1) 推 (2)–(5)，
(2) 与 (4) 在 \(a_*=0\) 被 (CR5) 排除，(3) 是 (4) 特例，
(5) 取足够大共同 \(N\) 又给 (4)。证毕。

<a id="cr-gaussian-object"></a>
## C130-v1：Gaussian Gibbs 对象

取 \(Q\in\mathbb R^{m\times m}\) 对称正定、\(m_0\in\mathbb R^m\)，
目标 \(\beta=N(m_0,Q^{-1})\)；固定 \(p_i>0,\sum_i p_i=1\)，
\(D=\operatorname{diag}(p_i/Q_{ii})\)、
\(\zeta=\lambda_{\min}(Q^{1/2}DQ^{1/2})>0\)。
每步选择 \(i\)，以 \(\beta\) 的第 \(i\) 位全条件 Gaussian 律
刷新该位，其余坐标不变。\(W_{2,Q}\) 用平方成本
\((x-y)^TQ(x-y)\)；对每个有限二阶矩律 \(\mu\) 定义
\[
\mathcal R_Q(\mu)^2=\sum_i p_iQ_{ii}\int
W_2\bigl(\mu_i(\cdot\mid x_{-i}),
\beta_i(\cdot\mid x_{-i})\bigr)^2\,\mu_{-i}(dx_{-i}).
\tag{CR6}
\]
右侧的一维 \(W_2\) 是通常欧氏距离；它不是 (CR1) 的守恒边缘
运输，也不是同步残差 \(\Psi\)。\(\mu\in\mathcal P_2\) 时
\(\mathcal R_Q(\mu)<\infty\)：条件二阶矩可积，目标条件均值是
\(x_{-i}\) 的仿射函数；以条件独立耦合估计，具体有
\(\mathcal R_Q(\mu)^2\le
\mathbb E_\mu[(X-m_0)^TQDQ(X-m_0)]+1<\infty\)。

<a id="cr-gaussian-theorem"></a>
## C130-v1：锐条件误差界与有效收缩

在全部有限二阶矩律上，
\[
W_{2,Q}(\mu,\beta)^2\le\zeta^{-1}\mathcal R_Q(\mu)^2,
\qquad
W_{2,Q}(\mu P,\beta)\le\sqrt{1-\zeta}\,W_{2,Q}(\mu,\beta).
\tag{CR7}
\]
\(\zeta^{-1/2}\) 是 EB 的全局及每个完整正半径目标球上的最佳
**未平方**系数；第二项只宣称有效因子，不宣称锐。
\(\beta\) 是有限二阶矩类唯一不变律，
\(\mathcal R_Q(\mu)=0\iff\mu=\beta\)。

**证明。** 目标条件均值记为
\(\bar m_i(z_{-i})=(m_0)_i-
\sum_{j\ne i}Q_{ij}(z_j-(m_0)_j)/Q_{ii}\)，
条件方差 \(Q_{ii}^{-1}\)。同噪声刷新两个点的差由
\(A_i=I-e_ie_i^TQ/Q_{ii}\) 作用，且
\[
\sum_i p_i\|A_ih\|_Q^2
=\|h\|_Q^2-h^TQDQh\le(1-\zeta)\|h\|_Q^2.
\tag{CR8}
\]
\(\beta\) 在每个目标 Gibbs 更新下不变。对 \(\mu,\beta\)
的最优输入耦合同噪声更新，即得 (CR7) 的收缩项。
又 \(\operatorname{tr}(Q^{1/2}DQ^{1/2})=\sum_i p_i=1\)，
所以 \(0<\zeta\le1\)，系数有意义。

为证更强的 EB，从任一有限成本的 \((X,Y)\) 耦合开始，
始终保持边缘为 \((\mu,\beta)\)。给定所选 \(i\)，用与旧
\((X,Y)\) **独立**的新均匀随机数 \(U_i\)，只按
\(X_{-i}\) 选择一维分位数最优耦合
\(X'_i\sim\mu_i(\cdot\mid X_{-i})\) 与
\(Z_i\sim\beta_i(\cdot\mid X_{-i})\)，并令
\(Y'_i=Z_i+\bar m_i(Y_{-i})-\bar m_i(X_{-i})\)；
其它坐标不变。条件 Gaussian 的方差不依赖条件坐标，
这里 \(\Phi\) 仅指一维标准正态分布函数；具体地
\(Z_i=\bar m_i(X_{-i})+Q_{ii}^{-1/2}\Phi^{-1}(U_i)\)，
故 \(Y'_i=\bar m_i(Y_{-i})+Q_{ii}^{-1/2}\Phi^{-1}(U_i)\)；
给定整个旧配对时它仍是目标在 \(Y_{-i}\) 的条件律。
第一边缘按自己的条件刷新后仍是 \(\mu\)。零测条件事件任取版本。
若 \(h=X-Y,\epsilon_i=X'_i-Z_i\)，则
\(h'=A_ih+e_i\epsilon_i\)，\(A_i^TQe_i=0\)，从而
\[
\|h'\|_Q^2=\|A_ih\|_Q^2+Q_{ii}\epsilon_i^2.
\tag{CR9}
\]
记第 \(n\) 次构造的期望成本为 \(C_n\)。第一边缘恒为 \(\mu\)，
条件一维最优成本恰给 (CR6)；(CR8)–(CR9) 因而给
\(C_{n+1}\le(1-\zeta)C_n+\mathcal R_Q(\mu)^2\)。
每个 \(C_n\) 都是**同一**两边缘的可行成本，故
\(W_{2,Q}(\mu,\beta)^2\le C_n\)；迭代并令 \(n\to\infty\)
给 (CR7) 的 EB。

取平移 Gaussian \(\mu=N(m_0+v,Q^{-1})\) 时，平移是最优运输，
条件均值差为 \((Qv)_i/Q_{ii}\)，于是
\[
W_{2,Q}(\mu,\beta)^2=v^TQv,
\qquad \mathcal R_Q(\mu)^2=v^TQDQv.
\tag{CR10}
\]
令 \(Q^{1/2}v\) 为 \(Q^{1/2}DQ^{1/2}\) 的最小特征向量便取等；
缩小 \(v\) 保比值并给任意目标球内的锐性。
EB 给残差的精确零集；收缩与 \(\zeta>0\) 给不变律唯一性。证毕。

## 来源、状态与可继续审查的门

二进制 [CM-M Theorem 6](../../../history/sources/次单调论文研究/MARKOV_PAPER_THEOREM_PACKAGE.md)
与 Gaussian 同包 Theorem 8 是来源版本；本页是独立写出的完整论证，
不继承该包的内部 PASS 或新颖性判断。两结论只在各自指定距离、
目标、律类和更新核上成立。其余该包的单 bit 精确模、随机原生提升、
外部先行性以及条件证书与同步 \(\Psi\) 的桥都没有由本页证明。
本库对 C129/C130 的状态限于 `derived-checked`：空白逆向检查重核了
二进制 (CR3)/(CR5) 的边缘与锐性、\(a_*=0,1\) 端点；另两路检查了
Gaussian 新独立随机数的双边缘保持、\(\mathcal P_2\) 有限性、
(CR8)–(CR10) 与局部取等。这个状态不转授给来源包的其他定理。
