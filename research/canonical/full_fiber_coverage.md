# 全域与固定窗口：定位全部逆纤维的锐覆盖半径

<a id="fc-object"></a>
## FC-OBJECT · 固定参数、完整图与相对极大

固定 \(n\ge1\)、\(\lambda,L>0\)、\(0<\gamma<1\)，
令 \(R=L^{1/(1-\gamma)}\)。本页 RL 始终要求同一图内的**每对**
\((x,v),(y,w)\) 在全部输入对尺度上满足
\[
\|(x-y)-\lambda(v-w)\|
\le L\|(x-y)+\lambda(v-w)\|^\gamma. \tag{FC1}
\]
graph-maximal 是在这些固定参数下不能再添加兼容图点，
不是极大单调。

对全局情形，取 \(\mathbb R^n\) 上非空完整 graph-maximal 关系 \(F\)，
并取任意图锚 \((x_0,v_0)\)。对固定窗情形，另取任意集合
\(U,W\subseteq\mathbb R^n\)，非空图 \(G\subset U\times W\) 满足 (FC1)
且不能在这个**同一窗口**内严格兼容扩张；这称相对 graph-maximal。
窗口不自动带来开域或覆盖，以下会直接列开球包含条件。

本页完整重构 C18 的定位、全局与固定窗覆盖以及统一锐性。
有限观测拓扑证书 C05 是另一套前件，不被本页赋予。

<a id="fc-root"></a>
## FC-ROOT · 最大根、单调性与成对定位

对 \(u\ge R\) 定义 \(g(u)=u-Lu^\gamma\)。
有 \(g(R)=0\)、\(g(u)\to\infty\)，且
\[
g'(u)=1-\gamma Lu^{\gamma-1}\ge1-\gamma>0. \tag{FC2}
\]
对每个 \(t\ge0\)，存在唯一 \(u(t)\ge R\) 使 \(g(u(t))=2t\)。
置 \(\rho(t)=u(t)-t=(u(t)+Lu(t)^\gamma)/2\)，便有
\[
\rho(0)=R,\quad \rho(t)>t,\quad
\rho(t)-t=L(\rho(t)+t)^\gamma. \tag{FC3}
\]
最后一个方程在 \(t>0\) 时只有此非负根：
其任意非负根都满足 \(\rho>t\) 且 \(u=\rho+t>R\)，可用 (FC2)。
在 \(t=0\) 时另有零根，故这里明确选择**最大**根 \(R\)。
\(\rho\) 连续严格增且趋无穷：\(u(t)\) 连续严格增，
\((u+Lu^\gamma)/2\) 对 \(u>0\) 严格增。
所以其值域为 \([R,\infty)\)。

令 \(s=\|x-x_0\|\)、\(t=\lambda\|v-v_0\|\)。
反三角及普通三角不等式与 (FC1) 给
\[
|s-t|\le L(s+t)^\gamma. \tag{FC4}
\]
若 \(s\le t\)，则 \(s\le\rho(t)\)。若 \(s>t\) 且 \(s+t\le R\)，
亦有 \(s\le R\le\rho(t)\)。余下情形由
\(g(s+t)\le2t=g(u(t))\) 及 (FC2) 得 \(s+t\le u(t)\)。
交换 \(s,t\) 再用同一论证，因此**每个**原图点满足
\[
\|x-x_0\|\le\rho(\lambda\|v-v_0\|),\qquad
\lambda\|v-v_0\|\le\rho(\|x-x_0\|). \tag{FC5}
\]
定位只需全对 RL；原逆纤维的非空性仍须另证。

对每个固定 \(r>R\)，函数
\(h\mapsto r-h-L(r+h)^\gamma\) 在 \([0,r]\) 连续严格减，
在零处为正、在 \(r\) 处为负。因此唯一 \(h(r)\in(0,r)\) 满足
\[
r-h(r)=L(r+h(r))^\gamma,\qquad \rho(h(r))=r. \tag{FC6}
\]

<a id="fc-global"></a>
## FC-GLOBAL · 所有目标及全部纤维的覆盖

所需全值域前件可直接验证。
[同参数扩张与 graph-maximal 门](holder_extension.md#he-extension)
使全局 \(F\) 的 Cayley 映射 \(C\) 定义在全部 \(\mathbb R^n\)，且
\(\|C(p)\|\le\|C(0)\|+L\|p\|^\gamma\)。
给定任意目标 \(v\)，选足够大 \(B>0\) 使
\[
2\lambda\|v\|+\|C(0)\|+LB^\gamma\le B.
\]
则连续映射 \(p\mapsto2\lambda v+C(p)\) 把闭 Euclidean 球
\(\overline B_B(0)\) 映入自己。这里明确导入的基础定理是
**Brouwer 闭球不动点定理**：有限维闭球的连续自映射有不动点。
得到 \(p-C(p)=2\lambda v\)，即完整图中有输出 \(v\) 的点。
这不需要原关系单调，也不把闭球不动点定理扩到任意 Hilbert 球。
完整有限维几何另见 [C04 的证明](finite_fiber_classification.md#ff-coercivity)。

现在给任意 \(v\in B(v_0,h(r)/\lambda)\)。
逆纤维已非空，且由 (FC5) 的**逐图点**界，
其每个成员 \(x\) 都满足
\(\|x-x_0\|\le\rho(\lambda\|v-v_0\|)<\rho(h(r))=r\)。
所以
\[
B(v_0,h(r)/\lambda)\subset F(B(x_0,r)),\qquad
\varnothing\ne F^{-1}(v)\subset B(x_0,r)
\quad(v\in B(v_0,h(r)/\lambda)). \tag{FC7}
\]
这不是仅找到某个近处选择；所有完整逆纤维点均被定位。
用 \(p\mapsto2x-C(p)\) 的同样闭球论证给 \(F(x)\ne\varnothing\)，
交换 (FC5) 两坐标得到对称正向覆盖：
\[
B(x_0,h(\lambda s))\subset F^{-1}(B(v_0,s)),\qquad
F(x)\subset B(v_0,s)
\quad(x\in B(x_0,h(\lambda s)),\ \lambda s>R). \tag{FC8}
\]

<a id="fc-window"></a>
## FC-WINDOW · 一个固定窗口内的完整逆纤维

对 FC-OBJECT 的同一相对极大图 \(G\)，取锚 \((x_0,v_0)\in G\)，
并假设 \(B(x_0,r)\subset U\)、\(B(v_0,s)\subset W\)、
\(r>R\)、\(s>0\)。

HE-EXTENSION 给其部分 Cayley 映射一个同常数全域扩张，
其 pullback 定义全局 graph-maximal 完整关系 \(\widehat F\)。
图 \(\operatorname{gph}\widehat F\cap(U\times W)\) 包含 \(G\)
并满足原固定参数 RL，相对极大性遂给
\[
G=\operatorname{gph}\widehat F\cap(U\times W). \tag{FC9}
\]
对每个 \(v\in B(v_0,\min\{s,h(r)/\lambda\})\)，
(FC7) 把 \(\widehat F^{-1}(v)\) 的全部非空纤维放在
\(B(x_0,r)\subset U\)，且该 \(v\in W\)，故由 (FC9)
这些点全部属于 \(G\)。反向 \(G\) 中的每个逆点也属于
\(\widehat F\)，受同一定位约束。因此
\[
\varnothing\ne G^{-1}(v)=\widehat F^{-1}(v)\subset B(x_0,r).
\tag{FC10}
\]
此纤维身份只对显示的目标球成立，不断言窗口外完整关系身份。
非相对极大的任意子图不由此取得覆盖。

<a id="fc-sharp"></a>
## FC-SHARP · 一维同对象的半径与严格门

固定原来的全部参数，在 \(\mathbb R\) 定义
\(C(p)=L(p_+)^\gamma\)、\(p_+=\max\{p,0\}\)。
对非负 \(a,b\)，
\(|a^\gamma-b^\gamma|\le|a-b|^\gamma\)：
令 d≥0，函数 a↦(a+d)^γ−a^γ 在 a>0 的导数非正，故由零处连续性有 (a+d)^γ−a^γ≤d^γ；这也覆盖 a=0、d=0。
再复合非扩张正部映射，得到全域 \(L\)-Hölder。
全域 pullback 是同固定参数的 graph-maximal 关系，锚为 \((0,0)\)，
\[
x(p)=(p+L(p_+)^\gamma)/2,\qquad
v(p)=(p-L(p_+)^\gamma)/(2\lambda). \tag{FC11}
\]
正输出只可能在 \(p>R\)。在这个区间 \(v'(p)>0\)，
\(v\) 从零增至无穷，故每个正目标有且只有一个逆点；
其输入 \(x(p)>R\)。
若 \(r\le R\)，任意正目标都没有 \((-r,r)\) 中的逆点，
因此不能在该门下统一保证任何正半径的中心输出球。

若 \(r>R\)，取 \(p=r+h(r)>R\)，则
\(Lp^\gamma=r-h(r)\)，所以
\[
x(p)=r,\qquad v(p)=h(r)/\lambda. \tag{FC12}
\]
该正输出的唯一逆点位于开输入球的边界，因而不在开球内。
任何严格大于 \(h(r)/\lambda\) 的中心输出球都会包含这个目标，
故统一半径不能提高。全空间 \(U=W=\mathbb R\) 又是合法固定窗，
同一个见证证明固定窗口类的统一锐性。
不声称某个指定关系或特定小窗口的最佳半径恰等于该统一保证。

<a id="fc-obligations"></a>
## 精确接收范围与来源

本页需要的外部接口只有已明确前件的同常数 Hilbert 扩张，
以及有限维 Brouwer 闭球不动点定理；FC2–FC12 完整给其余证明。
不需要原关系完整近端轨道收敛、真实残差 EB、有限样本网或 C03 的影子。
相对最大图仍使用全尺度成对 RL，不能把仅局部测试半径冒充本页前件。

来源 S23 TeX 的 lem:rho、thm:coverage、thm:window、
prop:coveragesharp，952–1100 行，只用于同身份溯源。
本页以闭球不动点直接证明全值域，不把来源 degree 路线的摘要当证明。
本页不核外部先行性；证明状态须与 C18 总账及本次独立接收范围一致。
