# DD2 在约化 PPPA 中的传递与影子恢复

固定实 Hilbert 空间 \(\mathcal H\) 与有界、自伴、半正定、非零且有闭值域的预条件算子 \(P\)。设 \(\mathcal R=\operatorname{ran}P\)，\(\mathcal N=\ker P\)，\(P_{\mathcal R}=P|_{\mathcal R}\)，\(C=\iota_{\mathcal R}P_{\mathcal R}^{1/2}\)，因此 \(P=CC^*\)、\(C:\mathcal R\to\mathcal R\subset\mathcal H\) 是同构而 \(C^*=P_{\mathcal R}^{1/2}\Pi_{\mathcal R}\) 是满射。设 \(M_C=\|C\|\)、\(m_C=\|C^{-1}\|^{-1}>0\)，其中逆仅作用在 \(\mathcal R\)。定义

\[
 A_{\mathcal R}(y)=A(y)\cap\mathcal R,\qquad Z=\operatorname{zer}A=\operatorname{zer}A_{\mathcal R},\qquad
 \mathscr H(z)=(P+A)^{-1}Cz.
\]

\(A\) 可以多值，\(\mathscr H\) 只需在约定的允许输入窗非空。记 \(G=(C^*A^{-1}C)^{-1}\)、\(F=\operatorname{Id}-J_G\)、\(Z_r=C^*Z\)。对一个物理影子 \(y\in\mathscr H(z)\)，记 \(w=C^*y\)、\(q=z-w\)。全图有

\[
 q\in F(z)\quad\Longleftrightarrow\quad q\in G(z-q)
 \quad\Longleftrightarrow\quad
 \exists y\ [C^*y=z-q,\ Cq\in A_{\mathcal R}(y)].\tag{1}
\]

最后一个量词中的所有 \(y\) 都在 \(\mathscr H(z)\)。\(C^*\mathscr H=J_G\)、\(F=J_{G^{-1}}\) 以及 \(\operatorname{zer}F=\operatorname{zer}G=Z_r\)。对物理 PPPA 输入 \(x\) 有 \(z=C^*x\)，松弛步是 \(z^+=z-\alpha q\)。这些是 Alcantara v1 Propositions 4.1–4.2 及式 (27) 的结论。文中第 4 节的轨道定理采用完整定义域。这里 (1) 的等式无需该前提，DD2 轨道需要单独核局部覆盖与留域。

## 锚定条件与最近点

取非空 \(S^*\subseteq Z\)，令 \(S=C^*S^*\)，定义 \(d_P(y,S^*)=\inf_{x_*\in S^*}\|C^*(y-x_*)\|=d(C^*y,S)\)。对每条测试边 \((z,q)\)，要求存在 \(p\in P_S(z)\)。等价地，每个原输入 lift \(x\) 都有某个 \(P\)-最近的 \(x_*\in S^*\)。任意一个 \(p\) 的所有 \(S^*\) 中的 lift 都是 \(P\)-最近锚。若对允许物理步 \((x,y)\) 存在这样的锚满足

\[
 \langle P(x-y),y-x_*\rangle\ge\Phi(d_P(x,S^*)),
\tag{2}
\]

则该边满足 DD2 的约化锚定条件 \(\langle q,w-p\rangle\ge\Phi(d(z,S))\)，因为两侧内积精确相等。反向同样成立，且固定 \((z,q)\) 时内积与影子在同一纤维内的选取无关。任意一条符合 (2) 的物理边即可认证相应约化边。要认证完整 \(F\) 纤维，需对其每个 \(q\) 保证这种认证。普通范数下的最近锚不能在这里直接代换。例如 \(P=\operatorname{diag}(1,0)\)、输入为原点、候选锚为 \((0,2),(1,0)\) 时，两种最近锚不同。

原图上的一条额外充分条件如下。若在指定物理测试窗内，对每个 \(x_*\in S^*\) 和所测 \((y,a)\in\operatorname{gra}A_{\mathcal R}\) 有 \(\langle a,y-x_*\rangle\ge-D_0(\|y-x_*\|)\)，其中 \(D_0\) 非降，且相应影子有相对于每个这样的 \(x_*\) 的恢复估计 \(\|y-x_*\|\le K\|z-C^*x_*\|\)，则在找到约化最近锚后可用缺陷 \(D(t)=D_0(Kt)\)。这给出从原范数输出缺陷到约化输入缺陷的一个充分条件。对于形如 (2) 的 \(P\)-输入假设，传递本身是等距重写。Alcantara 的 Lemma 4.3 从全指定零锚的二次 \((U,V)\) 不等式推导矩阵下界。它没有给出任意 \(\Phi\) 或真残差误差界。

最近锚的存在和目标闭性需要分别检查。有限维的非空闭 \(S\) 有最近点。Hilbert 空间里非空弱闭 \(S\) 也有最近点，证明是从有界极小化序列抽弱收敛子列并用范数弱下半连续。仅范数闭不足。例如在 \(\ell^2\)，集合 \(\{(1+1/n)e_n:n\ge1\}\) 范数闭，距零点为 1，无点达到。若只需能量估计，可改用一列近似锚 \(p_j\in S\) 且 \(\|z-p_j\|\to d(z,S)\)、\(\liminf_j\langle q,w-p_j\rangle\ge\Phi(d(z,S))\)。这一条件可以直接在平方展开中取极限。

即使 \(A\) 在有限维连续且 \(\mathscr H\) 处处非空，零集的投影也可能不闭。例如 \(P=\operatorname{diag}(1,0)\)，\(A(u,v)=(1-uv,0)\)。零集是闭双曲线 \(uv=1\)，投影是 \(\mathbb R\setminus\{0\}\)，而任意输入 \(z=s\) 的影子至少有 \((s-1,0)\)。后文给出处处唯一影子且 DD2 轨道发生投影误识别的闭图实例。

<a id="dd2-pppa-gauges"></a>
## 真残差与一般函数误差界

记 \(r_B(a)=\inf_{b\in B(a)}\|b\|\)，空值时取 \(+\infty\)。误差界写在算子定义域上。设 \(r^C_{A_{\mathcal R}}(y)=\inf_{a\in A_{\mathcal R}(y)}\|C^{-1}a\|\)。由 (1) 在完整纤维上有精确公式

\[
 r_G(w)=\inf_{C^*y=w}r^C_{A_{\mathcal R}}(y),\qquad
 m_C r_G(w)\le \inf_{C^*y=w}r_{A_{\mathcal R}}(y)\le M_C r_G(w).
\tag{3}
\]

逐边仅有 \(r_A(y)\le r_{A_{\mathcal R}}(y)\le\|Cq\|\le M_C\|q\|\)。实际 \(\|q\|\) 在输出点 \(w\) 上是 \(G\) 的一个图值范数，在输入点 \(z\) 上是 \(F\) 的一个图值范数。两处都可能远大于相应真残差。

令 \(\psi\) 是连续、非降、在零点消失的函数。全图上的等价与充分箭头如下。

| 假设 | 推出 |
| --- | --- |
| \(d_P(y,S^*)\le\psi(r_A(y))\) | 同一个 \(\psi\) 的 \(A_{\mathcal R}\) 误差界 |
| \(d_P(y,S^*)\le\psi(r_{A_{\mathcal R}}(y))\) | \(d(w,S)\le\psi(M_C r_G(w))\) |
| \(d(y,S^*)\le\psi(r_{A_{\mathcal R}}(y))\) | \(d(w,S)\le M_C\psi(M_C r_G(w))\) |
| \(d_P(y,S^*)\le\psi(r^C_{A_{\mathcal R}}(y))\) | 等价于 \(d(w,S)\le\psi(r_G(w))\) |
| \(d(w,S)\le\psi(r_G(w))\) | \(d(z,S)\le(\psi+\mathrm{id})(r_F(z))\) |
| \(d(z,S)\le\psi(r_F(z))\) | \(d(w,S)\le(\psi+\mathrm{id})(r_G(w))\) |

第一行用值域包含。第二至四行用 (3) 及 \(d_P(y,S^*)\le M_C d(y,S^*)\)，对逼近 infimum 的序列取极限。最后两行对任意边先用 \(|d(z,S)-d(w,S)|\le\|q\|\) 及真残差不超过 \(\|q\|\)，再在相应输入或输出的全图值上取 infimum。由 (3)，倒推投影 \(A_{\mathcal R}\) 误差界的常数可取 \(d_P(y,S^*)\le\psi(m_C^{-1}r_{A_{\mathcal R}}(y))\)，但倒推不控制原范数距离。所有这些箭头使用同一目标。若入口误差界仅对全零集 \(Z\) 而 DD2 针对 \(S^*\)，则至少要核 \(C^*S^*=C^*Z\) 或本窗内两者距离的定量比较。例如 \(G\equiv0\) 使全零集误差界恒成立，却无法推出针对单点 \(S\) 的误差界。

在锚点 \(z_*=C^*x_*\in S\) 附近，上表的 \(F\leftrightarrow G\) 箭头仍成立。先取小阈值 \(\delta>0\)，使 \(\psi(\delta)+\delta>0\)。小 \(\|q\|<\delta\) 时 \(w\) 与 \(z\) 之差小，两点进入对应的误差界窗。大 \(\|q\|\ge\delta\) 时，将所估计点缩至距 \(z_*\) 小于 \(\psi(\delta)+\delta\) 的球内，就得到同一个 gauge 的不等式。最后对全部 \(q\) 取 infimum。\(+\mathrm{id}\) 的线性项一般不可省。对 \(G(w)=a w\)，\(a>0\)，最小线性常数在 \(G\) 上为 \(1/a\)，在 \(F\) 上为 \(1/a+1\)。对 \(G(w)=-a w\)，\(0<a<1\)，两者顺序反转，常数仍相差 1。对于局部 Hölder 指数 \(0<\beta<1\)，\(+\mathrm{id}\) 可以吸收进 Hölder 常数。

**局部原空间入口。** 在 \(x_*\) 的某个原空间窗内假设第二行或第三行的入口误差界。记 \(\psi_G(s)=\psi(M_Cs)\) 或 \(\psi_G(s)=M_C\psi(M_Cs)\)。若对每个充分近 \(z_*\) 的 \(z\) 和每个充分小的全图值 \(q\in F(z)\)，至少有一个满足 (1) 的 lift 落在该物理窗内，则每条这样的边都满足

\[
 d(z-q,S)\le\psi_G(\|q\|).\tag{4}
\]

若局部恢复估计 \(\|y-x_*\|\le K\|z-z_*\|\) 对输入球中的所有影子成立，充分缩窗后 (4) 对该输入球的所有边成立。若只覆盖小 \(q\)，在 DD2 中可用锚定的不等式 \(\|q\|\le B_D(d(z,S))\) 与 \(D(t)\to0\) 保证所需步落入该小残差窗。这里 \(B_D(t)=(t+\sqrt{t^2+4D(t)})/2\)，由 \(\langle q,z-p\rangle-\|q\|^2\ge-D(t)\) 和 Cauchy–Schwarz 得到。

若 \(\psi_G\) 在小正阈值处正，(4) 仍推出局部完整的真残差误差界 \(\psi_G\) 对 \(G\) 及 \(\psi_G+\mathrm{id}\) 对 \(F\)。固定覆盖小残差的 \(\delta>0\)，对 \(G\) 的输出点缩球，使 \(w+q\) 落入 (4) 的输入窗或在大残差情形用 \(d(w,S)\le\|w-z_*\|\le\psi_G(\delta)\)。对 \(F\) 在小残差情形用平方外的距离三角式 \(d(z,S)\le d(z-q,S)+\|q\|\)，大残差情形用 \(d(z,S)\le\|z-z_*\|\)。分别对所有 \(q\) 取 infimum。以上把 Lemma 4.14 从线性模推到一般函数。原范数入口 \(\psi(s)=\chi_{\mathcal R}s\) 给出原文的 \(\chi_{\mathcal R}\|P\|\) 与 \(1+\chi_{\mathcal R}\|P\|\)。从局部仅有某些算法选择满足 (4) 的条件，不能推出完整真残差的结论。

有限维还有一个较弱的局部覆盖来源。设 \(\mathscr H\) 在 \(z_*\) 局部有界，\(A_{\mathcal R}\) 在零值外半连续，且 \(Z\cap(C^*)^{-1}(z_*)=\{x_*\}\)。则所有足够近 \(z_*\)、足够小 \(q\) 的 lift 都落入任意给定的 \(x_*\) 邻域。若失败，取一列逸出邻域的 lift，局部有界给强收敛子列，零值闭图与 \(C^*y=z-q\) 确认其极限为 \(x_*\)，矛盾。希尔伯特空间中的弱紧性只能直接给弱化版本。

**接入 DD2。** 令 \(\mathscr H_{\mathrm{ad}}(z)\subseteq\mathscr H(z)\) 为声明的允许关系。其每一输入纤维在工作窗非空，并在它诱导的每条 \((z,q)\) 上验证 (2) 和 (4)。对完整步 \(\alpha=1\)，这是 DD2 在约化 Hilbert 空间对 \(G\) 的近端步，参数为 1。一步与径向留域证明只依赖 Hilbert 恒等式、允许步最近锚和目标闭性。后两者须显式给出。幂次入口 \(\psi(s)=Ks^\beta\) 若用 \(P\)-距离，则 \(K_r=KM_C^\beta\)，若用原范数距离，则 \(K_r=KM_C^{1+\beta}\)。若缺陷为 \(M_Dt^p\)，临界 \(p=2/\beta\) 的严格门用约化常数 \(2M_D<K_r^{-2/\beta}\)。对一般非减模 \(\psi_r(s)=c_1\psi(c_2s)\)，令 \(m=\min\{1/c_2,c_1\},\,M=\max\{1/c_2,c_1\},\,\chi=(I+\psi)^{-1}\)。由 \(m(I+\psi)(c_2s)\le s+\psi_r(s)\le M(I+\psi)(c_2s)\) 得 \(\chi(t/M)/c_2\le(I+\psi_r)^{-1}(t)\le\chi(t/m)/c_2\)。因此 [C401](core.md#dd2-general-gauge) 的积分可积性在常数缩放下保持，缺陷吸收常数按新逆函数重新计算。

**逆向障碍。** 以下均可取完整图。

1. 令 \(P=\operatorname{diag}(1,0)\)，\(A(u,v)=\{(u,v),(0,u^2+|v|)\}\)。则 \(Z=\{(0,0)\}\)，\(A_{\mathcal R}(u,0)=\{(u,0)\}\)，其余 \(A_{\mathcal R}\) 值为空，影子为 \((z/2,0)\)。\(A_{\mathcal R}\) 有线性误差界，但 \(r_A(u,0)\le u^2\)，使原 \(A\) 的同一线性界失效。
2. 令 \(A(u,v)=(|u|/2+v^2,0)\)，同一个 \(P\) 且零集只有原点。\(G\) 的真残差为 \(|u|/2\)，有全局线性误差界。原空间在 \((0,v)\) 的距离为 \(|v|\)，残差为 \(v^2\)，原范数线性界失效。该影子关系全输入覆盖，因为 \(u\mapsto u+|u|/2+v^2\) 对每个固定 \(v\) 严格增且满射。
3. 令 \(G(w)=\{w,w^3\}\)。只选 \(w=z/2\) 的边时，\(d(w,\{0\})=\|q\|\)，但 \(r_G(w)=\min(|w|,|w|^3)\)，\(r_F(z)\asymp|z|^3\) 在零点附近成立。两种真实线性误差界都失败。以 \(A(u,v)=\{(u,v),(u^3,v)\}\) 和 \(P=\operatorname{diag}(1,0)\) 可得到完全相同的约化例子。
4. Alcantara Example 4.7 取 \(A(u,v)=(u/(1+v^2),0)\)。在 \((0,0)\) 周围 \(|v|<\epsilon\) 的物理窗中，\(d((u,v),Z)=|u|\le(1+\epsilon^2)r_A(u,v)\)。对任意可见 \(w\)，远端 \(v\to\infty\) 却给 \(r_G(w)=0\)。\(F(s)=\{s/(2+v^2):v\in\mathbb R\}\) 也使 \(r_F(s)=0\) 对所有输入成立。它具体显示局部物理误差界缺少近 lift 时不能传给完整纤维。原例还有如下轨道，依次取影子核坐标 \(k+1\)，则 \(s_{k+1}=s_k(1-(2+(k+1)^2)^{-1})\)，\(s_k\) 趋于正数，\(q_k\to0\)。正极限来自可和的相对下降量。此轨道没有满足统一 DD2 输出误差界，因为输出保持正距离而 \(\|q_k\|\to0\)。

<a id="dd2-pppa-recovery"></a>
## 投影识别与物理收敛

设约化 DD2 已给 \(z^k\to z_\infty\) 强收敛、\(d(z^k,S)\to0\)、\(q^k\to0\)。完整步下最后一点由有限长度直接推出。松弛步若 \(\inf_k\alpha_k>0\)，也由实际步 \(\alpha_k q^k\) 的有限长度推出。于是 \(w^k=z^k-q^k\to z_\infty\)，且 \(\Pi_{\mathcal R}x^k=P_{\mathcal R}^{-1/2}z^k\)、\(\Pi_{\mathcal R}y^k=P_{\mathcal R}^{-1/2}w^k\) 强收敛到同一点。完整步时 \(w^k=z^{k+1}\)。若 \(\alpha_k\ge a>0\)，约化影子的尾长还满足

\[
 \sum_{j\ge k}\|w^{j+1}-w^j\|\le (1+2/a)\sum_{j\ge k}\|z^{j+1}-z^j\|.
\tag{5}
\]

若 \(S\) 闭，则 \(z_\infty\in S\subseteq Z_r\)，投影识别已经完成，即使 \(A_{\mathcal R}\) 或 \(F\) 未知是否在零值 demiclosed。也无需 \(S=Z_r\)。若只知 \(S\) 的最近锚在工作窗存在，则只推出 \(z_\infty\in\overline S\)。此时在 \(z_\infty\) 处对残差趋零采用 \(F\) 闭性即可识别为 \(Z_r\)，并可用以下原空间条件获得该闭性。

Alcantara Lemma 4.8 的等价条款可由 (1) 直接读出。\(F\) 在零值 demiclosed、\(G\) 在零值 demiclosed，以及

\[
 Cq_j\in A_{\mathcal R}(y_j),\quad q_j\to0,\quad C^*y_j\rightharpoonup w
 \quad\Longrightarrow\quad w\in Z_r
\tag{6}
\]

三者等价。若所有有界的约化输入集都有有界的影子并且 \(A_{\mathcal R}\) 在零值 demiclosed，则 (6) 成立。证明把 \(y_j\) 作为 \(z_j=C^*y_j+q_j\) 的影子，用有界性抽取物理弱收敛子列，再用 \(Cq_j\to0\) 识别其零点。该全局条件还推出 \(Z_r\) 弱序列闭，因在 \(F\) 的 demiclosed 命题中取 \(q_j=0\)。它不会自动给任意更小的 \(S\) 闭性。对于同一给定轨道，只需所选 \(y^k\) 有界和 \(A_{\mathcal R}\) 在相关弱聚点零值 demiclosed，便可用同样证明识别聚点并获得至少一个物理零点 lift。

**物理弱收敛。** 若所选影子有界且 \(A_{\mathcal R}\) 在零值 demiclosed，每个弱聚点都在 \(X_\infty=Z\cap(C^*)^{-1}(z_\infty)\)，且 \(X_\infty\ne\varnothing\)。若这个零纤维为单点 \(\{x_\infty\}\)，则 \(y^k\rightharpoonup x_\infty\)。证明是若某连续线性泛函不收敛，可取其偏差有下界的子列并再取弱收敛子列得到矛盾。\(\mathscr H(z_\infty)\) 的单值性足够保证零纤维至多一元，全局 admissibility 更强。仅 \(F\) 单值不足，因为不同核分量可以诱导相同 \(q\)。若 \(\alpha_k\in[a,b]\Subset(0,2)\)，置 \(\theta=\max(|1-a|,|1-b|)<1\)。由 \(x^{k+1}=(1-\alpha_k)x^k+\alpha_k y^k\)，对任意连续线性泛函应用标量不等式 \(e_{k+1}\le\theta e_k+b\epsilon_k\) 得 \(x^k\rightharpoonup x_\infty\)。强收敛时同一论证可直接用于范数。单位步的原迭代与影子仅错一项。

这重构了 Lemma 4.9 的恢复部分。Theorem 4.10 的前件还包括 Corollary 4.4 的相对半单调性与步长条件、\(\liminf\delta_k>0\) 以及 \(C^*S^*=Z_r\)，用以得到约化弱收敛。DD2 提供约化强收敛后可以使用上面的恢复论证，无需另行假定 Theorem 4.10 的 Fejér 前件。

**物理强收敛与点率。** 若已知 \(x_\infty\in X_\infty\)，且 \(\|y-x_\infty\|\le K\|z-z_\infty\|\) 对极限输入邻域的所有影子成立，DD2 的约化尾长 \(L_k=\sum_{j\ge k}\|z^{j+1}-z^j\|\) 给出 \(\|y^k-x_\infty\|\le K L_k\)。若 \(L_k\le C\Theta(d(z^k,S))\)，也得到该势函数的点误差控制。根本条件是围绕固定零点的一点估计，所以并不要求 \(\mathscr H\) 在两个任意输入间 Lipschitz。对于松弛后的全迭代，范数误差 \(e_k=\|x^k-x_\infty\|\) 满足

\[
 e_k\le\theta^k e_0+b\sum_{j=0}^{k-1}\theta^{k-1-j}\|y^j-x_\infty\|.
\tag{7}
\]

几何卷积保留幂次上界，并将几何上界保留为 R 线性上界，具体几何因子要考虑 \(\theta\)。对任意一般函数尾势，应保留 (7)。

Theorem 4.11 在 \(A_{\mathcal R}\) 相对于所有所选零锚的 \((U,V)\)-半单调性下，用 \(U\succeq\tau P\)、\(I+C^*VC+\tau I\) 强正定、以及 \(U\) 在 \(\ker P\) 上强正定来得到该一点 Lipschitz 界。其证明将 \(y-x_*\) 分成值域和核分量。Theorem 4.12 另外假定 \(\tau>0\) 与相应的方向步长界，得到唯一投影零点，以及按步长和条件获得投影强收敛与线性率。它随后借局部 Lipschitz 恢复得到物理唯一零点和物理影子的点率。DD2 使用这些定理所提供的恢复估计时，独立验证 DD2 的约化前件。若本身已有足够的局部恢复，就可直接用这里的点率推论。

**有限维专门化。** 在 \(\mathcal H=\mathbb R^n\)，\(A_{\mathcal R}\) 的外半连续性给零值序列闭性。它可由 \(A\) 外半连续与 \(\mathcal R\) 闭直接推出。\((P+A)^{-1}P\) 在每个值域输入点局部有界等价于 \(\mathscr H\) 在每个约化点局部有界，且在有限维蕴含全局有界恢复，证明是对有界集的紧闭包取有限子覆盖。对已知范数极限的 DD2 轨道，局部有界只需在极限输入成立。结合零值外半连续，每个物理聚点在 \(X_\infty\)，单点纤维给物理范数收敛。Alcantara Corollary 4.15 另调用 Corollary 4.4 和 Proposition 4.5 建立其投影收敛。若在任意图值都有外半连续，则同一紧性论证给 \(F,G\) 的完整闭图。在有限维，若 \(S^*\) 自身闭且有有界恢复，则 \(C^*S^*\) 也闭，因为任何收敛投影序列的原零点 lift 都是对应的影子并具有物理收敛子列。

**恢复反例。**

1. 令 \(P=\operatorname{diag}(1,0)\)、\(A(u,v)=(u,v^2-1)\)。\(F(z)=z/2\) 单值，\(\mathscr H(z)=\{(z/2,1),(z/2,-1)\}\) 有界且外半连续。\(A\) 连续，约化 DD2 可用零缺陷和局部 Hölder 误差界。若交替取两个核分量，物理影子无极限。两个零点具有相同投影。
2. 令 \(\mathcal H=\mathbb R\oplus\ell^2\)，\(P(u,v)=(u,0)\)，\(\kappa(0)=0\)、\(\kappa(2^{-j})=e_j\)（\(j\ge1\)），正半轴在相邻节点间作线性插值，在最右节点外常值，在负半轴偶延拓。\(\kappa\) 有界且 \(\kappa(u)\rightharpoonup0\) 当 \(u\to0\)。其图 \(B=\{(u,\kappa(u)):u\in\mathbb R\}\) 范数闭，因为在 \(u\ne0\) 有范数连续性，在 \(u=0\) 任意存在的范数极限都必须等于弱极限 0。设连续算子 \(A(u,v)=(u,d((u,v),B)e_1)\)。若 \((u_j,v_j)\rightharpoonup(u,v)\) 且 \(A(u_j,v_j)\to0\)，则 \(u_j\to0\)，可取 \((s_j,\kappa(s_j))\in B\) 使两点之差趋于 0，故 \(s_j\to0\) 且 \(v_j\rightharpoonup0\)。这给零值 demiclosedness，\(A_{\mathcal R}\) 亦然。\(\mathscr H(z)=(z/2,\kappa(z/2))\) 全域唯一且有界恢复，唯一零点为原点。单位步由 \(z^0=1\) 出发，影子核分量为 \(e_{k+1}\)，故物理影子仅弱收敛。约化仍是满足 DD2 的几何收缩。
3. 可以在同时满足 DD2 一步条件、完整影子处处唯一及原算子连续时，出现目标不闭导致的投影误识别。令 \(P=\operatorname{diag}(1,1,0)\)，\(s_+=\max(s,0)\)，设

   \[
   A(u,w,v)=\left(\min(u_+,|w|)+\min(1,(-u)_+),\ w,\ (u-e^{-v})\big((u+1)_+^2+v^2\big)\right).
   \]

   第三个分量为零，当且仅当 \(u=e^{-v}>0\) 或 \(u\le-1,v=0\)。正支的可见输入是 \((s,t)=(u+\min(u,|w|),2w)\)，唯一覆盖 \(s>0\)。另一支给 \((s,t)=(u+1,2w)\)，唯一覆盖 \(s\le0\)。故 \(P\) admissible，且 \(S=Z_r=\{(s,0):s>0\}\)。在所有 \(s>0\) 的可见输入上，最近锚为 \((s,0)\)，位移为 \(q=(\min(u,|w|),w)\)，锚定内积为 \(w^2-\min(u,|w|)^2\ge0\)。原范围真残差在该影子处为 \(\|q\|\)，输出到 \(S\) 的距离为 \(|w|\le\|q\|\)。在小窗可用 \(s\mapsto s^\beta\) 的 DD2 gauge，其中 \(1/2<\beta<1\)。从 \(0<s_0\le t_0\) 的点出发，单位步将两个可见坐标都减半且全程 \(s>0\)。轨道留域由显式公式给出，\(q^k\to0\)，约化轨道有限长并趋于 \((0,0)\notin Z_r\)，而物理影子的核坐标 \(-\log(u)\) 发散。这里距目标趋零与最近锚的存在都成立。

<a id="dd2-pppa-length"></a>
## 物理长度及其严格边界

若所选影子沿有效尾轨满足二点估计 \(\|y^{k+1}-y^k\|\le K\|z^{k+1}-z^k\|\)，则 \(\sum_{j\ge k}\|y^{j+1}-y^j\|\le K L_k\)。局部单值 Lipschitz 恢复足够。也可直接假设沿轨的可和差分控制。Alcantara Theorem 4.11 的假设若由零锚相对半单调性加强为两个所测原图点的同一 \((U,V)\) 半单调性，原证明适用于差 \(d=z-z'\)、\(q-q'\)、\(y-y'\)。确切地，令 \(W=U-\tau P\) 且 \(H_0=I+C^*VC\)，同样得到

\[
 \|W^{1/2}(y-y')\|^2+\langle q-q',(H_0+\tau I)(q-q')\rangle
 \le (1+2\tau)\langle q-q',d\rangle-\tau\|d\|^2.
\]

强正定性与 Young 不等式控制 \(\|q-q'\|\) 和 \(\|W^{1/2}(y-y')\|\) 为 \(O(\|d\|)\)。值域分量由 \(C^*(y-y')=d-(q-q')\) 控制，核分量用 \(W\) 在核上的强正定性和三角不等式控制。于是得到二点 Lipschitz 恢复。此加强条件在完整图时还给出每个输入纤维至多一个影子。

在 \(\alpha_k\in[a,b]\Subset(0,2)\) 下，设 \(h_k=x^k-y^k\)。由 \(h_{k+1}=(1-\alpha_k)h_k+y^k-y^{k+1}\) 可得

\[
 \sum_{j\ge k}\|x^{j+1}-x^j\|\le \frac b{1-\theta}
 \left(\|h_k\|+\sum_{j\ge k}\|y^{j+1}-y^j\|\right).
\tag{8}
\]

证明先在有限前缀求和，再令前缀截断趋于无穷。所以二点控制下物理影子和物理迭代都有限长。

**锚定 Lipschitz 下的无限长度。** 在可见平面上令 \(J\) 为直角旋转，\(G(w)=\|w\|^{1/2}Jw\)。\(z=w+G(w)\) 按半径严格增，每个圆上的方位映射为固定旋转，由此全域有唯一逆 \(T\)。零锚内积恒为零，真残差 \(\|w\|^{3/2}\) 给指数 \(2/3\) 的精确输出界。单位步正半径 \(\rho_k=\|z^k\|\) 满足

\[
 \rho_k=\rho_{k+1}\sqrt{1+\rho_{k+1}},\qquad
 \rho_{k+1}^{-1}-\rho_k^{-1}
 =\frac{1-(1+\rho_{k+1})^{-1/2}}{\rho_{k+1}}\longrightarrow\frac12.
\]

故 \(\rho_k\sim2/k\)，约化增量为 \(\rho_{k+1}^{3/2}\) 并可和。给定一个正半径起点，取连续函数 \(f:[0,\infty)\to\mathbb R\) 满足 \(|f(r)|\le r\) 及 \(f(\rho_{k+1})=(-1)^k\rho_{k+1}\)。在这些节点间作线性插值、令 \(f(0)=0\)，在最大节点外常值，给出所需函数。取 \(P=\operatorname{diag}(I_2,0)\)、\(A(w,v)=(G(w),v-f(\|w\|))\)，则 \(A\) 连续，\(Z=\{0\}\)，\(\mathscr H(z)=(T(z),f(\|T(z)\|))\) 全域唯一，且 \(\|\mathscr H(z)\|\le\sqrt2\|z\|\)。原空间投影锚定零缺陷，在影子处真范围残差也是 \(\|w\|^{3/2}\)。但物理相邻影子距离至少为 \(\rho_{k+1}+\rho_{k+2}\)，全长无限。单位步使物理迭代同样无限长。

**可和点界仍可推出长度。** 若一点恢复给 \(\sum_k K L_k<\infty\)，由 \(\|y^{k+1}-y^k\|\le\|y^{k+1}-x_\infty\|+\|y^k-x_\infty\|\) 可得有限长度。C399 的幂次尾势 \(L_k=O(k^{-(2\beta-1)/(2-2\beta)})\) 在 \(\beta>3/4\) 时保证这点。更强的全锚统一 Lipschitz 恢复给出不同的充分门槛。它先给每个 \(p\in S\) 的唯一零 lift \(\ell(p)\)，并通过在 \(z=p'\) 代入 \(\ell(p')\) 得到 \(\ell\) 在 \(S\) 上 Lipschitz。对每个最近锚 \(p^k\) 有 \(\|y^k-\ell(p^k)\|\le Kd_k\)，且 \(\|p^{k+1}-p^k\|\le\|z^{k+1}-z^k\|+d_k+d_{k+1}\)。于是只要 \(\sum_k d_k<\infty\) 就有物理长度有限。C399 在 \(\beta>2/3\) 满足该门，端点 \(\beta=2/3\) 已由前例显示无法普遍保证。

**单一极限锚的 \(3/4\) 门可达。** 固定 \(1/2<\beta\le3/4\)，令 \(b=1/\beta\)、\(\nu=2b-2\)。在可见平面令

\[
 G(u,w)=(|w|^b,\operatorname{sgn}(w)|w|^{2b-1}).
\]

约化零集为水平轴 \(S\)。输入 \(z=(s,t)=(u+|w|^b,w+\operatorname{sgn}(w)|w|^{2b-1})\) 对每个 \(z\) 唯一确定输出。最近锚为 \((s,0)\)，且
\(\langle G(u,w),(u-s,w)\rangle=-|w|^{2b}+|w|^{2b}=0\)，
\(d((u,w),S)=|w|\le r_G(u,w)^\beta\)。
沿 \(t_0>0\) 的轨道，\(t_k=t_{k+1}(1+t_{k+1}^{\nu})\)，故 \(t_{k+1}^{-\nu}-t_k^{-\nu}\to\nu\) 且 \(t_k\sim(\nu k)^{-1/\nu}\)。切向步为 \(t_{k+1}^{b}\)，而 \(b/\nu>1\)。将起点的水平坐标选为 \(s_0=\sum_{j\ge0}t_{j+1}^b\)，则 \(s_\infty=0\) 且

\[
 s_k=\sum_{j\ge k}t_{j+1}^b\asymp k^{-(b/\nu-1)}.
\]

因为 \(b/\nu-1=(2-b)/(2b-2)\le1\)，\(\sum_k s_k=\infty\)。约化轨道本身有限长，因为水平步可和、竖直步望远镜可和。

在物理空间取 \(P=\operatorname{diag}(I_2,0)\) 与 \(A(u,w,v)=(G(u,w),v-f(u))\)，其中 \(f\) 连续、\(|f(u)|\le|u|\)、\(f(s_{k+1})=(-1)^ks_{k+1}\)，用前例的分段插值构造。原零点集合为 \(\{(u,0,f(u)):u\in\mathbb R\}\)，投影在 \(S\)，完整影子处处唯一。对输入 \((s,t)\) 近原点，其影子满足 \(|w|\le|t|\)、\(|u|\le |s|+|w|^b\)、\(|v|\le|u|\)。因此在极限零点 \(x_\infty=0\) 有局部锚定 Lipschitz 恢复。此轨道的物理影子增量至少为 \(s_{k+1}+s_{k+2}\)，长度发散。原算子连续，原范围残差就是上述 \(\|G(u,w)\|\)。该构造只用极限点的一点恢复，给出 \(\beta\le3/4\) 的完整反例范围。

## 证据边界

式 (1)、二次半单调性传递、弱闭图识别和一点恢复机制均来自或重构自 Alcantara。全纤维真残差公式 (3)、一般函数的误差界局部提升 (4)、已收敛轨道的有限维局部化、锚定恢复与长度分离的 DD2 反例，是本轮推导。证明不要求整个 \(F\) 全域有定义，只要 DD2 的所测关系在工作窗具覆盖。只有在全图或确证全部相关小残差边的场合，才对完整真残差作结论。弱恢复与一点 Lipschitz 恢复没有替代二点控制。本文未主张这些推导的公开优先性，也未在此验证方向自适应或具体分裂算法的 DD2 假设。

原文定位为 Jan Harold Alcantara, *Degenerate Preconditioned Proximal Point Algorithms as Forward Methods for Nonmonotone Inclusions*, arXiv:2611.20523v1，§2.2 与 §§4.1–4.6，特别是 Props. 4.1–4.2、4.5，Lemmas 4.3、4.8–4.9、4.14，Example 4.7，Theorems 4.10–4.12 及 Cor. 4.15。[版本全文](https://arxiv.org/html/2611.20523v1)
