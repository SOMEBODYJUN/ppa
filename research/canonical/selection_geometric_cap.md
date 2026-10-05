# 几何尾的完整二支 cap 图：独立对象卡

<a id="gc-object"></a>
## 对象、全部图值与完整近端

取 \(E=\mathbb R^3\) 的 Euclidean 范数、\(\lambda=1\)。对 \(y\ge0\) 置
\[
D_y(\eta)=\min\left\{2\sqrt y,\,
\frac{\sqrt{1+4\eta_+}-1}{2}\right\},\qquad
\eta_+=\max\{\eta,0\}.
\]
定义完整关系
\[
F(\xi,\eta,y)=
\begin{cases}
\{(-2\sqrt y,-D_y(\eta),3y),\,
  (-2\sqrt y,-D_y(\eta),-5y)\},&y\ge0,\\
\varnothing,&y<0.
\end{cases}                                                   \tag{GC-1}
\]
两个连续半代数分支定义在闭半空间上，故完整图闭且半代数；
\(y>0\) 时有两个不同值，\(y=0\) 时二者重合。
完整零集恰为 \(S=\mathbb R^2\times\{0\}\)。

对任意输入 \(x=(z,p,r)\)，完整 \(J_F(x)\) **只有一个**元素：
\[
T(z,p,r)=\left(z+\sqrt{|r|},\,
p+\sqrt{\min\{p_+,|r|\}},\,|r|/4\right).                       \tag{GC-2}
\]
确证全部纤维：写输出 \(u=(\xi,\eta,y)\)，两支的第三输入坐标
\(r=y+3y=4y\) 或 \(r=y-5y=-4y\)，故 \(y=|r|/4\)，
\(r\ne0\) 时只容许与符号一致的一支；第一坐标给
\(\xi=z+\sqrt{|r|}\)。令 \(a=|r|\)。第二坐标必须满足
\(p=\eta-\min\{\sqrt a,(\sqrt{1+4\eta_+}-1)/2\}\)。
此函数在 \(\eta\le0\) 是 \(\eta\)，在
\(0\le\eta\le a+\sqrt a\) 以 \(\eta=v^2+v\) 表示为 \(v^2\)
（\(0\le v\le\sqrt a\)），在 \(\eta\ge a+\sqrt a\) 是
\(\eta-\sqrt a\)。它连续、严格递增且像为整个实线，唯一逆为
\(\eta=p+\sqrt{\min\{p_+,a\}}\)；\(a=0\) 时也成立。
因而负输入、cap 接缝和合并分支处都没有遗漏的 proximal 输出。

<a id="gc-certificates"></a>
## 全对图模、真实残差与固定兼容半径

记 \(C=2T-I\)。对每个 \(R>0\) 和全部
\(\|x-x'\|=\delta\le R\)，有
\[
\|Cx-Cx'\|\le L_R\sqrt\delta,\qquad
L_R=2\sqrt2+\tfrac32\sqrt R.                                  \tag{GC-3}
\]
因为 \(C\) 的前两坐标为 \(z+2\sqrt{|r|}\) 和
\(p+2\sqrt{\min\{p_+,|r|\}}\)，两项根号的差各不超过
\(\sqrt\delta\)；第三坐标为 \(|r|/2-r\)，其全实线 Lipschitz
常数为 \(3/2\)。因此线性部分范数至多 \(3\delta/2\)，
根号部分至多 \(2\sqrt2\sqrt\delta\)。完整 \(M_+=I+F\)
的每个图点输入都由 (GC-2) 唯一反演，故 (GC-3) 正是完整图
在**输入对尺度** \(R\) 的全对
\(\mathrm{RL}(1,1/2,L_R;R)\)，包含异号输入的跨支比较。
这不声称 \(L_R\) 对每个固定正 \(R\) 最优。
特别地，由 \(T=(I+C)/2\)，对同一完整 \(T\) 的任意
\(\|x-x'\|=\delta\le R\) 有
\[
\|Tx-Tx'\|\le H_R\sqrt\delta,\qquad
H_R=\tfrac12(\sqrt R+L_R).                                    \tag{GC-3a}
\]
这是下文调用 SS-T1 的单步前提；它对每个固定 \(R>0\) 成立，
不要求 (GC-5) 的严格兼容半径或 (GC-4) 的真残差界。

取 \(x_t=(0,t,t),x'_t=(0,t,0)\)。则
\(\|x_t-x'_t\|=t\) 而
\(\|Cx_t-Cx'_t\|^2=8t+t^2/4\)。
因此零点附近任何大于 \(1/2\) 的指数均失败；
\(R\downarrow0\) 时最优半阶常数至少 \(2\sqrt2\)，
与 (GC-3) 的上界极限一致。

对 \(u=(\xi,\eta,y)\in\operatorname{dom}F\)，两支平方范数
分别是 \(4y+D_y(\eta)^2+9y^2\) 与
\(4y+D_y(\eta)^2+25y^2\)，故**完整最小残差**
\[
r_F(u)^2=4y+D_y(\eta)^2+9y^2\ge4y,\qquad
d(u,S)=y\le\tfrac14r_F(u)^2.                                  \tag{GC-4}
\]
在 \(\eta\le0,y\downarrow0\) 的输出序列，系数 \(1/4\)
渐近取到；负输入所选的是范数较大的另一支也不改变真残差。

令 \(\psi(t)=t^2/4\) 定义在 \([0,\bar t]\)，选择一个固定
\[
0<R<\left[\frac{2(4-2\sqrt2)}5\right]^2,\qquad
\bar t\ge (R+L_R\sqrt R)/2.                                    \tag{GC-5}
\]
同一完整图取 \(U=\mathbb R^3\)，
\(U_R=\{x:d(x,S)\le R\}\)。它在所有输入上 coverage，
每个最近零点 \((z,p,0)\) 的零图点属于此图。
对 \(d\le R\) 的锚比较既在尺度 \(R\) 内，也使所选图值范数
不超过 \((R+L_R\sqrt R)/2\le\bar t\)，所以 gauge 求值有定义。
代入 R02 的**直接**兼容测试得到
\[
\sup_{0<t\le R}\frac{\psi((t+L_R\sqrt t)/2)}t
=\frac{(\sqrt R+L_R)^2}{16}
=:\kappa_R<1.                                                  \tag{GC-6}
\]
最后一个严格不等式等价于 (GC-5) 的 \(R\) 上界；
任意正 \(R\) 的 (GC-3)/(GC-4) 并不自动给严格兼容。
此完整图的 \(J_F=T\) 全局单值，所以图块/完整纤维门在此例
确实闭合；留域可取整个 \(E\)。从而 C02-v2 直接适用该固定半径，
而不是把孤立的全对模与另一个模型的 EB 拼接。

<a id="gc-tail"></a>
## 逐初值法向率和全输入 collar 的共同几何尾

设 \(a_0=|r_0|\)。由 (GC-2)，
\[
r_k=a_0\,4^{-k}\ (k\ge1),\quad
z_k=z_0+2\sqrt{a_0}(1-2^{-k}),\quad
0\le p_{k+1}-p_k\le\sqrt{a_0}\,2^{-k}.                         \tag{GC-7}
\]
这里 \(r_0\) 可以为负；\(r_k\) 从第一步起非负。
每个初值的 \(p_k\) 因而收敛，极限
\(\Pi(x)\in S\)，且对**全部** \(x\) 及 \(k\ge0\)
\[
\|T^kx-\Pi(x)\|
\le 2\sqrt2\sqrt{a_0}\,2^{-k}+a_0\,4^{-k}.                    \tag{GC-8}
\]
切向两坐标的尾范数由每步 \(\sqrt2\sqrt{a_j}\) 求和；
法向至极限的距离是 \(a_k\)（\(k=0\) 时也是 \(|r_0|\)）。
故对共同输入 collar \(\{|r_0|\le R\}\) 可取
\(M=2\sqrt2\sqrt R+R,\ \sigma=1/2\)，并由
同一完整映射的 (GC-3a) 在全部比较轨道上提供 SS-T1 的
\(H_R,R,\gamma=1/2\)；再以共同点尾调用
SS-TRANSFER，获得同一极限映射的共同两点对数模，
其中几何尾的可用指数是 \(\beta=1\)。
直接距离率是 \(d(Tx,S)=d(x,S)/4\)，与证书
\(\kappa_R\to1/2\) 及其保守尾指数
\(\log(1/\kappa_R)/(2\log2)\to1/2\) 是不同层的量。
本页只证明上界；[C138 的同一完整图配对下界](selection_geometric_sharpness.md#gs-sharp)
另行证明此对数–对数阶在所显示的固定初值族不可改进。

**来源与边界。** 来源定位 SS1 修订包的
`research_note.md` §2 定理 2（181–293 行）。
本页从完整图重新计算；§3 的独立重构在 [C138](selection_geometric_sharpness.md#gs-sharp)，
并不借审计 PASS 升格任意参数族或文献优先权。不要把这里的几何尾模型与
[不同二次尾模型](solution_selection_rates.md#ss-quadratic-object)
合并；两者的 \(F,T\)、法向率和最小真残差不同。
