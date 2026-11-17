# Target 3：输出距离收缩与输出尺度步长的耦合

**日期**：2026-11-17。  
**身份**：`candidate` / `derived-checked` 的引理与反例；未作外部首创性判断。  
**目的**：严格区分下列一步性质与传统的次单调性加 metric subregularity，并检查是否存在不把二者简单重命名的候选性质。

## 1. 对象、量词和两条待比较的条件

令 `X` 为完备 Hilbert 空间（以下反例均在有限维欧氏空间），`S⊂X` 非空闭，
`d(z)=d(z,S)`。固定 `λ>0`，用
(mathcal Asubset X	imes X) 表示实际允许的输入—输出转移；对
`(x,y)∈𝒜` 记

\[
 d_x=d(x),qquad d_y=d(y),qquad s=\|x-y\|.
\]

若需要原算子，取 `w=(x−y)/λ∈F(y)`。必须区分 `𝒜` 是允许子关系还是完整关系

\[
 \mathcal G=\{(y,w): (y+\lambda w,y)inmathcal A\}
 \quad\text{与}\quad \operatorname{gph}F.
\]

本节讨论的两个条件是对**每个允许转移**量化的

\[
\tag{A} d_y\le \kappa d_x,qquad 0<\kappa<1,
\]

\[
\tag{B} s\le B d_y,qquad 0<B<\infty.
\]

传统的比较对象取 Luke--Tam 型的点对次单调性（`λ=1` 的写法）

\[
\tag{SM}
 \langle y-y',w-w'\rangle
 \ge -\tau\|(y+w)-(y'+w')\|^2,
 \qquad 	au\ge0,
\]

以及同一完整 `F` 上的线性 metric subregularity

\[
\tag{MSR} d(y,S)\le K r_F(y),
 \qquad r_F(y)=\inf_{vin F(y)}\|v\|.
\]

若文献采用另一种次单调缺陷（例如以 (|w-w'|^2) 为分母），必须重新核算；本文的“失败次单调”专指上面的 (SM)，即 Minty 输入差的版本。

## 2. 一个不能绕过的完整图障碍

### 引理 2.1（完整图上的 (A) 自动给出线性 MSR）

假设 (A) 对某个输出窗内的**每个**完整图点 `(y,w)∈gph F` 都适用，并且
`x=y+λw` 是该点对应的输入。则

\[
 d(y,S)\le \\frac{\\kappa\\lambda}{1-\\kappa}\\,r_F(y).
\tag{2.1}
\]

**证明。** 距离函数是 1-Lipschitz，故

\[
 d_x=d(y+\lambda w,S)\le d_y+\lambda\|w\|.
\]

由 (A)，

\[
 d_y\le\kappa(d_y+\lambda\|w\|),
 \qquad (1-\kappa)d_y\le\kappa\lambda\|w\|.
\]

对 `w∈F(y)` 取下确界即得 (2.1)。若只在一个局部窗内对完整纤维中满足 `y+λw∈U` 的图点使用 (A)，则 (2.1) 只在相应输出集合上成立；不能把它扩大成全局 MSR。\(\square\)

### 推论 2.2（完整图版本不可能有“(A)+(B)但无 MSR”反例）

如果 (A) 对完整 `gph F` 成立，则不论是否假设 (B)，传统线性 MSR 已由引理 2.1 得到。因此，要求“满足 (A)+(B) 但不满足 MSR”的反例只能把 (A)+(B) 量化在允许子关系

\[
\mathcal A\subsetneq\{(y+\lambda w,y): (y,w)\in\operatorname{gph}F\}
\]

上，或把 MSR 评价在完整纤维而 A 仅评价在选中输出上。这是量词差异，不是常数技巧。

### 引理 2.3（(A)+(B) 的有限长度结论）

若每个允许选择都满足 (A)+(B)，则任意轨道
`x_{k+1}∈𝒜(x_k)` 满足

\[
 d_k\le \kappa^k d_0,
 \qquad s_k:=\|x_{k+1}-x_k\|
 \le B\kappa^{k+1}d_0,
\]

以及

\[
 \sum_{k=0}^{\infty}s_k
 \le \frac{B\kappa}{1-\kappa}d_0<\infty.
\tag{2.2}
\]

因此在完备 `X` 中轨道收敛；`S` 闭且 `d_k→0` 时极限属于 `S`。在 `d_0=0` 时 (B) 直接给 `s_0=0`，所以 (A)+(B) 还自动给零集的逐点吸收。证明只用几何级数，不使用图内积或残差。

## 3. 真正不同于 (A)+(B) 的候选：幂次望远镜降落

### 定义 3.1（PTD，Power-Telescoping Descent）

在给定允许关系 `𝒜` 和工作窗 `d_x≤R` 上，称 `(S,𝒜)` 满足

\[
\operatorname{PTD}(\kappa,C,\alpha;R),
\qquad 0<\kappa<1,  C<\infty,  0<\alpha\le1,
\]

若对每个允许转移都有

\[
 d_y\le\kappa d_x,
 \qquad
 s\le C\bigl(d_x^{\alpha}-d_y^{\alpha}\bigr).
\tag{PTD}
\]

它的独立含义是：物理位移由一个**可望远镜的径向势** `V(z)=d(z,S)^α` 的实际下降支付。这里没有要求点对之间的内积、不需要 `r_F` 或完整逆纤维，也没有把 `s/d_y` 预先限制为有界常数。

### 命题 3.2（(A)+(B) 蕴含 PTD，但反向严格不成立）

若 (A)+(B) 成立，则 `PTD(κ,C,1;R)` 成立，其中可取

\[
 C=\frac{B\kappa}{1-\kappa}.
\tag{3.1}
\]

事实上 `d_y≤κd_x` 给出

\[
 d_x-d_y\ge\frac{1-\kappa}{\kappa}d_y,
\]

从而 `C(d_x−d_y)≥Bd_y≥s`。因此 PTD 是一个由单一望远镜不等式定义的独立候选；它不只是把 (A) 和 (B) 并列写一遍。

### 命题 3.3（PTD 的轨道结论）

在完备 `X` 中，PTD 的任意允许轨道满足

\[
 \sum_{j=0}^{N-1}s_j
 \le C`d_0^α−d_N^α`\le C d_0^\alpha,
 \qquad d_N\le\kappa^N d_0.
\tag{3.2}
\]

故轨道有限长并收敛于 `S`。零输入时右端为零，得到零吸收。此结论不需要 Dini 条件，因为 PTD 已经把实际位移写成望远镜差；如果只给一般模而不提供差分结构，不能直接套用 (3.2)。

### 例 3.4（PTD 成立而 (B) 失败；严格排除“PTD=(A)+(B)”）

令

\[
 X=\mathbb R^2,
 \quad S=\mathbb R\times\{0\},
 \quad U=\{(u,t):|t|\le1\},
\]

并取 `0<q<1`、(0<\alpha<1)，

\[
 T(u,t)=\bigl(u+|t|^\alpha,qt\bigr),
 \qquad (x,y)=(x,T(x)).
\tag{3.3}
\]

这里 (d_x=|t|)、(d_y=q|t|)，所以 (A) 以 `κ=q` 成立。并且

\[
 s\le |t|^\alpha+(1-q)|t|
 \le(2-q)|t|^\alpha
 =\frac{2-q}{1-q^\alpha}`d_x^α−d_y^α`.
\]

故 PTD 成立，可取 (C=(2-q)/(1-q^\alpha))。然而

\[
 \frac{s}{d_y}\ge\frac{|t|^\alpha}{q|t|}
 =q^{-1}|t|^{\alpha-1}\longrightarrow\infty
 \quad(t\to0),
\]

不存在任何有限 (B) 使 (B) 成立。轨道的水平位移虽比输出距离大得多，仍由
`∑q^{αk}|t_0|^α<∞` 支付。这个例子是 `derived-checked` 的严格包含见证。若要嵌入普通 PPA，取 `λ=1` 并令
`F(T(x))∋x−T(x)`，在 `S` 上另放置零图点；所有结论均关于所声明的允许关系。

**范围判断。** PTD 只在“已有距离收缩”的算法上下文中比传统图条件更弱。单独的传统次单调性加 MSR 并不自动推出 (A)：还需要 coverage、步长门、零吸收和评价窗。因此不能把 PTD 宣称为它们在裸逻辑上的蕴含弱化；准确说法是：在传统条件已经闭合为 (A)+(B) 的同一算法上，PTD 是更宽的、只保留收敛承重结构的证书。

## 4. 逐项反例与边界

### 4.1 (A)+(B) 成立但 (SM) 失败（完整图反例）

取 `X=ℝ²`、`S=ℝ×{0}`、`λ=1`。令

\[
 t_n=\frac1n,\qquad e_n=\frac1{n^3},\qquad
 y_n=(t_n,1),\qquad x_n=(e_n,3),
\]

\[
 w_n=x_n-y_n=(e_n-t_n,2).
\tag{4.1}
\]

把 (n=\infty) 定义为 (t_\infty=e_\infty=0)，并取完整图

\[
 \operatorname{gph}F
 = (S\times\{0\})\cup\{(y_n,w_n):n\in\mathbb N\cup\{\infty\}\}.
\]

相应输入—输出转移是 (x_n\mapsto y_n)，以及 `s↦s`（`s∈S`）。图的极限点已经加入，因此这是闭图；零集恰为 `S`。对每个 `n`，

\[
 d(x_n,S)=3,\quad d(y_n,S)=1,\quad
 \|x_n-y_n\|=\sqrt{(e_n-t_n)^2+4}<3.
\]

故 (A) 以 `κ=1/2` 成立，(B) 以 `B=3` 成立。

但令相邻差

\[
 \delta_t=t_n-t_{n+1}=\frac1{n(n+1)},\qquad
 \delta_e=e_n-e_{n+1}
 =\frac{3n^2+3n+1}{n^3(n+1)^3}.
\]

则

\[
 \Delta y=(\delta_t,0),\qquad
 \Delta w=(\delta_e-\delta_t,0),\qquad
 \Delta x=(\delta_e,0),
\]

从而

\[
 \frac{-\langle\Delta y,\Delta w\rangle}{\|\Delta x\|^2}
 =\frac{\delta_t(\delta_t-\delta_e)}{\delta_e^2}
 \sim\frac{n^4}{9}\longrightarrow\infty.
\]

任何固定 (	au) 都不能使 (SM) 对这些点对成立。这个例子显示，A+B 只控制每个输入—输出三元组相对于 `S` 的尺度，不控制不同图点之间的 Minty 输入差和方向相关性。

### 4.2 (A)+(B) 成立但完整 `F` 不满足 MSR（只能是允许子关系例）

令 `X=ℝ`、`S={0}`、`λ=1`，定义完整算子

\[
 F(0)=\{0\},\qquad F(y)=\{y,y^2\}\quad(y\ne0).
\tag{4.2}
\]

只允许选中值 `w=y`，即允许输入 `x=2y`；另一值 `w=y²` 的输入 `x=y+y²` 保留在完整图中但不在 `𝒜` 中。对允许转移，

\[
 d_y=|y|=\tfrac12d_x,qquad s=|y|=d_y,
\]

所以 (A)+(B) 取 `κ=1/2, B=1`。但在 `0<|y|<1` 时

\[
 r_F(y)=|y|^2,qquad
 \frac{d_y}{r_F(y)}=\frac1{|y|}\to\infty,
\]

完整 `F` 没有任何局部线性 MSR。这个例子不与引理 2.1 冲突：A 没有对额外完整图值量化。若强行要求 A 对完整纤维的所有 `w` 成立，则该反例被引理 2.1 排除。

### 4.3 只有 (A)：距离收缩而点列不收敛

仍取 `X=ℝ²`、`S=ℝ×{0}`。对 `t≠0` 定义

\[
 T(u,t)=(u+1,t/2),
 \qquad T(u,0)=(u,0).
\tag{4.3}
\]

每步有 `d(T(u,t),S)=d((u,t),S)/2`，即 (A) 取 `κ=1/2`。但

\[
 \frac{\|(u,t)-T(u,t)\|}{d(T(u,t),S)}
 =\frac{\sqrt{1+t^2}}{|t|/2}\to\infty,
\]

所以 (B) 失败。起点 `x_0=(0,1)` 的轨道为

\[
 x_k=(k,2^{-k}),
\]

距离趋于零而点列发散。故距离收缩不能替代物理步长可和性。

一个紧的非孤立版本是 `S=𝕊¹`，在管域 `1/2<‖x‖<3/2` 上令

\[
 T(re^{i\theta})=\bigl(1+\tfrac12(r-1)\bigr)e^{i(\theta+\theta_0)}.
\]

它满足 (d(Tx,S)=\frac12d(x,S))。若从 `S` 上起步且 (	heta_0/(2\pi)) 无理，轨道始终在 `S` 上旋转而不收敛；这揭示了 (A) 在 `d=0` 处没有零吸收信息。

### 4.4 只有 (B)：步长相对输出距离有界但轨道发散

取 `X=ℝ`、`S={0}`、`T(x)=2x`。则

\[
 d_y=2d_x,qquad |x-y|=d_x=\tfrac12d_y,
\]

故 (B) 取 `B=1/2`，但对任何 `κ<1` 都不满足 (A)。轨道 `x_k=2^k x_0` 发散。对应 `λ=1` 的单值原算子为 `F(y)=−y/2`。

### 4.5 非凸、非孤立解集并不自动破坏 (A)+(B)

取 `S=𝕊¹⊂ℝ²`，管域 `U={1/2<‖x‖<3/2}`，`0<q<1`，并定义

\[
 T(re^{i\theta})=\bigl(1+q(r-1)\bigr)e^{i\theta}.
\tag{4.4}
\]

这里 `S` 非凸且每个解点都非孤立；然而

\[
 d(Tx,S)=q d(x,S),\qquad
 \|x-Tx\|=(1-q)d(x,S)=\frac{1-q}{q}d(Tx,S).
\]

因此 (A)+(B) 取 `κ=q`、`B=(1−q)/q`。每条轨道保留自己的角度并收敛到 `S` 上的某点；集合不必凸、解点也不必孤立。若零集有整条线，(A)+(B) 同样只保证趋近集合，不选出唯一点。

## 5. 结构性候选：径向—切向图锥（仅候选，不冒充 PTD）

为寻找不依赖“先检查 A+B”的原生验证器，可在仿射零集上定义一个锥条件。令 `S` 为闭仿射子空间，`p=P_S(y)`，`n=y−p`，`s=x−y=λw`。考虑

\[
\tag{RTC}
 \langle n,s\rangle\ge \mu\|n\|^2,
 \qquad \|s\|\le C\|n\|,
 \qquad \mu>0.
\]

它是输出最近锚处的原始法向恢复与共同位移预算，不比较两个不同图点。因为 `S` 仿射，

\[
 d(x,S)^2=\|n+P_{N`S`}s\|^2
 \ge (1+2\mu)\|n\|^2,
\]

故 (RTC) 推出 (A)，其中 `κ=(1+2μ)⁻¹ᐟ²`，并直接推出 (B)，其中 `B=C`。对一般 `C²` 或 prox-regular `S`，上式需加入 reach/曲率误差和切向项；C282 的正常管定理提供了一个独立的曲率补偿模板，但尚未证明 RTC 的最小假设版本。

RTC 与 (SM) 是不同轴：它只用一个输出锚，不给任意两图点的 Minty 方向。第 4.1 节的完整图反例甚至满足 RTC：对 `n_n=(t_n,1)`、`s_n=w_n`，

\[
 \langle n_n,s_n\rangle
 =2-t_n^2+t_n^4
 \ge 1+t_n^2=\|n_n\|^2,
 \qquad \|s_n\|\le\sqrt5\|n_n\|,
\]

可取 `μ=1, C=√5`，但 (SM) 仍失败。反过来，`S={0}`、`T(x)=−x/2` 满足 (A)+(B)，而 `s=x−y=−3y` 给出 `⟨y,s⟩<0`，故不满足任何 `μ>0` 的 RTC。

**状态判断。** RTC 是一个可由零集邻管和原始法向/切向分解验证的结构候选，但目前只能说它与“次单调性+MSR”**不可比**：它可避开点对次单调性，但其正法向门比一般 A+B 更强，且曲零集上的覆盖、完整远根和最小曲率误差仍需独立证明。不能把 RTC 宣称成已经证明的“更弱统一性质”。PTD 才是目前有严格包含关系的算法级候选。

## 6. 对候选 P 的去重审查与剩余义务

1. **不是 (A)+(B) 改名。** PTD 的第二条是不同时刻的距离幂差 `d_x^α−d_y^α`，而不是输出距离 `d_y`；例 3.4 证明 PTD 可成立而 B 必然失败。
2. **仍未得到传统条件的裸逻辑弱化。** 次单调性+MSR 单独还缺 coverage、零吸收、参数门和完整输出量词。准确的比较是：在它们已经闭合成 A+B 的同一算法上，PTD 保留有限长度承重且放宽每步 B；裸假设层面二者不可直接排序。
3. **完整 MSR 的量词是决定性障碍。** 引理 2.1 必须进入 README/CLAIMS 的定义图：若未来声称 A+B 比传统 MSR 更弱，必须明确 A 是允许子关系性质；若 A 对完整纤维，则该声称为假。
4. **结构路线未闭。** RTC 在仿射 `S` 上的 A 推导已核；一般曲 `S` 需明确 reach、法向投影、coverage 和所有远端根。不能用有限数值或选中分支替代这些证明义务。
5. **未建立外部优先性。** 本文件只登记内部推导、反例和候选状态，不声称 PTD/RTC 在文献中首创，也不把它们升级为 canonical 定理。

## 7. 供后续工作的精确行动

- 若要把 PTD 升为 canonical，先固定允许关系、工作域、\(\alpha\) 量词和完整/子关系范围，再寻找一个不依赖已知轨道的原始模型验证器；至少检查非凸 `S`、非孤立 `S`、零输入和 coverage。
- 若要推进 RTC，先在具有 reach 下界的 `C²` 零集上给出含曲率余项的精确 A 因子，再构造一条满足 RTC 但完整远端纤维失效的反例，确定 coverage 是否必须单独假设。
- 若主目标只需局部算法结论，PTD 已给出比 B 更宽的可和接口；不要将“距离收缩但点不收敛”的 A-only 反例误读为 PTD 反例，因为 PTD 的望远镜预算正是排除该漂移的新增结构。
