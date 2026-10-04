# 算子空间：认证包含、内生观测与大小比较

本页按数学对象重构 9/20 证明包和 9/21 后续总账。**当前没有总体覆盖规模分离定理。** 本轮重读下列承重原文、检查公式依赖；“内部审计通过”保留为来源状态，不表示重新证明整套分类理论。9/21 缺失原证据的报告另列。

## 1. 定义：先固定计数对象

取有限维欧氏空间 \(E=\mathbb R^d\)，完整非空闭图 \(G=\operatorname{gph}F\)，步长 \(\lambda>0\)。图剪切

\[
L_\lambda(u,v)=(u+\lambda v,u),\qquad
L_\lambda G=\operatorname{gph}J_{\lambda F}
\]

是完整关系的等价坐标。若 \(J_{\lambda F}=T:E\to E\) 全域单值，则

\[
F(u)=\{(x-u)/\lambda:Tx=u\},\quad
r_F(u)=\lambda^{-1}\inf_{Tx=u}\|x-u\|.
\]

局部 \(T|_U\) 一般不决定完整 \(F\)，所选步只保证 \(r_F(Tx)\le\|x-Tx\|/\lambda\)。另一种合法对象是从一开始对所有 \(u\in E\) 定义
\(F_{T,K}(u)=\{(x-u)/\lambda:x\in K,Tx=u\}\)，其中紧 \(K\subset E\) 上 \(T:K\to K\)；**原关系的定义域为 \(T(K)\)，完整近端的自然输入域为 \(K\)**。裁去既有算子的域外图不属于无损改坐标。[OS-H §2]

| 必须固定的量词 | 不同问题 |
|---|---|
| \((F,\lambda)\) 或 \(F\) | 固定算法实例，或存在真实步长的原算子 |
| 选择 | 存在收敛选择，或每个合法选择都收敛 |
| 步长 | 固定、存在固定、全部固定、变步长策略 |
| 共同域 | 宏观工作块、可缩局部 germ、完整紧源图卡 |
| 性能 | 实际全时间尾，或某份证书的保守尾 |

反例：\(F(0)=\mathbb R,F(u)=\{-u/2\}\)（\(u\ne0\)）给 \(J_F(x)=\{0,2x\}\)，同时有终止和发散选择；\(F=I\) 的每个固定步长均收敛，但可和正步长序列可产生非零极限。[OS-H O1]

<a id="lt"></a>
<a id="os-e"></a>
## 2. 认证超边：LT 的准确包含范围

在已经对齐完整 coverage、同一目标 \(S\)、测试域、真实残差与留域预算的接口上，设 \(R_T=2T-I\)。

**OS-DIRECT：**

\[
\{\|R_Tx-R_Ty\|\le L\|x-y\|^\gamma,\quad
d(u,S)\le\psi(r_F(u)),\quad
\psi((t+Lt^\gamma)/(2\lambda))\le\kappa t, \kappa<1\}
\Longrightarrow d(Tx,S)\le\kappa d(x,S).
\]

**OS-ENERGY：**普通连续严格增 gauge 才使用 \(\alpha=\psi^{-1}\)。令

\[
A(t)=\tfrac12(t^2+L^2t^{2\gamma}),\quad
V(t)=t^2+\lambda^2\alpha(t)^2.
\]

\(A(t)\le q_EV(t),q_E<1\) 联合相同接口推出 \(V(d^+)\le q_EV(d)\)。一般 gauge 下不可删去 \(V\) 而声称距离固定 Q 线性。[OS-H §3.1]

**OS-LT：**这里仅取常用的非负 violation 参数 \(\tau\ge0\)、正线性 EB 系数 \(\rho>0\)；signed LT 或退化 \(\rho=0\) 不在此条转换的字面参数域。Luke–Tam 公共 all-pairs 接口是

\[
\operatorname{Lip}(R_T)\le\sqrt{1+4\tau},\quad
d(u,S)\le\rho r_F(u),\quad
2\tau(\lambda+\rho)^2<\lambda^2.
\]

取 \(\gamma=1,L^2=1+4\tau,\alpha(t)=t/\rho\)，得
\(q_E=(1+2\tau)\rho^2/(\rho^2+\lambda^2)<1\)。故
\(\mathcal L_{\rm ap}\subseteq\mathcal R_E\subseteq\mathcal R_D\cup\mathcal R_E\)。该转换不承诺保持最佳常数、最大初值域，也不覆盖历史 LTT pointwise／多值框架的全部量词。[OS-H §3.2]

<a id="phi"></a>
## 3. OS-PHI：实际尾与反射模的 proper 观测

固定非空紧 \(K\subset\mathbb R^d\)、非空闭 \(S\subset K\)，令

\[
X=\{T\in C(K,K):T|_S=I,\ T^n\to\Pi_T\text{ 一致},\ \Pi_T(K)\subset S\},
\qquad d_{\mathrm{all}}^K(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K.
\]

\(X\) 可能为空：非空蕴含 \(S\) 是 \(K\) 的回缩像。定义

\[
w_n(T)=\max\{\sup_{k,\ell\ge n}\|T^k-T^\ell\|_K,
\sup_{k\ge n,x\in K}d(T^kx,S)\},
\]
\[
m_j(T)=\sup_{\|x-y\|\le2^{-j}}\|R_Tx-R_Ty\|,\qquad
\Phi(T)=(w(T),m(T))\in c_0\times c_0.
\]

**结论。** \(X\) Polish，\(\Phi\) 连续且紧集逆像紧；实际像闭 Polish，非空精确纤维紧/Baire；到像的映射 perfect、quotient。[固定紧源的规范证明](canonical/compact_t_observation.md#ct-proper)。历史 OS-A §1 只作来源溯源。

**证明机制。** 迭代序列在收敛函数列空间中的闭递推约束给 Polish；\(\|\Delta w\|\le2d_{\mathrm{all}}^K\)、\(\|\Delta m\|\le4d_{\mathrm{all}}^K\) 给连续。共同趋零模给 Arzelà–Ascoli 单步紧性，共同尾使其升级为全时间紧性。\(c_0\) 紧参数集通过有限网提供统一趋零预算，因而逆像紧；闭映射及纤维结论接着从 properness 推出。具体极限与全时间估计都在[规范证明](canonical/compact_t_observation.md#ct-proper)。这里只用坐标有界不够。

<a id="cat-gap"></a>
<a id="local-loss"></a>
### 尚缺的两条桥

1. **保纲桥。** proper 不推出 category-preserving。\(p(x)=\max(x,0):[-1,1]\to[0,1]\) 为 proper 闭满射，但无处稠密 \(\{0\}\) 的逆像有内点。此例否定一般推理，未否定特定 \(\Phi\) 的保纲性。
2. **完整原图桥。** 在观测窗 \(K=[-1,1]^2\) 上，\(T_N(s,r)=(s,-\min\{1,N(r-2)_+\})\) 全等于投影；每个 \(T_N\) 在**全空间**两步终止。失紧位置 \(r=2\) 在 \(K\) **之外**：\(T_N(0,2)=(0,0)\)，\(T_N(0,2+1/N)=(0,-1)\)，故无包含该点的共同紧邻域上的一致收敛子列。局部 \(\Phi_K\) 的相同观测不能保证完整全局良定图纤维紧。[OS-A §2]

## 4. 紧源塔与完整纤维：可独立调用的条件引理

<a id="os-tower-proof"></a>
### OS-TOWER / C131：两条塔不等式给统一尾和回缩

令 \((K,d)\) 为**非空紧度量空间**，\(T,U:K\to K\) 连续，并假设每个 \(T\) 轨道有有限长度。定义

\[
V_j(x)=\sum_{k\ge j}d(T^{k+1}x,T^kx),\quad
L_j=\sup_{x\in K}V_j(x),\quad S=\operatorname{Fix}T.
\]

另假设 \(L_j\to0\)；这是**统一有限长度尾**的附加条件，不由逐点有限长度自动给出。每个 \(V_j\) 因连续部分和的余项统一受 \(L_N\) 控制而连续。对所有 \(x\in K,j\ge0\)，要求

\[
d(Ux,x)+V_0(Ux)\le V_0(x),\qquad V_j(Ux)\le V_{j+1}(x). \tag{OS1}
\]

则 \(\operatorname{Fix}U=S\)，每个 \(U\) 轨道有限长，且
\[
\sum_{k\ge n}d(U^{k+1}x,U^kx)\le V_0(U^nx)\le V_n(x)\le L_n. \tag{OS2}
\]
因此 \(U^n\) 一致收敛于连续回缩 \(\Pi_U:K\to S\)；对每个 \(x\)，\(d(U^nx,\Pi_Ux)\le V_n(x)\)。

**证明。** 对固定 \(j\)，\(V_j\) 的连续部分和到 \(N\) 的余项 \(V_N\le L_N\to0\)，故 \(V_j\) 连续。有限长度使 \(T^nx\) 为 Cauchy，紧空间完备，连续 \(T\) 使极限为不动点，故 \(S\ne\varnothing\)。恒等式 \(V_0(x)-V_1(x)=d(Tx,x)\) 成立。若 \(Ux=x\)，(OS1) 第二式在 \(j=0\) 给 \(V_0(x)\le V_1(x)\)，于是 \(Tx=x\)；若 \(Tx=x\)，\(V_0(x)=0\)，(OS1) 第一式给 \(Ux=x\)。归纳第二式给 \(V_0(U^nx)\le V_n(x)\)。第一式沿 \(U\) 轨道从 \(n\) 到 \(N\) 望远镜求和，再令 \(N\to\infty\)，得到 (OS2) 的第一界（剩余 \(V_0(U^{N+1}x)\ge0\)）；其余界由归纳与定义。\(L_n\to0\) 使连续映射 \(U^n\) 一致收敛，极限连续；\(U\Pi_U=\Pi_U\) 由连续性，故极限落在 \(S=\operatorname{Fix}U\)，并对 \(S\) 恒等。此引理**不**给满足 (OS1) 的 \(U\) 的丰富性，也不证明保纲或原算子空间规模。

<a id="os-fiber-eb"></a>
### OS-FIBER-EB / C132：输出步界转为新定义紧源关系的真残差

令 \(K\) 是实赋范空间 \(E\) 的非空紧子集，\(U:K\to K\) 连续，\(S=\operatorname{Fix}U\ne\varnothing\)，\(\lambda>0\)。**从头定义**完整紧输入源关系
\[
F_{U,K}(u)=\{(x-u)/\lambda:x\in K,\ Ux=u\},\quad u\in E, \tag{OS3}
\]
即 \(u\notin U(K)\) 的纤维为空。设 \(\psi:[0,\infty)\to[0,\infty)\) 非降，且对**每个** \(x\in K\) 有
\[
d(Ux,S)\le\psi(\|x-Ux\|/\lambda). \tag{OS4}
\]
那么 \(J_{\lambda F_{U,K}}(x)=\{Ux\}\) 对每个 \(x\in K\) 成立，其输入自然域**正好是** \(K\)；\(F_{U,K}^{-1}(0)=S\)。对每个 \(u\in U(K)\)，完整真实残差
\[
r_{F_{U,K}}(u)=\min_{x\in K:Ux=u}\|x-u\|/\lambda,
\qquad d(u,S)\le\psi(r_{F_{U,K}}(u)). \tag{OS5}
\]
**证明。** (OS3) 的图是紧图 \(\{(Ux,(x-Ux)/\lambda):x\in K\}\)，每个非空逆像 \(U^{-1}(u)\) 紧，故 (OS5) 的最小值由某个 \(x_u\) 取得。将 \(x_u\) 代入 (OS4) 即得真残差 EB；这里不需要把 inf 错当任意一次选择，也不需要 \(\psi\) 连续。\(0\in F_{U,K}(u)\) 当且仅当 \(u=x=Ux\)；由 (OS3) 的同输入反演，恰得完整近端在 \(K\) 上的单值性及自然域。若 \(U\) 满足 C131，那个引理另外提供非空 \(S\) 与一致收敛；本条本身对任意上述连续 \(U\) 成立。它只构造**新的** \(F_{U,K}\)：既有原关系 \(F\) 可能有 \(K\) 外的输入或更多输出纤维，不可将 (OS5) 自动授予它。

这里的原 \(\psi\) 是非降的**传递上界**，未假定 \(\psi(0)=0\) 或原点连续，因此不能未经说明直接称为 D04 型 gauge。若要获得 [D04](foundations.md#d04) 的零点及连续约定，定义内生函数
\[
\phi(t)=\max\{d(Ux,S):x\in K,\ \|x-Ux\|/\lambda\le t\},\quad t\ge0. \tag{OS6}
\]
每个子水平集非空（含 \(S\)）且紧；\(\phi\) 非降、\(\phi(0)=0\)，并由紧性和 \(U\) 连续得 \(\phi(t)\to0\) 当 \(t\downarrow0\)。由 (OS4) 与 \(\psi\) 非降还得 \(\phi(t)\le\psi(t)\)；对实现 (OS5) 最小值的 \(x_u\)，\(d(u,S)\le\phi(r_{F_{U,K}}(u))\)。这给出同一新关系上的 D04 型真残差 gauge；没有据此得到 \(K\) 外的环境开邻域 coverage。

<a id="os-compact-barrier"></a>
### OS-COMPACT-BARRIER / C142：紧源关系不能直接成为极大单调图

在任意**非零实 Hilbert 空间** \(H\) 中，非空紧图
\(G\subset H\times H\) 不可能是极大单调关系的完整图。
设 \(a=\max_{(x,y)\in G}\|x\|\)、
\(b=\max_{(x,y)\in G}\|y\|\)，取单位向量 \(e\)，令
\(u=(a+1)e\)、\(v=te\)，其中 \(t>(2a+1)b\)。对全部
\((x,y)\in G\)，有
\[
\langle u-x,v-y\rangle
\ge t\bigl((a+1)-a\bigr)-(2a+1)b>0. \tag{OS6a}
\]
\(\|u\|=a+1\) 使 \((u,v)\notin G\)。若 \(G\) 单调，
将此点加入会得到真单调扩张；若 \(G\) 原本不单调，更不可能
极大单调。因此 C132 的 \(F_{U,K}\) 虽给紧图、完整近端在
**紧源 \(K\) 上**单值和真残差 EB，却不能直接充当非零 Hilbert 空间中的**极大单调类成员**。
一个更大的母空间可以同时包含紧图和极大单调图；若只用
紧图作为全部成员，极大单调子类便为空。补上源外图以获得极大单调性
会改变完整输入/输出纤维，必须重新证明 coverage、真残差和
原有证书；本引理不否定存在某种经过明确控制的延拓。

<a id="os-successor-proof"></a>
### OS-SUCCESSOR / C133：连续轨道后继选择保持共同 Cauchy 尾

令 \((K,d)\) 非空紧度量，\(T:K\to K\) 连续，且实际尾
\[
e_n=\sup_{x\in K}\sup_{k,\ell\ge n}d(T^kx,T^\ell x)\longrightarrow0.
\]
写 \(A_n(x)=\overline{\{T^mx:m\ge n\}}\)。设 \(U:K\to K\) 是**已给定**的连续映射，且对每个 \(x\in K\) 有 \(Ux\in A_1(x)\)。那么
\[
U^nx\in A_n(x),\qquad d(U^mx,U^nx)\le e_n\quad(m\ge n). \tag{OS7}
\]
特别地 \(\operatorname{Fix}U=\operatorname{Fix}T\ne\varnothing\)，\(U^n\) 一致收敛到该固定集中的连续回缩。这是来源种子引理对应的 C133-v1；同一假设下的新加强 C133-v2 进一步给出**与 \(T\) 的极限相同**：
\[
d(U^nx,\Pi_Tx)\le e_n\quad(x\in K,n\ge0),\qquad \Pi_U=\Pi_T. \tag{OS8}
\]
平凡选择 \(U=T\) 存在；本命题**不构造**具有比较意义的非平凡选择，也不声称保持长度尾或原关系的真残差 EB。

**证明。** \(e_n\to0\) 使 \(T^n\) 在 \(C(K,K)\) 中一致 Cauchy；紧完备性与连续性给极限 \(\Pi_T\)，且 \(T\Pi_T=\Pi_T\)。对 \(m\ge n\) 的轨道点 \(y=T^mx\)，有 \(Uy\in A_{m+1}(x)\subset A_{n+1}(x)\)。以这些轨道点逼近一般 \(y\in A_n(x)\)，连续 \(U\) 与闭 \(A_{n+1}(x)\) 给 \(U(A_n(x))\subset A_{n+1}(x)\)。从 \(x\in A_0(x)\) 归纳得 (OS7) 第一式；尾闭包的直径 \(\le e_n\) 给第二式。更精确地，\(\Pi_Tx\in A_n(x)\)，故与 \(U^nx\) 的距离 \(\le e_n\)，证明 (OS8)。若 \(Tx=x\)，\(A_1(x)=\{x\}\)，故 \(Ux=x\)；若 \(Ux=x\)，则 \(x=U^nx\to\Pi_Tx\)，所以 \(x\in\operatorname{Fix}T\)。\(\Pi_T\) 为 \(U^n\) 的一致极限且在同一固定集恒等，故是连续回缩。没有使用完整 \(F\) 或改变源外图。

<a id="os-isometry-proof"></a>
### OS-ISOMETRY / C134：紧满射非扩张的刚性

任意非空紧度量空间 \((K,d)\) 上，若 \(h:K\to K\) 满射且 1-Lipschitz，则 \(h\) 保所有点对距离。

**证明。** \(\{h^n:n\ge0\}\) 等度连续且值域在紧 \(K\)，由 Arzelà–Ascoli 在一致拓扑中相对紧；因此有 \(n_j>m_j\ge0\) 且 \(d_\infty(h^{n_j},h^{m_j})=\sup_{x\in K}d(h^{n_j}x,h^{m_j}x)\to0\)。由于 \(h^{m_j}\) 满射，把 \(z=h^{m_j}x\) 遍历 \(K\) 可得 \(h^{n_j-m_j}\to I\) 一致。令 \(q_j=n_j-m_j\ge1\)，非扩张给
\[
d(x,y)=\lim_j d(h^{q_j}x,h^{q_j}y)\le d(hx,hy)\le d(x,y).
\]
故两端取等。此只排除**同一紧域满射且全局不扩张**的粗糙共轭；不限制仅在轨道点对控制的变换，也不提供 LT/RLEB 的类别比较。

<a id="os-spectrum-proof"></a>
## 4a. OS-SPECTRUM / C135：紧预算步长谱的条件上半连续

下述命题是**抽象闭预算块引理**，并没有断言现有 LT、direct、energy 三种认证的全部条件已在某个共同对象拓扑下成为闭集。对每种认证 \(C\) 必须分别证明其预算块的闭性；不能把一个类别的证明移植给另一个类别。

令 \(X\) 为拓扑空间（候选为已经明确固定完整原关系与拓扑的中立对象空间），对每个正整数 \(j\) 令 \(I_j=[1/j,j]\)，并给一个**在乘积拓扑中闭**的预算关系 \(B_{C,j}\subseteq X\times I_j\)。定义

\[
\Sigma_{C,j}(G)=\{\lambda\in I_j:(G,\lambda)\in B_{C,j}\},\qquad
P_{C,j}=\{G:\Sigma_{C,j}(G)\ne\varnothing\}. \tag{OS9}
\]

则每个纤维是紧集或空集，\(P_{C,j}\) 在 \(X\) 中闭；多值映射 \(G\mapsto\Sigma_{C,j}(G)\) 按**容许空值**的开集定义上半连续：若开集 \(O\subseteq I_j\) 含 \(\Sigma_{C,j}(G)\)，则 \(G\) 的某邻域内每个谱都包含于 \(O\)。等价的网表述是：\(G_\alpha\to G\)、\(\lambda_\alpha\in\Sigma_{C,j}(G_\alpha)\) 时，\(\lambda_\alpha\) 的任一收敛子网极限属于 \(\Sigma_{C,j}(G)\)。若认证存在性谓词**恰好**是 \(\bigcup_{j\ge1}P_{C,j}\)，则该谓词是 \(F_\sigma\)。这里的“恰好”还须逐类核实预算耗尽所有实步长和所有实际证书，不能只用有理步长或必要块替代。

**证明。** 连续映射 \(\lambda\mapsto(G,\lambda)\) 对闭集取原像，给闭且紧的纤维。若 \(G\notin P_{C,j}\)，对每个 \(\lambda\in I_j\)，闭性给排除 \((G,\lambda)\) 的乘积邻域；有限子覆盖 \(I_j\) 后得到一个 \(G\) 的邻域与整个 \(B_{C,j}\) 不相交。因此投影 \(P_{C,j}\) 闭。把 \(B_{C,j}\) 换成 \(B_{C,j}\cap[X\times(I_j\setminus O)]\) 同理可得上半连续；\(I_j\setminus O\) 紧。可数闭集的联合给最后的 \(F_\sigma\) 结论。闭图和紧参数**不提供下半连续**：在 \(X=\mathbb R,I=[0,1]\) 取 \(B=X\times\{0\}\cup\{(0,1)\}\)，各谱均非空，0 处的谱含 1，附近谱只有 0，因而在 1 周围的开集下半连续失败。

**适用边界。** 若 \(B_{C,j}\) 只在某个子空间闭，结论仅在那个子空间成立；若步长参数不紧，闭联合图的投影未必闭。上半连续不推出谱有开窗、下半连续、两认证类别的差集复杂度、保纲性或总体规模比较。来源 OS-R §7 G.1–G.2 给出了搜索种子，(OS9) 的拓扑量词和空谱约定在此独立重写；G.3 的尖锐描述复杂度 reduction 仍开放。

### 诊断与仍待重构的接口

下表的五个节点均有上述或链接中的规范条件证明；每个只在自己的固定源、尾、纤维及映射范围内调用。

| 数学节点 | 已有内容 | 承重限制 |
|---|---|---|
| OS-TOWER / C131 | (OS1) 两条逐点塔不等式加统一尾 \(L_j\to0\) 推出 (OS2)、同固定集与连续极限回缩 | [本页证明](#os-tower-proof)；未证满足塔条件的选择丰富或总体覆盖 |
| OS-FIBER-EB / C132 | 每个输入的输出步界经紧逆纤维极小值转为新定义 \(F_{U,K}\) 的真 EB | [本页证明](#os-fiber-eb)；不转授给含域外图或额外纤维的原算子 |
| OS-SUCCESSOR / C133-v1/v2 | 已给定连续后继选择的共同 Cauchy 尾、同固定集与连续回缩；v2 另证同一极限 \(\Pi_U=\Pi_T\) | [本页证明](#os-successor-proof)；非平凡选择的存在与丰富性未证明 |
| OS-BAIRE | [σ-紧度量空间诊断 C128](canonical/sigma_compact_baire.md#sc-proof)：\(Z=\bigcup K_n\)（紧）为 Baire 当且仅当 \(\bigcup\operatorname{Int}_ZK_n\) 稠密 | 未决定目标认证空间满足哪边，也不要求层递增 |
| OS-ISOMETRY / C134 | 紧度量空间的满射 1-Lipschitz 自映射是等距映射 | [本页证明](#os-isometry-proof)；仅排除该种粗糙共轭手法 |

四项紧源引理的来源线索见 OS-A §§3–6 及 OS-R §1 A.2–A.4、§6 F.2；这里的规范证明独立于来源文本。塔方案刚性不等于同尾层刚性：**在本例专用的** \(K'=[-1,1]\times[0,1]\)、\(S'=[-1,1]\times\{0\}\) 上，投影 \(P(s,r)=(s,0)\) 的塔只允许自身，但 \(U_a(s,r)=(s+ar(1-r)(1-s^2),0)\)（\(0<a\le1\)）仍把 \(K'\) 映入 \(S'\)：切向增量不超过 \(r(1-r)(1-s^2)\le(1-s)/2\)，也不超过 \(1-r\)。对每个输入它的位移 \(\sqrt{r^2+a^2r^2(1-r)^2(1-s^2)^2}\le1\)，之后步长皆零，故与 \(P\) 同具**全窗取上确界后的**精确尾 \((1,0,0,\dots)\)；它们的逐点首步长一般不同。此 \(K'\) 不是上一段的 \(K=[-1,1]^2\)。

<a id="size"></a>
<a id="no-go"></a>
## 5. 后续负结果与证据缺口

9/21 总账在其历史空间中报告：普通全图／\(C^0\) Baire、轨道小集理想、原动力度量的绝对孔隙性都把 LT 与 RLEB 同时判小；尤其报告

\[
\mathcal R_D\subseteq\mathcal H_+\in\sigma\mathcal P^-(X_D,d_{\rm dyn}),
\]

故旧“差集非 σ-upper-porous”目标在那里为假。**本页不补造这些空间、孔隙常数或原证明。** 总账的内禀联合模谱“完整双向恢复”也仍是报告结果，不能因更新日期而替代正文。[OS-N §§6–7；OS-I I-076–103]

本次附件已提供总账当时称缺失的 I-001（9/14，仓库展开保留 100/101 项，第三方 Frankowska PDF 未入库）、I-002（9/18）、I-003–005、I-059（selection 修订包）、I-075（9/20 展开包）。I-005 虽名为 `Codex_independent_audit.md`，正文实际是待执行审计任务，不支持“审计已通过”；I-004 为旧稿，修订结论须用 I-059 的主稿与关闭记录。I-097–099 孔隙否定审计、I-102 正式表示稿未在已盘点的仓库和 ZIP 文件名中发现；不能把所有 `SOURCE-MISSING` 原样复制为当前事实。

**当前主问题：**在不把 \((L,\gamma,\psi)\) 当作空间坐标的自然完整对象体系中，给有鉴别力且不受远端无关自由度污染的大小量尺，并证明三类的真实规模比较。受限仿射漂移层中的严格成员、任意步长 LT 排除和层内余稀都是有用构造；提升到中立母空间仍需独立证明。

## 6. 来源定位

设包根 `P=history/sources/次单调论文研究/分类集研究/RLEB_LT_operator_space_research_asset_v1/RLEB_LT_operator_space_research_asset_v1/`。

| 别名 | 原文路径与定位 |
|---|---|
| OS-H | `P/01_CANONICAL_HANDOFF/mathematician_handoff/07_final_handoff.md`，§§2–6、§11 来源表 |
| OS-A | `P/01_CANONICAL_HANDOFF/mathematician_handoff/06_math_audit.md`，§§1–7 |
| OS-R | `P/01_CANONICAL_HANDOFF/mathematician_handoff/04_research_ideas.md`，§1 A.2–A.4、§6 F.2 |
| OS-E | `P/02_NEUTRAL_PPA_SYSTEM/ppa_system_team/03_certificate_embeddings.md`；`07_embedding_math_audit.md` |
| OS-N | `history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md`；`03_NO_GO_LEDGER.md` |
| OS-I | `history/sources/提纯总账_2026-09-21_v0.9/05_INTERNAL_INDEX.md`，恢复清单；路径是历史位置 |

来源文件属于证据层；上述 OS-* 数学节点与超边属于规范层。若后续证明改变域、选择或步长量词，应另立版本，不能静默覆盖此页。
