# HJ 二阶开盆候选：交叉审查

**裁决：继续验证。** 候选有分量，但尚未达到 theorem；唯一实质未闭义务是把 HJ 的显式公式逐项化为统一常数 \(a,A,c,C_0,\theta_1\)。

HJ 构造取 \(\gamma_1=1+e^{-\theta}\)、\(\gamma_2=1+\mu e^{-\theta}\)、\(h=e^{-\theta^2}\)，且候选管道 \(b_i\) 位于 \(F'\) 取得最大值的内层，故归一化径向变量 \(\xi\in[-\beta,\beta]\subset(-1,1)\)，\(\varphi\) 在管内有正下界。令 \(\Delta=(\mu-1)e^{-\theta}\)，则 \(\partial_r\varphi=O(e^\theta)\)、\(\partial_\theta\varphi=O(1)\)，而 \(h'=-2\theta h\)。因此对 \(X=-\nabla f\)，取充分大 \(\theta_1\) 后可得到
\[
a\theta e^{-\theta^2}\le X_\theta/r\le A\theta e^{-\theta^2}
\]
在全管道内成立。HJ 的边界显式公式给内向法向余量
\[
m(\theta)=c e^{-\theta^2+\theta}.
\]
源文用 \(X=\nabla f\) 写法向符号；改成 \(X=-\nabla f\) 后两个边界号同时翻转，得到
\[
s_i'\ge m(\theta)-C_0|w|,
\quad
a\theta e^{-\theta^2}-C_0|w|\le\theta'\le A\theta e^{-\theta^2}+C_0|w|.
\]

令 \(w=v+\nabla f\)。二阶系统等价于
\[
x'=-\nabla f+w,\qquad w'=(\nabla^2f-\alpha I)w.
\]
闭管上 \(\kappa=\sup\lambda_{\max}(\nabla^2f)<\infty\)：径向二阶导数最多产生 \(e^{2\theta}\)，仍被 \(e^{-\theta^2}\) 压倒。若 \(\alpha>\kappa\)，留在管道时
\[
|w(t)|\le e^{-\delta t}|w_0|,\qquad\delta=\alpha-\kappa.
\]

可用依赖初始角度的首次离开比较闭合开集。固定 \(\theta_0>\theta_1\)，设 \(A_0=\theta_0^2+1\)、\(U(t)=\sqrt{A_0+2\log(1+t)}\)。令
\[
K_{A_0,\delta}=\sup_{t\ge0}(1+t)U(t)e^{-\delta t},\quad
M_\delta=\sup_{t\ge0}(1+t)^2e^{-\delta t}.
\]
选择
\[
|w_0|<\min\left\{(2C_0K_{A_0,\delta})^{-1},
\frac{ce^{-A_0+\theta_1}}{2C_0M_\delta},
\frac{a\theta_1e^{-A_0}}{2C_0M_\delta}\right\}.
\]
首次离开前，\(\theta\le U\) 给
\(m(\theta)\ge ce^{-A_0+\theta_1}(1+t)^{-2}\)，第一项使角度上界不超过 \(U'\)，第二项使 \(s_i'\ge m/2>0\)，第三项使 \(\theta'\ge(a/2)\theta e^{-\theta^2}>0\)。故不能先离开管道或跌到 \(\theta_1\)。角度单调；有限极限会与正的角漂移下界矛盾，所以 \(\theta\to\infty\)。于是 \(b_i(\theta)\to1\) 夹出 \(r\to1\)，连续无界角度给 \(\omega\)-limit 全圆。管内 \(x,v,w\) 有界，且 HJ 的 \(f\) 全局 \(C^\infty\)，所以 \(\chi_\alpha\) 也全局 \(C^\infty\)，解可延拓。

## 仍需核对

1. 从 HJ 原式逐项取 \(a,A,c,C_0,\theta_1\)，特别是边界法向量方向和 \(m(\theta)\) 的常数。
2. 把 \(\varepsilon(\theta_0)\) 写成连续正函数，并取 \(D_*\Subset D\)，从而 \(\{(x_0,v_0):x_0\in D_*, |v_0+\nabla f(x_0)|<\varepsilon(\theta_0)\}\) 真的是相空间四维开集。
3. 不得以“指数衰减自动胜过缩管”替代上述 \(\theta\)-dependent 常数和首次离开论证。

HJ Remark 3 已把相空间开集问题列为 open；该候选因此没有被源文直接覆盖。
