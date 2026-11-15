# C303：隐式惯性 PPA 的精确 normal-error 递推

状态：`derived-checked`（在 `c303_global_bounds.md` 的全局 (g,H,D^3f) 界和 (a>K+delta) 假设下）。本引理关闭 D4--D5 的代数门；它不单独证明 HJ 尾管留域或开盆 \\(\\omega\\)-极限。

## 1. 隐式步与记号

令
\[
g=\\nabla f,\qquad H=\\nabla^2f,\qquad \\chi_a=af-\\tfrac12\\|g\\|^2,\qquad F=\\nabla\\chi_a=ag-Hg.
\]
给定 (h>0)，(x,v) 和隐式输出 (y) 满足
\[
y+\\lambda F(y)=x+\\beta v,\qquad \\beta=\\frac{h}{1+ah},\qquad \\lambda=h\\beta.
\]
令
\[
v^+=\\frac{y-x}{h},\qquad w=v+g(x),\qquad w^+=v^++g(y).
\]
等价的隐式 Euler 形式是
\[
(1+ah)v^+=v-hF(y),\qquad y=x+hv^+.
\tag{NR1}
\]

## 2. 精确矩阵恒等式

由 (F=ag-Hg) 和 (NR1)，
\[
(1+ah)w^+=w+g(y)-g(x)+hH(y)g(y).
\tag{NR2}
\]
写 \\(\\delta=y-x=hv^+\\) 并设
\[
\\bar H=\\int_0^1H(x+s\\delta)\\,ds,
\qquad g(y)-g(x)=\\bar H\\delta=h\\bar H v^+.
\]
因 (v^+=w^+-g(y))，得到精确等式
\[
\\bigl[(1+ah)I-h\\bar H\\bigr]w^+
 =w+h\\bigl(H(y)-\\bar H\\bigr)g(y).
\tag{NR3}
\]

设 (K=\\sup_x\\lambda_{\\max}(H(x))) 且 (a\\ge K+\\delta), \\(\\delta>0\\)。则
\[
A_h:=(1+ah)I-h\\bar H\\succeq(1+\\delta h)I,
\qquad \\|A_h^{-1}\\|\\le(1+\\delta h)^{-1}.
\tag{NR4}
\]
若 (M_3=\\sup_x\\|D^3f(x)\\|)、(G=\\sup_x\\|g(x)\\|)，则
\[
\\|H(y)-\\bar H\\|\\le M_3\\|y-x\\|=M_3h\\|v^+\\|\\le M_3h(\\|w^+\\|+G).
\tag{NR5}
\]
缩小 (h) 后由 (NR3)--(NR5) 吸收 (Ch^2\\|w^+\\|)，得到常数 (c_\\delta,C_\\delta>0) 使
\[
\\boxed{\\|w^+\\|\\le(1-c_\\delta h)\\|w\\|+C_\\delta h^2.}
\tag{NR6}
\]
常数不依赖 lifted angle。

## 3. 连续 \\(\\tau\\)-resolvent 路径

固定 \\(x_k,v_k\\) 和 (h=h_k)，对 \\(0\\le\\tau\\le1\\) 令 \\(h_\\tau=\\tau h\\)，并令 \\(y_\\tau\\) 解
\[
y_\\tau+\\lambda_\\tau F(y_\\tau)=x_k+\\beta_\\tau v_k,
\\qquad
\\beta_\\tau=\\frac{h_\\tau}{1+ah_\\tau},\\quad
\\lambda_\\tau=h_\\tau\\beta_\\tau.
\]
定义 \\(v_\\tau=(y_\\tau-x_k)/h_\\tau\\)（\\(\\tau>0\\)）和 \\(w_\\tau=v_\\tau+g(y_\\tau)\\)。同一推导给出
\[
A_{h_\\tau}w_\\tau
 =w_k+h_\\tau(H(y_\\tau)-\\bar H_\\tau)g(y_\\tau).
\tag{NR7}
\]
所以在同一小步长门内
\[
\\|w_\\tau\\|\\le(1-c_\\delta h_\\tau)\\|w_k\\|+C_\\delta h_\\tau^2,
\\qquad
\\sup_{0\\le\\tau\\le1}\\|w_\\tau\\|\\le\\|w_k\\|+C h_k^2.
\tag{NR8}
\]
这正是首接触 \\(\\tau_*\\) 处所需的统一误差。

## 4. 幂步长下的共同界

令 \\(h_k=h_0(k+1)^{-\\alpha}\\), (0<\\alpha<1)。取 (M>2C_\\delta/c_\\delta)。由于
\[
\\frac{h_k-h_{k+1}}{h_k^2}\\longrightarrow0,
\]
存在固定 (K_0) 使 (k\\ge K_0) 时 (Mh_k) 是 (NR6) 的 supersolution。对前缀 (k<K_0)，先固定一个闭初始子带并取 (h_0) 足够小，再取正半径 \\(\\varepsilon_w\\)-球使有限个连续递推均满足 \\(\\|w_k\\|\\le Mh_k\\)。于是同一个非空开相空间集给出
\[
\\|w_k\\|\\le Mh_k\\quad(k\\ge K_0),
\tag{NR9}
\]
且 (NR8) 给出所有后续 \\(\\tau\\)-路径的 \\(O(h_k)\\) 界。这里 (K_0) 是由递推常数确定的固定整数，不依赖未知的首次出界时刻。

## 5. 范围

(NR1)--(NR9) 关闭隐式 inertial PPA 的 normal-error 代数、与 lifted angle 无关的收缩常数、连续 \\(\\tau\\)-path 的统一误差以及幂步长下的共同 \\(O(h_k)\\) 界。它不单独关闭 HJ cutoff 的整个 outer-strip 尾部分离、首次接触的几何门、初始子带 slack 或 \\(\\omega\\)-极限。
