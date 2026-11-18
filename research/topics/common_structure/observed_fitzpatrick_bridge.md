# 观察复合图的 Fitzpatrick 母结构与残差传递

本文记录一条只在固定观察坐标上成立的窄桥。它把参考最大单调图的移位 Fitzpatrick 间隙、复合原图的真实残差和近端弦上的方向功放在同一个公式中。它不把一般有界可逆的复合核误认为保持原空间单调性。

## 1. 对象与母结构

令 (X=mathbb R^n)、(Z=mathbb R^m)，(C:X	o Z) 为满射线性映射，(T:Zightrightarrows Z) 为最大单调图，

\[
 Z_0=T^{-1}(0)\ne\varnothing,
 \qquad
 F(y)=B(y)T(Cy).
\]

在一个完整活跃纤维 \(mathcal A\subset X\) 上，假设 (B(y):Z	o X) 满列秩并有统一界

\[
 b_-\|w\|\leq\|B(y)w\|\leq b_+\|w\|,
 \qquad y\in\mathcal A, w\in Z,
 \tag{B-bounds}
\]

其中 (0<b_-\leq b_+<\infty)。写

\[
 c_-:=\sigma_{min}^+(C)>0,
 \qquad c_+:=\|C\|,
 \qquad Q_y:=CB(y).
\]

对 (a\geq0) 定义参考图的移位间隙

\[
 \mathsf M_a(z,u)
 :=\sup_{(z',u')\in\operatorname{gph}T}
 \left\{\langle z-z',u' -u\rangle-
 \frac a2\|z-z'\|^2\right\}.
 \tag{M}
\]

上确界允许为 (+\infty)。这是同一变分对象的两个截面

\[
 \mathsf M_a\big|_{\operatorname{gph}T},
 \qquad
 m_a(z):=\mathsf M_a(z,0).
\]

若把 (v=B(y)w\) 代回去，也可在原图上写成

\[
 \widehat{\mathsf M}_a(y,v)
 :=\mathsf M_a\big(Cy,B(y)^\dagger v\big),
 \qquad (y,v)\in\operatorname{gph}F,
 \tag{M-lift}
\]

其中 (B(y)^\dagger B(y)=I_Z)。该提升只改变坐标，不改变 (M) 的参考图含义。

## 2. 图截面与正则截面的精确含义

### 2.1 图截面

若 (T) 在一个图块上满足

\[
 \langle z-z',u-u'\rangle\geq-\beta\|z-z'\|^2,
 \tag{H\(_{\rm mon}\)}
\]

则对任意 (a\geq2\beta)，

\[
 \mathsf M_a(z,u)=0
 \quad\text{对所有 }(z,u)\in\operatorname{gph}T
\]

当且仅当上式的全对弱单调不等式成立。(a=0) 时这正是普通单调性。这个断言只涉及参考图的全对量词，不要求 (T) 的极大性来证明零值等价。

若 (B=C^*\)，则 (F=C^*TC) 在同一图块上继承单调性，因为

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

则 (H\(_{\rm mon}\)) 给出原图的

\[
 \langle v-v',y-y'\rangle
 \geq-(\beta c_+^2+\delta)\|y-y'\|^2.
 \tag{F-hypomon}
\]

因此，单调性的传递需要对齐条件或同等强度的结构。仅有 (B-bounds) 不足。

### 2.2 零残差截面

因为 (B(y)) 满列秩，

\[
 S:=F^{-1}(0)=C^{-1}(Z_0).
 \tag{zero-set}
\]

对 (d_T(z):=\operatorname{dist}(z,Z_0)) 和 (d_S(y):=\operatorname{dist}(y,S))，伪逆给出

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

反向若 (d_S(y)\leq K_F r_F(y)^q)，则

\[
 d_T(Cy)\leq c_+K_F b_+^q r_T(Cy)^q.
 \tag{EB-backward}
\]

这些常数只用满射观察和完整纤维上下界，不要求 (B) 连续，也不把某个选定的局部根误当成完整零集。

## 3. 近端弦上的方向功

取一个原近端根

\[
 x=y+\lambda B(y)w,
 \qquad w\in T(Cy).
 \tag{prox-chord}
\]

把图点 ((Cy,w)) 作为 (M) 的竞争点，得到精确见证

\[
 \mathsf M_a(Cx,0)
 \geq
 \lambda\langle Q_yw,w\rangle-
 \frac{a\lambda^2}{2}\|Q_yw\|^2.
 \tag{directional-witness}
\]

这就是 (CB(y)) 在同一近端弦上的方向功。若在完整活跃纤维上

\[
 \operatorname{sym}Q_y\succeq\mu I_Z,
 \qquad \|Q_y\|\leq q_+,
 \tag{Q-sector}
\]

并且 (a\lambda q_+^2<2\mu)，则

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

这条估计把 (M) 的残差截面和实际 PPA 输入连接起来。它在 (m_a\) 的一般二次增长之外，保留了原近端弦的方向信息。

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

它在 (Q_y=\rho_yI)、\(\rho_y\geq0) 时直接传递；更一般地可假设 (T) 对 (Q_y) 的定向单调性，或直接要求

\[
 \langle Q_yw,C(y-p)\rangle
 \geq\nu\langle w,C(y-p)\rangle-
 \varepsilon\|w\|\,\|C(y-p)\|.
 \tag{angle-transfer}
\]

没有这项，(Q-sector) 只控制 (w) 自身的功，不能控制其与目标方向的交叉项。

## 4. 反例与边界

令 (C=I)、(T=I)、(Z_0=S=\{0\})。所有下列例子有相同的参考间隙 (M_a)、相同的零集和相同的精确残差界。

* (B=-I)。此时 (F=-I)，而
  \[
  J_{\lambda F}(x)=\frac{x}{1-\lambda},
  \qquad 0<\lambda<1,
  \]
  是扩张。(Q=-I) 的方向功为负，(positive-witness) 的门不能成立。
* (B=J) 为二维九十度旋转。此时 (F=J) 仍单调但非循环梯度，且
  \[
  \|J_{\lambda F}(x)\|=(1+\lambda^2)^{-1/2}\|x\|.
  \]
  这里 (\operatorname{sym}Q=0)，说明正扇区是充分条件而非必要条件。
* (B=\operatorname{diag}(1,-1))。一个方向收缩，另一个方向扩张。它说明残差和零集传递不能替代方向性条件。

因此，仅保留 (M\) 的图零值和 (m_a\) 的零残差增长，无法区分同一参考图经过不同有界可逆核后的原 PPA 动力学。C322 的通信谱中位置输运造成的一阶交叉项正属于 (chord-power) 所保留的信息，不能由标量残差截面恢复。

## 5. 精确范围与下一义务

这条桥已经证明了三件事。第一，(M) 的图截面在对齐缺口可控时给原图的弱单调性。第二，(M) 的零残差截面在完整满射纤维上与原零集的真实误差界双向等价。第三，(CB(y)) 在同一近端弦上的定向功给出一个可计算的 (M)-增长常数。

尚未证明的是仅由 (Q-sector) 和参考图的单调性推出原空间每个完整近端根的点收敛。必须补充 (chord-power) 的目标方向估计、所有根的共同观察窗口以及原空间到观测空间的留域控制。若这些条件不能在自然模型中验证，(B=-I) 与 C322 型位置输运反例说明缺口是结构性的。

