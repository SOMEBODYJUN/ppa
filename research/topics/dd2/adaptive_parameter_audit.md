# DD2 方向自适应参数审计

本文把变松弛证明中三个容易混用的量分开。方向曲率由 \(V\) 和实际图值决定，锚缺陷由输入与最近零锚的内积决定，
而 \(\alpha\) 是算法在观察到这些量以后选择的松弛参数。三者的可计算性和量词不同。
本文使用方向松弛中的记号
\[
 z^+=z-\alpha q,\qquad \widehat z=z-q,\qquad
 t=d(z,S),\quad a=d(\widehat z,S),\quad u=d(z^+,S),\quad s=\|q\|.
\]
设 \(V=V^*\succeq\eta I\), \(\eta>0\)，并令
\[
 \rho_V(q)=\frac{\langle q,Vq\rangle}{s^2}\quad(s>0),\qquad
 \rho_V(0)=\eta.
\]
允许边的最近锚条件写成
\[
 \langle q,z-p\rangle\ge \langle q,Vq\rangle-D(t),\qquad p\in P_S(z).
 \tag{A1}
\]
若只知道一个模型下界 \(D(t)\)，下面的 \(D(t)\) 指该上界。若 \(p\) 和 \(V\) 可计算，则可以逐边用实际缺陷
\[
 d_{\rm e}(z,q,p)=\bigl[\langle q,Vq\rangle-\langle q,z-p\rangle\bigr]_+
\]
替换它。

## 1. 三个参数的可认证分离

令 \(\psi\) 为输出位移误差界，\(a\le\psi(s)\)，并令
\[
 \chi=(I+\psi)^{-1},\qquad
 \omega_D(t)=\frac{D(t)}{\chi(t)^2}.
\]
由 \(t\le a+s\le \psi(s)+s\) 得 \(s\ge\chi(t)\)。取任何可证明的方向下界
\[
 \underline\beta_k\le\rho_V(q_k).
\]
将 \(\gamma_k=2\underline\beta_k-\alpha_k\) 代入平方展开得到
\[
 u_k^2\le t_k^2+2\alpha_kD(t_k)-\alpha_k\gamma_k s_k^2
 \le t_k^2-\alpha_k\mu_k s_k^2,
 \qquad
 \mu_k:=\gamma_k-2\omega_D(t_k).
 \tag{A2}
\]
这里第二个不等式只使用 \(s_k\ge\chi(t_k)\)。因此，给定一个希望保留的严格余量 \(\mu_{\rm req,k}\ge0\)，逐边可认证的最小方向系数是
\[
 \boxed{
 \beta_{\min,k}=\frac{\alpha_k}{2}+\omega_D(t_k)+\frac{\mu_{\rm req,k}}2 .
 }
 \tag{A3}
\]
需要 \(\underline\beta_k\ge\beta_{\min,k}\)。只要求严格下降时 \(\mu_{\rm req,k}=0\)，但不等号必须改为严格不等号。反解得到给定方向下界允许的最大松弛
\[
 \boxed{
 \alpha_k<2\bigl(\underline\beta_k-\omega_D(t_k)\bigr)
 }
 \tag{A4}
\]
或在预留余量时 \(\alpha_k\le2(\underline\beta_k-\omega_D)-\mu_{\rm req,k}\)。

(A3) 中的三项具有不同的信息来源。

| 量 | 定义 | 能否由单条边直接观察 |
| --- | --- | --- |
| 方向项 | \(\rho_V(q_k)=\langle q_k,Vq_k\rangle/s_k^2\) | 已知 \(V,q_k\) 且 \(s_k>0\) 时可以；只有 \(V\succeq\eta I\) 时只能认证 \(\eta\) |
| 吸收项 | \(\omega_D(t_k)=D(t_k)/\chi(t_k)^2\) | 需要 \(t_k\)、输出模和缺陷上界；若最近投影未知，只能使用模型上界 |
| 松弛项 | \(\alpha_k\) | 算法给定。它不能反过来证明方向项或吸收项 |

若 \(p_k\) 是已计算的精确最近锚，可以用 \(d_{\rm e,k}/\chi(t_k)^2\) 代替 \(\omega_D(t_k)\)。这只给当前边的证书，不能自动给所有允许边的统一函数 \(D\)。若 \(p_k\) 只是近似最近点，则 (A1) 必须对逼近列取 \(\liminf\)，而 \(d_{\rm e,k}\) 仍不能被称作完整缺陷上界。若 \(t_k\) 或 \(\chi(t_k)\) 不可观察，(A3) 是模型可认证阈值，不是一个可执行的逐边数值。

**证明。** 展开同一锚的平方距离并使用 (A1)，有
\[
\begin{aligned}
 u_k^2
 &=\|z_k-p_k-\alpha_kq_k\|^2\\
 &\le t_k^2-2\alpha_k\langle q_k,Vq_k\rangle
      +2\alpha_kD(t_k)+\alpha_k^2s_k^2\\
 &\le t_k^2+2\alpha_kD(t_k)-\alpha_k(2\underline\beta_k-\alpha_k)s_k^2.
\end{aligned}
\]
再用 \(s_k\ge\chi(t_k)\) 即得 (A2)，随后解出 \(\underline\beta_k\) 和 \(\alpha_k\) 得 (A3)–(A4)。

这也说明了一个常见误读。条件 \(\alpha_k\le2\underline\beta_k\) 只支付方向余量，不能支付缺陷吸收。即使 \(\alpha_k<2\underline\beta_k\)，若 \(2\omega_D(t_k)\ge2\underline\beta_k-\alpha_k\)，(A2) 没有正的净耗散。

## 2. Hölder 近上限松弛和同时临界常数

令
\[
 \psi(s)=Ks^\vartheta,\qquad \frac12<\vartheta<1,
\]
则当 \(t\downarrow0\) 时
\[
 \chi(t)\sim K^{-1/\vartheta}t^{1/\vartheta}.
 \tag{A5}
\]
考虑方向余量在零点衰减的规则
\[
 \gamma(t)\ge c_\gamma\chi(t)^\kappa,\qquad c_\gamma>0,\quad\kappa>0,
 \tag{A6}
\]
以及幂次缺陷 \(D(t)\le Ct^p\)。当
\[
 p=\frac{2+\kappa}{\vartheta}
 \tag{A7}
\]
时，(A5) 给出
\[
\begin{aligned}
 \mu(t)
 &\ge c_\gamma\chi(t)^\kappa-\frac{2Ct^p}{\chi(t)^2}\\
 &=\left(c_\gamma K^{-\kappa/\vartheta}-2C K^{2/\vartheta}\right)t^{\kappa/\vartheta}(1+o(1)).
\end{aligned}
 \tag{A8}
\]
所以严格正的同阶余量的锐常数门是
\[
 \boxed{
 2C<c_\gamma K^{-(2+\kappa)/\vartheta}.
 }
 \tag{A9}
\]
当 \(p>(2+\kappa)/\vartheta\) 时缺陷是高阶项。当 \(p<(2+\kappa)/\vartheta\)，或在 (A7) 下反向违反 (A9) 时，(A2) 不能给出统一正耗散。等号时首项完全抵消，必须再给一个高阶正余量，不能把等号写成定理假设。

(A9) 包含固定方向间隙的已知门。令 \(\kappa=0\) 且 \(c_\gamma=g_0\)，便得到
\[
 2C<g_0K^{-2/\vartheta}.
\]
它也修正了把 \(\alpha\to2\beta\) 和缺陷门分别检查的做法。两项同时在临界尺度时，比较的是同一个常数 \(c_\gamma\) 和 \(2C K^{(2+\kappa)/\vartheta}\)。

在严格门 (A9) 下，距离递推满足
\[
 t_k-t_{k+1}\gtrsim t_k^{1+\nu},\qquad
 \nu=\frac{2+\kappa}{\vartheta}-2.
 \tag{A10}
\]
在输出模达到的 sharp 子类（包括下文见证）中
\(s_k\asymp\chi(t_k)\asymp t_k^{1/\vartheta}\)，于是
\[
 \alpha_ks_k\asymp k^{-1/(2+\kappa-2\vartheta)}.
 \tag{A11}
\]
该 sharp 子类的位移总和有限当且仅当
\[
 \boxed{\kappa<2\vartheta-1.}
 \tag{A12}
\]
在 \(\kappa=2\vartheta-1\) 时，(A11) 是调和级数，距离仍可趋零但总长度可以发散。这个端点与常数门 (A9) 是两个独立的临界性。先满足 (A9) 只能保证正距离上的耗散，不能把 (A12) 的严格不等式改成等号。

### 同时临界的完整见证

方向松弛正文的平面单值构造给出 (A9) 等号的闭合见证。取 \(V=\beta I\)，令 \(s=s(r)\) 为构造中的位移范数，并在小窗把径向系数写成
\[
 b(r)=\beta-\frac{c_\gamma}{2}s(r)^\kappa,\qquad
 \alpha(r)=2\beta-c_\gamma s(r)^\kappa.
\]
令 \(q\) 的径向分量满足 \(\langle q,z\rangle=b(r)s(r)^2\)，切向分量补足 \(\|q\|=s(r)\)。于是
\[
 2\langle q,z\rangle=\alpha(r)s(r)^2,
\]
从而实际更新 \(z^+=z-\alpha q\) 精确保半径。相同构造的锚缺陷满足
\[
 2D=s(r)^{2+\kappa},
\]
将 \(c_\gamma=1\) 归一化后正好是 (A9) 的等号。它的 \(I-q\) 是全域连续单值同胚，反向图 \(F=(I-q)^{-1}-I\) 给出完整图和唯一近端分支。因此等号下存在真实轨道没有净半径下降，不能把等号吸收到“严格小窗”中。一般 \(c_\gamma\) 只需把 \(s^\kappa\) 换成 \(c_\gamma s^\kappa\)，缺陷同样按 \(2D=c_\gamma s^{2+\kappa}\) 缩放。

## 3. 最近锚、全锚和零聚点必须分开

### 3.1 最近锚只给标量距离结论

若每条允许边只存在一个最近锚 \(p_k\)，并满足 (A1)，且输出模、覆盖和留域条件在同一窗口成立，则 (A2) 是标量距离估计。若存在正函数 \(\mu(t)\) 使
\[
 \frac{2t}{\mu(t)\chi(t)}
\]
有可积的非增上包络，得到
\[
 \alpha_ks_k\le\Theta(t_k)-\Theta(t_{k+1}),\qquad
 \Theta(t)=\int_0^t\overline h(v)\,dv,\quad
 \overline h\ge \frac{2v}{\mu(v)\chi(v)}.
 \tag{A13}
\]
有限前缀预算给出留域和有限长度。若另有
\[
 \sum_k\alpha_k=\infty,\qquad
 \inf_{t\in[c,R]}\mu(t)>0\quad(0<c\le R),
 \tag{A14}
\]
则 \(t_k\to0\)。证明是反设 \(t_k\downarrow t_*>0\)。此时 \(s_k\ge\chi(t_*)\) 且 \(\mu(t_k)\) 有正下界，(A2) 求和与 \(\sum\alpha_k=\infty\) 矛盾。

(A13)–(A14) 不给固定锚的 Fejér 性。最近锚可能随步切换，切向分量可以累积而 \(t_k\to0\)。例如方向松弛正文的连续单值图
\[
 G(u,v)=(-v^2,v^3),\qquad S=\mathbb R\times\{0\},\qquad
 F=I-(I+G)^{-1}
\]
满足最近锚条件。其轨道满足
\[
 v_k=v_{k+1}+v_{k+1}^3,\qquad
 u_{k+1}-u_k=v_{k+1}^2,\qquad
 v_k^2\sim(2k)^{-1}.
\]
因此 \(d(z_k,S)\to0\)，但 \(u_k\sim\tfrac12\log k\to\infty\)。最近锚结论本身没有零聚点，更不能推出点收敛。

### 3.2 全锚给准 Fejér，参数和误差另有量词

若对每个允许步和每个 \(w\in S\) 都有
\[
 \langle q_k,z_k-w\rangle\ge\beta_ks_k^2+L_w(z_k)-e_k,\qquad L_w\ge0,\ e_k\ge0,
 \tag{A15}
\]
则
\[
 \|z_{k+1}-w\|^2\le\|z_k-w\|^2-\delta_ks_k^2
 -2\alpha_kL_w(z_k)+2\alpha_ke_k,\qquad
 \delta_k=\alpha_k(2\beta_k-\alpha_k).
 \tag{A16}
\]
若 \(2\alpha_ke_k\le(1-\tau)\delta_ks_k^2\) 对某 \(\tau>0\)，得到 Fejér 下降并控制 \(\sum\delta_ks_k^2\)。若只知道 \(\sum\alpha_ke_k<\infty\)，得到准 Fejér 和有界性，但不能把 \(e_k\) 的可和性改写成每步零误差。

全锚条件和最近锚条件的零识别仍需独立检查。若最近锚部分已经给出 \(t_k\to0\)，且 \(S\) 弱序列闭，则任意弱聚点属于 \(S\)。在 (A15) 和可和误差下，所有固定锚距离有极限。若所有弱聚点属于 \(S\)，Opial 论证给唯一弱极限。有限维时弱、强相同，闭 \(S\) 和有界性给强收敛。若 \(S=\operatorname{zer}F\)，也可改用 \(s_k\to0\)、\(\widehat z_k-z_k=-q_k\to0\) 与 \(F\) 在零处 demiclosed 来识别零点。

近上限规则中 \(\delta_k\to0\)，所以不能使用 \(\liminf\delta_k>0\) 的残差论证。零识别来自 (A14) 和吸收门，先得到 \(t_k\to0\)，再由锚定给 \(s_k\le M t_k\)，从而 \(q_k\to0\)。只有在全锚 (A15) 也成立时，才能再调用准 Fejér 或 Opial 结论。把最近锚的标量结论写成全锚结论会增加未证明的量词。

### 3.3 “\(\sum\alpha_k=\infty\)”单独不够

取 \(F(z)=z\)、\(S=\{0\}\)、\(V=I\)、\(D=0\)，并令
\[
 \alpha_k=2-2^{-k-2}.
\]
每步都有 \(\alpha_k<2\beta_k\) 且 \(\sum_k\alpha_k=\infty\)，但
\[
 z_{k+1}=(-1+2^{-k-2})z_k,\qquad
 |z_k|=|z_0|\prod_{j<k}(1-2^{-j-2})\longrightarrow c|z_0|>0.
\]
方向余量 \(\gamma_k=2^{-k-2}\) 衰减过快，距离不趋零。若 \(\alpha_k=2\)，则 \(z_{k+1}=-z_k\) 直接说明非严格门不能给下降。因而零聚点识别必须使用 (A14)、统一严格包络或别的累积耗散条件，不能只记录 \(\alpha_k\) 的发散和逐步不等号。

## 4. 实施时的检查顺序

对每个候选边先记录 \(q_k,s_k,t_k\) 及锚的来源，再分别计算或上界
\[
 \underline\beta_k,\qquad \overline\omega_k=\overline D(t_k)/\chi(t_k)^2,\qquad \alpha_k.
\]
只有在
\[
 2\underline\beta_k-\alpha_k-2\overline\omega_k>0
 \tag{A17}
\]
时才登记为有净耗散的边。需要长度时，再检查 \(2t/(\mu\chi)\) 的统一可积包络。需要全锚点收敛时，再逐个 \(w\in S\) 验证 (A15) 和误差尾。需要零聚点识别时，单独注明采用闭目标、有限维有界性、弱闭性或 demiclosedness 中的哪一种。

这套顺序保留了三个独立的门。方向下界不能代替缺陷吸收，逐边严格下降不能代替累计识别，全锚准 Fejér 也不能由最近锚存在性推出。

