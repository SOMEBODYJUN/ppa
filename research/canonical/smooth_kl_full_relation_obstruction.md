# 完整动力学图排除共同光滑与可定义单状态能量合同

本页固定 **C261-v1、v2、v3**，状态 `derived-checked`。v1排共同C¹单状态H1/H2，v2排C¹的H1本身，v3排有限局部Lipschitz且具有强次梯度链式法则的共同H1/H2，涵盖可定义及Whitney分层能量。它们保持同一物理算法、同一输入窗及全部输出量词；不排任意lsc能量、记忆或非二次下降，也不排本轮新几何支持的直接能量求和证明。

<a id="sko-object"></a>
## 对象与量词

X=Cⁿ×Cⁿ按实Euclidean空间，n≥1，||u||=1，M={e^{iθ}u}。固定Γ≥0、A=1+Γ、h(p)=p/√||p||（p0时为0）。设完整关系F满足
\[
F(c,p)=\{(-h(p),\Gamma p)\}\quad(c\in M,p\in\mathbb C^n),\qquad
S=\operatorname{zer}F=(M\cup\{0\})\times\{0\}.
\tag{SKO1}
\]
其余位置的F不参与证明。算法J=(I+F)⁻¹，取
\[
U=\{(a,b):d(a,M)<1/2\},\quad
0<R\le\min\{1/100,1/A\},\quad U_R=\{w\in U:d(w,S)\le R\}.
\]
任取包含U_R∪J(U_R)的开集O。本轮[C260-v1/v2](orthogonal_feedback_rleb.md#ofr-large-window)取Γ10、R分别10⁻¹²/10⁻⁴，[C256](amplitude_circle_hamilton.md#ach-object)取Γ99、R10⁻⁴，均满足这些完全相同的运动量结构。

<a id="sko-theorem"></a>
## 不可能定理

不存在E∈C¹(O)、α>0、有限β≥0，使对**每个w∈U_R和每个y∈J(w)**同时有
\[
E(w)-E(y)\ge\alpha\|w-y\|^2,\qquad
\|\nabla E(y)\|\le\beta\|w-y\|.
\tag{SKO2}
\]
E不要求等于原机械能、不要求径向、相位不变、凸或半代数。共同函数和共同常数是本定理的全称合同；不排某一固定轨道另有函数或常数。

**证明。** 置P_*=R²/4。对任意c∈M、p且P=||p||≤P_*，以及全部t∈[0,1]，令
\[
y_t=(c,tp),\qquad w_t=(c-h(tp),Atp).
\]
SKO1给w_t−y_t∈F(y_t)，这是完整算法的真实前驱，而非任选测试点。它们先验处于共同输入窗，因为
\[
d(w_t,S)^2\le tP+A^2t^2P^2\le P+A^2P^2
\le5R^2/16<R^2,
\quad d(c-h(tp),M)\le\sqrt{tP}<1/2.
\]
步长平方tP+Γ²t²P²≤2tP，因此SKO2的第二项给||∇E(c,tp)||≤β√(2tP)。沿动量线段积分，
\[
|E(c,p)-E(c,0)|\le C_0P^{3/2},\qquad C_0=2\sqrt2\beta/3.
\tag{SKO3}
\]
常数统一于所有c和动量方向。零步(c,0)∈J(c,0)迫使∇E(c,0)=0；相位圆连通，故E(c,0)=E_*是由合同推出的常数。

现在取两个不同且任意接近的a,z∈M，ℓ=||z−a||、p=ℓ(z−a)、P=ℓ²，令
\[
w=(a,Ap),\qquad y=(z,p).
\]
h(p)=z−a与SKO1证明y∈J(w)。选P≤P_*/A，则AP≤P_*、d(w,S)=AP<R，实际步长平方P+Γ²P²≥P。SKO3同时适用于p和Ap，圆上常数消去后，
\[
E(w)-E(y)\le C_0(A^{3/2}+1)P^{3/2}.
\tag{SKO4}
\]
第一项SKO2却要求α≤C_0(A^{3/2}+1)√P。圆具有任意小非零弦，P↓0给α≤0，矛盾。证毕。

<a id="sko-metric"></a>
## 固定能量度量不能修复该合同

若把SKO2中的步长改为一个固定SPD矩阵W的范数，梯度改为对应对偶范数，同样不可能。有限维范数等价把这样的H1/H2分别转成Euclidean正常数α′与有限β′，立即与定理矛盾。甚至一组满足统一正上下界mI≼W≼MI的变化能量度量，也有同一必要转换。

这是**保持原算法的能量度量**结论，不能读成改变GPPA核或近端子问题后算法仍相同。退化度量、非线性坐标提升和扩展状态另有义务，不在本障碍范围。

<a id="sko-comparison"></a>
## 与 ABS 的准确关系及不排除的路线

Attouch–Bolte–Svaiter作者报告（2010-12-15）§2.3的H1是固定正系数平方步长下降，H2是输出处存在受步长控制的limiting subgradient；Theorem2.9在H1–H3与KL条件下给有限长度。C¹函数的limiting subgradient唯一为梯度，故本页严格排除直接以**任意共同C¹单状态E**为该完整算法逐输出认证H1/H2的路线，甚至不需要先检验KL或H3。原文允许非光滑E，因此不能写成排除整个ABS定理。

v1/v2仍允许：某条预选轨道自己的E；删支后的不同算法；非光滑E（v3另核具有强链式法则的子类）；多步或记忆扩展能量；非二次下降或其他误差指数；先证明直接几何/能量收缩再用物理跳步模求和。[C259](amplitude_classical_energy.md#eca-fixed99)以及[C260的正面能量替代](orthogonal_feedback_rleb.md#ofr-comparison)正是最后一种路线。共同能量可以存在，却不能同时满足SKO2，这两个结论完全相容。

一手版本、页码与本轮推导身份见[LITERATURE](../LITERATURE.md#lit-smooth-kl-obstruction)；独立冷读及算术检查见[接续筛选](../../发表成果整理/应用优势继续筛选.md)。

<a id="sko-h1-only"></a>
## C261-v2：二次下降 H1 本身已不可能

本节另立强化身份，状态 `derived-checked`，保留v1对象和共同完整输入/输出窗口，删去H2假设。不存在E∈C¹(O)、α>0，使**每个w∈U_R和每个y∈J(w)**均满足E(w)−E(y)≥α||w−y||²。其余不排除范围与v1相同；固定SPD及统一正上下界的变化能量范数仍不能修复。

**证明。** 固定c∈M，对正负两侧θ→0，令z_θ=e^{iθ}c、ℓ_θ=||z_θ−c||、p_θ=ℓ_θ(z_θ−c)、P_θ=ℓ_θ²。SKO1给真实转移w_θ=(c,Ap_θ)→y_θ=(z_θ,p_θ)。小θ时d(w_θ,S)=AP_θ<R，全部转移都在共同窗，且步长平方P_θ+Γ²P_θ²。

C¹性使两端动量变化为O(P_θ)=O(θ²)。H1于是给E(c,0)−E(e^{iθ}c,0)≥−O(θ²)。除以|θ|并取两侧极限，迫使圆上θ导数为零。对每个c成立，故E|_{M×0}是常数。

现在只沿动量线段积分；不能用一次关于(c,0)的全状态泰勒余项替代这一步。由于∇_pE连续、z_θ→c且p_θ→0，
\[
E(z_\theta,p_\theta)-E(z_\theta,0)
=\int_0^1\langle\nabla_pE(z_\theta,tp_\theta),p_\theta\rangle\,dt
=\langle\nabla_pE(c,0),p_\theta\rangle+o(P_\theta).
\tag{SKO5}
\]
输入端同样是A⟨∇_pE(c,0),p_θ⟩+o(P_θ)。圆上常数消去，且p_θ/P_θ→±ic，所以
\[
\frac{E(w_\theta)-E(y_\theta)}{P_\theta}
\longrightarrow\pm\Gamma\langle\nabla_pE(c,0),ic\rangle.
\tag{SKO6}
\]
H1要求两个相反极限都至少α>0，不可能；Γ0时两者均为0。证毕。固定或统一非退化能量范数的步长平方下界为m||step||²，亦立即矛盾。

这一强化只用了同一根c的两侧圆弦完整转移，不用残差、KL、H2、反馈角或附近势能形式。它给[C260](orthogonal_feedback_rleb.md#ofr-certificate)的明确比较：RLEB可处理的完整算法不可能通过任何共同C¹单状态平方步长下降合同。正面非二次能量收缩仍可成立，所以不宣称全部经典方法或全部ABS非光滑版本失败。


<a id="sko-nonsmooth"></a>
## C261-v3：具有强链式法则的非光滑 H1/H2 也不可能

保留SKO1、Γ/R/U/O与完整全输出量词。limiting次微分记∂E，Clarke次微分记∂CE。设E:O→R有限、局部Lipschitz，并满足：对于每条绝对连续曲线η:[0,1]→O，在一个曲线依赖的共同零测集之外，
\[
(E\circ\eta)'(t)=\langle v,\eta'(t)\rangle
\quad\text{对所有 }v\in\partial E(\eta(t)).
\tag{SKO7}
\]
同一零测集对所有v有效。不存在这样的E、α>0及有限β≥0，使每个w∈U_R及每个y∈J(w)同时满足
\[
E(w)-E(y)\ge\alpha\|w-y\|^2,\qquad
\exists v\in\partial E(y):\|v\|\le\beta\|w-y\|.
\tag{SKO8}
\]
这是输出处**存在一个**小范数limiting次梯度的ABS-H2，不要求所有Clarke次梯度小。固定SPD及统一正上下界的变化能量范数亦不可能；不改变近端算法。

**证明。** 仍取P_*=R²/4。v1已逐项认证全部真实前驱w_t=(c−h(tp),Atp)属于同一U_R，以及真实步长平方≤2tP。SKO8对η(t)=(c,tp)给至少一个v_t∈∂E(η(t))，||v_t||≤β√(2tP)。SKO7在共同零测集外可评价这个值，因此
\[
|(E\circ\eta)'(t)|\le\beta P\sqrt{2tP}.
\]
局部Lipschitz与曲线图像紧保证组合绝对连续。积分仍得SKO3，不需要可测次梯度选择，也没有把所选次梯度的范数上界赋给整个Clarke集合。

零步(c,0)→(c,0)的H2给0∈∂E(c,0)。沿相位圆的光滑参数曲线，SKO7给导数几乎处处为0；组合绝对连续，故E(c,0)常数。最后取同一真实圆弦w=(a,Ap)→y=(z,p)，0<P≤P_*/A。SKO3对两个动量都有效，故再次得到α≤C_0(A^{3/2}+1)√P，P↓0矛盾。Γ0没有例外。证毕。

<a id="sko-chain-rule-bridge"></a>
### 可定义能量与局部开集的准确文献桥

Davis–Drusvyatskiy–Kakade–Lee作者32页PDF，Definition5.1与Theorem5.8/证明，给局部Lipschitz、Whitney C¹分层函数沿任意绝对连续曲线的强链式法则，对**全部Clarke次梯度**共同成立。limiting⊂Clarke，因此供应SKO7。有限局部Lipschitz可定义函数（特别半代数函数）属于这一类。一手来源与导入范围见[LITERATURE](../LITERATURE.md#lit-stratified-chain-rule)。链式法则是既有事实，本页圆弦障碍是本轮推导。

作者定理写在全空间，而E定义在O。这里有显式全域桥，不能略掉。置M₀=M×0、D₀(x)=d(x,M₀)。闭管{D₀≤3R/4}紧且包含于U_R⊂O。取半代数Lipschitz截断χ：D₀≤R/2时χ1，R/2<D₀<3R/4时χ=3−4D₀/R，余下χ0。定义全域Φ在D₀<3R/4为χE，在外为0。紧支持完全在O内部，E在其邻域局部Lipschitz且有界，故Φ全域局部Lipschitz；E可定义时Φ也可定义。

实际积分路径(c,tp)、相位曲线、最后圆弦输入(a,Ap)和输出(z,p)都有D₀≤P_*=R²/4<R/2。Φ在它们的开邻域等于E，局部次微分相同，作者全域定理于是供应本证明所需的链式法则。辅助前驱w_t可能只有D₀≤√5R/4，未必χ1；它只用于原E的H2，不沿其积分，不需要替换为Φ。

对O上局部有限Whitney C¹图分层，亦可将作者证明局部化：局部Lipschitz排除垂直图切向，紧曲线图像有限覆盖，曲线速度几乎处处属于当前层切空间；全部Clarke次梯度的切投影相同，从而得到SKO7。仅用“tame”名称而不给分层或SKO7，不足以导入。

若能量步长范数由mI≼W≼MI定义，H1转成系数αm的Euclidean下降，H2转成所选limiting次梯度的Euclidean界βM||step||。故固定或统一非退化SPD能量范数亦被SKO8排除。修改GPPA核是另一算法，不能由此自动裁定。

<a id="sko-nonsmooth-boundary"></a>
### 为什么非光滑扩展需要 H2 和链式条件

v2的H1-only结论**不能**扩到全部非光滑可定义能量。[C260同组证书](orthogonal_feedback_rleb.md#ofr-certificate)对全部完整输出已给d₊<.47d及P<.469d（d>0），因此
\[
\|w-y\|^2=P+\|b-p\|^2
\le(.469+1.469^2R)d<.47d.
\tag{SKO9}
\]
E₀=d(·,S)是全域Lipschitz、半代数函数，E₀(w)−E₀(y)>.53d>||step||²，所以完整H1可取α1；d0时由C260完整吸收成立等式。可是y=(c,p)、p≠0小、c∈M处E₀光滑且梯度范数1，真实前驱(c−h(p),11p)的步长√(P+100P²)趋0，任何统一H2都失败。

也不能仅以局部Lipschitz替换SKO7。一个稠密平台构造可使E≈d、处处0∈∂E，并对C260全部转移同时满足H1和H2；该非可定义函数没有KL性质。较弱无KL构造及独立冷读见[非光滑合同接收](../../发表成果整理/非光滑能量合同独立接收.md)。更强[C262](artificial_kl_energy_bridge.md#akb-theorem)把微区间的导数0改成√t，确实得到非可定义KL能量及同完整算法H1/H2/H3。因此不得扩大为排除整个ABS；C262登记的是正面比较边界。

v3严格排除共同有限局部Lipschitz可定义单状态ABS-H1/H2合同，甚至不需要先假定KL。它仍不排任意非局部Lipschitz或不连续lsc能量、扩展状态/记忆、非二次下降、预选轨道能量，以及共享本轮几何的直接机械能收缩和长度求和。
