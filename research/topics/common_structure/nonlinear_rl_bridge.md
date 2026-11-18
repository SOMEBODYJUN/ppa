# 原非线性 RL 与真残差的图桥

固定普通欧氏 PPA \(x=y+\lambda v,\ v\in F(y),\ \lambda>0\)。用完整原纤维定义 \(r_\eta(z)=\operatorname{dist}(\eta,F(z))\)，\(\eta=0\) 即真残差。除非另有说明，\(S=F^{-1}(0)\) 非空闭。全对一般模 RL 采用 [C09](../../canonical/general_modulus_dynamics.md#gm-data)。最近输入零锚 RL 对每个允许步只要求存在 \(p\in P_S(x)\) 使 \(\|2y-x-p\|\le\omega(d(x,S))\)，按[原 RLEB 主定理](../../canonical/true_residual_selection_rleb.md#trs-object)使用。这两个全称范围不同。

<a id="rl-shift-obstruction"></a>
## 1. C333 · 只在输出位移上加惩罚，无法延续同一近端弦的强制性

给定位移惩罚 \(P:X\to\mathbb R\cup\{+\infty\}\)，考虑
\[
\mathcal M_P(z,u)=\sup_{(y,v)\in\Gamma}
 \{\langle z-y,v-u\rangle-P(z-y)\}.
\]
允许 \(P\) 非径向、非幂次、非凸。固定仓库 [C242](../../canonical/triangular_rleb.md#tri-object) 的完整原算子 \(F(a,b)=(a,-\sqrt{|a|})\)、\(\lambda=1\)、\(S=\{0\}\times\mathbb R\)。\(\Gamma\) 可取完整图，或取任一包含 \((0,0)\) 附近完整图点的图窗。若 \(\mathcal M_P(0,0)=0\)，则对充分小的 \(a>0\)，取 \(v_a=(a,-\sqrt a)\)，在零锚上确界中代入原图点 \((-v_a,F(-v_a))\)，得
\[
 P(v_a)\ge \langle v_a,F(-v_a)\rangle=a-a^2 .
\]
另一方面，\(v_a=F(a,0)\) 是实际 PPA 图值。令 \(y=(a,0),\ x=y+v_a\)，在 \(\mathcal M_P(x,0)\) 中用这条实际近端弦的见证，得到的项满足
\[
 \|v_a\|^2-P(v_a)\le 2a^2=o(\|v_a\|^2).
\]
故不存在与尺度无关的正 \(c\)，使这条见证在所有小实际步上给出 \(c\|v\|^2\) 下界。若 \(P(h)=\phi(\|h\|)\) 径向，另取 \(y=(a,a)\) 代入 \(\mathcal M_P(0,0)=0\)，得 \(\phi(\sqrt2a)\ge a^{3/2}-a^2\)。因此 \(\phi(\rho)\ge 2^{-3/4}\rho^{3/2}-\rho^2/2\) 对每个充分小 \(\rho>0\) 成立；实际弦见证在小非零步上严格为负。结论只针对这条见证和固定的输出位移惩罚。上确界的其他竞争点及输入、反射差共同参与的惩罚仍可研究。

该同一个 \(F\) 全域唯一完整预解式，真残差平方为 \(a^2+|a|\)。反射是 \((A,B)\mapsto(0,B+\sqrt{2|A|})\)，故全对 RL 可取 \(\omega_{\rm pair}(t)=t+\sqrt{2t}\)，最近零锚可取 \(\omega_{\rm anchor}(t)=\sqrt{2t}\)。取 \(\psi(s)=s^2\)、\(R=1/16\)，全对兼容比例最多 \((1/4+1/\sqrt2)^2<1\)，最近零锚版最多 \((1/8+1/\sqrt2)^2<1\)，两模均 Dini。它们都是原 RLEB 的实际实例。此反例也说明验收必须含有 \(\omega(t)/t\to\infty\) 的工作模型。C329 的弱单调与 Luke–Tam 的输入差平方次单调各有不同分母，本页只把它们作为可能丢失非线性 RL 的二次比较。

<a id="rl-tube"></a>
## 2. C334 · 直接使用输入差与反射差的定量联系

设 \(X=\mathbb R^n,\ n\ge1\)，取任意非空认证原图块 \(\Gamma\subset\operatorname{gph}F\)。对任意探测点 \(c=(z,u)\) 定义
\[
 P_+(c)=z+\lambda u,\qquad P_-(c)=z-\lambda u.
\]
固定有限、非减的 \(\omega:[0,\infty)\to[0,\infty)\)，\(\omega(0)=0\)，在零处连续。局部约定见下文。定义容许宽度集
\[
 I_\omega(c;\Gamma)=\left\{h\ge0:\quad
 \|P_-(c)-P_-(b)\|\le h+\omega\big(\|P_+(c)-P_+(b)\|+h\big)
 \quad\text{对每个 } b\in\Gamma\right\},\qquad
 g_\omega(c)=\inf I_\omega(c;\Gamma).
 \tag{1}
\]
空集下确界为 \(+\infty\)。式 (1) 对所有比较对象使用同一 \(h\)。\(0\in I_\omega(c;\Gamma)\) 对每个 \(c\in\Gamma\) 成立，当且仅当原图块对所有图对满足**同一原模**的全对 RL。这里使用实际可行的 \(h=0\)，因此即使 \(\omega\) 在正点有跳跃也不改变原条件。

几何上 \(g_\omega\) 是各双差到集合
\(\mathcal C_\omega=\{(a,b):\|b\|\le\omega(\|a\|)\}\) 的积空间最大范数距离之上确界。给定宽度 \(h\)，第一坐标在原向量方向外移至范数 \(\|a\|+h\)，第二坐标向零缩至范数 \((\|b\|-h)_+\)，于是单项的可行条件正是 (1)。每个单项的可行宽度集向上封闭，交集的下确界等于各下确界的上确界。连续情况下集合闭，可用 \(g_\omega=0\) 取代 \(0\in I_\omega\)；有跳跃时仍按后者检验 RL。

**真残差给可行宽度。** 假定该图块满足全对 RL。给定 \(z,\eta\)，若 \((z,u)\in\Gamma\)，则
\[
 \lambda\|u-\eta\|\in I_\omega((z,\eta);\Gamma).
 \tag{2}
\]
证明是把探测点 \((z,\eta)\) 改为图点 \((z,u)\)。两坐标都改变 \(\lambda\|u-\eta\|\)，对每个 \(b\in\Gamma\) 用一次同模 RL 和三角不等式。若同一图块含完整纤维中任意逼近 \(r_\eta(z)\) 的图值，则
\[
 g_\omega(z,\eta)\le \lambda r_\eta(z).
 \tag{3}
\]
无需残差达到，且不能对缺少近极小图值的选中支宣称 (3)。

**同一可行宽度约束原近端弦。** 对每个 \(z=y+\lambda(v-\eta)\)、\((y,v)\in\Gamma\)，把 \(b=(y,v)\) 代入 (1)。输入差恰为零，反射差恰为 \(2(z-y)\)。所以对每个可行 \(h\)，
\[
 \|z-y\|\le H(h),\qquad H(h)=\tfrac12\big(h+\omega(h)\big).
 \tag{4}
\]
若取下确界，用 \(H_+(g)=\lim_{t\downarrow g}H(t)\)，连续模时就是 \(H(g)\)。式 (4) 不需要比较任何平方弱单调项。实际原 PPA 取 \(\eta=0\)；一般 \(\eta\) 的见证只用于验证正则性的右端变化。

**接到同一零集或逆纤维。** 固定 \(\eta\) 且 \(S_\eta=F^{-1}(\eta)\ne\varnothing\)。若覆盖根 \(y\) 的输出域有真误差界 \(d(y,S_\eta)\le\psi(r_\eta(y))\)，则 (4) 和三角不等式给
\[
 d(z,S_\eta)\le H(h)+\psi(H(h)/\lambda)
       \qquad(h\in I_\omega((z,\eta);\Gamma)).
 \tag{5}
\]
只在 \(\psi\) 的评价窗内调用 (5)。反向，若某非减右连续 \(\Xi\) 给出 \(d(z,S_\eta)\le\Xi(g_\omega(z,\eta))\)，则在可取完整纤维近极小图值的同一输入窗，(3) 给真误差界 \(d(z,S_\eta)\le\Xi(\lambda r_\eta(z))\)。对一族 \(\eta\) 均匀，结论是变化右端上的度量正则不等式；固定零右端时是次正则。反向的根覆盖只用于选一个见证。要谈原轨道的全部根，须对每个根验证其图点在 \(\Gamma\)。

在**原 RLEB 收缩** \(d(y,S)\le\kappa d(z,S)\) 的域内，还得到更强的正向增长
\[
 (1-\kappa)d(z,S)\le H(h)\quad(h\in I_\omega((z,0);\Gamma)).
 \tag{6}
\]
证明是 \( (1-\kappa)d(z,S)\le\|z-y\|\) 加 (4)。这是评估图宽度能否直接取代真残差的定量转接。

**局部尺度。** 若只给 \(\omega:[0,R]\to[0,\infty)\)，可先固定一个比较子块和探测窗，使 (1)–(2) 使用的 \(\|P_+(c)-P_+(b)\|+h\le R\)。比较同输入的根时要求 \(h\le R\)。等价地，可在页首用任一非减扩展完成定义，证明只调用原窗内的值。不能从远图点的缺失推断余量界。反向只需图宽度的增长及用于 (2) 的共同测试窗，不会替代完整预解式覆盖。

**最近零锚的量词。** 对允许步 \(c=(y,v)\) 可用同一 (1) 的单锚比较集 \(\{(p,0)\}\)。存在 \(p\in P_S(P_+(c))\) 使 \(0\in I_\omega(c;\{(p,0)\})\)，恰为原最近零锚 RL。然而 (2) 要比较残差近极小图点和用于 (4) 的根图点。它不能由单锚版本自动推出。取 \(F(y)=\{4y,9y\}\)、\(\lambda=1\)、\(S=\{0\}\) 即知：每个输入的全部根 \(x/5,x/10\) 满足最近零锚模 \(0.8t\)、真误差界 \(d=r_F/4\)，以及 \(H(t)/4=0.225t<0.25t\)，但每个非零输入的两反射输出不同，不能在完整图上满足任何 \(\omega(0)=0\) 的全对 RL。

<a id="rl-tube-sharp"></a>
## 3. C335 · 即使原 RLEB 全部成立，标量图宽度也会改变最佳真残差幂

任取 \(0<\gamma<1\)，固定 \(\lambda=1\)，取完整单值算子
\[
 F(a,b,c)=\big(\operatorname{sgn}(a)|a|^\gamma,\ m b,\ -|b|^\gamma\big),\qquad
 S=\{(0,0,c):c\in\mathbb R\}.
\]
令 \(c_0=(1+m)^{-\gamma}\)。取 \(m\) 足够大使 \(7c_0/2<1\)，并取局部尺度 \(R>0\) 使 \(R^{1-\gamma}\le c_0\)。原方程逐坐标唯一可解，第一坐标的反射 \(R_0=2J_f-I\) 非扩张，因为 \(f(a)=\operatorname{sgn}(a)|a|^\gamma\) 单调且 \((\Delta a-\Delta f)^2\le(\Delta a+\Delta f)^2\)。第二、第三反射坐标分别为 \((1-m)b/(1+m)\) 和 \(c+2c_0|b|^\gamma\)（这里 \(b,c\) 是输入坐标）。故对输入对距 \(\delta\le R\)，反射差至多 \(\delta+2c_0\delta^\gamma\le3c_0\delta^\gamma\)。给定原模 \(\omega(\delta)=6c_0\delta^\gamma\)，这一估计留出一半余量；输入沿第二坐标趋零时第三反射差是 \(2c_0\delta^\gamma\)，所以线性 RL 失败。

完整真残差 \(r_F(a,b,c)\ge (a^2+b^2)^{\gamma/2}\)，且在 \(b=0\) 取等，因此 \(\psi(s)=s^{1/\gamma}\) 是原真误差界，其最佳幂为 \(1/\gamma\)。有 \(H(t)\le(7c_0/2)t^\gamma\) 对 \(t\le R\) 成立，故旧兼容给 \(\kappa=(7c_0/2)^{1/\gamma}<1\)，Dini 成立。可取包含原点的任意更小有界输入球 \(W\)（直径小于 \(R/2\)）及其完整根图块作为 \(\Gamma\)。再缩输入以满足原留域预算和残差近极小图点的覆盖。

对 \(z=(t,0,0)\)，\(t>0\) 小，原步长 \(s=t-J_f(t)\asymp t\)，因为 \(t=y+y^\gamma\) 给 \(y/t\to0\)。由 (4)，\(g_\omega(z,0)\gtrsim t^{1/\gamma}\)。反向，对每个比较点 \(b\in\Gamma\)，记 \(\delta=\|z-P_+(b)\|\)。探测点的反射差 \(\|z-P_-(b)\|\le 2s+\omega(\delta)/2\)（先比较输入 \(z\) 处的实际反射）。取 \(h=(4s/(6c_0))^{1/\gamma}\)。由非减性，
\[
 \omega(\delta+h)\ge\tfrac12(\omega(\delta)+\omega(h))
                    =\omega(\delta)/2+2s .
\]
故 \(h\) 可行，所有测试尺度仍小于 \(R\)。于是
\[
 g_\omega((t,0,0),0)\asymp t^{1/\gamma},
 \qquad r_F(t,0,0)=t^\gamma,\qquad d((t,0,0),S)=t .
\]
由 (6)，整个充分小输入窗有 \(d(z,S)\lesssim g_\omega(z,0)^\gamma\)，方才的轴上例证明这是该宽度检验的最佳幂。结论是在**同一完整原 PPA、同一固定非线性模、旧 RLEB 真的成立**的前提下，真实残差一侧的最佳幂 \(1/\gamma\) 与标量图宽度一侧的最佳幂 \(\gamma\) 可以不同。不能把 (1) 的标量宽度按同一个 \(\psi\) 当作原真残差。

<a id="rl-next-obligation"></a>
## 4. 研究边界

第 2 节在全对 RL 的原 \(\omega\) 上给出双方向的定量转换。第 3 节把转换损失定位到对输入与反射方向使用各自容许的标量宽度。最近零锚量词下，这个桥目前只恢复原锚比较，仍缺能同时接全输出与真残差的独立方向结构。下一步是考察让两坐标通过同一个原图值扰动共同移动时，能否用独立可验证的条件得到保真残差界，避免把完整原算子藏回定义里。C329 继续作为二次弱单调专门结果。
