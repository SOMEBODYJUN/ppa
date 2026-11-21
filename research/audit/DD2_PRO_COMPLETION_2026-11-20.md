# DD2 GPT-Pro 验收补充：覆盖、矩阵门、非幂扰动与分布式能量

<a id="dd2-pro-scope"></a>
## 0. 作用域与状态

本文固定普通近端图的同一约定：

- \(H\) 是有限维实 Hilbert 空间，\(\lambda>0\)，\(S\subseteq\operatorname{zer}F\) 非空闭；
- \(G=(F^{-1}-I)^{-1}\) 是把图值写成位移的剪切关系，故 \(q\in G(y)\) 等价于 \(x=y+q\) 且 \(y\in J_{\lambda F}(x)\)（把 \(\lambda\) 吸收入 \(q\) 时按文中约定缩放）；
- \(r_G(y)=\inf\{\|q\|:q\in G(y)\}\) 的 infimum 取完整图值，允许关系 \(\mathcal J\) 可以只是完整图的子关系；
- \(t=d(x,S)\)、\(a=d(y,S)\)、\(s=\|q\|\)，最近输入锚 \(p\in P_S(x)\) 满足
  \[
  \langle q,x-p\rangle=\langle q,y-p\rangle+\|q\|^2\ge \beta s^2-D(t).
  \tag{P0}
  \]

本文件只登记本轮新核对的命题、证明和反例。它不把“选定分支上的输出界”升级为“完整真残差界”，也不把比较级的必要预算升级为某个算子类的普遍必要定理。

<a id="dd2-pro-coverage"></a>
## 1. 完整图覆盖的精确门与弱化不可能性

### 命题 P2-A（近极小图值 lift 足以恢复完整真残差）

设 \(U\subset H\) 是工作窗，\(\psi:[0,\infty)\to[0,\infty)\) 连续、非减、\(\psi(0)=0\)。设允许边集 \(\mathscr E\subset H\times H\) 满足：

1. 对每个 \(x\in U\) 至少有一个 \((x,y)\in\mathscr E\)，并且该边属于完整近端图；
2. 对每个 \((x,y)\in\mathscr E\)，存在 \(p\in P_S(x)\) 使 (P0) 成立，且
   \[
   d(y,S)\le \psi(\|q\|),\qquad q=x-y;
   \tag{P1}
   \]
3. **近极小 lift 条件**：若 \(y\in H\) 满足 \(d(y,S)\) 小于工作窗半径，\(q\in G(y)\) 且 \(\|q\|\le r_G(y)+\varepsilon\)，则 \(x=y+q\in U\)，并且 \((x,y)\in\mathscr E\)；同一 \(y\) 的零锚条件对这条边成立。

则在该窗内
\[
 d(y,S)\le \psi(r_G(y)).
 \tag{P2}
\]
若完整图值的 infimum 不达到，只需把“\(\|q\|\le r_G(y)+\varepsilon\)”理解为每个 \(\varepsilon>0\) 存在这样的 \(q\)。

**证明。** 固定 \(y\) 和 \(\varepsilon>0\)，按近极小 lift 取 \(q_\varepsilon\) 和边 \((x_\varepsilon,y)\in\mathscr E\)。由 (P1)
\[
 d(y,S)\le\psi(\|q_\varepsilon\|)\le\psi(r_G(y)+\varepsilon).
\]
令 \(\varepsilon\downarrow0\)，由 \(\psi\) 连续得到 (P2)。注意证明只使用输出点 \(y\) 的距离；零锚可随 \(\varepsilon\) 改变，不能在没有额外条件时把它固定成同一个 \(p\)。

### 反例 P2-A-1（只选一支不能推出完整残差界）

在 \(H=\mathbb R\) 取 \(S=\{0\}\)，
\[
 G(y)=\{y,y^3\},\qquad y\in\mathbb R.
\]
完整近端输入为 \(x=y+q\)，所以第一支 \(q=y\) 给出对每个 \(x\) 的允许边 \(y=x/2\)，覆盖全域；第二支的输入为 \(x=y+y^3\)，也连续覆盖。若允许关系只选第一支，则
\[
 d(y,S)=|q|,
\]
从而选定分支具有线性输出界。完整真残差却为
\[
 r_G(y)=\min\{|y|,|y|^3\}=|y|^3\quad (|y|\le1),
\]
故不存在任何局部常数 \(K\) 使 \(d(y,S)\le K r_G(y)\)。图是闭的，完整输入覆盖也成立；失败只来自量词没有覆盖第二支。由 \(G\) 反剪切得到的 \(F\) 是一个合法的集合值近端图，因此这不是抽象点集伪例。

### 推论 P2-A-2（只约束近极小残差的最弱可用版本）

若工作算法不要求每个完整图值均可选，但要求对每个 \(y\) 和每个 \(\varepsilon>0\) 至少存在一个近极小 \(q_\varepsilon\) 满足 (P2-A) 的输入覆盖和选定边条件，则完整真残差界仍成立。若该条件只在一列算法输出上成立，则只能得到这列输出的逐点界，不能把结论写成完整 \(r_G\) 界。

**证明义务的边界。** 近极小 lift 条件是一个存在量词；它不要求图值唯一，也不要求所有图值都满足 (P1)。如果希望使用“所有允许边”的 DD2 距离递推，则必须把 \(\mathscr E\) 本身的每条边都纳入 (P1)，并另列覆盖。若仅知道每个 \(y\) 存在一个好值，却允许算法选择任意坏值，距离递推不成立。

<a id="dd2-pro-matrix"></a>
## 2. 非线性原始—对偶块的可计算矩阵门

### 命题 P2-B（完成平方与半正定可计算证书）

令
\[
 \mathcal K=\begin{pmatrix}0&L^*\\-L&0\end{pmatrix},\qquad
 M=M^*,\quad N=N^*,\quad W=W^*\succ0.
\]
假设对相对于同一零锚 \(x_*\) 的每个完整块图点 \(x=x_*+d,\ y\in T(x)\) 有
\[
 \langle d,y\rangle\ge \langle d,Md\rangle
 +\langle y-\mathcal Kd,N(y-\mathcal Kd)\rangle .
 \tag{P3}
\]
定义
\[
 V=N-W,\qquad
 U=M+\mathcal K^*(N-NW^{-1}N)\mathcal K.
 \tag{P4}
\]
则
\[
 \langle d,y\rangle\ge\langle d,Ud\rangle+\langle y,Vy\rangle,\tag{P5}
\]
且差额精确等于
\[
 \langle d,y\rangle-\langle d,Ud\rangle-\langle y,Vy\rangle
 =\|W^{1/2}y-W^{-1/2}N\mathcal Kd\|^2\ge0 .\tag{P6}
\]

**证明。** 展开右端的平方：
\[
 \|W^{1/2}y-W^{-1/2}N\mathcal Kd\|^2
 =\langle y,Wy\rangle-2\langle y,N\mathcal Kd\rangle
 +\langle \mathcal Kd,NW^{-1}N\mathcal Kd\rangle .
\]
把它加到 (P4) 的两项即得到 (P3) 的右端。

### 半正定门

若 \(P=CC^*\) 是退化预条件器，DD2 的同一步耗散只需核验
\[
 U+\sigma P\succeq0,\qquad C^*VC\succeq \eta I_{\operatorname{ran}P},\qquad \eta>-1/2,\tag{P7}
\]
以及实际边的锚条件
\[
 \langle d,Ud\rangle\ge D_+(x,y,x_*)-M_0t^p,\qquad D_+\ge0.\tag{P8}
\]
于是对 \(q=C^{-1}y\) 有
\[
 t^2-a^2\ge (1+2\eta)\|q\|^2+2D_+-2M_0t^p,\tag{P9}
\]
在 \(1+2\eta>0\) 时可直接接入 C399/C401 的 \(\chi\)-势证明。若只知道 \(U\succeq-\sigma P\)，负位置项是 \(O(t^2)\)，除非另有 \(p>2\) 的尺度吸收或局部正半定补偿，不能把它当作零缺陷。

### 可计算性

对给定有限维块 \(M,N,\mathcal K,P\)，寻找最大的方向余量可以写成半正定可行问题：
\[
 \eta_*=\sup_{W\succ0,\ \sigma\ge0}
 \{\eta:\ C^*(N-W)C\succeq\eta I,\quad
 M+\mathcal K^*(N-NW^{-1}N)\mathcal K+\sigma P\succeq0\}.
 \tag{P10}
\]
第二个约束等价于 Schur 补门
\[
 \begin{pmatrix}
 W&N\mathcal K\\
 \mathcal K^*N&M+\mathcal K^*N\mathcal K+\sigma P
 \end{pmatrix}\succeq0 .\tag{P11}
\]
因此 \(W\) 的选择、可认证的最小 \(\beta_k\) 与实际 \(\alpha_k\) 是三种不同观察量：\(\beta_k\) 是当前 \(q_k\) 的 Rayleigh 商，(P10) 是一步前可离线认证的矩阵下界，\(\alpha_k\) 只需满足 \(0<\alpha_k\le2\beta_k\) 并保留正余量。任何把三者写成同一个“可计算参数”的表述都改变了量词。

### 退化临界例

取 \(N=0\)、\(M=0\)、\(W=I\)。则 \(U=0,V=-I\)，在 \(P\)-值域上 \(\eta=-\|C\|^2\)；若 \(\eta\le-1/2\)，(P9) 没有正耗散。即使复合算子本身有误差界，实际松弛也可能放大（见 splitting.md 中 A=-3I/4,B=I/4 的 DR 例）。这说明矩阵门和复合误差界必须同时核验，不能只检查原始 \(A+L^*B L\) 的正则性。

<a id="dd2-pro-theta"></a>
## 3. 一般 Θ 的扰动锐性与物理恢复

### 命题 P3-A（势增量是比较级的必要扰动预算）

设 \(\Theta:[0,R]\to[0,\infty)\) 连续非减、\(\Theta(0)=0\)，且精确同一步几何给出
\[
 \ell_k\le C\,[\Theta(\tau_k)-\Theta(a_k)],\qquad
 \tau_k\le r_k+\eta_k,\tag{P12}
\]
其中 \(r_k\) 是实际输入到目标的距离，\(\tau_k\) 是未扰动图边的输入距离，\(\eta_k=\|e_k\|\) 是输入扰动。则
\[
 \ell_k\le C[\Theta(r_k)-\Theta(a_k)]
 +C\,\Delta_\Theta(r_k,\eta_k),\quad
 \Delta_\Theta(r,\eta):=\Theta(r+\eta)-\Theta(r).
 \tag{P13}
\]
因而
\[
 \sum_k\Delta_\Theta(r_k,\eta_k)<\infty\tag{P14}
\]
连同 C401 的精确下降和有限前缀留域预算，足以把无扰动有限长度、点收敛及极限识别传给受扰轨道。

**证明。** 由 \(\Theta\) 非减和 \(\tau_k\le r_k+\eta_k\)，\(\Theta(\tau_k)\le\Theta(r_k+\eta_k)\)。再将右端写成 \(\Theta(r_k)-\Theta(a_k)+\Delta_\Theta(r_k,\eta_k)\) 即得 (P13)。对有限前缀求和，第一项望远镜，第二项由 (P14) 控制；严格小于工作域余量后取极限。

### 比较级必要性与明确限度

若只允许使用 (P12)–(P13) 这组标量信息，那么任何统一的绝对误差条件都必须控制 \(\sum_k\Delta_\Theta(r_k,\eta_k)\)，或给出一个逐项更强且能推出它的条件。否则可在标量比较系统中取 \(a_k=0\)、\(\ell_k=C\Delta_\Theta(r_k,\eta_k)\)，使总长度恰为该债务级数；所以从 \(\Theta\) 与 \(\{\eta_k\}\) 本身不能推出有限长度。这个“必要”是对比较证书的必要性，不宣称每个坏债务序列都能由同一个最大单调算子实现。

若 \(\Theta\) 局部绝对连续，则
\[
 \Delta_\Theta(r,\eta)=\int_r^{r+\eta}\Theta'(u)\,du.\tag{P15}
\]
例如 \(\Theta(t)=t^\alpha\) 时，(P14) 是 \(\sum[(r_k+\eta_k)^\alpha-r_k^\alpha]<\infty\)；对于 \(\Theta(t)=t^\alpha(1+|\log t|)\) 或 \(\Theta(t)=t^\alpha/(1+|\log t|)\)，不能把误差条件简写成固定幂指数而不检查对数因子。

### 命题 P3-B（物理恢复的二点条件）

设约化 shadow \(h:V\to X\) 满足同一极限纤维的二点模
\[
 \|h(z)-h(z')\|\le K\,\omega(\|z-z'\|),\qquad \omega(0)=0,\tag{P16}
\]
其中 \(\omega\) 非减。若约化轨道满足 \(\sum_k\omega(\|z^{k+1}-z^k\|)<\infty\)，则 shadow 轨道有限长度并强收敛。若物理更新为 \(x^{k+1}=h(z^k)\) 或在其上另有可和的内层误差，则同样成立。

**证明。** 直接求和 (P16)；尾和趋零给 Cauchy 性，闭纤维/零值 demiclosedness 再识别极限。

一点评估
\[
 \|h(z)-x_*\|\le K\,\omega(d(z,S))\tag{P17}
\]
只给点误差和聚点识别，不能推出 (P16)。pppa_recovery.md#dd2-pppa-length 中的唯一纤维反例给出连续甚至局部 Lipschitz 的一点评估与无限物理长度并存；因此主文必须把“点恢复”和“物理有限长度”分成两个定理前件。

<a id="dd2-pro-distributed"></a>
## 4. 分布式分裂：固定步、图拓扑与通信假设

### 定理 P3-C（共识约束下的预条件前向—后向证书）

设通信图 \(\mathcal G=(V,E)\) 是有限、无向、连通图，拉普拉斯矩阵 \(\mathsf L\succeq0\) 的核为共识空间 \(\mathcal C\)。在堆叠空间 \(\mathbb R^{n|V|}\) 取
\[
 A_{\rm net}=\operatorname{diag}(A_i)+N_{\mathcal C},\qquad
 B_{\rm net}=(B_i)_i,\qquad
 P=\operatorname{diag}(\tau_i^{-1}I)+\rho\,\mathsf L\otimes I,\quad \tau_i>0,\ \rho\ge0.
\]
假设每个 \(A_i\) 最大单调，\(B_{\rm net}\) 在 \(P\)-度量中 \(\kappa\)-cocoercive：
\[
 \langle Bx-By,x-y\rangle\ge\kappa\|B x-B y\|_{P^{-1}}^2,\tag{P18}
\]
并取 \(0<\lambda<2\kappa\). 令
\[
 x^{k+1}=J_{\lambda P^{-1}A_{\rm net}}\bigl(x^k-\lambda P^{-1}B_{\rm net}x^k\bigr).\tag{P19}
\]
则对每个 \(x_*\in\operatorname{zer}(A_{\rm net}+B_{\rm net})\)
\[
 \|x^{k+1}-x_*\|_P^2
 \le \|x^k-x_*\|_P^2
 -(2\kappa\lambda-\lambda^2)\|B x^k-B x_*\|_{P^{-1}}^2
 -\|x^{k+1}-x^k\|_P^2.\tag{P20}
\]
在 \(\lambda<2\kappa\) 下得到 Fejér 单调和平方可和；若零集非空且 \(A_{\rm net}+B_{\rm net}\) 零值闭，则有限维轨道收敛到共识解。若各节点只交换 \(L^{1/2}x^k\) 的量化值，误差 \(e^k\) 满足 \(\sum_k\|e^k\|_P<\infty\)，则 (P20) 右端增加一个可和拟 Fejér误差项，结论保留。

**证明。** 预条件 resolvent 的单调性给
\[
 \langle x^{k+1}-x_*,P(x^k-x^{k+1})-\lambda(Bx^k-Bx_*)\rangle\ge0.
\]
用 \(2\langle a,b\rangle=\|a\|_P^2+\|b\|_P^2-\|a-b\|_P^2\) 展开，并用 (P18) 控制前向项，得到 (P20)。连通性只用于 \(\ker\mathsf L=\mathcal C\) 和 \(P\) 在共识/分歧分解上的正定性；\(\lambda_2(\mathsf L)>0\) 给分歧方向的定量门。量化扰动先按 C406 的同图误差写成 \(e^k\)，再用可和尾控制。

### 不能删除的通信前件

若图不连通，\(\ker\mathsf L\) 大于 \(\mathcal C\)，节点间不同常数向量不受能量控制；即使每个本地算子都满足 (P18)，也不能从 (P20) 识别全局共识零点。若 \(P\) 只有半正定而在分歧空间无闭值域，\(P^{-1}\) 和 (P19) 不良定义；应转入 C404 的值域约化并重新验证 lift 与物理长度。时间变化图还需统一 \(\lambda_2(\mathsf L_k)\ge\underline\lambda_2>0\) 和度数上界，单一固定能量不能直接沿用。

### 作用域结论

定理 P3-C 是固定步、共识约束、可验证 cocoercive 的网络子类；它不是对一般非单调、多算子或分布式异步算法的统一定理。把本定理接入 DD2，需要再以 (P0)–(P9) 核验最近锚、真实残差和工作域；仅有网络 Fejér 证书不能自动给原空间 shadow 的有限长度。

<a id="dd2-pro-verification"></a>
## 5. 验收结论与下一义务

- P2 完成了“完整图覆盖锐性”的正向门和只选一支的精确反例；近极小 residual lift 的量词已经显式化。
- P2 完成了非线性 CP/DR 块矩阵的完成平方、Schur 补可计算门和负位置模的边界；最优 \(W\) 的数值求解仍属于逐实例工作，不把 SDP 的最优值当作普遍常数。
- P3 给出了任意连续势 \(\Theta\) 的扰动债务 \(\Delta_\Theta\) 以及二点恢复对物理长度的精确充分条件；“势债务级数发散”只证明比较层不能保证长度，算子实现的坏例需按具体 \(\Theta\) 另构造。
- P3 给出有图拓扑和通信误差假设的固定步分布式前向—后向证书；变图、异步、非单调和多算子情形仍是开放扩展。

这些结果与 core.md、dual_eb.md、pppa_recovery.md、splitting.md 和 inexact.md 的量词一致；不改变 C400–C406 的既有身份。
