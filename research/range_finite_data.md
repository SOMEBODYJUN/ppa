# 全局值域定位、有限数据影子与信息边界

来源 S23 结构稿 TeX §5–§7（行 952–1572），21 页 PDF 同版；中文教学稿帮助解释机制，不作为证明。这里的全局/固定窗口值域结果属于**全图全尺度 RL 的有限维结构线**；9/25 §8 的局部拓扑证书是另一套假设，见 [holder_structure H07](holder_structure.md)。本轮逐式核对了定位函数、二次规划构造、覆盖不等式与有限信息反例的推理；外部扩张/degree 定理及先行性仍是门。

## W01 · 精确标量定位与整个纤维的值域覆盖

固定 \(\lambda,L>0,0<\gamma<1\)，令 \(R=L^{1/(1-\gamma)}\)。对 \(t\ge0\)，定义 \(\rho(t)\) 为
\(\rho-t=L(\rho+t)^\gamma\) 的**最大非负根**；\(\rho(0)=R\)，严格增，值域 \([R,\infty)\)。对每个图锚 \((x_0,v_0)\) 和每个图点有

\[
\|x-x_0\|\le\rho(\lambda\|v-v_0\|),\qquad
\lambda\|v-v_0\|\le\rho(\|x-x_0\|).
\tag{W01}
\]

若 \(r>R\)，唯一 \(h(r)\in(0,r)\) 满足 \(r-h=L(r+h)^\gamma\)，且 \(\rho(h(r))=r\)。有限维 graph-maximal 全局关系先由 S23 finite_geometry 得所有逆纤维非空，再有

\[
B(v_0,h(r)/\lambda)\subset F(B(x_0,r)),\quad
F^{-1}(v)\subset B(x_0,r)\quad
\bigl(v\in B(v_0,h(r)/\lambda)\bigr).
\tag{W02}
\]

第二式管的是**整个非空逆纤维**。正向对偶版也成立。对窗口 \(G\subset U\times W\) 的非空**相对 maximal** RL 图，若锚在图内、\(B(x_0,r)\subset U\)、\(B(v_0,s)\subset W\)、\(r>R,s>0\)，则所有 \(v\in B(v_0,\min\{s,h(r)/\lambda\})\) 在 \(G\) 中有非空逆纤维，整个纤维落在 \(B(x_0,r)\)。证明先作同参数全局 completion，再由相对 maximal 得窗口内相等。半径和严格 \(r>R\) 门槛在**所有维数统一**的意义上锐：一维 \(C(p)=L(p_+)^\gamma\) 见 S23 prop:coveragesharp。它没有声称任意非 maximal 子图也覆盖。来源：lem:rho、thm:coverage、thm:window、prop:coveragesharp。

## Q01 · 一个有限样本构造的全局一致影子

给 \(m\ge1\) 个图样本 \((x_i,v_i)\)，\(p_i=x_i+\lambda v_i,c_i=x_i-\lambda v_i\)，重复且一致的 \(p_i\) 可合并。固定 \(0<\sigma<1\)，取 H02 的 \(M_\sigma\)、\(a^2=M_\sigma/2>0\)，矩阵 \(P=[p_i]\)、\(V=[c_i]\)。**只需样本兼容**

\[
\|c_i-c_j\|^2\le\sigma^2\|p_i-p_j\|^2+M_\sigma
\quad(1\le i,j\le m).
\tag{Q-sample}
\]

令 \(Q=\sigma^2P^TP+V^TV+a^2I_m\)，
\(d_i(q)=\sigma^2\|p_i\|^2-\|c_i\|^2-4\sigma^2\langle p_i,q\rangle\)，在单纯形 \(\Delta_m\) 上唯一极小化
\(\theta^TQ\theta+d(q)^T\theta\)，定义 \(N_m(q)=V\theta(q)\)。
因 \(Q\succeq a^2I_m\) 唯一性成立；在正交抬升点上比较两个 QP 的一阶条件，得到**一个**全局 \(\sigma\)-Lipschitz \(N_m:\mathbb R^n\to\mathbb R^n\)，并有

\[
\|c_i-N_m(q)\|^2\le\sigma^2\|p_i-q\|^2+a^2
\quad\text{对每个样本 }i\text{ 与每个 }q.
\tag{Q-cross}
\]

由 \(x=(q+N_m(q))/2,\ A_m(x)=(q-N_m(q))/(2\lambda)\) 得单一强单调双 Lipschitz 同胚。对**已采样图点**同时有
\(\|v_i-A_m(x_i)\|\le a/[\lambda\sqrt{1-\sigma^2}]\) 与
\(\|x_i-A_m^{-1}(v_i)\|\le a/\sqrt{1-\sigma^2}\)。\(N_m\) 全球定义并不使它自动在**未观测完整图**上获得全球误差认证；独立逐查询挑一个球交值也不保证共同 Lipschitz 性。来源：S23 thm:finite_qp、行 1114–1223。

## Q02 · 覆盖的对象是 Cayley 参数，不只是原输入

若样本来自 RL 图，且未知图点的 \(p=x+\lambda v\) 离某个样本参数不超过 \(\delta\)，置 \(b=L\delta^\gamma\)，

\[
K_\delta=
\frac{b+\sigma^2\delta+
\sqrt{\sigma^2(b+\delta)^2+(1-\sigma^2)a^2}}{1-\sigma^2}.
\]

则对**每个此类图点**同时有
\(\lambda\|v-A_m(x)\|\le K_\delta\)、
\(\|x-A_m^{-1}(v)\|\le K_\delta\)。
证明把 Hölder 样本偏差和 Q-cross 相加，再解
\(t\le b+\sqrt{\sigma^2(t+\delta)^2+a^2}\) 的上根。若非空完整纤维的**所有图点参数**被此网覆盖，才得到到 singleton 的 Hausdorff 界 \(K_\delta/\lambda\) 或 \(K_\delta\)。当 \(\delta=0,\sigma=\sqrt\gamma\) 为 \(R/\sqrt2\)；对固定小 \(\delta\) 不声称常数最优。若完整 \(C(0)\) 已知，原输入 \(\|x\|\le B\) 或输出 \(\lambda\|v\|\le B\) 时有
\(\|p\|\le T_B=\max\{4B+2\|C(0)\|,(2L)^{1/(1-\gamma)}\}\)；取得该参数球的 \(\delta\)-网是额外采样假设。来源：thm:covered、cor:coveredfibers，行 1227–1311。

## Q03 · 可计算误差分解

对可行近似 \(\widehat\theta\in\Delta_m\)，QP 梯度 \(g_q=2Q\widehat\theta+d(q)\) 的 Frank–Wolfe gap
\(G=\langle g_q,\widehat\theta\rangle-\min_i(g_q)_i\ge0\)，且
\(\|V\widehat\theta-N_m(q)\|\le\sqrt G\)。
若 \(\widehat N(q)\) 到 \(N_m(q)\) 的**已认证**误差为 \(e\)，可用除以 \(1-\sigma\) 的固定点残差估计正反求值误差。真实 \(v\) 有观测 \(\widetilde v\)、\(\|\widetilde v-v\|\le\eta\)，且完整 \(F^{-1}(v)\) 的所有参数满足 Q02 的覆盖，则对每个 \(x\in F^{-1}(v)\) 和近似代理 \(\widehat x\)：

\[
\|x-\widehat x\|\le K_\delta+
\frac{\lambda(1+\sigma)}{1-\sigma}\eta+e.
\tag{Q03}
\]

三项分别是覆盖/模型偏差、噪声放大、求值误差。浮点 gap 用于严格证书需验证容差或向外取整；原稿**未给维数无关样本复杂度或运行时间**。来源：prop:evaluation、cor:totalerror。

## Q04 · 有限总查询不可能认证无界全空间

对 \(n\ge1\) 的无限制全局 \(L\)-Hölder \(C:\mathbb R^n\to\mathbb R^n\)，任何确定性程序若只作**有限次（可自适应）点查询**后输出一个不再访问 oracle 的单值 \(A\)，不能对所有这样的 \(C\) 保证其对应关系的全空间统一有限正向纤维误差。对零图 \(C_0=0\) 运行并记录有限查询集 \(E\)（加原点）；令 \(C_1(p)=L\,d(p,E)^\gamma e\)。两图给完全相同的自适应 transcript，却在无界远处任意分离；若输出 \(A\) 对 \(C_0\) 有有界误差，则对 \(C_1\) 必无界。这不排除持续 oracle、随机保障、已知解析式或指定紧域的认证。来源：prop:information。

## B01 · deadband 实例的意义和限度

\(K=U[-a,a]^2\)（\(U\) 正交）、\(F(x)=x-P_Kx\)、\(\lambda=1\)：本身已单调且 \(d(x,K)=\|F(x)\|\)，完整 Cayley \(C=P_K\)。在 \(\gamma=1/2\) 时最小全局 Hölder 常数 \(\sqrt{\operatorname{diam}K}\)。输出 \(w_\pm=\pm\varepsilon Ue_1\)（\(0<4\varepsilon<a\)）的完整逆纤维两侧相隔至少 \(2a+2\varepsilon\)，任何精确逆选择增益至少 \(a/\varepsilon+1\)。选 \(N=P_K/2\) 的代理逆映射为每坐标 \(\alpha(w)=3w\) 若 \(|w|\le a/4\)，否则 \(w+(a/2)\operatorname{sign}w\)；增益 3 且完整逆纤维误差至多 \(a\sqrt2\)。这展示精确重构与稳定近似的两种要求，**不证明该代理优于定制正则化**：恒等代理已有同样的全局 \(a\sqrt2\) 半径。来源：prop:deadbandjump、prop:deadbandproxy。

## 超边与未闭门

| ID | 合取前件 → 后件 | 证据/限制 |
| --- | --- | --- |
| HE-W01 | {全局 RL、锚点、标量 \(\rho\)} → 成对原坐标定位 | 稿内标量证明 |
| HE-W02 | {有限维 graph-maximal、非空完整纤维、W01、\(r>R\)} → 全纤维值域覆盖 | 稿内证明；非 maximal 无此结论 |
| HE-W03 | {相对 maximal 窗口、同参数全局 completion、W02} → 固定窗口覆盖 | 扩张与窗口等式须核 |
| HE-Q01 | {有限兼容样本、抬升、严格凸 QP} → 全球一致 \(N_m,A_m\) | 仅采样点有无覆盖的直接界 |
| HE-Q02 | {Q01、未知参数 \(\delta\)-覆盖、原图 Hölder} → 该区域的正反配对界 | 全纤维需每个图点被覆盖 |
| HE-Q03 | {Q02、验证过的 QP gap、观测误差} → 三项总误差 | 浮点误差不能只凭机器输出 |
| HE-Q04 | {确定性有限总查询、无界 Hölder 类} → 全空间统一认证不可能 | 明确不可区分图构造 |
| HE-B01 | {精确多值逆纤维、解析代理} → 稳定近似与不稳定精确逆的分离 | 单调例，不主张新算法优越 |
