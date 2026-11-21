# DD2 的真实图输入扰动、扰动精度和 shadow

## 设定

设 \(H\) 是 Hilbert 空间，\(S\subseteq\operatorname{zer}F\) 非空闭，\(d=d(\cdot,S)\)，并固定 \(\lambda>0\)、开工作域 \(U\) 与半径 \(R>0\)。允许关系 \(\mathcal J(u)\subseteq J_{\lambda F}(u)\) 在 \(U_R=\{u\in U:d(u)\le R\}\) 非空。DD2 的图条件对同一个 \(\mathcal J\) 逐步成立。对 \(y\in\mathcal J(u)\) 记
\[
\tau=d(u),\qquad a=d(y),\qquad s=\|u-y\|,\qquad w=(u-y)/\lambda\in F(y).
\]
DD2 的真实残差误差界给 \(a\le\psi(r_F(y))\le\psi(s/\lambda)\)，其中 \(r_F(y)=\inf\{\|v\|:v\in F(y)\}\)，\(\psi\) 非减且在零点连续，\(\psi(0)=0\)。下文分别使用两个已经由精确 DD2 验证的条件。
\[
s\le C[\Theta(\tau)-\Theta(a)],\qquad a\le \tau.
\tag{I1}
\]
\[
\tau^2-a^2\ge s^2-2D(\tau)\ge\beta s^2,\qquad \beta>0.
\tag{I2}
\]
版本 (I1) 使用连续、严格递增、凹的长度势 \(\Theta\) 和 \(\Theta(0)=0\)。若精确证明仅给出 \(G(t)=\int_0^t u/\chi(u)\,du\)，其中 \(\chi\) 非减且在正点为正，可令
\[
g(t)=t/\chi(t),\qquad \bar g(t)=\sup_{t\le u\le R}g(u),\qquad \Theta(t)=\int_0^t\bar g(u)\,du.
\]
因为 \(g(v)\ge g(u)/2\) 对 \(v\in[u/2,u]\) 成立，对每个 \(\ell>0\) 有 \(|\{\bar g>\ell\}|\le2|\{g>\ell/2\}|\)。按水平集积分得 \(\int_0^R\bar g\le4\int_0^R g\)。因此原 Dini 条件已保证新势有限、凹且逐区间支配原势差。一般绝对扰动引理使用这个新势。同样的构造适用于 \(g(t)=t/\chi(t/2)\)。

若 \(D(t)\le\chi(t/2)^2/4\)、\(\chi(t)=o(t)\)、\(\chi(t)=\lambda\psi^{-1}(t)\)，小窗内 \(\chi(\tau/2)\le\tau/2\)。当 \(a\ge\tau/2\)，误差界给 \(s\ge\chi(\tau/2)\)。当 \(a<\tau/2\)，三角不等式给 \(s\ge\tau-a>\tau/2\)。两种情形都给 \(2D(\tau)\le s^2/2\)，故 (I2) 可取 \(\beta=1/2\)。C399 的强幂窗也直接给 (I1) 与 (I2)。

非精确步的实际输入为 \(x\)，真实图见证为 \(y,w\)，定义
\[
 u=x+e=y+\lambda w,\qquad y\in\mathcal J(u),\qquad
 r=d(x),\quad \eta=\|e\|,\quad \ell=\|x-y\|.
 \tag{I3}
\]
外迭代接受 \(x^+=y\)。所测长度为 \(\ell\)，图位移为 \(s=\lambda\|w\|\)，且 \(|\tau-r|\le\eta\)、\(|\ell-s|\le\eta\)。对于给定的 \(e_k\)，方法在 \(x^k+e_k\) 精确求允许根。对于内层求解器报告的 \(y,w\)，则由残差 \(e=y+\lambda w-x\) 定义受扰输入。后一个解释仍要求图成员和允许分支证书。

<a id="dd2-inexact-absolute"></a>
## 绝对误差与真实长度

在 (I1) 下，凹性给 \(\Theta(r+\eta)\le\Theta(r)+\Theta(\eta)\)，只要 \(r+\eta\le R\)。每一步具有
\[
\ell\le C[\Theta(r)-\Theta(a)]
   +\eta+C(\Theta(\tau)-\Theta(r))_+
 \le C[\Theta(r)-\Theta(a)]+\eta+C\Theta(\eta).
\tag{I4}
\]
第二个不等式给出与方向无关的充分预算。第一个不等式记录实际提高距离势的误差成本。例如，当 \(\tau\le r\)，仅需这一步的欧氏误差。

设 \(x^0\in U\)，给定误差包络 \(0\le\eta_k\le b_k\)，满足
\[
r_0+\sum_{k\ge0}b_k\le R,\qquad
B_0:=C\Theta(r_0)+\sum_{k\ge0}[b_k+C\Theta(b_k)]
  <\operatorname{dist}(x^0,H\setminus U).
\tag{I5}
\]
则每个按该误差包络选择的轨道可续、留域并有有限真实长度，且
\[
\sum_{j=k}^{\infty}\|x^{j+1}-x^j\|
   \le C\Theta(r_k)+\sum_{j=k}^{\infty}[b_j+C\Theta(b_j)].
\tag{I6}
\]
证明从有限前缀开始。因为 \(a\le\tau\le r+\eta\)，归纳给 \(r_k+b_k\le r_0+\sum_{i\le k}b_i\le R\)。到目前为止的实际长度加将要使用的 \(b_k\)，由 (I4) 的望远镜估计被 \(B_0\) 控制，故新受扰输入在 \(U_R\)，可选允许根。下一输出也被相同预算留在 \(U\)。任意尾段求和给 (I6)。有限长度使 \(x^k\) 强收敛，且将 \(x^\infty\) 留在 \(U\)。由 \(s_k\le\|x^{k+1}-x^k\|+\eta_k\to0\) 与 \(d(x^{k+1})\le\psi(s_k/\lambda)\) 得 \(x^\infty\in S\)。在一个非平凡凹势窗口内，单独的 \(\sum\Theta(b_k)<\infty\) 已蕴含 \(\sum b_k<\infty\)，因为 \(\Theta(b)\ge b\Theta(R)/R\)。

若外迭代另有输出误差 \(x^+=y+\xi\)，记 \(\delta=\|\xi\|\)、\(a^+=d(x^+)\)。使用 \(\Theta(a^+)\le\Theta(a)+\Theta(\delta)\) 给
\[
\|x^+-x\|\le C[\Theta(r)-\Theta(a^+)]
   +\eta+\delta+C[\Theta(\eta)+\Theta(\delta)].
\]
以两项误差的和代替 (I5) 中的半径预算，并在长度预算加入各自的势成本，同一有限前缀归纳成立。极限由 \(d(y)\le\psi(s/\lambda)\) 与 \(d(x^+)\le d(y)+\delta\) 识别。纯输出误差对应取 \(e=0\) 并附上某个精确允许根见证。它的欧氏可和反例也由 (I8) 实现，从零点先加一次纯法向输出误差，接着精确步推进，最后用第二次纯法向输出误差复位。切向位移的下界沿用同一凹幂估计。

只有 \(\sum\eta_k<\infty\) 时，若已知所有受扰输入都在 (I2) 的工作域，则仍有
\[
\beta\sum_{k\ge0}s_k^2
 \le r_0^2+\sum_{k\ge0}(2r_k\eta_k+\eta_k^2)<\infty.
\tag{I7}
\]
这里 \(r_k\le r_0+\sum\eta_k\)，且 \(\tau_k^2\le(r_k+\eta_k)^2\)。因此实际步长平方可和，\(d(x^k)\to0\)。下面的完整原算子表明这一结论的边界也出现在 \(U=H\) 的零管内。

### 欧氏绝对误差的反例

固定 \(1/2<q<1\)，写 \(b=1/q\in(1,2)\)、\(\alpha=2-b\in(0,1)\)，取 \(\lambda=K=1\)。在 \(\mathbb R^2\) 定义
\[
F(t,z)=
\left(\operatorname{sgn}(t)|t|^{2b-1},\
      -\operatorname{sgn}(t)|t|^b\right).
\tag{I8}
\]
其零集为 \(S=\{0\}\times\mathbb R\)。法向输入函数 \(t\mapsto t+\operatorname{sgn}(t)|t|^{2b-1}\) 连续严格递增且满射，第二坐标为平移，因此 \(I+F\) 是全域同胚，完整近端唯一。对输出 \(y=(t,z)\)，其输入为 \(u=y+F(y)\)，最近锚为 \(p=(0,z-\operatorname{sgn}(t)|t|^b)\)。直接得到
\[
\langle F(y),y-p\rangle=|t|^{2b}-|t|^{2b}=0,\qquad
d(y,S)=|t|\le\|F(y)\|^q.
\]
因此整个图满足 DD2 的零缺陷幂次条件。

从零线施加法向输入误差 \(h>0\)，随后用精确步推进。法向半径从 \(a_0=h\) 依 \(a_{i-1}=a_i+a_i^{2b-1}\) 降至零，前 \(N\) 步切向位移 \(g_N(h)=\sum_{i=1}^N a_i^b\)。由幂函数凹性，
\[
a_{i-1}^{\alpha}-a_i^\alpha\le
\alpha a_i^{\alpha-1}a_i^{2b-1}=\alpha a_i^b.
\]
选 \(N\) 使 \(a_N\le h/2\)，即有 \(g_N(h)\ge(1-2^{-\alpha})h^\alpha/\alpha\)。此时用法向误差 \(-a_N\) 将输入复位到零线，最后一步无切向位移。两个非零误差均不超过 \(h\)。

对任意给定切向位移 \(L>0\)，重复上述段 \(\lfloor L/g_N(h)\rfloor\) 次，再以同一个 \(N\) 和某个幅度 \(h'\in[0,h]\) 完成余量。由法向近端的连续性，\(g_N(h')\) 取到 \([0,g_N(h)]\) 内每个值。沿每段切向单调移动，法向半径不超过 \(h\)。方向反转可用负法向注入实现。以 \(\sum\eta_k^\rho\) 计费时，一次运输的成本至多
\[
2h^\rho\left(1+L/g_N(h)\right)=O(h^\rho+Lh^{\rho-\alpha}).
\]
每个 \(\rho>\alpha\) 都可让该成本任意小。逐段交替精确连接 \((0,0)\) 和 \((0,L)\)，令第 \(j\) 段成本不超过 \(2^{-j}\)，并令相应 \(h_j\downarrow0\)。选择 \(\rho=\min\{1,p\}\) 可使 \(\sum\eta_k\) 和 \(\sum\eta_k^p\) 同时有限，其中 \(p>\alpha\) 任意。真实轨道有界、留在任意给定的小零管，距离趋零，但两个端点都是聚点且每段真实长度至少 \(L\)。这证明 \(\alpha=2-1/q\) 是仅按绝对误差幂可和性、对整个 C399 类保证有限长度和点收敛的锐指数。该例可由加一个核变量和恒等恢复块嵌入退化 PPPA。

孤立目标也不能从欧氏误差可和推出真实有限长度。取平面上的直角旋转 \(J\) 与 \(F(y)=\|y\|^{b-1}Jy\)，此时 \(r_F(y)=\|y\|^b\)，目标为 \(\{0\}\)，\(\langle F(y),y\rangle=0\)。映射 \(I+F\) 对每个圆施加固定旋转和新的半径 \(\sqrt{a^2+a^{2b}}\)，新半径严格递增且满射，故它为同胚。由 \(\tau^2-a^2=a^{2b}\) 与凹性得到
\[
\tau^\alpha-a^\alpha\le \alpha a^{\alpha-1}(\tau-a)
\le \frac{\alpha}{2}a^b.
\]
从零注入大小 \(h\) 的输入误差，沿精确步走到半径至多 \(h/2\)，再用一次反向输入误差回零。若 \(h<1\)，第一步实际长度 \(a\) 至少为该步图位移 \(a^b\)，故每段实际长度至少 \(2(1-2^{-\alpha})h^\alpha/\alpha\)。取 \(h_j\downarrow0\) 并满足 \(\sum_j h_j<\infty\)、\(\sum_jh_j^\alpha=\infty\)，例如 \(h_j=cj^{-p}\) 与 \(1<p\le1/\alpha\)。全部轨道收敛到唯一零点，实际长度发散。

<a id="dd2-inexact-relative"></a>
## 相对于下降的误差与可计算的真实残差准则

设 \(0\le\theta<1\)。相对准则
\[
\eta\le\theta(\tau-a)
\tag{I9}
\]
保证 \(r-a\ge(1-\theta)(\tau-a)\)，以及 \(\eta\le\theta s\)。当 \(r<\tau\)，在 \([a,\tau]\) 对凹势插值，得到
\(\Theta(r)-\Theta(a)\ge(1-\theta)[\Theta(\tau)-\Theta(a)]\)。当 \(r\ge\tau\)，同一界由单调性成立。因此
\[
\ell\le C_\theta[\Theta(r)-\Theta(a)],\qquad
C_\theta=C(1+\theta)/(1-\theta).
\tag{I10}
\]
若使用原势 \(G(t)=\int_0^t u/\chi(u)\,du\)，其在 \([a,r]\) 的增量占 \([a,\tau]\) 增量的至少 \((r^2-a^2)/(\tau^2-a^2)\ge(1-\theta)^2\)，因为 \(g(u)/u\) 非增且 \(r-a\ge(1-\theta)(\tau-a)\)。这也给出 (I10)，系数改为 \(C(1+\theta)/(1-\theta)^2\)。

(I9) 允许在用精确估计之前控制试探输入。仅由 \(\tau\le r+\eta\) 可得 \(\eta\le\theta r/(1-\theta)\)、\(\tau\le r/(1-\theta)\)。因此 \(r_0\le(1-\theta)R\) 与
\[
C_\theta\Theta(r_0)+\theta r_0/(1-\theta)
 <\operatorname{dist}(x^0,H\setminus U)
\tag{I11}
\]
将每个有限前缀的实际点和新输入保留在工作域。精确根 \(e=0\) 是可接受的种子。望远镜给真实尾长 \(\le C_\theta\Theta(r_k)\)。此外
\(\eta_k\le\theta(r_k-r_{k+1})/(1-\theta)\)，误差自动可和，故极限属于 \(S\cap U\)，遇到 \(S\) 后驻定。在正距离处有 \(s>0\)，否则 \(a\le\psi(0)\) 会连同 \(u=y\) 强制 \(\tau=0\)。若精确步的下降为 \(\tau-a\ge\gamma\tau^{1+\nu}\)，由 \(r\le(1+\theta)\tau\) 得
\[
r-a\ge\gamma_\theta r^{1+\nu},\qquad
\gamma_\theta=(1-\theta)\gamma/(1+\theta)^{1+\nu}.
\tag{I12}
\]

给定真实图见证 \(w\in F(y)\) 后，(I9) 有一个无需评价未知零集距离的充分准则。若 (I2) 可用，由 \(\tau+a\le s+2\psi(s/\lambda)\) 得
\[
\boxed{\quad
\|y+\lambda w-x\|\le
\theta\beta\,\frac{(\lambda\|w\|)^2}
{\lambda\|w\|+2\psi(\|w\|)} .
\quad}
\tag{I13}
\]
分母在 \(s=0\) 时按右侧为零处理。因为 \((\tau-a)(\tau+a)\ge\beta s^2\)，(I13) 蕴含 (I9)。可以同时施加绝对缺陷帽 \(\eta\le\mu\)，事先取 \(r_0+\mu\le R\) 且 \(C_\theta\Theta(r_0)+\mu<\operatorname{dist}(x^0,H\setminus U)\)。这一留域预算在有限前缀上先确保候选 \(u=x+e\) 位于精确窗口，才调用 (I2) 和 (I9)。试探政策仍须有 \(y\in\mathcal J(u)\) 的同一关系证书。精确种子满足帽和准则，种子存在本身只保证抽象非空。若允许图块内的候选真实图对趋向一个正步长、严格帽内的精确种子，同时 \(\psi\) 在该见证范数处连续，则 (I13) 有严格正余量，候选最终通过。给定的内层算法能生成此类候选，是另外的实现条件。

若只知道候选 \(v\) 的同点图距离至多 \(\varepsilon\)，可在存在 \(w\in F(y)\) 且 \(\|w-v\|\le\varepsilon\) 的条件下给保守证书。设 \(s_-=\lambda(\|v\|-\varepsilon)_+\)、\(s_+=\lambda(\|v\|+\varepsilon)\)。若
\[
\|y+\lambda v-x\|+\lambda\varepsilon
\le\theta\beta\frac{s_-^2}{s_++2\psi(s_+/\lambda)},
\]
则真正见证满足 (I13)。还要验证这个真正见证对应允许分支、保留绝对帽并落入工作域。若所报的是未达到的下确界，可用严格容差选真正见证。邻近点的近似图与算子扩大，须另证与这个同点图条件的联系。

### 幂次误差的锐阈值

设 \(\psi(t)=Kt^q\)、\(h=K/\lambda^q\)，并取 C399 的幂缺陷，记 \(c_*=h^{-1/q}\)。在 \(D(t)\le Mt^p\) 和 \(p>2/q\) 的分支上令 \(\beta_*=1\)。在 \(p=2/q\)、\(2M<c_*^2\) 的分支上令 \(\beta_*=1-2M/c_*^2\)。零缺陷时同样用 \(\beta_*=1\)。由 \(\tau\le s+h s^q\) 得 \(s\ge c\tau^{1/q}\) 对每个 \(c<c_*\) 在足够小窗口成立，故任取 \(0<\beta<\beta_*\) 可验证 (I2)。式 (I13) 因而允许在小窗直接使用
\[
\eta\le c_{\rm e}s^{\,2-q},\qquad
c_{\rm e}<\beta_* /(2h).
\tag{I14}
\]
严格系数可留给 \(\theta<1\) 和 \(\beta<\beta_*\) 所需的余量。

取 \(b=1/q\)、\(0\le 2M<c_*^2\) 和 \(\beta_*=1-2M/c_*^2\)。令 \(c(a)=(M/c_*)\min(a,\varepsilon)^{b-1}\le1/2\)，其中 \(\varepsilon>0\) 足够小。以下平面完整旋转图实现系数边界。
\[
\lambda F_M(y)=c_*a^{b-1}\big[-c(a)y+\sqrt{1-c(a)^2}\,Jy\big],
\qquad a=\|y\|.
\]
这里 \(\|\lambda F_M(y)\|=c_*a^b\)，故 \(K\|F_M(y)\|^q=a\)。又有 \(\langle \lambda F_M(y),y\rangle=-c_*c(a)a^{b+1}\ge-Ma^{2b}\)。输入半径 \(\tau(a)\) 满足
\[
\tau(a)^2=a^2+c_*^2a^{2b}-2c_*c(a)a^{b+1}
\ge a^2+\beta_*c_*^2a^{2b}.
\]
在 \(a\le\varepsilon\) 时右边取等号，因而输入锚定缺陷 \(D(\tau)=M\tau^{2b}\) 有效。对 \(a>\varepsilon\)，上式左边的导数至少为 \(2a+[2bc_*^2-2M(b+1)]a^{2b-1}>0\)。半径函数连续、严格递增且满射，每个正半径上的角度映射为旋转，因此完整近端全域单值连续。

任取固定的 \(0<a\le\varepsilon\)，取半径为 \(a\) 的实际输入 \(x\)，将 \(u\) 取为同向、长为 \(\tau(a)\) 的向量，令 \(y=J_{\lambda F_M}(u)\)。输出 \(y\) 的半径仍为 \(a\)，其角度相对 \(x\) 有一个固定非零转角。所需误差满足
\[
\eta=\tau(a)-a=\frac{\beta_*s^2}{\tau(a)+a}
 <\frac{\beta_*}{2h}s^{2-q},\qquad s=c_*a^b.
\]
在整个固定小圆上不断重复这一步，轨道既不到解集也不点收敛。随着所选圆半径趋零，\(\eta/s\to0\) 且 \(\eta/s^{2-q}\to\beta_*/(2h)\)。因 \(\|x-y\|\ge s-\eta\)，用实际步长替代 \(s\) 的任意固定小线性相对系数也会接受足够小的这些圆。该族证明 (I14) 的最优幂与严格系数门，还反驳临界系数处使用 \(o(s)\) 的点态误差函数。\(M=0\) 的例子还适用于 \(p>2/q\) 的任给非负缺陷上界。

实际单条轨道上 \(\eta_k/s_k\to0\) 也能与欧氏误差可和、点不收敛同时成立。取 \(\lambda=K=1\)、\(b=1/q\)，令 \(Q_\vartheta\) 为二维旋转，在 \(\mathbb R\times\mathbb R^2\) 设
\[
F(t,v)=
\big(\operatorname{sgn}(t)|t|^{2b-1},
     (Q_{-\vartheta(|t|,\|v\|)}-I)v\big),
\qquad
\vartheta(a,\rho)=2\arcsin\big(\min\{1/2,a^b/(2\rho)\}\big)
\quad(\rho>0).
\]
在 \(v=0\) 令第二分量为零。\(I+F\) 的法向部分严格递增且满射，切向部分在每个圆上是旋转，故完整近端全域唯一。固定开域 \(1/2<\|v\|<2\) 和足够小的法向管。切向弦长此时正好为 \(a^b\)，最近锚的零缺陷等式与真误差界同 (I8)。

令实际法向半径 \(a_k=c(k+1)^{-p}\)，其中 \(c>0\) 足够小且 \((2b-1)^{-1}<p\le b^{-1}\)，切向坐标在单位圆上。以纯法向误差 \(a_{k+1}+a_{k+1}^{2b-1}-a_k\) 得到规定的下一半径，同时切向转角为 \(2\arcsin(a_{k+1}^b/2)\)。有
\[
\eta_k\le a_k-a_{k+1}+a_{k+1}^{2b-1},
\qquad
s_k\ge a_{k+1}^b.
\]
因此 \(\sum\eta_k<\infty\)，且 \(\eta_k/s_k\le a_{k+1}^{b-1}+O(k^{-1+p(b-1)})\to0\)。由于 \(\sum a_{k+1}^b=\infty\)，转角累积无界且单步转角趋零。按每次首次越过 \(2m\pi\) 或 \(2m\pi+\pi\) 取子列，得到两个相反的切向聚点。轨道始终在该工作域内，真实长度也发散。

### 线性相对系数的可和指数

设 \(\eta_k\le\sigma_k s_k\)、\(0\le\sigma_k\le\sqrt\beta/2\)。对工作域内的步，(I2) 给 \(s_k\le\tau_k/\sqrt\beta\)，从而
\[
\tau_k\le(1-\sigma_k/\sqrt\beta)^{-1}r_k,\qquad
(\Theta(\tau_k)-\Theta(r_k))_+
\le (2\sigma_k/\sqrt\beta)\Theta(r_k).
\]
第二式用凹势的 \(\Theta(0)=0\)，故 \(\Theta(t)/t\) 非增。当 \(\sum_k\sigma_k<\infty\)，设 \(P=\prod_k(1-\sigma_k/\sqrt\beta)^{-1}\)，则 \(r_k\le Pr_0\)。相对系数可和时，由 (I4) 的第一个估计得真实总长度上界
\[
C\Theta(r_0)+(2/\sqrt\beta)\sum_k\sigma_k\,[Pr_0+C\Theta(Pr_0)].
\]
这里 \(\eta_k\le2\sigma_kPr_0/\sqrt\beta\)。在局部实施时可加缺陷帽 \(\eta_k\le\mu\)，以 \(Pr_0+\mu\le R\) 及上述长度上界加 \(\mu\) 严格小于到 \(U^c\) 的距离关闭有限前缀。\(e=0\) 保留可接受的精确种子。

对 C399 幂窗，有限长度的最优可和指数为
\[
m_*=\frac{b}{b-1}=\frac{1}{1-q},\qquad b=1/q,\quad\alpha=2-b.
\tag{I14a}
\]
精确步满足 (I1) 的幂势形式与 \(s\ge c\tau^b\)。可将 \(\beta\) 取在 \((0,1]\)，并仍要求 \(0\le\sigma_k\le\sqrt\beta/2\)。若 \(\eta\le(\tau-a)/2\)，则 (I10) 给 \(\ell\le3C(r^\alpha-a^\alpha)\)。若 \(\eta>(\tau-a)/2\)，由 \(\tau-a\ge\beta s^2/(2\tau)\) 与 \(\eta\le\sigma s\) 得
\[
s\le4\sigma\tau/\beta,\qquad
\tau\le[4\sigma/(\beta c)]^{1/(b-1)},\qquad
r\ge\tau/2.
\]
于是 \(\ell=O(\sigma^{m_*})\)，而势的可能增量满足
\[
(a^\alpha-r^\alpha)_+
\le(\tau^\alpha-r^\alpha)_+
\le\alpha(\tau/2)^{\alpha-1}\eta
\le C_1\sigma^2\tau^\alpha
\le C_2\sigma^{m_*}.
\]
最后一步用 \(2+\alpha/(b-1)=m_*\)。两种情形统一为
\[
\ell\le3C(r^\alpha-a^\alpha)+C_3\sigma^{m_*},
\tag{I14b}
\]
其中 \(C_3\) 只依赖精确幂窗的数据。设 \(M_\sigma=\sum_k\sigma_k^{m_*}<\infty\)，且试探规则另带固定缺陷帽 \(\eta_k\le\mu\)。若
\[
\left(r_0^\alpha+\frac{C_3}{3C}M_\sigma\right)^{1/\alpha}+\mu\le R,\qquad
3Cr_0^\alpha+C_3M_\sigma+\mu<\operatorname{dist}(x^0,H\setminus U),
\]
则每个有效有限前缀按 (I14b) 先控制当前实际点和距离，帽再保证新的 \(u=x+e\) 落入 \(U_R\)。精确根保持可接受，故归纳得到所有允许选择的续接。真实尾长至多 \(3Cr_k^\alpha+C_3\sum_{i\ge k}\sigma_i^{m_*}\)。因 \(\eta_k\le s_k/2\)，有 \(s_k\le2\ell_k\)，误差与图位移均可和，(I3) 的真残差界识别极限属于 \(S\cap U\)。

对每个 \(m>m_*\)，上一节的三维环向轨道取 \(p=1/b\)，有 \(\eta_k/s_k=O(k^{-(b-1)/b})\)，因此 \(\sum_k(\eta_k/s_k)^m<\infty\)。从足够靠后的项开始，所有相对系数也在 \([0,\sqrt\beta/2]\)，所有绝对缺陷可同时小于任意给定正帽。该轨道始终留在认证管内并有两个不同点为聚点，切向实际长度至少为发散的 \(\sum_k a_{k+1}^b\)。这固定了幂次 C399 全类的指数边界。

对 C399 的幂窗，仅 \(\sum_k\sigma_k^2<\infty\) 已足以保住距离与实际长度率。由 \(\tau_k\le r_k+\sigma_k s_k\) 和 Young 不等式得
\[
r_{k+1}^2\le(1+4\sigma_k^2/\beta)r_k^2-(\beta/2)s_k^2.
\]
又 \(r_k\le\tau_k+\sigma_k s_k\le(3/2)\tau_k\)，且精确步有 \(s_k\ge c\tau_k^{1/q}\)。记 \(P_k=\prod_{i<k}(1+4\sigma_i^2/\beta)\)，\(\varepsilon_k=r_k^2/P_k\)，\(\mu_0=(\beta/2)c^2(2/3)^{2/q}\)。有
\[
\varepsilon_{k+1}\le\varepsilon_k-(\mu_0/2)\varepsilon_k^{1/q},
\]
因为 \(P_k^{1/q}/P_{k+1}\ge1/2\)。这给 \(r_k\le\sqrt{P_\infty}r_0\) 和
\(r_k\le A(k+n_0)^{-p_0}\)，其中 \(p_0=(2/q-2)^{-1}\)，\(A\) 可不依赖 \(r_0\)，当 \(r_0>0\) 足够小时可取整数 \(n_0\asymp r_0^{-(2/q-2)}\)。每个长度 \(n=k+n_0\) 的块上求和同一平方不等式，得到
\[
(\beta/2)\sum_{i=k}^{k+n-1}s_i^2
\le A^2\left(1+(4/\beta)\sum_i\sigma_i^2\right)n^{-2p_0}.
\]
由于 \(\|x^{i+1}-x^i\|\le(1+\sigma_i)s_i\)，按二倍块相加得尾长 \(O((k+n_0)^{1/2-p_0})\)，前缀总长为 \(O(r_0^{2-1/q})\)。和上段一样，可用共同误差帽保证试探输入先落在工作域。相应半径条件为 \(\sqrt{P_\infty}r_0+\mu\le R\)，空间余量为有限前缀长度上界加 \(\mu\) 严格小于到 \(U^c\) 的距离。若 \(r_0=0\)，所有工作域内的相对步均驻定。

<a id="dd2-inexact-rate"></a>
## 误差尾和、点误差与有限次命中

对于 C399，记 \(\nu=2/q-2\)、\(p_0=1/\nu>1/2\)。精确步有 \(a\le f(\tau)=\tau-\gamma\tau^{1+\nu}\) 与 (I2)。缩窗使 \(f\) 在 \([0,R]\) 非负、非减且 \(1\)-Lipschitz。相对准则由 (I12) 给 \(r_k=O(k^{-p_0})\)；结合 (I10) 的幂势 \(\Theta(t)=t^{2-1/q}\)，点误差和真实尾长都是 \(O(k^{1/2-p_0})\)。

绝对误差也可在只有欧氏尾和约束时保住这两个幂率。取整数 \(n_0\ge1\)、常数 \(A_0,B\ge0\)，并设
\[
 r_0\le A_0 n_0^{-p_0},\qquad
 E_k:=\sum_{j\ge k}b_j\le B(k+n_0)^{-p_0},\qquad
 (A_0+B)n_0^{-p_0}\le R,\qquad \eta_k\le b_k.
\tag{I15}
\]
在有效有限前缀，对 \(j<k\) 有
\[
 r_{k}\le f^{\,k-j}(r_j)+\sum_{i=j}^{k-1}\eta_i,\qquad
 f^m(t)\le(\nu\gamma m)^{-p_0}\quad(m\ge1).
\tag{I16}
\]
第一式由 \(r_{k+1}\le f(r_k+\eta_k)\le f(r_k)+\eta_k\) 和 \(f\) 的单调、非扩张性反复应用得到。第二式对精确标量轨道逐步比较 \(t^{-\nu}\)，遇零后右界显然成立。这里 \(r_k+\eta_k\le R\) 先由 \(r_k\le r_0+\sum_{j<k}\eta_j\) 保证。

当 \(k\ge n_0\)，令 \(j=\lfloor k/2\rfloor\) 可取 \(r_k\le A(k+n_0)^{-p_0}\)，其中
\[
 A=\max\{2^{p_0}(A_0+B),\ (4/(\nu\gamma))^{p_0}+2^{p_0}B\}.
\]
当 \(k<n_0\)，同一上界由 \(r_k\le r_0+E_0\) 得到。令 \(n=k+n_0\)。在 \(i=k,\ldots,k+n-1\) 的任意有效部分块上，平方能量给
\[
\beta\sum_i s_i^2
 \le r_k^2+\sum_i(2r_i\eta_i+\eta_i^2)
 \le (A+B)^2n^{-2p_0}.
\]
块内真实步长之和至多 \((A+B)n^{1/2-p_0}/\sqrt{\beta}+\sum_i\eta_i\)。随后每块的起点加当前 \(n\)，故 \(n\) 逐块加倍。于是对所有有限尾段都有界
\[
L(k)=\frac{A+B}{\sqrt{\beta}(1-2^{\,1/2-p_0})}(k+n_0)^{1/2-p_0}
       +B(k+n_0)^{-p_0}.
\tag{I17}
\]
若 \(L(0)+Bn_0^{-p_0}<\operatorname{dist}(x^0,H\setminus U)\)，到任意当前点的已走长度加下一试探输入扰动均留在 \(U\)。与 (I15) 的距离半径合用，归纳关闭每个有限前缀，因而所有允许轨道均可续，并有真实尾长、点误差 \(\le L(k)\)。这允许单次稀疏误差达到 \(k^{-p_0}\) 阶。条件也覆盖 \(\eta_k=O((k+1)^{-1-p_0})\) 的误差尾型，在相应局部初始余量内适用。当 \(q\le 2/3\)，后一个逐项包络允许 \(\sum\eta_k^{2-1/q}=\infty\)，因为 \((1+p_0)(2-1/q)\le1\)。

不带时序条件的 (I5) 没有统一的迭代计数率。即使 \(F(x)=x\)、\(\lambda=1\) 且 \(\mathcal J(x)=x/2\)，也可以使此类轨道压过任给预先指定的率 \(R_k\downarrow0\)。从零出发，在稀疏时刻 \(N_j\) 注入 \(b_j'>0\)，其余时刻误差为零。事先令 \(b_j'\) 小到 \(\sum_j(b_j')^{2-1/q}<\infty\) 并满足小窗预算，再取 \(N_j\) 使 \(R_{N_j+1}\le b_j'/j\)。此时 \(x^{N_j+1}\ge b_j'/2\)，而极限为零。该算子在 \(|y|\le1\) 满足任意 \(q\in(1/2,1)\) 的 C399 误差界与零缺陷。

有限长度定理识别出一个属于 \(S\) 的轨道极限。误差可以改变由同一初值选到的零点，例如 \(F(t,z)=(t,0)\) 的一次纯切向输入误差使最终 \(z\) 改变。一般没有有限次命中保证，已知精确半步迭代 \(x\mapsto x/2\) 从任意正点出发始终为正。相对误差一旦命中 \(S\) 就吸收，绝对误差还能将下一点推出 \(S\)。

<a id="dd2-inexact-shadow"></a>
## 退化 PPPA 的受扰 shadow

考虑带预条件算子 \(P=CC^*\) 的全松弛约化算法。在约化空间用 \(\lambda=1\) 的上述真图位移形式，令
\[
u_k=z^k+e_k,\quad
\bar x^k\in\mathscr R_{\rm sh}(u_k)=(P+A)^{-1}Cu_k,\quad
q_k=u_k-C^*\bar x^k,\quad z^{k+1}=u_k-q_k.
\tag{I18}
\]
于是 \(C^*\bar x^k=z^{k+1}\) 且 \(Cq_k\in A_{\mathcal R}\bar x^k\)。在上面任一有限长度条件下，\(z^k,u_k,z^{k+1}\to z^\infty\)，\(q_k\to0\)，且
\[
 \sum_{j\ge k}\|u_{j+1}-u_j\|
 \le\sum_{j\ge k}\|z^{j+1}-z^j\|+2\sum_{j\ge k}\eta_j .
\tag{I19}
\]
若恢复映射在实际输入集上有界，\(A_{\mathcal R}\) 对弱输入、强零残差 demiclosed，则任何弱聚点属于 \(\{x\in\operatorname{zer}A:C^*x=z^\infty\}\)。该纤维为单点时得到弱收敛。若每个实际选择满足单点 Lipschitz 估计
\(\|\bar x^k-x^\infty\|\le L\|u_k-z^\infty\|\) 且 \(x^\infty\) 属于该零纤维，则
\[
\|\bar x^k-x^\infty\|
 \le L\Big[\sum_{j\ge k}\|z^{j+1}-z^j\|+\eta_k\Big].
\tag{I20}
\]
因此 (I16)–(I17) 的点率与 (I9) 的点率传到 shadow。在后者使用 \(\eta_k\le\theta r_k/(1-\theta)\)，在前者使用 \(\eta_k\le E_k\)。若恢复还可对连续两次的任意允许选择用共同 Lipschitz 常数比较，则 (I19) 给出物理 shadow 的有限长度。只有 (I20) 时，稀疏脉冲的无率反例已可在 \(C=I\) 和一致 Lipschitz 恢复中实现。

[精确 PPPA 的完整反例](pppa_recovery.md#dd2-pppa-length) 也适用于误差为零的子类。单一极限锚的 Lipschitz 恢复在 C399 幂次下以 \(q>3/4\) 保证物理长度，全锚统一恢复的门为 \(q>2/3\)。二者的端点均有连续原图和唯一完整影子的反例。

若实际算法用 \(z^{k+1}=z^k-q_k\) 且仍在受扰输入 \(u_k=z^k+e_k\) 取见证，则投影关系为 \(C^*\bar x^k=z^{k+1}+e_k\)。这同时有输入误差 \(e_k\) 与输出误差 \(-e_k\)，可用前述双误差长度预算。对变松弛更新，需要按实际更新重新写出相应的投影关系。

## 研究依据和作用域

- C358 的原近端剪切已经确定 RLEB 的扰动搬运障碍。式 (I8) 的法向衰减为幂次，零缺陷锚定等式与 C399 的 Hölder 指数同时成立。故这里得到的是 DD2 自身的绝对误差指数边界。[C358](../common_structure/proximal_input_noise_transport.md) · [C399](../../canonical/dd2_power_defect_finite_length.md)
- C275 已将真实图见证用于 RLEB 的可计算停止余量。式 (I13) 用 DD2 同一步平方能量除以可计算的距离和上界。在一般非单调图上，近似图成员、内层实现成本、其他更新策略与公开优先性仍各有义务。[C275](../inexact_ppa/real_graph_stopping.md)
- Solodov–Svaiter 1999 的 Algorithm 1.1 之后已给出线性斜对称算子上纯非精确迭代的固定相对误差反例，并为带额外投影的更新另证收敛。Iusem–Pennanen–Svaiter 2003 的式 (6)–(9) 也明确使用不同的混合更新。这里的幂反例把比例压到零，并固定纯更新在 C399 临界系数下的精确范围。[Solodov–Svaiter 原文](https://w3.impa.br/~benar/docs/hyb-proj.pdf) · [Iusem–Pennanen–Svaiter 原文](https://nms.kcl.ac.uk/teemu.pennanen/iproxSIOPT.pdf)
- Wang–Li–Ng 2023 的正式摘要确认最大单调 Hilbert 算子的 Hölder 次正则下有 Rockafellar 型非精确 PPA 的强收敛和定量速率。摘要不足以核其误差假设、真实长度或逐项包含。Li–Mordukhovich–Zhu v1 的 Theorem 4.3 由 (H0)–(H3)、水平集有界与渐近收缩的误差控制推出有限长度，Theorem 4.4 另有基于函数的假设。本文的直接比较限于真实图扰动与距离平方耗散，全球优先未判定。[Wang–Li–Ng 正式摘要](https://doi.org/10.1137/22M152147X) · [Li–Mordukhovich–Zhu v1](https://arxiv.org/pdf/2406.13207v1)
