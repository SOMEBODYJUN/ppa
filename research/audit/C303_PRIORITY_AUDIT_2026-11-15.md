# C303 priority audit: what is old, what could be new

日期：2026-11-15
状态：**continue validation / priority provisional**

本页只核对最接近的一手工作与 C303 的对象差异。没有把检索未命中升级为首创性，也没有把一个正确的局部恒等式自动称为主要贡献。

## 1. 已有算法模式（Paper Facts）

- 变量步隐式二阶梯度格式和 inertial PPA/resolvent 重写已有公开先例。Chen–Ma–Yang, *A General Inertial Proximal Point Method for Mixed Variational Inequality Problem*, Optimization Online (2014), pp. 1–2, [PDF](https://optimization-online.org/wp-content/uploads/2014/07/4470.pdf)，已有 HBF 形式把二阶隐式差分写成
  \(w_{k+1}=(I+\lambda\nabla f)^{-1}(w_k+\alpha(w_k-w_{k-1}))\)，并明确称为 inertial PPA。早期 hybrid projection-proximal 文献也使用
  \(x_{n+1}=J^A_{\lambda_n}(x_n+\theta_n(x_n-x_{n-1}))\)。
- 因此 C303 不得把“引入变量步隐式惯性 PPA”本身作为新颖性中心。

## 2. 最近的离散二阶梯度文献

Horsin–Jendoubi, *Asymptotics for some discretizations of dynamical systems, application to second order systems with nonlocal nonlinearities*, HAL-03278131, equation (23), [PDF](https://cnam.hal.science/hal-03278131v1/preview/Horsin-Jendoubi.pdf)，研究有限维全隐式二阶方案，在离散角条件与 Łojasiewicz 条件下推出平衡点收敛。其状态变量是
\[
\frac{u_{n+1}-u_n}{\Delta t}=v_{n+1},
\qquad
\frac{v_{n+1}-v_n}{\Delta t}
 =-\|v_{n+1}\|^\alpha v_{n+1}-\nabla F(u_{n+1}),
\]
并以能量/Łojasiewicz 机制证明收敛。

这与 C303 的精确对象不同：

- C303 的 resolvent 是
  \[
  y+\lambda(a\nabla f-D^2f\,\nabla f)(y)=x+\beta v,
  \qquad \beta=\frac h{1+ah},\quad \lambda=h\beta;
  \]
- C303 的相空间误差是 \(w=v+\nabla f(x)\)，端点矩阵是
  \(A_y=(I-\beta D^2f(y))^{-1}\)；
- C303 研究 HJ 螺旋管、变量步 shrinking margin、\(q_k\) 法向递推以及
  \(\omega=S^1\) 的开相空间非收敛，而上述离散工作不提供 EP1–EP8、共同停止域或该非收敛结论。

## 3. 原始 HJ 问题与真正的潜在增量

Horsin–Jendoubi, *Non-genericity of initial data with punctual \(\omega\)-limit set*, Archiv der Mathematik 114 (2020), DOI [10.1007/s00013-019-01377-8](https://doi.org/10.1007/s00013-019-01377-8)，HJ 2020 的一阶梯度构造给出圆形 \(\omega\)-极限，并明确说二阶系统
\[
x''+a x'+\nabla\chi_a(x)=0,
\qquad \chi_a=af-\tfrac12\|\nabla f\|^2,
\]
只有在特殊初值 \(v_0=-\nabla f(x_0)\) 下可由一阶轨道继承；相空间开集非收敛在该文中仍被称为 open。

因此 C303 可主张的真正潜在新颖性，若全部证明义务闭合，应是：对同一个 HJ 构造、同一个 \(F=\nabla\chi_a\)、变量步隐式惯性 PPA，在一个共同相空间开集上得到全局轨道、\(\omega=S^1\) 和非收敛。EP1–EP8 是支撑这一桥的可复用局部引理，不能单独承担四大级贡献。

## 4. EP 与 W 候选的优先性风险

目前未找到一手文献直接陈述 C303 的特定组合
\[
\beta=\frac h{1+ah},\quad \lambda=h\beta,\quad
F= a\nabla f-D^2f\,\nabla f,
\]
与 EP1–EP8 的法向/极角端点恒等式，或
\(W_k=e^{z_k^2}\) 到 \(W_k\le K(1+t_k)\log(e+t_k)\) 的 HJ shrinking-angle 比较。

这只是“当前检索范围内未发现”，不是首创性证明：EP1–EP3 是短的代数重排，EP4/EP7–EP8 是在同一紧 patch、可逆性和场 margin 假设下的局部推论，W 比较本身也是标量超解。优先性风险低到中等，主要新颖性仍必须放在完整离散开盆非收敛定理及其与 HJ open problem 的精确闭合上。

## 5. 改变 priority 判断的最小证据

至少需要下列之一：

1. 对同一 C303 的 \(F=\nabla\chi_a\)、变量 \(h_k\) 和共同开初集，完成全局 resolvent coverage、source/lift、normal recursion、W 或 p=2 schedule、首接触和 \(\omega=S^1\) 的完整定理；或
2. 找到一手文献已经逐字给出同一 HJ geometry 下的 EP1–EP8 / W 比较，从而明确本库只能作再证明或迁移。

在这些证据出现前，C303 的 Truth 仍是 conditional，Value 可能实质但未闭，Novelty provisional，Ambition 保持；裁决为 **continue validation**，不是主要贡献。
