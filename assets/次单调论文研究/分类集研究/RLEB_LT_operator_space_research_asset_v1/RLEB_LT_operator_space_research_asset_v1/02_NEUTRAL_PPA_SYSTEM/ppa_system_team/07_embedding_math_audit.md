# 第二轮专项数学审核：证书嵌入、gauge 规范化与 F_sigma 编码

日期：2026-09-20。被审稿：03_certificate_embeddings.md，重点为 §5.2、§6、§7，以及随后提出的 energy running-maximum 逆 gauge 候选。审核方式：从完整纤维与标量不等式重新推导，未以数值测试代替证明。

## 0. 总判定

**PASS，附明确接口边界。**

通过的结论：

1. LT2025 公共 all-pairs＋线性 EB 的严格收敛证书，可转换到原 RLEB-energy；在固定共同自映射图卡内无需修改存在量词。
2. direct-RLEB 在实际调用的残差预算上的 canonical gauge 规范化成立，并保留原严格常数 \(\kappa\)。
3. 在固定 \(\lambda,K,S,R\) 的标准完整紧图卡内，direct 可认证对象类为 \(F_\sigma\)；加强到全轨道拓扑后仍为相对 \(F_\sigma\)。
4. energy 新候选成立：允许把原 \(q<1\) 增大为另一个 \(q'<1\)，全部普通连续严格增 gauge 的 energy 可认证对象，都可改用有限参数的 running-maximum 逆 gauge。因此同一标准图卡内，全部这类 energy 可认证对象亦为 \(F_\sigma\)。

没有证明第一纲、稠密、余稀或理论总体优越性；\(F_\sigma\) 是可测结构结论，不是大小结论。也未核准把上述结论扩展到任意原图、可变局部域或存在任意步长的无标签原算子类。

## 1. 必须固定的精确接口

设 \(K\subset\mathbb R^d\) 非空紧，\(\varnothing\ne S\subset K\) 闭，固定
\(\lambda>0,R>0\)，且 \(R\ge\sup_{x\in K}d(x,S)\)。取
\(T\in C(K,K)\)、\(T|_S=I\)，源算子确为

\[
F_{T,K}(y)=
\left\{\frac{x-y}{\lambda}:x\in K,\ Tx=y\right\}.
\tag{1.1}
\]

于是每个 \(y\in T(K)\) 的纤维非空紧，真正的最小残差为

\[
r_F(y)=\frac1\lambda\min_{x\in K:\,Tx=y}\|x-y\|.
\tag{1.2}
\]

all-pairs RL 写成反射映射条件

\[
\|R_Tx-R_Tz\|\le L\|x-z\|^\gamma,\qquad R_T=2T-I,
\quad \|x-z\|\le R.
\tag{1.3}
\]

取 \(p\in P_Sx\subset S\)，令
\(d=d(x,S),d^+=d(Tx,S),s=\|x-Tx\|\)。
由于 \(d\le R\)，与 \(p\) 比较合法，并得到

\[
s\le\frac{d+Ld^\gamma}{2},
\tag{1.4}
\]

\[
(d^+)^2+s^2
\le \|Tx-p\|^2+\|x-Tx\|^2
=\frac{\|x-p\|^2+\|R_Tx-p\|^2}{2}
\le A(d),\qquad A(r)=\frac{r^2+L^2r^{2\gamma}}2.
\tag{1.5}
\]

后文所有编码依赖这一完整接口。若原 \(F\) 还含图卡外纤维，(1.2) 未必正确，必须补纤维覆盖；不能仅裁剪原算子后称为同一对象。

## 2. LT → 原 RLEB-energy：通过

设线性真实输出 EB 为 \(d(y,S)\le\rho r_F(y)\)，\(\rho>0\)。
LT 公共 all-pairs 常数给 \(L^2=1+4\tau,\gamma=1\)。
取 \(\psi(t)=\rho t\)，则

\[
V(r)=r^2+\lambda^2[\psi^{-1}(r)]^2
=\left(1+\frac{\lambda^2}{\rho^2}\right)r^2,
\qquad A(r)=(1+2\tau)r^2.
\]

所以 energy 常数可取

\[
q_E=\frac{(1+2\tau)\rho^2}{\rho^2+\lambda^2},
\qquad q_E<1\iff2\tau\rho^2<\lambda^2.
\tag{2.1}
\]

LT 公共严格阈值
\(2\tau(\lambda+\rho)^2<\lambda^2\)
蕴含 (2.1)：\(\tau\ge0\) 时比较平方项，\(\tau<0\) 时 (2.1) 自动成立；反射常数实数的前提为 \(1+4\tau\ge0\)。

结合 (1.5) 和真实 EB 的
\(\lambda^2[\psi^{-1}(d^+)]^2\le s^2\)，得到
\(V(d^+)\le A(d)\le q_EV(d)\)。
这确实是证书转换，不只是数值阈值比较。

边界：

- \(\rho=0\) 表示所有实际输出已在 \(S\)；可把 EB 常数放大为足够小的正 \(\rho'\)，或单列一步终止，不应使用 \((0t)^{-1}\)。
- 固定自映射 \(K\) 内没有离域问题。原局部图块若不是自映射图卡，新长度预算仍须关闭；不能据 (2.1) 宣称保留原先同一个大初值域。
- 只覆盖已明示的 LT 公共 all-pairs 接口，不覆盖所有 pointwise、多值、环域或自适应策略框架。

## 3. Direct canonical gauge：通过，保留原 κ

令

\[
h(r)=\frac{r+Lr^\gamma}{2\lambda},\qquad0\le r\le R.
\]

\(h\) 连续严格增。若原单调 gauge 满足
\(\psi(h(r))\le\kappa r,\ 0<\kappa<1\)，
代入 \(t=h(r)\) 即得

\[
\psi(t)\le\widehat\psi(t):=\kappa h^{-1}(t),
\qquad0\le t\le h(R).
\tag{3.1}
\]

由 (1.4)，每个实际输出 \(y=Tx\) 满足

\[
r_F(y)\le\|x-Tx\|/\lambda
\le h(d(x,S))\le h(R).
\]

故原 EB 可放大为 \(d(y,S)\le\widehat\psi(r_F(y))\)，而
\(\widehat\psi(h(r))=\kappa r\) 精确保留兼容常数。

“无损”只指实际调用输出与该 \(\kappa\)，不是任意更大输出域上的全部旧 EB 数据。

### 3.1 全纤维闭编码

规范 inverse 为
\(\widehat\alpha(a)=h(a/\kappa)\)，定义于 \(0\le a\le\kappa R\)。
真实 EB 等价于

\[
d(Tx,S)\le\kappa R,\qquad
h(d(Tx,S)/\kappa)\le\|x-Tx\|/\lambda
\quad(\forall x\in K).
\tag{3.2}
\]

必要性由 \(r_F(Tx)\le\|x-Tx\|/\lambda\) 得出。
充分性必须对固定输出 \(y\) 的全部 \(x\in T^{-1}(y)\) 取最小值，才得到
\(\widehat\alpha(d(y,S))\le r_F(y)\)。
由于全部纤维确在 \(K\)，这一步合法。乘去 \(\lambda\) 后，正是被审稿 (7.3)。
第一条尺度限制不能遗漏。

## 4. Direct 的 F_sigma 与全轨道拓扑：通过

取紧参数盒

\[
P_j=\{(\gamma,L,\kappa):
1/j\le\gamma\le1,\ 0\le L\le j,\
1/j\le\kappa\le1-1/j\}.
\]

\(T|_S=I\)、固定测试对上的 (1.3)、全部输入上的 (3.2)，在
\(C(K,K)\times P_j\) 中联合闭。
正指数下界避免 \(r=0,\gamma\to0\) 不连续；\(\kappa\) 正下界避免除零。

若 \(T_n\to T\)，取盒内证书参数收敛子序列，再用联合闭性，则 \(T\) 仍有盒内证书。
因此遗忘紧参数后的像 \(C_j\) 闭，而
\(\mathcal R_D=\bigcup_jC_j\) 为 \(F_\sigma\)。

没有将真实指数改成有理指数。原证书若允许 \(\kappa=0\)，可将其放大成任意正的 \(\kappa<1\)。

在全轨道拓扑上仍为相对 \(F_\sigma\)，理由是恒等映射

\[
(\mathcal C_{\rm lu},d_{\rm dyn})
\longrightarrow(C(K,K),\|\cdot\|_\infty)
\]

连续，故每个 \(C_j\cap\mathcal C_{\rm lu}\) 仍闭。此论证不使用任何“连续投影保纲”主张。

## 5. 新 energy running-maximum 规范化：独立证明通过

### 5.1 命题的准确版本

在第 1 节固定完整紧图卡中，原 energy 证书使用普通连续严格增 gauge，
\(\alpha=\psi^{-1}\) 在 \([0,R]\) 有定义，并满足

\[
\alpha(d(y,S))\le r_F(y)\qquad(y\in T(K)),
\tag{5.1}
\]

\[
A(r)\le q\{r^2+\lambda^2\alpha(r)^2\},
\quad0\le r\le R,\quad0<q<1.
\tag{5.2}
\]

定义

\[
g_q(r)=\frac1\lambda
\sqrt{\left[\frac{A(r)}q-r^2\right]_+},
\qquad
u_q(r)=\max_{0\le s\le r}g_q(s).
\tag{5.3}
\]

则可改用有限参数 inverse gauge

\[
\widehat\alpha(r)=u_{q'}(r)+\eta r,\qquad q<q'<1,\quad\eta>0,
\tag{5.4}
\]

或在退化分支先无损令 \(\gamma=1\)，得到同一 \(T\) 的严格 energy 证书。

此结论保持“存在 energy 证书”的成员资格，不承诺保持原 \(q\)、原 gauge、最佳速率或同一个局部化长度预算。

### 5.2 必要 running-max 下界

由 (5.2)，\(\alpha(r)\ge g_q(r)\)。
又因 \(\alpha\) 非降，对每个 \(s\le r\) 有
\(\alpha(r)\ge\alpha(s)\ge g_q(s)\)，故

\[
\alpha(r)\ge u_q(r)\qquad(0\le r\le R).
\tag{5.5}
\]

### 5.3 主分支：0<γ<1、L>0

固定任意 \(q'\in(q,1)\)。有

\[
c_*=\inf_{0<r\le R}
\frac{u_q(r)-u_{q'}(r)}r>0.
\tag{5.6}
\]

证明：

1. 对每个 \(r>0\)，\(u_{q'}(r)>0\)，因为
\[
A(s)/q'-s^2
=\left(\frac1{2q'}-1\right)s^2
+\frac{L^2}{2q'}s^{2\gamma}>0
\]
对足够小 \(s>0\) 成立。取 \(u_{q'}(r)\) 的正最大点 \(s_*\)，则
\(g_q(s_*)>g_{q'}(s_*)=u_{q'}(r)\)，故 \(u_q(r)>u_{q'}(r)\)。

2. 近零时 \(g_q,g_{q'}\) 严格增加，running maximum 等于自身，且
\[
\frac{u_q(r)-u_{q'}(r)}r
\sim\frac{L}{\lambda\sqrt2}
\left(q^{-1/2}-(q')^{-1/2}\right)r^{\gamma-1}
\longrightarrow+\infty.
\]
在远离零的紧区间上，该商连续且严格正，故得到 (5.6)。

选 \(0<\eta\le c_*\)，则

\[
\widehat\alpha(r)=u_{q'}(r)+\eta r
\le u_q(r)\le\alpha(r)
\quad(0\le r\le R).
\tag{5.7}
\]

原真实 EB 因而蕴含新 EB。另一方面 \(\widehat\alpha\ge g_{q'}\)，所以

\[
A(r)\le q'\{r^2+\lambda^2\widehat\alpha(r)^2\}.
\tag{5.8}
\]

\(u_{q'}\) 连续非降，加入 \(\eta r\) 后连续严格增。主分支没有缺口。

### 5.4 线性主分支：γ=1、a=(1+L²)/2>q

此时

\[
u_q(r)=\frac r\lambda\sqrt{[a/q-1]_+}.
\]

对任意 \(q'\in(q,1)\)，有严格正的常数

\[
\frac{u_q(r)-u_{q'}(r)}r
=\frac1\lambda
\left(\sqrt{a/q-1}-\sqrt{[a/q'-1]_+}\right)>0.
\]

因此同样可选正 \(\eta\)，得到 (5.7)–(5.8)。

### 5.5 退化分支：γ=1、a≤q<1

此时不能用正 running-max 间隙，因为两者可能都为零。
必须独立重证真实 EB；候选稿采用的处理正确。

由 \(a<1\) 得 \(L<1\)。令 \(c=(1+L)/2\in[1/2,1)\)。
与最近解比较 (1.3)，以及距离函数的 1-Lipschitz 性，得到

\[
d(Tx,S)\le c\,d(x,S),\qquad
\|x-Tx\|\ge(1-c)d(x,S).
\]

因此

\[
d(Tx,S)\le\frac c{1-c}\|x-Tx\|.
\]

对输出的全部纤维取最小值，得到真正的线性 EB

\[
d(y,S)\le\frac{\lambda c}{1-c}r_F(y).
\tag{5.9}
\]

取 \(q'\in(q,1)\)，因 \(a\le q<q'\)，有 \(u_{q'}=0\)。
令

\[
\eta=\frac{1-c}{\lambda c}>0,\qquad\widehat\alpha(r)=\eta r.
\]

(5.9) 给新 EB，而
\(A(r)=ar^2\le q'r^2\le q'[r^2+\lambda^2\widehat\alpha(r)^2]\)。
这一支的新 inverse gauge 未必小于旧 \(\alpha\)，但由完整算子独立得到，足以保持可认证成员资格。

### 5.6 L=0 与 inverse 定义域

\(L=0\) 时 RL 右端恒零，且 \(A(r)=r^2/2\)，都不依赖 \(\gamma\)。
故可先无损改为 \(\gamma=1\)，再使用两个线性分支。

建议 (5.3)–(5.4) 直接定义于全部 \(r\ge0\)。
\(\eta>0\) 保证 \(\widehat\alpha\) 连续严格增、从零开始且趋于无穷，所以
\(\widehat\psi=\widehat\alpha^{-1}:[0,\infty)\to[0,\infty)\) 完整有定义。
这避免“只在 [0,R] 定义 inverse，却作用于更大真实残差”的尺度漏洞。
需要保留 EB 与兼容的实际输出距离范围仍只到 \(R\)。

## 6. 全部 energy gauge 消去后的 F_sigma：通过

第 5 节表明，标准图卡中存在任意普通连续严格增 gauge 的 energy 证书，等价于存在
\(0<\gamma\le1,L\ge0,0<q<1,\eta>0\)，满足 (1.3) 以及

\[
u_q(d(Tx,S))+\eta d(Tx,S)
\le\frac{\|x-Tx\|}{\lambda}
\qquad(\forall x\in K).
\tag{6.1}
\]

反向也完整：以 \(\alpha=u_q+\eta r\) 定义全域 inverse gauge，
(6.1) 在完整纤维取最小值给真实 EB；\(\alpha\ge g_q\) 给 energy 兼容。

取紧参数盒

\[
Q_j=\{(\gamma,L,q,\eta):
1/j\le\gamma\le1,\ 0\le L\le j,\
1/j\le q\le1-1/j,\ 1/j\le\eta\le j\}.
\tag{6.2}
\]

令 \(s=rt\)，可写

\[
u_q(r)=\frac1\lambda\max_{0\le t\le1}
\sqrt{\left[
\frac{(rt)^2+L^2(rt)^{2\gamma}}{2q}
-(rt)^2
\right]_+}.
\tag{6.3}
\]

被最大化函数在紧参数盒、\(r\in[0,R]\)、\(t\in[0,1]\) 上连续，
故最大值联合连续。于是 (1.3)、(6.1)、\(T|_S=I\) 定义闭证书关系。
紧参数投影闭、可数并为

\[
\boxed{\mathcal R_E\text{ 在标准完整紧图卡内为 }F_\sigma.}
\]

同第 4 节，它在全轨道一致收敛空间及共同结论预算层内仍是相对 \(F_\sigma\)。

每个固定参数盒还给真正的共同尾：
若 \(V(r)=r^2+\lambda^2[u_q(r)+\eta r]^2\)，则由 (1.5)、(6.1)

\[
V(d(T^kx,S))\le q^kV(d(x,S)),\qquad
\|T^{k+1}x-T^kx\|\le q^{(k+1)/2}\sqrt{V(R)}.
\]

盒内 \(q\le1-1/j\)，且 \(V(R)\) 有共同有限上界，所以统一有限长和统一点尾确实成立。这些闭片没有包含不收敛的伪证书。

## 7. 可修补文字、已核范围与仍未解决

可修补文字：

1. 被审稿 §6 末句“energy 一般 gauge 的同样消去，本轮未证明”可升级为本报告第 5–6 节的结论，但须保留完整紧图卡、普通连续严格增 inverse gauge、允许增大 q 三个边界。
2. §7.2 的一般 energy 只得 analytic，可在上述图卡中升级为 \(F_\sigma\)；外层任意证书 bundle 不自动升级。
3. 规范 inverse 宜定义全 \(r\ge0\)，避免残差超出 inverse 定义域。
4. \(L<1\) 退化支必须独立重证全纤维真 EB，不能假用正 running-max 间隙。
5. LT 转换如允许 \(\rho=0\)，需单列或显式要求正 EB 常数。

仍未解决：

- 全局原 \(F\) 的图卡外纤维、可变工作域/解集/步长的共同编码；
- 原 maximality、任意局部 graph block 条件在外层的精确描述复杂度；
- 存在步长/策略投影是否保留 Borel 或 \(F_\sigma\)；
- RLEB/LT 在中立母空间中的稠密性、第一纲或余稀性；
- 规范化引理的文献优先权。本审核只核数学，不主张首创。

## 8. 联动修复：证书投影不能笼统保纲

交叉审计指出 05_stress_test.md 中“连续开放满射足以把任意见证子集的纲结论降到像”的措辞过强，已修正。

准确版本：连续开放满射可用于底层具有 Baire 性质的集合 \(A\) 与其饱和逆像 \(p^{-1}(A)\) 的纲比较。
对任意见证子集 \(C\)，即使 \(p\) 开放，也不能由 \(C\) 第一纲推出 \(p(C)\) 第一纲。
例如 \(p:\mathbb R^2\to\mathbb R,\ p(x,y)=x\)，
\(C=\mathbb R\times\{0\}\) 无处稠密，而其像是整个 \(\mathbb R\)。

Direct/energy 的 \(F_\sigma\) 证明不依赖该错误推论：它们使用联合闭条件与紧参数投影的闭性，因此不受这一修补影响。

