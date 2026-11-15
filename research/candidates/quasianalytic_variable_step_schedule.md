# C307 · 准解析 Denjoy–Carleman 权重下有界变步精确 PPA 的 sharp 分界

**状态：** candidate / major-potential conditional。本文件保存本轮最值得继续验证的主线；它不是已闭定理，也没有把外部优先性升级成已认证事实。

## 1. 研究问题与精确候选

固定有限维欧氏空间、强对数凸总权重 \(M=(M_j)_{j\ge0}\)，\(M_0=1\)，并令

\[
\mathcal C(M):=\sum_{j\ge1}\frac{M_{j-1}}{M_j}.
\]

给定预先指定的步长序列

\[
0<\lambda_-\le \lambda_k\le \lambda_+<\infty,
\qquad
x_k\in\operatorname*{argmin}_y\left\{f(y)+\frac{\|y-x_{k-1}\|^2}{2\lambda_k}\right\}.
\]

主候选由两部分组成。

### 正向（准解析侧）

若 \(\mathcal C(M)=\infty\)，则对每个 \(f\in E^{\{M\}}\)，每个有界、全局精确且所有步长满足上述双侧界的 PPA 轨道都具有有限长度并收敛到一个临界点。

这一部分的承重估计是

\[
 f(x_k)-f(x_{k+1})
 \ge \frac{\|x_{k+1}-x_k\|^2}{2\lambda_+},
 \qquad
 \|\nabla f(x_{k+1})\|
 =\frac{\|x_{k+1}-x_k\|}{\lambda_k}
 \le \frac{\|x_{k+1}-x_k\|}{\lambda_-}.
\]

因此已有的准解析可定义性、KL/ABS 有限长度链可在同一权重类中使用；\(\lambda_-\) 与 \(\lambda_+\) 分别承担相对误差与下降常数，不能删除。

### 反向（非准解析侧）

若 \(\mathcal C(M)<\infty\)，则对每一个预先给定的 schedule \((\lambda_k)\)（先从任意两步周期 \((\lambda_1,\lambda_2)\) 开始，最终再攻任意 bounded-away sequence）以及每个同维可实现的紧连通集 \(K\)，存在一个**依赖该 schedule 的单一函数** \(f_{(\lambda_k)}\in E^{(M)}\)，使得：

1. \(f_{(\lambda_k)}\) 强制、全局 weakly convex，并可选取 \(\nabla^2 f\succeq-\mu I\) 且 \(\mu<1/\lambda_+\)；
2. 每个 \(I+\lambda_k\nabla f\) 都是全域同胚，故每一步完整 global-min prox 有全输入覆盖且无被删掉的远端纤维；
3. 存在一个有界精确轨道，其聚点集恰为 \(K\)，并可保留 C297/C298 中的严格物理长度或 Hölder 预算；
4. 同一函数对所有步长的说法仅指该固定 schedule 的每一个 \(\lambda_k\)，不声称存在一个 \(f\) 同时实现所有可能 schedules。

这使 \(\mathcal C(M)=\infty\) 成为“所有 bounded-away adaptive schedules 仍强制单点极限”的正则性门，而 \(\mathcal C(M)<\infty\) 仍允许任意紧连通极限集；固定步 C302 是其特例。

## 2. 当前证据与关键承重

- 仓库 C302 已完成固定 \(\lambda\) 的正反分界；RESEARCH_STATE.md 明确把任意有界步长列为开放门。
- C297 的反向弦先指定 \(x_k\) 与 \(g_k=x_k-x_{k+1}\)；变步只把梯度数据改成
  \[
  v_k=\frac{x_k-x_{k+1}}{\lambda_k}.
  \]
  双侧步长界不改变其趋零阶。若轨道位置与梯度幅度选择得足够快，并用 schedule-specific flat bumps 插值，可望保留 Whitney/Beurling 全阶兼容。
- 统一 Hessian 下界 \(\nabla^2f\succeq-\mu I,\ \mu<1/\lambda_+\) 同时保证所有 \(\lambda_k\)-子问题强凸，从而把“给出一条形式轨道”提升为完整 global-min resolvent 轨道。
- 最小决定性对象是任意两步周期 \((\lambda_1,\lambda_2)\) 与任意 \(K\) 的同一函数构造。若该门闭合，再处理任意振荡 schedule 的远索引 Whitney 兼容。

## 3. 已完成的去重与失败路线

- 与 C302 不重复：C302 只固定单步长；本候选要求同一权重分界对每个 bounded-away schedule 保持，并在非准解析侧构造 schedule-specific 函数。
- 与 C297–C299 不重复：那些结果固定步或标准梯度下降；这里的新增量是变步策略不改变准解析正则性相变。
- 与变量度量 PPA 文献的通常收敛定理不重复：已有结果给下降、KL 或最终稳定度量条件，但没有 Denjoy–Carleman 的 sharp converse 和任意紧连通聚点集实现。
- 不能把 \(\lambda_k\to0\) 纳入本命题；没有 \(\lambda_-\) 时相对误差门失效，属于另一个问题。
- 不能把“同一个 \(f\) 对所有 schedule 都成立”写入命题。若同一输入/输出对固定，梯度方程会强制步长，任意 schedule 的共同函数一般不可能。

## 4. 最危险的反例与决定性验证

最危险义务不是下降估计，而是非准解析反向构造：任意振荡的 \(\lambda_k\) 可能在近回点产生不相容的 Whitney 一阶数据。需要先写出两步周期版本：选择反向弦 \(z(t)\)、梯度 \(v_k=(z(t_k)-z(t_{k+1}))/\lambda_k\)，逐段给出一阶及全阶 jet 的 \(E^{(M)}\) 控制，并证明所有平滑补丁的 Hessian 总和仍小于 \(1/\lambda_+\)。

若两步周期不能保持 schedule-specific 的全局 coverage，则本候选降为 scope-limited；若两步周期和任意 schedule 都能闭合，才有资格作为主论文的 sharp converse。

## 5. 一手文献范围与价值判断

已核对的近邻是 Attouch–Bolte–Svaiter 的变量步 proximal/KL 下降框架、Rolin–Speissegger–Wilkie 的准解析 Denjoy–Carleman/o-minimal 结构，以及 Burke–Qian、Rockafellar 的 variable-metric PPA 收敛接口。它们覆盖充分收敛机制或正则性结构，没有覆盖本候选的“权重 Carleman 分界对 bounded-away variable schedules 不变 + 非准解析 schedule-specific 任意聚点集反向实现”。

若闭合，读者可以在不知道具体势函数的情况下，仅由权重的 Carleman 和与步长上下界判断：任何有界精确自适应隐式策略是否必然有限长；反向侧则说明该判断在非准解析类不能推广。这是对当前论文从固定算法实例到策略稳定正则性相变的实质提升。当前仍需外部逐定理优先性核验，不能把未检索到先例当作首创性证明。

