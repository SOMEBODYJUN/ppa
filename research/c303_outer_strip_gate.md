# C303：cutoff-free normalized outer-strip gate

状态：`derived-checked`（在 HJ 的显式 \\(\\gamma_i,F\\) 构造和可自由选择的 cutoff \\(\\Pi\\) 约定下）。本页只证明首接触前可使用同一 cutoff-free 公式的外条带；不单独证明惯性 PPA 轨道不出界。

## 1. 选择整个尾管分离的 cutoff

取
\[
0<\\eta_0<\\frac12\\min\\{\\gamma_1(0)-1,\\gamma_2(0)-1\\}.
\]
在环带 \\(\\{r>1+\\eta_0\\}\\) 内选一个连通、紧支撑的 \\(C^\\infty\\) bump \\(\\Pi\\)，使初始两条曲线点 \\(\\gamma_1(0),\\gamma_2(0)\\) 落在其支撑的内部。由于 \\(\\gamma_2(\\vartheta)=1+\\mu e^{-\\vartheta}\\to1\\)，取 \\(\\vartheta_0\\) 使
\[
\\gamma_2(\\vartheta)<1+\\eta_0/2
\\qquad(\\vartheta\\ge\\vartheta_0).
\tag{OS1}
\]

固定 \\(0<\\eta<1-\\beta\\)。令 normalized outer strip
\[
\\widetilde D_\\eta=\\{(r,\\vartheta):\\vartheta\\ge\\vartheta_0,\\ |q(r,\\vartheta)|\\le\\beta+\\eta\\}.
\]
因为 \\(q_r=2/\\Delta\\)、\\(\\Delta=(\\mu-1)e^{-\\vartheta}\\)，其半径满足
\[
r\\le m(\\vartheta)+\\frac{\\beta+\\eta}{2}\\Delta(\\vartheta)\\le1+C_{\\mu,\\beta,\\eta}e^{-\\vartheta}.
\]
再增大 \\(\\vartheta_0\\) 后，整个闭外条带满足 \\(r<1+\\eta_0/2\\)。故
\[
\\operatorname{supp}\\Pi\\cap\\overline{\\widetilde D_\\eta}=\\varnothing,
\\qquad
\\Pi\\equiv0,
\\qquad
1-\\Pi\\equiv1
\\quad\\text{on }\\overline{\\widetilde D_\\eta}.
\tag{OS2}
\]
因此 HJ 的精确公式 \\(f=hF(q)\\) 在整个 normalized outer strip 上成立。

## 2. 首接触前的条带包含

令 (x_k) 位于核心管 \\( |q_k|\\le\\beta\\)，并假设在一条隐式 \\(\\tau\\)-路径上
\[
\\|y_\\tau-x_k\\|\\le C h_k,
\\qquad
|\\vartheta_\\tau-\\vartheta_k|\\le C h_k,
\tag{OS3}
\]
且物理半径在 \\( [1/2,3/2]\\)。由
\[
q_r=O(e^{\\vartheta_k}),
\\qquad q_\\vartheta=O(1),
\]
得到
\[
|q(y_\\tau)-q(x_k)|\\le C h_k e^{\\vartheta_k}.
\tag{OS4}
\]
在停止区间使用 v4 的无循环包络
\[
\\vartheta_k^2\\le C_0+2\\log(1+t_k),
\\qquad t_k\\asymp k^{1-\\alpha}.
\tag{OS5}
\]
于是 \\(e^{\\vartheta_k}=\\exp O(\\sqrt{\\log(1+t_k)})=t_k^{o(1)}\\)，而 \\(h_k=h_0(k+1)^{-\\alpha}\\)，故
\[
h_k e^{\\vartheta_k}\\to0.
\tag{OS6}
\]
选择有限初始前缀的 \\(h_0\\) 足够小，并取尾部阈值后，使右侧小于 \\(\\eta/2\\)。则所有首接触前的 \\(\\tau\\)-路径包含于 \\(|q|\\le\\beta+\\eta\\)，从而均位于 cutoff-free outer strip。

## 3. 范围

(OS1)--(OS6) 关闭：HJ cutoff 对整个 normalized outer strip 的尾部分离，以及由角度包络得到的首接触前公式合法性。它仍需与 `c303_normal_error_recursion.md` 和 `c303_tau_common_tail_v5.md` 合并，才能处理 \\(w\\)-递推、首接触几何、有限初始子带及最终 \\(\\omega\\)-极限。
