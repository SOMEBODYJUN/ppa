# 目标二：LMZ 的 KL 框架、普通 exact PPA 转移与独立反例

日期：2026-11-17
状态：阶段性独立审查；本文件不把 LMZ 的抽象定理转写成 PPA 的无条件结论，也不新增或升级 CLAIMS.md 中的 Claim。

## 0. 来源与审查边界

本轮逐段核对的固定抽取是 'mor/paper.txt'（SHA-256 00cd42f151df9be145541b83274db10e06e616560967d701cdfa02d1053cda92，对应 arXiv:2406.13207 v1）以及同一批源码 'lmz-src/main_update.tex'（SHA-256 6a853b0f04882e5ea8a22d8e07ecdfe8144790e7017e84f097ed649caa120d5f）。

本文中的“paper fact”只指上述 v1 文本明确写出的定义、假设、定理和证明步骤；“PPA transfer”是把这些前件逐项映射到普通精确近端点算法后得到的条件结论；“objection”是量词、适用域、缺失前件或公式本身的独立检查，不是对论文整体的否定。

## 1. Paper fact：定义、基本假设与定理接口

### 1.1 Definition 3.1（广义度量次正则）

令 \(f:\mathbb R^m\to\overline{\mathbb R}\)，
\[
\Gamma=\{x\mid 0\in\partial f(x)\},\qquad \Xi\subset\Gamma,
\qquad \bar x\in\Xi,
\]
并令 \(\psi:\mathbb R_+\to\mathbb R_+\) 为 admissible（\(\psi(0)=0\)，且 \(\psi(t_n)\to0\Rightarrow t_n\to0\)）。

* pointwise：存在 \(\kappa,\delta>0\)，使
  \[
  \psi(d(x,\Xi))\le \kappa\,d(0,\partial f(x))
  \quad(x\in B(\bar x,\delta));
  \]
* uniform：存在 \(\kappa,\rho>0\)，使同一不等式对
  \(\mathcal N(\Xi,\rho)=\{x:d(x,\Xi)\le\rho\}\) 全部成立。

这一定义是误差界型前件；它本身没有给出能量下降、次梯度 relative-error、输入覆盖或 PPA 的 proximal 最小化。KL 性质与 Definition 3.1 是两个不同接口。

### 1.2 (H0)–(H3) 与 (H1')

源码明确列出基本假设（'lmz-src/main_update.tex:496--518'；抽取见 'mor/paper.txt:367--386'）：

* (H0) descent：\(f(x_{k+1})\le f(x_k)\)；
* (H1) surrogate：存在 \(c>0\)，且在 \(e_k\to0\) 时
  \(\|x_{k+1}-x_k\|\le c e_k\)；
* (H2) relative error：存在 \(w_{k+1}\in\partial f(x_{k+1})\)，
  \[
  \|w_{k+1}\|\le b\,\beta(e_k),
  \]
  其中 \(b>0\)，\(\beta\) admissible；
* (H3) continuity along cluster subsequences：若 \(x_{k_j}\to\tilde x\)，则
  \(\limsup_j f(x_{k_j})\le f(\tilde x)\)。

论文随后使用更强的 (H1')：存在 \(a,c>0\) 与 admissible \(\varphi\)，使
\[
 f(x_{k+1})+a\varphi(e_k)\le f(x_k),\qquad
 \|x_{k+1}-x_k\|\le c e_k. \tag{H1'}
\]
定理 5.1 还要求 \(\varphi,\beta\) **increasing**；这不是“KL 性质自动提供”的条件。

从 (H1')、(H2)、(H3) 以及有界 level set，Lemma 4.1 给出 \(e_k\to0\)、所有聚点是 \(\Gamma\) 中的 stationary point，并且对任意 \(\Omega\subset\Xi\subset\Gamma\)，\(d(x_k,\Xi)\to0\)。

### 1.3 Theorem 4.3 / 4.4

Theorem 4.3（'mor/paper.txt:459--481'）不是“KL 定理”：在 (H0)–(H3)、有界 level set、\(\bar x\in\Omega\subset\Xi\subset\Gamma\) 下，另给非负误差 \(s_k\to0\)、asymptotically shrinking 的 \(\tau\)，以及局部递推
\[
s_k\le\tau(s_{k-1}),\qquad
e_k\le \ell_1e_{k-1}+\ell_2\Lambda_{k,k+1}+\ell_3s_k,
\]
其中 \(0\le\ell_1<1\)，
\[
\Lambda_{k,k+1}=\xi(f(x_k)-f(\bar x))-\xi(f(x_{k+1})-f(\bar x)).
\]
结论是最终留在 KL/局部球内、\(\sum e_k<\infty\)、\(\sum\|x_{k+1}-x_k\|<\infty\)，并且 \(x_k\to\bar x\)。

Theorem 4.4（'mor/paper.txt:592--635'）把 Definition 3.1 的 pointwise generalized metric subregularity 与
\[
e_k\le\ell d(x_k,\Xi)
\]
及
\[
\tau(t)=\psi^{-1}(\gamma b\beta(\ell t)),\qquad
\limsup_{t\downarrow0}\tau(t)/t<1
\]
组合起来。注意 \(e_k\le\ell d(x_k,\Xi)\) 是独立算法前件，不能由 Definition 3.1 单独反向推出。

### 1.3a 正则化步中的 (2\sigma) 项（Lemma L3.3/L4.4）

这一步不是 KL 证明本身，而是论文为高阶正则化算法验证 Theorem 4.4 所需的
\(e_k\le\ell d(x_k,\Theta)\) 型估计。源码 `lmz-src/main_update.tex` 的
Lemma L3.3（约 1313--1356 行）令
\[
 z=y_\sigma(x),\quad u=\|z-x\|,\quad v=\|x-\widecheck x\|=d(x,\Theta),
\]
其中 \(\widecheck x\) 是到 \(\Theta\) 的投影点。由正则化子问题的一阶方程
（式 (A92)）和 Hessian 的 Hölder 估计，论文先得到（式 (A96)）
\[
 {\sigma\over q+1}u^q\|z-\widecheck x\|
 \le {L_2\over q+1}v^{q+1}+{\sigma\over q+1}u^qv+L_2uv^q.
\]
三角不等式 \(\|z-\widecheck x\|\ge u-v\) 给出
\[
 {\sigma\over q+1}u^{q+1}-{\sigma\over q+1}u^qv
 \le {\sigma\over q+1}u^q\|z-\widecheck x\|.
\]
把这个下界代回 (A96) 时，右侧原有的
\(\frac{\sigma}{q+1}u^qv\) 与代回产生的同量项相加，**必须**保留为
\(\frac{2\sigma}{q+1}u^qv\)：
\[
 {\sigma\over q+1}u^{q+1}
 \le {L_2\over q+1}v^{q+1}
   +{2\sigma\over q+1}u^qv+L_2uv^q. \tag{A96'}
\]
当 \(v>0\) 时令 \(t=u/v\)，乘以 \((q+1)/v^{q+1}\)，得到
\[
 H_\sigma(t):=\sigma t^{q+1}-2\sigma t^q-L_2(q+1)t-L_2\le0. \tag{A97'}
\]
Lemma L4.4(i)--(ii)（源码约 1253--1308 行）证明：对 \(q\in(0,1]\)，
\(H_\sigma\) 有唯一正根 \(t(\sigma)>2\)，且 \(H_\sigma(t)\le0\) 蕴含
\(t\le t(\sigma)\)。故
\[
 \|y_\sigma(x)-x\|=u\le t(\sigma)v=t(\sigma)d(x,\Theta).
\]
若 \(v=0\)，则应直接回到 (A96')：其右侧为零，故 \(u=0\)；不能在
\(v=0\) 时先除以 \(v^{q+1}\)。这正是 Lemma L4.4(ii) 中单独处理 \(y=0\)
的边界情形。

* **Paper fact：** 论文没有丢掉第二个 \(\sigma\) 项，而是通过 (A96') 将它编码
  到 \(H_\sigma(t)=\sigma t^{q+1}-2\sigma t^q-L_2(q+1)t-L_2\) 中，再调用
  Lemma L4.4 得到统一常数 \(\ell_\sigma=t(\sigma)\)。
* **PPA transfer：** 只有在算法步确实是该正则化子问题的选定 minimizer，且投影点
  \(\widecheck x\in\mathcal F\) 等论文前件成立时，才能把这一步转写成
  Theorem 4.4 所需的 \(e_k\le\ell d(x_k,\Xi)\)（并且要明确 \(\Xi=\Theta\) 或给出
  从 \(\Theta\) 到所用 stationary 集的包含关系）。普通 exact PPA 的
  \(e_k=\|x^{k+1}-x^k\|\) 映射并不自动使用这个 (2\sigma) 推导。
* **Objection：** 若把 (A96) 直接写成只有一个 \(\sigma\) 项，所得根方程会错误地变成
  \(\sigma t^{q+1}-\sigma t^q-\cdots=0\)，从而改变 \(\ell_\sigma\)；若在 \(v=0\)
  时除法，则会漏掉 \(x\in\Theta\) 的退化情形。审查中应把这两点列为代数和量词检查项，
  但按 v1 源码本身，(2\sigma) 的处理是完整的。

### 1.4 Theorem 5.1：KL 证明的真实桥梁

定理 5.1（'mor/paper.txt:716--785'）假设：

1. (H1')、(H2)、(H3) 与某个有界 level set；
2. \(\bar x\) 是迭代序列的 accumulation point；
3. \(f\) 在 \(\bar x\) 满足 KL，desingularizer 为 \(\vartheta\)；
4. 存在 \((\mu_1,\mu_2)\in(0,1)\times\mathbb R_+\)，满足
   \[
   \limsup_{(s,t)\to(0,0)}
   \frac{\varphi^{-1}(\beta(s)t)}{\mu_1s+\mu_2t}\le1. \tag{5.1}
   \]

证明的可审计链条如下：

* 取 \(\alpha\in(1,1/\mu_1)\)，由 (5.1) 得小量不等式
  \[
  \varphi^{-1}(\beta(s)t)\le\alpha\mu_1s+\alpha\mu_2t. \tag{5.2}
  \]
* 由 Lemma 4.1 和 (H1') 得 \(f(x_k)\downarrow f(\bar x)\)、\(e_k\to0\)。进入 KL 球后，若 \(e_k>0\)，(H1') 给出严格下降 \(f(x_{k+1})<f(x_k)\)。
* 将 (H2) 移位一格写成 \(w_k\in\partial f(x_k)\)、\(\|w_k\|\le b\beta(e_{k-1})\)。KL 不等式与 \(d(0,\partial f(x_k))\le\|w_k\|\) 给出
  \[
  \vartheta'(f(x_k)-f(\bar x))\ge\frac1{\|w_k\|}
  \ge\frac1{b\beta(e_{k-1})}. \tag{5.6}
  \]
* 凹性与 (H1') 给出
  \[
  \Lambda_{k,k+1}:=\vartheta(f(x_k)-f(\bar x))-
  \vartheta(f(x_{k+1})-f(\bar x))
  \ge a\vartheta'(f(x_k)-f(\bar x))\varphi(e_k). \tag{5.7}
  \]
  因而
  \[
  \varphi(e_k)\le {b\over a}\,\beta(e_{k-1})\Lambda_{k,k+1}.
  \]
* 对 \(s=e_{k-1}\)、\(t=(b/a)\Lambda_{k,k+1}\) 应用 (5.2)，得到
  \[
  e_k\le \alpha\mu_1 e_{k-1}+{\alpha\mu_2b\over a}\Lambda_{k,k+1},
  \]
  这是 Theorem 4.3 所需的递推，且 \(\alpha\mu_1<1\)。因此有限长度与单点收敛来自 Theorem 4.3，而不是来自 KL 不等式单独。

### 1.5 Theorem 5.2 与 Remark 5.3

定理 5.2（'mor/paper.txt:795--872'）先定义
\[
\rho(t)=((\vartheta^{-1})')^{-1}(b\beta(t)),\qquad
\xi(t)=\varphi^{-1}\!\left({\vartheta^{-1}(\rho(t))\over a}\right),
\]
再额外要求 \(\xi\) increasing 且 \(\xi(t)/t\to0\)。由定理 5.1 的有限长度先得到
\(e_k\le\xi(e_{k-1})<e_{k-1}/2\)，继而
\(\|\bar x-x_k\|\le2c\xi(e_{k-1})\)。若再有 \(e_k\le r\|x_{k+1}-x_k\|\) 或 \(e_k\le\ell d(x_k,\Xi)\)，才得到 (5.8)/(5.10) 的点收敛率。

Remark 5.3 的第一项是正确的：普通 proximal 参数 \(\varphi(t)=t^2,\ \beta(t)=t\) 时
\[
\varphi^{-1}(\beta(s)t)=\sqrt{st}\le(s+t)/2,
\]
故可取 \((\mu_1,\mu_2)=(1/2,1/2)\)。一般 \(\beta(t)=t^\alpha,\ \varphi(t)=t^{1+\alpha}\) 时，权 AM–GM 给
\[
(\mu_1,\mu_2)=\left({\alpha\over1+\alpha},{1\over1+\alpha}\right).
\]

**独立公式审查（objection，局限于 Remark 5.3 的文字率式）：**同一段 'mor/paper.txt:899--909'（源码 'lmz-src/main_update.tex:913--920'）在 \(\theta>\alpha/(1+\alpha)\) 的尾率中印出
\[
 k^{-\alpha(1-\alpha)/((1+\alpha)\theta-\alpha)}.
\]
从其前面已经得到的 \(\xi(t)=C\,t^r\)、\(r=\alpha/((1+\alpha)\theta)<1\) 直接解递推，标准尾和指数应为
\[
 {r\over1-r}={\alpha\over(1+\alpha)\theta-\alpha},
\]
若按高阶 regularized Newton 的专门参数化则为
\((q+1)(1-\theta)/((q+2)\theta-(q+1))\)（源码 'lmz-src/main_update.tex:1441--1448'）。因此 Remark 5.3 的 \(1-\alpha\) 很可能是排版/笔误；它不进入 Theorem 5.1 的有限长度证明，但应在任何正式引用中标为待修正，不能把该印刷式当作已核定一般率。

## 2. KL-only 反例：没有下降和 relative-error 就没有有限长度

这是一个只使用 KL、平滑性和有界 level set 的抽象序列，不满足 LMZ 的算法接口。

取
\[
 f(x)=\tfrac12x^2\quad(x\in\mathbb R),\qquad
 x_k=\sin(\log(k+2)),\qquad e_k=|x_{k+1}-x_k|.
\]
则 \(f\) proper、连续、bounded below，任意有限 sublevel set 有界；\(\bar x=0\) 是序列的 accumulation point。取 \(\vartheta(s)=\sqrt{2s}\)，对于 \(x\ne0\) 有
\[
\vartheta'(f(x)-f(0))\,d(0,\partial f(x))
 ={1\over|x|}|x|=1,
\]
故 \(f\) 在 \(0\) 满足 KL（指数 \(1/2\)）。

另一方面，\(x_k\) 沿 \(\sin(\log k)\) 的相位反复经过接近 \(1\) 与 \(-1\)，所以不收敛；在每个 \(|\cos t|\ge1/2\) 的对数相位区间内，
\(|x_{k+1}-x_k|\gtrsim1/k\)，从而
\[
\sum_k e_k=\infty,\qquad \sum_k|x_{k+1}-x_k|=\infty.
\]
这里 \(f(x_{k+1})\le f(x_k)\) 反复失败，因而任何 \(a>0\) 与正的 admissible \(\varphi\) 都不可能使 (H1') 成立。更强地，在 \(x_{k_j+1}\to1\) 的子列上，\(e_{k_j}\to0\) 但唯一次梯度 \(w_{k_j+1}=x_{k_j+1}\to1\)。对**任意** admissible \(\beta\)，\(\beta(e_{k_j})\to0\)，故不存在固定 \(b\) 使 (H2) 成立。

该反例还满足 H3（\(f\) 连续）和有界 level set；失败仅来自缺少 Lyapunov 下降与 relative-error 接口。因此“目标函数 KL”不能绕过 (H1')/(H2)，也不能单独推出有限长度、单点收敛或 Theorem 5.1 的局部递推。

## 3. 普通 exact PPA 的可审计映射定理（PPA transfer）

**定理（exact global proximal step 的 LMZ 接口）。** 设 \(H=\mathbb R^m\)，\(\lambda>0\)，\(f:H\to\overline{\mathbb R}\) proper l.s.c.；给定 \(x^0\in\operatorname{dom}f\)，并假设每一步全局子问题
\[
 x^{k+1}\in P_\lambda(x^k):=\operatorname*{argmin}_{y\in H}
 \left\{f(y)+{1\over2\lambda}\|y-x^k\|^2\right\}
\]
有有限值解且选定一个解。令
\[
 e_k:=\|x^{k+1}-x^k\|,
 \qquad w_{k+1}:={x^k-x^{k+1}\over\lambda}.
\]
则逐步有：

1. **Lyapunov descent（全局最小化比较）**
   \[
   f(x^{k+1})+{1\over2\lambda}e_k^2\le f(x^k).
   \]
2. **Fermat/次梯度接口**
   \[
   w_{k+1}\in\partial f(x^{k+1}),
   \qquad \|w_{k+1}\|={1\over\lambda}e_k.
   \]
3. 因而 exact PPA 自动满足 LMZ 的 (H1') 与 (H2)，可取
   \[
   a={1\over2\lambda},\quad c=1,\quad
   \varphi(t)=t^2,\quad \beta(t)=t,\quad b={1\over\lambda}.
   \]
4. (5.1) 由 \(\sqrt{st}\le(s+t)/2\) 成立，取
   \((\mu_1,\mu_2)=(1/2,1/2)\)。

因此，若再单独验证某个有界 level set、存在 accumulation point，以及 H3（例如 \(f\) 在该 level set 上连续，或直接核对每个收敛子序列的函数值），并且 accumulation point 处有 KL，则 Theorem 5.1 才能合法导入，得到有限长度与收敛。

**范围限制。**

* 对一般非凸 \(f\)，\(P_\lambda(x)\) 可能多值或为空；上面的定理把“全局精确 prox 最小化”作为假设，不能用任意 resolvent 根
  \(x^k-x^{k+1}\in\lambda\partial f(x^{k+1})\) 替代。后者没有全局比较就不供应第 1 项下降。
* 仅有 proper l.s.c. 不自动给 H3；l.s.c. 给的是函数值的 liminf 方向，而 H3 要求沿聚点子列的 limsup 上界。
* convex 情形下 \(P_\lambda\) 单值（在标准存在条件下），但若聚点位于非连续边界，H3 仍需单独检查。非凸情形还必须说明选取的是 global argmin 而非任意临界 prox 根。
* Theorem 5.1 的转移只覆盖 ordinary exact PPA 这一明确对象；RLEB/GPPA 的图关系、物理步、覆盖和真实残差不能由这个映射定理自动补齐。

## 4. 正式出版版本检索状态

已找到 INFORMS 正式页面：<https://pubsonline.informs.org/doi/10.1287/moor.2024.0570>，DOI '10.1287/moor.2024.0570'，页面标注 Received 2024-06-19、Accepted 2026-03-02、Published Online 2026-04-07，并感谢两位审稿人。正式摘要的可见措辞将 v1 的 “over-parameterized compressed sensing model” 改为 “Hadamard reparameterized compressed sensing model”，并新增/更新资助信息（包括 DP250101112）。这些是**已见的元数据/摘要差异**，不是定理差异。

目前不能从该页面的 cookieAbsent/PDF 下载入口取得可搜索的正式全文（共享目录中的 'mor/official.pdf' 实为 HTML cookieAbsent 页面，不是 PDF；不能据此比较 Definition 3.1、Theorem 4.3/4.4、Theorem 5.1/5.2 或 Remark 5.3 的正式编号/措辞）。因此正式版对 KL 证明、H1'、H2、H3、(5.1) 及 Remark 5.3 率式的逐字变化状态记为 **unknown**，不把 v1 结论升级为“已核正式版”。后续若取得正式 PDF，应优先 diff 第 3–5 节及 Section 7 的 KL 推论。

## 5. 当前判断与下一义务

* **可接收的 paper fact：** LMZ 的 KL 有限长度结论严格依赖 (H1')、(H2)、(H3)、有界 level set、accumulation point 与 (5.1)；KL 只提供把下降量转成递推的正则性桥。
* **可接收的 PPA transfer：** 全局 exact proximal minimizer 逐步供应 H1'/H2 与 (5.1) 的普通参数；还须补 H3、level boundedness、prox 解存在性与非凸多值选取。
* **objection：** KL-only 反例排除“只凭 KL 得到 finite length”的说法；Remark 5.3 通用子线性尾率中的 \(1-\alpha\) 与前面 \(\xi\) 递推不相容，暂记疑似笔误；正式出版版定理级差异仍未知。
