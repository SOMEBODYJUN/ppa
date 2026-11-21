# 有限长度不要求给定积分候选：真误差模取等的双图

沿用 [E0](core.md#dd2-exact-contract) 的完整真残差和同一最近输入锚，预设目标由共同原数据认证。本页在 [F=I 配松半阶模](../../canonical/dd2_function_hypotheses.md#fh-length-boundaries) 之外，给出全域连续单值的径向／旋转配对。精确模仍可伴有限长度的现象在 C278 的 JP32–JP36 多值模型已有实例；这里新增的对象和比较范围如下，不把该现象说成首次发现。

<a id="dd2-sharp-gauge-finite-length-pair"></a>
## FG1 · C456-v1 的同模配对与准确范围

**状态：derived-checked。三席已独立重构并逐式复读实际正文、身份、图边与地图，未留下致命异议。**

对每个 \(m\ge2,R>0\)，共同固定
\[
H=\mathbb R^2,\quad S=\{0\},\quad\lambda=1,\quad
U=V_\psi=H,\quad D_\psi=[0,\infty),\quad
\psi_m(\rho)=\rho^{1/m},\quad\Phi=0 .
\tag{FG1}
\]
令 \(Q=R_{\pi/2}\)，定义全域连续单值
\[
F_{\rm rad}(y)=\|y\|^{m-1}y,\qquad
F_{\rm rot}(y)=\|y\|^{m-1}Qy .
\tag{FG2}
\]
两者精确零集都是 S，全部完整近端在全空间唯一可解，零输入驻定，距离 R 窗不变。每个输出都有
\[
\rho=s=a^m,\qquad a=\psi_m(\rho).
\tag{FG3}
\]
先指定共同目标
\[
h_{\rm rot}(a)=\sqrt{a^2+a^{2m}},\qquad
\varphi_m=h_{\rm rot}^{-1}\quad\text{于 }[0,R].
\tag{FG4}
\]
该目标由共同 E0 数据认证全部边，旋转逐步取等，径向在正尺度严格低于它。

两个图都从任意初点范数收敛到0，但
\[
\sum_{k\ge0}s_k=t_0\quad(F_{\rm rad}),\qquad
\sum_{k\ge0}s_k=\infty\quad(F_{\rm rot},\ t_0>0).
\tag{FG5}
\]
共同 C401/C419 候选 \(\chi_\Sigma=(\operatorname{id}+\psi_m)^{-1}\) 的积分在每个正上限发散。原 F1、F2 均满足，原 F3 失败。原 \(\psi_m\) 在全输出域逐点最小；更强的零端真误差模不存在。径向图的实际 \(s(t)=\chi_\Sigma(t)\)，故改选任何有效实际步下界也不能使这一积分模板有限，尽管该图有精确支付势 \(\Theta(t)=t\)。

## FG2 · 完整图、共同目标和最小误差模

令 \(h_{\rm rad}(a)=a+a^m\)。两个半径函数连续严格增、归零且满射。
对 \(x\ne0\)，径向图的唯一完整输出为
\[
a=h_{\rm rad}^{-1}(\|x\|),\qquad y=(a/\|x\|)x .
\tag{FG6}
\]
旋转图的 \(I+F_{\rm rot}\) 将半径 a 变成 \(h_{\rm rot}(a)\)，角度增加
\(\arctan(a^{m-1})\)。因此先唯一取 \(a=h_{\rm rot}^{-1}(\|x\|)\)，再令
\[
y=(I+a^{m-1}Q)^{-1}x
 =\frac{I-a^{m-1}Q}{1+a^{2m-2}}x .
\tag{FG7}
\]
该 y 的范数确为 a。两种 \(I+F\) 都为全域同胚，零输入取零，以上穷尽全部近端。F 单值，因此完整真残差就是所选图值范数，FG3 不隐藏其他纤维。

唯一最近输入锚为0，两种实际内积分别为
\[
\langle x-y,y\rangle=a^{m+1}\quad(F_{\rm rad}),\qquad
\langle x-y,y\rangle=0\quad(F_{\rm rot}).
\tag{FG8}
\]
所以它们共享原下界 \(\Phi=0\)，但径向图的最紧实际锚信息更强，不声称两图的最紧 \(\Phi\) 相同。对任意同数据 E0 边，
\[
a^m\le\rho\le s,\qquad
a^2+a^{2m}\le a^2+s^2\le t^2 .
\tag{FG9}
\]
这独立认证预设目标 \(\varphi_m\)。由于 \(h_{\rm rad}(a)>h_{\rm rot}(a)\) 于 \(a>0\)，径向后继严格小于原目标，旋转达到；全部实际距离窗不变。

对任意 \(r\ge0\)，任取 \(\|y\|=r^{1/m}\) 就在任一图的输出实现 \(\rho=r\)。任何对全部输出有效的真误差模因而必须满足
\[
\widetilde\psi(r)\ge r^{1/m}\quad(r\ge0).
\tag{FG10}
\]
在固定输入 R 窗内，对该图可达到的残差范围也逐点如此；该范围含一个零邻域。特别地，任意 \(q>1/m\) 和有限 K 都不能给局部 \(a\le K\rho^q\)，因为
\(a/\rho^q=a^{1-mq}\to\infty\)。这排除“仅仅选松误差模”的解释，不排除使用原图额外方向、锚或函数值信息。

## FG3 · 哪一条候选合同失败

令 \(c=\psi_m(\chi_\Sigma(t))\)，准确逆方程是
\[
t=c+c^m,\qquad\chi_\Sigma(t)=c^m .
\tag{FG11}
\]
故 \(c/t\to1,\chi_\Sigma(t)\sim t^m\)。在 \(0<t\le1\) 更有
\[
(t/2)^m\le\chi_\Sigma(t)\le t^m,\qquad
\int_0^\epsilon\frac{t}{\chi_\Sigma(t)}\,dt
\ge\int_0^{\min\{\epsilon,1\}}t^{1-m}\,dt=\infty.
\tag{FG12}
\]
原模连续严格增，因此准确原域 \(b_\psi=\chi_\Sigma\)。严格吸收没有失败：\(D=0\) 可用 \(\delta=1\)，是积分不满足。

原 \(b_{\rm inv}(u)=u^m\) 给 F2 \(b_{\rm inv}(u)=o(u)\)；F1 的 \(D\le b_{\rm inv}(t/2)^2/4\) 也成立。F3 需要支配的函数为
\[
t/b_{\rm inv}(t/2)=2^m t^{1-m},
\tag{FG13}
\]
不可积，因而没有可积支配函数。C453 删除 F2 不修复这里仍发散的 P。

更强地，径向的实际步长从 FG6、FG11 正好为 \(s(t)=\chi_\Sigma(t)\)。若 \(\widetilde b\) 是该固定图的任何正、可测的有效输入尺度步下界（特别包括 C419 的正有限非减下界），则对每个 \(0<t\le R\)
\[
\widetilde b(t)\le s(t)=\chi_\Sigma(t),\qquad
\int_0^R t/\widetilde b(t)\,dt=\infty .
\tag{FG14}
\]
因此失败不只属于默认的 \(b_\psi\)。这仅排除这类有效步下界的积分模板，绝非排除全部距离势。FG10 也表明，在零邻域改用别的有效原误差模不能改善这个积分。

## FG4 · 真实轨道和同一步支付

径向每步与输入同射线，
\[
t_k=t_{k+1}+t_{k+1}^m,\qquad
s_k=t_{k+1}^m=t_k-t_{k+1}.
\tag{FG15}
\]
连续严格下降及 \(h_{\rm rad}(a)>a\) 给 \(t_k\to0\)，故
\[
\sum_{j=k}^{\infty}s_j=t_k.
\tag{FG16}
\]
所以 \(\Theta(t)=t,C=1\) 精确支付这个完整固定图的全部边，且尾界取等。

旋转则有
\[
t_k^2=t_{k+1}^2+t_{k+1}^{2m},\qquad s_k=t_{k+1}^m.
\tag{FG17}
\]
同样 \(t_k\downarrow0\)，实际点因而趋零。对正边 \(a=t_{k+1},t=t_k\)，
\[
\int_a^t u^{1-m}\,du
\le a^{1-m}(t-a)
=\frac{a^{m+1}}{t+a}
\le \frac{s_k}{2}.
\tag{FG18}
\]
各相邻壳恰拼满 \((0,t_0]\)，左侧在零端发散，故每个正初距的实际总长度无限。初点零另为驻定轨道。这是同一个完整旋转的实际轨道，不是数值外推。

两图的精确平方差分别为 \(2as+s^2\) 和 \(s^2\)。共同原下界 \(\Phi=0\) 没有要求径向特有的额外 \(2as\) 或同向几何。固定图的 \(s=t-a\) 可直接望远镜，而统一类仍包含旋转坏图，符合 C420/C454 的必要性。旋转侧还排除任何有限且末值有下界的支付势，但不据此声称排除所有无下界实值势。

## FG5 · 径向图是真正的凸最小化近端

取 \(f(y)=\|y\|^{m+1}/(m+1)\)。范数凸且 \(r^{m+1}\) 在非负轴上凸、非减，所以 f 凸；直接微分得 \(\nabla f=F_{\rm rad}\)，零处导数为零。
对 \(x=y+F_{\rm rad}(y)\)，凸支撑式和平方展开给任意 z
\[
f(z)+\tfrac12\|z-x\|^2-
 \bigl[f(y)+\tfrac12\|y-x\|^2\bigr]
\ge\langle F_{\rm rad}(y)+y-x,z-y\rangle
       +\tfrac12\|z-y\|^2
=\tfrac12\|z-y\|^2.
\tag{FG19}
\]
故 FG6 就是这个全局最小化子问题的唯一解，不只是挑出的 stationary 根。该具体凸模型有精确半阶或更弱幂真误差界、真实有限长度，但不满足所指候选积分。没有宣称所有凸最小化近端都有同样预算，也没有认定公开新颖性。

C420 已给旋转的通用机制，C278 的 JP32–JP36 已有局部多值精确模正例。本配对的新增身份是全域连续单值、同一精确模与原目标、凸最小化正侧，以及正侧所有正可测有效步下界积分模板仍失败。所有有限实值距离势均不存在的更强否定属于 C278 的另一对象；[C457](angular_length_obstruction.md#dd2-angular-length-obstruction)在全域连续单值对象中排除有共同下界的距离势，仍允许无下界支付函数。C452 的不能规则化、C453 的有限 P 却不支付也各自保留原身份。
