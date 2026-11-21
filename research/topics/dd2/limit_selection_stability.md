# 完整 DD1 的快速点收敛与极限解选择的低稳定性

本页回答一个正文问题：DD 已经保证有限长度和点收敛以后，初值到最终零点的映射能有多稳定？已有 C116、C138–C141 给 RLEB / 一般尾界下的坏选择。本页把这一现象直接落实到二维、连续单值原算子、唯一完整近端及完整 DD1 的线性真误差界。连续回缩的既有机制和定量先例见 [文献核验](../../LITERATURE.md#lit-dd-retraction-priority)。本页不认定公开新颖性。

<a id="dd1-limit-selection-stability"></a>
## C462-v1：精确对象与结论

固定 Euclidean 平面，\(\lambda=1\)、\(S=\mathbb R\times\{0\}\)、\(B=R=1/4\)，令
\[
g(r)=\frac{r|r|}{1+|r|},\qquad
h_t(p)=p+B\min\{\sqrt{p_+},t\},\qquad
T(p,r)=(h_{|r|}(p),g(r)),\qquad F=T^{-1}-I. \tag{LS1}
\]
这里 \(p_+=\max(p,0)\)。T 是全空间同胚，F 是全域连续单值原算子，完整 \(J_F=T\)，精确零集等于 S。对完整输入带 \(D_R=\{(p,r):|r|\le R\}\) 的每条边 \(x\mapsto y=Tx\)，记 \(t=d(x,S),a=d(y,S),s=\|x-y\|\)、\(\rho=r_F(y)=\|F(y)\|\)。全部边满足
\[
a\le\tfrac14\rho,\qquad
\langle x-y,y-P_Sx\rangle\ge-\tfrac1{16}t^2. \tag{LS2}
\]
零输入驻定，完整近端全域存在，\(D_R\) 前向不变。这是完整 DD1，\(L=1/4,\sigma=1/16\)，其严格收缩证书为
\[
m=\frac14\sqrt{\frac{18}{17}}=\frac3{\sqrt{136}}<1. \tag{LS3}
\]
每条带内轨道有限长、收敛到 \(P(x)\in S\)，并有共同物理尾界
\[
\|T^kx-P(x)\|\le\sum_{j\ge k}s_j
\le\frac{\sqrt{17}}3t_k
\le\frac{\sqrt{17}}3R^{2^k},\qquad t_k=d(T^kx,S). \tag{LS4}
\]
因此 P 在该带上连续且是回缩。每个 \(t_0>0\) 的点误差 \(e_k=\|T^kx-P(x)\|\) 甚至 Q-二次收敛：当初始 p≤0 时 \(e_{k+1}/e_k^2\to1\)，当初始 p>0 时该比值趋于 \(4/\sqrt{17}\)。初始 \(t_0=0\) 另为驻定轨道。

然而，固定 \(r_0=1/8\)、\(x_0=(0,r_0)\)、\(x_\varepsilon=(\varepsilon,r_0)\)，存在正常数 c,C 及 \(\varepsilon_0\)，使
\[
B\exp[-C\sqrt{\log(1/\varepsilon)}]
\le\|P(x_\varepsilon)-P(x_0)\|
\le\tfrac56\exp[-c\sqrt{\log(1/\varepsilon)}]
\quad(0<\varepsilon<\varepsilon_0). \tag{LS5}
\]
故 P 在这个非零初值处没有任何正阶两点 Hölder 模。这不否定在零点处的稳定性，也不否定完整 DD1 的任何收敛结论。事实上，对每个固定 \(z\in S\)，LS4 和 \(d(x,S)\le\|x-z\|\) 直接给
\(\|P(x)-z\|\le(1+\sqrt{17}/3)\|x-z\|\)，即固定零点处甚至有 Lipschitz calmness。输入 r0 可以换成任意固定 \(0<r_0\le R\)，常数随之改变；所以坏初值可任意接近零线。

## 完整原图和 DD1 的核验

每个 \(h_t\) 连续、严格增且满射，\(|h_t(p)-p|\le Bt\)。其逆在 \(\eta\le0\) 为 \(\eta\)；在 \(0\le\eta\le t^2+Bt\) 为
\[
h_t^{-1}(\eta)=\left(\frac{2\eta}{B+\sqrt{B^2+4\eta}}\right)^2;
\]
在 \(\eta\ge t^2+Bt\) 为 \(\eta-Bt\)。接缝值相同，且在 t=0 时退化为恒等。g 为严格递增全域同胚，其非负半径逆为
\[
|g^{-1}(z)|=\frac{|z|+\sqrt{|z|^2+4|z|}}2.
\]
先由输出的第二坐标唯一恢复 r，再反解 h，便得到连续的全域 \(T^{-1}\)。由 \(I+F=T^{-1}\) 可知完整近端恰为 T；不涉及允许子关系或遗漏图值。因为 \(|g(r)|<|r|\) 对 r≠0 成立，\(\operatorname{Fix}T=S\)，也就有 \(\operatorname{zer}F=S\)。

写 \(v=B\min\{\sqrt{p_+},t\}\)，则 \(0\le v\le Bt\)，且
\[
a=\frac{t^2}{1+t},\quad t-a=\frac t{1+t},\quad
s=\rho=\sqrt{v^2+(t-a)^2},\quad
\langle x-y,y-P_Sx\rangle=a(t-a)-v^2. \tag{LS6}
\]
同一完整 F 单值，故这里 \(s=\rho\) 来自确切纤维，不是把某个多值选择范数冒充真残差。由 \(a=t(t-a)\le R\rho\) 及 \(v^2\le B^2t^2\) 得 LS2。\(\ell=R\) 在 t=R,p≤0 取等；饱和边随 t↓0 使锚内积除以 t² 趋于 −B²，所以 \(\sigma=B^2\) 是本输入带的最小统一非负二次缺陷系数。

在 DD1 的原两条几何约束中，\(b=(2+\sqrt5)/4\)，而
\(h=\max\{1/b,\sqrt{(1+L^2)/(1+2\sigma)}\}=\sqrt{17/18}\)，给 LS3。另有实际更强的 \(a/t=t/(1+t)\le1/5\)，但它不替代 DD1 认证。全部原图、同一零集、含零输入、误差界输出域和不变输入带均已经核实。

原算子确实非单调。取相同 \(r_0>0\) 及 \(0<\varepsilon<r_0^2\)，两个输出之差为 \((\varepsilon+B\sqrt\varepsilon,0)\)，对应图值之差为 \((-B\sqrt\varepsilon,0)\)，其内积严格为负。

## 有限长度、二次点率和连续回缩

径向递推为 \(t_{k+1}=t_k^2/(1+t_k)\le t_k^2\le Rt_k\)。由 LS6，\(s_k\le\sqrt{1+B^2}\,t_k\)，求几何尾即得 LS4。有限长度、闭 S 和 \(t_k\to0\) 给点极限；T 连续，LS4 对全部带内初值一致，故有限迭代的一致极限 P 连续。T 在 S 上恒等，P 是回缩。

若初始 p≤0，切向坐标不动，\(e_k=t_k\)，所以二次比值趋1。若初始 p>0，p_k 非减且 t_k↓0，故终会有 \(\sqrt{p_k}\ge t_k\)，以后一直饱和，切向尾为 \(B\sum_{j\ge k}t_j\)。由 \(t_{k+1}=O(t_k^2)\)，
\[
\sum_{j\ge k}t_j=t_k+O(t_k^2),\qquad
e_k=\sqrt{1+B^2}\,t_k(1+O(t_k)).
\]
于是 \(e_{k+1}/e_k^2\to1/\sqrt{1+B^2}=4/\sqrt{17}\)。这是真实点误差的结论，不只是集合距离率。

## 首次饱和与两点低稳定性

两条比较轨道的 r_k 完全相同，零切向初值始终为0。对正切向初值记 \(z=\log(1/\varepsilon)\)，令
\[
N=\min\{k:p_k\ge t_k^2\}.
\]
N 有限，因为 \(p_k\ge\varepsilon>0,t_k\to0\)；当 ε↓0 时 N→∞，因为每个有限次迭代连续且参考轨道 p_k=0。令 \(A_0=\log8,B_0=\log10\)。径向对数递推给
\[
A_0 2^k\le-\log t_k\le B_0 2^k. \tag{LS7}
\]
事实上 \(-\log t_{k+1}=2(-\log t_k)+\log(1+t_k)\)，而 \(0\le\log(1+t_k)\le\log(5/4)\)。

在 k<N，\(p_{k+1}=\sqrt{p_k}(B+\sqrt{p_k})\)，且 \(B\le B+\sqrt{p_k}\le B+R=1/2\)。迭代对数，得到包括产生饱和的第 N 步在内的
\[
B^2e^{-z2^{-k}}\le p_k\le e^{-z2^{-k}}\quad(0\le k\le N). \tag{LS8}
\]
N 的条件结合上界给 \(z\le2B_0 4^N\)；第 N−1 步尚未饱和结合下界给
\[
z>2A_0 4^{N-1}-\log(1/B^2)2^{N-1}.
\]
所以对充分小 ε，
\[
\sqrt{z/(2B_0)}\le2^N<2\sqrt{z/A_0}. \tag{LS9}
\]
饱和以后 \(p_\infty=p_N+B\sum_{j\ge N}t_j\)。下界 \(p_\infty\ge Bt_N\)；又
\(p_N<t_{N-1}^2+Bt_{N-1}\le(R+B)t_{N-1}\)，因此
\[
Bt_N\le p_\infty\le\left(R+B+\frac B{1-R}\right)t_{N-1}=\tfrac56t_{N-1}.
\]
LS7、LS9 证明 LS5，可取
\(C=2B_0/\sqrt{A_0},c=A_0/(2\sqrt{2B_0})\)。P(x0)=(0,0)，极限差恰为 p∞。任意 α>0 都有
\(p_\infty/\varepsilon^\alpha\ge B\exp(\alpha z-C\sqrt z)\to\infty\)，这严格排除所有正阶 Hölder 模。

## 证据、独立攻击和正文用途

本轮直接重构了完整逆、原真残差、正负法向、零输入、局部窗、非单调图对、实际点率和首次饱和两侧估计；没有使用独立代理，也不把既有代理审查追溯授予此新模型。复算见 [固定参数与 Decimal 程序](../../code/dd1_limit_selection/README.md)，有限计算只核指定实例。

冷读检查：LS1 先定义原图及目标；LS6 将证书落实到同一完整纤维；LS4 供应连续回缩；LS7–LS9 再比较两个非零初值，故没有把零点处 calmness 误当两点 Hölder。旧 C116/C141 的模型不变，本页新身份专门保存二维连续单值 F 与完整 DD1 的直接桥。与 Wiśnicki 的区别是其定量引理要求单步 Lipschitz；本 T 在 p=0 附近的切向差为 ε+B√ε，未满足该条件。更广文献的新颖性比较仍未关闭。

正文功能是揭示“收敛速度”和“选出哪个零点的稳定性”各需要什么信息：DD1 的完整 A+B、绝对可和与点收敛全部成立，极限回缩仍可极不满足幂次稳定性。它可与 C426–C427 的目标几何和 C444/C457 的实际续接边界并列筛选，不能包装成修补 DD1 收敛缺口。
