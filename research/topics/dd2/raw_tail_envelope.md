# 一般原误差模的零缺陷最佳尾上确界

本页在 [C458](tail_envelopes.md#dd2-zero-defect-optimal-tail) 的平方降幅证明之外，补上原 \(\psi\) 不连续、不非减甚至不可测时的原域实现。数值上界可以连续，但不把原函数改名为其包络，也不把未取到的最坏边说成实际达到。

<a id="dd2-raw-gauge-optimal-tail"></a>
## RT1 · C461-v1 的原域、对象与结论

**状态：derived-checked。三席已独立重构并逐源冷读实际正文、身份、图边及地图，无未关闭实质异议。**

固定 \(\lambda,R>0\)，\(0\in D_\psi\subseteq[0,\infty)\)，原 \(\psi:D_\psi\to[0,\infty)\) 有限，且
\[
\lim_{\epsilon\downarrow0}
 \sup_{\rho\in D_\psi\cap[0,\epsilon]}\psi(\rho)=0 .
\tag{RT1}
\]
不要求原 ψ 可测、连续或非减。含零的前缀使 \(\psi(0)=0\)。
定义派生平方距离上界
\[
m(q)=\sup_{\rho\in D_\psi}
 \min\{\psi(\rho)^2,(q-\lambda^2\rho^2)_+\},\qquad
p(t)=\sqrt{m(t^2)} .
\tag{RT2}
\]
这里的原尺度行池明确为
\[
\mathcal E_\psi(t)=\left\{(a,s):
0\le a\le t,\ t-a\le s\le\sqrt{t^2-a^2},\
\exists\rho\in D_\psi\cap[0,s/\lambda],\
a\le\psi(\rho),\ a=0\Rightarrow\rho=0\right\}.
\tag{RT2a}
\]
成本是该行的实际 s；它保留原残差的存在量词，未把上确界端点补进原行。
先指定 \(\varphi:[0,R]\to[0,R]\)，并核 \(p\le\varphi\)。
本节量化 \(\Phi=0,U=V_\psi=H\) 的全部有限维 E0 对象，S 为非空闭子零集，
完整真残差在原域评价，同一允许关系在全 R 距离窗非空覆盖。
该类包含全部合格的二维闭完整图、精确单点零集和全部近端选择。

对每个 \(t\in[0,R]\)，令
\[
q_0=t^2,\qquad q_{k+1}=m(q_k),\qquad
\mathcal T_\psi(t)=\sum_{k\ge0}\sqrt{q_k-q_{k+1}} .
\tag{RT3}
\]
则 \(\mathcal T_\psi(t)\) 是：

1. 同一原数据类、同一原预设目标，从精确初距 t 出发的全部真实轨道长度的上确界；
2. 原可实现真残差尺度行池的最小非负支付值；
3. 放宽到 \(0\le a\le p(t)\)、成本 \(\sqrt{t^2-a^2}\) 的闭尺度池的最小非负支付值。

允许值为无穷。第3项中的端点可以是原数据未取到的上确界；同值不表示两个边池相同。第1项的下界由每个有限精度、有限前缀对应的完整原图逼近，不宣称一个图或一条轨道同时达到全部最优值。连续非减原模另由 C458 的同一完整旋转达到。

## RT2 · 派生上界的正则性与原数据认证

对每个固定原 \(\rho\)，RT2 中的函数关于 q 非减、1-Lipschitz，且在 \([0,q]\) 内。取上确界得
\[
m(0)=0,\qquad
0\le m(q_2)-m(q_1)\le q_2-q_1\quad(q_2\ge q_1),
\tag{RT4}
\]
所以 m 连续非减，\(q-m(q)\) 非减。

对固定 q>0，由 RT1 选 \(\epsilon>0\) 使原前缀上的 \(\psi^2\le q/2\)。
前缀外的项至多 \((q-\lambda^2\epsilon^2)_+<q\)，因此
\[
m(q)\le\max\{q/2,(q-\lambda^2\epsilon^2)_+\}<q .
\tag{RT5}
\]
故 p 连续非减、正尺度严格小于 t，RT3 中 \(q_k\downarrow0\)，
\(G_k=q_k-q_{k+1}\) 非增且总和 \(t^2\)。

任意实际原边保同一真 \(\rho\in D_\psi\)，有
\[
a^2\le\psi(\rho)^2,\qquad
a^2\le t^2-s^2\le t^2-\lambda^2\rho^2,
\]
所以 \(a\le p(t)\le\varphi(t)\)。没有评价 \(\psi(s/\lambda)\)。
\(\lambda\rho>t\) 的数值行在 RT2 只贡献0；实际零输出已有 \(\rho=0\) 的原行，不用不合法残差实现这个0。零输入的能量强制驻定。

## RT3 · 全部实际路径与闭尺度池的共同上界

从任何 \(0<t_0\le R\) 出发，覆盖与距离不增给全路径存在。
对实际距离 \(u_k\)，RT2 给 \(u_k^2\le q_k\)，且 \(u_k\to0\)。
能量给 \(\Delta_k=u_k^2-u_{k+1}^2\ge s_k^2\)，因此
\[
\sum\Delta_k=\sum G_k=t_0^2,\qquad
\sum_{k<n}\Delta_k\ge\sum_{k<n}G_k .
\]
G 非增，故 [ZT4–ZT5 的正部和与根号积分](tail_envelopes.md#dd2-zero-defect-optimal-tail)
逐字给
\[
\sum_k s_k\le\sum_k\sqrt{G_k}=\mathcal T_\psi(t_0).
\tag{RT6}
\]
同一证明适用于闭尺度池和其有限前缀，不要求实际 \(\Delta_k\) 排序。
零尺度单独为0；本结论是全尾上界，不称每个固定步数的贪心前缀最优。

## RT4 · 用原残差和完整辅助前像逼近最优尾

固定 \(t>0\)、有限 N 和 \(0<\theta<1\)，递推
\[
q_0^\theta=t^2,\qquad q_{k+1}^\theta=\theta m(q_k^\theta).
\tag{RT7}
\]
若后继为0，该步投影到0，令 \(s_k=\sqrt{q_k^\theta}\)，以后驻定。对正后继
\(a=\sqrt{q_{k+1}^\theta}\)，有 \(a^2<m(q_k^\theta)\)。
所以能选一个同一原域的 \(\rho_k\) 满足
\[
a<\psi(\rho_k),\qquad
0<\lambda\rho_k<\sqrt{q_k^\theta-a^2}=:s_k .
\tag{RT8}
\]
正性用 \(\psi(0)=0\)；同一个 \(\rho_k\) 同时满足两个不等式。

在二维从任意 \(\|x_0\|=t\) 开始，每步取 \(\|y_k\|=a\)，使
\[
\|x_k-y_k\|=s_k,\qquad
\langle x_k-y_k,y_k\rangle=0,\qquad x_{k+1}=y_k .
\]
可用相对于 xₖ 的角度余弦 \(a/\|x_k\|\) 显式实现。
全部正输出半径严格下降，所以各正输出点互异。
在投影底图 \(P_{\{0\}}\) 上加入这至多 N 条主边，并对每个正输出加一条辅助边
\[
w_k=(1+\lambda\rho_k/a)y_k\ \longmapsto\ y_k .
\tag{RT9}
\]
辅助步为 \(\lambda\rho_k\)，锚积为 \(\lambda\rho_k a>0\)。
将所得有限附加关系记为 J，取完整
\(F(y)=\lambda^{-1}\{x-y:y\in J(x)\}\)。

每个正输出 yₖ 的全部前像只有它的主前像和径向辅助前像；
输入彼此重合只增加合法后继，不制造别的同输出纤维。
RT8 使完整真残差恰为 \(\rho_k\)。零输出的纤维 \(F(0)=H\)，真残差0。
每条辅助边及主边都保原 E0 的零缺陷、原真残差界；辅助输入即使在 R 外，
也保留在完整纤维内，若在 R 内则同样由 RT2 认证原预设目标。
所有附加边非驻定，故精确零集0。投影底图给全域覆盖及零驻定，
有限添边给闭图；原 R 窗全选择不变。

因此从 x₀ 出发可以在这个同一完整图中实际走完所选主链，再投影到零。
它的长度至少为 \(\sum_{k<N}s_k\)。
m 连续使 \(\theta\uparrow1\) 时每个固定前缀的 \(q_k^\theta\to q_k\)，故这些成本逼近
\(\sum_{k<N}\sqrt{q_k-q_{k+1}}\)。最后取 \(N\to\infty\)，证明真实类的上确界至少为 RT3。
这些真实边也在原尺度池中，结合 RT6 得 RT1 所列三个值相等。

## RT5 · 有限性、原目标与使用边界

原域输入步下界为
\[
b_\psi(t)=\inf_{\rho\in D_\psi}
 \max\{\lambda\rho,t-\psi(\rho)\}.
\tag{RT10}
\]
RT1 使它在正尺度为正：取前缀 \(\psi\le t/2\)，则前缀内第二项至少 t/2，
前缀外第一项至少 \(\lambda\epsilon\)。它非减、1-Lipschitz，且 \(b_\psi\le t\)。

m 和 \(q-m(q)\) 均非减，所以 RT3 的每个 \(q_k(t)\) 及每个降幅
\(q_k(t)-m(q_k(t))\) 随初距 t 非减，\(\mathcal T_\psi\) 也非减。
[C454 的完整统一类充要门](irregular_zero_defect_length.md#dd2-irregular-zero-defect-length)
因此适用，给
\[
\mathcal T_\psi(R)<\infty
\quad\Longleftrightarrow\quad
\int_0^R\frac{t}{b_\psi(t)}\,dt<\infty ,
\qquad
\mathcal T_\psi(t)\le2\int_0^t\frac{u}{b_\psi(u)}\,du
\quad\text{于可积窗}.
\tag{RT11}
\]
必要侧保留 C454 的同一个真实无限长闭图；任一坏初距 \(t_*\le R\) 迫使
\(\mathcal T_\psi(t_*)=\infty\)，非减性再给 \(\mathcal T_\psi(R)=\infty\)。
该图的原边自动满足已经认证的
\(a\le p(t)\le\varphi(t)\)，不因为 p 可能小于一个旧安全包络而被删掉。
RT4 的逼近本身不保证有限最优值达到，积分发散时的同图坏轨道是另一份已核构造。

\(\mathcal T_\psi\) 有限时是同原数据共同的最小非负距离支付函数；
一般开 U 的应用须保输入覆盖和严格有限前缀预算
\(\mathcal T_\psi(t_0)<d(x^0,U^c)\)。原 ψ 的不可测性不妨碍这个变分定理，
但也不赋予上确界、级数或积分有限查询可计算性。
不处理 RT1 失效的原模，不把更强预设目标的筛选、正锚下界、指定连续单值结构的
最优值或公开新颖性纳入此身份。
