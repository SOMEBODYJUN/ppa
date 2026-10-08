# 独立攻击审计：任意核、任意拆分与标准提升

审计日期：2026-10-08。比较基线：`3dd02110d7666ba77b561bf2ab26641013a79fd3`；开始时仓库 main：`5daf6fa`。本报告先独立重建原文和规范对象，再接收 root 提出的待核排除及 T4 修复；写入初版前没有阅读 `gppa_review.md` 或 `nfb_review.md`。它不是全世界先行性检索结论，也不改变 C02 原稿多选择版等现有证据状态。

使用原件为本目录 `sources/gppa_2608.01584v1.pdf`、`sources/nfb_2608.22687v1.pdf`，其指纹见 `sources/manifest.json`。arXiv 原始版本页面已直接打开核对：GPPA 提交日 2026-08-03，NFB 提交日 2026-08-24。承重页已渲染目读：GPPA p.5、p.7；NFB p.6、p.8、p.12。公式和页面号以下均按论文印刷页码。

## 1. 可以成立的总判断及不能推广的版本

1. 两篇论文确实与本库的非单调近端收敛、误差界和线性率有强重合。不能把“非单调”“Hölder EB”“有限长度”单独作为新颖性标签。
2. GPPA Theorem 2 不在任意核下自动覆盖**同一完整普通 PPA 的全部纤维**。C137 甚至存在同一完整原图的非平凡普通轨道，不能成为任何 adaptively strongly monotone 核的 GPPA 轨道，证明见 §5。
3. NFB 对**任意合格同空间 cocoercive 拆分**都有一个原总关系上的必要固定二次锚界；该界还可压缩经过论文标准 primal-dual 提升。因此 C193 的非退化自然类，以及 C137/C141 的近零图点序列，给出真正限定的非涵盖证据，见 §4。
4. 这些结论不排除删支、重建另一算子、只保零集、另选一条分支、非线性改坐标、任意未分类提升，或别的既有论文覆盖相同结论。它们也不能独自证明 uploaded 结构/纤维稿 C03/C04 的全球新颖性。

| 比较要求 | 可以推出什么 | 必须避免的替换 |
| --- | --- | --- |
| 同一个包含问题/同零集 | 可以换迭代来求解该问题 | 冒充原 PPA 的完整一步纤维和轨道 |
| 同完整原图、同一步全部纤维 | 可比较原 resolvent 的全部动力 | 只展示一个合法输出或删掉坏分支 |
| 同一实际轨道 | 可比较该轨道是否满足外部算法更新 | 冒充全部输入、全部纤维或完整图量词 |
| 同空间拆分 `F=A+C` | 必须保持全部原图值 | 只拟合所选图值，改变真残差 |
| 标准 primal-dual 提升 | 可使用 §4 的配对和输出压缩 | 推广至没有这些保真等式的任意 lift |

## 2. 外部定理的准确身份

### GPPA

原文 p.2 的 (5)–(6)、p.5 Definition 4 定义
\[
 J^v_{\eta F}=(\eta F+v)^{-1}\circ v,
 \qquad v(x_k)-v(x_{k+1})\in\eta F(x_{k+1}).
\]
这里为避免和本库 Hölder 幂混淆，把原文步长 \(\gamma\) 改记 \(\eta\)。核 \(v:H\to H\) 可以非线性、非单射；Definition 4 的 coverage 是 \(\operatorname{ran}v\subset\operatorname{ran}(\eta F+v)\)，不是普通 Minty coverage。

Definition 3（p.5）要求存在 \(\epsilon>0\)，对全部原图点对
\[
 \langle f-g,v(x)-v(y)\rangle\ge\epsilon\|v(x)-v(y)\|^2.
 \tag{IA-G1}
\]
Theorem 2（pp.7–8）另要非空零集和上述 coverage。其 (a) 结论是核坐标距离及核增量按 \((1+2\eta\epsilon)^{-1/2}\) 线性趋零；其 (b) 加 \(F^{-1}\) 在 0 的 R-Lipschitz 后给**到零集距离**线性趋零。原文没有从这些假设给任意非单射核的物理点收敛或有限长度。Theorem 1（p.6）只要 pair monotonicity，结论包括核增量趋零、闭图下弱聚点为解，以及 R-continuity 下集合距离趋零；不要把 §5 对 adaptive 条件的排除移用于 Theorem 1。

Definition 5（pp.5–6）的 R-continuity 是完整逆像包含 `F^{-1}(w) ⊂ S+rho(||w||)B`。在本审计的 Euclidean 闭零集模型中，最近零点取到，连续幂 gauge 的完整真 EB 给此包含；高阶 gauge \(cs^q,q>1\) 在小残差窗内还给 R-Lipschitz。因此“我们 EB 幂大于 1”并不排除 GPPA 的逆像正则性门。

Theorem 4（pp.9–11）研究 \(\widetilde F=F+\epsilon v\) 的 IGPPA，假设 pair monotonicity、Lipschitz 核、两个非空零集、原逆像 R-continuity 以及合法生成轨道，取误差上界 \(\delta=\epsilon^2\)，结论为到原零集的双极限邻近估计。它改变了算法及 regularized relation，不是原普通 PPA 的精确动力定理。其打印证明的 modulus 极限步骤可修复，不能据此否定定理，见 §6。

### NFB

定义 (2.3)（p.4）明确使用 `on S` 的 solution-anchored 量词：每个锚与**每个完整原图点**比较；它不要求所有两个非解图点之间的全对 semimonotonicity。

Assumption 3.1（p.6）要求强正定有界线性 metric \(S\)、全局 \(\beta\)-cocoercive \(C\)、`(M+A)^{-1}` 单值满域、总关系弱强序列闭，以及 \(A\) 在每个 solution graph anchor 上的 \(\rho S^{-1}\)-comonotonicity，其中 \(\rho>-\beta\)。核还受 `tau M-S` 的全局 Lipschitz 常数 \(\zeta<1/2\) 约束。故 NFB 的非线性核不能简单视作完全任意的 GPPA 核。

Algorithm 3.7（p.8，(3.6a)–(3.6c)）包含辅助变量及 relaxation。Theorem 3.10（pp.12–13）另要 (3.8) 的下降常数 \(\lambda_{\rm NFB}>0\)：(i) 给物理变量弱收敛；(ii) 加 \(\mu S\) 正项 \(\mu>0\) 后给唯一解的物理 R-linear 收敛。这里 \(\rho\) 可负，不能把 (ii) 简化成“原算子强单调”。

Notation 4.1（p.17，(4.1)–(4.2)）、Assumption 4.2（p.17）、Propositions 4.6–4.8（pp.21–24）给标准乘积关系及其锚界；Algorithm 4.9（p.24，(4.21)）和 Theorem 4.10（pp.24–25）将其归约到 Theorem 3.10。该 theorem 的 R-linear 分支要 \(\nu_A,\nu_B>0\)，并在**乘积物理范数**中收敛到唯一 primal-dual 解。

## 3. 强重合的完整对象与长度结论

### 三条路线的同图同一步重合

取 \(F=I\)、普通步长 1，完整 \(J_Fx=x/2\)。本库 C02-v2 取 \(L=0\)、\(\psi(t)=t\)、\(\kappa=1/2\)，全域 coverage、零集 \(\{0\}\)、完整纤维与留域门全部成立。

GPPA 取 \(v=I,\eta=\epsilon=1\)，得到同完整一步纤维。NFB 取 \(A=I,C=0,S=M=I,\tau=\theta=1,\zeta=\rho=0,\beta=1\)，(3.8) 的下降常数为 \(1/2>0\)，\(\mu=1\)；辅助量第一步后为 0，\(u_0=0\) 时从初步就精确为普通 PPA。这是真正同对象、同完整轨道的重合。

### NFB 还覆盖原范数纯旋转的线性点收敛

取二维 \(B=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\)，\(F=B\)、普通步长 1。令 NFB \(A=B,C=0,S=M=I,\tau=\theta=1,\zeta=0,\beta=1\)，以及 \(\mu=1/4,\rho=-1/4\)。由于
\[
 \langle d,Bd\rangle=0=\tfrac14\|d\|^2-\tfrac14\|Bd\|^2,
\]
solution-anchored semimonotonicity（事实上全对）成立，唯一解为 0，满域/闭图均直接成立。
原文 (3.8) 的完整下降常数是
\[
 \lambda_{\rm NFB}=1-\frac{(1-1/2)^2}{2(1-1/4)}-\frac12=\frac13>0.
\]
最后 \(2\hat\rho\tau\zeta_M^2\) 项在 \(\zeta=0\) 时**并不消失**。初发给 root 的 \(5/6\) 漏此项，已在写入前更正并以 Fraction 复算。Theorem 3.10(ii) 因而覆盖同普通 PPA 的 R-linear 点收敛；这与本库 C24 的旋转收敛结论重合。该参数下 C02 **直接**兼容测试为 1，不能称严格 C02-v2 证书的三方重合；本库的实际收敛证明与其它能量路线应单列。

### GPPA 也实质覆盖一个非单调、非 calm 的严格 RLEB 子类

交叉核验 `gppa_review.md` §5.2 后确认其更强重合。取 C191 合法数据形成完整关系
\[
 F(t,y)=\{(-cy^\alpha,ay+n):n\in N_{\mathbb R_+}(y)\},
 \quad y\ge0,\quad a,c>0,\quad0<\alpha<1.
\]
普通完整单点映射为
\(T(t,y)=(t+\lambda c(qy_+)^\alpha,qy_+)\)，\(q=(1+\lambda a)^{-1}\)。令
\[
 K=\frac{\lambda c q^\alpha}{1-q^\alpha},\qquad
 v(t,y)=\frac h\lambda(-K(y_+)^\alpha,y_+).
\]
该显式非线性、非单射核与完整 F 满足 adaptive 条件，常数可取
\(\min\{c/(hK/\lambda),a/(h/\lambda)\}>0\)。包括 y=0 的全部法锥值 n≤0；没有删支。全部 warped 纤维为 `R × {q y_+}`，故全输入 coverage 成立，每条普通选择均合法。原逆像甚至全局 R-Lipschitz，常数 \(1/a\)。

正初值的普通选择由**一步恒等式**保留 \(I=t_k+Ky_k^\alpha\)，预先确定的 \(x_*=(I,0)\) 是原零点，且
\[
 v(x_k)-v(x_*)=\frac h\lambda(x_k-x_*).
\]
所以 Theorem 2(a) 配上已核的不变量桥，直接给同一普通轨道的**物理点 R-linear 和有限长度**，不是仅集合距离重合；不需要先假设极限存在。小输入半径满足
\(R^{1-\alpha}<\lambda c(1-q^\alpha)\) 时又有严格 C02-v2 证书。这个完整例否定“非 calm/固定二次锚失败必然排除 GPPA”以及“GPPA 对这些子类只有距离信息”两种过宽叙述。

同时，warped 纤维仍有自由 t 方向；任意 warped 选择不自动保持此不变量，完整两个算法并不相等。y₀≤0 的普通轨道一步驻定，须单列，不能在其初步硬套正法向的核反演等式。

### NFB 的非单调严格 C02 重合及非零前向/记忆补偿

交叉核 `nfb_review.md` §6 后确认其更有鉴别力的完整非单调重合：\(F=-I\)、普通步长 3，\(J_{3F}=-I/2\)。C02 取 \(\gamma=1,L=2,\psi(s)=s,\kappa=1/2\)，全域所有门成立。NFB 取 \(A=F,C=0,S=I,M=I/3,\tau=3,\theta=1,u_0=0,\rho=-11/10,\mu=1/10,\beta=100,\zeta=0\)，完整 inverse 可逆，semimonotone 条件等号成立，(3.8) 下降常数精确为正，约 \(0.2655881361644759\)。因此 source(ii) 与严格 C02-v2 的**非单调**同完整算法和实际尾重合。

该报告的两个其它等式也已独立核：\(F=2I\) 可取非零 \(C=I/2\)、\(A=M=S=3I/2\)、\(\tau=\theta=1,u_0=0\)，得到同完整映射 \(x/3\)；\(F=I\) 可取 \(C=I/10,A=M=9I/10,S=I,\tau=\theta=1,u_0=x_0/10\)，记忆不变量 \(u_n=x_n/10\) 使物理轨道仍为 \(x_n/2\)。所有 source 参数门已有合法正证书。故“只有零前向、零 memory、identity metric 才能成为普通 PPA”也是不正确的必要性叙述；其标准还原门只是充分条件。后者须保留所示初始化，不可宣称任意初始 memory 都相同。

只要 \(\|x_k-x_*\|\le Cq^k\)、\(0<q<1\)，即有
\[
 \sum_k\|x_{k+1}-x_k\|\le\sum_k(\|x_{k+1}-x_*\|+\|x_k-x_*\|)<\infty.
\]
因此 NFB 物理 R-linear 结果已经蕴含物理有限长度。这不是本库相对该结果的独立分离点。只有集合距离或非单射核坐标的线性率不授予此推理。

## 4. NFB 任意合格拆分与标准 lift 的必要二次锚界

### 任意同空间 `F=A+C` 的必要条件

固定 \((u,f)\in\operatorname{gph}F\) 和完整零锚 \(s\)。若完整图逐值满足 \(F=A+C\)，置 \(d=u-s\)、\(c=Cu-Cs\)。Assumption 3.1(iii) 与 cocoercivity 给
\[
 \langle d,f\rangle\ge\rho\|f-c\|_{S^{-1}}^2+\beta\|c\|_{S^{-1}}^2.
\]
严格门 \(\beta+\rho>0\) 允许平方完成：
\[
 \rho\|f-c\|_{S^{-1}}^2+\beta\|c\|_{S^{-1}}^2
 =\frac{\beta\rho}{\beta+\rho}\|f\|_{S^{-1}}^2
 +(\beta+\rho)\left\|c-\frac{\rho}{\beta+\rho}f\right\|_{S^{-1}}^2.
\]
故每个原图点必须满足
\[
 \langle u-s,f\rangle\ge\kappa\langle f,S^{-1}f\rangle,
 \qquad \kappa=\frac{\beta\rho}{\beta+\rho}.
 \tag{IA-N1}
\]
它等于 C193 的 SN17，取固定有限矩阵 \(V=-\kappa S^{-1}\)。本推导只需 **solution-anchored** A 条件，不误用 p.7 Proposition 3.3(ii) 的全对前件。正 \(\mu\) 项可直接舍掉，不会取消必要性。

因此 C191 的 \(C\ne\{0\}\) 门、C192 的非退化法向门下，C193 的同图近零序列排除每个合格同空间拆分。不依赖 \(M\) 或算法参数是否有更聪明的选择。C191 的退化 \(C=\{0\}\) 不可排除。

### 标准 primal-dual lift 的压缩

若完整物理关系逐图值确为
\(F=A+C+D+L^*BL\)，则 p.17 的标准总乘积关系为
\[
 K(z,v)=((A+C+D)z+L^*v,\ B^{-1}v-Lz).
\]
每个 \(f\in F(z)\) 都有某 \(v\in BLz\) 满足 \((f,0)\in K(z,v)\)。每个物理解零点 \(s\) 亦可选对应 \(v_*\) 组成乘积零锚。Theorem 4.10 的归约满足上述 anchored completion，故
\[
 \langle z-s,f\rangle
 =\langle(z-s,v-v_*),(f,0)\rangle
 \ge\kappa\langle f,P S^{-1}P^*f\rangle.
 \tag{IA-N2}
\]
这里 \(P\) 是有界坐标投影，故压缩得到固定有限矩阵。这将相同 C193 障碍传递到**论文标准提升**。不必证明 \(v\) 近 \(v_*\)，因为原定理锚界对全部乘积图点全称成立。若自行提出局部版本，则须另核全部近零原图值的近锚 lifting，不能用这一全域理由免门。

任意其它 lift 若不保持 `lifted output=(f,0)`、上述配对或可控残差压缩，IA-N2 没有获得，保持开放。

### C137/C141 的额外近零见证

C137 在任意零锚 \((\bar\xi,\bar\eta,0)\) 取 \(u_\varepsilon=(\bar\xi+\varepsilon^a,\bar\eta,\varepsilon)\)，\(0<a<1/2\)，正支图值。则
\[
 \langle u_\varepsilon-s,f_\varepsilon\rangle=-2\varepsilon^{a+1/2}+3\varepsilon^2,
 \qquad \|f_\varepsilon\|^2=O(\varepsilon).
\]
第二坐标不发生位移，且完整第二图值绝对值至多 \(2\sqrt\varepsilon\)，所以任意锚的同图近零序列均有效。负商发散排除任何固定二次锚界。

C141 取 \(0<a<\gamma/\nu\)，同样第一坐标位移 \(\varepsilon^a\)、法向 \(y=\varepsilon\) 和正支，得到
\[
 \langle u_\varepsilon-s,f_\varepsilon\rangle
 =-A\varepsilon^{a+\gamma/\nu}+\varepsilon^{1+1/\nu}-\varepsilon^2,
 \quad\|f_\varepsilon\|^2=O(\varepsilon^{2\gamma/\nu}).
\]
因为 \(a+\gamma/\nu<2\gamma/\nu<1+1/\nu\)，负项支配每个固定矩阵二次项。所有点最终在 C141 固定小输出 collar 中。因此该局部 collar 也不能靠任意合格同空间拆分或保真标准 lift 直接套用 NFB。

## 5. GPPA 任意 nonlinear ASM 核：两个不同强度的障碍

### 完整纤维障碍：所有零点都被核识别

取两个零图点，IA-G1 立即给 \(v(s)=v(s')\)。故对任意 \(s\in S\)，
\[
 S\subset J^v_{\eta F}(s).
\]
若普通完整 \(J_{\lambda F}(s)=\{s\}\) 且零集非单点，就不可能有该完整一步纤维等号。这适用于 C137、C141、C191/C192 的唯一局部完整纤维。局部包含一段解集亦有相同障碍。

但此结论不排除指定选择绕过额外输出。尤其 \(v\equiv0\) 满足 IA-G1 的任意 \(\epsilon>0\)，非空零集就给 coverage，GPPA 每步任取 \(S\)。各高阶 EB 模型又有局部 inverse R-Lipschitz，所以 Theorem 2 **形式上可以适用于同 F 的这一另一算法**。这是任何“该 F 绝不在 GPPA 框架”说法的致命反例。

### C137 的更强障碍：一条普通非平凡轨道都不能作为 T2 GPPA

在 GC-1 的 \(\eta\le0\)、固定 \(y\ge0\) 切片上，全部图值与 \(\xi,\eta\) 无关：
\[
 f_+(y)=(-2\sqrt y,0,3y),\qquad
 f_-(y)=(-2\sqrt y,0,-5y).
\]
任取同一支相同图值的两个图点，IA-G1 强制核在每个切片常值，记 \(V(y)\)。没有假设核连续或可微。

固定 \(0<a<b<\infty\)。正支差 \(f_+(y)-f_+(z)\) 在 \([a,b]\) 上 Lipschitz。IA-G1 加 Cauchy 给
\(\|V(y)-V(z)\|\le K_{a,b}|y-z|\)。写 \(\Delta V=V(y)-V(z)\)、\(\Delta r=\sqrt y-\sqrt z\)，两种**跨支**比较分别给
\[
 \epsilon\|\Delta V\|^2+2\Delta r\,\Delta V_1
 \le(3y+5z)\Delta V_3,
\]
\[
 \epsilon\|\Delta V\|^2+2\Delta r\,\Delta V_1
 \le-(5y+3z)\Delta V_3.
\]
两分母至少 \(8a\)，分子绝对值为 \(O(|y-z|^2)\)，故
\(|V_3(y)-V_3(z)|\le K'_{a,b}|y-z|^2\)。对区间等分成 \(N\) 段后相加，得到总差至多 \(K'_{a,b}(b-a)^2/N\to0\)。所以 \(V_3\) 在所有正 \(y\) 上常值。

同零锚比较给
\(\|V(y)-V(0)\|\le\|f_+(y)\|/\epsilon\to0\)，故 \(V_3(y)=V_3(0)\) 对每个 \(y>0\) 成立。

普通 GC-2 轨道从 \(p_0\le0,r_0>0\) 出发，始终 \(p_k=p_0\le0\)、\(r_{k+1}=r_k/4>0\)。任何 GPPA 合法更新都要求
\[
 V_3(r_k)-V_3(r_{k+1})\in\eta\{3r_{k+1},-5r_{k+1}\}.
\]
左边为 0，右边两值都非零，矛盾。因此不存在任意 ASM 核、任意正 GPPA 步长，使这条同 F 的非平凡普通轨道成为 Theorem 2 的轨道。

证明没有使用 coverage；即使想补它，矛盾也不会消失。局部版须保留某一近极限邻域中的双支及完整小正 y 切片。只为排除相邻物理轨道更新，正法向核恒定已经足够，不需与零锚识别常数；零锚用于前面的极限识别。删负支或改原图会破坏关键跨支比较，不能泛排除。

交叉核验 GPPA review §7 的推广后，也确认 C141 和 C10 的相应同轨道排除：在切向值只依赖 y 的完整双支片上，正轴紧区间的同支 local Lipschitz 和严格正支间隙，给相邻跨支 normal 变化二阶小量；细 partition 同样强制 normal 核恒定。C141 的 \(\eta\le0\) 片取 \(H(y)=(-Ay^{\gamma/\nu},0)\)、normal 两值 \(y^{1/\nu}-y,-y^{1/\nu}-y\)，在 \(0<y<1\) 上均非零；普通正法向小 collar 轨道遂矛盾。C10 的完整片为 \(H(y)=-\ell_a(4y)\)、normal 两值 3y,-5y，正轴 local C¹ 且间隙8y>0，结论相同。该推广仍依赖完整双支和连续正区间；只沿离散轨道声明条件不能使用 partition，也不符合原文全图 ASM。

## 6. GPPA Theorem 4 的 modulus 极限步骤可修复

原 p.10 证明对 \(\widetilde F=F+\epsilon v\) 用 \((1+2\eta\epsilon)^{-1/2}\)。更直接地，令
\(a=v(u_{k+1})-v(x_*)\)、\(b=v(x_k)-v(x_*)\)，其中 \(x_*\in\operatorname{zer}\widetilde F\)。Adaptive 条件给
\[
 (1+\eta\epsilon)\|a\|^2\le\langle b,a\rangle,
 \qquad \|a\|\le q\|b\|,
 \quad q=(1+\eta\epsilon)^{-1}.
\]
对 \(x_k=u_k+y_k\)、\(\|y_k\|\le\delta\)、L-Lipschitz 核，
\[
 \limsup_k\|v(u_k)-v(x_*)\|
 \le\frac{qL\delta}{1-q}
 =\frac{L\delta}{\eta\epsilon}
 =\frac{L\epsilon}{\eta}.
\]
原 Lemma 3 给 \(\|v(x_*)\|\le a_0:=\inf_{s\in S}\|v(s)\|\)。实际 inverse modulus 输入的 limsup 至多
\[
 B_0=\frac{L\epsilon^2+2L\epsilon/\eta}{\eta}
      +\epsilon(L\epsilon/\eta+a_0).
\]
原 Theorem 4 打印使用
\[
 B=\frac{L\epsilon^2+4L\epsilon/\eta}{\eta}
      +\epsilon(2L\epsilon/\eta+a_0),
 \qquad B-B_0=\frac{2L\epsilon}{\eta^2}+\frac{L\epsilon^2}{\eta}>0
\]
当 \(L,\epsilon>0\)。因此实际输入最终小于 \(B\)，仅由 \(\rho\) 非减即可得打印 \(\epsilon^2+\rho(B)\) bound，无需在正点右连续。不能把原 p.11 的未明说裕度当成定理反例。

边界：固定 \(\eta>0\)、\(\epsilon>0\) 足够小使 \(B<\sigma\) 才在 Definition 5 的窗口内。\(L=0\) 时核常值，实际输入精确等于 \(\epsilon\|v\|=\epsilon a_0=B\)，可直接套包含，无需严格裕度。\(\epsilon=0\) 不在原定理正 regularization 参数范围，不可对 \(q=1\) 使用上述 stationary 公式。若宣称每个任意初值都能生成轨道，须另给 regularized warped coverage；若只对已经合法生成的轨道陈述，该存在性不应被偷换成无条件算法完备性。

## 7. 最后仍未闭的义务与推广阻断

- 完整图的限定排除不是自然母空间总体大小比较，也不是 global prior-art exclusion。
- 任何 nonlinear coordinate change 或非标准 lift，都要单独证明全部原纤维、真实残差、零集和轨道投影身份；本报告没有分类全部这些变换。
- C09 的 Dini 模链保留非幂有限长度与连续回缩；C10 对数族在非 Dini 边界上可距离收缩而点发散。GPPA 的“集合距离不控制物理点”也有同类逻辑边界，故区别本身不宜宣传为首次观察。
- C137/C141 的共同尾与极限选择锐两点模不能仅凭外部线性轨道率推得；但精确外部来源先行性仍待查，不以 NFB 唯一解分支排除它的弱收敛分支所有可能行为。
- uploaded 主稿若承载全图全尺度 Hölder 影子、graph-maximal 完成、完整正反纤维分类，其先行性必须按 C03/C04 单列。两篇算法论文未出现同身份定理，不等于结构稿已获全球新颖性认证。
- `independent_attack_checks.py` 只复核有限 rational 恒等式和几个近零图点。它不证明无限 partition、任意核或任意拆分命题；这些证明在上文逐量词展开。

## 8. 交叉审查记录

已阅读 `gppa_review.md` 冻结稿及 `gppa_check.py`，独立确认如下：

- §3.2 的 T4 严格裕度修复、L=0 常核边界、固定步长小 regularization 窗成立，与本报告 §6 相同。没有理由因打印 proof 的 modulus limit passage 推广为整 theorem 被反驳。
- §5.2 非 calm 子类完整边界、全部 warped 纤维、coverage、inverse R-Lipschitz 和不变量回代均成立；其物理点与长度重合已补到本报告 §3。
- §6 cap 任意核证明及 §7 的 C141/C10 推广量词成立。局部表述必须保留完整双支产品片及连接正法向区间，足够细 partition 是承重门；删支或离散轨道条件不够。
- 唯一非数学措辞建议：§5.2 标题的“带任意非单射核”宜改成“带显式非线性非单射核”，以免读成每个任意核都保原轨道。
- 初版自检修正：纯旋转 (3.8) 的下降常数由漏项的 `5/6` 改成完整的 `1/3`；该修正没有改变覆盖结论。NFB 审查者也独立指出同一漏项。

随后已阅读 `nfb_review.md` 全文、`nfb_check.py` 和 root 的 `COMPARISON.md`。N4/N6 的 anchored square completion、N11 的全图标准 lift 压缩、非退化例外以及 §6 的四个真实重合例均通过独立核验；没有找到阻止这些限定结论升级的 fatal objection。C141 的二次锚近零序列在本报告 §4 已独立闭合，供 NFB 报告补录。

已向 root 提醒一处需改的数学措辞：NFB report §8 的“非几何的可和点尾”宜改成“非几何点尾及可和步长”。C10 在 \(1<a\le2\) 时点误差尾 \(\asymp k^{1-a}\) 本身不可和，但步长 \(\asymp k^{-a}\) 可和。这是文本范围修正，不损害 N4/N11 或有限长度结论。`COMPARISON.md` 保留了固定原图、原轨道、合法分解和指定 lift 的排除合同；本次未见把它们泛化成任意表示或全球先行性结论。

专用有限审计脚本已全通过，输出见 `independent_attack_results.txt`，明确不作为无限量词证明。

### 最终登记层接收：C199–C203 与 E327–E341

受检范围严格限 `CLAIMS.md` 的 C199-v1–C203-v1、`research/graph.json` 的新增 E327–E341 及这些边直接引用的对象/数据/结论节点；对照已经冻结的本报告、GPPA/NFB 专篇与 `COMPARISON.md`。没有重新运行三份已过的计算，也没有重新宣称全文或外部先行性完成。另定向核了 NFB 报告新增 §4.4 C141 任意零锚序列及 §8 步长措辞修正，二者都已正确补入。

登记层核验结果：

- C199：显式核、完整边界法锥和 coverage 保留；全部普通轨道仅声明 GPPA **合法选择包含**，不是 warped 全纤维相等。物理桥限正部/非负法向不变量，负法向初值单列；严格 RLEB 小 R 独立携带。
- C200：cap 固定完整图、固定普通初始化、任意正 h/ε、允许跨支选择及正轴 partition 门保留。C141 的 `p₀≤0,0<r₀<1` 和 C10 全部 a>0 的完整双支排除没有被扩大成全部关系/全部算法；mere monotone、正则化及任意 lift 仍排除在结论外。
- C201：完整 `F=A+C`、固定有界自伴强正定 S、全局 cocoercivity、全部解锚、`ρ>−β` 与每个原图点全称保留。C193 的非退化门完整；C141 任意零锚证明比只选 η≤0 更强但成立，因为第二坐标位移为零，完整第二图值仍为 `O(ε^{γ/ν})`。
- C202：非单调 −Id 的全部 x₀ 重合明确以 `u₀=0` 开始，下降系数 `788/2967>0` 与先前结果文件一致。纯旋转下降 `1/3`，只声明 C24 结论重合；没有将直接兼容等 1 的参数称作严格 C02 证书。非零 C/memory 例未被误宣称为任意初始化等式。
- C203：同一完整原图逐值等号、每个原图值的 `(f,0)` lift、product 零锚、同一 product 的 NFB Assumption 3.1 合法性及固定度量全部明列。压缩 Q 有界且强正定，不因任意辅助变量远离锚而失效；任意其它 lift、局部新定理和算法投影等式仍保留独立门。
- E327–E341 的边方向均是数据/联合必要条件到重合、锚界或限定排除，未倒推类包含。E332/E338 使用非退化锚失败 **合取** 必要锚；cap/SF/log 的排除边也合取相应完整对象和原/压缩必要锚。数据节点单独使用的 E327/E331/E336，在 scope 中已经给全套构造/参数门。

曾提出一个登记澄清：E337 的 scope 及 `AUG-NFB-LIFT-DATA` 标签须显式写“同一 product K 满足 NFB Assumption 3.1”，特别是 product cocoercivity、全部解锚和 `ρ>−β`；这一门在 C203 与证明中原已正确存在。root 已将同一 product 的全部合法性前件补入 E337、数据节点标签与 `COMPARISON.md` §7。本审查已再次定向读取这三处，确认补显完整；不存在把任意完整图 lift 与条件性必要引理无条件合用的登记逃口。

**最终登记接收冻结；Fatal 清单：空。** 接收仅针对以上固定身份/合取合同，不授予任意 reformulation 总排除、整个自然类核分类、总体规模比较或全球先行性结论。C199–C203 与 E327–E341 在此次受检范围内未新增过宽量词、错误边方向或遗漏承重合取门；生成资产验证与提交由 root 负责，本子审查未执行 commit/push。
