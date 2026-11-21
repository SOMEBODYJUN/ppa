# DD2 的非幂次实际轨道

本页保留 [E0](core.md#dd2-exact-contract) 的对象：\(t=d(x,S)\)、\(a=d(y,S)\)、实际步 \(s=\|x-y\|\)、完整真残差 \(\rho=r_F(y)\)。目标 \(\varphi\) 先被指定，再用原 \(\Phi,\psi\) 认证；固定图实际达到该目标时另外证明。全部模型取普通 PPA、\(\lambda=1\)、\(U=V_\psi=H\)、\(D_\psi=[0,\infty)\)，并允许完整近端的全部选择。

第一节是既有 [C400](core.md#dd2-reverse) 的定量特化。第二节的 C451 是独立的对数误差模、完整旋转与剪切及其实际速率身份；通用零缺陷积分定理仍引用 [C420](../../canonical/dd2_function_hypotheses.md#fh-zero-defect-sharp)，不将该通用机制另称新结果。没有公开新颖性判断。

<a id="dd2-stretched-exponential-target"></a>
## 1. C400 补证：预设平方对数计步曲线

**NP1：先定目标和反向预算。** 取 \(H=\mathbb R^2,S=\{0\},R=e^{-2}\)，指定
\[
A(0)=0,\qquad
A(t)=\exp\!\left[-\sqrt{\log^2(1/t)+1}\right]
\quad(0<t\le R).
\tag{NP.e1}
\]
写 \(u=\log(1/t)\ge2\)，则
\[
\sqrt{u^2+1}-u=\frac1{\sqrt{u^2+1}+u}
\le\sqrt5-2<\frac14<\log\sqrt2 .
\]
最后一式可由 \(\log2=\int_1^2 dv/v>1/2\) 得到。因此
\(1/\sqrt2<A(t)/t<1\)，比例在零端趋 1；
\(A'(t)=(A(t)/t)u/\sqrt{u^2+1}>0\)，并在零处连续。按 C400 取
\[
\psi(r)=r,\qquad D(0)=0,\quad
D(t)=A(t)^2-\tfrac12t^2\ge0,\qquad \Phi(t)=-D(t).
\tag{NP.e2}
\]
该数据给 \(2a^2\le a^2+s^2\le t^2+2D(t)=2A(t)^2\)，故认证预设 \(a\le A(t)\)，且
\(D(t)/t^2=\Sigma_1(A(t)/t)\)。预设比例无共同小于 1 的上界，并不影响逐尺度认证。

**NP2：同一完整图在全部尺度取等。** 在窗内令
\[
J(x)=\frac{A(t)}t R_{\theta(t)}x,\qquad
\theta(t)=\arccos\!\frac{t}{2A(t)},\quad t=\|x\|>0,\qquad J(0)=0 .
\tag{NP.e3}
\]
窗外把半径延拓为 \(\widetilde A(t)=A(R)t/R\)，角度固定为 \(\theta(R)\)。
径向映射连续、严格递增且满射；给定非零输出，先唯一反解半径，再反旋转，因此 \(J\) 为全域同胚。令 \(F=J^{-1}-I\)，则 \(F\) 连续单值、完整 \(J_F=J\) 全域唯一，精确零集为 \(S\)，零输入驻定。对全部受检输入，唯一输出的完整纤维就是 \(F(y)=\{x-y\}\)，所以
\[
\rho=s=a=A(t),\qquad
\langle x-y,y\rangle=\frac{t^2}{2}-a^2=\Phi(t).
\tag{NP.e4}
\]
由 \(A(t)<t\) 得所有距离窗输入的实际输出仍在窗内。这里同时实现原真残差、同一最近锚和所指定的反向预算，不只是自由标量构形。

**NP3：精确速率和真实尾长。** 对任意 \(0<t_0\le R\)，记 \(u_0=\log(1/t_0)\)。唯一实际轨道恰有
\[
\log^2(1/t_{k+1})=\log^2(1/t_k)+1,\qquad
t_k=\exp[-\sqrt{u_0^2+k}],\quad
s_k=t_{k+1},\quad \|x^k-0\|=t_k .
\tag{NP.e5}
\]
因而 \(x^k\to0\)，距离、点误差的相邻比趋 1，根率也趋 1，故无 Q/R 线性率；但对每个 \(p>0\)，\(k^pt_k\to0\)。该实际渐近行为不与任何单一 \(k^{-p}\) 双侧同阶，仍可以有任意幂次的保守上界。

设 \(v_k=\sqrt{u_0^2+k}\)。对递减函数 \(f(x)=\exp[-\sqrt{u_0^2+x}]\) 作积分比较，实际尾长满足
\[
2(v_{k+1}+1)e^{-v_{k+1}}
\le\mathcal L_k=\sum_{n=k+1}^{\infty}f(n)
\le2(v_k+1)e^{-v_k},
\qquad
\mathcal L_k\sim2(v_k+1)e^{-v_k}.
\tag{NP.e6}
\]
两界比趋 1，且上界有限。由 \(A\) 非减，使用同一原数据、始终合法的任意允许轨道还有统一距离比较 \(t_k\le A^{\circ k}(t_0)\)，该见证每步取等。上面的尾长渐近是这个固定旋转的实际值，未宣称全类的最优尾常数。非减比较尾和可和时，全选择留域和长度另依 C400 的原预算；此处 \(U=H\) 无位置边界。

<a id="dd2-log-half-order"></a>
## 2. C451-v1：对数强化半阶真误差界

**状态：derived-checked。** 三席独立重构并复读完整原图、实际渐近式、原模和统一类范围；负高度、零输入、外侧延拓、临界等号及两种指定目标均已核。

### LG1：共同原模和预设目标

固定 \(\beta>0\)、\(B>\max\{\beta,1\}\) 和 \(R=e^{-B}\)。在 \(a\ge0\) 定义
\[
g(0)=0,\qquad
g(a)=
\begin{cases}
a[\log(1/a)]^\beta,&0<a\le R,\\
R B^\beta,&a>R,
\end{cases}
\qquad
w(a)=a g(a),\qquad
h_{\rm rot}(a)=\sqrt{a^2+w(a)^2}.
\tag{LG.e1}
\]
窗内 \(g'(a)=[\log(1/a)]^\beta[1-\beta/\log(1/a)]>0\)，而
\(w'(a)=a[\log(1/a)]^\beta[2-\beta/\log(1/a)]>0\)。
窗外 \(g\) 为正的常数，\(w\) 线性增加；在接点连续。因而 \(w\) 和 \(h_{\rm rot}\) 都是 \([0,\infty)\) 上连续、严格递增的满射。固定
\[
\psi_\beta=w^{-1},\qquad
\Phi=0,\qquad
\varphi_\beta=h_{\rm rot}^{-1}\ \text{于 }[0,R].
\tag{LG.e2}
\]
原模全域有限、连续严格增、零点值为零，所指定目标在每个正尺度满足 \(0<\varphi_\beta(t)<t\)。

对任意满足这组 E0 的边，原真误差界给
\(w(a)\le\rho\le s\)，同一最近输入锚的能量给
\[
h_{\rm rot}(a)^2=a^2+w(a)^2
\le a^2+s^2\le t^2.
\tag{LG.e3}
\]
所以原数据认证预设 \(a\le\varphi_\beta(t)\)。这一步未使用下述某个固定图的法向递推；目标并非由剪切的额外结构冒名取得。

### LG2：完整旋转，精确零集为单点

令 \(H=\mathbb R^2\)、\(S_{\rm rot}=\{0\}\)，记 \(Q=R_{\pi/2}\)，定义全域单值
\[
F_{\rm rot}(y)=g(\|y\|)Qy.
\tag{LG.e4}
\]
它连续，非零点的值范数为 \(w(\|y\|)>0\)，故精确零集为 \(S_{\rm rot}\)。
\(I+F_{\rm rot}\) 将半径 \(a\) 变成 \(h_{\rm rot}(a)\)，并在该圆旋转固定角
\(\arctan g(a)\)。由于 \(h_{\rm rot}\) 是严格递增满射，完整近端全域唯一，并为同胚；给定 \(x\)，令 \(a=h_{\rm rot}^{-1}(\|x\|)\)，再用
\(y=(I+g(a)Q)^{-1}x\) 唯一反解。

对完整实际边有
\[
\rho=s=w(a),\qquad
\langle x-y,y\rangle=0,\qquad
a=\psi_\beta(\rho)=\varphi_\beta(t).
\tag{LG.e5}
\]
因而真误差界、预设目标和零锚能量在同一边取等。全部输入覆盖，零输入驻定，正距离窗不变。该图是 C420 通用构造在严格递增模上的一种明确写法；本页进一步计算其对数模和实际轨道。

### LG3：完整剪切，精确零集为直线

另取 \(H=\mathbb R^2\)、\(S_{\rm sh}=\mathbb R\times\{0\}\)，定义
\[
F_{\rm sh}(u,v)=
\begin{cases}
\bigl(-w(a),\ \operatorname{sgn}(v)w(a)^2/a\bigr),&a=|v|>0,\\
(0,0),&v=0.
\end{cases}
\tag{LG.e6}
\]
这是另一完整原图。\(w(a)\to0\)、\(w(a)^2/a=a^3[\log(1/a)]^{2\beta}\to0\)，故在零线连续；其精确零集为 \(S_{\rm sh}\)。令
\[
h_{\rm sh}(a)=a+\frac{w(a)^2}{a}=a[1+g(a)^2]\quad(a>0),\qquad h_{\rm sh}(0)=0.
\tag{LG.e7}
\]
因 \(g\) 非减，\(h_{\rm sh}\) 连续、严格递增且满射。完整输入的竖坐标为
\(\operatorname{sgn}(v)h_{\rm sh}(|v|)\)；先唯一反解竖坐标，再反解横坐标 \(x_1=u-w(a)\)，给全域唯一完整近端。

对输出 \(y=(u,v)\)，最近输入零锚为 \(p=(u-w(a),0)\)。直接得到
\[
\langle x-y,y-p\rangle=-w(a)^2+w(a)^2=0,\qquad
\rho=s=w(a)\sqrt{1+g(a)^2}\ge w(a).
\tag{LG.e8}
\]
故该图满足同一 \(\psi_\beta,\Phi=0\) 数据；原误差界未被说成取等。由 (LG.e3)，同一个预设目标 \(\varphi_\beta\) 仍获原 DD 认证。实际后继是
\(h_{\rm sh}^{-1}(t)\)，在正尺度严格小于 \(h_{\rm rot}^{-1}(t)\)，两者不混称。零线输入驻定，非零高度的符号保持，全部距离窗不变。对正高度实际轨道，
\[
t_k=h_{\rm sh}(t_{k+1}),\qquad
u_{k+1}-u_k=w(t_{k+1})>0 .
\tag{LG.e9}
\]
负高度有同一距离递推；以下取正高度表达具体轨道。

### LG4：两个完整图的非幂次距离与实际步

在任意 \(0<t_0\le R\) 出发的旋转轨道，或任意 \(u_0\in\mathbb R,0<t_0\le R\) 出发的剪切轨道，距离严格下降到零。若极限 \(l>0\)，相应连续径向函数将满足 \(h(l)=l\)，与 \(g(l)>0\) 矛盾。特别地，两种实际相邻距离比都趋 1。

写 \(\ell(t)=\log(1/t)\)，
\[
P(t)=t^{-2}\ell(t)^{-2\beta},\qquad
P'(t)=-2t^{-3}\ell(t)^{-2\beta}
       [1-\beta/\ell(t)] .
\tag{LG.e10}
\]
对输出 \(a=t_{k+1}\) 和输入 \(t=t_k\)，有 \(a/t\to1\)、\(\ell(a)/\ell(t)\to1\)。旋转满足
\(t-a=w(a)^2/(t+a)\sim\tfrac12a^3\ell(a)^{2\beta}\)；
剪切满足 \(t-a=a^3\ell(a)^{2\beta}\)。均值定理因而给
\[
P(t_{k+1})-P(t_k)\longrightarrow\sigma,\qquad
\sigma=
\begin{cases}1,&F_{\rm rot},\\2,&F_{\rm sh}.\end{cases}
\]
求增量平均得到 \(P(t_k)\sim\sigma k\)。对数化
\(2\ell(t_k)-2\beta\log\ell(t_k)=\log k+\log\sigma+o(1)\)，
所以 \(\ell(t_k)\sim\tfrac12\log k\)，进而
\[
t_k\sim\frac{2^\beta}{\sqrt{\sigma}}\,
        k^{-1/2}(\log k)^{-\beta},
\qquad
s_k\sim w(t_k)
\sim\frac{2^\beta}{\sigma}\,
        \frac1{k(\log k)^\beta}.
\tag{LG.e11}
\]
步长中的剪切额外因子 \(\sqrt{1+g(t_{k+1})^2}\to1\) 已保留后再取极限。以上是实际完整轨道的渐近等价，不是有限数值搜索或仅有上界。

### LG5：长度边界与无任何正幂的点率

由正项积分
\(\int^\infty dv/[v(\log v)^\beta]\)，两图每个上述正初始距离轨道的实际总长度有限，当且仅当 \(\beta>1\)。当 \(\beta>1\) 时，逐尾夹逼 (LG.e11) 得
\[
\mathcal L_k
\sim\frac{2^\beta}{\sigma(\beta-1)}(\log k)^{1-\beta}
\sim\frac{2}{\sigma(\beta-1)}
       [\log(1/t_k)]^{1-\beta}.
\tag{LG.e12}
\]
旋转始终有 \(x^k\to0\)，点误差就是 (LG.e11) 的 \(t_k\)；即使
\(0<\beta\le1\)，点收敛仍成立而长度无限。

剪切在 \(\beta>1\) 时有 \(u_k\to u_\infty\)、\(x^k\to(u_\infty,0)\)。
切移 \(w(t_{k+1})\) 与实际步比趋 1，故切向尾移和实际尾长同阶且等价；点误差被二者夹住。于是
\[
\|x^k-(u_\infty,0)\|
\sim\mathcal L_k
\sim\frac{2^{\beta-1}}{\beta-1}(\log k)^{1-\beta}.
\tag{LG.e13}
\]
对每个 \(p>0\)，该实际点误差乘 \(k^p\) 趋无穷，故不存在任何正幂
\(O(k^{-p})\) 的点误差率。距离却仍有 (LG.e11) 的幂次乘对数率。若 \(0<\beta\le1\)，切向增量不可和且恒正，故 \(u_k\to+\infty\)：剪切轨道距离趋零而沿零线逃逸。两分支的零集、点结论和尾常数不互相转授。

### LG6：原误差模、积分判据和统一类范围

由 \(\rho=w(a)=a^2[\log(1/a)]^\beta\) 反解，
\[
\psi_\beta(\rho)\sim
2^{\beta/2}\rho^{1/2}
[\log(1/\rho)]^{-\beta/2}
\quad(\rho\downarrow0).
\tag{LG.e14}
\]
例如取对数先得 \(\log(1/a)\sim\tfrac12\log(1/\rho)\)，再回代即得常数。
对任何 \(q>1/2\)，\(\psi_\beta(\rho)/\rho^q\to\infty\)；
旋转的误差界取等，而剪切的真实 \(\rho\sim w(a)\)，故两图都不具有这个 \(q\) 的任何局部 Hölder 真误差界常数。不能将 \(\beta>1\) 的有限长度简单归入 [C399](../../canonical/dd2_power_defect_finite_length.md#dd2-power-defect) 某个 \(q>1/2\) 的实例。

令 \(\chi_\beta=(\operatorname{id}+\psi_\beta)^{-1}\)。
写 \(b=\psi_\beta(\chi_\beta(t))\)，则
\(t=b+w(b)\)、\(\chi_\beta(t)=w(b)\)。由 \(w(b)/b=g(b)\to0\) 得
\(b/t\to1\)，进而 \(w(b)/w(t)\to1\)，所以
\[
\chi_\beta(t)\sim t^2[\log(1/t)]^\beta .
\tag{LG.e15}
\]
当 \(\beta>1\) 时，原 [C401](core.md#dd2-general-gauge) 势有限，且
\[
\Theta_\beta(t)=\int_0^t\frac{u}{\chi_\beta(u)}\,du
\sim\frac{[\log(1/t)]^{1-\beta}}{\beta-1}.
\tag{LG.e16}
\]
当 \(0<\beta\le1\) 时，该积分在每个正上限发散。这里只用正函数在足够小尾部的相对误差夹逼和换元，不依赖未声明的渐近反演定理。(LG.e12) 也给旋转
\(\mathcal L_k\sim2\Theta_\beta(t_k)\)、剪切
\(\mathcal L_k\sim\Theta_\beta(t_k)\)，均只作为本模型的实际常数。

固定这个 \(\beta,B,\psi_\beta,\lambda=1\)，在 C420 所述的、包含二维空间的自由闭目标普通 PPA 统一类中，要求 \(U=H\)、全距离窗覆盖、每条允许边有非负最近输入锚积、完整真误差界。则“该类每个算子的全部允许轨道都有限长”恰等价于 \(\beta>1\)。充分性由 (LG.e15)–(LG.e16) 和 C401/C420 的 \(\delta=1\) 版本；必要性由 \(\beta\le1\) 的上述完整旋转或剪切实际轨道。同一统一类中，\(\varphi_\beta\) 连续非减，原证书与覆盖给 \(t_k\le\varphi_\beta^{\circ k}(t_0)\le\varphi_\beta^{\circ k}(R)\)，中项和最右项分别是旋转从初半径 \(t_0\) 和 \(R\) 出发的实际距离。因此这些合法轨道统一获得 \(O(k^{-1/2}(\log k)^{-\beta})\) 的距离率；\(\beta>1\) 时 C401 的 \(2\Theta_\beta(t_k)\) 又给 \(O((\log k)^{1-\beta})\) 的尾长和点误差界。剪切说明不能统一改为任意正幂的点误差率。一般开 \(U\) 的充分使用仍保
\(2\Theta_\beta(t_0)<d(x^0,U^c)\)。这不是每个固定算子有限长的必要条件，也不把必要性转授正 \(\Phi\)、指定更强目标或别的受限类。

<a id="dd2-nonpower-scope"></a>
## 3. 与幂次、上包络和当前开放问题的关系

C400 的平方对数计步曲线在固定线性误差界下给非几何、快于所有幂次的点率；C451 的剪切在零缺陷、对数强化的半阶模下给有限长度却慢于所有正幂的点率。两者不是同一组原数据或同一个算子。它们证明 DD2 的函数对象有真实动力学内容，不需要假设所有函数都能被一个幂指数精确表示。

C451 的旋转及剪切由同一 \(\psi_\beta,\Phi=0\) 认证同一目标 \(\varphi_\beta\)，但使用不同指定零集；只有旋转逐尺度取等。其完整单值实例与 [C10 的几何距离—对数切移族](../../canonical/general_modulus_dynamics.md#gm-log-object)、[C424 的纯幂误差模—临界缺陷余量族](../../canonical/dd2_power_defect_finite_length.md#dd2-vanishing-budget)也不同。

用较松模包住原模只能给另一份充分证书。该包络必须实际存在、在所需域有限且满足其定理的条件；再核原 \(\Phi\) 的吸收、原预设目标和新积分。C451 的 \(\beta>1\) 原势有限，但在零端放宽到常数倍 \(\sqrt{\rho}\)，所得势发散，有限长证书会丢失。保留原非单调 \(\rho\) 的联合域版本和已有 C419 的位移下界版本仍是各自独立路线，不要求先把原函数改成幂函数或连续非减函数。

本页未关闭[非绝对可和点收敛的当前文章主问题](../../manuscripts/dd2/DD2_outline_and_pro_handoff.md#dd2-nonabsolute-main-task)。\(\beta>1\) 的剪切靠有限长度；\(\beta\le1\) 的旋转靠单点目标，剪切反而逃逸。原问题所要求的非平凡方向或跨步机制及匹配失效侧仍另行研究。
