# DD2 的前向输入与图剪切输出误差界

<a id="dd2-dual-transfer"></a>
## 1. 对象、量词和局部转移

设 \(X\) 为实 Hilbert 空间，\(F:X\rightrightarrows X\)，
\[
G=(F^{-1}-I)^{-1},\qquad S=\operatorname{zer}F=\operatorname{zer}G\ne\varnothing .
\]
图恒等式为 \(q\in F(z)\Longleftrightarrow q\in G(z-q)\)。原近端 \(J_{\lambda A}\) 的前向映射为 \(F=I-J_{\lambda A}\)，此时 \(G=\lambda A\)。对每条允许图边 \(q\in F(z)\) 记
\[
w=z-q,\quad z_\alpha=z-\alpha q,\quad
t=d(z,S),\quad a=d(w,S),\quad s=\|q\|,\quad r=d(z_\alpha,S),\qquad \alpha>0 .
\]
取 \(S\) 闭，假设每条允许边都有一个 \(p\in P_S(z)\) 满足
\[
\langle q,z-p\rangle \ge \beta s^2-D(t),\qquad \beta>0 .
\tag{1}
\]
\(D\ge0\)，\(D(0)=0\)。上传稿的条件 \(\langle q,w-p\rangle\ge\Phi(t)\) 蕴含 (1) 的 \(\beta=1,\ D=(-\Phi)_+\) 版本。全部计算可对每条边分别取方向相关的 \(\beta\)。

真正的输入、输出误差界分别为
\[
\mathrm{I}:\quad d(z,S)\le h(r_F(z)),\qquad
\mathrm{O}:\quad d(w,S)\le \psi(r_G(w)),\qquad
r_M(u)=\inf_{v\in M(u)}\|v\|.
\tag{2}
\]
每项各有自己的位置和残差评价窗。空纤维残差约定为 \(+\infty\)。本文用有限值、非降、右连续且在零点取零值的模，可约定模在 \(+\infty\) 时取 \(+\infty\)。在合格的窗中，\(\mathrm I\) 给 \(t\le h(s)\)，\(\mathrm O\) 给 \(a\le\psi(s)\)。反向须对每个完整纤维的每个值成立，方可对 \(\|q\|\) 取下确界。右连续性保证这个步骤，即使残差下确界未达到。若仅假设记录在允许子图中的每条边满足选中值不等式，以下逐边估计照样成立，度量次正则性结论则只在完整纤维经过验证时成立。

例如 \(G(w)=\{w,w^3\}\) 在 \(\mathbb R\) 上给出全域、闭图的 \(F\)。分支 \(q=w,\ z=2w\) 满足 \(t=2s,\ a=s\)。另一支 \(z=w+w^3\) 有 \(s=|w|^3=o(|z|)\)，且 \(r_G(w)=|w|^3\) 对 \(|w|<1\) 成立。因此选中值线性界并未给出两个完整纤维中的任何线性界。两支都满足 (1) 的 \(\beta=1,\ D=0\)。

**两个完整误差界的局部关系。** 在以 \(z^\star\in S\) 为中心的 \(B_R\) 中有 \(\mathrm I\)，则 \(B_{R/2}\) 中有 \(\mathrm O\) 的模 \(s\mapsto h(s)+s\)。对每个 \(q\in G(w)\)，若 \(s<R/2\)，利用 \(z=w+q\in B_R\) 得 \(d(w,S)\le d(z,S)+s\le h(s)+s\)。若 \(s\ge R/2\)，则 \(d(w,S)\le\|w-z^\star\|<R/2\le s\)。取下确界即得。交换 \(z,w\) 同样得到 \(\mathrm O\Rightarrow\mathrm I\) 的模 \(\psi+I\)。有额外残差帽时，缩小待认证的残差窗，令近极小图值仍在原残差帽内，再作同样的证明。这个局部关系不依赖 (1) 或覆盖。加入的 \(s\) 一般不可省。\(G(w)=w\) 时最佳线性模为 \((h,\psi)=(2I,I)\)，而 \(G(w)=-w/2\) 时为 \((I,2I)\)。两个端点可各自用作假设，定量结论仍依赖保留的是哪一个模。

<a id="dd2-dual-envelope"></a>
## 2. 逐边的精确几何

固定 \(t>0\) 及 \(\alpha>0\)。令
\[
\begin{aligned}
B(t)&=\frac{t+\sqrt{t^2+4\beta D(t)}}{2\beta},\\
E_\alpha(t,s)^2&=t^2+2\alpha D(t)-\alpha(2\beta-\alpha)s^2,\\
M_\alpha(t,s)&=\min\{t+\alpha s,\ E_\alpha(t,s)\},\qquad 0\le s\le B(t).
\end{aligned}
\tag{3}
\]
此处取非负平方根。令 \(A=\langle q,z-p\rangle\)。(1) 和 Cauchy–Schwarz 给
\[
\max\{-ts,\beta s^2-D(t)\}\le A\le ts .
\]
它恰好要求 \(s\le B(t)\)，也保证 \(E_\alpha(t,s)^2\ge(t-\alpha s)^2\)。在维数至少二时，可取最小的 \(A\) 并同时达到 \(\|w-p\|=M_1(t,s)\) 与 \(\|z_\alpha-p\|=M_\alpha(t,s)\)。若要保留上传稿原条件中的正 \(\Phi\)，在几何定理直接置 \(D=-\Phi\)，并用 \(\{s\ge0:\beta s^2-ts\le D(t)\}\) 替代 \([0,B(t)]\)。下述非负缺陷的严格门和长度推论仍采用 \(D\ge0\)。

给定实际 \(a\)，其可行范围为 \(\max\{0,t-s\}\le a\le M_1(t,s)\)。取 \(s>0\)。定义
\[
U_\alpha(t,s,R)=
\begin{cases}
R+(1-\alpha)s,& 0<\alpha\le1,\\[1mm]
\min\!\left\{R+(\alpha-1)s,\
\sqrt{\alpha R^2+\alpha(\alpha-1)s^2-(\alpha-1)t^2}\right\},&\alpha>1 ,
\end{cases}
\tag{4}
\]
其中 \(R+s\ge t\)。在给定 \(t,s,a\) 下，\(r\) 的精确上端为
\[
r_{\max}=\min\{M_\alpha(t,s),U_\alpha(t,s,a)\}.
\tag{5}
\]
精确下端条件为
\[
r\ge\max\{0,t-\alpha s,a-|1-\alpha|s\},
\tag{6}
\]
当 \(0<\alpha<1\) 还须
\[
r^2\ge (1-\alpha)t^2+\alpha a^2-\alpha(1-\alpha)s^2 .
\tag{7}
\]
维数至少二时，每个满足 (3)、\(a\) 的范围及 (5)–(7) 的四元组，均可在一个至多有三个元素的零集 \(S\) 中实现。\(s=0\) 时三点重合，\(a=r=t\)。\(t=0\) 时 (1) 与 \(D(0)=0\) 强制 \(s=0\)。

**证明。** (3) 来自上面的内积区间和平方展开。以 \(w\) 为原点，写 \(z=s e_1\)，\(z_\alpha=(1-\alpha)s e_1\)。当取到输出最近点 \(v\) 时，\(\|v\|=a\)，且 \(\|v-s e_1\|\ge t\)。维数至少二时，固定半径 \(R=\|v\|\)，其第一坐标可取区间
\[
-R\le v_1\le\min\{R,(R^2+s^2-t^2)/(2s)\}.
\]
恰有 \(R+s\ge t\) 时该区间非空。对 \(0<\alpha\le1\)，取 \(v_1=-R\) 使到 \(z_\alpha\) 的距离最大。对 \(\alpha>1\)，取区间最大值。代入平方距离即得 (4)。当只知 \(\|v\|\le R\) 时，(4) 随半径非降，结果相同。即使未取到输出最近点，也可用趋于实际 \(a\) 的半径取极限以得到上界。

再取 \(u=z_\alpha+b\) 为更新点的候选最近锚，固定 \(\|b\|=r\)，要求 \(\|u-z\|\ge t\) 及 \(\|u-w\|\ge a\)。令 \(d=(1-\alpha)s\)。第一条件给
\[
b_1\le(r^2+\alpha^2s^2-t^2)/(2\alpha s).
\]
第二条件要求 \(r^2+d^2+2d b_1\ge a^2\)。若 \(\alpha<1\)，它给一个下界，与 \([-r,r]\) 及前一上界有公共点，恰等价于 (6)–(7)。若 \(\alpha>1\)，两个条件都给上界，取 \(b_1=-r\) 可检验其相容性。若 \(\alpha=1\)，第一条件与 \(r\ge a\) 即给 (6)。这些不等式也可对近极小锚取极限，因而对任意真实距离成立。当 \(a\le M_1\) 且 \(r\le r_{\max}\) 时，取最大化两个距离的 \(p\)、按 (4) 选的 \(v\)，再加刚构造的 \(u\)。三者到每个点的距离都不小于其指定值，且分别达到 \(t,a,r\)。这样同时实现四个量和 (1)。证毕。

**输出半径与输入误差界一起优化。** 在固定 \(t\) 时，令 \(\mathcal A(t)\) 为 \(0\le s\le B(t)\) 中满足以下每一项已启用限制的集合。启用 \(\mathrm I\) 时加 \(t\le h(s)\)。启用 \(\mathrm O\) 时加 \(t\le s+\psi(s)\)。精确几何上包络为
\[
\mathcal P_\alpha(t)=
\sup_{s\in\mathcal A(t)}
\begin{cases}
M_\alpha(t,s),&\text{仅启用 }\mathrm I,\\
\min\{M_\alpha(t,s),U_\alpha(t,s,\psi(s))\},&\text{启用 }\mathrm O .
\end{cases}
\tag{8}
\]
空集对应没有正距离允许边。若只为记账，可把无边的距离包络记为零。启用 \(\mathrm O\) 时可直接在 (4) 取半径 \(R=\psi(s)\)。即使输入锚 \(p\) 到 \(w\) 小于 \(R\)，这样构造的两个锚也给 \(d(w,S)\le R\)，同时达到 (8) 的被优化值。这项论证保留了同一边的 \(s\)，不把两个误差界的不同选中值混用。

**完整闭图的达到。** 若 \(0<\beta\le1\) 且启用 \(\mathrm I\) 时 \(h(u)\ge u\)，对几何见证的有限目标集 \(S\)，定义完整 \(F\) 为所有边 \(q=z-p,\ p\in P_S(z)\) 加见证的那一条边。默认边满足 (1)，且把 \(w\) 送到 \(S\)。附加边由 (8) 可行性保证两项已启用误差界。全图于是满足 (2)，因为每个值已验证。\(F\) 全域非空、闭图，\(G\) 也闭图，二者的零集恰为 \(S\)。更一般可用默认边 \(q=\gamma(z-p)\)，其中 \(\gamma>0\) 要在覆盖窗的所有距离 \(u\) 上满足
\[
D(u)\ge(\beta\gamma^2-\gamma)u^2,\quad
h(\gamma u)\ge u\text{（若启用）},\quad
\psi(\gamma u)\ge|1-\gamma|u\text{（若启用）}.
\]
相应默认边界也可在闭距离窗上定义。当 \(D\) 为二次、误差界模为线性且默认边在整个空间可用时，能在一个完整闭图算子中将见证缩放到任意小尺度。把模板点和其距离球填入以 \(\tau^n e_1\) 为中心、半径 \(c\tau^n\) 的两两不交球，\(c<1/4,\ \tau<1/3\)，并在各球内以统一比例缩小。将所有模板锚及极限 \(0\) 纳入 \(S\)，保留全部默认边和所有缩放的见证边。球中模板点的距离在其模板球内已经达到，外球锚不改变这些距离，附加边只积聚到 \((0,0)\)。

(8) 在上述范围之外仍是逐点最优的几何结果。维数一、固定目标集、固定原算子和额外的全图覆盖结构均可进一步收紧。一个给定算子的最坏一步因子或其收敛门需要额外证据。

## 3. 严格下降门与线性回收

假设 \(t>0\)，\(\beta>0\)，\(D(t)\ge0\)。令
\[
m=
\begin{cases}
\min\{B(t),\sqrt{2D(t)/(2\beta-\alpha)}\},&0<\alpha<2\beta,\\
B(t),&\alpha\ge2\beta .
\end{cases}
\tag{9}
\]
恰在 \(s\le m\) 时 \(M_\alpha(t,s)\ge t\)。可行条件 \(t\le h(s)\)、\(t\le s+\psi(s)\) 和 (4) 的值，均随 \(s\) 非降。因此 \(\mathcal P_\alpha(t)\ge t\) 当且仅当 \(s=m\) 满足所有启用的可行条件，并且启用 \(\mathrm O\) 时 \(U_\alpha(t,m,\psi(m))\ge t\)。右连续模在可行区间使上包络被取到，这里才能把逐边门写作严格的上包络门。

完整步长 \(\alpha=\beta=1\) 给 \(m=\min\{B,\sqrt{2D}\}\)。输入单独使用的严格门为 \(h(m)<t\)，输出单独使用为 \(\psi(m)<t\)，共同使用为 \(\min\{h(m),\psi(m)\}<t\)。此时输出型包络仍须保留 \(t+s\) 和可行域 \(t\le s+\psi(s)\)。只有正距离才讨论严格下降。

过松弛的第二根式能改变门。取 \(\alpha=3/2,\ \beta=1,\ D(t)=25t^2/169,\ \psi(s)=4s/5\)，则 \(m=10t/13\)。简单三角不等式在 \(m\) 给出 \(\psi(m)+(\alpha-1)m=t\)，只能把 \(t\) 留在几何上界中。用 (4) 时，\(\psi(m)^2+(\alpha-1)m^2=114t^2/169<t^2\)，所以 \(U_\alpha(t,m,\psi(m))<t\)。这给每个 \(t>0\) 的严格门，且默认投影提供完整闭图类的几何达到。

对 \(\alpha=\beta=1,\ D(t)=\sigma t^2\)、\(h(s)=\chi s\)、\(\psi(s)=k s\)，若两个误差界均启用，记
\[
b=(1+\sqrt{1+4\sigma})/2,\quad e=\sqrt{1+2\sigma},\quad
\ell=\max\{1/\chi,1/(1+k)\}.
\]
可行性为 \(\ell\le b\)，此时精确几何因子为
\[
\min\{b,kb,ek/\sqrt{1+k^2},\sqrt{e^2-\ell^2}\}.
\tag{10}
\]
将 \(s/t\) 记作 \(v\)。能量候选 \(E(v)=\sqrt{e^2-v^2}\) 分别在 \(v=b-1\) 和 \(v=e/\sqrt{1+k^2}\) 与两条上升的候选 \(1+v,kv\) 相交。若 \(kb<b-1=E(b)\)，则 \(k<1\) 且全区间上的最小候选始终是 \(kv\)，最优值在 \(v=b\) 取到。其余情形下，后一个交点不超过 \(b\)，两条上升候选的较小者与能量项在两个交点的较大处相交。若该处在 \([\ell,b]\)，就取这个交点。若它在 \(\ell\) 左侧，取左端的 \(E(\ell)\)。这给出 (10)。仅启用输入时删除 \(k\) 相关两项并取 \(\ell=1/\chi\)。仅启用输出时，\(\ell=1/(1+k)\le e/\sqrt{1+k^2}\)，且 \(\ell\le b\)，因此其裁切项冗余，即 C285 的三项因子。

**(10) 的完整闭图锐性。** 除 \(kb<b-1\) 外，可在最优 \(s\) 处使 (8) 的距离值等于 \(M_1(1,s)\)。在单位输入上选取复平面图边 \(1\mapsto q\)，满足 \(|q|=s\) 及 \(|1-q|=M_1(1,s)\)，再延拓为 \(F(z)=qz\)。每个条件按 \(|z|\) 或 \(|z|^2\) 缩放，因而对全图成立。若 \(q=1\)，则图剪切后的 \(G\) 只在零点有非空纤维，输出误差界仍成立。

若 \(a_0:=kb<b-1\)，取
\[
S=\mathbb R\setminus\bigl((-1,1)\cup(b-a_0,b+a_0)\bigr),\qquad F(z)=b(z-P_S(z)).
\]
对所有输入，\(s=b t\)，因此 \(\chi b\ge1\) 给输入真残差误差界，而 (1) 取等。对任一最近点，默认输出越过所选的缺口端点。若向另一缺口前进，须先越过宽度 \(\Delta=b-a_0-1>0\) 的零集间隙。若输入距离 \(u=d(z,S)\le1\)，输出到目标的距离至多 \([(b-1)u-\Delta]_+\le a_0u\)。若 \(u>1\)，输入必在第二个缺口，其中 \(u\le a_0\)。朝第一个缺口的输出到 \(S\) 的距离至多 1，且 \(1<a_0u\)。反向输出落入 \(S\)。由此每条完整图边都满足 \(a\le a_0t=ks\)，取下确界得输出真残差误差界。\(z=0\) 选择 \(p=1\) 时，\(w=b\) 使 \(d(w,S)=kb\)，达到 (10)。将各组缺口和可能的输出安排在趋零的两两不交缩放区间内，并保留所有外部点属于 \(S\)，同一个闭图关系便在任意小尺度达到该因子。缺口内距 \(S\) 的距离由本缺口端点决定，且所有默认输出留在该组区间内。

<a id="dd2-dual-length"></a>
## 4. 两端可共用的长度势与变松弛

定义
\[
H(s)=
\begin{cases}
h(s),&\text{输入型},\\
s+\psi(s),&\text{输出型},\\
\min\{h(s),s+\psi(s)\},&\text{联合型},
\end{cases}\qquad
\ell(t)=\inf\{s\ge0:H(s)\ge t\}.
\]
每条边有 \(s\ge\ell(t)\)。在有覆盖且 \(0<t\le R\) 的工作距离中，此下界有限、为正、非降。假设 \(\alpha\) 可变且 \(2\beta-\alpha\ge c>0\)，并存在 \(0<\theta<1\) 使
\[
2D(t)\le(1-\theta)c\,\ell(t)^2 .
\tag{11}
\]
若 \(\Theta(t)=\int_0^t u/\ell(u)\,du\) 有限，由 (3)、(11) 得
\[
t^2-r^2\ge\theta\alpha(2\beta-\alpha)s^2
\ge\theta c\,(\alpha s)\ell(t).
\]
从而
\[
\boxed{\ \alpha s\le\frac{2}{\theta c}[\Theta(t)-\Theta(r)]\ },\qquad
t^2-r^2\ge\theta c\,\alpha\ell(t)^2 .
\tag{12}
\]
这里使用 \(\ell(u)\le\ell(t)\) 给出的 \(\Theta(t)-\Theta(r)\ge(t^2-r^2)/(2\ell(t))\)。若 \(\sum_k\alpha_k=\infty\)，则 (12) 保证 \(t_k\downarrow0\)，因为正的极限下 \(\ell(t_k)\) 有正下界。有限长度保证强极限，且极限属于闭 \(S\)。结论包括 \(2\beta_k-\alpha_k\ge c\)、\(\alpha_k\) 变化的方向松弛。仅有限长度结论无需对 \(\sum\alpha_k\) 另作要求。对 \(F=I\)、\(\alpha_k\in(0,1)\) 且 \(\sum\alpha_k<\infty\)，非零轨道仍可收敛在 \(S\) 之外，故该条件有实际作用。

有限前缀的预算为 \(2\Theta(t_0)/(\theta c)\)。若从 \(z_0\) 出发的预算闭球及相应距离窗包含在输入覆盖域内，每个前缀可借此留在输入工作窗。需要输出位置或残差窗时，另留出 \(\sup_{0\le t\le t_0} B_{\eta,D}(t)\) 的裕量，其中 \(\beta\ge\eta>0\)。\(D(t)\to0\) 时此裕量趋零。由 \(s\le B_{\eta,D}(t)\) 控制 \(w=z-q\) 与残差，再用每个有限前缀的长度预算留域，得到对全部当步允许选择的结论。尾长至多 \(2\Theta(t_k)/(\theta c)\)，且 \(\|w_k-z_\infty\|\le \|z_k-z_\infty\|+B_{\eta,D}(t_k)\)。

例如 \(\psi(s)=K's^\rho\)、\(1/2<\rho<1\)，则输出型 \(\ell(t)\sim (t/K')^{1/\rho}\)，故 \(\Theta(t)\asymp t^{2-1/\rho}\)。当 \(D=Mt^p\) 时 \(p>2/\rho\) 满足 (11)，临界 \(p=2/\rho\) 的严格充分常数为 \(2M<c\,(K')^{-2/\rho}\)。写 \(\nu=2/\rho-2\)，由 (12) 和 \(u\mapsto u^{-\nu}\) 的凸性可得未到零前 \(t_{k+1}^{-\nu}-t_k^{-\nu}\ge C_0\alpha_k\)，其中 \(C_0>0\) 与 \(k\) 无关。把由此得到的距离率代入 \(\Theta(t_k)\) 即给尾长及点率。普通 PPA 的 \(K'=K/\lambda^\rho,\ \alpha=\beta=1\) 恢复 C399。该论证只需要工作窗中的下界 \(\ell(t)\)，无需额外假定显式逆模是 \(o(t)\)。

## 5. 与 Alcantara v1 的逐式比较

Jan Harold Alcantara, [arXiv:2611.20523v1](https://arxiv.org/pdf/2611.20523v1)，Definition 3.3、Proposition 3.4 和 Remark 3.5，印刷页 8–11。原文在零集相对 \((U,V)\)-半单调、\(U\succeq-\varepsilon I,\ V\succeq\eta I\) 下，对全部图值及零锚给出 (1) 的 \(D(t)=\varepsilon t^2\) 版本。其证明对所有零锚取下确界，因此不需要最近锚存在。这里采用对每条合法边存在最近锚的量词。原文的两个备选条件分别在同一参考零球内对 \(F\) 和 \(G\) 施加真正的线性度量次正则性。原文有单独的全轨道覆盖、留域和收敛验证，下列对照首先针对一步不等式。

设 \(\delta=\alpha(2\beta-\alpha)\ge0\)。取 \(h(s)=\chi s\)，原文式 (14) 把 \(s\ge t/\chi\) 代入能量，给
\[
r^2\le (1+2\alpha\varepsilon-\delta/\chi^2)t^2,\qquad
\Delta_a=\delta-2\alpha\varepsilon\chi^2.
\]
取 \(\psi(s)=\widehat\chi s\)，原文通过 \(r\le(\widehat\chi+|1-\alpha|)s\)，令 \(b_\alpha=\widehat\chi+|1-\alpha|\)，得到
\[
r^2\le\frac{(1+2\alpha\varepsilon)b_\alpha^2}{b_\alpha^2+\delta}t^2,\qquad
\Delta_b=\delta-2\alpha\varepsilon b_\alpha^2 .
\]
原文要求相应 \(\Delta_k\) 统一正下界，给两种可变松弛的线性收敛方案。其证明末尾已给从 \(G\) 到 \(F\) 的局部模 \(1+\widehat\chi\)，并说明输出型可能给更小因子。Remark 3.5 在普通 PPA 的 \(\alpha=\beta=1\) 明写 \((1+2\varepsilon)\widehat\chi^2/(1+\widehat\chi^2)\) 这个平方因子。这里的 (8) 同时保留两端下界、输入锚和过松弛的输出锚。式 (12) 给可非线性的同一步尾势，使用的统一参数条件为 \(2\beta_k-\alpha_k\ge c>0\)、(11) 和相应覆盖。逐式对照不能推出一般性的定理包含或公开优先权。
