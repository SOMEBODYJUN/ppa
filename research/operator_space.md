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

局部 \(T|_U\) 一般不决定完整 \(F\)，所选步只保证 \(r_F(Tx)\le\|x-Tx\|/\lambda\)。另一种合法对象是从一开始定义
\(F_{T,K}(u)=\{(x-u)/\lambda:x\in K,Tx=u\}\)，其中紧 \(K\) 上 \(T:K\to K\)；其完整输入域就是 \(K\)。裁去既有算子的域外图不属于无损改坐标。[OS-H §2]

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

**OS-LT：**Luke–Tam 公共 all-pairs 接口是

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
\qquad \rho(T,U)=\sup_{n\ge0}\|T^n-U^n\|_K.
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

**结论。** \(X\) Polish，\(\Phi\) 连续且紧集逆像紧；实际像闭 Polish，非空精确纤维紧/Baire；到像的映射 perfect、quotient。[OS-A §1，完整证明]

**证明机制。** 迭代序列的闭递推约束给 Polish；\(\|\Delta w\|\le2\rho\)、\(\|\Delta m\|\le4\rho\) 给连续。共同趋零模给 Arzelà–Ascoli 单步紧性，共同尾使其升级为全时间紧性。\(c_0\) 紧参数集通过有限网提供统一趋零预算，因而逆像紧。这里只用坐标有界不够。

<a id="cat-gap"></a>
<a id="local-loss"></a>
### 尚缺的两条桥

1. **保纲桥。** proper 不推出 category-preserving。\(p(x)=\max(x,0):[-1,1]\to[0,1]\) 为 proper 闭满射，但无处稠密 \(\{0\}\) 的逆像有内点。此例否定一般推理，未否定特定 \(\Phi\) 的保纲性。
2. **完整原图桥。** 在观测窗 \(K=[-1,1]^2\) 上，\(T_N(s,r)=(s,-\min\{1,N(r-2)_+\})\) 全等于投影；每个 \(T_N\) 在**全空间**两步终止。失紧位置 \(r=2\) 在 \(K\) **之外**：\(T_N(0,2)=(0,0)\)，\(T_N(0,2+1/N)=(0,-1)\)，故无包含该点的共同紧邻域上的一致收敛子列。局部 \(\Phi_K\) 的相同观测不能保证完整全局良定图纤维紧。[OS-A §2]

## 4. 可复用工具与它们不能证明的结论

| 数学节点 | 已有内容 | 承重限制 |
|---|---|---|
| OS-TOWER | 一致有限长度尾产生连续 \(V_j(x)=\sum_{k\ge j}\|T^{k+1}x-T^kx\|\)，满足适当塔不等式的 \(U\) 保长度尾 | 充分选择方案；未证丰富选择或覆盖母空间 |
| OS-FIBER-EB | 紧完整源中，对每个输入的输出 EB 可在整条逆纤维取 inf，得到真实 EB | 需要完整纤维与 gauge 连续非降；不能只保一个 transition |
| OS-SUCCESSOR | 连续选择 \(Ux\in\overline{\{T^mx:m\ge1\}}\) 保原 Cauchy 尾及固定集 | 连续选择存在性、丰富性未证明 |
| OS-BAIRE | \(Z=\bigcup K_n\)（紧）为 Baire 当且仅当 \(\bigcup\operatorname{Int}_ZK_n\) 稠密 | 未决定目标认证空间满足哪边 |
| OS-ISOMETRY | 紧度量空间的满射 1-Lipschitz 自映射是等距映射 | 仅排除该种粗糙共轭手法 |

以上来源为 OS-A §§3–6。塔方案刚性不等于同尾层刚性：**在本例专用的** \(K'=[-1,1]\times[0,1]\)、\(S'=[-1,1]\times\{0\}\) 上，投影 \(P(s,r)=(s,0)\) 的塔只允许自身，但 \(U_a(s,r)=(s+ar(1-r)(1-s^2),0)\)（\(0<a\le1\)）仍把 \(K'\) 映入 \(S'\)。对每个输入它的位移 \(\sqrt{r^2+a^2r^2(1-r)^2(1-s^2)^2}\le1\)，之后步长皆零，故与 \(P\) 同具**全窗取上确界后的**精确尾 \((1,0,0,\dots)\)；它们的逐点首步长一般不同。此 \(K'\) 不是上一段的 \(K=[-1,1]^2\)。

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
| OS-E | `P/02_NEUTRAL_PPA_SYSTEM/ppa_system_team/03_certificate_embeddings.md`；`07_embedding_math_audit.md` |
| OS-N | `history/sources/提纯总账_2026-09-21_v0.9/02_VERIFIED_CORE.md`；`03_NO_GO_LEDGER.md` |
| OS-I | `history/sources/提纯总账_2026-09-21_v0.9/05_INTERNAL_INDEX.md`，恢复清单；路径是历史位置 |

来源文件属于证据层；上述 OS-* 数学节点与超边属于规范层。若后续证明改变域、选择或步长量词，应另立版本，不能静默覆盖此页。
