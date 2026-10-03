# 不一致随机近端：条件分布残差与逐分支零集障碍

版本：RP-v1，2026-10-01。身份：从历史来源重新推导的规范模块。
本页给出有限维模型的完整证明，不主张新颖性；外部文献比较尚未在本轮复核。
所有收敛结论均针对概率律。样本路径持续受到随机扰动，不能据此声称路径收敛。

<a id="rp-object"></a>
## RP-OBJECT · 对象、空间与固定量词

固定有限维实欧氏空间 \(H\)、整数 \(m\ge1\)、\(\lambda>0\)，以及对每个 \(i=1,\ldots,m\) 的
\(H_i=H_i^*\succeq0\)、\(b_i\in\operatorname{range}H_i\)、\(p_i>0\)，其中 \(\sum_i p_i=1\)。定义

\[
f_i(z)=\tfrac12\langle z,H_i z\rangle-\langle b_i,z\rangle,
\quad T_i=\operatorname{prox}_{\lambda f_i}=A_i z+c_i,
\quad A_i=(I+\lambda H_i)^{-1},\quad c_i=\lambda A_i b_i.
\]

不要求各函数有共同极小点，不要求矩阵可交换。每一步选取独立于当前状态、服从同一 \((p_i)\) 的新索引。
令 \(U=\cap_i\ker H_i\)、\(V=U^\perp\)，以下假设 \(V\ne\{0\}\)。
每个 \(A_i\) 保持这个分解，在 \(U\) 上是恒等，且 \(c_i\in V\)。
因此 \(T_i(u,x)=(u,A_i|_Vx+c_i)\)。令 \(K\) 为 \(V\) 上的混合转移核，\(P\) 为 \(H=U\oplus V\) 上保持 \(u\) 的核。

固定 \(\nu\in\mathscr P_2(U)\)。\(\mathscr M_\nu\) 是 \(H\) 上所有具有 \(U\) 边缘 \(\nu\) 的有限二阶矩概率律。
其条件分解写为 \(\mu(du,dx)=\nu(du)\mu_u(dx)\)，并定义

\[
\mathsf W_\nu(\mu,\eta)^2=\int W_2(\mu_u,\eta_u)^2\,d\nu(u),
\qquad \mathcal R_\nu(\mu)=\mathsf W_\nu(\mu,\mu P).
\]

条件分解只需几乎处处指定；积分不依赖其零测集版本。这个距离只允许守恒坐标相等的耦合。
它与普通联合 \(W_2\)、同步位移缺陷 \(\Psi\)、物理步长二阶矩是不同对象。

<a id="rp-gap"></a>
## RP-GAP · 从原生矩阵得到严格间隙

在 \(V\) 上定义

\[
B=\sum_i p_i A_i^*A_i|_V,\qquad c=\sqrt{\lambda_{\max}(B)}.
\]

**结论：**\(0<c<1\)，且对所有 \(x,y\in V\)，
\(\sum_i p_i\|T_i x-T_i y\|^2\le c^2\|x-y\|^2\)。

**证明。** \(A_i\) 的特征值在 \((0,1]\)，且 \(\|A_iv\|=\|v\|\) 当且仅当 \(H_iv=0\)。
若单位 \(v\in V\) 使 \(\langle v,Bv\rangle=1\)，各非负缺口因 \(p_i>0\) 都为零，故 \(v\in U\cap V=\{0\}\)，矛盾。
有限维单位球的紧性使逐方向严格性成为统一严格间隙。仿射常数在差中消去，得所需估计。∎

**边界。** 若 \(V=\{0\}\)，全核为恒等，所有律均不变，应单独处理；不能套用 \(1/(1-c)\)。
无限维时紧性步骤失效，不能把有限维定理直接推广。

<a id="rp-contraction"></a>
## RP-CONTRACTION · 唯一活跃不变律、全部联合不变律

**精确结论。** 存在唯一 \(\pi\in\mathscr P_2(V)\) 满足 \(\pi K=\pi\)。
全部联合有限二阶矩不变律恰为
\(\mathcal I_2=\{\nu\otimes\pi:\nu\in\mathscr P_2(U)\}\)。
对每个固定 \(\nu\) 和任意 \(\mu,\eta\in\mathscr M_\nu\)，

\[
\mathsf W_\nu(\mu P,\eta P)\le c\mathsf W_\nu(\mu,\eta).
\]

**证明。** 给定活跃律的任一最优耦合，同步使用同一个独立索引。
RP-GAP 使输出耦合成本至多输入成本的 \(c^2\) 倍，故
\(W_2(\alpha K,\beta K)\le cW_2(\alpha,\beta)\)。
有限多个仿射映射保持有限二阶矩；\(\mathscr P_2(V)\) 完备，Banach 不动点定理给 \(\pi\)。
逐纤维应用上述估计再积分得条件收缩。
若 \(\mu P=\mu\)，守恒边缘相同且分解唯一，故 \(\mu_u K=\mu_u\) 对 \(\nu\) 几乎处处成立；条件二阶矩几乎处处有限，活跃唯一性给 \(\mu_u=\pi\)。反向直接代入。∎

<a id="rp-eb"></a>
## RP-EB · 真实条件 law-step 残差的误差界

记 \(\pi_\nu=\nu\otimes\pi\)、\(E_\nu(\mu)=\mathsf W_\nu(\mu,\pi_\nu)\)。
对全部 \(\mu\in\mathscr M_\nu\) 和整数 \(k\ge0\)，

\[
(1-c)E_\nu(\mu)\le\mathcal R_\nu(\mu)\le(1+c)E_\nu(\mu),
\]
\[
E_\nu(\mu P^k)\le c^k E_\nu(\mu),\qquad
\mathcal R_\nu(\mu P^k)\le c^k\mathcal R_\nu(\mu),
\]
\[
\sum_{k\ge0}\mathsf W_\nu(\mu P^{k+1},\mu P^k)
\le\frac{\mathcal R_\nu(\mu)}{1-c}.
\]

**证明。** 三角不等式给 \(E\le\mathcal R+cE\) 与 \(\mathcal R\le E+cE\)。
收缩分别用于 \((\mu,\pi_\nu)\) 和 \((\mu,\mu P)\)，迭代并求几何级数即得。∎
特别 \(\mathcal R_\nu=0\iff\mu=\pi_\nu\)。
普通联合运输只得到充分界
\(d_{W_2}(\mu,\mathcal I_2)\le W_2(\mu,\pi_\nu)\le E_\nu(\mu)\le\mathcal R_\nu(\mu)/(1-c)\)。
这个不等式不传递条件距离下的必要性、最优常数或以普通距离为分母的相对收敛率。

<a id="rp-branch"></a>
## RP-BRANCH · 逐分支残差不识别混合平稳性

**独立命题。** 固定有限个 firmly nonexpansive 映射 \(S_i:H\to H\)，每个有不动点，权重 \(p_i>0\)。对任意 \(\mu\in\mathscr P_2(H)\)，

\[
\sum_i p_i W_2(\mu,(S_i)_\#\mu)^2=0
\iff \mu\left(\bigcap_i\operatorname{Fix}S_i\right)=1.
\]

**证明。** 零和意味着每个推前律都等于 \(\mu\)。固定 \(z_i\in\operatorname{Fix}S_i\)，firm nonexpansiveness 给
\(\|S_ix-z_i\|^2+\|x-S_ix\|^2\le\|x-z_i\|^2\)。
积分后首项与右边因律不变而抵消，故 \(S_ix=x\) 几乎处处。有限交保持全测度。反向显然。∎

因此不一致二次近端模型若共同不动点为空，上式残差在每一个有限二阶矩律上都严格正，包含真正的混合不变律。
零集检验应先于任何 EB 或速率论证。这个结论针对指定的分组；将所有分支合成整个核后的 law-step 残差是另一残差。

<a id="rp-scalar"></a>
## RP-SCALAR · 尖锐例与持续物理运动

取 \(0<a<1\)，活跃维数为一，\(T_\pm x=ax\pm(1-a)\)，两支概率各半。
它们分别是 \(f_\pm(x)=(1-a)(x\mp1)^2/(2\lambda a)\) 的近端映射。
活跃不变律为
\(\pi_a=\mathcal L((1-a)\sum_{j\ge0}a^j\varepsilon_j)\)，其中独立 \(\varepsilon_j=\pm1\) 各半。
级数绝对收敛；剥去首项验证平稳性，且 \(\operatorname{Var}(\pi_a)=(1-a)/(1+a)\)。

对任意 \(h\in L^2(\nu)\)，设 \(\mu_u=(\mathrm{Id}+h(u))_\#\pi_a\)。
平移律之间的 \(W_2\) 恰等于平移长度：平移耦合给上界、均值差给下界。因此

\[
E_\nu(\mu)=\|h\|_{L^2(\nu)},\quad
\mathcal R_\nu(\mu)=(1-a)\|h\|_{L^2(\nu)},\quad
E_\nu(\mu P^k)=a^k\|h\|_{L^2(\nu)}.
\]

所以此模型的最佳 EB 系数为 \(1/(1-a)\)，最佳相对收缩因子为 \(a^k\)。
缩小非零 \(h\) 同时证明任意完整条件距离邻域内的尖锐性。
另一方面，在平稳状态且新噪声独立时，

\[
\mathbb E|X-T_\varepsilon X|^2
=(1-a)^2(\operatorname{Var}(X)+1)
=\frac{2(1-a)^2}{1+a}>0,
\qquad W_2(\pi_a,\pi_a K)=0.
\]

这给物理步长不能直接充当不变律残差的明确反例。

## RP-DEPENDENCIES · 可机读关系应保存的逻辑

| 稳定身份 | 合取输入 | 输出 | 限制 |
|---|---|---|---|
| RP-GAP | 有限维、有限正权重、二次近端、剔除共同核 | 活跃均方严格收缩 | 无共同极小点要求；无限维须另证间隙 |
| RP-CONTRACTION | RP-GAP、仿射有限二阶矩、固定守恒分解 | 唯一活跃律与全部联合不变律 | 只分类有限二阶矩律 |
| RP-EB | RP-CONTRACTION、固定同一边缘、真实条件 law-step | 全局线性 EB 与律空间有限长度 | 不替换成同步缺陷或物理步长 |
| RP-BRANCH | 每支 firmly nonexpansive、有固定点、有限二阶矩、正权重 | 分支残差零集等于共同固定点支持律 | 不是混合核不变律的一般表示 |
| RP-SCALAR | 标量双近端模型、条件平移 | EB 与速率尖锐；物理步长反例 | 一般矩阵常数未宣称锐 |

与 [既有 Markov 模块](../cone_markov.md) 的接口：RP-EB 在固定边缘上使用其自身的条件 \(W_2\) 距离；C129 的固定边缘二进制距离 \(\mathsf W_\nu\) 与 C130 的 Gaussian \(W_{2,Q}\) 各自定义，不能仅因都按条件律计算而视为同一度量。RP-EB 的残差是整个混合核的 law-step；条件刷新残差与同步 \(\Psi\) 也不可静默替换。
与确定性 [RLEB–PPA](../rleb_ppa.md) 暂无已证超边：还缺原生图几何、真实残差和耦合之间的桥。

## RP-SOURCE · 来源、复核与后续增长

- 原始推导：[历史报告](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/04_相关性与随机表示/相关性感知_随机近端正类与分支缺陷障碍.md)，§2、Theorem A、§4、Proposition B。
- 计算证据：[历史验证器](../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/03_随机与Markov理论/06_验证程序/验证_随机近端相关性与常数.py)。包含浮点矩阵检查及有理数标量恒等式；有限计算不代替本页证明。
- 本轮执行：2026-10-01 在当前 Python 环境运行上述历史验证器，退出码 0；矩阵谱、1000 个有限配对检查、标量有理数恒等式均 PASS。这不验证一般测度论结论。
- 本轮复核：重新推导谱间隙、同步耦合、分解唯一性、双边 EB、分支支撑结论、平移尖锐性和物理步长公式。未沿用原稿的“GO/KILL”作为数学状态。
- 证据状态：本页推导已独立重算；外部优先权和历史报告引用的 HLS 精确包含关系未本轮核验，不作原创断言。
- 开放义务 RP-O1：参数随守恒坐标变化、严格收缩常数趋于 1 时，重新给可积性与最优一般模；禁止套现有统一常数。
- 开放义务 RP-O2：寻找确实需要非线性 RL 的正向模型并给原生耦合桥；本有限二次模型已有线性谱隙，不构成该目标的解决。
- 版本规则：改变状态空间、噪声独立性、分支权重、残差或目标集时新增版本，并重新验零集；保留 RP-v1 作为反例和基准。
