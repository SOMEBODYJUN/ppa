# 合法路径、块收缩与整条轨道

本模块从 2026-09-09 的多步札记重新建立可调用的定理。历史文本给出路径图集、块 RL 和有限捕获的思路；下面的量词、延拓条件和周期结论以本页为准。这里的 `PA` 身份与历史复合次正则 `C11` 无关。文献新颖性未审定。

<a id="pa-def"></a>
## PA-DEF · 对象和合法路径

令 \(X=\mathbb R^n\)，\(S\subset X\) 非空闭，\(V\subset X\) 开，\(m\ge1\)。一条合法长度 \(m\) 路径是
\(x_0,x_1,\ldots,x_m\)，其中每个转移遵守指定的模式、相位和分支邻接规则。合法词集 \(\mathcal W_m\) 可以无限；不能用各步可能转移的笛卡儿积代替它。所有下述上界量化于**每条**合法路径，而非某个有利选择。若只有存在性选择，则必须另立命题。

对 \(w\in\mathcal W_m\) 和 \(0\le j\le m\) 给非负、非减函数 \(D_{w,j}\)，对 \(j<m\) 给非负、非减函数 \(G_{w,j}\)，令 \(D_{w,0}(t)=t\)。路径从 \(x\) 出发且 \(t=d(x,S)\) 时，要求每个已存在前缀满足
\[
d(x_j,S)\le D_{w,j}(t),\qquad
\|x_{j+1}-x_j\|\le G_{w,j}(t).
\]
这套条件应由真实图、模式和覆盖证明；仅给出终点 \(T^m\) 的公式不够。模式转移写作 \(x_{j+1}\in T_{\sigma_j}(x_j)\)；若合法性依赖已经走过的词，覆盖条件的状态也包含该前缀或相位，不能只检查裸点 \(x_j\)。定义统一包络
\[
G(t)=\sup_{w\in\mathcal W_m}\sum_{j=0}^{m-1}G_{w,j}(t),
\qquad \Theta(t)=\sup_{w\in\mathcal W_m}D_{w,m}(t).
\]
终点 \(D_{w,m}\) 可以来自联合分支计算，不必等于逐步最坏界的合成。要求这些包络在本定理的半径内有限。

<a id="pa-step"></a>
### RL 如何实际产生步位移界

若每个可达模式转移 \(x_j\mapsto x_{j+1}\) 都有某个最近点
\(p_j\in P_S(x_j)\)，满足
\[
\|2x_{j+1}-x_j-p_j\|\le\omega_{\sigma_j}(d(x_j,S)),
\]
其中 \(\omega_\sigma\) 非负非减，则
\[
2(x_j-x_{j+1})=(x_j-p_j)-(2x_{j+1}-x_j-p_j)
\]
给出
\[
\|x_{j+1}-x_j\|
\le\frac{d(x_j,S)+\omega_{\sigma_j}(d(x_j,S))}{2}
\le\widehat G_{w,j}(t):=
\frac{D_{w,j}(t)+\omega_{\sigma_j}(D_{w,j}(t))}{2}.
\]
因此可**取** \(G_{w,j}=\widehat G_{w,j}\)，或取任意更大的非减函数。
另一条直接证明若给出更小的有效 \(G_{w,j}\)，当然也可采用。
历史式 (2.12) 单独写 \(G_{w,j}\le\widehat G_{w,j}\) 不能认证一个任意候选
\(G_{w,j}\)；小于已知上界的数未必仍大于实际步长。
若模式比较只在某个距离窗有效，所有 \(D_{w,j}(t)\) 也必须处于该窗。
这里的 \(p_j\) 可依赖实际转移，无需各边共享同一最近点。

<a id="pa-lift"></a>
## PA-LIFT-v1 · 完整块关系、resolvent 与全对反射

先固定真正要分析的**全部合法末点关系**
\[
\mathcal B_m(x)=\{y:\text{存在从 }x\text{ 到 }y\text{ 的合法长度 }m\text{ 路径}\}.
\]
本段固定块边界的相位/记忆条件；若不同边界条件给出不同关系，须分别标记。
若另用增广状态编码相位/记忆，状态空间和度量也要重新声明。
只在原空间编码末点时，跨块允许的重启规则仍须另证。
对 \(\Lambda>0\)，定义完整关系
\[
\mathcal F_{m,\Lambda}(y)
=\{(x-y)/\Lambda:x\in X,\ y\in\mathcal B_m(x)\}.
\]
则作为集合值关系，在所有输入上精确成立
\[
J_{\Lambda\mathcal F_{m,\Lambda}}(x)
:=(I+\Lambda\mathcal F_{m,\Lambda})^{-1}(x)
=\mathcal B_m(x),\qquad
\operatorname{zer}\mathcal F_{m,\Lambda}=\operatorname{Fix}\mathcal B_m.
\]
**证明。** \(y\in J_{\Lambda\mathcal F}(x)\) 等价于存在 \(v\in\mathcal F(y)\)
使 \(x=y+\Lambda v\)。由图的定义存在 \(\tilde x\) 使
\(v=(\tilde x-y)/\Lambda\)、\(y\in\mathcal B_m(\tilde x)\)；该等式迫使
\(\tilde x=x\)。逆向取 \(v=(x-y)/\Lambda\) 即可。
取 \(v=0\) 同理得到零集等式；空输入纤维也包含在等式中。\(\square\)

固定输入片 \(U\subset X\)、\(0<L<\infty\)、\(\gamma>0\)。在输入
\(x=y+\Lambda v\in U\)、\(x'=y'+\Lambda v'\in U\) 对应的**全部**图点上，AP-RL 条件
\[
\|(y-y')-\Lambda(v-v')\|
\le L\|(y-y')+\Lambda(v-v')\|^\gamma
\]
等价于
\[
\|2(y-y')-(x-x')\|\le L\|x-x'\|^\gamma
\quad(y\in\mathcal B_m(x),\ y'\in\mathcal B_m(x')).
\]
证明只需代入 \(\Lambda v=x-y\)；前一证明保证这代换双向覆盖全部纤维。
同输入 \(x=x'\) 时得到 \(2\|y-y'\|\le0\)，所以每个输入**至多**有一个输出。
它不保证每个 \(x\in U\) 都有输出：空关系已满足全对不等式。
还须另证 \(U\subset\operatorname{dom}\mathcal B_m\)，才能在整个 \(U\) 上称单值映射。
唯一末点也不使内部合法路径唯一。

只有已经证明合法路径恰好枚举 \(T\) 的全部 \(m\) 步路径时，才可写
\(\mathcal B_m=T^m\)。任意受限词或选定分支一般只给子关系；为它反向编码的
\(\mathcal F_{m,\Lambda}\) 不是原生生成算子的身份或完整纤维证明。
在 \(\mathcal B_m=T^m\) 情形，零集为 \(\operatorname{Fix}T^m\)，不自动等于
\(\operatorname{Fix}T\)。欲以原固定集 \(S\) 调用以零集为目标的块次正则性，须证明实际输出窗上的
距离目标对齐。一项可用的集合身份检查是
\(\operatorname{Fix}T^m\cap V=\operatorname{Fix}T\cap V=S\cap V\)；若只使用更小的窗口，
可在该相关窗口核身份，不把整个 \(V\) 的集合等式列为必要条件。仅有集合在 \(V\) 内相等，
也不自动使整个 \(V\) 上到两全局集合的距离相等。
例如 \(V=(-1,1)\)、\(S=\{0\}\)、\(Z'=\{0,1.01\}\) 在 \(V\) 内相等，
而 \(y=0.99\) 满足 \(d(y,S)=0.99\)、\(d(y,Z')=0.02\)。
下节若直接假设以 \(S\) 为目标的输出界，则无需从零集等式推导该界。

<a id="pa-whole"></a>
## PA-WHOLE-v1 · 局部整轨道定理

**精确陈述。** 固定 \(r,\eta>0\)、\(0\le\kappa<1\)。对所有从 \(V\) 中 \(d(x,S)\le r\) 的块起点和所有合法前缀，假设：

1. 前缀有至少一个合法下一步；任何允许的下一步都属于某个合法完整词，遵守上面的 \(D,G\) 界。此延拓条件在前缀位于 \(V\)、距离 \(S\) 小于 \(\eta\) 时成立。块边界也允许重新选词；任意选取均有相同界。
2. 对 \(t\in[0,r]\) 和所有 \(w,j<m\)，\(D_{w,j}(t)<\eta\)，且 \(\Theta(t)\le\kappa t\)。
3. \(H(t):=\sum_{q=0}^{\infty}G(\kappa^q t)<\infty\) 对 \(t\in[0,r]\) 成立。

当 \(\kappa=0\) 时，约定第 \(q=0\) 项的 \(\kappa^q t=t\)，以后各项的参数为0。

若 \(x_0\in V\)、\(d_0=d(x_0,S)\le r\)，并且
\[
H(d_0)<\operatorname{dist}(x_0,X\setminus V)
\quad(\operatorname{dist}(x_0,\varnothing)=+\infty),
\]
则每条由允许转移构造的轨道可无限延拓，停留在 \(V\)，且
\[
d(x_{qm},S)\le\kappa^q d_0,\qquad
\sum_{k\ge0}\|x_{k+1}-x_k\|\le H(d_0).
\]
特别地，**整条**轨道收敛于 \(S\) 中一点，且从块 \(q\) 起的长度至多 \(H(\kappa^q d_0)\)。这是有限维陈述；在指定完备的赋范空间中相同证明也成立，只要闭集和距离等约定保留。

**证明。** 设第 \(q\) 个块起点已构造，且 \(t_q\le\kappa^q d_0\)。由前缀延拓和 \(D_{w,j}(t_q)<\eta\) 可逐步构造完整合法词；该块的长度至多 \(G(t_q)\le G(\kappa^q d_0)\)，终点距离至多 \(\kappa t_q\)。每个有限前缀到 \(x_0\) 的距离不超过前面块和当前部分块的长度之和，不超过 \(H(d_0)\)，故严格的边界预算使它始终在 \(V\)。于是归纳可以继续。各块相加给有限总长，轨道 Cauchy；\(\mathbb R^n\) 完备使其有极限。块端点距离趋零，而 \(S\) 闭，故极限在 \(S\)。尾界同理由非减性给出。\(\square\)

**使用限制。** 半径 \(r\) 和 \(\eta\) 的覆盖必须对实际中间状态成立；仅有块端点收缩、或仅有每个词各自的常数，不满足本陈述。\(H(0)<\infty\) 迫使 \(G(0)=0\)，因此本定理不容许零集上的非零周期位移。

<a id="pa-block"></a>
## PA-BLOCK-v1 · 块 RL 与输出误差界的接口

固定 \(\Lambda>0\)。对每个合法块 \(x=x_0\mapsto y=x_m\) 选 \(p\in P_S(x)\)；若同一块满足
\[
\|2y-x-p\|\le\omega(d(x,S)),\qquad
d(y,S)\le\psi(\|x-y\|/\Lambda),
\]
其中 \(\omega,\psi\) 非负非减，在声明窗口内全部求值有定义，便有
\[
\|x-y\|\le B(t),\quad d(y,S)\le\rho(t),\quad
B(t)=\frac{t+\omega(t)}2,\quad
\rho(t)=\min\{B(t),\psi(B(t)/\Lambda)\},\quad t=d(x,S).
\]
证明是 \(2(y-p)=(2y-x-p)+(x-p)\) 与 \(2(x-y)=(x-p)-(2y-x-p)\) 的三角不等式；再用 \(\psi\) 单调。
来源还要求 \(\omega(0)=\psi(0)=0\)，这些零值条件可保留，但上面代数本身无需它们。
若 \(\rho(t)\le\kappa t\)，它只给 PA-WHOLE 的**终点**前件，仍须独立验证中间路径的覆盖、\(D,G\) 和可求和预算。

普通块残差条件如何产生输出界也可直接核：若同一实际输出窗有
\[
d(y,S)\le\psi(r_{\mathcal F}(y)),\qquad
r_{\mathcal F}(y):=\inf_{v\in\mathcal F_{m,\Lambda}(y)}\|v\|,
\]
则每个合法块的选中值 \((x-y)/\Lambda\) 属于完整纤维，故
\(r_{\mathcal F}(y)\le\|x-y\|/\Lambda\)，由单调性即得所需界，无需最小残差取到。
反过来，算法只在部分实际块上验证的输出界并不授予完整输出邻域的普通次正则性。
如果已经对某个 \(y\) 的**所有**完整纤维值验证该界，且 \(\psi\) 在真实残差处右连续，
则可以沿趋近最小残差的序列取极限，得到该 \(y\) 的真残差界；这一步不能从选定路径省略。
图被截取后得到的残差和完整原生算子的残差也不能互换。
对块 \(\mathcal F_{m,\Lambda}\) 的身份和零集要求见 PA-LIFT；整个推导不需要
\(\psi\) 被某个幂函数支配，也不单独产生输入覆盖。

<a id="pa-capture"></a>
## PA-CAPTURE-v1 · 有限进入与停机的准确区别

给定初值 \(x_0\in V\)、\(t_0=d(x_0,S)\)，假设首个块的每个合法前缀满足
PA-DEF 的距离/位移界、实际前缀覆盖与延拓条件，且
\[
D_{w,j}(t_0)<\eta\quad(j<m),\qquad
L_0:=\sup_w\sum_{j<m}G_{w,j}(t_0)<\operatorname{dist}(x_0,X\setminus V).
\]
若每条完整合法长度 \(m\) 路径均有 \(x_m\in S\)，则每条允许轨道都能构造到
第 \(m\) 步，首块留在 \(V\)，在不超过 \(m\) 步进入 \(S\)，首块总长至多 \(L_0\)。
证明为有限归纳：在任何已构造前缀上，距离界使覆盖有效，下一步位移的部分和不超过
\(L_0\)，故下一状态仍在 \(V\)；逐步继续到 \(m\) 后应用末点身份。
对整片初值若都已核这样的首块条件，可以选终点 gauge \(D_{w,m}\equiv0\)、\(\Theta\equiv0\)，
无需无限级数预算，也无需 RL；RL 是获得某种可用步位移界的一条途径。

若 \(S\) 对所有允许后续转移**吸收**（每个后继仍在 \(S\)），只能推出已经可延拓的
后续路径不再离开 \(S\)。它本身不保证后续留在 \(V\)、存在下一步、有限总长或点收敛。
例如 \(X=\mathbb R\)、\(S=\{-1,1\}\)、\(T(x)=-1\) 当 \(x\ge0\)，
\(T(x)=1\) 当 \(x<0\)，每个输入一步进入吸收集 \(S\)，而从 \(1\) 出发永远在
\(1,-1\) 间往返。停止规则“首次进入 \(S\) 即停”会有限停机；若要求继续迭代后保持固定，
须另假设每个目标点至少有一步且**全部**允许后继等于它本身。
在这个驻定目标条件下，轨道第 \(m\) 步起恒定，总长至多 \(L_0\)，极限就在 \(S\cap V\)。
历史 §3.3 中的“termination”只按这两种明确含义使用，不能仅由吸收性授予驻定结论。

<a id="pa-power"></a>
## PA-POWER-v1 · 合法词的幂次与统一性

若词 \(w=(\sigma_0,\ldots,\sigma_{m-1})\) 的第 \(j\) 步有 \(d_{j+1}\le c_{\sigma_j}d_j^{\alpha_{\sigma_j}}\)，\(c_{\sigma_j}>0,\alpha_{\sigma_j}>0\)，则
\[
d_m\le C_w d_0^{A_w},\qquad
A_w=\prod_{j=0}^{m-1}\alpha_{\sigma_j},\qquad
C_w=\prod_{j=0}^{m-1}c_{\sigma_j}^{\prod_{\ell=j+1}^{m-1}\alpha_{\sigma_\ell}}.
\]
空乘积约为1。证明按长度归纳：若前 \(j\) 步的系数和指数是 \(C_j,A_j\)，
代入第 \(j\) 边得 \(C_{j+1}=c_{\sigma_j}C_j^{\alpha_{\sigma_j}}\)、
\(A_{j+1}=A_j\alpha_{\sigma_j}\)，从 \(C_0=A_0=1\) 递推即得公式。
对有限合法词集，所有 \(A_w>1\) 确有共同充分小的半径使 \(C_wt^{A_w}\le\kappa t\)，其中先固定任意 \(0<\kappa<1\)。对无限词集，充分条件是 \(\inf_w A_w>1\) 且 \(\sup_w C_w<\infty\)（取 \(0<t\le r<1\)，再选 \(r\)）。若某些 \(A_w=1\)，还须其 \(C_w\le\kappa<1\) 并统一控制其余词；\(A_w<1\) 的**这项上界**在任意小尺度上不能证明线性块收缩，但实际路径可能因联合恒等式有限捕获。

逐词 \(A_w>1\) 本身并无统一半径：长度 \(m=1\)，\(A_j=1+1/j,C_j=1\)，则对任何固定 \(0<t<1\)，\(\sup_j t^{A_j}=t\)。这是否定历史札记 §4 无限定量词版本的反例，而非否定每个固定词的估计。

“\(\alpha_\sigma=\gamma_\sigma q_\sigma\)”是特定单步生产器的记账，须写出其门：
若 \(0<\gamma_\sigma<1\)、\(L_\sigma\ge0\)、\(a_\sigma,q_\sigma>0\)、
\(\omega_\sigma(t)=L_\sigma t^{\gamma_\sigma}\)、\(\psi_\sigma(s)=a_\sigma s^{q_\sigma}\)，
且同一步长为 \(\lambda_\sigma>0\)，则在共同 \(0\le t\le r\)、\(r>0\) 上
\[
B_\sigma(t)\le b_\sigma t^{\gamma_\sigma},\quad
b_\sigma=\tfrac12(r^{1-\gamma_\sigma}+L_\sigma),\qquad
d^+\le a_\sigma(b_\sigma/\lambda_\sigma)^{q_\sigma}
t^{\gamma_\sigma q_\sigma}.
\]
这是 PA-BLOCK 在 \(m=1\) 的 EB 分量给出的上界，另一个分量仍是
\(d^+\le b_\sigma t^{\gamma_\sigma}\)。它不是实际收敛阶或最佳指数的身份；全部求值窗、
词的统一性与中间预算仍须核验。有限捕获的联合末点 gauge 可为0，严格优于这些分离幂界。
若只有某个内部边使状态进入 \(S\)，还须后续每条允许转移保持 \(S\)，才能把整个块的末点界置零；
没有这项吸收门，中间进入不能替代末端进入。

<a id="pa-cycles"></a>
## PA-CYCLES-v1 · 相位极限的另一种命题

对确定的周期映射 \(T_0,\ldots,T_{m-1}\)，置 \(C=T_{m-1}\circ\cdots\circ T_0\) 与 \(P_j=T_{j-1}\circ\cdots\circ T_0\)，\(P_0=I\)。若**另已证明** \(C^q x_0\to\bar x_0\in\operatorname{Fix}C\)，且每个 \(P_j\) 在 \(\bar x_0\) 连续，则 \(x_{qm+j}=P_j(C^qx_0)\to\bar x_j=P_j\bar x_0\)。这是有限前缀恒等式和连续性的直接应用。
整条轨道若收敛，各相位子列必有同一极限；反过来若各相位极限相同，对任意误差阈值取这有限 \(m\) 个子列所需块序号的最大值，便得到整列收敛。
这里不调用 PA-WHOLE；非平凡周期一般有不消失的块内位移，和它的有限总长结论不相容。例如 \(T(x)=1-x\) 使 \(T^2=I\)，任意 \(x\ne1/2\) 在两点间往返，而 \(\operatorname{Fix}T^2=\mathbb R\ne\operatorname{Fix}T\)。

<a id="pa-source"></a>
## 证据、限制与下一步

- 本页的代数、统一性反例和 PA-WHOLE 证明为本仓库重写并独立核算；状态 `derived-checked`，不含新颖性或外部优先权判断。
- 原件524个物理LF行现已[全部逐断言枚举](../audit/PATH_FULL_COVERAGE.md#path-full)；全件枚举与原生身份、外部版本/优先权的证明义务分开。
- 来源线索：[2026-09-09 多步路径札记](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/多步路径与有限捕获_RL研究札记_2026-09-09.md) §2–§5。§5 给定单值映射的半径与两步捕获以及较晚审计的一步锐因子，现由 [C38/C39](../topics/path_dynamics/m1_capture.md) 独立重算；原生多值图身份未闭；[固定外部接口](c11_m1_literature_interfaces.md)已逐版本核已访问声明，全文/刊本与原生对应仍有具体门，不作为本页抽象定理的证据。
- 下一个高信息量任务：从原始多值广义方程重算 M1 的合法分支及两步捕获半径，再明确区分“每条合法选择”与“存在一条选择”；同时按上述一手卡匹配已核组合/Fejér接口和仍未闭的全文、目标/残差/metric及原生选择条件。
