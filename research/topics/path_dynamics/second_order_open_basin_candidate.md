# 二阶阻尼梯度系统的开盆域非收敛候选

状态：`candidate`。本文件只记录一个待独立复核的精确候选，不把它升级为已证 Claim。

## 候选命题

存在 (C^\infty) 势 \(\chi:\mathbb R^4\to\mathbb R)、常数 \(\alpha>0\) 及非空开集
\(\mathcal U\subset\mathbb R^4\times\mathbb R^4\)，使得二阶系统
\[
 x''+\alpha x'+\nabla\chi(x)=0
\]
对每个 \((x_0,v_0)\in\mathcal U\) 都全局存在、有界，并满足
\[
 \omega(x)=S^1,\qquad \lim_{t\to\infty}x(t)\text{ 不存在}.
\]
这里的相空间应为 \(\mathbb R^2\times\mathbb R^2\cong\mathbb R^4\)，而 \(S^1\) 嵌入位置空间。

这正对接 Horsin--Jendoubi (Archiv Math. 2020, Remark 3) 留下的开问题：他们将一阶开盆域圆形例通过
\(\chi=\alpha f-\frac12|\nabla f|^2\) 嵌入二阶系统，但只得到相空间中的二维初值子流形，并明确称相空间开集的存在性当时未知。

## 关键恒等式

令 \(f:\mathbb R^2\to\mathbb R\) 为 Horsin--Jendoubi 的一阶圆形开盆域构造，\(X=-\nabla f\)，并令
\[
 \chi_\alpha=\alpha f-\tfrac12|\nabla f|^2,
 \qquad w=v+\nabla f(x).
\]
二阶方程等价于
\[
 x'= -\nabla f(x)+w,
 \qquad
 w'=\bigl(\nabla^2 f(x)-\alpha I\bigr)w.
\]
若 \(D\) 是一阶构造的闭曲线管道，且
\[
 \kappa:=\sup_{x\in\overline D}\lambda_{\max}(\nabla^2 f(x))<\alpha,
 \]
则在 \(D\) 内
\[
 |w(t)|\le e^{-\delta t}|w(0)|,
 \qquad \delta=\alpha-\kappa>0.
\]
这给出图 \(v=-\nabla f(x)\) 的统一正常指数吸引；困难是证明它足以抵抗管道宽度随时间趋零的边界扰动。

## 需核验的 HJ 几何估计

在大参数 \(\theta\) 上取
\[
 \gamma_1(\theta)=1+e^{-\theta},\quad
 \gamma_2(\theta)=1+\mu e^{-\theta},\quad
 h(\theta)=e^{-\theta^2},\quad \mu>1,
\]
并用 HJ 的两个边界曲线 \(b_i(\theta)=1+c_i e^{-\theta}\) 围成
\(D=\{b_1(\theta)<r<b_2(\theta),\theta>\theta_1\}\)。从 HJ 的显式梯度公式应逐项核得常数 \(c,C>0\) 使
\[
 \begin{aligned}
  &X_\theta(r,\theta)\ge c\,\theta e^{-\theta^2},
  &&(r,\theta)\in D,\\
  &X\cdot n_1\le -c\,e^{-\theta^2+\theta},
  &&r=b_1(\theta),\\
  &X\cdot n_2\ge c\,e^{-\theta^2+\theta},
  &&r=b_2(\theta).
 \end{aligned}
\]
法向量可取 \(n_i=-b_i e_r+b_i'e_\theta\)（上边界方向相反）。\(F\) 在 \([b_1,b_2]\) 对应的归一化参数子区间上有正下界，故第一式的主项来自 \(-h'F\)，后二式的主项来自 \(\pm2hF'/ (\gamma_2-\gamma_1)\)。

## 开盆域 bootstrap（尚待写成正式证明）

令 \(s_1=r-b_1(\theta)\)、\(s_2=b_2(\theta)-r\)。在边界上，\(|\nabla s_i|\le C_0\)，故扰动系统满足
\[
 s_i'\ge m(\theta)-C_0|w|,
 \qquad m(\theta):=c e^{-\theta^2+\theta}.
\]
另一方面，管道内的显式公式给
\[
 \theta'\le C_1\theta e^{-\theta^2}+C_0|w|.
\]
只要轨道留在管道，比较方程可给出
\[
 \theta(t)^2\le C_2+2\log(1+t),
 \qquad m(\theta(t))\ge c_2(1+t)^{-p}
\]
（任取稍大的固定 \(p>1\)，例如 \(p=3)，并吸收初始有限时间段）。于是
\[
 \sup_{t\ge0}\frac{e^{-\delta t}}{m(\theta(t))}<\infty,
 \qquad
 \frac{e^{-\delta t}}{m(\theta(t))}\longrightarrow0.
\]
选择 \(|w(0)|<\varepsilon\) 使 \(C_0e^{-\delta t}|w(0)|\le m(\theta(t))/2\)；连续首次离开论证即闭合 \(s_i>0\) 的不变性。还需在同一 bootstrap 中处理 \(\theta'\) 的下界：当 \(\theta\) 大时，\(X_\theta\ge c\theta e^{-\theta^2}\)，而 \(|w|=O(e^{-\delta t})\)，故 \(\theta'>0\) 且 \(\theta(t)\to\infty\)。从而
\[
 r(t)\to1,
 \qquad \theta(t)\to\infty,
 \qquad \omega(x)=S^1.
\]

## 致命审查点

1. 必须从 HJ 公式而非图形直觉逐项给出 \(m(\theta)\) 和 \(X_\theta\) 的统一常数，注意法向主项为 \(h/(\gamma_2-\gamma_1)\asymp e^{-\theta^2+\theta}\)。
2. \(\theta(t)^2\le C+2\log(1+t)\) 的比较不能预设不变性；应以首次离开时间上的 bootstrap 写成闭合不等式。
3. \(\chi_\alpha\) 的全局行为不需强制，只要证明 \(\mathcal U\) 轨道留在有界 \(D\)；仍须说明局部 ODE 解可延拓。
4. 仅有图的正常收缩不能自动推出开 basin；shrinking barrier 的量化比较是核心新义务。
5. 二阶命题不能与 C302 的一阶/PPA 准解析分界混写。即使候选成立，函数仅为 \(C^\infty\)；要得到权重类版本需另证 HJ 构造的 Denjoy--Carleman 界。

## 文献锚点

- Horsin--Jendoubi, *Non-genericity of initial data with punctual \(\omega\)-limit set*, Archiv der Mathematik 114 (2020), Theorem 1.1 and Remark 3, DOI 10.1007/s00013-019-01377-8.
- Jendoubi--Bégout--Bolte--Jendoubi, *On damped second-order gradient systems*, arXiv:1411.8005 / JDE 2015：可定义/KL 势下的收敛结论；不能直接排除本候选的非 KL 势。
- 仓库 [C297--C302](../../canonical/exact_proximal_limit_sets.md) 与 [准解析分界](../../canonical/quasianalytic_proximal_dichotomy.md)：给一阶精确近端/梯度流的聚点集及权重分界，尚不含本二阶开盆域问题。

