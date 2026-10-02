# 伴随 Volterra：端点方向与酉共轭的来源身份

<a id="av-object"></a>
## 完整对象、逆像和来源

在实 \(H=L^2(0,1)\) 的**整个空间**上取
\[
(V^*x)(t)=\int_t^1x(s)\,ds,\qquad (Uf)(t)=f(1-t). \tag{AV1}
\]
\(U=U^{-1}=U^*\) 是等距映射，逐点换元给 \(V^*=UVU\)。因此
GX-061 与 [GX-060 的完整图](volterra_integration.md#vo-object) 是**同一个
等距不变量例型的两个方向观察**；它不是另一个独立的反例机制。
这个等价在历史同包 `work/c_consistency_audit.md` CCA-M10 单独提出，
而 GX-061 的端点公式来自 `work/c_gx053_065.md` 第 713–764 行。

逐纤维反演仍须明确写出，避免把左端点条件照抄到右端点：
\[
(V^*)^{-1}(y)=
\begin{cases}
\{-y'\},&y\in H^1(0,1),\ y(1)=0,\\
\varnothing,&\text{其它 }y\in H.
\end{cases} \tag{AV2}
\]
导数按弱导数解释，端点是绝对连续代表的迹。于是
\(\operatorname{zer}V^*=\{0\}\)，其值域稠密但非满，
原算子真残差是 \(r_{V^*}(x)=\|V^*x\|\)。
前述等价由 (AV1) 的换元直接核算；来源中“逐方向独立见证”
不等于两个独立的等距不变量样本。

<a id="av-graph"></a>
## C120-v1：完整图几何和残差量词

\[
\langle x,V^*x\rangle=\tfrac12\left(\int_0^1x\right)^2\ge0. \tag{AV3}
\]
全域有界线性单调算子由双侧扰动图点的标准论证得极大单调。
取零均值 \(h(t)=\tfrac12-t\ne0\)，有
\(\langle h,V^*h\rangle=0\)、\(V^*h\ne0\)，否定严格单调、
正强单调和正 cocoercivity 模，也以 \((h,0)\notin\operatorname{gra}V^*\)
否定 paramonotonicity。对 rectangular 的完整图表达式，固定
\(x=0,v=V^*1=1-t,z=\alpha h\)，由于
\(\langle h,v\rangle=1/12\)、\(\langle h,V^*h\rangle=0\)，
\(\langle x-z,v-V^*z\rangle=-\alpha/12\to-\infty\)。
这是方向特定的直接见证，不调用未核的外部等价定理。

令 \(e_n(t)=\sqrt2\cos(n\pi t)\)。完整图上
\[
\|e_n\|=1,\quad (V^*e_n)(t)=-\frac{\sqrt2}{n\pi}\sin(n\pi t),
\quad\|V^*e_n\|=\frac1{n\pi}. \tag{AV4}
\]
对**任意** \(\eta>0\)、非负 \(\psi:[0,\eta)\to[0,\infty)\)
且 \(\lim_{s\downarrow0}\psi(s)=0\)，任意 \(C,\delta>0\)，
固定 \(0<a<\delta\) 后取 \(x=ae_n\)，总有大 \(n\) 使
\(\|x\|>C\psi(\|V^*x\|)\)、\(\|V^*x\|<\eta\)。
这否定**固定零目标、统一局部**的任何消失 gauge 真残差 EB；
不排除逐方向估计。小的 \(y\notin\operatorname{ran}V^*\)
又使完整逆纤维为空，否定邻域内全部目标的两变量 MR。
这些结论也可由 \(U\) 转移 C104，但 (AV2)–(AV4) 核实了右端点方向。

<a id="av-prox"></a>
## C121-v1：完整近端的逐点与统一门

对每个固定 \(\lambda>0\)，齐次方程排除多余纤维，完整 resolvent
在全 \(H\) 上单值，且
\[
(J_{\lambda V^*}p)(t)
=p(t)-\lambda\int_t^1e^{-\lambda(s-t)}p(s)\,ds,
\quad J_{\lambda V^*}=U J_{\lambda V}U,
\quad R_{\lambda V^*}=U R_{\lambda V}U. \tag{AV5}
\]
因此同参数全部图点对的线性反射 RL 锐常数为 1；取等发生在
**零均值图点差**，不是任意零均值 Minty 输入差。在无界完整图上
任何 \(0<\gamma<1\) 的全图有限 Hölder 常数都被缩放否定。

酉共轭逐次保持范数和极限。依照
[C105 的能量、高频和稠密值域证明](volterra_integration.md#vo-prox)，
对每个整数 \(k\ge1\)，\(\|J_{\lambda V^*}^k\|=1\)；
每个非零输入单步严格缩短范数，而每个固定初值
\(J_{\lambda V^*}^kp\to0\) 强收敛。这里的后一个结论以固定
\(p\) 后令 \(k\to\infty\)，不提供单位球上的统一速率或每轨道有限长度。
同样 \(\|(I-J_{\lambda V^*})(ae_n)\|
\le\lambda a/(n\pi)\)，所以**近端输入步残差**的任意统一局部
消失 gauge EB 也失败。它与上一节原算子输出真残差是不同量。

本页只关闭明确列出的完整图、逆纤维、残差及近端观察；来源中
其它性质标签、外部 BWY 归属和历史先行性仍需分别核对。
