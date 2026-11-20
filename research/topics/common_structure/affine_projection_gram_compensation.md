# 仿射投影的 Gram 平衡与维数无关的 τ–L 补偿

<a id="affine-projection-gram-compensation"></a>

## C398-v1 · 角度加权的仿射投影平衡与 A+B 收缩门

**Status**：`derived-checked`。有限维欧氏空间中的恒等式、Gram 缺陷、
τ–L 收缩估计和高维反例均已独立重构。公开先行性和它作为一般共同结构
\(M\) 的资格尚未审查。

### 1. 仿射目标上的精确恒等式

令 \(H=\mathbb R^n\) 为欧氏空间，\(M\subset H\) 为非空仿射子空间，
\(p_1=P_Mx\)、\(p_2=P_My\)。写
\[
u=x-p_1,\qquad v=y-p_2,qquad d=p_2-p_1,
\]
并记
\[
a=\|u\|=\|x-p_1\|,\quad t=\|v\|=\|y-p_2\|,
\quad b=\|y-p_1\|,\quad s=\|x-y\|,\quad D=\|d\|.
\]
由于 \(u,v\perp(M-M)\) 且 \(d\in M-M\)，有
\[
b^2=D^2+t^2,
\qquad
s^2=D^2+a^2+t^2-2\langle u,v\rangle.
\]
因此
\[
\boxed{a^2+b^2-s^2=2\langle u,v\rangle.}
\tag{G}
\]

当 \(a,t>0\) 时，四条长度只能恢复
\[
I:=\frac{a^2+b^2-s^2}{2at}
 =\left\langle\frac ua,\frac vt\right\rangle
 =\cos\theta,
\tag{G1}
\]
而不能在一般高维构形中恢复常数。只用四条长度还可以写出精确的 Gram 缺陷
\[
\mathfrak G
 :=4a^2t^2-(a^2+b^2-s^2)^2
 =4\|u\wedge v\|^2\ge0.
\tag{G2}
\]
\(\mathfrak G=0\) 当且仅当两个法向向量共线。目标为仿射超平面且 \(x,y\)
 在同一侧时，法空间是一维并且 \(u/a=v/t\)，于是 \(I=1\)，这正是
 C396 的平面恒等式。共同法向射线 \(v=(t/a)u\) 也能在任意环境维数中恢复
 \(I=1\)。余维至少二且没有对齐条件时，\(I\) 可以变化。

令
\[
\Delta_M=a^2-s^2-b^2,
\qquad
\Delta_C^{\angle}=2(\langle u,v\rangle-b^2).
\]
由 (G) 得到维数无关的余量平衡
\[
\boxed{\Delta_M=\Delta_C^{\angle}.}
\tag{G3}
\]
在共同法向子类中，\(\Delta_C^{\angle}=2(at-b^2)\)，退化为 C396 的
“单调性余量等于高度下降减锚移余量”。高维的正确对象是 (G)、(G1) 或 (G3)，
而不是无条件的常数比值 (1)。

### 2. 仅由 A+B 得到的维数无关收缩

这一部分不使用 (G)，也不要求目标为平面或仿射子空间。令 \(S\) 为有限维
欧氏空间中的非空闭集，取一个合法近端对 \(y\in J_{\lambda F}(x)\) 和
一个最近点 \(p_1\in P_S(x)\)。设
\[
a=d(x,S),\quad s=\|x-y\|,\quad b=\|y-p_1\|,\quad t=d(y,S).
\]
考虑同一窗口、同一量词下的两个几何条件
\[
\tag{A_\tau}
s^2+b^2\le(1+2\tau)a^2,
\qquad
\tag{B_L}
t\le Ls,
\]
其中 \(\tau\ge0\)、\(L\ge0\)。最近点和三角不等式给出
\[
b\ge t,
\qquad b\ge |a-s|,
\qquad s\ge |a-b|.
\]
令
\[
e_\tau=\sqrt{1+2\tau},
\qquad
\beta_\tau=\frac{1+\sqrt{1+4\tau}}2.
\]
由两条对称三角不等式与 \(A_\tau\) 得
\[
s\le\beta_\tau a,
\qquad b\le\beta_\tau a.
\tag{C1}
\]
若 \(L>0\)，由 \(t\le b\) 和 \(t\le Ls\) 还有
\[
t\le L\beta_\tau a,
\qquad
t^2(1+L^{-2})\le s^2+b^2\le e_\tau^2a^2.
\tag{C2}
\]
故所有满足 A+B 的近端对都满足
\[
t\le m(\tau,L)a,
\qquad
m(\tau,L):=min\left\{\beta_\tau,
L\beta_\tau,\frac{Le_\tau}{\sqrt{1+L^2}}\right\}.
\tag{C3}
\]
当 \(L=0\) 时，\(t=0\)。当 \(m(\tau,L)<1\) 且完整近端关系在窗口内有 coverage 时，
\[
d(y,S)\le m(\tau,L)d(x,S),
\qquad
\|x-y\|\le\beta_\tau d(x,S).
\tag{C4}
\]
因此从满足留域预算的初值出发，任一满足同一 A+B 的选择策略都给出
\[
\sum_{k\ge0}\|x^k-x^{k+1}\|
 \le \frac{\beta_\tau}{1-m(\tau,L)}d(x^0,S),
\]
并在闭目标和留域条件下收敛到 \(S\)。这是一个维数无关的
“弱 A 由 B 补偿”的收缩定理。

对 \(\tau\ge0\)、\(L>0\)，由 (C3) 得到该估计的严格参数门
\[
\tau<T(L):=
\begin{cases}
\dfrac{1-L}{L^2},&0<L\le\dfrac12,\\[2mm]
\dfrac1{2L^2},&L\ge\dfrac12.
\end{cases}
\tag{C5}
\]
第一段来自 \(L\beta_\tau<1\)，第二段来自
\(Le_\tau/\sqrt{1+L^2}<1\)。图中的绿/橙分界表达的是这个后端收缩估计的
严格门。它不依赖平面投影恒等式，因此升到高维时这条 \(\tau\)–\(L\) 曲线
可以保留。

### 3. 非线性 B 与正则性的量词边界

若把 \(B_L\) 改为
\[
t\le\psi(s),
\tag{B_\psi}
\]
其中 \(\psi\) 非减且 \(\psi(0)=0\)，A+B 给出通用上包络
\[
\mathcal M_{\tau,\psi}(a)
 :=\sup_{0\le r\le\beta_\tau a}
 \min\left\{\psi(r),\sqrt{e_\tau^2a^2-r^2}\right\},
\qquad
t\le\mathcal M_{\tau,\psi}(a).
\tag{C6}
\]
如果 \(\mathcal M_{\tau,\psi}(a)\le\kappa a\) 在工作窗内成立，或它的迭代具有趋零和可和尾势，则可用 (C4) 的同一覆盖、留域和极限识别证明收敛。这个版本可以在不先命名 GMSR 的情况下表达非线性补偿。

但在线性全纤维量词下，\(B_L\) 不是独立于正则性的另一种假设。若
\(x=y+\lambda v\) 对所有相关 \(v\in F(y)\) 都处在同一认证窗口，则
\[
t\le L\lambda\|v\|\quad(\forall v\in F(y))
\Longrightarrow
d(y,S)\le \lambda L\,r_F(y),
\tag{C7}
\]
其中 \(r_F(y)=\inf_{v\in F(y)}\|v\|\)。反向地，线性 GMSR
\(d(y,S)\le K r_F(y)\) 给出 \(B_L\) 且 \(L=K/\lambda\)。所以保持线性
\(B_L\) 时，不需要把 GMSR 另列为输入，但也不能声称已经弱化了线性正则性。
只有改用 \(B_\psi\) 并加入 (C6) 的迭代/尾势门，才得到真正的非线性正则尺度。

选定轨道或选定图值的 A+B 不能取下确界。\(F(y)=\{y,y^3\}\)、\(\lambda=1\)、
选取 \(v=y\) 时，\(\tau=0,L=1\) 的 A+B 成立，但
\(r_F(y)=|y|^3\)、\(d(y,S)=|y|\)，不存在局部线性 GMSR。这是完整图量词必须
写入定理的原因。

### 4. 高维与非仿射的边界

在 \(\mathbb R^3\) 取 \(M=\{(q,0,0):q\in\mathbb R\}\)、\(p_1=p_2=0\)、
\[
x=(0,2,0),qquad y=(0,1/2,\sqrt3/2).
\]
则 \(a=2,t=1,b=1,s=\sqrt3\)，所以 \(A_0\) 取等、\(B_1\) 成立，
但 \(I=(a^2+b^2-s^2)/(2at)=1/2\)。这排除了把 C396 的常数 (1)
直接推广到余维至少二的目标。

若目标是一般曲线或曲面，令 \(d=p_2-p_1\) 仍可展开为
\[
a^2+b^2-s^2=2\langle u,v\rangle+2\langle d,u\rangle.
\tag{C8}
\]
第二项是弦方向与输入法向的曲率/倾斜缺陷。正 reach 或局部投影正则性只能把
它控制成误差预算，不能保留 (G) 的 exact 常数 (1)。

**结论边界**：本页已经得到一个真实且可复用的结果，即仿射投影的角度加权
平衡和任意维数的 A+B 收缩门。它尚未证明一般多值原算子存在一个同时恢复通常
单调性和完整 GMSR 的统一结构 (M)。
