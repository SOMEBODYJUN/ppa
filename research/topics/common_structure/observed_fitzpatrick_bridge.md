# 观察复合图的 Fitzpatrick 母结构与残差传递

本文记录一条只在固定观察坐标上成立的窄桥。它把参考最大单调图的移位 Fitzpatrick 间隙、复合原图的真实残差和近端弦上的方向功放在同一个公式中。它不把一般有界可逆的复合核误认为保持原空间单调性。

## 1. 对象与母结构

令 \(X=\mathbb R^n\)、\(Z=\mathbb R^m\)，\(C:X\to Z\) 为满射线性映射，\(T:Z\rightrightarrows Z\) 为最大单调图，
\[
 Z_0=T^{-1}(0)\ne\varnothing,
 \qquad
 F(y)=B(y)T(Cy).
\]

在一个完整活跃纤维 \(\mathcal A\subset X\) 上，假设 \(B(y):Z\to X\) 满列秩并有统一界
\[
 b_-\|w\|\leq\|B(y)w\|\leq b_+\|w\|,
 \qquad y\in\mathcal A,\ w\in Z,
 \tag{B-bounds}
\]
其中 \(0<b_-\leq b_+<\infty\)。写
\[
 c_-:=\sigma_{\min}^+(C)>0,
 \qquad c_+:=\|C\|,
 \qquad Q_y:=CB(y).
\]

对 \(a\geq0\) 定义参考图的移位间隙
\[
 \mathsf M_a(z,u)
 :=\sup_{(z',u')\in\operatorname{gph}T}
 \left\{\langle z-z',u'-u\rangle-
 \frac a2\|z-z'\|^2\right\}.
 \tag{M}
\]
上确界允许为 \(+\infty\)。这是同一变分对象的两个截面
\[
 \mathsf M_a\big|_{\operatorname{gph}T},
 \qquad
 m_a(z):=\mathsf M_a(z,0).
\]

若把 \(v=B(y)w\) 代回去，也可在原图上写成
\[
 \widehat{\mathsf M}_a(y,v)
 :=\mathsf M_a\big(Cy,B(y)^\dagger v\big),
 \qquad (y,v)\in\operatorname{gph}F,
 \tag{M-lift}
\]
其中 \(B(y)^\dagger B(y)=I_Z\)。该提升只改变坐标，不改变 \(M\) 的参考图含义。

令 \(T_a:=T+\frac a2 I_Z\)，记其 Fitzpatrick 函数为 \(\Phi_{T_a}\)。直接展开定义得到
\[
 \mathsf M_a(z,u)
 =\Phi_{T_a}\!\left(z,u+\frac a2 z\right)
  -\left\langle z,u+\frac a2 z\right\rangle.
 \tag{Fitzpatrick-shift}
\]
所以 \(M\) 不是把单调性和正则性并列编码的合取，而是同一个移位图的 Fenchel--Young 型间隙。图截面和零残差截面只是这个间隙在不同坐标超平面上的限制。

## 2. 图截面与正则截面的精确含义

### 2.1 图截面

对任意 \(a\geq0\)，
\[
 \mathsf M_a(z,u)=0
 \quad\text{对所有 }(z,u)\in\operatorname{gph}T
\]
当且仅当
\[
 \langle z-z',u-u'\rangle\geq-\frac a2\|z-z'\|^2
\]
对图块中的所有两点成立。也就是说，\(M_a\) 的图截面精确表示 \(a/2\)-弱单调性，\(a=0\) 时这正是普通单调性。若已知 \(T\) 是 \(\beta\)-弱单调且 \(a\geq2\beta\)，则该截面确实为零，但在 \(a>2\beta\) 时不能反向恢复原来的 \(\beta\) 常数。这个断言只涉及参考图的全对量词，不要求 \(T\) 的极大性来证明零值等价。

若 \(B=C^*\)，则 \(F=C^*TC\) 在同一图块上继承单调性，因为
\[
 \langle B(y)w-B(y')w',y-y'\rangle
 =\langle w-w',C(y-y')\rangle\geq0.
 \tag{alignment}
\]

更一般地，若图对满足对某个 \(\delta\geq0\) 的对齐缺口估计
\[
 \left|
 \langle B(y)w-B(y')w',y-y'\rangle
 -\langle w-w',C(y-y')\rangle
 \right|
 \leq\delta\|y-y'\|^2,
 \tag{alignment-defect}
\]
则 (H_{\rm mon}) 给出原图的
\[
 \langle v-v',y-y'\rangle
 \geq-(\beta c_+^2+\delta)\|y-y'\|^2.
 \tag{F-hypomon}
\]
因此，单调性的传递需要对齐条件或同等强度的结构。仅有 (B-bounds) 不足。

### 2.2 零残差截面

因为 \(B(y)\) 满列秩，
\[
 S:=F^{-1}(0)=C^{-1}(Z_0).
 \tag{zero-set}
\]
对 \(d_T(z):=\operatorname{dist}(z,Z_0)\) 和 \(d_S(y):=\operatorname{dist}(y,S)\)，伪逆给出
\[
 c_+^{-1}d_T(Cy)\leq d_S(y)\leq c_-^{-1}d_T(Cy).
 \tag{distance-transfer}
\]
真实残差
\[
 r_T(z):=\inf_{u\in T(z)}\|u\|,
 \qquad
 r_F(y):=\inf_{v\in F(y)}\|v\|
\]
满足
\[
 b_-r_T(Cy)\leq r_F(y)\leq b_+r_T(Cy).
 \tag{residual-transfer}
\]
所以在同一活跃纤维上，参考图的线性或幂次误差界和原图的误差界双向传递。特别地，若
\[
 d_T(Cy)\leq K_T r_T(Cy)^q,
 \qquad q>0,
\]
则
\[
 d_S(y)\leq c_-^{-1}K_T b_-^{-q}r_F(y)^q.
 \tag{EB-forward}
\]
反向若 \(d_S(y)\leq K_F r_F(y)^q\)，则
\[
 d_T(Cy)\leq c_+K_F b_+^q r_T(Cy)^q.
 \tag{EB-backward}
\]
这些常数只用满射观察和完整纤维上下界，不要求 \(B\) 连续，也不把某个选定的局部根误当成完整零集。

## 3. 近端弦上的方向功

取一个原近端根
\[
 x=y+\lambda B(y)w,
 \qquad w\in T(Cy).
 \tag{prox-chord}
\]
把图点 \((Cy,w)\) 作为 \(M\) 的竞争点，得到精确见证
\[
 \mathsf M_a(Cx,0)
 \geq
 \lambda\langle Q_yw,w\rangle-
 \frac{a\lambda^2}{2}\|Q_yw\|^2.
 \tag{directional-witness}
\]
这就是 \(CB(y)\) 在同一近端弦上的方向功。若在完整活跃纤维上
\[
 \operatorname{sym}Q_y\succeq\mu I_Z,
 \qquad \|Q_y\|\leq q_+,
 \tag{Q-sector}
\]
并且 \(a\lambda q_+^2<2\mu\)，则
\[
 \mathsf M_a(Cx,0)
 \geq \lambda\left(\mu-\frac{a\lambda q_+^2}{2}\right)\|w\|^2.
 \tag{positive-witness}
\]
若输出窗口中的每个参考图值满足
\[
 d_T(Cy,Z_0)\leq K_T\|w\|,
\]
则
\[
 d_T(Cx,Z_0)\leq(K_T+\lambda q_+)\|w\|
\]
并且
\[
 \mathsf M_a(Cx,0)
 \geq
 \frac{\lambda(\mu-a\lambda q_+^2/2)}{(K_T+\lambda q_+)^2}
 d_T(Cx,Z_0)^2.
 \tag{bridge-growth}
\]
用 (distance-transfer) 还得到原零集版本
\[
 \mathsf M_a(Cx,0)
 \geq
 \frac{c_-^2\lambda(\mu-a\lambda q_+^2/2)}{(K_T+\lambda q_+)^2}
 d_S(x)^2.
 \tag{bridge-growth-S}
\]
这条估计把 \(M\) 的残差截面和实际 PPA 输入连接起来。它在 \(m_a\) 的一般二次增长之外，保留了原近端弦的方向信息。

为了得到 Fejér 型的观测距离估计，还需控制
\[
 \langle Q_yw,C(y-p)\rangle,
 \qquad p\in S.
 \tag{chord-power}
\]
参考单调性只给
\[
 \langle w,C(y-p)\rangle\geq0.
\]
它在 \(Q_y=\rho_yI\)、\(\rho_y\geq0\) 时直接传递。更一般地可假设 \(T\) 对 \(Q_y\) 的定向单调性，或直接要求
\[
 \langle Q_yw,C(y-p)\rangle
 \geq\nu\langle w,C(y-p)\rangle-
 \varepsilon\|w\|\,\|C(y-p)\|.
 \tag{angle-transfer}
\]
没有这项，(Q-sector) 只控制 \(w\) 自身的功，不能控制其与目标方向的交叉项。

## 4. 反例与边界

令 \(C=I\)、\(T=I\)、\(Z_0=S=\{0\}\)。所有下列例子有相同的参考间隙 \(M_a\)、相同的零集和相同的精确残差界。

* \(B=-I\)。此时 \(F=-I\)，而
  \[
  J_{\lambda F}(x)=\frac{x}{1-\lambda},
  \qquad 0<\lambda<1,
  \]
  是扩张。\(Q=-I\) 的方向功为负，(positive-witness) 的门不能成立。
* \(B=J\) 为二维九十度旋转。此时 \(F=J\) 仍单调但非循环梯度，且
  \[
  \|J_{\lambda F}(x)\|=(1+\lambda^2)^{-1/2}\|x\|.
  \]
  这里 \(\operatorname{sym}Q=0\)，说明正扇区是充分条件而非必要条件。
* \(B=\operatorname{diag}(1,-1)\)。一个方向收缩，另一个方向扩张。它说明残差和零集传递不能替代方向性条件。

因此，仅保留 \(M\) 的图零值和 \(m_a\) 的零残差增长，无法区分同一参考图经过不同有界可逆核后的原 PPA 动力学。C322 的通信谱中位置输运造成的一阶交叉项正属于 (chord-power) 所保留的信息，不能由标量残差截面恢复。

## 5. 精确范围与下一义务

这条桥已经证明了三件事。第一，\(M\) 的图截面在对齐缺口可控时给原图的弱单调性。第二，\(M\) 的零残差截面在完整满射纤维上与原零集的真实误差界双向等价。第三，\(CB(y)\) 在同一近端弦上的定向功给出一个可计算的 \(M\)-增长常数。

尚未证明的是仅由 (Q-sector) 和参考图的单调性推出原空间每个完整近端根的点收敛。必须补充 (chord-power) 的目标方向估计、所有根的共同观察窗口以及原空间到观测空间的留域控制。若这些条件不能在自然模型中验证，\(B=-I\) 与 C322 型位置输运反例说明缺口是结构性的。

## 6. 对齐子类中的完整 PPA 桥

上面的对象在 \(B(y)=\rho C^*\)、\(\rho>0\) 的对齐子类上还给出一个直接的收缩定理。先取 \(T\) 单调（即 \(\beta=0\)），并假设零残差截面在相关窗口满足
\[
 d_T(Cy,Z_0)\leq K_T r_T(Cy).
 \tag{T-EB}
\]
则 \(F=\rho C^*TC\) 是最大单调图。最大性可直接由 Minty 判据检查。若 \((y,v)\) 与 \(\operatorname{gph}F\) 单调相关，沿 \(\ker C\) 的平移先迫使 \(v\in\operatorname{ran}C^*\)，再由 \(C\) 满射把关系降到 \(T\) 的图上。

对任意原近端根
\[
 x=y+\lambda\rho C^*w,
 \qquad w\in T(Cy),
 \tag{aligned-root}
\]
以及任意 \(p\in S\)，单调性与 \(Cp\in Z_0\) 给出
\[
 \langle C^*w,y-p\rangle=\langle w,Cy-Cp\rangle\geq0.
\]
因此欧氏平方恒等式、(T-EB) 和 \(\|C^*w\|\geq c_-\|w\|\) 给出
\[
 \begin{aligned}
 \|x-p\|^2
 &\geq d_S(y)^2+\lambda^2\rho^2\|C^*w\|^2,\\
 d_S(y)&\leq K_F r_F(y)\leq K_F\rho\|C^*w\|,
 \end{aligned}
\]
其中
\[
 K_F=\frac{K_T}{\rho c_-^2}
\]
由 (EB-forward) 得到。取 \(p\in P_S(x)\)（在这个最大单调子类中 \(S\) 为闭凸集，投影唯一），则 \(\|x-p\|=d_S(x)\) 且 \(\|y-p\|\geq d_S(y)\)，得到对每个完整根
\[
 d_S(y)\leq \kappa d_S(x),
 \qquad
 \kappa=\left(1+\frac{\lambda^2}{K_F^2}\right)^{-1/2}<1.
 \tag{A-bridge}
\]
这里 \(M\) 的图截面提供单调性的交叉项符号，\(m_a\) 的增长截面提供 \(K_F\)，同一个近端平方恒等式把两者接成 (A)。在最大单调对齐子类上，完整预解式是单值的，且经典坚固性给出
\[
 \|x-y\|^2+\|y-p\|^2\leq\|x-p\|^2,
 \qquad p\in S.
 \tag{firm}
\]
故 \(\|x-y\|\leq d_S(x)\)。迭代留在给定窗口时，(A-bridge) 使距离几何衰减，(firm) 使绝对步长和有限，点列收敛到 \(S\)。若只假设 \(\beta\)-弱单调，交叉项不能直接用 \(d_S(y)\) 控制，因为 \(p\) 是输入 \(x\) 的最近零点。若另有一个根一致的锚输运常数 \(L\) 满足
\[
 \|y-p\|\leq L\,d_S(y),
 \qquad p\in P_S(x),
 \tag{AT}
\]
则
\[
 \langle C^*w,y-p\rangle\geq-\beta c_+^2L^2d_S(y)^2.
\]
这时平方恒等式与 \(d_S(y)\leq K_F\|\rho C^*w\|\) 给出
\[
 d_S(x)^2\geq
 \left(1-2\lambda\rho\beta c_+^2L^2+\frac{\lambda^2}{K_F^2}\right)d_S(y)^2.
\]
严格收缩的这个方向需要
\[
 \lambda>2\rho\beta c_+^2L^2K_F^2.
\]
没有 (AT)，负交叉项含有 \(\|y-p\|\) 而不是 \(d_S(y)\)，所以不能把弱单调情形延伸到这个门。标量 \(F=-I\) 说明缺少锚输运时同一残差界可产生扩张。

## 7. 观测间隙看不见的切向输运

同一框架还有一个与 C322 位置输运相同的线性障碍。取
\[
 X=\mathbb R^2,
 \quad C(a,n)=n,
 \quad T=I_{\mathbb R},
 \quad B_\ell w=(\ell w,w).
\]
于是
\[
 F_\ell(a,n)=(\ell n,n),
 \quad S=\mathbb R\times\{0\},
 \quad d_S(a,n)=|n|,
 \quad r_{F_\ell}(a,n)=\sqrt{1+\ell^2}|n|.
\]
所有 \(\ell\) 共享同一个参考间隙 \(M_a\)，而且 \(CB_\ell=1\)，所以 (directional-witness) 的观测方向功完全相同。对输入 \(x=(a_x,n_x)\)，原 PPA 输出满足
\[
 n_y=\frac{n_x}{1+\lambda},
 \qquad
 a_y=a_x-\lambda\ell n_y.
\]
距离因子始终为 \((1+\lambda)^{-1}\)，但实际位移为
\[
 \|x-y\|=\lambda\sqrt{1+\ell^2}|n_y|.
\]
因此 \(M\) 及 \(CB\) 的法向信息不能单独控制原空间的步长和有限长度。需要在活跃纤维上保留 \(B\) 的全向上界，或加入 C322 型位置输运的额外谱/预算。这个例子还说明，残差到零集的双向传递与 PPA 的点列收敛、有限长度属于不同层次的结论。



## 8. C314 四周期在复合类中的精确嵌入

取 \(X=Z=\mathbb R^2\)、\(C=I\)、\(T=I\)，令 \(Q\) 为逆时针九十度旋转并置
\[
 B=Q^\top-I,
 \qquad F(y)=B y.
\]
因为 \(Q^\top-I\) 的两个奇异值均为 \(\sqrt2\)，它满足完整活跃纤维的上下界。零集为 \(S=\{0\}\)，且
\[
 r_F(y)=\sqrt2\,\|y\|,
 \qquad d_S(y)=\|y\|.
\]
参考图仍是 \(T=I\)，所以 \(\mathsf M_a\) 的两个参考截面与收缩模型完全相同。可是
\[
 I+F=Q^\top,
 \qquad
 J_F=Q
\]
在 \(\lambda=1\) 时成立，非零轨道是四周期。此时
\[
 \operatorname{sym}(CB)=\operatorname{sym}(Q^\top-I)=-I,
\]
所以 (positive-witness) 和任意正扇区型方向功均失败。这个例子把 C314 的“全图 RL 而无正耗散”阻碍放进 \(F=B T(Cy)\) 类，说明残差/零集传递和参考图的单调性不能单独排除周期。只有对齐条件、锚输运或直接的原近端方向功才能阻止它。


对任意图点差 \(\Delta y\)，有
\[
 \Delta y+\Delta v=Q^\top\Delta y,\qquad
 \Delta y-\Delta v=(2I-Q^\top)\Delta y.
\]
前者范数为 \(\|\Delta y\|\)，后者范数为 \(\sqrt5\|\Delta y\|\)，故该完整图满足全域 \(\mathrm{RL}(1,1,\sqrt5)\)。这正是仅凭全图 RL 不能产生正耗散的四周期阻碍。



## 9. 固定度量下的单一母间隙

当标准参考坐标的根覆盖被 \(CB\) 改变时，可以把同一间隙直接放回原图，并吸收一个固定的 SPD 度量。令 \(P=P^\top\succ0\)，
\[
 m_P I\preceq P\preceq M_P I,
 \qquad
 \langle h,k\rangle_P:=\langle Ph,k\rangle,
 \qquad
 \|h\|_P^2:=\langle Ph,h\rangle.
\]
对原图定义
\[
 \mathsf M^P_a(x,u)
 :=\sup_{(y,v)\in\operatorname{gph}F}
 \left\{\langle x-y,v-u\rangle_P-
 \frac a2\|x-y\|_P^2\right\}.
 \tag{M-P}
\]
令
\[
 \widetilde F(\tilde x):=
 P^{1/2}F(P^{-1/2}\tilde x).
\]
则 \(\mathsf M^P_a(x,u)\) 正好是普通欧氏间隙
\[
 \mathcal G^{\widetilde F}_a(P^{1/2}x,P^{1/2}u)
\]
在等距坐标下的拉回。这说明 \(P\) 改变的是图的内积表示，原始 PPA 的向量方程不变。其图截面零值等价于
\[
 \langle x-y,u-v\rangle_P\geq-\frac a2\|x-y\|_P^2,
\]
即 \(F\) 的 \(P\)-弱单调性。令
\[
 r_{P,F}(x):=\inf_{v\in F(x)}\|v\|_P,
 \qquad
 d_{P,S}(x):=\operatorname{dist}_P(x,S).
\]
若该图块满足 \(P\)-弱单调常数 \(\beta_P\)，\(a>2\beta_P\)，则
\[
 m^P_a(x):=\mathsf M^P_a(x,0)
 \leq \frac{r_{P,F}(x)^2}{2(a-2\beta_P)}.
 \tag{M-P-upper}
\]
所以在窗口上 \(m^P_a\geq\gamma d_{P,S}^2\) 蕴含
\[
 d_{P,S}(x)\leq K_P r_{P,F}(x),
 \qquad
 K_P=[2\gamma(a-2\beta_P)]^{-1/2}.
\]
反向若每个窗口输入 \(x\) 有一个完整根 \(x=y+\lambda v\) 且 \(a\lambda<2\)，则
\[
 m^P_a(x)
 \geq\lambda\left(1-\frac{a\lambda}{2}\right)\|v\|_P^2.
\]
结合 \(d_{P,S}(x)\leq(\lambda+K_P)\|v\|_P\)，得到同一窗口的二次增长，常数为
\[
 \frac{\lambda(1-a\lambda/2)}{(\lambda+K_P)^2}.
 \tag{M-P-lower}
\]
这里的反向箭头使用的是原图的完整 PPA coverage，所以不需要 \(CB=I\)。

对复合图，固定 \(B\) 并假设
\[
 P B=C^*.
 \tag{metric-alignment}
\]
则 \(B=P^{-1}C^*\) 满列秩，\(Q:=CB=CP^{-1}C^*\succ0\)，且
\[
 \|Bw\|_P^2=\langle Qw,w\rangle.
 \tag{Q-power}
\]
对 \(v=Bw\)、\(v'=Bw'\) 有
\[
 \langle y-y',v-v'\rangle_P
 =\langle C(y-y'),w-w'\rangle.
\]
因为 \(C\) 满射，\(T\) 单调当且仅当 \(F\) \(P\)-单调。于是 \(M^P_0\) 的图截面是这两个命题的等价表示，而 (Q-power) 把原近端弦上的 \(CB\) 定向自功写进同一 \(M^P\) 见证。

同样的 \(Q\) 给出完整纤维的精确传递。令
\[
 q_-:=\lambda_{\min}(Q),\qquad q_+:=\lambda_{\max}(Q).
\]
则
\[
 q_+^{-1/2}d_T(Cy)\leq d_{P,S}(y)\leq q_-^{-1/2}d_T(Cy),
\]
以及
\[
 \sqrt{q_-}\,r_T(Cy)\leq r_{P,F}(y)\leq\sqrt{q_+}\,r_T(Cy).
\]
因此 \(d_T\leq K_T r_T\) 当且仅当 \(d_{P,S}\leq K_P r_{P,F}\)，其中可取
\[
 K_P=\frac{K_T}{q_-},
 \qquad
 K_T=q_+K_P.
 \tag{metric-transfer}
\]

在 \(T\) 单调并满足这个 EB 的窗口内，任意原近端根
\[
 x=y+\lambda Bw
\]
和任意 \(p\in S\) 满足
\[
 \langle y-p,Bw\rangle_P
 =\langle C(y-p),w\rangle\geq0.
\]
取 \(p\in P_S(x)\) 并用 \(d_{P,S}(y)\leq K_P\|Bw\|_P\)，得到
\[
 d_{P,S}(y)\leq
 \left(1+\frac{\lambda^2}{K_P^2}\right)^{-1/2}d_{P,S}(x).
 \tag{M-P-A}
\]
在 \(P\)-范数中，(M-P-A) 给出几何距离衰减，完整最大
\(P\)-单调图的 \(P\)-firmness 给出
\(\|x-y\|_P\le d_{P,S}(x)\)，从而留域、有限长度和 \(P\)-范数点收敛。
有限维范数等价随后给出原欧氏距离趋零、欧氏有限长度和欧氏点收敛。
若还要把同一个 \(\kappa_P\) 作为欧氏 \(A\) 的因子，则需额外门
\(\kappa_P\sqrt{M_P/m_P}<1\)。\(C=B=I\) 时 \(P=I\)、\(Q=I\)，这条度量间隙退化为普通欧氏 Fitzpatrick 间隙。

