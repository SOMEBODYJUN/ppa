# RL–PPA 主线程数学推导（待交叉审计）

## 1. Minty 图表的精确形式

对局部图块 \(\Gamma\subset\operatorname{gph}F\)，定义
\[
M_+(u,u^*)=u+\lambda u^*,\qquad M_-(u,u^*)=u-\lambda u^*.
\]
则局部 all-pairs RL 当且仅当 \(M_+|_\Gamma\) 单射，且图耦合映射
\[
Q_\Gamma:=M_-\circ(M_+|_\Gamma)^{-1}
\]
在 \(M_+(\Gamma)\) 上满足
\[
\|Q_\Gamma x-Q_\Gamma y\|\le L\|x-y\|^\gamma.
\]
若 \(M_+(\Gamma)\) 包含输入邻域 \(V\)，则局部 resolvent 为
\[
J_{\Gamma}(x)=\frac{x+Q_\Gamma(x)}2,
\]
并在 \(V\) 上存在且单值。多值情形不能把 \(Q_\Gamma\) 写成普通关系复合
\((I-\lambda F)\circ(I+\lambda F)^{-1}\)，因为后者会在同一 primal 点重选输出分支。

## 2. 完整标量包络

记
\[
A(d)=\frac{d^2+L^2d^{2\gamma}}2,
\qquad
B(d)=\frac{d+Ld^\gamma}{2}.
\]
RL 不仅给
\[
d_+^2+s^2\le A(d),
\]
还同时给
\[
d_+\le B(d),\qquad s\le B(d).
\]
后两式分别来自
\(x^+-p=((x-p)+(Qx-Qp))/2\) 与
\(x-x^+=((x-p)-(Qx-Qp))/2\)。结合
\(d_+\le\psi(s/\lambda)\)，从这些标量后果能得到的最优统一包络为
\[
\widehat R(d)=
\sup_{0\le t\le B(d)/\lambda}
\min\left\{
B(d),\;\psi(t),\;\sqrt{A(d)-\lambda^2t^2}
\right\}.
\]
因此 \(\limsup_{d\downarrow0}\widehat R(d)/d<1\) 是这四条标量约束的精确收缩证书。
“精确”仅指完整保留此处列出的四条约束；投影距离几何（例如 \(|d-d_+|\le s\)）或其他原生信息
还能进一步缩小可行集。
它不是一个给定 RL 算子实际收缩的必要条件。

### 2.1 \(0<\gamma<1\)

若 \(L>0\) 且
\[
C_\gamma=\limsup_{t\downarrow0}\frac{\psi(t)}{t^{1/\gamma}},
\]
则
\[
\limsup_{d\downarrow0}\frac{\widehat R(d)}d
=C_\gamma\left(\frac{L}{2\lambda}\right)^{1/\gamma}.
\]
理由是 \(B(d)\sim (L/2)d^\gamma\)，而在 \(t=B(d)/\lambda\) 处
\[
\sqrt{A(d)-\lambda^2t^2}=\frac{|d-Ld^\gamma|}{2}\asymp d^\gamma,
\]
后两项相对 \(d\) 均不约束临界的 \(\psi\)-项。故临界条件是
\[
C_\gamma<\left(\frac{2\lambda}{L}\right)^{1/\gamma}.
\]

若残差增长为
\[
d(0,F(y))\ge m\,d(y,S)^a,
\]
则 \(\psi(t)=(t/m)^{1/a}\)，从而
\[
\begin{array}{c|c}
a<\gamma & \text{自动兼容，且给距离阶 }\gamma/a>1\text{ 的局部超线性上界}\cr
a=\gamma & \lambda m>L/2\cr
a>\gamma & \text{本证书不能推出固定 Q-linear}
\end{array}
\]
等价地，对 \(d(y,S)\le\kappa r(y)^q\)：
\[
q>1/\gamma\text{ 给距离阶 }\gamma q>1\text{ 的局部超线性上界};\quad
q=1/\gamma:\ \kappa(L/(2\lambda))^{1/\gamma}<1.
\]

### 2.2 \(\gamma=1\) 与线性误差界

若 \(\psi(t)=\rho t\)，令
\[
\kappa_E=\sqrt{\frac{1+L^2}{2}}\frac{\rho}{\sqrt{\rho^2+\lambda^2}},
\quad
\kappa_S=\frac{\rho(1+L)}{2\lambda},
\quad
\kappa_J=\frac{1+L}{2}.
\]
则完整包络的因子为
\[
\widehat\kappa=\min\{\kappa_E,\kappa_S,\kappa_J\}.
\]
因此材料中的 \(\kappa_E\) 只是 energy+EB 子系统的最优因子，不是完整 RL 后果的最优标量因子。

## 3. 不要把原生二次信息过早压成单个 L

若相对某个解点 \(p\) 已知
\[
\langle a,b\rangle\ge\mu\|a\|^2+\nu\|b\|^2,
\quad a=x^+-p,\quad \lambda b=x-x^+,
\]
且
\[
A_0=1+2\lambda\mu\ge0,\qquad
B_0=1+2\nu/\lambda\ge0,
\]
并且 \(A_0\rho^2+B_0\lambda^2>0\)，
则直接有
\[
A_0d_+^2+B_0s^2\le d^2.
\]
配上线性 EB \(d_+\le(\rho/\lambda)s\) 得
\[
\kappa_{\mu,\nu}
=\frac{\rho}{\sqrt{A_0\rho^2+B_0\lambda^2}}
=\frac{\rho}{\sqrt{(1+2\lambda\mu)\rho^2+\lambda^2+2\lambda\nu}}.
\]
这通常强于先把 \((\mu,\nu)\) 压缩成 balanced RL 常数。

若只需转成 \(\gamma=1\) RL，设
\[
c=\lambda\mu+\nu/\lambda,\quad
h=\lambda\mu-\nu/\lambda,\quad
\Delta=1-4\mu\nu.
\]
当 \(1+c>0\)、\(\Delta\ge0\) 时，由配方
\[
\left\|w+\frac{h}{1+c}z\right\|
\le\frac{\sqrt\Delta}{1+c}\|z\|
\]
得到仅凭该二次不等式可保证的锐常数
\[
L_{\mu,\nu}(\lambda)
=\frac{|h|+\sqrt\Delta}{1+c}.
\]

## 4. 高阶误差界的去奇异化移植

对任意 \(q>0\) 定义
\[
T_q(v)=\|v\|^{q-1}v\ (v\ne0),\quad T_q(0)=0,
\qquad H_q=T_q\circ F.
\]
精确恒等式为
\[
H_q^{-1}(0)=F^{-1}(0),\qquad
d(0,H_q(x))=d(0,F(x))^q.
\]
所以 \(H_q\) 的普通 metric subregularity
\[
d(x,S)\le\kappa d(0,H_q(x))
\]
与 \(F\) 的 q-order subregularity 完全等价。由此可以把 Hoffman/Robinson、
FOSCMS/SOSCMS、方向 coderivative、slope 等 q=1 工具用在 \(H_q\) 上。
在 \(0\) 处不能不加资格条件地对 \(T_q\circ F\) 套 coderivative 链式法则；必须直接计算
\(\operatorname{gph}H_q\)、分支导数或标量残差斜率。

必要障碍：若存在非解点 \(x_k\to S\) 且
\(d(0,F(x))\le M d(x,S)\)，则任何 \(q>1\) 的
\(d(x,S)\le\kappa d(0,F(x))^q\) 都不可能成立。

## 5. 半代数定性联合证书

设 \(\Gamma\) 是紧半代数局部图块。若 \(M_+|_\Gamma\) 单射，则在
\(\Gamma\times\Gamma\) 上，半代数函数
\[
U=\|\Delta M_-\|^2,\qquad V=\|\Delta M_+\|^2
\]
满足 \(V=0\Rightarrow U=0\)。Łojasiewicz 不等式因此给出某个
\(C>0,N\in\mathbb N\) 使 \(U^N\le CV\)，即某个 all-pairs RL Hölder 证书。
若 \(M_+(\Gamma)\) 还覆盖输入邻域，则兼得局部 resolvent existence。
闭半代数 multifunction 对其完整局部零集也有某个 Hölder metric subregularity 证书；
若使用 \(S=F^{-1}(0)\cap D\)，还需 \(D\) 同属半代数局部化，或确认邻域内没有被 \(D\) 排除的零点。
因此半代数结构已经解决“是否存在某个指数”的定性问题；未解决的是可手算、足够锐且彼此兼容的
\((\gamma,L,q,\kappa)\)。

## 6. 锐的多值非孤立剪切族

取 \(t\in\mathbb R^m,y\ge0\)、单位向量 \(e\)、\(0<\alpha<1\)、\(b,c>0\)，定义
\[
F(t,y)=\left\{
\left(-b y^\alpha e,\frac{c-1}{\lambda}y\right),
\left(-b y^\alpha e,-\frac{c+1}{\lambda}y\right)
\right\}.
\]
则 \(\operatorname{gph}F\) 闭，\(S=\mathbb R^m\times\{0\}\)，且全域单值 resolvent 为
\[
J_{\lambda F}(p,q)=
\left(p+\lambda b c^{-\alpha}|q|^\alpha e,\frac{|q|}{c}\right).
\]
故
\[
Q(p,q)=
\left(p+2\lambda b c^{-\alpha}|q|^\alpha e,
\frac{2|q|}{c}-q\right).
\]
其最佳局部 Hölder 指数是 \(\alpha\)，渐近最小 RL 模量为
\[
L_0=2\lambda b c^{-\alpha}.
\]
另一方面
\[
d(0,F(t,y))\ge b y^\alpha,
\]
所以临界残差系数 \(m=b\)。PPA 的距离递推精确为
\[
d(J(p,q),S)=\frac1c d((p,q),S).
\]
新的临界条件
\(\lambda m>L_0/2\) 精确化为 \(c>1\)，与真实收缩边界完全一致；
旧的 \(L_0/\sqrt2\) 条件严格保守。该族同时使 step bound 渐近取等，证明常数 \(2\) 一般不可改进。

## 7. 模块化证书编译器

保留所有原生约束。对 \(p\in P_S(x)\) 置
\[
a=x^+-p,\quad b=(x-x^+)/\lambda,\quad
e=d_+,\quad v=\|a\|,\quad w=s,\quad z=\lambda\langle a,b\rangle.
\]
给定旧距离 \(d\)，基础可行集保留
\[
d^2=v^2+w^2+2z,\quad |z|\le vw,\quad
0\le e\le v,\quad |d-e|\le w,\quad e\le\psi(w/\lambda),
\]
以及 RL 的精确标量式
\[
2(v^2+w^2)-d^2\le L^2d^{2\gamma}.
\]
原生 semimonotone 证书直接加入
\[
z\ge\lambda\mu v^2+(\nu/\lambda)w^2,
\]
solution-anchored weak-Minty 证书 \(\langle a,b\rangle\ge\beta\|b\|^2\)
直接加入 \(z\ge(\beta/\lambda)w^2\)。partial semimonotonicity、法向/切向或 blockwise
约束也各自保留，而不是先压成单一 \(L\)。最终令
\[
R_{\mathcal C}(d)=
\sup\{e:\exists(v,w,z)\text{ 使全部已核实约束成立}\}.
\]
若 \(\limsup R_{\mathcal C}(d)/d<1\)，得到局部距离收缩；再由任一可求和 step 上界完成有限长度、
局部化和点收敛。这是现有 partial-information 工具进入 RL-PPA 时最不损失信息的统一接口。

## 8. 高阶误差界并非实际收缩的必要条件

取标量 \(t\)、\(y\ge0\)、\(0<\gamma<1\)、\(b>0,c>1\)，局部令
\[
F(t,y)=\left\{
\left(-b|t|y^\gamma,\frac{c-1}{\lambda}y\right),
\left(-b|t|y^\gamma,-\frac{c+1}{\lambda}y\right)
\right\}.
\]
在 \(\lambda b y^\gamma<1\) 的输入/图邻域内，
\[
J(p,q)=\left(
\frac{p}{1-\lambda b\operatorname{sign}(p)(|q|/c)^\gamma},
\frac{|q|}{c}
\right).
\]
因此 \(d_+=d/c\)，而反射映射在任何邻域都非 Lipschitz、最佳 all-pairs Hölder 指数为
\(\gamma\)。但是沿 \(t=0\)，最小残差恰为 \((c-1)y/\lambda\)，故任何 \(q>1\) 的统一
高阶误差界都失败。这个例子证明：阶数匹配是聚合 RL+EB 证书推出固定 Q-linear 的结构要求，
不是一个实际已经收缩的 RL-PPA 的必要条件。
