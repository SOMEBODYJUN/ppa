# 完整反馈的人工非可定义 KL 能量：禁止扩大理论排除范围

本页固定 **C262-v1**，状态 `derived-checked`；两位独立读者核limiting次梯度、KL和全部输出。本例是**比较范围的正面反证**，不是新的自然应用候选。它使用[C260](orthogonal_feedback_rleb.md#ofr-large-window)已经证明的全部纤维距离/真EB几何，构造一个共同非可定义能量，使同一完整算法能导入ABS。故[C261-v3](smooth_kl_full_relation_obstruction.md#sko-nonsmooth)只分离强链式/可定义单状态合同，不能写成整个ABS不可分析。

<a id="akb-object"></a>
## 对象与稠密微区间

保持C260-v2完整F、S、λ1、U及R=10⁻⁴，全部允许关系仍是完整J_F。每个合法转移w→y的d=d(w,S)>0、d₊=d(y,S)与步长s满足
\[
d_+<.501d,\quad s^2<.501d,\quad d_+\le1.1r_F(y)^2\le1.1s^2.
\tag{AK1}
\]
d0时完整吸收。最近零分量在此管内是M₀=M×0，dS的唯一最近phase点及光滑正距离公式已明确认证。

枚举(0,R)的全部有理数r_j，j≥1；令
\[
\epsilon_j=2^{-j-6}r_j,\quad I_j=(r_j-\epsilon_j,r_j+\epsilon_j)\cap(0,R),
\quad\Omega=\bigcup_jI_j.
\]
Ω稠密开。若I_j交(0,t)，r_j<(4/3)t，因而|I_j|<(1/24)2^{-j}t。求和给
\[
|\Omega\cap(0,t)|\le t/24\quad(0<t\le R).
\tag{AK2}
\]
对t≥0定义
\[
a(t)=\begin{cases}\sqrt t,&t\in\Omega,\\1,&t\notin\Omega,\end{cases}
\quad\varphi(t)=\int_0^ta(s)\,ds,\qquad E(x)=\varphi(d(x,S)).
\tag{AK3}
\]
Ω在(0,R)且R<1，所以φ全域单调、1-Lipschitz，E全域有限连续、非负、1-Lipschitz，零集恰S。AK2给23t/24≤φ(t)≤t（0≤t≤R）。它没有可定义性。

<a id="akb-subgradient"></a>
## limiting 次梯度的最小范数

对0<t<R，a(s)≥√s、a(s)≤1。Fréchet次梯度v的负向增量检验给v≥√t，正向增量给v≤1。连续取极限，∂φ(t)⊂[√t,1]。Ω内φ光滑且φ′=√t；稠密性给√t∈∂φ(t)。这里不宣称整个区间都是limiting次微分。

在phase管d>0处，d(x,S)光滑且n(x)=∇d范数1。沿光滑等距离层的正负切向曲线测试，E的Fréchet次梯度必须沿n；沿最近点normal射线的双向增量测试，法向系数属于[√d,1]。limiting取极限仍满足这个包含。

反过来，沿内向最近点射线取距离层t_k∈Ω趋d，该射线上距离恰t_k（由最近点上界与距离1-Lipschitz下界共同给出），n连续；对应光滑梯度√t_kn(x)趋√dn(x)。故
\[
\partial E(x)\subset[\sqrt d,1]n(x),\qquad
\sqrt d\,n(x)\in\partial E(x),\qquad
\operatorname{dist}(0,\partial E(x))=\sqrt d.
\tag{AK4}
\]
d0处E达到全域最小值，0为Fréchet次梯度。端点d=R亦由内向Ω序列及两向下界成立；实际非零输出d₊<R，H2不依赖端点扩张。

<a id="akb-theorem"></a>
## 同一完整算法的 ABS-H1/H2/H3 与 KL

AK1–3对每个非零合法输入及全部输出给
\[
E(w)-E(y)>(23/24-.501)d>.9s^2.
\tag{AK5}
\]
零输入为等式，所以H1共同α=.9。AK4给实际输出处一个limiting次梯度v_y，
\[
\|v_y\|=\sqrt{d_+}\le\sqrt{1.1}\,s.
\tag{AK6}
\]
因此H2共同β=√1.1；用了原关系真EB以及实际图值对inf的上界，没有把它们等同。

对任意phase零点的充分小邻域，0<E(x)<φ(R)意味着0<d<R，且E(x)≤d。AK4遂给dist(0,∂E(x))≥√E(x)。凹去奇异函数ψ_KL(t)=2√t满足ψ′_KL(E)dist(0,∂E)≥1，所以E在这些零点具有KL指数1/2。

完整几何AK1先给所有有限前缀留管和d_k≤.501^kd₀。位置靠紧圆、动量有界，故任意完整轨道有子序列聚于M₀；E连续且E(x_k)→0，供应ABS-H3。全域E为proper lsc且有下界，H1/H2沿每条完整轨道成立，cluster处KL/H3已核，因此ABS作者稿Theorem2.9确实给这些轨道有限长度和点收敛。该导入依赖本轮先获得的全输出几何，不是旧文已经供应这个模型的证明。

<a id="akb-scope"></a>
## 不与 C261 矛盾及研究价值

沿normal射线，φ在Ω补集的正测集上导数1，但每个正距离处都有limiting次梯度√t。R<1使两者不同，故E不满足强链式法则；由既有分层链式定理，它也不可定义、不能具有该Whitney图分层。它不反驳C261-v3的任何前件。

它确实反驳“同一完整反馈算法没有任何局部Lipschitz KL能量可供ABS”或“RLEB在此算法排除整个ABS”的表述。自然机械能仍有本轮新几何支持的非二次收缩。允许任意人工能量时的全理论严格分离没有闭合；推荐价值须限定为自然/可定义单状态合同无法逐输出认证，而RLEB直接用同锚真残差处理全反馈/完整根。

[独立双审与较弱非KL平台边界](../../发表成果整理/非光滑能量合同独立接收.md)保留全过程；[旧ABS合同](../LITERATURE.md#lit-smooth-kl-obstruction)和[链式接口](../LITERATURE.md#lit-stratified-chain-rule)的论文事实与本轮构造严格区分。Python只检查AK2/AK5系数，不证明稠密性、limiting全称、KL或无限轨道。
