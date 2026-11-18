# 用线性次正则与条件性角度估计替代 RLEB 整窗兼容

<a id="rfa-theorem"></a>
## C315-v1 · 普通 PPA 的严格弱化

**共同前提。** 固定 \(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，非空闭集 \(S\subset\operatorname{zer}F\)，\(\lambda>0\)、开集 \(U\)、\(R>0\)。写 \(d(z)=d(z,S)\)、\(U_R=\{x\in U:d(x)\le R\}\)。每个 \(x\in U_R\) 的允许输出集 \(\mathcal J(x)\subset J_{\lambda F}(x)\) 非空。对每个 \(y\in\mathcal J(x)\)，存在 \(p\in P_S(x)\) 使
\[
 \|2y-x-p\|\le\omega(d(x)),\qquad H(t)=\frac{t+\omega(t)}2 ,
\]
其中 \(\omega:[0,R]\to[0,\infty)\) 非减、在 \(0\) 处连续且 \(\omega(0)=0\)，且 \(\int_0^R\omega(t)\,dt/t<\infty\)。这是投稿主定理的最近零锚 RL 基线。C09 的同图块全对 RL 加最近零锚覆盖也足以给出这个前提。令 \(Y=\mathcal J(U_R)\)，\(r(y)=d(0,F(y))\) 始终对完整 \(F(y)\) 取下确界。由三角不等式，
\[
 \lambda r(y)\le\|x-y\|\le H(d(x))\le H(R).
 \tag{1}
\]
因此在整个 \(Y\) 上可定义标尺 \(a(y)=\inf\{t\in[0,R]:H(t)\ge\lambda r(y)\}\)。右端点 \(R\) 属于该集合。每个允许输入都满足 \(a(y)\le d(x)\)。当 \(H\) 连续时，\(a(y)=H^{-1}(\lambda r(y))\)。

**新条件。** 存在 \(m>0,\ q\in(0,1),\ \delta>0\)，使以下两条同时成立。

- 线性次正则（LMSR）。对每个 \(y\in Y\)，\(\lambda r(y)\ge m\,d(y)\)。
- 条件性角度估计（\(\mathcal K\)）。对每个 \(x\in U_R,\ y\in\mathcal J(x)\)，若 \(d(y)>q\,a(y)\)，则某个 \(p\in P_S(x)\) 满足
  \[
   2\langle y-p,x-y\rangle\ge -(1-\delta)\|x-y\|^2 .
   \tag{2}
  \]
  角度估计和 RL 可各用自己的最近点。无需零集凸、最近点唯一或所有图值有统一正角度。

**结论及证明。** 对每个允许输出有 (A)，统一因子为
\[
  \eta=\max\{q,(1+\delta m^2)^{-1/2}\}<1.
\]
若 \(d(y)\le q a(y)\)，由 (1) 立即得 \(d(y)\le q d(x)\)。其余图点用 (2) 展开 \(\|x-p\|^2\)，再用 LMSR 和 (1)，得到
\[
 d(x)^2 \ge \|y-p\|^2+\delta\|x-y\|^2
          \ge (1+\delta m^2)d(y)^2.
\]
零距离输入由 (1) 固定。这里的 \(\mathcal K\) 是图点在最近零锚下的内积估计，LMSR 将其中的正步长耗散换成距离的定量下降。

令 \(\Theta(t)=\sum_{j\ge0}H(\eta^jt)\)。Dini 条件保证 \(\sum_j H(\eta^jR)<\infty\)，故在 \([0,R]\) 上一致收敛，\(\Theta\) 非减、在 \(0\) 处连续且 \(\Theta(0)=0\)。由 \(\Theta(t)=H(t)+\Theta(\eta t)\) 和 (1)，每步满足
\[
 \|x-y\|+\Theta(d(y))\le\Theta(d(x)).
 \tag{3}
\]
若 \(x^0\in U_R\) 且 \(\Theta(d(x^0))<d(x^0,X\setminus U)\)，用 (3) 归纳控制已走有限前缀的长度，故下一点仍在 \(U\)。由 (A) 下一点仍满足 \(d\le R\)，可继续使用输入覆盖。所有允许轨道因此无限延拓，\(d(x^k)\le\eta^k d(x^0)\)，总长度不超过 \(\Theta(d(x^0))\)，尾长不超过 \(\Theta(d(x^k))\)。由 Cauchy 性、\(S\) 闭以及严格的留域余量，极限在 \(S\cap U\)。取 \(\mathcal J=J_{\lambda F}\) 时对应完整纤维，取图块时结论只量化其全部允许输出。

(3) 是 [C09 的 Dini 长度机制](general_modulus_dynamics.md#gm-dini-length)。本条改变的是产生 (A) 的正则性假设。有限长度仍是绝对步长可和，未要求输出相对的线性步界 (B)，也未调用 LMZ 的 KL 条件。若已有递推 \(E_{k+1}+D_k\le E_k+2\sigma\|x^{k+1}-x^k\|\)（固定 \(\sigma\ge0\)），(3) 允许把线性误差吸收到 \(E_k+2\sigma\Theta(d(x^k))\) 中。这条代数推论仍使用原有 Dini 条件。

<a id="rfa-kl"></a>
## 距离能量的 KL 形式

同一结论还允许一个满足 KL 不等式的步长势。设 \(E(x)=d(x)^2/2,\ T=R^2/2,\ M(u)=H(\sqrt{2u})\)，对 \(0<u\le T\) 令
\[
 G(u)=\frac{M(T)}{T}+\int_u^T\frac{M(v)}{v^2}\,dv,\qquad
 \phi(u)=\frac{1}{1-\eta^2}\int_0^u G(v)\,dv .
\]
\(G\) 连续非增且 \(G(u)\ge M(u)/u\)。换序积分给
\(\int_0^T G=M(T)+\int_0^T M(v)\,dv/v<\infty\)，末项就是两倍的 \(H\) 的 Dini 积分。因此 \(\phi\) 在零连续且 \(\phi(0)=0\)，在 \((0,T)\) 为 \(C^1\)、递增、凹。若 \(E(x)>0\)，由 \(E(y)\le\eta^2 E(x)\) 得
\[
 \phi(E(x))-\phi(E(y))
 \ge \frac{G(E(x))}{1-\eta^2}\bigl(E(x)-E(y)\bigr)
 \ge H(d(x))\ge\|x-y\| .
\]

对任意闭 \(S\)，在 \(x\notin S\) 处 \(\operatorname{dist}(0,\partial E(x))=d(x)\)，其中 \(\partial\) 是极限次微分。任一 Fréchet 次梯度须等于 \(x-p\)（每个 \(p\in P_S(x)\) 的光滑平方距离是接触的上界），所以每个极限次梯度的范数为 \(d(x)\)。非空性可沿 \([p,x)\) 逼近：每个内点的投影唯一等于 \(p\)（由三角等式），平方距离在唯一投影点可微（扰动点的任意最近点趋于 \(p\)，用上下二次估计夹逼）。故
\[
 \phi'(E(x))\operatorname{dist}(0,\partial E(x))
 \ \ge\ \frac{2H(d(x))}{(1-\eta^2)d(x)}\ \ge\ 1 .
\]
这给出 KL 势的实际望远镜差，且 LMSR 直接给出真实相对误差 \(d(y)\le\|x-y\|/m\)。这里仍由 RL、距离收缩及 Dini 构造 \(\phi\)，无需将 LMZ 的充分下降假设附加到 \(E\) 上。留域用 (3) 的原预算。

<a id="rfa-strict"></a>
## 整体蕴含与完整图严格例

**旧条件推出整个新条件。** 比较对象是普通 PPA 主稿 (c)–(d) 或 C09 (GM3)–(GM4) 中的真实残差界及其**整窗兼容**。具体地，旧条件在同一 \(Y\) 上有 \(\psi\) 非减、\(\psi(0)=0\)、评价窗 \(\bar t\ge H(R)/\lambda\)，满足 \(d(y)\le\psi(r(y))\) 及 \(\psi(H(t)/\lambda)\le\kappa t\) 对每个 \(0<t\le R\) 成立，某个 \(0<\kappa<1\)。对每个满足 \(H(t)\ge\lambda r(y)\) 的 \(t>0\)，由旧界得到 \(d(y)\le\kappa t\)。取下确界得 \(d(y)\le\kappa a(y)\)。由于 \(H(t)\ge t/2\)，取 \(t=\min\{R,2\lambda r(y)\}\) 可得 \(a(y)\le2\lambda r(y)\)，因而 \(d(y)\le2\kappa\lambda r(y)\)。\(r(y)=0\) 时由 \(\psi(0)=0\) 得同结论。取 \(q=\kappa,\ m=1/(2\kappa)\) 和 \(\delta\ge(\kappa^{-2}-1)/m^2\)，(2) 的触发条件从不出现。因此同一对象与同一尺度上的旧条件蕴含 \(\mathrm{LMSR}\land\mathcal K\)，且保留旧收缩因子 \(\eta=\kappa\) 和相同的初始留域预算。

**严格例。** 在 \(\mathbb R^2\) 取 \(\lambda=1\)，\(g(b)=\sqrt{\max\{b,0\}}\)，
\[
 F(a,b)=(g(b),3b),\quad S=\mathbb R\times\{0\},\quad
 J_F(u,t)=(u-g(t/4),t/4).
\]
这个公式由两个近端坐标方程反解，给出全域完整单值 resolvent。\(C=2J_F-I\) 为 \((u-2g(t/4),-t/2)\)，由 \(|g(b)-g(b')|\le\sqrt{|b-b'|}\)，全对 RL 可取 \(\omega(t)=7t+\sqrt t\)（事实上 \(t+\sqrt t\) 已足够），它满足 Dini。取 \(U=X\)、\(0<R\le1/1024\)，\(q=1/2,\delta=1,m=3\)。每个输出 \(y=(a,b)\) 有 \(d(y)=|b|\le R/4\)，且 \(r(y)=\sqrt{g(b)^2+9b^2}\ge3|b|\)。

在 \(b\le0\) 一侧，对输入 \(x=(a,4b)\) 取 \(p=(a,0)\)，就有 \(\langle y-p,x-y\rangle=3b^2\ge0\)。在 \(b>0\) 一侧，因 \(H(2b)=8b+\sqrt{b/2}\le\sqrt b\le r(y)\)，有 \(a(y)\ge2b\)，故角度条件未触发。负侧的条件确实会触发，例如足够小的 \(b<0\) 满足 \(H(2|b|)>3|b|\)。正侧的 \(2\langle y-p,x-y\rangle/\|x-y\|^2\to-2\)，因此把 (2) 强加到全部图点会排掉这个例子。实际距离收缩因子是 \(1/4\)。正侧步长除以输出距离为 \(\sqrt{b^{-1}+9}\)，无界，故 (3) 实际覆盖违反 (B) 的完整 PPA。

允许重新选择任何有效的旧 RL 模 \(\widetilde\omega\)。正侧输入 \((0,t)\) 和其最近零锚 \((0,0)\) 强制 \(\widetilde\omega(t)\ge\sqrt t\)，所以 \(\widetilde H(t)/t\to\infty\)。给定足够小的 \(t>0\)，取负侧输出 \(b=-\widetilde H(t)/3\)，其近端输入法向坐标 \(4b\to0\)，确属同一整窗。此时 \(r(y)=\widetilde H(t)\)、\(d(y)=\widetilde H(t)/3\)。若旧 EB 和整窗兼容同时成立，则
\[
 \frac{\widetilde H(t)}3\le\psi(\widetilde H(t))\le\kappa t,
\]
矛盾。取 \(\bar x=(0,0)\) 时，即使任意缩小含 \(\bar x\) 的开邻域或作含零的值域截断，这两个分支测试仍可在足够小的尺度进行。固定原来的标量兼容条件也可见严格性。取 \(\psi_0(s)=s^2\)，因 \(H(t)=4t+\sqrt t/2\le\sqrt{t/2}\) 对上述 \(R\) 成立，有 \(\psi_0(H(t))\le t/2\)。负侧却有 \(\psi_0(r(y))=9b^2<|b|\)（非零小 \(b\)）。在同一标量数据下，\(F_0(a,b)=(0,\operatorname{sgn}(b)\sqrt{|b|})\) 具有全域完整单值近端，其全对反射模可取 \(t\)，且误差界取等。因此固定模的旧类也非空。正侧决定统一 RL 模，负侧决定小残差所能达到的输出距离。旧标量整窗把两侧最坏尺度配在一起，(2) 在小残差一侧改用实际图点的内积。

<a id="rfa-boundary"></a>
## 范围与反向检验

- **单独的 GMSR。** 若允许任意误差界模且没有整窗兼容，LMSR 本身就是线性模的 GMSR，严格例 \(\mathrm{LMSR}\land\mathcal K\land\neg\mathrm{GMSR}\) 在该定义下不可能。反向也失败。\(F(y)=y^3,\lambda=1,S=\{0\}\) 在完整图上有 RL 模 \(\omega(t)=t\) 和 \(\psi(s)=s^{1/3}\) 的真实 EB，而 \(r(y)/d(y)=y^2\to0\)。每步角度非负，故该例也检验删去 LMSR，距离比 \(1/(1+y^2)\to1\)。
- **删去 \(\mathcal K\)。** 取 \(F_-(a,b)=(g(b)+3(-b)_+,3b_+)\)。它有相同零集、完整真实残差 \(r(a,b)=\sqrt{b_++9b^2}\) 和相同的全对 RL 模 \(7t+\sqrt t\)。正侧近端同严格例，负侧为 \(J_{F_-}(u,t)=(u+3t,t)\)。其反射映射的横坐标为 \(u-2g(t/4)-6(-t)_+\)，纵坐标在正负侧分别为 \(-t/2,t\)。映射 \((u,t)\mapsto(u,t\mathbf1_{t\le0}-(t/2)\mathbf1_{t>0})\) 为 \(1\)-Lipschitz，额外负侧横移为 \(6\)-Lipschitz，平方根项至多 \(\sqrt{\|\Delta x\|}\)。同一负侧轨道保持到 \(S\) 的距离，且总长度发散。两个完整图的残差场和共同 RL 模一致，角度条件能区分它们。
- **角度条件有独立约束。** 若在严格例中只把 \(b<0\) 时的 \(g(b)\) 改为 \(4(-b)\)，则完整近端仍将法向距离缩小为 \(1/4\)，全对 RL 仍有 Dini 模。任一有效的 \(\omega\) 仍满足 \(\omega(t)\ge\sqrt t\)。负侧 \(r(y)=5|b|\)，故 \(a(y)\le100b^2\)，角度测试在足够小的负 \(b\) 上必触发。其唯一最近输入锚给 \(2\langle y-p,x-y\rangle=-26b^2\)、\(\|x-y\|^2=25b^2\)，所以任何 \(\delta>0\) 都不能通过 (2)。这验证了该条件比单凭 (A) 和有限长度更有约束。
- **删去 RL。** 取 \(S=\{0\}\)、\(\lambda=1\)、\(Q\) 为四分之一周旋转。令 \(T(x)=\chi(\|x\|)Qx\)，其中连续 \(\chi\in[0,1]\) 在 \([0,R/4]\) 上为 1，在 \([R/2,\infty)\) 上为 0。定义 \(F(y)=\{x-y:T(x)=y\}\)，故完整 \(J_F=T\) 且 \(\operatorname{zer}F=S\)。对非零输出，每个原像与 \(y\) 正交且 \(\|y\|\le\|x\|\le R/2\)，故 \(\sqrt2\,d(y)\le r(y)\le R/\sqrt2\)。声明 \(\omega(t)=t\)，有 \(a(y)=r(y)\)、残差仍全在窗内，取 \(q=3/4\) 则 (2) 未触发。内球的非零轨道是四周期。
- [C310](../../CLAIMS.md#c310) 的最大单调幂例甚至符合旧整窗条件（取线性 \(\omega\) 和 \(\psi(s)=s^{1/\alpha}\)，缩窗即可），已排除从旧条件到原始 (B) 的普遍蕴含。新定理的严格弱化针对 C09 的旧整窗兼容。它与 [C285 的线性联合包络](rleb_sharp_linear_frontier.md#rsl-envelope) 有共同的一步欧氏恒等式。此处完整反例的 \(\omega(t)/t\to\infty\)，失效的是统一小尺度模，不是线性常数选得不够好。
- **Status** `derived-checked`，普通 PPA 的同图、同窗比较。**Truth** 为上述严格包含和有限长度。**Mechanism** 为残差标尺与最近零锚内积的逐图点配合。**Value** 为取消统一整窗的误差界配对。**Ambition** 为先闭合普通 PPA。一般固定核 GPPA 的物理角度仍需另证。若直接删除 Dini，[C10 的对数模型](general_modulus_dynamics.md#gm-log-object) 在非 Dini 参数下已有相容真实残差界，因此也有本条两项新条件，却发生无限长度。任何取代 Dini 的 KL 条件都须提供额外的耗散信息。外部文献新颖性未判定。原有 [C277 的弱 Minty 分支](unified_ppa_joint_certificates.md) 已提供 (2) 的耗散恒等式。这里的独立贡献是以完整残差标尺判定哪些边需要该估计，证明整个新条件由旧整窗兼容推出，并给出重新选择 RL 模也无法通过旧兼容的严格例。
