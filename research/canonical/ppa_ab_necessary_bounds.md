# 普通 PPA 的 A 与 B：必要条件、锐常数与长度上界

<a id="ab-scope"></a>
## 1. 对象和量词

取欧氏空间 \(X=\mathbb R^n\)，关系 \(F:X\rightrightarrows X\)，步长 \(\lambda>0\)，非空闭集 \(S\subseteq\operatorname{zer}F\)，开集 \(U\subseteq X\)，以及 \(R>0\)。记
\[
d(z)=\operatorname{dist}(z,S),\quad U_R=\{x\in U:d(x)\le R\},\quad
J_{\lambda F}(x)=\{y:x-y\in\lambda F(y)\},\quad r_F(y)=\inf_{v\in F(y)}\|v\|.
\]
空纤维残差取 \(+\infty\)。令 \(0<\kappa<1\)，\(\omega:[0,R]\to[0,\infty)\) 有限、非减，在零处连续且 \(\omega(0)=0\)。用 \(H(t)=(t+\omega(t))/2\) 表示正式稿的步长函数 \(B(t)\)。对指定允许关系 \(\mathcal J(x)\subseteq J_{\lambda F}(x)\)，以下条件逐一量化每个 \(x\in U_R\) 和每个 \(y\in\mathcal J(x)\)：
\[
\tag{A} d(y)\le\kappa d(x),\qquad
\tag{B} \|x-y\|\le H(d(x)).
\]
覆盖是指每个相关输入都有 \(\mathcal J(x)\ne\varnothing\)；完整窗是指 \(\mathcal J=J_{\lambda F}\) 在该窗内逐点相等。[普通 PPA 主稿的 (P1)–(P4)](../../发表成果整理/RLEB/sections/theorem_spine.tex) 从 (P2) 得 B，从 (P3) 与 (P4) 的兼容得 A，另列覆盖和可和条件。以下只使用各项结论所列前提。

任取输入—输出关系 \(T\)，定义
\[
 F_T(y)=\{(x-y)/\lambda:y\in T(x)\}.\tag{1}
\]
代入近端包含式即得 \(J_{\lambda F_T}=T\)，且 \(\operatorname{zer}F_T=\{x:x\in T(x)\}\)。若 \(T\) 是全域双射，则 \(F_T=(T^{-1}-I)/\lambda\) 也是全域单值算子。

<a id="ab-geometry"></a>
## 2. 一步可行域、覆盖边界及零集

置 \(t=d(x)\)、\(u=d(y)\)、\(s=\|x-y\|\)。距离函数的 1-Lipschitz 性给出 \(|t-u|\le s\)。

- **A 单独。** \(s\ge t-u\ge(1-\kappa)t\)。任一合法轨道有 \(d(x^k)\le\kappa^k d(x^0)\)。取 \(T(x)=\kappa x\)、\(S=\{0\}\) 使这两个界同时取等。若检验完整窗，任取该窗中原算子的零点 \(x\)，完整近端包含 \(y=x\)，A 强制 \(x\in S\)。因此 \(\operatorname{zer}F\cap U_R=S\cap U_R\)。对非孤立零集，双射 \(T(a,b)=(a+\mathbf 1_{b\ne0},\kappa b)\) 的固定集为横轴。非零高度的轨道步长始终不小于 1，切向坐标发散。把切向增量换成 \(1/|b|\)（在 \(b=0\) 仍取 0），可排除靠近零集时的任何有界统一步长包络。若 \(S=\{p\}\)，则 \(s\le t+u\le(1+\kappa)t\)，所以所有无限合法轨道均有限长并趋于 \(p\)。此时 \(T(x)=p-\kappa(x-p)\) 达到一步上界以及总长 \((1+\kappa)t/(1-\kappa)\)。
- **B 单独。** \((t-H(t))_+\le u\le t+H(t)\)。两个距离端点分别由原点目标上的径向映射
  \[
  T_-(x)=(1-H(\|x\|)/\|x\|)_+x,\qquad
  T_+(x)=(1+H(\|x\|)/\|x\|)x
  \]
  达到。令 \(T_\pm(0)=0\)，窗外任选非减延拓。固定集均为 \(\{0\}\)。对覆盖的 \(p\in S\)，B 强制 \(\mathcal J(p)=\{p\}\)，且 \(x\to p\) 时全部允许输出统一满足 \(\|y-p\|\le\|x-p\|+H(d(x))\to0\)。B 容许不收敛的轨道。取 \(S=\{0\}\) 和平面转角 \(2\pi/16\) 的旋转 \(T\)，则 \(s=2\sin(\pi/16)t<t/2\le H(t)\)，每条非零轨道循环。B 也不强制线性次正则。取 \(F(y)=y^3\)、\(\lambda=1\)，在 \(|x|\le1\) 的唯一近端输出上 \(s=|y|^3\le(|y|+|y|^3)/2=t/2\)，而 \(d(y)/r_F(y)=1/y^2\)。
- **A 与 B。** 任一步的三个标量的精确可行域是
  \[
  0\le u\le\kappa t,\qquad t-u\le s\le H(t).\tag{2}
  \]
  必要性由距离的 1-Lipschitz 性得到。任给满足 (2) 的三元组，在横轴目标上令 \(x=(0,t)\)、\(y=(\sqrt{s^2-(t-u)^2},u)\)，并加上 \(S\) 上的恒等步，由 (1) 实现该三元组。若整个距离窗均允许覆盖，这一步还可加入 \(T(a,b)=(a,\kappa b)\) 的完整关系。新增步在 \(t>0\) 时严格下降，因此不会新增零点。

在每个被覆盖的输入距离 \(t>0\)，(2) 强制
\[
 H(t)\ge(1-\kappa)t
 \quad\Longleftrightarrow\quad
 \omega(t)\ge(1-2\kappa)t.\tag{3}
\]
这也是在整个距离管上存在实现的精确条件，取 \(T(a,b)=(a,\kappa b)\) 即可。若 (3) 在一列趋零的正尺度上失败，而覆盖整个 \(U_R\)，则 \(S\cap U\) 在 \(U\) 内相对开且相对闭。否则可找到 \(p\in S\cap U\) 和任意近的 \(x\notin S\)，使 \([p,x]\subset U_R\)。连续距离函数在该线段取遍 \([0,d(x)]\)，与失败尺度处的覆盖矛盾。此时连通 \(U\) 若与 \(S\) 相交，就有 \(U\subseteq S\)。

若某个实测 \(t>0\) 满足 \(H(t)=(1-\kappa)t\)，必有 \(s=(1-\kappa)t\)、\(u=\kappa t\)。任取 \(p\in P_S(y)\)，则
\[
t\le\|x-p\|\le\|x-y\|+\|y-p\|=t.
\]
欧氏范数三角等号给 \(y=\kappa x+(1-\kappa)p\)。因此 \(p\) 由该步唯一确定，同时属于 \(P_S(x)\)。若轨道各正距离尺度均达到该临界等式，各步共享同一最近零点，沿同一线段前进，轨道总长恰为初始距离。

给定任意非空闭集 \(S\)，取全域关系 \(T(x)=\{p+\kappa(x-p):p\in P_S(x)\}\)。它的每个输出有 \(s=(1-\kappa)t\) 及 \(u=\kappa t\)，后者由 \(t-s\le u\le\|y-p\|\) 得到。在满足 (3) 的工作窗内，全部输出均满足 A+B，且 (1) 给出以 \(S\) 为完整零集的实现。因此 A+B 容许任意非空闭的零集形状。以 \(S=\{-1,1\}\) 为例，输入 0 的两个输出不同，A+B 也容许多值近端。

<a id="ab-residual"></a>
## 3. A 强制的真残差界及其适用域

对受检图值 \(v=(x-y)/\lambda\)，A 给出
\[
 u\le\kappa t\le\kappa(u+\lambda\|v\|)
 \quad\Longrightarrow\quad
 u\le\frac{\lambda\kappa}{1-\kappa}\|v\|.\tag{4}
\]
对已覆盖的输入，另有 \((1-\kappa)t\le\inf_{y\in\mathcal J(x)}\|x-y\|\)。B 单独给出 \(\sup_{y\in\mathcal J(x)}\|x-y\|\le H(t)\) 和 \(r_F(y)\le s/\lambda\le H(t)/\lambda\)。因此沿 A+B 轨道，所选图值的范数和输出真残差都趋零；若长度预算有限，两者逐项求和也均不超过该预算除以 \(\lambda\)。

对给定 \(y\)，若存在 \(\rho(y)\ge0\)，使每个满足 \(\lambda\|v\|<\rho(y)\) 的 \(v\in F(y)\) 均对应受检步，则
\[
 \lambda r_F(y)\ge\min\!\left\{\frac{1-\kappa}{\kappa}d(y),\rho(y)\right\}.\tag{5}
\]
短图值由 (4) 控制，长图值满足 \(\lambda\|v\|\ge\rho(y)\)。对全纤维取下确界即可，无须最小值达到。特别地，\(\rho(y)\ge(1-\kappa)d(y)/\kappa\) 时得到完整真残差的线性次正则界。若允许图值的下确界等于 \(r_F(y)\)，也可直接对它们取下确界。

对完整窗和 \(y\in U_R\)，可取
\(\rho(y)=\min\{\operatorname{dist}(y,X\setminus U),R-d(y)\}\)，因为短图值的输入 \(y+\lambda v\) 属于 \(U_R\)。特别地，当 \(U=X\)，
\[
 d(y)\le\frac{\lambda\kappa}{1-\kappa}r_F(y)\qquad(d(y)\le\kappa R).\tag{6}
\]
在一般开窗下，(6) 至少适用于以任意 \(p\in S\cap U\) 为中心、半径 \(\kappa\min\{R,\operatorname{dist}(p,X\setminus U)\}\) 的球。由 \(d(y)\le\|y-p\|\) 和 \(\operatorname{dist}(y,X\setminus U)\ge\operatorname{dist}(p,X\setminus U)-\|y-p\|\) 即可验证 (5) 的余量。若采用输出和图值均截断的近端，并且 \(y\) 落在输出窗内部，可把 \(\rho(y)\) 同时限制到允许的缩放图值球半径。对一般允许关系，需要核对该性质。

\(T(x)=\kappa x\) 使 (4) 和 (6) 取等。整输入管保证半径 \(\kappa R\) 对同一常数也是锐的。在 \(X=\mathbb R\)、\(S=\{0\}\) 上，给完整径向关系 \(x\mapsto\kappa x\) 加入单步 \(R+\varepsilon\mapsto y\)，其中 \(\kappa R<y<R\)、\(0<\varepsilon<y/\kappa-R\)。原输入窗上的图不变，新增步却给出 \(\lambda r_F(y)\le R+\varepsilon-y<(1-\kappa)y/\kappa\)。

仅检验一般子关系时，局部真线性次正则也可能失败。取 \(\lambda=1\)、\(F(y)=\{y,y^3\}\)、\(S=\{0\}\)，只允许 \(y=x/2\)。覆盖全体输入，\(u=s=t/2\)，但 \(r_F(y)=|y|^3\) 当 \(|y|\le1\)，所以 (6) 失败。这里较小的图值分支未进入 A 的量词。

<a id="ab-output"></a>
## 4. 输出相对步长界及原模的边界

固定 \(H,\kappa\)，假定 (3) 在整个 \((0,R]\) 上成立。令 \(\eta=\sup_{0<t\le R}H(t)/t\)。对所有该窗上的 A+B 关系，同时保证某个有限统一常数 \(C\) 使 \(s\le C d(y)\) 的充要条件是 \(\eta<1\)。最小通用常数为 \(\eta/(1-\eta)\)。

若 \(\eta<1\)，则 \(s\le\eta t\le\eta(u+s)\)，移项即得。取 §2 的完整径向近端 \(T_-\)。由 (3)，\(u=(t-H(t))_+\le\kappa t\)，位移为 \(\min\{t,H(t)\}\)。当 \(H(t)<t\) 时比值为 \((H(t)/t)/(1-H(t)/t)\)，达到或逼近所给常数。若某尺度 \(H(t)\ge t\)，则 \(u=0<s\)。若 \(\eta=1\) 且处处 \(H(t)<t\)，这个比值在一列尺度上发散。局部缩窗版的精确门是 \(\limsup_{t\downarrow0}\omega(t)/t<1\)。

同一个 \(\omega\) 的最近零锚 RL 也未必成立。取横轴目标和双射 \(T(a,b)=(a+(\sqrt3/2)b,b/2)\)。此时 \(u=t/2\)、\(s=t\)，非线性模 \(\omega(t)=t+t^2\) 足以保证 B。输入的唯一最近零锚为 \(p=(a,0)\)，而 \(\|2T(x)-x-p\|=\sqrt3t>\omega(t)\) 当 \(0<t<\sqrt3-1\)。对任意最近输入锚 \(p\)，一般可用 B 推得 \(\|2y-x-p\|\le t+2H(t)=2t+\omega(t)\)，这是向量恒等式 \(2y-x-p=(x-p)+2(y-x)\) 的直接结果。

<a id="ab-length"></a>
## 5. 所有 A+B 关系的锐长度预算

定义
\[
 \Theta_H(t)=\sum_{j=0}^{\infty}H(\kappa^jt)
 =\frac{t}{2(1-\kappa)}+\frac12\sum_{j=0}^{\infty}\omega(\kappa^jt).\tag{7}
\]
对合法轨道，自 \(x^k\) 开始的第 \(j\) 步满足 \(d(x^{k+j})\le\kappa^jd(x^k)\)、\(\|x^{k+j+1}-x^{k+j}\|\le H(\kappa^jd(x^k))\)。故任一无限合法尾满足
\[
 d(x^k)\le\sum_{j=k}^{\infty}\|x^{j+1}-x^j\|\le\Theta_H(d(x^k)).\tag{8}
\]
下界由 \(s_j\ge d(x^j)-d(x^{j+1})\) 求和及 \(d(x^j)\to0\) 得到，由径向收缩达到。若 \(\Theta_H(d(x^0))<\operatorname{dist}(x^0,X\setminus U)\)，则有限前缀的位移和小于开窗余量，而且 A 保证输出距离仍 \(\le R\)。有覆盖时可归纳地延拓任意选择。若 \(\Theta_H(d(x^0))<\infty\)，轨道 Cauchy，极限属于闭集 \(S\)。严格开窗余量还保证极限在 \(U\)。有限预算满足
\[
 H(t)+\Theta_H(\kappa t)=\Theta_H(t),\qquad s+\Theta_H(u)\le\Theta_H(t).
\]

固定满足 (3) 的任意 \(H,\kappa\)，取 \(X=\mathbb R^2\)、\(S=\mathbb R\times\{0\}\)，并令
\[
 a(t)=\sqrt{H(t)^2-(1-\kappa)^2t^2},\qquad T(z,b)=(z+a(|b|),\kappa b).\tag{9}
\]
可用 \(\omega(t)=\omega(R)+(1-2\kappa)_+(t-R)\) 在 \(t>R\) 延拓模，保持 (3)。映射 (9) 的逆是 \((z,b)\mapsto(z-a(|b|/\kappa),b/\kappa)\)。于是 (1) 给出全域单值算子及其完整单值近端，零集恰为 \(S\)。每步满足 \(d(Tx)=\kappa d(x)\)、\(\|Tx-x\|=H(d(x))\)。因此任意初始距离、任意前缀和任意尾的长度上界由**同一个**完整近端逐项达到。若非负标量势 \(W\) 在整个类上满足 \(s\le W(t)-W(u)\)，代入 (9) 并迭代可知 \(W(t)\ge\Theta_H(t)\)，所以有限时 \(\Theta_H\) 是最小的通用势。

对每个 \(0<t\le R\)，\(\omega\) 在 \([\kappa^{j+1}t,\kappa^jt]\) 上介于两个端点值，故
\[
 \log(1/\kappa)\omega(\kappa^{j+1}t)
 \le\int_{\kappa^{j+1}t}^{\kappa^jt}\frac{\omega(v)}{v}\,dv
 \le\log(1/\kappa)\omega(\kappa^jt).
\]
求和并注意 \(\int_t^R\omega(v)\,dv/v<\infty\)，得到
\[
 \Theta_H(t)<\infty\quad\Longleftrightarrow\quad\int_0^R\frac{\omega(v)}v\,dv<\infty.\tag{10}
\]
同理，对任意 \(p>0\)，\(\sum_jH(\kappa^jt)^p\) 是相邻步长 \(p\) 次幂和的最优统一上界，有限当且仅当 \(\int_0^R\omega(v)^p\,dv/v<\infty\)。用 \(\omega^p\) 作分段比较，并用 \(H(v)^p\) 与 \(\max\{v^p,\omega(v)^p\}\) 只相差固定倍数即可。

若 (10) 发散，(9) 的轨道仍有 \(d(x^k)\to0\) 和步长趋零，但切向坐标趋于 \(+\infty\)，因为 \(a(t)\ge H(t)-(1-\kappa)t\)。所以对固定可行模和所有原关系，Dini 是统一保证有限长度的必要条件。用同一个非 Dini 包络，径向收缩仍可有限长，因此单条轨道的有限长度不强制给定包络满足 Dini。

在单点零集子类，固定 \(H,\kappa\) 的锐上界更小。令 \(h_*(t)=\min\{H(t),(1+\kappa)t\}\)。由 §2 与非减性，每个尾长至多为 \(\sum_{j\ge0}h_*(\kappa^jd(x^k))\)。平面上取零点为原点，令 \(T\) 把每个半径 \(t>0\) 缩为 \(\kappa t\)，并旋转角度
\[
 \alpha(t)=\arccos\!\left(\frac{1+\kappa^2-(h_*(t)/t)^2}{2\kappa}\right).
\]
公式有定义，因为 \((1-\kappa)t\le h_*(t)\le(1+\kappa)t\)。余弦定理给出 \(s=h_*(t)\)，逆映射先由输出半径恢复输入半径，再反向旋转。因此这是完整双射近端，逐步饱和该子类的预算。

若只量化无限合法轨道，允许关系无需覆盖整个距离管，Dini 发散时也可构造反例，即使 (3) 在某些尺度失败。从 \(\kappa^jt\) 中保留满足 \(H(\kappa^jt)\ge\kappa^jt\) 的指标。丢弃的项之和至多等于可和的几何级数，因此保留项的 \(H\)-和发散。记保留的高度为 \(t_i\)，满足 \(t_{i+1}\le\kappa t_i\)。在横轴上令近端恒等，在每个高度 \(t_i\) 上将下一步法向坐标设为 \(t_{i+1}\)，切向位移设为 \(\sqrt{H(t_i)^2-(t_i-t_{i+1})^2}\)。这些步满足 A+B，切向和依旧发散，因为 \(\sum_i(t_i-t_{i+1})=t_0\)。由 (1) 得到完整近端，其输入域为所列层与横轴。

<a id="ab-clusters"></a>
## 6. 有界轨道、紧零集和单调子类

A+B 使每条合法轨道的距离和步长都趋零。若轨道有界，其聚点集 \(L\) 非空、紧且 \(L\subseteq S\)。它也是连通的。若 \(L=L_1\cup L_2\) 是不相交非空紧集的分解，给两块取正间距邻域。轨道最终属于两邻域之并，否则从余下的有界点列可抽出一个新的聚点。同时两邻域各被无限次访问，故轨道需无限次跨越正间距，与步长趋零矛盾。因此若 \(S\) 全不连通，有界轨道必收敛到一点。

对给定可行的非 Dini 模，有界不收敛也能在完整近端上实现。取平面单位圆 \(S\)，在充分小的环带上写 \(x=(1+b)e^{i\theta}\)。用 (9) 的 \(a\) 定义
\[
 \beta(b)=2\arcsin\!\frac{a(|b|)}{2\sqrt{(1+b)(1+\kappa b)}},\qquad
 T(x)=(1+\kappa b)e^{i(\theta+\beta(b))}.
\]
\(H(t)\to0\) 保证缩小环带后反正弦有定义。距离恰缩为 \(\kappa|b|\)，弦长平方为 \((1-\kappa)^2b^2+4(1+b)(1+\kappa b)\sin^2(\beta(b)/2)=H(|b|)^2\)。环带外令 \(T(x)\) 为任意一个到圆的最近点，便得全域单值完整近端，由 (1) 给出原算子，零集恰为圆。任取环带内的 \(b_0>0\)，角增量趋零而和发散，因为 \(\arcsin z\ge z\)、分母有上界且 \(\sum_j a(\kappa^jb_0)=\infty\)。对任意目标角，取第一次越过其加上 \(2\pi m\) 的时刻，超越量趋零。因此聚点集恰为整个圆。

在另有单调性的子类中，A 单独给出锐长度界。对每步取 \(p\in P_S(x)\)，单调性给 \(\langle y-p,x-y\rangle\ge0\)，所以 \(u^2+s^2\le t^2\)。因为 \((t+u)/(t-u)\le(1+\kappa)/(1-\kappa)\)（\(t>0\)），有
\[
s\le\sqrt{\frac{1+\kappa}{1-\kappa}}(t-u).
\]
当 \(t=0\) 时 \(s=0\) 也由平方界得到。沿合法轨道求和即给相应的总长度界。取 \(S=\{0\}\) 及 \(T=\kappa R_{\arccos\kappa}\)，其中 \(R_\alpha\) 为平面旋转，则 \(T^{-1}-I\) 的对称部分为零，故由 (1) 得到单调线性算子。其每步和总长都达到所给界。

## 证据与适用范围

正向 Dini 估计已见 [C09](general_modulus_dynamics.md#gm-dini-length)，非 Dini 特例见 [C10](general_modulus_dynamics.md#gm-log-object) 和 [C287](rleb_dini_geometry.md#rdg-winding)。本页补充固定一般模的逐步精确饱和、完整图真残差的锐窗，以及输入步界何时统一推出输出相对界。两条独立推导分别复核了一步和残差量词、长度及反例，证明均给于正文。公开先行性未核。
