# 幂次剪切：同一法向射线的精确速率校准

<a id="ps-object"></a>
## PS-OBJECT · 显式完整图与约定

取 \(0<\gamma<1\)、\(q>1/\gamma\)、\(\alpha=\gamma q>1\)，令 \(P_a(z)=\operatorname{sign}(z)|z|^a\)。在 \(\mathbb R^2\) 固定生成步长 \(\lambda=1\)：
\[
J(t,z)=(t+|z|^\gamma,P_\alpha z),\quad
F=J^{-1}-I,
\quad S=\operatorname{zer}F=\mathbb R\times\{0\}.
\]
\(J\) 为全域三角双射，其逆为 \(J^{-1}(s,u)=(s-|u|^{1/q},P_{1/\alpha}u)\)。因此 \(F\) 是完整、处处单值的原关系
\[
F(s,u)=(-|u|^{1/q},P_{1/\alpha}u-u),\qquad
r_F(s,u)^2=|u|^{2/q}+|P_{1/\alpha}u-u|^2.
\]
在无界全图上不能声称次线性全对 RL；以下 \(\gamma\)-Hölder 证书只用**有界输入窗口**。精确轨道公式则在全域成立。

<a id="ps-rate"></a>
## C42-v1 / PS-RATE · 可达到的 \(\gamma q\) 而非普遍速率

对任意 \(x=(t,z)\) 且 \(0<|z|<1\)，令 \(r=|z|\)。有
\[
d(x,S)=r,\quad d(Jx,S)=r^\alpha=r^{\gamma q},\quad
\|x-Jx\|^2=r^{2\gamma}+(z-P_\alpha z)^2.
\]
真残差对全部 \((s,u)\) 满足 \(d((s,u),S)=|u|\le r_F(s,u)^q\)；指数 \(q\) 在零集旁不可增大，且沿 \(u\to0\)，\(r_F(s,u)/|u|^{1/q}\to1\)。对实际输出 \(u=P_\alpha z\)，
\[
\frac{d(Jx,S)}{\|x-Jx\|^q}\to1
\quad(r\downarrow0),
\qquad
\frac{d(Jx,S)}{d(x,S)^{\gamma q}}=1.
\]

**证明。** 反演给上面的完整图与残差。因为 \(1/\alpha>1/q\) 且 \(1/\alpha<1\)，\(|P_{1/\alpha}u-u|=O(|u|^{1/\alpha})=o(|u|^{1/q})\)，故残差渐近等价于 \(|u|^{1/q}\)，任意大于 \(q\) 的幂界沿 \(u\to0\) 失败。又 \(\alpha>1>\gamma\)，所以 \(z-P_\alpha z=O(r)\) 而 \(\|x-Jx\|/r^\gamma\to1\)。代入 \(r_+=r^\alpha\) 得两项比例。证毕。

<a id="ps-rl"></a>
## 有界窗口上的全对反射指数及留域

反射为 \(C=2J-I\)，即 \(C(t,z)=(t+2|z|^\gamma,2P_\alpha z-z)\)。在任意**有界**输入矩形 \(D=[-M,M]\times[-b,b]\) 上，\(C\) 对所有输入对为某个有限常数的 \(\gamma\)-Hölder：\(|z|^\gamma\) 有 \(\gamma\)-Hölder 界，\(P_\alpha\)、\(z\) 与 \(t\) 在矩形上 Lipschitz，且有界直径使一阶界降为 \(\gamma\) 次幂。沿 \((t,z)\)、\((t,0)\) 的反射差除以 \(|z|^\gamma\) 趋于 2，故在含此法向射线的任意邻域没有更大指数。该极限仅是常数下界，未证明某个窗口的最优有限常数恰为 2。

迭代满足 \(r_{k+1}=r_k^\alpha\)、\(t_{k+1}=t_k+r_k^\gamma\)。对 \(0<r_0<1\)，
\[
\sum_{k\ge0}r_k^\gamma
\le\frac{r_0^\gamma}{1-r_0^{\gamma(\alpha-1)}}.
\]
因此若有界矩形的初始切向余量严格大于右侧、法向半径大于 \(r_0\)，**这条初始轨道**留在窗口并收敛于 \(S\) 中一点。不能说整个矩形对 J 不变：靠切向边界的点一步就可能出界；也不能把有界窗口证书延伸到无界全图。

<a id="ps-source"></a>
## 证据和使用边界

本页重新计算 [9/01 RL_foundations §9.2 / GX-071](../../../history/sources/次单调论文研究/RL_foundations.md) 的对象、完整图、真残差、比例和切向预算；状态 `derived-checked` 限于上述算术。它展示一个**特意反向校准**使实际法向速率恰为 \(\gamma q\) 的模型，不能推出所有 RL–EB 算法的必要速率、自然性、genericity 或最优全对常数。历史同源冻结稿是版本副本，不算第二个独立见证。下一例 GX-072 的振荡粗糙度与实际轨道分离须另立对象卡并核两尺度估计。
