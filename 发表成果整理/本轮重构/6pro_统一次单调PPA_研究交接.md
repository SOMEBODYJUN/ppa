# 给 6pro 的研究交接：联合状态、曲零簇与变化核

2026-10-14 UTC。以下是可直接复制给下一位数学研究助手的三个提示词。它们不是已证明结论，也没有实际调用 6pro。先看[本轮报告](次单调PPA统一框架_证明与边界_2026-10-14.md)；具体版本以规范正文及 CLAIMS 的注册状态为准。提交前后 Git hash 由本批 audit 记录。

共同纪律：先读 README、AGENTS、RESEARCH_PROTOCOL、CLAIMS、RESEARCH_STATE、FAILED_ROUTES 与相关 canonical；只用仓库 academic-writing-skills 的数学证明/审查模式，不建多技能流水线。固定完整 F、算法、步长、完整零集、真 inf 残差与全部输出。Python 先做边界、算术和反算，解析证明承担全称。文献比较读一手固定版本，不凭摘要。保持主稿、摘要和正文编号不变。不要把下列 refuted 版本重新当作有希望的 conjecture。

## 提示词一：从完整原图自动生成保记忆的有限状态证书

你是数学合作者。请研究“有限原生状态的近端收敛证书”，不是重述 Caristi 或以实际轨道定义一个未知长度上界。起点是：

- research/canonical/unified_ppa_joint_certificates.md，特别 JP1–JP3、JP7–JP9；
- research/canonical/unified_ppa_raw_calculus.md；
- research/canonical/generalized_ppa_modulus.md 的 NGK-3–8；
- research/novelty/2026_10_14_unified/independent_review.md；
- research/code/unified_ppa/joint_verify.py。

### 已证内容及尝试

第一轮把两个向量范数损失和独立真 EB 合并，仍丢掉 GU3 法向/真实距离关联。原图投影和分支条件必须共同保存。PSD 外松弛是安全充分法，不能假装保留正共线/秩。

第二轮保一步距离—步长关系。完整 F(y)={y,y³} 的任何独立最坏距离/步长尾和都发散，但原图给 s=t−q，W(t)=t 精确闭合。因此联合长度确实强于独立尾和门。旧平方下降/壳层 Hölder 半阶门亦能构造 W，不能错误宣称旧 C208 全部失败。

第三轮发现距离状态本身不完备。完整闭半代数图
F((0,u))={(u+u³,ξ):ξ∈R}，其余 F 空，lambda1，完整零集0，真残差 |u+u³|。
完整 T(x1,x2)=(0,g(x1))，g+g³=id；T²0，全输入、全部政策两步到零且长度≤3||x||。
但精确径向关系含 (g(t),sqrt(t²+g(t)²))；虚假反复拼接产生不可和成本，排所有有限的仅距离 W。此宽完备性版本已被反驳。

已修正的父接口记录原生有限状态 i=χ(x)，所有实际转移保 E_ij(t)，并测试
W_i(t)≥sup[s+W_j(q)]，共同 tau 连续非减且 tau<t，另完整 coverage 和严格 finite-prefix 留域。两步例用 χ区分 x1=0，W0=3t,W1=t 即闭。

### 精确待攻目标

固定有限维、lambda>0、完整闭半代数图 F、完整闭非空半代数 S=zer F，以及认证紧输入窗 K。完整 J 在 K 每点非空，全部输出联合有界且留在 K。另有统一的正壳层距离下降，并且所有完整政策确有共同的物理尾预算 m(d(x,S))，m(0)=0 且 m(t)→0；因此全部零输入已经驻定。

问题：能否从原图有限多项式数据有效构造一个有限半代数状态描述 χ及可有限表示的 W_i，使同一完整关系通过状态版联合长度与趋零门？如果不可能，给满足全部上述前件的完整反例，并证明每一种允许的有限状态/势语法都失败。不要只反驳 SDP 层或某个选出的势。

需要先严定“有效构造”和势的语法：可以先限定有理幂有限和、有限 semialgebraic partition、认证代数参数；更宽的 semialgebraic W 若声称完备须独立证明。证明预算的存在性不等于算法已经能求出它。

保留原空间、同 F、lambda、S、r_F 和全部 J 输出。不能换到一个人为共轭的单调算法后当作原物理长度证书。也不要以“假设存在能认证的 W”作为主定理的唯一新前件。

### 可接受成果与失败记录

优先产出可由原始结构认证的有限 feature calculus：和/逆/拉回怎样传递状态，什么时候可以消元，什么时候产生跨步错误重配。至少完整恢复 diagonal、GU3、两支标量例及 nilpotent 例。

若全完备目标太大，做一个有自然原始描述的非平凡子类，并给一个此前只有纯距离接口不能认证、状态接口能够认证的全图区域。声明同一步长/政策的准确差异，不假称排尽经典方法。

已试 Bellman 无限迭代：存在形式上的最小上解，不保证半代数、连续、有限表示或可计算。量词消去只处理有限一步，不能自动关闭无限 horizon。请至少再尝试两条不同证明路线，明确剩余承重引理，再交接，不给空泛“继续研究”。

## 提示词二：曲零簇的原始联合证书与全图远根屏障

你是数学合作者。请把仿射方向证书推进到真正曲零簇，但不能先造一个满足期望收缩的近端映射。起点：

- research/canonical/unified_ppa_curved_geometry.md；
- research/candidates/coupled_holder_structural.md，SC14–SC15；
- research/canonical/amplitude_circle_hamilton.md；
- research/canonical/amplitude_circle_damping_threshold.md；
- research/canonical/physical_rleb_gppa.md；
- research/code/unified_ppa/curved_verify.py。

### 已证内容及尝试

第一轮直接把输入最近锚处的法/切投影替换成曲流形投影。Taylor 曲率误差尺度 O(d^(2gamma))，但证明需要先保证全部输出位于共同 chart；缩输入管不能排原图远端完整根。

修正后，从输出最近点处的原始法向正耗散和切向 Holder 上界，在整个闭R管认证同一 reachrho。空球估计给
d(y+lambda w,M)≥(1+lambda m)s−E_R s^(2gamma)，
E_R=lambda²C²/[2(rho−(1+lambda L)R)]。
至少一连续模式及 boundary homotopy degree 给整输入管 coverage；全部原根、zero吸收、留管、有限长度在同一参数窗闭合。
gamma>.5可缩窗，gamma=.5要求m>lambda C²/(2rho)。圆给临界等号失败。原定理若任意gamma>0只检验R端点，是已修掉的错误。

第二轮圆反例：未补偿 w=m s e_r+c|s|gamma e_t 的输入半径平方
(1+(1+lambda m)s)²+lambda²c²|s|^(2gamma)。
gamma<.5时两侧近零输出都进入外侧，内侧输入覆盖失败；保留大管又可能给零输入非零完整根。不是“满足全部前件但收敛失败”的反例。
固定设计lambda的精确圆弦补偿可处理每个0<gamma<1，但函数依赖设计步长，是机制构造。只截断到二次补偿在gamma<.25再次丢内侧覆盖。

### 精确待攻目标

寻找一个非人为拼接、全空间自然原图类，其已识别零簇 M 是紧C²流形，原图由优化、平衡、对称拟合、非线性方程或 Hamilton 原始函数组成。允许 M 外其他零点；不得假设全空间相对M收缩。

从原始曲率、增长、角度、damping 或组成项参数证明一个明确局部输入管的所有完整近端输出都进入受控输出窗；必须独立给全输入 coverage 与远端完整根屏障。随后把同锚反射/方向、完整trueEB、兼容、物理位移和留域逐项接到统一证书。

真正希望解决的是 gamma≤.5 的曲率耦合或 Hamilton 核不可见方向；不能将原始法向sector失败简单改称“不满足任何次单调”。用曲率补偿、耦合能量或更完整方向状态均可，但补偿应由真实模型推导。

必须先检查旧 C256/C257 已闭的同模型范围，不能重新包装圆阻尼参数族。一般紧M与真实全空间图的屏障若做不出，应固定一个清楚的新模型和未闭的最短引理。

### 可接受成果与比较

给完整 F、完整S、lambda、输入域、全部纤维的解析描述或承重存在性证明。验证zero输入、跨符号、非孤立M、切向大步、远根、damping临界系数。不能删支、取任选图值、把selectednorm当trueinf或凭数值轨道。

证明自然性、有效性、应用作用、新颖性分开评价。若已有更短的机械能、KL或普通对偶PPA证明，如实保留。目标可以是更容易认证、参数更好、全部不确定政策或物理sharp率；不能只说某个旧证书失败。

若使用Euler/指数推额外零点，另核连续单值完整J、隔离边界、局部吸引管和全局总指数；当前多值曲管定理不自动给此桥。需要时先建立单值子类，再作准确的经典degree导入。

## 提示词三：从原图推导非单射/变化核的可实施物理停止预算

你是数学合作者。请研究GPPA实际物理输出的停止与跨步核变化，不能仅将一个抽象h加进C249后求和。起点：

- research/canonical/unified_ppa_inexact_interfaces.md；
- research/topics/inexact_ppa/real_graph_stopping.md；
- research/topics/inexact_ppa/sharp_precision_frontier.md；
- research/canonical/physical_rleb_gppa.md；
- research/canonical/unified_ppa_joint_certificates.md；
- research/code/unified_ppa/inexact_verify.py。

### 已证内容及失败版本

算法必须先定义：真实图 w∈F(y)，缺陷
e=v_k(x)−v_k(y)−lambda w，接受关系包含所有通过规则的输出。真残差仍是 inf{||w||:w∈F(y)}。不要假设v_k可逆或v_k(x)−e有物理原像。

第一轮由核误差自动提升到物理长度，被精确零纤维自由漂移反驳；连续逆也不保可和长度。

第二轮从图方程闭合F=Id的固定/移动正交投影。固定P相对误差sigma<1皆物理有限长；任意movingP的锐统一门sigma<sqrt[2lambda/(1+2lambda)]，二维临界旋转恒范数。全部接受输出、全域种子和zero吸收都解析核实。

零见证陷阱：Px=0而x非zero时，sigma<1下唯一接受输出是zero。任意始终非zero的真实图逼近序列不能有限停止，尽管精确种子存在。一般非单射核必须提供可计算zero证书分支，或另一个明定终止机制。

第三轮宽变化度量安全猜想已经否定：F=I+3K强单调，lambda=.1，真实e=0，M_k沿当前x转动且谱恒{1,.1}。完整更新唯一
y=(20I−30K)x/31，radius²增益1300/961>1；每固定M谱半径²10/31<1。
所以“uniformSPD＋strongmonotone＋exactPPA ⇒任意moving核收敛”不是开放猜想，而是refuted。

### 精确待攻目标

在一个有原始组成数据的非线性类中，同时认证：

1. 可见方向耗散；
2. 核纤维内的物理运动；
3. 跨步核变化或状态传递；
4. 全部输入精确种子 coverage；
5. 全部接受输出的trueEB与物理可和性；
6. 严格非零见证内层余量及zero见证分支。

接受条件只能读取当前x,y,w,e及已认证原始常数，不能运行时查d(x,S)、d(y,S)或精确J。可先做固定秩、非线性核；或有限族变秩核配合可认证状态转移。任意moving核不是目标前件，必须明确新结构怎样排掉上述旋转反例。

保持原F、完整S、物理范数和所有误差方向。希望同时保住RL非线性停止余量、inverse/cohypo的大步长优势、GU3方向优势及非几何joint长度，而不是对每一分支重新换一个算法。

### 现有部分接口和真正断点

同点近似成员资格有可计算证书：
G_y∩B(wtilde,delta)非空。
用Eplus=||etilde||+lambda delta、Wminus=(||wtilde||−delta)_+、Wplus=||wtilde||+delta，保守编译已闭合若干真图停止预算。这只认证同输出点的membership；邻近真图点还需delta_y与核连续模。

真图oracle并非自动可得；“求解器残差小”不能代替membership证书。精确种子存在亦不等于任意inner method有限停止。
经典变量度量PPA、相对误差PPPA、非精确KKT框架必须逐定理核同一物理算法；若已有共同Lyapunov或可和metricvariation短证明，应将它作为正面基线，重新评估新结果的价值。

至少两条不同路线：原图隐式消元的物理lifting；联合状态/度量误差的potential证书。若仍失败，交付精确缺失引理、完整反例与缩窄目标，不把“需要更强regularity”当成果。

## 共同交付与判停门

每题先冻结精确statement，再做解析证明与独立反审。新代码放research/code/<topic>/，记环境、精度、参数、命令与输出。能闭就按协议进入canonical及CLAIMS；有fatal objection就保candidate或refuted。不要以研究报告、漂亮图或有限网格提升状态。

优先顺序：题一最高，因为它决定统一理论究竟能保哪些信息；题二寻找自然原图的承重桥；题三寻找可实施物理算法入口。三题可分别推进，不要求全部成功才能交付已经证明的认识。
