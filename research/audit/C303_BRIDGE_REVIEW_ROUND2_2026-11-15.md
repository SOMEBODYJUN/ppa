# C303 第二轮独立审查：HJ 估计、原文身份与 PPA/GPPA 桥

日期：2026-11-15

## 裁决

C303 的连续时间二阶候选目前应判为 **继续验证**。formal estimate lemma 的主要微分计算与原始 HJ 页面一致，首次离开 bootstrap 没有发现新的动力学反例；但 cutoff 的全尾支撑分离需要作为显式构造条件写出，且项目目标是 PPA/GPPA，当前候选仍只有 ODE 结论。

不能把 HJ 2020 的 open-problem 说明升级为“无人先行”的事实。现有证据只支持 provisional priority：HJ 原文 Remark 3 明确说他们只构造了 (\mathbb R^4) 中二维初值子流形，并把相空间开集问题称为 open；检索到的后续二阶梯度系统文献讨论 KL/收敛条件、渐近阻尼或离散化，但没有核到直接解决同一开盆 (\omega=S^1) 命题的原始定理。仍需人工完成完整文献核查。

## 1. 与 HJ 原始页面的逐项对照

HJ 原文（ResearchGate 可核 PDF）给出：

- 螺旋曲线满足 (1<\gamma_2(\theta+2\pi)<\gamma_1(\theta)<\gamma_2(\theta))，且 (\gamma_i(\theta)\to1)。代入 (\gamma_1=1+e^{-\theta})、(\gamma_2=1+\mu e^{-\theta}) 后，确实需要 (1<\mu<e^{2\pi}) 才有全尾不重叠。
- (F) 是偶的 (C^\infty) bump，支持为 ([-1,1])，在 ((-1,1)) 为正；(b_1,b_2) 选在 (|F'|) 达到最大的位置，对应 (q=-\beta,+\beta)。由偶性和 (F) 在正半轴的递增性，(F'(-\beta)<0<F'(\beta))。
- 原文显示的向量公式虽然文字写作 (X=\nabla f)，但径向项为 (-2hF'/\Delta)，切向项为 (-h'F/r)，即实际使用的是 (Y=-\nabla f)。这与 C303 的符号约定一致。
- 原文在边界以 (n_i=-b_i e_r+b_i'e_\theta) 计算 (Y\cdot n_1<0)、(Y\cdot n_2>0)。换成 (s_1=r-b_1(\theta))、(s_2=b_2(\theta)-r) 后正好得到 (
abla s_i\cdot Y>0)。
- 原文说 cutoff (Pi) 的 support 连通、包含初始曲线附近，并且大角度时两条边界曲线不在 support 中；它没有在该页面明确写出“support 紧”或“整个闭管与 support 分离”。因此 C303 不能仅从“边界曲线不在 support”推出 (Pi=0) 于整个尾管。

formal lemma 中的微分恒等式为
[
q_r=2/\Delta,
\quad q_\theta=q+(1+\mu)/(\mu-1),
\quad q_{r\theta}=q_r,
\quad q_{\theta\theta}=q_\theta.
]
这与 (Delta'=-Delta)、(-\gamma_1'-\gamma_2'=(1+\mu)e^{-\theta}) 一致。特别需要保留
[
f_{r\theta}=h'F'q_r+hF''q_rq_\theta+hF'q_{r\theta};
]
遗漏第一项虽然不改变阶数，但会使“精确恒等式”不完整。当前仓库版本已补入。

在 (|q|\le\beta) 上，(F_*:=\min F>0)、(|F'|\le G_1) 给出
[
Y_\theta=\frac{h}{r}(2\theta F-F'q_\theta)
\asymp \theta e^{-\theta^2}.
]
边界径向主项为 (h/\Delta\asymp e^{-\theta^2+\theta})，而切向法向修正为 (O(\theta h e^{-\theta}))，比值 (O(\theta e^{-2\theta})\to0)。Hessian 阶分别为 (he^{2\theta})、(\theta he^\theta)、(\theta^2h)，全部趋零；HJ 的 (C^\infty) 延拓给出物理闭管上的有限 Hessian 上界。

## 2. cutoff 支撑的最小修复

有两种严谨写法：

1. **构造性写法。** 选连通紧支撑的 (Pi)，支撑包含 (gamma_1(0),\gamma_2(0)) 附近且落在 (r\ge1+\eta) 的有限初始环带；再取 (\theta_0) 使 (\gamma_2(\theta)<1+\eta/2) 对所有 (\theta\ge\theta_0)。于是整个闭尾管与 (operatorname{supp}\Pi) 分离，(Pi=0)、(1-Pi=1)。
2. **假设性写法。** 把 (operatorname{supp}\Pi\cap\overline D_{\theta_0}=\varnothing) 作为 C303 的明确假设，不再声称它由原文的两条边界曲线条件自动推出。

第一种写法不会改变 HJ 尾管机制，但需要在正式证明中说明这样选择的 (Pi) 仍保留 HJ 初始局部化与全局 (C^\infty) 构造。若不补这一门，C303 仍有一个未闭的定义义务。

## 3. 首次离开 bootstrap 的再核查

在 cutoff 分离和嵌入条件 (\mu<e^{2\pi}) 下，令 (w=v+\nabla f(x))。
[
x'=Y+w,
\qquad
w'=(\nabla^2f-aI)w,
\qquad
|w(t)|\le e^{-\delta t}|w_0|.
]
从有限初始角带开始，(W=C\int|w|) 给 (\theta\ge\Theta_0-C\varepsilon/\delta)。令 (u=\theta-W)，在首次离开时间区间内使用 (s e^{-s^2}) 在 (s\ge1) 的递减性，得到
[
u'\le C_0u e^{-u^2},
\qquad
\theta^2\le C+p\log(1+t).
]
故边界 inward margin 至少是 (c(1+t)^{-p})，可选 (\varepsilon) 使指数扰动始终小于其一半。任何首次边界接触都会满足 (s_i'>0)，矛盾。再由
[
\theta'\ge c_0\theta e^{-\theta^2}/2
]
得到 (	heta\to\infty)，继而 (r\to1)、(\omega=S^1)。这一段的量词和 bootstrap 顺序现已正确。

## 4. 可行的离散桥：两种层次

### 4.1 直接隐式 Euler / 普通 PPA：有希望但尚未闭合

若取 (F=\nabla f)、(v=I)，普通 PPA 迭代是
[
x_k-x_{k+1}=\lambda\nabla f(x_{k+1}),
\qquad x_{k+1}=x_k+\lambda Y(x_{k+1}).
]
在尾管中若 (lambda\|\nabla^2f\|<1)，局部方程 (G(y)=y-\lambda Y(y)=x_k) 可由局部逆函数定理处理。若 (y=x_{k+1}) 位于边界，
[
s_i(x_k)=s_i(y)-\lambda\nabla s_i(y)\cdot Y(y)<0,
]
所以隐式步的局部分支具有很强的边界内向性；角度也可由
[
\theta_k=\theta_{k+1}-\arctan\frac{\lambda Y_\theta(y)}{r(y)-\lambda Y_r(y)}
]
核得严格增加（当 (lambda) 足够小）。

但这还不是完整 PPA 证明。必须建立：

- 对每一个 (x_k) 存在同一局部分支的 (y\in D)，而不是只在给定轨道上应用局部逆函数定理；
- 该分支在无限收缩管中不丢失，且没有其他完整 resolvent 分支改变算法量词；
- 离散角度发散的定量估计（例如对 (e^{\theta_k^2}) 的单步增长）和所有离散边界余量；
- 若要称作完整 PPA/GPPA，还需给出全域关系、输入 coverage、图闭性及所用输出选择的精确量词。

因此该桥当前只能判为“可执行的下一项数学任务”，不能把 C303 升级为已闭 PPA 结果。

### 4.2 精确流映射编码：形式可行但研究价值弱

把 (Y) 在管外平滑延拓为有界 (C^\infty) 完备向量场，令 (Phi_t) 为其全局流。固定 (\lambda>0)，定义
[
F_\lambda(y)=\frac{\Phi_{-\lambda}(y)-y}{\lambda},
\qquad v=I.
]
则
[
I+\lambda F_\lambda=\Phi_{-\lambda},
\qquad
J_{\lambda F_\lambda}=\Phi_\lambda.
]
因此 HJ 连续流的开盆 (\omega=S^1) 轨道在整数时刻精确转成 PPA 轨道。

这个编码只适用于非单调的完整关系；它一般不保持 maximal monotonicity、凸性、firm nonexpansiveness 或优化结构，而且把目标 PPA 算子定义成流映射的逆，容易被视为把连续动力学的结论重新编码进 resolvent。它可以作为形式桥或 sanity check，却不足以支撑 PPA/GPPA 领域的主要贡献。

## 5. 外部先行性与最终证据门

HJ 2020 Remark 3 的原始页面明确记录：他们的二阶转移只有二维初值子流形，并称相空间开集问题在当时 open。后续检索到的二阶梯度系统结果主要在 KL、渐近阻尼、非局部非线性或隐式离散化的收敛框架内；未找到直接证明同一 (\chi_a)、同一 (\omega=S^1) 开盆命题的来源。但这只是检索结果，不能写成“文献证明了新颖性”。

**当前裁决：继续验证。**

改变 C303 数学真值判断的最小证据门：

1. 把 cutoff 选择写成一个独立、可复核的构造，证明整个闭尾管上 (Pi=0)；
2. 在需要 PPA/GPPA 主贡献的情况下，完成 4.1 的局部隐式分支、离散留域和角度发散证明，并明确完整关系的 coverage/selection 量词；
3. 若采用 4.2，只能把它记作形式编码，不能把它当作有实质优化意义的桥。

在这些证据补齐前，C303 不能裁决为“达到主要贡献标准”。

### 4.3 进一步的可行闭合路线：全局单值非凸 PPA

HJ 的 (phi) 仅在 (1<r<gamma_2(0)=1+mu) 的有界物理环带内非零；若 (Pi) 取紧支撑，所得全局 (C^infty) 势 (f) 有界 Hessian。记 (Y=-\nabla f)、(|\nabla^2f|le L)，取 (0<\lambda<1/L)。则
[
G_s=I-s\lambda Y=I+s\lambda\nabla f,qquad 0\le s\le1,
]
都是全局强单调微分同胚。对 (x\in D) 定义 (y_s=G_s^{-1}(x))，从 (y_0=x) 连续延拓到 (y_1=T_\lambda x)。若在首次 (s) 发生 radial 边界接触，令 (g_i=s_i)，则
[
g_i(G_s y)= -s\lambda\nabla g_i(y)\cdot Y(y)+O(s^2\lambda^2|Y(y)|^2)<0,
]
只要 (lambda) 在有限初始角段取小，并利用尾部
(|Y|^2/m(\theta)=O(e^{-\theta^2+\theta})\to0)。因此 (x\in D) 不可能是该边界的像。入口边界 (\theta=\theta_*) 也不能穿越，因为 (Y_\theta>0) 且 (r-s\lambda Y_r>0) 使 (G_s) 的极角严格小于 (\theta_*)。连续无穿越给出 (T_\lambda(D)\subset D)，且这是完整单值非凸 PPA resolvent，而非选支。

若 (y=T_\lambda x) 的 lifted 极坐标为 ((r,\theta))，则
[
\theta_x=\theta-\arctan\frac{\lambda Y_\theta(y)}{r-\lambda Y_r(y)}.
]
取 (lambda) 小使分母正，得 (\theta_{k+1}>\theta_k) 且
[
\theta_{k+1}-\theta_k\ge c\lambda\theta_ke^{-\theta_k^2}.
]
从而 (e^{\theta_{k+1}^2}-e^{\theta_k^2}\ge c'\lambda\theta_k^2ge c''\lambda)，所以角度发散。增量趋于零，单调无界离散角在每个 (2\pi) 周期的首次穿越误差趋于零，故投影相位的极限集是整个圆；管界给 (r_k\to1)。

这是一个比流映射编码更有实质的桥：它使用原 HJ 势的完整非凸 prox，且 (I+\lambda\nabla f) 的强单调性消除了 alternate resolvent branches。仍需把上述 boundary Taylor remainder、有限初始段的统一 (lambda) 和全局支撑/\(\|Hf\|\le L) 写成正式引理；在此之前不能升级 C303，但最小义务已从“存在桥”变成一组可核的有限常数估计。

## 6. 对 C303 惯性桥的更正与最终判断

上文 4.1 的 (G_\lambda=I-\lambda Y) 只给出 **普通 PPA for (F=\nabla f)** 的一阶 HJ 离散桥。它复现 HJ 一阶螺旋流，但没有离散化 (chi_a) 的二阶系统，因此不能直接算作 C303 的惯性桥。

C303 的正确对象是仓库 `research/c303_discrete_bridge.md` 中的 D1：
[
y_k=J_{\lambda_k\nabla\chi_a}(x_k+\beta_kv_k),
\qquad
v_{k+1}=v_k-h_k(av_{k+1}+\nabla\chi_a(y_k)).
]
若 (f) 由紧物理支撑的全局 (C^\infty) cutoff 构造，则 (\nabla\chi_a) 全局 Lipschitz；小 (\lambda_k) 下 (I+\lambda_k\nabla\chi_a) 强单调双射，complete coverage 这一步可以成立。

但 D6–D7 仍非正式证明。离散轨道可能在一个整数步内从 (D) 内跳到 (D) 外，不能仅以连续时间的“首次边界接触且 (s_i'>0)”替代。必须对带动量的输入 (z_k=x_k+\beta_kv_k) 和隐式输出建立离散 barrier，或者沿隐式求解路径证明相空间 tube 不穿越。还需统一证明：

1. D4 的 (w_k) 展开在无界 lifted angle 上具有统一 (O(h_k^2)) 常数；
2. 在 tube 未闭合前，D5 的 (w_k=O(h_k)) 与 D6 的 margin 比较不形成循环；
3. (h_k=o(m(\theta_k))) 和 (h_k=o(Y_\theta(\theta_k))) 的指数/多项式换算沿离散首次离开 bootstrap 成立；
4. 初始有限前缀和所有动量初值给出同一相空间开集量词；
5. 离散增量趋零后，单调无界 lifted angle 的模 (2\pi) 相位确实逼近每个相位。

因此，**C303 当前仍为继续验证**。普通 (F=\nabla f) PPA 桥是独立的一阶结果，研究价值和 C303 的关系均有限；真正能改变 PPA/GPPA 贡献判断的最小证据是完成 D1–D7 的带动量离散留域证明，特别是离散 integer-step crossing 的 barrier 门。若只完成普通桥，不能把 C303 升级为惯性 PPA 主要贡献。

### 6.1 可补足 D6 的连续步长参数

整数步穿越并非不可处理。固定 ((x_k,v_k))，对 (	auin[0,1]) 令
[
\beta(\tau)=\frac{\tau h_k}{1+a\tau h_k},
\qquad
\lambda(\tau)=\tau h_k\beta(\tau),
\qquad
 y(\tau)=J_{\lambda(\tau)\nabla\chi_a}(x_k+\beta(\tau)v_k).
]
全局强单调性给出 (y(\tau)) 的连续性，且 (y(0)=x_k)、(y(1)=x_{k+1})。对 (	au>0) 定义 (v_\tau=(y(\tau)-x_k)/(\tau h_k))，则它满足同一个惯性隐式 Euler 关系，步长为 (	au h_k)。若 D4 的展开对所有 (	auin[0,1]) 统一成立，则 (sup_\tau\|w_\tau\|\le\|w_k\|+Ch_k^2=O(h_k))。

若 (y(\tau_*)) 首次接触 radial 边界，(s_i(y(\tau_*))=0)，则
[
s_i(x_k)=s_i(y)-\tau_*h_k\nabla s_i(y)\cdot(Y(y)+w_{\tau_*})+O((\tau_*h_k)^2)<0,
]
因为 (\nabla s_i\cdot Y\ge m(\theta))、(w_\tau=O(h_k))、且 (h_k=o(m(\theta)))。这与 (x_k\in D) 矛盾；入口角边界同理由正切向漂移排除。该参数化提供了把 D6 从“整数步首次接触”改成严格连续路径 barrier 的可执行闭合路线，但仍需逐式写出 uniform remainder 和有限前缀常数。

### 6.2 对 v2 桥稿的独立复核

仓库 `c303_discrete_bridge_v2.md` 已修正一个重要问题：不能预先断言 (alpha>2/3) 对所有 bootstrap 指数均足够，而应先由离散角度上界得到某个有限 (p)，再选
[
\alpha>\max\{2/3,p/(p+1)\}.
]
V3 的全局强单调 coverage、V7 的 (w) 递推和 V11 的边界 strip 修正均是合理的。V12 最终仍须写成线段积分：若 (widehat x) 是 ([x_{k-1},x_k]) 上的首次边界交点，则用 (
abla s_i(\widehat x)\cdot v_k) 的正性，并以 (Y(x_k)-Y(\widehat x)=O(h_k))、(w_k=O(h_k)) 控制端点替换误差。还需说明小步长和 (mu<e^{2\pi}) 保证该线段位于同一物理 lift 图中。当前 v2 仍是“继续验证”，但已具有一条可执行的完整 PPA/GPPA 证明路线；普通 (
abla f) PPA 桥不承担这一结论。
