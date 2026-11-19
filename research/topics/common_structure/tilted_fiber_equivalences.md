# 倾斜纤维的两个真实距离与原 RLEB 的导入边界

**状态：C348-v1，`derived-checked`，共同结构任务未完成。** 独立冷审及主代理已核两等价、原允许图量词、模函数跳跃、可和性和有限前缀。其原 RLEB 下降被已有下逆关系的更强估计直接支配；倾斜距离关系没有在该行承担新机制，故不接收为当前任务的 \(M\)。

本文固定一个候选条件。它与先前只按选中值大小收取缺口的版本不同。以下 \(\theta\) 在整个定理中固定，\(0<\theta<1\)，也可一律取 \(1/2\)。两个等价、允许图的量词和保留原 \(\kappa\) 的导入是不同断言。公开新颖性与对研究目标的最终接收未定。

<a id="tilted-fiber-definition"></a>
## 1. 同一条件及其方向意义

给定 \(X=\mathbb R^n\)、\(F:X\rightrightarrows X\)、\(\lambda>0\)、非空闭 \(S\subseteq F^{-1}(0)\)、原图块 \(\Gamma\subseteq\operatorname{gph}F\)。写 \(\Gamma_y=\{v:(y,v)\in\Gamma\}\)，只测试 \(\Gamma_y\ne\varnothing\) 的输出。记 \(d(z)=\operatorname{dist}(z,S)\) 与 \(r_y=\inf_{w\in F(y)}\|w\|\)。后者始终为完整纤维下确界，允许没有达到。对 \((y,v)\in\Gamma\) 写

\[
 x=y+\lambda v,\quad t=d(x),\quad q=d(y),\quad s=\lambda\|v\|.
\]

取 \(m>0\) 和非减函数 \(\chi:[0,\infty)\to[0,\infty]\)，\(\chi(0)=0\)，要求 \(\chi(s)\) 在实际受检弦上有限。写 \(h=\chi(s)\)、\(b=\chi(\lambda r_y)\)。于是 \(0\le b\le h\)。定义倾斜纤维的下确界

\[
 I_{\theta,\chi}(y)=
  \inf_{v\in\Gamma_y,\ p\in S}
       \big[\|y-p+\lambda v\|^2-(1-\theta)\chi(\lambda\|v\|)^2\big].
\]

**定义。** \(M_{\theta}(m,\chi)\) 要求对所有受检 \(y\) 有

\[
 I_{\theta,\chi}(y)\ge q^2+\theta b^2+(mq-b)_+^2 .            \tag{1}
\]

右端的缺口是完整真残差的变换值 \(b\) 到 \([mq,\infty)\) 的欧氏距离。左端须支付此缺口的是允许纤维的每一条物理弦。对每一条实际弦先对 \(p\in S\) 取最小值，见证正是 \(P_S(x)\)，于是 (1) 当且仅当

\[
 t^2\ge q^2+(1-\theta)h^2+\theta b^2+(mq-b)_+^2
                 \quad ((y,v)\in\Gamma).                     \tag{2}
\]

从另一个原图值产生的 \(b\) 可以与受检弦的 \(h\) 不同。固定 \(q>0,h\) 时，\(\theta b^2+(mq-b)_+^2\) 在 \(0\le b\le mq/(1+\theta)\) 上下降，之后上升。故把 \(b\) 换成 \(h\) 一般没有固定的不等式方向。

<a id="tilted-fiber-equivalences"></a>
## 2. 独立结构定理与两个等价

取 \(S=p_0+L\) 仿射，\(F(y)\subseteq L^\perp\)，\(n=y-P_Sy\)。此合同允许任意单点目标；对单点不限制任何图值方向。此节固定 \(\chi(s)=s\)；两条等价使用同一定义、同一 \(m,\theta\) 及同一完整图窗 \(\Gamma_y=F(y)\)（\(y\in Y\subseteq\operatorname{dom}F\)）。记 \(r_\eta(y)=\operatorname{dist}(\eta,F(y))\)。因 \(v\in L^\perp\)，\(P_S(x)=P_S(y)\)，故 (2) 准确等价于

\[
 2\lambda\langle n,v\rangle+
      \theta\lambda^2(\|v\|^2-r_y^2)
                  \ge (m q-\lambda r_y)_+^2\qquad (v\in F(y)). \tag{3}
\]

**同一输出的两个真实右端。** 完成平方并对完整 \(F(y)\) 取下确界，(3) 等价于

\[
 \theta\lambda^2
 \left[
 r_{-n/(\theta\lambda)}(y)^2-r_0(y)^2-
                   \frac{\|n\|^2}{\theta^2\lambda^2}
 \right]\ge(mq-\lambda r_0(y))_+^2 .                          \tag{4}
\]

此处两个 \(r_\eta\) 都是同一原纤维的真实距离，通常由不同的图值给出。左端即 (3) 左端的下确界。若只核准 \(\Gamma_y\subsetneq F(y)\)，(3) 仍按允许的 \(v\) 为真，(4) 第一项必须换成 \(\operatorname{dist}(-n/(\theta\lambda),\Gamma_y)^2\)，第二个 \(r_0\) 仍取完整 \(F(y)\)。不从原 RLEB 的任意允许子关系推断完整图的方向。

**条件 \(A\) 及通常零锚单调的等价。** 假定 \(\lambda r_y\ge m d(y)\) 对全 \(Y\) 成立，且每个纤维的投影 \(\{\langle n,v\rangle:v\in F(y)\}\) 只有一个实数值。后者不规定正负。此类包含全部单值算子及同一输出上法向分量固定、其他分量可变的多值算子。若 \(S\) 有正维，此处“分量”是沿当前 \(n\) 的标量，与 \(L^\perp\) 的工作合同并行。则

\[
              M_\theta(m,\mathrm{id})
          \quad\Longleftrightarrow\quad
              \langle y-p,v\rangle\ge0
       (y\in Y,\ v\in F(y),\ p\in S).                          \tag{5}
\]

证明：在 \(A\) 下 (3) 右端为零，且 \(\langle n,v\rangle\) 等于仅依赖 \(y\) 的 \(\gamma_y\)。取完整纤维的近最小范数值，范数平方超额趋零，故 (3) 对所有值成立当且仅当 \(\gamma_y\ge0\)。又因 \(v\in L^\perp\)，有 \(\langle y-p,v\rangle=\gamma_y\) 对每个 \(p\in S\) 成立。在 \(S=\{0\}\)、\(Y=X\)、\(F\) 单值线性的子类，每个图对之差是一个原图点，(5) 进一步等价于通常全对单调。一般情况下结论为零锚单调。

**条件 \(B\) 及通常真正则的等价。** 假定每个原图值做非负零锚功，且对每个 \(y\in Y\) 存在 \(v_j\in F(y)\) 满足 \(\|v_j\|\to r_y\)、\(\langle n,v_j\rangle\to0\)。这规定最小范数可以由不做径向功的方向渐近实现，不限定 \(r_y/q\)。所有原图值与 \(n\) 正交足以逐纤维满足 \(B\)。则

\[
              M_\theta(m,\mathrm{id})\quad\Longleftrightarrow\quad
              \lambda\,\operatorname{dist}(0,F(y))\ge m d(y)
                                      \quad(y\in Y).            \tag{6}
\]

由 \(B\)，(3) 左端处处非负且下确界是零。故 (3) 当且仅当其右端为零，恰为 (6)。更一般，若完整纤维直接给出勾股等式
\(r_{-n/(\theta\lambda)}(y)^2=r_0(y)^2+\|n\|^2/(\theta^2\lambda^2)\)，则也有 (6)。该条件通过两个完整右端距离判断，允许个别较长值做负功。

定量地，(4) 说明若 \(\lambda r_0<mq\)，倾斜残差超过勾股基线的平方余量必须至少为 \((mq-\lambda r_0)^2/(\theta\lambda^2)\)。反之，独立给出的上界 \(D\) 若控制 (4) 左端，则 \(\lambda r_0\ge mq-\sqrt D\)。这是从倾斜方向的观测反推完整误差尺度的关系。它与只取某个实际 \(v\) 所得的同一弦恒等式不同。

<a id="tilted-fiber-convergence"></a>
## 3. 原步的下降、续接与点收敛

由 \(b^2+(mq-b)_+^2\ge m^2q^2/2\)，(2) 蕴含

\[
 t^2\ge (1+m^2/2)q^2+
                 (1-\theta)\big(h^2-b^2\big).                 \tag{7}
\]

当 \(b\le mq\) 时，被丢去的标量项恰为 \(2(b-mq/2)^2\)；\(b>mq\) 时最初不等式亦成立。式 (7) 保留同一实际步相对于完整最小残差的超额支付。由 (2) 还得 \(h\le t/\sqrt{1-\theta}\)。

固定开集 \(U\)、\(R>0\)，写 \(U_R=U\cap\{d\le R\}\)。对每个 \(x\in U_R\) 假定存在允许根 \(\varnothing\ne\mathcal J(x)\subseteq J_{\lambda F}(x)\)，且全部允许根之图值均属 \(\Gamma\)。令

\[
 \rho_m=(1+m^2/2)^{-1/2},\quad
 B_\chi(t)=\sup\{s\ge0:\chi(s)\le t/\sqrt{1-\theta}\},
 \qquad T_\chi(t)=\sum_{j\ge0}B_\chi(\rho_m^j t).
\]

标量数据须有 \(B_\chi(0)=0\)、\(B_\chi(t)\to0\) 当 \(t\downarrow0\) 及 \(T_\chi(R)<\infty\)。定义 \(D_0=\{x\in U_R:T_\chi(d(x))<\operatorname{dist}(x,U^c)\}\)，非平凡认证要求 \(D_0\setminus F^{-1}(0)\ne\varnothing\)。若 \(U\) 包含 \(S\cap\overline{X\setminus F^{-1}(0)}\) 中一点，此要求自动成立，因为支配收敛给 \(T_\chi(t)\to0\)。

对每条允许步有 \(q\le\rho_m t\)、\(s\le B_\chi(t)\)。从 \(D_0\) 任一点出发，对已在窗内的有限前缀用覆盖选取下一根。下一点距离至多 \(\rho_m^{k+1}d(x^0)\)，到起点的路长至多 \(\sum_{j=0}^k B_\chi(\rho_m^jd(x^0))<\operatorname{dist}(x^0,U^c)\)，因而下一点仍在 \(U_R\)。归纳给无限续接。尾和趋零，故每条允许原轨道在 \(X\) 中 Cauchy，距离趋零和严格留域余量使其极限在 \(S\cap U\)。这里使用的都是原步 \(x-y\in\lambda F(y)\)。

<a id="tilted-fiber-rleb"></a>
## 4. 固定原论文距离因子的非线性 RLEB 导入

采用当前投稿正文 P1–P4 的原允许关系，取 \(\Gamma_y=\{(x-y)/\lambda:x\in U_R,\ y\in\mathcal J(x)\}\)。每个实际步有自己的 \(p\in P_S(x)\) 满足 \(\|2y-x-p\|\le\omega(t)\)。比较 \(x-p\) 与 \(2y-x-p\) 得 \(s\le H(t)=(t+\omega(t))/2\)。因此 \(r_y\le s/\lambda\le H(R)/\lambda\le\bar t\)，可调用原完整残差界 \(q\le\psi(r_y)\)。保留原相容 \(\psi(H(z)/\lambda)\le\kappa z\) 对 \(0<z\le R\) 与 \(\sum_jH(\kappa^jR)<\infty\)。定义

\[
 L(s)=\inf\{z\in[0,R]:H(z)\ge s\},\quad
 a=L(\lambda r_y),\quad u=L(s),\qquad \inf\varnothing=+\infty .
\]

对每个见证 \(z>0\) 满足 \(H(z)\ge\lambda r_y\)，有 \(q\le\psi(r_y)\le\kappa z\)；若 \(z=0\) 是见证，则 \(r_y=q=0\)。对见证取下确界，得

\[
                   q\le\kappa a,\qquad 0\le a\le u\le t .     \tag{8}
\]

此步不要求 \(H(L(s))\ge s\)，因此允许原一般模在正点跳跃。

为使 (7) 输出**输入数据中已经给定的同一 \(\kappa\)**，固定

\[
 m=\frac{\sqrt{2(1-\kappa^2)}}{\kappa},\qquad
 c=\sqrt{(1-\kappa^2)/2},\qquad \chi=cL.                     \tag{9}
\]

第一式由 \(\rho_m=\kappa\) 唯一确定。第二式使残差侧的费用在名义刻度 \(q=\kappa a\) 对准 \(b=mq/2\)，即 (7) 中标量费用 \(b^2+(mq-b)_+^2\) 的唯一极小点。它也可由要求原直接标量数据无其他余量地给出 (2) 唯一推出：在 \(q=\kappa a,\ u=a=t\) 代入即需 \(\kappa^2+c^2+(m\kappa-c)_+^2\le1\)；固定该 \(m\) 后，左侧最小值为 \(1\)，唯一极小点 \(c=m\kappa/2\)。这是原指标的匹配，不主张每个真实算子均达到这些大小。

由于 \(m\kappa=2c\)、\(\kappa^2+2c^2=1\)，(8) 在同一实际步给出

\[
 \begin{aligned}
 q^2+(1-\theta)c^2u^2+\theta c^2a^2+(mq-ca)_+^2
 &\le[\kappa^2+(1+\theta)c^2]a^2+(1-\theta)c^2u^2\\
 &\le t^2 .
 \end{aligned}                                                \tag{10}
\]

这正是 (2)，且其中 \(a\) 来自完整纤维，\(u\) 来自允许值。特别地 (7) 给

\[
 t^2\ge \kappa^{-2}q^2+(1-\theta)c^2\{L(s)^2-L(\lambda r_y)^2\}.  \tag{11}
\]

在 \(\chi=cL\) 下，\(B_\chi(0)=0\)，且当 \(0<2t/(c\sqrt{1-\theta})<R\) 时，
\(B_\chi(t)\le H(2t/(c\sqrt{1-\theta}))\)，在其余正尺度上 \(B_\chi(t)\le H(R)\)。事实上 \(L(s)\le t/(c\sqrt{1-\theta})\) 允许取一个严格小于其两倍的见证 \(z\)，再用 \(s\le H(z)\) 与非减性。\(H(0)=0\) 且零处连续，所以 \(B_\chi(t)\to0\)。令 \(D=2/(c\sqrt{1-\theta})\)，取整数 \(\ell\ge0\) 使 \(D\kappa^\ell\le1\)。对大尺度的有限项直接界以 \(H(R)\)，其余有 \(H(D\kappa^jR)\le H(\kappa^{j-\ell}R)\)，原 Dini 采样遂给 \(T_\chi(R)<\infty\)。第三节因此对含非解的 \(D_0\) 适用。若需原文按 \(\sum_j H(\kappa^j d_0)\) 认证的全部初值，其较宽预算可由 (7) 的原 \(\kappa\) 与 P2 的原步长界直接作同一有限前缀证明。

**两种量词强度。** 若自由缩小 \(m,c\)，仅凭旧距离—步长结论 \(q\le\kappa t,s\le H(t)\) 已能以 \((1+m^2)\kappa^2+c^2\le1\) 吸收 (2)，无需 P3。这确实排除了把“存在某些小参数”称为从真残差到方向的新收敛机制。固定 (9) 时，只知 \(q\le\kappa t,u\le t\) 并不能推 (10) 的标量命题：在名义 \(q=\kappa t\)、\(a\downarrow0\) 时，单是 \(q^2+(mq-ca)_+^2\) 即趋于 \((2-\kappa^2)t^2>t^2\)。这一检验针对从这两个旧标量不等式进行的推理，并未宣称所有名义极值均被一个完整原算子实现。固定 \(\kappa\) 的 (10) 额外使用了 (8) 的完整纤维关系；(8) 本身是原 P2–P4、C315 已有的下逆转接。当前 P1 只约束允许子关系，添加漏检方向且不改 \(r_y\) 可保留全部原输入数据；本导入未对这些新方向声称任何信息。

<a id="tilted-fiber-boundary"></a>
## 5. 另一原始组合、先行关系与未决点

若全部受检图值对所有 \(p\in S\) 有 \(\langle y-p,v\rangle\ge-\eta\|v\|^2\)，输出均有 \(d(y)\le K r_y\)，取 \(\lambda>2\eta\)、\(\chi(s)=\delta s\) 其中 \(0<\delta\le\sqrt{1-2\eta/\lambda}\)，且 \(0<m\le\delta\lambda/K\)。平方展开对最靠近输入的 \(p\) 给 \(t^2\ge q^2+(1-2\eta/\lambda)s^2\)。而 \(b\ge mq\)、\(b\le h\)，于是 (2) 成立。全对单调和负共单调的零锚比较均可这样导入。残差帽与原根覆盖仍须在声明窗成立。此时 \(B_\chi\) 为线性函数，第三节的标量可和性成立。

Garciga Otero–Iusem 的 Proposition 5 与 Evens–Pas–Latafat–Patrinos 的 Definition 4.1 已分别给同一图弦长度的平方刻画和标准 \((\mu,\rho)\)-半单调预算；Ryu–Hannah–Yin 的 Theorem 4 给 SRG 的平移缩放。这些结论处理给定图对。式 (4) 的两项是对同一原纤维在两个不同右端分别取下确界的距离；式 (10) 则须区分完整零右端的下确界和允许原值的代价。仓库 C277 的联合原图数据足以**编码** (2)，故不能据此主张新证书语言。C285 已有一步最近锚能量，C315 已有 (8) 的完整残差下逆。C334 对全对 RL 图宽度的右端变化需要不同的比较量词。本文的具体比较对象是 (4)–(6) 的两个真实距离及保留给定 \(\kappa\) 时 (11) 的完整残差超额；尚未证明世界首创。

对 RLEB 这一行，不能把 (11) 的余量作为超出原半和数据的新下降定理。事实上 (8) 本身直接给 \(t^2\ge q^2/\kappa^2+[u^2-a^2]\)，还允许比 (11) 大的系数。只要求不带参数的点收敛且允许任意缩参时，上述自由缩小攻击也仍在。待审的是同一条件的两条通常性质等价、不同真实右端的转接，以及固定外给 \(\kappa\) 时它们与原一般模的具体关系。没有证明定性 PPA 的原 RLEB 机制必须经过 (4)。


<a id="tilted-fiber-reduction"></a>
## 6. 独立验收：固定原因子仍未关闭机制门

第 (8) 式的全部信息是
\[
 q/\kappa\le a\le u\le t.
\]
它直接给出
\[
 t^2-\kappa^{-2}q^2-(u^2-a^2)
       =(t^2-u^2)+(a^2-\kappa^{-2}q^2)\ge0.                 \tag{12}
\]
因为 \(0<(1-\theta)c^2<1\)，式 (12) 严格支配候选的 (11) 所需系数。推导 (12) 不使用第二节的倾斜残差、纤维投影单值或近最小零功条件。这是精确的承重缺口：固定原 \(\kappa\) 关闭了“任意缩小强度”的攻击，却没有关闭从旧完整残差下逆直接得到更强下降的归约。

C348 的可复用内容是第二节的两个原纤维距离、条件 (5)/(6) 的精确等价与相应参数强度。完整倾斜距离不从原允许 RLEB 自动导入，见 [C347 最大补全](residual_preserving_fiber_completion.md)。第一项改为允许纤维距离后，数学陈述仍正确，但其现有非线性 RLEB 导入依旧绕开了第二节的恢复机制。因此这里既不否定 (1)–(11)，也不声称已找到题目所求共同生成结构。

最近的内部关系：[C315 下逆及条件性角度](../../canonical/rleb_residual_filtered_angle.md)、[C277 联合原图证书](../../canonical/unified_ppa_joint_certificates.md)、[C285 最近输入锚几何](../../canonical/rleb_sharp_linear_frontier.md)。一手约定见 Gárciga Otero–Iusem [2010 作者稿 Proposition 5](https://webdoc.sub.gwdg.de/ebook/serien/e/IMPA_A/672.pdf)、Evens–Pas–Latafat–Patrinos [2305.03605v2 Definitions 2.1/4.1](https://arxiv.org/pdf/2305.03605v2) 与 Ryu–Hannah–Yin [Scaled Relative Graphs](https://arxiv.org/pdf/1902.09788)。平方恒等、SRG 表示和既有收敛后端不作为本文件的原创主张。
