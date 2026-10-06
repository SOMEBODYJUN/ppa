# 自然完整母空间的构造义务

<a id="ocf-specification"></a>
## 先冻结同一个比较问题

总体目标仍是 [RESEARCH_STATE](../../RESEARCH_STATE.md#active-frontier) 中的 \((\mathfrak X,\mathfrak I,\mathcal R,\mathcal L,\mathcal M)\)：\(\mathfrak X\) 的成员必须是明确的完整原关系，不能按认证参数预先挑选；\(\mathfrak I\) 是自然且非退化的大小量尺；三类谓词在同一对象/空间/拓扑/目标下定义。需明确计数 \(F\) 还是 \((F,\lambda)\)，以及某步长/全部步长、某选择/全部选择的量词。一个紧源映射层可以是工具，但 [C142](../operator_space.md#os-compact-barrier) 已阻止它直接充当极大单调共同分母。

下面记录可研究的八项**开放构造义务**。来源提出的成功目标在此作为问题重写，不把它们升级成定理；某个充分工具失败也不否定全部母空间构造。

<a id="ocf-a"></a>
## A · 同尾可行选择的自由度

在 [C131](../operator_space.md#os-tower-proof) 的同一非空紧 \(K\)、连续 \(T\)、统一有限长度尾和固定集 \(S\) 下，塔 \(V_j\) 已有明确规范定义。给定步长 \(\lambda>0\) 与非减残差上界 \(\psi\)，定义
\[
\mathcal Q_{T,\psi}(x)=\{y\in K:d(y,x)+V_0(y)\le V_0(x),\ V_j(y)\le V_{j+1}(x)\ (j\ge0),\ d(y,S)\le\psi(d(x,y)/\lambda)\}. \tag{OCF1}
\]
若要称其为闭可行对应，另须 \(\psi\) 在使用区间连续或独立证明末条约束闭；非减本身不能保证闭性。要求构造非平凡连续选择 \(U\)，并在一个参数中立区域证明选择丰富性/该层的母空间位置。C131只给已经满足这些约束的 \(U\) 的尾；使用 [C132](../operator_space.md#os-fiber-eb) 生成新紧源关系并转真EB时，另要求 \(K\) 位于实赋范空间（可取Hilbert）且 \(d\) 为其诱导范数距离，以定义 \((x-u)/\lambda\)。抽象紧度量空间没有默认的图值相减运算。

投影塔的单点刚性与同精确全窗尾层可变的反例在 [operator_space](../operator_space.md#os-isometry-proof) 后的诊断中；长度尾、Cauchy尾和逐点位移不得混用。[C133-v2](../operator_space.md#os-successor-proof) 的后继选择保持同一极限，但不提供非平凡选择。轨道漏斗方案须独立构造嵌套、转移不变、规定直径的集合及其连续选择；闭或非凸值不满足未核的选择定理条件。

<a id="ocf-b"></a>
## B · 实际尾坐标的保纲桥

固定 [OS-PHI](../operator_space.md#phi) 的完整紧源 \(T\)-only 空间 \(X\)、全时间度量、固定 \(K,S\) 和 \(\Phi=(w,m)\)。其连续、proper、闭Polish像与紧纤维已有 [C06](compact_t_observation.md#ct-proper) 的证明。目标是找一个有数学理由的非退化 Polish 区域 \(X_0\) 和 Polish 基底 \(Z_0\)，证明该**同一映射**的 category-preserving 性：任何余稀集合在 \(Z_0\) 的逆像余稀于 \(X_0\)。

proper 不给保纲，连续像不自动 Polish；[局部观测的域外自由度反例](../operator_space.md#local-loss) 也禁止把紧源结论授予完整全空间图。“direct integral”没有自然概率测度身份。

<a id="ocf-category-import"></a>
### 已核的一手类别转移接口

[Melleray–Tsankov 作者PDF](../LITERATURE.md#lit-mt-category) 的 Appendix A、印刷p.25：连续 \(f:X\to Y\)（两空间Polish）保纲，当且仅当每个非空开 \(O\subset X\) 的像非第一纲（Proposition A.3）；若再给 Baire可测 \(A\subset X\)，则 \(A\) 在 \(X\) 余稀，当且仅当对 \(Y\) 中余稀的 \(y\)，\(A\cap f^{-1}(y)\) 在该纤维余稀（Theorem A.5）。空纤维按相对拓扑读；不把“余稀y”擅改为“每个y”。

应用到 \(\Phi|_{X_0}:X_0\to Z_0\) 需依次核两空间Polish、映射连续、非空开像的非第一纲性和欲比较集合的Baire可测性。C06仅提供前三项中的空间/连续信息；保纲仍是实质开放义务。作者定理已核不认证特定 \(\Phi\) 的保纲，也不核源稿当年的阅读行为；源稿另一Melleray版本的Theorem 2.9未因本次核验自动升级。

<a id="ocf-c"></a>
## C · 先认证 Baire 分母

[C128](sigma_compact_baire.md#sc-proof) 已给任一**已证明** \(Z=\bigcup_n K_n\) 的σ紧度量空间的 Baire 诊断：\(\bigcup_n\operatorname{Int}_Z K_n\) 稠密当且仅当 \(Z\) Baire。应用义务是先在原对象拓扑证明目标认证像的紧覆盖，继而判定局部预算有界性及该核心的母空间位置。

不要把“每个邻域离开每个给定紧块”直接读为处处非局部紧，除非该块族有适当穷尽/共尾性质；单一紧覆盖的内部并不逐点等于局部紧点。任何改变拓扑的 Polish envelope 产生的是另一个问题，回到原空间须证明桥。

<a id="ocf-d"></a>
## D · 有限约束的同预算相容性

在同一个完整对象紧块 \(\mathcal K\) 中，把全时间尾、图点对RL、真残差、边界拼接、精确零集及带余量的LT越界见证写成闭约束 \(C_i\)。[C167](operator_profile_tools.md#op-compactness) 只在所有有限交都非空后给全部交非空。真正待证的是同一 \(\mathcal K\)、同一正余量、全部完整纤维的有限 extension/amalgamation。

离散网格推广到整窗要有可重建的连续模/图覆盖桥；随级数退化的指数、系数或严格兼容余量不满足同预算门。有限不相容证书可以否定该构造体系；要否定全部相关母空间修改，还须证明这些约束的必要性。

<a id="ocf-e"></a>
## E · 联合图剖面和几何可实现性

在同一完整关系及固定输出窗上，真实剖面 \(\mathcal B_{F,V,S}\) 使用 [C166](operator_profile_tools.md#op-profile) 的全部纤维；反射剖面另使用一个已经良定的指定图块 Cayley 映射及同一输入对距尺度。需独立证明它们在所选对象拓扑下的半连续/Borel性质、截断相容性和具体可实现区域。只有图值界时，转为同一 gauge 真EB仍须残差取到或右连续门。

若两剖面真有共同双侧幂阶 \(M(t)\asymp t^\gamma\)、\(\mathcal B(r)\asymp r^p\)，[C172](operator_profile_tools.md#op-power) 证明精确复合式的 \(\gamma p>1\) 充分门和 \(\gamma p<1\) 障碍；\(\gamma p=1\) 必须另核系数，只有上界指数不能提供必要性。慢变或振荡因子另保留。线性切向漂移层若明写 \(A(y,0)=0\)，对所有充分小法向 \(z\) 有 \(\|A(y,z)\|\ge c\|z\|\) 且在零可微，则令法向沿任意方向 \(tz\) 趋零、除以正 \(t\)，得到 \(\|D_zA(y,0)z\|\ge c\|z\|\)；微分单射要求切向维数不少于法向维数，不以该层默认覆盖所有余维。没有零值前提时此推理不成立。即使剖面区域不同，仍缺可实现性和保纲回传。

<a id="ocf-f"></a>
## F · 仅沿轨道约束的完整图共轭

固定步长剪切 \(L_\lambda(u,v)=(u+\lambda v,u-\lambda v)\)，同胚 \(h\) 的完整图作用可写 \(G^h=L_\lambda^{-1}(h\times h)L_\lambda G\)。但它不自动保真残差、同一零集距离、精确尾或换步相容。[C134](../operator_space.md#os-isometry-proof) 只阻止同紧域满射的全局非扩张粗糙共轭。

开放任务是给仅沿全部实际轨道点对的尾约束、完整transition真EB及同一初值域的非平凡变换；或证明这种特定约束体系的必要刚性。若允许尾预算从 \(e\) 到 \(ce\)，层间连续箭头仍须另核保纲。只控制正向Lipschitz的一族同胚不自动对取逆闭合，不称其为已定义群。

<a id="ocf-g"></a>
## G · 紧预算步长谱

[C135](../operator_space.md#os-spectrum-proof) 的逐类闭预算关系 \(B_{C,j}\subset X\times[1/j,j]\) 给上半连续紧谱/闭存在投影；认证谓词**恰好**是其可数并时才给 \(F_\sigma\)。仍须在同一自然空间分别证明 LT/direct/energy 的乘积闭性和证书耗尽。

谱下半连续、非空鲁棒窗、类别间谱包含/差集、保纲和任何尖锐描述复杂度 reduction 都未由该工具给出。来源“步长谱可以是任意紧集”和标准 \(\Sigma^0_2\)-完全性目标也需独立对象实现/准确基础定理，不作为本页已证前提。复杂度不是大小，孤点/Cantor谱不自动说明认证类大。

<a id="ocf-h"></a>
## H · 同母空间、同预算的定量孔洞

[C168](operator_profile_tools.md#op-hole) 已把固定评价点上的越界余量和相对球稳定性分开。要对一个有界LT必要条件层证明孔洞，还须对**每个所声明中心与全部足够小半径**构造同一完整对象空间内的中心 \(U\)，使余量至少与原球半径成固定正比，并满足孔球包含。若需要upper-porosity的较弱尺度量词，则明确另定义，不能与全部小尺度混称。

任意步长LT先要由真正的紧步长/有界证书块推出统一必要常数。孔隙定量依赖度量，不能仅以同拓扑替换；prevalence也另须合法向量/群结构、probe和平移量词。当前源报告的σ孔隙否定没有原证明，仍不是这条路线的禁止定理。

<a id="ocf-source"></a>
## 完成与未闭边界

八项义务已经能从规范定义和上列证明工具理解，不需猜旧稿；它们的答案仍开放。路线的充分工具刚性、母空间位置和总体比较是三个不同结论。来自完整578 LF旧路线稿的每个数学/证据/组织单元及未核文献访问在[逐源记录](../audit/OPERATOR_IDEAS_FULL_COVERAGE.md#oi-scope)分别登记；枚举完成不关闭这些构造义务，也不要求未来研究局限于这八条路线。
