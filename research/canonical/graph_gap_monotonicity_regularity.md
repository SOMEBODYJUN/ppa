# 同一原图间隙的两个切片

把 Fitzpatrick 图间隙沿原变量加二次正则化，比较图上零值与零残差截面的增长。以下推导适用于有限维多值算子和非孤立零集。二次间隙的适用边界见反例。相近间隙方法的公开先行性仍需逐式核对。

<a id="gap-two-slices"></a>
## 图上为零和零残差截面的增长

设 \(X=\mathbb R^n\)，\(F:X\rightrightarrows X\)，\(S=F^{-1}(0)\) 非空闭。固定 \(D\subset X\)，令 \(\Gamma_D=\{(y,v):y\in D,\ v\in F(y)\}\) 非空。对 \(a\ge0\) 定义
\[
\mathcal G_a(z,u):=\sup_{(y,v)\in\Gamma_D}
  \left\{\langle z-y,v-u\rangle-\tfrac a2\|z-y\|^2\right\}.
\]
允许上确界为 \(+\infty\)。这整个族可以写成移位图上的同一个 Fitzpatrick 间隙。令 \(T_a=F+(a/2)I\) 并将图限制到 \(D\)，则
\[
\mathcal G_a(z,u)=\mathcal G^{T_a}_0(z,u+(a/2)z).
\]
代入 \(T_a\) 的图值 \(v+(a/2)y\) 即得。这是已知的 Fitzpatrick 构造；以下次正则比较使用的是原算子 \(F\) 的近端根。若 \((z,u)\in\Gamma_D\)，取其本身即知 \(\mathcal G_a(z,u)\ge0\)。所以
\[
\left.\mathcal G_a\right|_{\Gamma_D}=0
\quad\Longleftrightarrow\quad
\forall (z,u),(y,v)\in\Gamma_D,\quad
\langle z-y,u-v\rangle\ge-\tfrac a2\|z-y\|^2.
\]
特别地，\(a=0\) 正好给全对单调性。全对量化到 \(D\) 上的完整纤维，无需图极大性。

固定 \(\beta\ge0\)，假设 \(\Gamma_D\) 上的上述全对不等式以 \(\beta\) 作为右侧二次系数。固定 \(\lambda>0\) 使 \(\lambda\beta<1\)，并取 \(2\beta<a<2/\lambda\)。记 \(c=\lambda(1-a\lambda/2)>0\)，\(g_a(z)=\mathcal G_a(z,0)\)，\(r_F(z)=\inf_{u\in F(z)}\|u\|\)，\(\inf\varnothing=+\infty\)。若 \(z\in D\)，则
\[
 g_a(z)\le \frac{r_F(z)^2}{2(a-2\beta)}.
\]
确实，任取 \(u\in F(z)\)，对每个竞争图点均有
\(\langle z-y,v\rangle-\frac a2\|z-y\|^2\le
\langle z-y,u\rangle-\frac{a-2\beta}{2}\|z-y\|^2\le
\frac{\|u\|^2}{2(a-2\beta)}\)。取上确界再取下确界。空纤维时上界按扩展实数解释。反向，每个满足 \(z=y+\lambda v\)、\((y,v)\in\Gamma_D\) 的根提供见证
\[
g_a(z)\ge c\|v\|^2 .
\]
因此对任意 \(W\subset D\)，若每个 \(z\in W\) 至少有一个这样的根，\(g_a\) 在 \(W\) 非负且零点恰为 \(S\cap W\)。若 \(g_a(z)=0\)，任一个根都给 \(v=0\)。反向用对零点的上界。

**由增长导出真残差次正则。** 在任意 \(W\subset D\) 上，若 \(g_a(z)\ge\gamma d(z,S)^2\)，\(\gamma>0\)，则
\[
d(z,S)\le [2\gamma(a-2\beta)]^{-1/2}r_F(z)\qquad(z\in W).
\]
此向无需存在根，也无需残差下确界取到。

**由真残差次正则导出增长。** 若在 \(D\) 上有 \(d(y,S)\le K r_F(y)\)，\(0<K<\infty\)，且每个 \(z\in W\subset D\) 至少有一个输出在 \(D\) 的原 PPA 根，则
\[
g_a(z)\ge \frac{c}{(\lambda+K)^2}d(z,S)^2\qquad(z\in W).
\]
见证根满足 \(d(z,S)\le\lambda\|v\|+d(y,S)\le(\lambda+K)\|v\|\)。当 \(W=D\) 且窗口内覆盖成立时，同一区域上二次增长与统一真残差线性次正则等价。一般 \(W\subsetneq D\) 时，逆向用到已证误差界的输出域 \(D\)。截断根的存在只用于构造一个见证。若要对完整预解式的每个根应用同一证明，须另证全部根落在适用域。普通度量正则依赖变化的右端，这里只处理零值次正则。

<a id="gap-varying-target"></a>
## 改变右端时的同一间隙

在同一个 \(\Gamma_D\) 假设和参数下，固定 \(W\subset D\) 与一族右端 \(V\subset X\)。令 \(S_\eta=F^{-1}(\eta)\ne\varnothing\) 对每个 \(\eta\in V\)，\(r_\eta(z)=\operatorname{dist}(\eta,F(z))\)。上节的上界直接给
\[
\mathcal G_a(z,\eta)\le\frac{r_\eta(z)^2}{2(a-2\beta)}
\qquad (z,\eta)\in D\times V.
\]
所以 \(W\times V\) 上的统一增长 \(\mathcal G_a(z,\eta)\ge\gamma d(z,S_\eta)^2\) 推出这一窗口的统一度量正则不等式。反向，若在 \(D\times V\) 有统一 \(d(y,S_\eta)\le K r_\eta(y)\)，且对每个 \((z,\eta)\in W\times V\) 存在 \((y,v)\in\Gamma_D\) 使 \(z=y+\lambda(v-\eta)\)，则
\[
\mathcal G_a(z,\eta)\ge c\|v-\eta\|^2\ge
\frac{c}{(\lambda+K)^2} d(z,S_\eta)^2.
\]
第一步用该图点作为竞争项，第二步用距离三角不等式及 \(r_\eta(y)\le\|v-\eta\|\)。在 \(W=D\) 并具备这族覆盖时，两类估计同窗等价。若 \(W,V\) 是参考图点两坐标的邻域，即是普通局部度量正则的不等式形式。变化右端用于检验正则性，原零问题的 PPA 仍取 \(\eta=0\)。

<a id="gap-obstruction"></a>
## 切片的增长与原 PPA 的符号

固定 \(\beta>0\)，在 \(X=\mathbb R^2\) 取 \(F(t,n)=(0,-\beta n)\)，\(S=\mathbb R\times\{0\}\)，\(D=X\)。这是 \(\beta\)-弱单调图（hypomonotone）。对 \(0<\lambda\beta<1\)，每个输入的完整原根唯一，\(J_{\lambda F}(t,n)=(t,n/(1-\lambda\beta))\)。任意非零法向轨道都扩张，而 \(r_F(t,n)=\beta|n|\)，且
\[
g_a(t,n)=\sup_{h\in\mathbb R}\left\{-\beta nh-\tfrac{a-2\beta}{2}h^2\right\}
   =\frac{\beta^2 n^2}{2(a-2\beta)}.
\]
这里 \(2\beta<a<2/\lambda\)，输出横坐标取输入横坐标即消除无关的惩罚。故 \(\mathcal G_a\) 在全图为零且零残差切片有精确二次增长，完整 PPA 仍发散。这给出了将两个切片直接合用的反例。参数门依赖小步，结论的范围止于所给窗口和步长。

**相同零残差切片、不同原动力学。** 再取 \(X=\mathbb R\times\mathbb R\times\mathbb R^2\)，\(F_\pm(s,n,h)=(0,c_\pm n,Jh)\)，其中 \(c_+=1,\ c_-=-1/3\)，\(J\) 为 90 度旋转。两者零集均为 \(S=\mathbb R\times\{0\}\times\{0\}\)，共享 \(\beta=1/3,\lambda=a=1\)。计算标量方向的间隙 \(\sup_d[c_\pm nd-(1+2c_\pm)d^2/2]\)，再加旋转方向 \(\|h\|^2/2\)，得到两个图的完整零残差切片都恰是
\[
g_1(s,n,h)=n^2/6+\|h\|^2/2.
\]
两个算子的正则化间隙均在各自完整图上为零，且全部原根都存在、唯一。它们在 \(n\) 方向的近端倍率分别为 \(1/2,3/2\)。因此只保留这整个零残差切片和图上零值性质仍不足以识别 PPA 吸引。两张完整二变量间隙函数并未被断言相同。

非势型正例取 \(F(t,n)=(0,Kn)\)，\(n\in\mathbb R^2\)，\(K=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\)。它全对单调，斜对称部分非零，故无法写成凸函数的全次梯度图。此时 \(g_a(t,n)=\|n\|^2/(2a)\) 对任意 \(a>0\) 成立。原 PPA 由 \(\|(I+\lambda K)n\|^2=(1+\lambda^2)\|n\|^2\) 收缩，切向固定。一般全对单调图上，若增长在每个相关输出推出 \(d(y,S)\le K_0r_F(y)\)，则对每个原根 \(z=y+\lambda v\) 和每个 \(p\in P_S(z)\)，只要 \((y,v),(p,0)\) 位于同一单调图块，就有
\[
 d(z,S)^2\ge d(y,S)^2+\lambda^2\|v\|^2
  \ge(1+\lambda^2/K_0^2)d(y,S)^2,
  \qquad \lambda\|v\|\le d(z,S).
\]
若另有同窗覆盖及初值长度预算，则标准几何步长和给出原空间有限长度。这个收敛分支是经典单调路线，桥接贡献只在于同一原图函数的两个切片。

<a id="gap-next"></a>
## 向一般非线性 RLEB 延拓的试证门

将二次惩罚换成从原图导出的非负 \(\Pi(z,y)\) 时，同一步见证只给
\(g_\Pi(z)\ge\lambda\|v\|^2-\Pi(z,y)\)。若 \(\Pi(z,y)=C\|z-y\|^q\)、\(C>0,\ 0<q<2\)，在小非零步上两项的比值为 \(C\lambda^{q-1}\|v\|^{q-2}\to\infty\)。负下界排除该见证直接提供正二次增长，其他竞争图点仍可能给增长。下一门是从原图提取沿同一近端弦仍保留正余额的惩罚，或构造一个显出较弱信息不足的反例。验证对象包括非孤立目标、非势算子、完整真残差和所有原根。
