# 原 PPA 的回返缺口、完整真残差及循环条件的归约

**状态：C346-v1，`derived-checked`。** 有限路径上的两项估计已由另一研究席和主代理分别重构；它们是阶段性关系，不是本轮所求共同结构。一般最近输入零锚下的方向恢复、两条等价及结构新意仍未解决。

固定有限维欧氏空间、步长 \(\lambda>0\)、非空闭集 \(S\subseteq F^{-1}(0)\)。记 \(d(a)=\operatorname{dist}(a,S)\)，\(r_F(a)=\inf_{v\in F(a)}\|v\|\)。允许的有向边 \((a,b)\in K\) 满足 \(a-b\in\lambda F(b)\)。下面只估计已存在的有限路径，因而无需假设整个输入域有根或闭合。若要对无限原轨道作结论，须另证其能持续选择原根并保持有界。

<a id="loop-reduction"></a>
## 连续补偿耗散推出任意周期的统一估计

固定 \(R,\ell,\tau>0\) 和有限非负连续函数 \(h:[0,R]\to[0,\infty)\)，\(h(0)=0\)。受检边两端的目标距离落在 \([0,R]\)，且对其每个零锚 \(p\in S\) 有

\[
 \|b-p\|+h(d(b))+
 \tau\frac{\|a-b\|^2}{\ell+\|a-p\|+\|b-p\|}
 \le \|a-p\|+h(d(a)).
 \tag{1}
\]

令 \(Y_0\subseteq\{y:d(y)\le R\}\) 为有界的允许输出集。在这个集合上要求完整真残差有以下性质。若 \(y_j\in Y_0\) 且 \(r_F(y_j)\to0\)，则 \(d(y_j)\to0\)。等价地，取

\[
 b_0(s)=\sup\bigl(\{d(y):y\in Y_0,\ r_F(y)\le s\}\cup\{0\}\bigr),
\]

就有 \(b_0(s)\to0\) 当 \(s\downarrow0\)，以及 \(b_0(0)=0\)。有界性只用于从 C341 的有界序列表述取得这一统一模。若预先给出了有限且零连续的同类统一上界模，\(Y_0\) 本身可以无界，但仍保留 \(d(y)\le R\) 的距离窗。

任取 \(\delta_*>0\)。对任意整数 \(m\ge1\) 和点列

\[
 z_0=z_m+e,\qquad z_m\in Y_0,\qquad
 (z_{i-1},z_i)\in K\quad(1\le i\le m),\qquad
 \delta=\|e\|\le\delta_* ,
\]

有一个与 \(m\) 无关的非减函数 \(\Xi\)，使

\[
  \inf_{p\in S}\max_{1\le i\le m}\|z_i-p\|\le\Xi(\delta),
  \qquad \Xi(0)=0,\qquad \lim_{\delta\downarrow0}\Xi(\delta)=0 .
  \tag{2}
\]

**证明。**  一开始就取 \(p\in P_S(z_m)\)，并在整条路径固定它。记 \(V_p(z)=\|z-p\|+h(d(z))\)。由 (1) 及 \(h\ge0\)，所有端点满足

\[
 \|z_i-p\|\le V_p(z_i)\le V_p(z_0)
 \le R+\delta_*+\max_{[0,R]}h=:C .
\]

这给全部平方项同一个分母上界 \(\ell+2C\)，与路径长度、锚的位置及域是否闭合无关。令

\[
 \sigma_h(u)=\max_{s,t\in[0,R],\ |s-t|\le u}|h(s)-h(t)|.
\]

\(h\) 在该紧区间一致连续，因此 \(\sigma_h(u)\to0\)。对 (1) 求和，用 \(d\) 的 1-Lipschitz 性可得

\[
 \sum_{i=1}^m\|z_i-z_{i-1}\|^2
 \le \frac{\ell+2C}{\tau}
        [V_p(z_0)-V_p(z_m)]
 \le \frac{\ell+2C}{\tau}[\delta+\sigma_h(\delta)].
 \tag{3}
\]

最后一条实际图边给

\[
 r_F(z_m)\le \frac{\|z_m-z_{m-1}\|}{\lambda}
 \le w(\delta):=\frac1\lambda
 \sqrt{\frac{\ell+2C}{\tau}[\delta+\sigma_h(\delta)]}.
\]

\(m=1\) 时实际边就是从 \(z_m+e\) 到 \(z_m\)。故 \(d(z_m)\le b_0(w(\delta))=:b(\delta)\)。写 \(\widehat h(t)=\max_{0\le s\le t}h(s)\)。再次使用同一个 \(p\in P_S(z_m)\) 以及逐边的 \(V_p\) 单调性，得到

\[
 \max_{0\le i\le m}\|z_i-p\|
 \le d(z_m)+\delta+h(d(z_0))
 \le b(\delta)+\delta+\widehat h\bigl(\min\{R,b(\delta)+\delta\}\bigr).
 \tag{4}
\]

取 (4) 右端为 \(\Xi\) 即证。全过程只在最后一个输出使用真残差。用于 (3) 的一致连续性是在所有受检接缝距离所在的正尺度区间上要求的，单有零处连续不保证这个估计。

若每个受检输出 \(y\) 在完整纤维中的小范数近极小值可以作为允许边 \((y+\lambda v,y)\)，那么 (2) 也能恢复上述定性真残差条件。给定 \(r_F(y_j)\to0\)，分别取这些允许边使 \(\|v_j\|\le r_F(y_j)+o(1)\)。在 (2) 令 \(m=1,e_j=\lambda v_j\)，遂有 \(d(y_j)\to0\)。正点处任意指定模的逐点恢复还需核右极限或取到性。这个方向在未覆盖完整纤维近极小值的图块上只识别图块自己的残差。

<a id="loop-imports"></a>
## 对原 RLEB 与共次单调的含义

原 RLEB 给定 \(B(t)=(t+\omega(t))/2\)、\(0<\kappa<1\) 及 \(\Theta(R)=\sum_{j\ge0}B(\kappa^jR)<\infty\)。用于条件 (1) 的连续补偿可以完全从原有 \([0,R]\) 上的数值构造。定义

\[
 \overline B(t)=\frac{1}{\log2}\int_1^2 B(\min\{R,tu\})\,\frac{du}{u},
 \qquad
 h(t)=2\sum_{j\ge0}\overline B(\kappa^jt).
 \tag{5}
\]

有 \(B(t)\le\overline B(t)\le B(\min\{R,2t\})\)。对正的 \(t\)，将积分写成从 \(t\) 到 \(2t\) 的 \(B(\min\{R,s\})/s\) 的积分，局部可积性给出连续性。零处连续性由上述上界得到。取整数 \(k_0\) 使 \(2\kappa^{k_0}\le1\)，则

\[
 \sum_{j\ge0}\overline B(\kappa^j R)\le k_0B(R)+\Theta(R)<\infty.
\]

故 (5) 在原闭窗上一致收敛，\(h\) 连续非减，且 \(h(t)-h(\kappa t)=2\overline B(t)\ge2B(t)\)。积分中的截断从未要求在 \(R\) 外验证反射不等式。

对允许边 \((a,b)\)，原最近输入零锚给 \(\|a-b\|\le B(d(a))\)。完整真残差误差界、评价帽 \(B(R)/\lambda\le\bar t\) 及原兼容给 \(d(b)\le\kappa d(a)\)。对任意 \(p\in S\)，有 \(\|b-p\|-\|a-p\|\le\|a-b\|\)，且 \(\|a-b\|\le\|a-p\|+\|b-p\|\)，故 (1) 在 \(\tau=1\) 成立。正则性在输出集由 \(\psi(0+)=0\) 给出。原始留域仍采用 \(\Theta\) 与原严格初值预算，(5) 只用于估计已经处在工作窗的循环。这证明此测试行的 (2) 是原一步收缩及连续补偿的推论。

若每个允许原图点 \(v=(a-b)/\lambda\in F(b)\) 与所有零锚满足 \(\langle b-p,v\rangle\ge-\rho\|v\|^2\)，且 \(\tau=1-2\rho/\lambda>0\)，则

\[
 \|a-p\|^2-\|b-p\|^2\ge\tau\|a-b\|^2.
\]

两锚距之和为正时以该和为分母；两者皆零时边驻定。两种情形均推出 (1)，可取 \(h=0\) 及任意 \(\ell>0\)。若 \(0<\tau<1\)，所用耗散系数为 \(\tau\)。C341 原定义的系数是 1，且对可能无界的全体 \(S\) 测试；不能从上述平方估计把该系数直接改成 1。

[C341 共同条件与 (5a)](compensated_anchor_convergence.md#ca-definition) 已含归一化平方耗散和完整残差的有界序列识别。本推导所加的是接缝两端的连续补偿振幅，从而能统一估计任意有限周期。它给出了两条测试行在此定性循环条件上的共同来源。它没有给出仅凭循环条件反向恢复一般最近零锚反射不等式的证明。

<a id="return-residual"></a>
## 固定输出的最小回返缺口与完整真残差

对同一允许原图边关系 \(K\)，定义

\[
 I_K(y)=\{u:(u,y)\in K\},\qquad
 Q_K(y)=\{z:\text{有一条从 }y\text{ 到 }z\text{ 的有限 }K\text{ 路径}\},
 \qquad
 c_K(y)=\operatorname{dist}(I_K(y),Q_K(y)).
 \tag{6}
\]

零步路径使 \(y\in Q_K(y)\)，空输入集给 \(c_K(y)=+\infty\)。式 (6) 就是固定输出 \(y\) 的有限循环只在一处允许外力时，该处所需输入位移范数的下确界。对任一从 \(y\) 到 \(z\) 的允许路径和 \(u\in I_K(y)\)，所需位移为 \(u-z\)，且每个这样的循环有这项表示。

设允许边对全体 \(p\in S\) 满足平方耗散

\[
 \|a-p\|^2-\|b-p\|^2\ge\beta\|a-b\|^2,\qquad \beta>0 .
 \tag{7}
\]

则对任一具有允许输入的 \(y\)，有

\[
 \sqrt{d(y)^2+\beta\lambda^2r_F(y)^2}-d(y)\le c_K(y).
 \tag{8}
\]

确实，固定 \(p\in P_S(y)\)。对每个 \(z\in Q_K(y)\)，(7) 在有限路径上给 \(\|z-p\|\le d(y)\)。对每个 \(u\in I_K(y)\)，该步的图值属于 \(F(y)\)，因而

\[
 \beta\lambda^2r_F(y)^2\le\beta\|u-y\|^2
 \le\|u-p\|^2-d(y)^2
 \le\bigl(d(y)+\|u-z\|\bigr)^2-d(y)^2 .
\]

先开方，再对 \(u,z\) 取下确界即得 (8)，无需任一最小值达到。若允许输入中存在一列 \(u_j=y+\lambda v_j\)，其中 \(v_j\in F(y)\) 且 \(\|v_j\|\to r_F(y)\)，零步路径另给

\[
 c_K(y)\le\lambda r_F(y).
 \tag{9}
\]

在 \(d(y)\le R\) 且 \(c_K(y)<\infty\) 的输出窗，(8) 给 \(r_F(y)\le\sqrt{2Rc_K(y)+c_K(y)^2}/(\lambda\sqrt\beta)\)。因此若全纤维满足 \(d(y)\le\psi(r_F(y))\)，可用右侧代入非减的 \(\psi\)，限于该上界也在 \(\psi\) 的评价帽内。若 \(d(y)\le\chi(c_K(y))\) 且 (9) 成立，则可代入 \(\lambda r_F(y)\) 得到相应完整真残差界。在线性情形，\(d(y)\le K_0 r_F(y)\) 与 \(0<K_0<\infty\) 直接使

\[
 \bigl(\sqrt{1+\beta\lambda^2/K_0^2}-1\bigr)d(y)\le c_K(y).
 \tag{10}
\]

(8) 对共次单调的 \(\beta=1-2\rho/\lambda>0\) 成立，当中没有先用正则性或点收敛。(9) 准确标明从允许图回复完整纤维所需的条件。对原最近输入零锚的一般反射模，只要允许内链的目标距离非增，就有 \(\lambda r_F(y)\le B(d(u))\le B(\min\{R,d(y)+\|u-z\|\})\)，其中前一不等式来自单步反射且 \(d(u)\le R\)。取下确界时一般只能使用右侧函数的右极限。该式的 \(d(y)\) 在回返缺口为零时仍保留，故不能由它推出 (8) 的零处识别；而在原 RLEB 行，内链距离非增仍由原兼容给出。这个固定输出的转接已有 (8)–(10) 的独立证明，一般最近零锚下与单调性的反向等价仍未得到。


<a id="loop-open"></a>
## 验收范围与首个缺口

式 (8)–(10) 的方向到正则转接先于轨道收敛，并且保持完整真残差，因而可独立复用。它的方向前件是所有零锚上的平方耗散；不能从原最近输入零锚的非线性反射界自动得到这个前件。反过来，回返缺口只记录能否接近闭返，没有给出恢复一般单调或次单调的证明。

式 (2) 在两个基准上的导入则完全由连续补偿耗散推出。原 RLEB 行的参数作用和承重下降已经在构造 (5) 之前由原半和界及误差模相容得到；把这之后的循环误差界命名为共同结构，不会增加原始两侧的共同推导。上述结论不证明所有回返方法不可能，只排除把此处已经推得的循环条件直接认领为当前任务的完成。

本文件不宣称公开首创。近邻文献中的循环和 gap vector 是另一套已建立的对象；例如 Alwadani–Bauschke–Wang 的 [Attouch–Théra Duality, Generalized Cycles, and Gap Vectors](https://doi.org/10.1137/21M1392085)（SIAM J. Optim. 31(3), 1926–1946, 2021）研究近端映射复合的循环、gap vector 与对偶关系。本轮只核到原作者摘要所陈述的范围，不将其作为 (1)–(10) 的证明导入，也不据此裁定 (8) 的先行性。
