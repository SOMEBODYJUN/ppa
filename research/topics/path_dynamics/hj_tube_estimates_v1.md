# HJ 螺旋管的显式渐近估计引理 v1

状态：`candidate`。本文件只承担 C303 的局部几何估计；它不把 Horsin--Jendoubi 的原构造重写成新的势，也不提供 PPA/GPPA 离散桥。所有常数均依赖于所选 HJ 管参数和有限初始角阈值。

## 1. 精确管模型

固定
\[
\gamma_1(\vartheta)=1+e^{-\vartheta},\qquad
\gamma_2(\vartheta)=1+\mu e^{-\vartheta},\qquad
\Delta(\vartheta)=\gamma_2-\gamma_1=(\mu-1)e^{-\vartheta},
\]
其中
\[
1<\mu<e^{2\pi}.
\]
后一不等式是 HJ 未展开螺旋分支的物理不重叠条件：
\(\gamma_2(\vartheta+2\pi)<\gamma_1(\vartheta)\)。令
\[
m(\vartheta)=\frac{\gamma_1+\gamma_2}{2},\qquad
q(r,\vartheta)=\frac{2(r-m(\vartheta))}{\Delta(\vartheta)}.
\]
取固定 \(0<\beta<1\)，并令内边界为
\[
b_1(\vartheta)=m(\vartheta)-\frac{\beta}{2}\Delta(\vartheta),
\qquad
b_2(\vartheta)=m(\vartheta)+\frac{\beta}{2}\Delta(\vartheta).
\]
于是 \(b_i=1+c_i e^{-\vartheta}\)、\(0<c_1<c_2\)，且
\[
q(b_1(\vartheta),\vartheta)=-\beta,
\qquad
q(b_2(\vartheta),\vartheta)=\beta.
\]
在 HJ 的 cutoff 恒等于一的管内，写
\[
f(r,\vartheta)=h(\vartheta)F(q(r,\vartheta)),
\qquad h(\vartheta)=e^{-\vartheta^2},
\]
并假设 \(F\in C^2([-\beta,\beta])\) 满足
\[
F_*:=\min_{[-\beta,\beta]}F>0,
\qquad
G_j:=\max_{[-\beta,\beta]}|F^{(j)}|<\infty\quad(j=1,2),
\]
以及 HJ 边界符号
\[
F'(-\beta)<0<F'(\beta).
\]

## 2. 导数恒等式

因为 \(\Delta'=-\Delta\)、\(\gamma_1'+\gamma_2'=-(1+\mu)e^{-\vartheta}\)，对固定物理半径 \(r\) 有
\[
q_r=\frac{2}{\Delta},
\qquad
q_{\vartheta}=q+\frac{1+\mu}{\mu-1},
\qquad
q_{\vartheta\vartheta}=q_{\vartheta}.
\tag{E1}
\]
特别地，在闭管 \(|q|\le\beta\) 上，\(q_\vartheta\) 与 \(q_{\vartheta\vartheta}\) 由只依赖 \((\mu,\beta)\) 的常数统一控制，而 \(q_r\asymp e^{\vartheta}\)。

令 \(Y=-\nabla f\)。极坐标中的正交分量为
\[
Y_r=-f_r=-\frac{2h}{\Delta}F'(q),
\qquad
Y_{\vartheta}=-\frac1r f_{\vartheta}
 =\frac{h}{r}\bigl(2\vartheta F(q)-F'(q)q_\vartheta\bigr).
\tag{E2}
\]
取 \(\vartheta_0\) 足够大，使闭管位于 \(1/2\le r\le3/2\)，并使
\[
2\vartheta F_*\ge 2G_1\sup_{|q|\le\beta}|q_\vartheta|
\qquad(\vartheta\ge\vartheta_0).
\]
则存在 \(0<c_0<C_0<\infty\) 使
\[
c_0\vartheta e^{-\vartheta^2}
\le Y_{\vartheta}(r,\vartheta)
\le C_0\vartheta e^{-\vartheta^2}
\qquad(|q|\le\beta,\ \vartheta\ge\vartheta_0).
\tag{HJ-1'}
\]

## 3. 边界向内漂移

有 \(b_i'(\vartheta)=O(e^{-\vartheta})\)。在 \(b_1\) 上，(E2) 和 \(F'(-\beta)<0\) 给
\[
Y_r(b_1,\vartheta)=\frac{2h|F'(-\beta)|}{\Delta}>0;
\]
在 \(b_2\) 上，\(F'(\beta)>0\) 给
\[
Y_r(b_2,\vartheta)=-\frac{2hF'(\beta)}{\Delta}<0.
\]
令
\[
s_1=r-b_1(\vartheta),
\qquad
s_2=b_2(\vartheta)-r.
\]
在极坐标度量下
\[
\nabla s_1=e_r-\frac{b_1'}r e_{\vartheta},
\qquad
\nabla s_2=-e_r+\frac{b_2'}r e_{\vartheta}.
\]
由于 \(Y_{\vartheta}=O(\vartheta h)\)，而
\[
\frac{h}{\Delta}\asymp e^{-\vartheta^2+\vartheta},
\qquad
|b_i'Y_{\vartheta}|=O(\vartheta h e^{-\vartheta}),
\]
有
\[
\frac{|b_i'Y_{\vartheta}|}{h/\Delta}=O(\vartheta e^{-2\vartheta})\longrightarrow0.
\]
因此增大 \(\vartheta_0\) 后存在 \(m_0>0\) 使两条边界均满足
\[
\nabla s_i\cdot Y
\ge m_0e^{-\vartheta^2+\vartheta}
\qquad(s_i=0,\ \vartheta\ge\vartheta_0).
\tag{HJ-2'}
\]
同时，因 \(r\ge1/2\) 且 \(b_i'=O(e^{-\vartheta})\)，存在 \(L_s<\infty\) 使
\[
|\nabla s_i|\le L_s.
\tag{E3}
\]

## 4. Hessian 阶与全局有界性

在闭管内由 (E1) 及 \(F\in C^2\) 得
\[
f_{rr}=hF''(q)q_r^2=O(e^{-\vartheta^2+2\vartheta}),
\]
\[
f_{r\vartheta}
 =h'F'(q)q_r+hF''(q)q_rq_\vartheta+hF'(q)q_{r\vartheta}
 =O(e^{-\vartheta^2+\vartheta}),
\]
其中 \(q_{r\vartheta}=q_r\)，以及
\[
f_{\vartheta\vartheta}
 =h\left((4\vartheta^2-2)F-4\vartheta F'q_\vartheta
 +F''q_\vartheta^2+F'q_{\vartheta\vartheta}\right)
 =O(\vartheta^2e^{-\vartheta^2}).
\tag{E4}
\]
从极坐标到笛卡尔坐标只引入 \(r^{-1},r^{-2}\) 以及一阶项 \(f_r/r,f_\vartheta/r^2\)，故这些项也在尾部衰减。HJ 构造的 \(f\) 在整个 \(\mathbb R^2\) 上为 \(C^\infty\)，而物理闭管连同其极限圆是紧集，所以
\[
K:=\sup_{x\in\overline D}\lambda_{\max}(\nabla^2f(x))<\infty.
\tag{E5}
\]

## 5. cutoff 支撑门

C303 的 bootstrap 只在 cutoff 因子还原为一的闭尾管中使用上面的公式。HJ 原式为 \(f=e^{-\vartheta^2}\phi(r,\vartheta)(1-\Pi)\)，所以所需精确门是：再取 \(\vartheta_0\) 足够大，使
\[
\operatorname{supp}\Pi
\cap
\{(r,\vartheta): b_1(\vartheta)\le r\le b_2(\vartheta),\ \vartheta\ge\vartheta_0\}
=\varnothing.
\tag{E6}
\]
于是该闭尾管上 \(\Pi\equiv0\)，从而 \(1-\Pi\equiv1\)、\(f=hF(q)\)；(E1)--(E5) 适用到所有首次接触时刻。HJ 原文要求 \(\Pi\) 的支撑包含初始曲线附近而在足够大的 \(\vartheta\) 不包含 \(\gamma_i\)；但仅排除两条边界曲线并不自动排除整个闭管，因此需要逐字核对或另行给出上述尾部分离，不能由“趋近圆”一句话替代。

## 6. 本引理关闭的范围

在 (E6) 及 HJ 的全局 \(C^\infty\) 延拓已逐字核对后，本文件关闭 C303 证明中唯一的局部常数义务：\(Y_\vartheta\) 的双边界、法向内漂移和 Hessian 有界性。它仍不关闭以下问题：

1. HJ 原文中 cutoff、\(F\) 和边界参数的精确函数身份及符号需要按原页逐式对照；
2. 二阶开盆结果是 ODE 结论，尚未提供离散 PPA/GPPA 桥；
3. HJ Remark 3 的 open-problem 事实不等于全面外部优先性证明。
