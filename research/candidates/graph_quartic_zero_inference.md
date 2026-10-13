# 图四次非凸优化：已认证极小点之后的未知驻点推断

状态：最终备选一。自然优化来源、完整临界 prox、同窗能量分支、全根证书及指数链通过。经典 Morse 能以同样条件给更细结论，不推荐它承担理论独占优势。

## 1. 优化模型、完整零集与算法

取13节点周期图 Laplacian $L=2I-S-S^{-1}$，固定 $J=1/4$ 和

\[
b=(-7,4,2,-3,6,-5,1,8,-4,3,-6,5,-2)/1000,
\]

\[
f(u)=\tfrac14\sum_i(u_i^2-1)^2+\tfrac18u^TLu-b^Tu,
\quad F=\nabla f=u^{[3]}-u+Lu/4-b.
\]

双阱与图平滑能用于软标签／双稳态图状态拟合，线性项是节点偏好。标准 graph GL 来源：Luo–Bertozzi, *Convergence of the Graph Allen–Cahn Scheme*, J.Stat.Phys.167 (2017), 934–958，DOI [10.1007/s10955-017-1772-4](https://doi.org/10.1007/s10955-017-1772-4)， [作者稿](https://www.math.ucla.edu/~bertozzi/papers/JSTATPHYS2017-final.pdf)，Eq.(6)为 $\epsilon u^TLu/2+\sum W(u_i)/\epsilon$，$W(s)=(s^2-1)^2/4$；$\epsilon=1/2$ 后乘 $\epsilon$ 得无载荷部分。其 Eq.(9) 是二次 fidelity，**不是**本纯线性载荷。线性 bulk 项另见 Dirr–Orlandi, SIAM J.Math.Anal.41 (2009), 781–824, DOI [10.1137/070684100](https://doi.org/10.1137/070684100)，[正式 PDF](https://orca.cardiff.ac.uk/id/eprint/13064/1/Dirr%202009.pdf) p.781。具体有限图、节点输入与 PPA 是本轮定义的可认证实例，没有冒称现成数据。

完整 $S=\{u\in\mathbb R^{13}:F(u)=0\}$ 是所有驻点；其中局部极小、其它驻点、global minimizer 和算法极限严格区分。已认证 $M=\{p_1,\ldots,p_{16}\}$ 只是一部分严格极小点。

普通核 $v=I$、$\lambda=1$，完整更新为

\[
T(x)=\operatorname*{argmin}_y\{f(y)+\tfrac12\|y-x\|^2\},quad
y\in J_F(x)\iff y^{[3]}+Ly/4=x+b.
\]

该子问题删去常数后为 $\sum y_i^4/4+y^TLy/8-(x+b)^Ty$，严格凸、强制；对每个 $x\in\mathbb R^{13}$ 恰一个输出。完整驻点近端和完整 argmin prox 相同，没有挑分支。完整图为 $\{(y^{[3]}+Ly/4-b,y):y\in\mathbb R^{13}\}$，$\operatorname{Fix}T=S$。

四次严格单调给 $\|T(x)-T(z)\|\le52^{1/3}\|x-z\|^{1/3}$；常数方向有 $T(-b+t^3\mathbf1)=t\mathbf1$，故最佳全局 Hölder 指数1/3，非 Lipschitz 在 $-b$。本输入不是固定点。无完整坐标闭式或一般精确轨道；最短完整证明是严格凸子问题一段。

## 2. 已识别根球与同一 RLEB 元组

[精确证书代码](../code/graph_quartic_zero_inference/verify.py)默认17次局部优化，得到16个有理中心 $z_i\in10^{-12}\mathbb Z^{13}$；每点以 Fraction LDL 证明 $DF(z_i)\succ I/2$，精确残差满足 $\|F(z_i)\|_1<(2/5)10^{-10}$，$\|z_i\|_\infty\le1.01$，所有中心距离平方大于1。

取 $\rho=.01$，对角变化不超过 .0609，所以 $DF\succeq mI$、$m=2/5$。在半径 $\varepsilon=10^{-10}$ 球边界梯度严格向外；限制目标的内点极小值给真根 $p_i$，强单调给 $B_\rho(z_i)$ 内唯一性及 $\|p_i-z_i\|<\varepsilon$。这是解析存在／唯一证明，不以浮点极小点标签承重。

取

\[
U=\bigcup B_{1/200}(p_i),\quad R=1/10000,\quad
a(t)=t,quad\omega(t)=t,quad h(t,q)=q,quad
\psi(t)=5t/2,quad\bar t=1,
\]

\[
\rho_E(q)=q,quad g(q)=2q/5,quad\kappa=5/\sqrt{29}.
\]

完整 $H=I+F$ 全域单调；对从 $p_i$ 出发的射线，小球边界的径向增量至少 $(1+m)/200$，边界外不减。因此每个输入在该球时全部真实输出先留在同一球，再得到 $\|Tx-p_i\|\le5\|x-p_i\|/7$。这先验输出定位避免局部 EB／留域循环。

同一物理最近锚 $p_i$ 满足

\[
\|2Tx-x-p_i\|^2=\|x-p_i\|^2-4\langle Tx-p_i,F(Tx)\rangle
\le d(x,M)^2,
\]

\[
r_F(y)=\|F(y)\|,qquad d(y,M)\le(5/2)r_F(y).
\]

局部最佳 EB 幂为1；固定点处 $DF$ 可逆，此幂不能提高。$K(t)=H_{\rm step}(t)=t$，$K(R)<\bar t$。指定常数的直接 C249/C02 门给 $\psi(K)=2.5t$，失败；C250 能量门则为

\[
(1+4/25)q^2\le t^2\Longrightarrow q\le\kappa t.
\]

从 $5/\sqrt{29}<15/16$ 得 $\Theta(t)<16t$，共同严格留域预算

\[
\Theta(R)<16R=.0016<.0049=1/200-R.
\]

全部输出、真实残差、零距离吸收、同窗能量兼容和物理有限长度通过。每条认证 PPA 轨道趋所属球的唯一 $p_i$；$d_k\le\kappa^k d_0$，尾长小于 $16\kappa^k d_0$。最近锚及残差不替换成选中图值；这里 singleton 是完整 $F$ 的属性。

## 3. 拓扑、全根正则与预测

$M$ 为16个 isolated strict minima，$\chi(M)=16$；各点 $\det DF>0$，且 $I+DF$ 正定，近端局部指数各为+1。上述球给隔离吸引管。

极值原理独立证明 $T([-1.1,1.1]^{13})$ 严格进入该立方体及全部 $S\subset[-1.05,1.05]^{13}$。完整连续映射的总指数是1。远场 $2T-I$ 有线性项，不能直接调用原 C254；使用候选报告重建的紧立方体 ENR 归一化／可加性。

[共同模3附页](graph_quartic_modular_certificate.md)完整证明：$\mathbb Z_{(3)}[u]/(F)$ 以指数0、1、2的单项式为有限自由基；$\det DF$ 模3为可逆常数。准确13阶检验

\[
\det(L/4-I)=-4^{-12},qquad\det(L-I)=2\pmod3
\]

给全部复／实零点非退化，恰1594323个不同复根，而未生成指数阶矩阵或求隐藏根。每个实零点 $p\ne0$，connected $L$ 给 $I+DF(p)$ 正定，所以完整 $T$ 在所有固定点可微，各指数为 $\pm1$。

因此未知驻点簇总指数 $-15$，至少有15个不同负指数实驻点，未知总实点数为奇数；完整实点数至少31。位置在 $[-1.05,1.05]^{13}$ 且不在16个中心半径.01的认证根球内。准确总实根数、全部稳定态／最优值和坐标仍需解方程；不以复根总数替代它们。

## 4. 经典正面、失败模式及准入表

经典 ABS 的 H1 来自同一 global-min 比较，H2 来自 $F(y)=x-y$，$f$ 为强制多项式、满足 KL；同一算法已有正面有限长度路径。局部强单调直接收缩更短。尤其全根非退化以后，Milnor *Morse Theory*, Theorem3.5 和 §5 p.30 strong inequalities 给 $m_1\ge m_0-1\ge15$，能进一步证明至少15个 **Morse index1** 鞍点，比本指数总和更细。必须保留这一比较，不将优化备选说成旧理论空白。

| 门 | 裁决 |
|---|---|
| 优化来源 | 通过；标准图 GL 与明确线性偏好组合，非实测问题 |
| 全输入、全部纤维 | 通过，完整严格凸临界子问题 |
| 真残差、最近锚、全输出定位 | 通过同一球与同一常数 |
| 直接兼容 | 指定常数失败；C250能量分支通过 |
| 留域／可和位移 | 通过，.0016<.0049 |
| 全局指数入口 | 独立cube通过，原C254反射门失败 |
| 全根正则／固定点可微 | 两项分别通过 |
| 额外点数、指数、位置 | 通过；精确全分类未求 |
| 解点noncalm、非孤立零集 | 不提供：所有根孤立、完整prox在根处smooth |
| 经典差异／复杂度优势 | 独占或最优速度声称不通过；同成本Morse正面 |

临界攻击：$\lambda>1$ 时，输入 $-\lambda b$ 的完整纤维至少含 $0,\pm\sqrt{1-1/\lambda}\mathbf1$；不能沿用唯一完整近端。偶数周期／非法模分母要重新认证。最短承重证明约2页：严格凸覆盖、统一根球与C250、一个公共代数引理。完整内容与参数在代码及 [results.json](../code/graph_quartic_zero_inference/results.json)，模门反例另有 [modular_verify.py](../code/graph_quartic_zero_inference/modular_verify.py)。
