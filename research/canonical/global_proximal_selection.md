# 全局随机近端：物理吸收、连续噪声与有限支撑分类

本页补齐固定目标非乘积来源中尚未进入规范层的四组独立命题。固定目标吸收主定理和二维接缝的有限长反例直接使用 [C62-v2/C63](../topics/random_markov/proximal_selection_seam.md#ps-objects)，不将它们重新编号，也不调用不一致二次近端的 C22/C23 来证明同一目标的结论。本页各命题是有限维的直接推导；不声称外部优先权。

<a id="npr-objects"></a>
## 对象与选择合同

欧氏空间为 \(\mathbb R^n\)，\(\lambda>0\)。对 proper 函数 \(f:\mathbb R^n\to(-\infty,+\infty]\)，
\[
P_\lambda f(x)=\arg\min_y\{f(y)+\|y-x\|^2/(2\lambda)\}.
\tag{NP1}
\]
它总指全部全局最小解，不指完整非凸次梯度 resolvent。若给定 Borel 核 \(K\)，物理实现要求 \(\mathcal L(X^+\mid X)=K(X,\cdot)\)；仅要求 \(X^+\in P_\lambda f(X)\) 的图支持实现可以改变条件选择概率；仅给输入、输出边缘的运输实现又更弱。平稳律满足 \(\pi K=\pi\)。只有明确讨论 \(W_2\) 时才要求二阶矩；平稳吸收证明无需这一矩条件。

<a id="npr-physical"></a>
## C187-v1 / NP-PHYSICAL · 零距离物理证书强制吸收

设 \(K\) 为 Borel 核，\(X\sim\pi\)、\(\pi K=\pi\)，且 \((X,X^+)\) 是上述物理实现。若同一概率空间上的 \(Y\) 满足 \(\mathbb E\|X-Y\|^2=0\)，并有
\[
\|2X^+-X-Y\|\le\omega(\|X-Y\|)\quad\text{a.s.},\qquad \omega(0)=0,
\tag{NP2}
\]
则 \(X^+=X\) a.s.，从而 \(K(x,\{x\})=1\) 对 \(\pi\)-几乎处处的 \(x\) 成立。证明只是 \(X=Y\) 后代入 NP2，再对输入条件化；事实上这一步连平稳性也无需使用，平稳性指定了被攻击的应用位置。无需 EB、幂模或分别要求 \(X,Y\in L^2\)。

**不达参考的版本。** 固定同一个物理联合律 \((X,X^+)\)。参考 \(Y_j\) 可在扩展概率空间上实现，只须保留这同一个联合律。若 \(d_j=\|X-Y_j\|_2\to0\)，且
\[
\|2X^+-X-Y_j\|_2\le Ld_j^\gamma,
\qquad L<\infty,\ \gamma>0,
\]
则三角不等式给 \(2\|X^+-X\|_2\le d_j+Ld_j^\gamma\to0\)。右侧有限本身保证位移的二阶矩，无需预先要求状态的二阶矩。若已知点态 \(L\|X-Y_j\|^\gamma\) 界且 \(0<\gamma\le1\)，则凹性/Jensen 给 \(\mathbb E\|X-Y_j\|^{2\gamma}\le d_j^{2\gamma}\)，得到同一结论。一般模只可在其相应 \(L^2\) 上界也趋零时如此使用。

**多步与支持边界。** 把 NP2 中的 \(X^+\) 改成物理 \(m\) 步输出，得到的是 \(K^m(x,\cdot)=\delta_x\)，\(\pi\)-a.e.，不是一步吸收。周期整除 \(m\) 的确定性链满足此式。若 \(\pi\) 非 Dirac，取 \(0<\pi(A)<1\)；沿 \(km\) 的平稳相关为 \(\pi(A)\)，不会趋向 \(\pi(A)^2\)，所以该链不满足通常的平稳强混合结论。若只有图支持实现，NP2 仅给 \(x\in P_\lambda f(x)\) 对 \(\pi\)-a.e. 的 \(x\)，不能推出指定核选取对角。

**移动参考的不同对象。** 以 \((X^+-Y^+)-(X-Y)\) 作缺陷不会遇到相同对角障碍。例如在 \(\{-1,1\}\) 上每步独立均匀重采样，取 \(X=Y\) 为平稳均匀变量，\(X^+=Y^+\) 为新的独立均匀变量；相对缺陷恒零而 \(\mathbb P(X^+\ne X)=1/2\)。这只说明残差不同，不自动给原生图支持、输入最优性或所需回耦。

<a id="npr-variable-descent"></a>
### 同目标可变步长的附加边界

设 \((X,X^+)\) 同律且落在同一个 proper Borel \(f\) 的有限值域内，实际转移满足
\[
f(X^+)+a\|X^+-X\|^2\le f(X),\qquad a>0\quad\text{a.s.}
\]
其中 \(a\) 可以随机且没有统一正下界。沿 [C62-v2](../topics/random_markov/proximal_selection_seam.md#ps-absorption) 的有界严格递增 \(\arctan f\) 论证，先得 \(f(X^+)=f(X)\) a.s.，再由逐点 \(a>0\) 得吸收。若随机正步长的全局 prox 使用同一 \(f\)，可取 \(a=1/(2\lambda_{\rm step})\)。随机换目标或允许不带严格下降的误差不满足该合同。

<a id="npr-common-minimizer"></a>
## C188-v1 / NP-ANCHORED · 共同全局极小点的线性锚界

对任意 proper \(f_i\)、任意全局极小点 \(p\in\arg\min f_i\)、任意 \(\lambda>0\) 和任意 \(x^+\in P_\lambda f_i(x)\)，有
\[
\|x-x^+\|\le\|x-p\|,\qquad
\|x^+-p\|\le2\|x-p\|,\qquad
\|2x^+-x-p\|\le3\|x-p\|.
\tag{NP3}
\]
比较近端目标在 \(x^+\) 与 \(p\) 的值，再用 \(f_i(x^+)\ge f_i(p)\)，得到第一式；后两式分别由三角不等式和 \(2x^+-x-p=(x-p)+2(x^+-x)\) 得到。证明允许非凸目标，不需要 \(x\in\operatorname{dom}f_i\)。若一族函数有共同全局极小集 \(S\ne\varnothing\)，三式对全部函数、全部步长、全部最小解及每个 \(p\in S\) 同时成立。只有在最近点存在时才写 \(p\in P_S(x)\)；一般版本直接保留任意 \(p\in S\)。指标函数给最近投影的相同结论。

NP3 不声称最优常数、全对 Lipschitz、Fejér 单调或收敛；它只是排除了在这同一锚比较任务中必须使用低于一次幂的理由。例如扩展实指标 \(\delta_A=0\)（在 \(A\) 上）、\(+\infty\)（域外），取 \(f=\delta_{\{-1,1\}}\)，\(x=0,p=1,x^+=-1\) 时 \(\|x^+-p\|=2>\|x-p\|=1\)，且输入两侧的唯一投影发生跳跃。共同极小点与 NP3 因而不能补出上述更强结论。

<a id="npr-seam-completion"></a>
## 已有二维 C63 对象的精确附加计算

以下沿用 [PS-SEAM](../topics/random_markov/proximal_selection_seam.md#ps-example) 的完整同一个对象：\(\lambda=1\)、\(H=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\)、\(b=(3,3)\)、\(f(y)=\tfrac12y^THy-b^Ty+4\mathbf1_{y\ne0}\)，\(Q=H+I\)、\(t(x)=Q^{-1}(b+x)\)、\(g(x)=\tfrac12(b+x)^TQ^{-1}(b+x)\)。\(H\) 的特征值为 \(1,3\)，所以二次部分强制；零处向外有正跳，给 lsc 和非凸性，且该有限分段多项式函数为半代数。展开得到
\[
g(x)=\{3x_1^2-2x_1x_2+3x_2^2+12x_1+12x_2+36\}/16.
\]
由交叉二次项及共同组惩罚，目标和完整近端关系不分离为两个标量关系的笛卡尔积；在 tie 上 \(\{0,t(x)\}\) 的两个坐标一般同时非零，也直接否定笛卡尔积表示。

**完整 fair-bit 表示。** 令
\[
T_0(x)=\begin{cases}0,&g(x)\le4,\\t(x),&g(x)>4,\end{cases}
\quad
T_1(x)=\begin{cases}0,&g(x)<4,\\t(x),&g(x)\ge4.\end{cases}
\tag{NP4}
\]
用每步独立 fair bit 选择，核恰为 C63 的 \(K=(\delta_{T_0(x)}+\delta_{T_1(x)})/2\)。两图均 Borel、固定零点且至多线性增长，因此保持 \(\mathscr P_2\)。相对于唯一平稳律 \(\delta_0\)，定义本表示的同步位移残差
\[
\Psi_K(\mu)^2=\int\tfrac12\sum_{i=0}^1
\|(T_i x-x)-(T_i0-0)\|^2\,d\mu(x).
\tag{NP5}
\]
与 \(\delta_0\) 的输入耦合唯一，故无额外 OT 选择；\(\Psi_K=0\) 当且仅当两个非负位移都几乎处处为零，即 \(\mu\) 支撑核的吸收点，由 C63 恰为 \(\delta_0\)。在 C63 的 \(\mu_k=(1-\epsilon)\delta_0+\epsilon\delta_{a_kv}\)、\(a_k>1,v=(1,1)\) 上，两标签都选同一个非零输出，所以 \(\Psi_K(\mu_k)=\sqrt{2\epsilon}(a_k-a_{k+1})=W_2(\mu_k,\mu_kK)\)。这个局部同值不识别别的表示或核的同步残差，也不把 C63 的一般残差声明改为同步对象。

**接缝、图模与零点。** C63 的左右强制核极限 \(\delta_0\) 和 \(\delta_v\) 不同，故在 \(v\) 的任何完整邻域内，任何 tie 政策都不可能满足 \(W_2(Kx,Ky)\le L\|x-y\|^\gamma\)（\(L<\infty,\gamma>0\)）。在相同输入 \(v\)，全局 prox 有输出 \(0,v\)；两输出的反射差为 \(2v\ne0\)，输入差为零，故该完整关系也不满足零点消失的全对 RL 模。

这里 Fréchet 次梯度在零处是全部 \(\mathbb R^2\)：对任意 \(w\)，其定义中的差商是 \(4/\|z\|+O(1)\to+\infty\)。因此 limiting 次梯度在零处也为全部空间，非零处则为普通梯度 \(Hy-b\)。于是
\[
\operatorname{zer}\partial f=\{0,v\},\qquad
(I+\partial f)^{-1}(x)=\{0\}\cup\{t(x):t(x)\ne0\}.
\tag{NP6}
\]
完整 resolvent 在所有输入都有零输出，确实比全局 prox 大；局部非零图支为仿射 \(t\)，而从 \(v\) 选到零离开该图支。C63 的极限 \(v\) 是算子零点而不是所选核的吸收点。直接从 \(v\) 起步，首次转到零的步数满足 \(\mathbb P(\tau=j)=2^{-j}\)（\(j\ge1\)）；这与从 \(a_0v,a_0>1\) 永不触及 tie 的见证轨道不同。

<a id="npr-ae-singleton"></a>
## C189-v1 / NP-NOISE · 几乎处处唯一近端与卷积连续化

设 \(f\) proper lsc，\(\lambda>0\)，\(h(y)=\lambda f(y)+\|y\|^2/2\)，\(g=h^*\)。令 \(U\subset\mathbb R^n\) 为开集，并假定 \(g\) 在 \(U\) 有限、\(P_\lambda f(x)\ne\varnothing\) 对每个 \(x\in U\) 成立。则 \(P_\lambda f\) 在 \(U\) 上 Lebesgue-a.e. 单值。

**证明及基础接口。** \(g\) 是仿射函数的上确界，故为扩展实凸函数。对任一 \(y\in P_\lambda f(x)\)，完成平方表明它达到 \(g(x)\)，从而对全部 \(z\)，
\[
g(z)\ge g(x)+\langle z-x,y\rangle.
\tag{NP7}
\]
取闭包仍在 \(U\) 的开坐标盒。对固定其余坐标，沿第 \(i\) 坐标的 \(g\) 为有限一维凸函数。其左右导数由差商单调性存在且有限；发生不相等时，非空区间 \((g'_-,g'_+)\) 可各取有理数，而不同位置的这些区间互不重叠，所以该直线上的异常点至多可数。左右导数可用有理步长差商极限定义，异常集可测。由 Fubini，其 \(n\) 维测度为零。对有限个坐标取并集；在余下的每个 \(x\)，把 NP7 的 \(z\) 限制在各坐标直线并从两侧取差商，迫使每个最小解的第 \(i\) 坐标等于同一个偏导数。因此所有最小解相同；非空性使之恰为单点。可数坐标盒覆盖 \(U\)，完成证明。此证明只调用一维凸差商和 Fubini，不把未核文献中的广义刻画当作定理导入。

若噪声后的输入条件律对 Lebesgue 测度绝对连续且由 \(U\) 支撑，任意两个 Borel tie 政策在该条件律下 a.s. 相同，因此产生相同的输出律。这里不是声称任意噪声都绝对连续，也不是声称没有噪声的近端处处单值。

<a id="npr-convolution"></a>
### 指定二维对象的强 Feller 修补

在 NP4 同一模型中，\(g(x)=4\) 是非退化椭圆。经可逆仿射变换成为圆，故为二维 Lebesgue 零测集。任意支持完整全局 prox 的 Borel 核 \(k\) 只在该零测集可能不同。对概率密度 \(p\ge0,\int p=1\)，置
\[
K_p(x,A)=\int k(u,A)p(u-x)\,du.
\tag{NP8}
\]
对所有有界 Borel \(\varphi\)，
\[
|K_p\varphi(x)-K_p\varphi(y)|
\le\|\varphi\|_\infty\|p(\cdot-x)-p(\cdot-y)\|_1.
\tag{NP9}
\]
由矩形阶梯函数在 \(L^1\) 的稠密性及矩形平移的对称差体积趋零，可得 \(L^1\) 平移连续：先用阶梯函数逼近 \(p\)，两端逼近误差相同，再控制有限个矩形平移。NP9 因此使 \(K_p\) 把每个有界 Borel 函数送成连续函数，即强 Feller。政策只在零测集不同，故 NP8 与其选择无关。核的 Borel 性由参数积分得到。这是换输入机制之后的新核，不从此推出平稳律存在、唯一、速率或新的 RL–EB。

<a id="npr-finite-support"></a>
## C190-v1 / NP-SUPPORT · 坐标稀疏二次目标的完整有限分类

固定 \(n<\infty,H=H^T\succ0,b\in\mathbb R^n,\kappa>0,\lambda>0\)，令
\[
f(y)=\tfrac12y^THy-b^Ty+\kappa\|y\|_0,
\quad Q=H+\lambda^{-1}I,\quad c(x)=b+\lambda^{-1}x.
\]
对每个 \(J\subset\{1,\ldots,n\}\)，定义
\[
(T_Jx)_J=Q_{JJ}^{-1}c_J(x),\quad(T_Jx)_{J^c}=0,
\quad V_J(x)=\kappa|J|-\tfrac12c_J(x)^TQ_{JJ}^{-1}c_J(x).
\tag{NP10}
\]
约定 \(T_\varnothing x=0,V_\varnothing=0\)，空矩阵不要求取逆。记 \(M(x)=\arg\min_J V_J(x)\)。则
\[
P_\lambda f(x)=\{T_Jx:J\in M(x)\};
\tag{NP11}
\]
每个获胜 \(J\) 都满足 \(\operatorname{supp}(T_Jx)=J\)，所以不同获胜支撑给不同输出，完整纤维非空有限。

**全部候选及排伪证明。** 除去不依赖 \(y\) 的 \(\|x\|^2/(2\lambda)\)，在指定支撑 \(J\) 的二次最小值是 NP10 的 \(V_J\)，其严格凸候选为 \(T_Jx\)。若某个获胜候选在 \(j\in J\) 处为零，删去全部零坐标得到真子集 \(I\)。同一个候选也满足 \(I\) 上的二次一阶条件，故是其唯一二次极小点，且 \(V_I=V_J-\kappa(|J|-|I|)<V_J\)，矛盾。因此获胜候选确实实现所计惩罚。任意 \(y\) 取其真实支撑 \(J\)，目标至少为 \(V_J+\|x\|^2/(2\lambda)\)；获胜候选达到全局最低值。反向，全局最小解在其非零坐标的开支撑层上必须满足二次一阶条件，故为 \(T_Jx\)，且其得分必须最小。这证明 NP11 的两个方向。

**政策与全部平稳律。** 均匀选取有限集合 \(M(x)\) 给 Borel 核：各 \(V_J\) 连续，获胜事件为有限个闭不等式的交，\(|M(x)|\ge1\)，各 \(T_J\) 仿射。也可使用对每个获胜支撑均给严格正概率的 Borel 政策。令
\[
(x^J)_J=H_{JJ}^{-1}b_J,\quad (x^J)_{J^c}=0,
\quad x^\varnothing=0.
\]
其吸收集恰为以下有限候选集：
\[
A_K=\left\{x^J:\ x^J_j\ne0\ (j\in J),\quad
V_J(x^J)<V_I(x^J)\ \text{对每个 }I\ne J\right\}.
\tag{NP12}
\]
因为每个完整纤维均有限且所有成员获正概率，[C62-v2](../topics/random_markov/proximal_selection_seam.md#ps-absorption) 的正确完整量词适用：吸收当且仅当 \(P_\lambda f(x)=\{x\}\)。由精确支撑，单点纤维当且仅当存在唯一获胜 \(J\)，即全部严格得分不等式；固定点方程 \(T_Jx=x\) 又等价于 \(H_{JJ}x_J=b_J\) 和域外零。这证明 NP12 的必要与充分两方向。所有平稳概率律恰为支撑于 NP12 的律，无需矩条件或目标可积性。

这里非严格得分比较只能说明输入是一个全局近端固定点，不能保证在另有 tie 输出时吸收。不得把“已核每个有限纤维”偷换成“每个完整纤维都有限”；本模型是由 NP11 实际证明后者。所得有限数据分类不认证其它稀疏目标、无限维模型或其它随机选择政策。

<a id="npr-review"></a>
## 证明边界与来源

本页重构 NP2–NP12 的数学推导；C62-v2/C63 的既有主证明仍在其原规范页。C189 的实际基础接口为有限维一维凸差商、Fubini、\(L^1\) 简单函数逼近；没有依赖来源自报的 Gribonval–Nikolova 或 HLS 定理。半代数标签只按本具体分段多项式定义核查。没有本轮数值执行、新颖性或期刊等级结论。

来源为 `history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/04_相关性与随机表示/非乘积随机近端_吸收选择与非不变极限障碍.md`，SHA-256 `f45947f55a8e36b80e80d90cd31e425fcd869393957d828e7574f6140dd4c3f2`。完整源范围、逐断言处置及明确未核的文献/历史执行证据见 [全源审计](../audit/NONPRODUCT_FULL_COVERAGE_2026_10_07.md#npr-scope)。源中“已完成”“独立审查”“VERIFIED_SOURCE/EXECUTED_LOCAL”均不代替本页证明或实际证据。
