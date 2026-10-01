# 下一条结构分类定理：可用工具与优先权边界审计

日期：2026-09-20。角色：工具级原始文献审计；不重审原 RLEB，不再以特殊尖点族代替中立母空间的类比较。本文是团队中间研究报告。

## 0. 结论

**确有可用的扩张、局部替换、固定点集保留和步长转换工具，但本轮没有核到一条可直接完成下述全部要求的现成定理：**在任意给定 RLEB 认证对象附近，保留同一完整 resolvent 身份、精确非点零集、真实全纤维 EB、共同实际迭代尾及允许步长量词，同时离开每个有界 LT 认证层。

这不是“工具完全没有”，也不是“多找一个反例即可”。当前缺口是**对象级闭合／变形引理**。文献把它分解到可以具体建设的程度：

1. 完整 resolvent 的坐标编码本身已经成熟，固定一个步长时容易保留。
2. 单步 Lipschitz／Hölder 模可用扩张与局部替换控制。
3. 精确固定集可通过 trace 加额外排除零残差条件控制。
4. 共同实际尾和全纤维 EB 不由前面三项自动推出；这是实质耦合瓶颈。
5. “存在任意正步长 LT 证书”比固定步长结论多一层步长谱问题，不能用一个坐标中的非 Lipschitz 自动排除。

## 1. 原始工具核查表

下列编号按所链接的原始公开版本；有 arXiv 时不猜未核对的期刊 DOI。表中“不能”指该原文定理不足以直接推出，不是断言任何推广都不可能。

| 原始来源与编号 | 已核假设及结论 | 可直接供给什么 | 未供给什么 |
|---|---|---|---|
| Davide Ravasini, *Generic uniformly continuous mappings on unbounded hyperbolic spaces*, JMAA 538(1) (2024), 128440；[DOI 10.1016/j.jmaa.2024.128440](https://doi.org/10.1016/j.jmaa.2024.128440)，[arXiv:2308.15277v2](https://arxiv.org/html/2308.15277v2)，Lemma 3.2、Theorem 3.3 | 完备无界 hyperbolic 空间；固定非零连续非降凹模；有界集一致拓扑。泛型映射的全局模等于允许模。局部压平映射在小球恒定、远处恒等，Lipschitz 常数可显式控制。 | 模饱和的 Baire 机制；压平后插入局部模型；利用正则性预算余量。 | 没有固定共同 S、共同尾、EB 或 PPA 步长谱。模饱和见证可逃向无穷，不能直接推出某固定解点附近非 Lipschitz。 |
| Christian Bargetz, Simeon Reich, Daylen Thimm, *Generic properties of nonexpansive mappings on unbounded domains*, JMAA 526(1) (2023), 127179；[arXiv:2204.10279v3](https://arxiv.org/pdf/2204.10279)，Lemmas 5.3、5.5 | 完备无界 hyperbolic 空间。5.3 提供局部压平且外部恒等的近非扩张映射；5.5 从具有严格余量的收缩出发，在保留指定球内原映射的同时制造接近最大允许斜率的点对。 | 真正的对象级局部替换，而不只是一个参数例子；边界拼接和 all-pairs 控制已有可复用证明。 | 起点严格收缩不可能固定非点 S；其替换不保迭代尾和真实 EB，不能直接在本项目的共同固定集层应用。 |
| Christian Bargetz, Michael Dymond, *σ-Porosity of the set of strict contractions in a space of non-expansive mappings*, Israel J. Math. 214 (2016), 235–244；[arXiv:1505.07656](https://arxiv.org/pdf/1505.07656)，Lemmas 2.5–2.7、Theorems 2.1–2.2 | Banach 空间内有界闭凸域；非扩张自映射的一致拓扑。紧支撑域变形使局部斜率增大，同时保全局非扩张性，导出 σ-porosity。 | 局部斜率逃逸的定量孔隙证明模板。 | 不是固定多解集 WPO 空间；既定吸引域、极限回缩及尾率不在保留清单内。 |
| Daniel Azagra, Erwan Le Gruyer, Carlos Mudarra, *Kirszbraun’s theorem via an explicit formula*；[arXiv:1810.10288v3](https://arxiv.org/pdf/1810.10288)，Theorem 2、Corollary 3、Theorem 8 | Hilbert→Hilbert 部分 Lipschitz 映射可同常数全域扩张；FNE 部分映射可扩张为全域 FNE；满足特定强双 Lipschitz 不等式的部分映射可保其常数扩张。 | 保 trace 和单步常数；可用来完成局部坐标／共轭变换。 | 一般双 Lipschitz 不够，原文 Example 5 即给拓扑障碍；扩张不保精确 Fix 或既定尾。强双 Lipschitz 扩张也不能制造非 Lipschitz 共轭。 |
| 同三作者，*Explicit formulas for C^{1,1} and C^{1,ω}_{conv} extensions of 1-jets in Hilbert and superreflexive spaces*, JFA 274 (2018), 3003–3032；[arXiv:1706.02235](https://arxiv.org/pdf/1706.02235)，Theorems 2.4、3.4 | 满足相应 Whitney／凸 Whitney 二点相容不等式的 jet，具有保梯度 Lipschitz 预算的显式延拓；凸版本还保凸性。 | 当研究对象限定为梯度／次梯度结构时，避免把任意向量场错误当梯度的工具。 | 不能把任意局部 graph patch 强行延拓为同一个 proximal 类；不保预定零集、EB 和迭代尾。 |
| Heinz H. Bauschke, Xianfu Wang, *Firmly nonexpansive and Kirszbraun–Valentine extensions: a constructive approach via monotone operator theory*, Contemporary Mathematics 513 (2010), 55–64；[作者原文](https://cmps-people.ok.ubc.ca/bauschke/Research/c10.pdf)，Theorems 3.1、3.4–3.6 | Hilbert 空间；通过 Fitzpatrick／proximal-average 的极大单调扩张，构造全域非扩张或 FNE 扩张；额外范围条件下控制扩张的像闭包。 | 从局部映射数据提升到完整单调图的现成构造。 | 像集控制不等于零集或吸引域控制；没有保原实际尾、原 EB 的断言。 |
| Heinz H. Bauschke, Xianfu Wang, Liangjin Yao, *General Resolvents for Monotone Operators: Characterization and Extension* (2010 章节)；[作者原文](https://cmps-people.ok.ubc.ca/bauschke/Research/c11.pdf)，Theorem 8.1 | 反身 Banach 空间，满足文中条件的基准映射 F；F-firmly nonexpansive 部分映射可扩张为全域同类，且是相应广义 resolvent。 | 若将来引入 Bregman／对偶映射坐标，这是现成表征与扩张支点。 | 这不是任意非线性坐标下保持同一个欧氏 PPA 的结论；不能混淆广义 resolvent 与 J_{λA}。 |
| Dan Butnariu, Simeon Reich, Alexander J. Zaslavski, *Asymptotic Behavior of Relatively Nonexpansive Operators in Banach Spaces*, J. Applied Analysis 7(2) (2001), 151–174；[DOI 10.1515/JAA.2001.151](https://doi.org/10.1515/JAA.2001.151)，[作者原始 PS](https://math.haifa.ac.il/dbutnaru/publications/but-rei-zas-jaa.ps)，Lemmas 4.1–4.2、5.1 | 固定非点闭凸集 S；共同相对 Bregman 下降、投影 P 与原文 Assumption A。T_η=ηP+(1−η)T 保母类，并引入到 S 的严格下降；附近算子有可统一的晚期控制。 | 最接近本项目的“固定多解集＋保类变形＋泛型收敛”先例。 | 母类预设共同 Bregman 下降；并非任意 RLEB 或任意共同实际尾层。证据来自工作区原始论文文本，而非只读摘要。 |

### 使用上真正有区分力的判断

“Lipschitz 类在 Hölder 模球里第一纲”属于成熟函数空间现象。把它通过**开放坐标映射**拉回，或在凸层中沿一个粗糙方向作凸组合，也属于标准范畴套路。论文的主要新内容不能放在这些步骤本身，而应放在：所构造的对象级坐标／闭合操作为何同时保留实际动力学和完整图证书。

## 2. 为什么扩张定理不等于所需变形定理

以下为本轮独立校准，不归作上表文献的新定理。

### 2.1 固定 trace、精确固定点集、尾率是三件事

取 K=[−1,1]^2，S=[−1,1]×{0}。映射

\[
P(p,r)=(p,0),\qquad R(p,r)=(p,-r)
\]

均为非扩张，均有 Fix=S，且在 S 上均为恒等；但 P 一步收敛，R 在 r≠0 处为二周期。因此即使扩张保持非扩张和**精确**固定点集，也不保证 WPO，更不保证共同尾。

加强到 FNE 仍不能保给定速度。对 a∈[0,1)，

\[
T_a(p,r)=(p,ar),\qquad
\|T_a^n(p,r)-(p,0)\|=a^n|r|.
\]

它们都是 FNE、Fix=S、极限回缩同为 P，但 a>q 时不满足任一固定倍数 Cq^n 的共同尾。故在固定 tail 层内套用 FNE 扩张，需要另外证明动态预算闭合。

### 2.2 McShane 型公式只能解决单步 trace

标量 L-Lipschitz 数据 g:E→R 的公式

\[
\widetilde g(x)=\inf_{z\in E}\{g(z)+L d(x,z)\}
\]

保 trace 与 L-Lipschitz 性；以 d^γ 替代 d 可作标量 Hölder 延拓。把 S 放入 E 可锁定 S 上值，但公式没有约束 \(\widetilde T^n\)、新不动点及全纤维残差。向量值逐坐标延拓还会改变常数，不能冒称保原 Hilbert 最佳常数。McShane 1934 原文此次未取得可核页，不填造其定理号；这里仅使用上式的直接验证及已读的现代原始扩张论文。

### 2.3 全纤维 EB 的保留必须逐对象检查

设 λ>0，T 为全域连续映射。定义完整图

\[
A_T(y)=\{(x-y)/\lambda:T(x)=y\}.
\]

则 J_{λA_T}=T；图为 graph T 的可逆线性像，因而闭。此时真实残差是

\[
\operatorname{dist}(0,A_T(y))
=\lambda^{-1}\inf_{x:T(x)=y}\|x-y\|.
\]

局部 extension/patch 可能增加某个 y 的输入纤维，从而降低这个 infimum。只估计新选定的一条轨道残差，或只检查一个逆分支，均不能保证原 EB。此处完整图编码不是障碍，**受约束的输入纤维几何**才是障碍。

## 3. 共轭／shear：有用，但必须登记它改变的预算

令 h:K→K 为同胚，h(S)=S，令 \(T^h=h^{-1}Th\)。直接代数给

\[
(T^h)^n=h^{-1}T^nh,\quad
\operatorname{Fix}(T^h)=h^{-1}(S),\quad
\Pi_{T^h}=h^{-1}\Pi_T h.
\]

故 WPO 性和固定集可以随共轭运输。这是基础动力系统事实，不能作为新颖性卖点。更具体地，若 h^{-1} 的模为 θ 且 T 的共同尾为 ω_n，则

\[
\sup_x d((T^h)^nx,\Pi_{T^h}x)\le\theta(\omega_n)
\]

（非紧域应把 h(K_0) 对应的尾预算写入公式）。若 h^{-1} 为 C-Lipschitz，尾变成 Cω_n；若仅 α-Hölder，则变成 Cω_n^α。**这未必还在同一个精确尾层。**

两个重要限制：

1. h 和 h^{-1} 都局部 Lipschitz 时，T 局部 Lipschitz 当且仅当 T^h 局部 Lipschitz。因此光滑／双 Lipschitz shear 不能把 LT 的正则端点变成非 Lipschitz 对象。
2. 粗糙 h 能改变正则性，却也改变 RL、EB、尾预算。只知道 h 连续且接近恒等不足以保这些数值条件。非线性 h 一般也不与步长重参数化交换。

若要用此法，应先证明可量化的“允许共轭群作用”或“有预算损失的层间态射”，再问其轨道／切片的范畴大小。不能从单个粗糙共轭推断整个母类的 residual 性。本轮未核到在同时固定 S、Π、共同原范数尾和真实图 EB 的 WPO 母空间中，现成的 generic shear/conjugacy 定理；这是检索与已读文献边界，不是无人研究的证明。

作为收敛闭合的另一支点，Ioan A. Rus、Adrian Petruşel、Marcel Adrian Şerban, *Weakly Picard operators: equivalent definitions, applications and open problems*, Fixed Point Theory 7(1) (2006), 3–22，[原文](https://www.math.ubbcluj.ro/~nodeacj/download.php?f=061rus.pdf)，Theorem 6.2 从闭 Q-graph contraction 得到点态 WPO、有限长度和显式几何尾；Theorem 4.1 用 Caristi 不等式给收敛。它们能帮助设计一个保尾的中立不变量，但**不能先把母空间改成 graph contraction，再未经嵌入证明声称覆盖全部 RLEB**。

## 4. 步长谱：已有精确接口，尚不是所需全分类

应分别记

\[
\Sigma_{\rm wd}(A)=\{\lambda>0:J_{\lambda A}\text{ 全域单值连续}\},
\]
\[
\Sigma_{\rm Lip}(A)=\{\lambda>0:J_{\lambda A}\text{ 在指定域 Lipschitz}\},
\quad
\Sigma_{\rm conv}(A)=\{\lambda>0:J_{\lambda A}\text{ 满足指定收敛性质}\}.
\]

局部图表版本必须另写共同输入域和图定位；不要把局部 selector 的谱写成完整图的谱。

### 4.1 已读的原始定理

**Heinz H. Bauschke、Walaa M. Moursi、Xianfu Wang**, *Generalized monotone operators and their averaged resolvents*，[arXiv:1902.09827v1](https://arxiv.org/pdf/1902.09827)：Fact 2.1、Corollary 2.13、Theorem 2.16、Proposition 3.8、Corollary 3.10、Proposition 6.3、Theorem 6.4 已读。

它们给出全域 resolvent、广义单调性与 conically nonexpansive／averaged 的精确转换。尤其最大 \(\rho\)-comonotone 且 \(\rho>-1\) 时 J_A 全域单值；\(\rho=1/(2\alpha)-1\) 对应 α-conically nonexpansive。按这些定理缩放，最大 cohypomonotone

\[
\langle x-y,u-v\rangle\ge-c\|u-v\|^2
\]

给 μ>c 的良定完整 resolvent；μ>2c 时 J_{μA} 为 \(\alpha=\mu/[2(\mu-c)]<1\) 的 averaged 映射。此为已知结构嵌入，不是新谱理论；也不附带统一几何尾。

### 4.2 直接计算的校准：良定与收敛谱可完全不同

若 B=A+cI 极大单调，则对 0<λ<1/c，

\[
J_{\lambda A}(x)
=J_{\frac{\lambda}{1-c\lambda}B}
\left(\frac{x}{1-c\lambda}\right),\qquad
\operatorname{Lip}J_{\lambda A}\le\frac1{1-c\lambda}.
\]

这给一个良定/Lipschitz 区间，不给收敛。取 \(A(p,r)=(0,-cr)\)，其零集为整条水平线，且

\[
J_{\lambda A}(p,r)=\left(p,\frac{r}{1-c\lambda}\right).
\]

完整良定谱为 \((0,\infty)\setminus\{1/c\}\)，从所有初值收敛到零集的固定步长谱却为 \((2/c,\infty)\)。在 λ=2/c 出现二周期；λ=1/c 处非零法向输入无解、零法向输入多解。故“存在某个良定小步长”不能代替“存在某个收敛步长”，步长谱也不应预设为从零开始的区间。

### 4.3 Prox-regular 的局部化不能消失

**R. A. Poliquin、R. T. Rockafellar**, *Prox-regular functions in variational analysis*, Trans. AMS 348 (1996), 1805–1838，[作者原文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf)：Theorem 3.2、Theorem 4.4、Theorem 4.7 已读。它们给 f-attentive 局部次梯度图的 hypomonotonicity、小步长单值 Lipschitz proximal 图表及图流形结构。**局部化是结论的一部分。**

例如光滑 \(f(x)=x^2-x^4\) 在 0 附近 prox-regular，但原始完整 resolvent 在输入 0 满足

\[
J_{\lambda\partial f}(0)
\supseteq\left\{0,\ \pm\sqrt{\frac{1+2\lambda}{4\lambda}}\right\}
\quad(\lambda>0).
\]

这说明不能从局部 selector 良定推出原始全图 resolvent 良定。上式不质疑原定理，它恰恰展示为何 f-attentive/local graph localization 必须保留。

另核 **Poliquin、Rockafellar、Thibault**, *Local differentiability of distance functions*, Trans. AMS 352 (2000), 5231–5241，[作者原文](https://sites.math.washington.edu/~rtr/papers/rtr170-LocalDiffDistance.pdf)，Theorem 1.3、Corollary 2.2：局部 prox-regular 集、截断法锥 hypomonotonicity、局部单值 Lipschitz 投影之间已有精确关系。可用于特定几何子类的图表，但不是任意 RLEB 算子的天然结构。

## 5. 建议下一核心引理的验收清单

不预设 LT 必定第一纲。先对中立对象层 Y 建立或否定下面的闭合能力。对每个有界 LT 层 L_{m,j}、T∈Y∩L_{m,j} 和每个对象邻域 U，找到 G∈U∩Y，使 G∉L_{m,j}，并逐项检查：

1. **对象身份**：G=J_{λA_G} 是完整解映射，不是选中分支；若保所有步长，给 A_G 的同一个完整图。
2. **共同域及精确零集**：G(K)⊂K、Fix G=S，不能只证明 S⊂Fix G。
3. **动态闭合**：同一 tail ω 的不等式成立；若只有 Cω 或 ω^α，明确是层间映射，并证明这种改变不会偷换比较分母。
4. **RL 闭合**：全部点对／分支，且常数与尺度保持在允许预算内。
5. **EB 闭合**：检查 \(\inf_{Gx=y}\|x-y\|\)，而非所选输入残差。
6. **严格兼容**：新常数代入后仍留正余量；边界饱和对象是否可先移入严格内层，需另证稠密性。
7. **步长量词**：若比较 LT_{∃μ}，必须证明改变 μ 不能恢复证书，或者先有覆盖全部允许 μ 的可数局部化定理。仅固定 λ 逃逸不够。

完成这一引理后，闭层＋可数并的 Baire 步骤通常很短；做不成时，应记录究竟哪个结构约束导致刚性。这样的“不存在某种变形／某些层不同”也是分类结果，不应为了期待的优势删除约束。

## 6. 优先权与价值终判

- **高先例风险／应直接引用**：单步模饱和；压平／局部斜率提升；Lipschitz/FNE/Whitney 扩张；WPO 的轨道分解；固定非点集上的投影混合泛型收敛；单调/共单调与 resolvent 的常数换算。
- **仍可形成实质新结果的位置**：在中立 PPA 动态层中证明保全纤维 EB、共同实际尾、完整图和步长身份的对象级闭合定理，再由它推出 RLEB/LT 的类位置；或者证明这些约束的刚性导致某个期待的泛性结论不成立。
- **本轮不能声称**：已检索穷尽所有 generic WPO/conjugacy 文献；没人做过类似变形；RLEB 的大类结论已有证明。原始工具阅读目前支持的是明确的 construction gap，不是预判分类答案。

给监督人的一句话：**目前主要不需要用户补数学材料或选择“想要哪个结论”；需要团队继续完成一个具体的构建性桥梁——让局部正则性自由度与全轨道、全纤维约束在同一对象空间中真正兼容。**
