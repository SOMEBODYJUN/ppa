# 指定下降目标的双向补偿：原真残差与有符号锚下界

本页完成 S02.07，登记 C430。DD1 取同一个 \(\kappa<1\) 的目标 \(A(t)=\kappa t\)；DD2 先指定 \(A=\varphi\)，再问哪些 \(\Phi,\psi\) 能保证它。以下不把原非单调 \(\psi\) 代入物理步长，也不以空可行域充当成功下降。

<a id="dd2-compensation-contract"></a>
## 1. 对象、非空性与准确逐尺度界

固定 \(t,\lambda>0,c=A(t)\ge0\)，有限有符号数 \(\phi=\Phi(t)\)，以及 \(0\in D_\psi\subseteq[0,\infty)\)、有限非负函数 \(\psi:D_\psi\to[0,\infty)\)。默认类是维数至少二、允许选择闭非空目标 \(S\subseteq\operatorname{zer}F\) 的自由单边类。边的实际量为
\[
t=d(x,S),\quad a=d(y,S),\quad s=\|x-y\|,\quad
\rho=r_F(y),\quad u=\lambda\rho\le s,
\]
且某个 \(p\in P_S(x)\) 满足 \(\langle x-y,y-p\rangle\ge\phi\)，输出满足 \(a\le\psi(\rho)\)。真残差取完整输出纤维的下确界。定义和实现范围沿用 [C417](../../canonical/dd2_function_hypotheses.md#fh-raw-residual) 与 [C421](../../canonical/dd2_function_hypotheses.md#fh-envelope-explicit)。

若 \(\phi>t^2/4\)，没有合法边。否则置
\[
B=\frac{t+\sqrt{t^2-4\phi}}2,\quad
h=|B-t|,\quad \alpha=(t-B)_+,\quad E=t^2-2\phi=B^2+h^2.
\tag{RC1}
\]
准确域非空，当且仅当
\[
\exists\rho\in D_\psi:\quad \lambda\rho\le B,
\qquad \psi(\rho)\ge\alpha.
\tag{RC2}
\]
在已核非空的前提下，其最小共同输出上界为
\[
M_{\phi,\psi}(t)=
\sup_{\rho\in D_\psi,\lambda\rho\le B}
\min\{\psi(\rho),B,\sqrt{E-\lambda^2\rho^2}\}.
\tag{RC3}
\]
这是 C421 的非空时等值式。式中未筛选的每一行不必各自实现；实际行还须 \(\psi(\rho)\ge\alpha\)。输出零值的原域约束 \(a=0\Rightarrow\rho=0\) 也未删除。它们不改变 (RC2) 或已核非空时的上确界值。

本文说“允许”均同时要求 (RC2) 和 \(M_{\phi,\psi}(t)\le c\)。\(t=0\) 的吸收由[零尺度合同](../../canonical/dd2_function_hypotheses.md#fh-domains)另核，不由正尺度公式外推。

<a id="dd2-compensation-psi-cap"></a>
## 2. 给定 \(\Phi\)：哪些原残差值必须受控？

**定理 RC-A。** 固定 (RC1)。在 (RC2) 下，存在如下准确分类。

| 指定目标 | 允许的 \(\psi\) |
| --- | --- |
| \(0\le c<\alpha\) | 没有非空成功的原模；每条合法边都有 \(a\ge\alpha>c\)。 |
| \(c\ge B\) | 除 (RC2) 外不需额外限制。 |
| \(\alpha\le c<B\) | 恰须 \(\psi(\rho)\le c\) 对下述危险前缀 \(P_{t,c}\) 中每个原残差点成立。 |

这里
\[
P_{t,c}=D_\psi\cap[0,B/\lambda]
             \cap[0,\sqrt{E-c^2}/\lambda).
\tag{RC4}
\]
尤其平方能量端点是开端，根上限端点是闭端，不能统一改成一个闭区间。当 \(c<h\) 时 \(D_\psi\cap[0,B/\lambda]\) 的全体点都受帽；\(c=h\) 时恰排除根右端；\(c>h\) 时开端在根上限之前。

**证明。** 每条准确行的输出下端至少为 \(\alpha\)，上端至多为 \(B\)。在中间情形，\(\psi(\rho)>c\ge\alpha\) 已保证该行通过原域筛选。该行存在严格坏输出 \(a>c\)，当且仅当
\[
\lambda\rho\le B,\quad \psi(\rho)>c,
\quad B>c,\quad E-\lambda^2\rho^2>c^2.
\]
这正是危险前缀上违反点态帽。严格坏输出为正，因而不触发零输出例外。由 C417/C421 的原真残差单边实现，两向均为实际自由类的判定。端点说明来自 \(E=B^2+h^2\)。证毕。

**同一个 \(\psi\) 覆盖整个正距离窗。** 固定 \(\Phi,A\) 于 \((0,R]\)，先逐尺度核 \(\Phi(t)\le t^2/4\) 和 \(\alpha_t\le A(t)\)。若 \(A(t)\ge B_t\) 令 \(P_t=\varnothing\)，否则按 (RC4) 取 \(P_t\)。定义
\[
G(\rho)=\inf\{A(t):0<t\le R,\ \rho\in P_t\},
\qquad \inf\varnothing=+\infty.
\tag{RC5}
\]
同一个原模满足所有逐尺度合同，当且仅当 \(\psi(\rho)\le G(\rho)\) 于 \(D_\psi\)，并且每个尺度分别满足 (RC2)。这只是对所有帽取交集；\(G\) 允许为无穷，不强制原模非减。各 \(P_t\) 是相对于 \(D_\psi\) 的初始段，故 \(G\) 自身非减。此函数交集不单独保证存在一个满足正下界整窗条件的完整算子，完整图量词见 §5。

<a id="dd2-compensation-phi-budget"></a>
## 3. 给定 \(\psi\)：允许的有符号 \(\Phi(t)\) 区间

### 3.1 非空性的准确上端

定义
\[
f_t(\rho)=\max\{\lambda\rho,t-\psi(\rho)\},\quad
b=\inf_{\rho\in D_\psi} f_t(\rho),\quad
\beta=\max\{t/2,b\},\quad H=\beta(t-\beta).
\tag{RC6}
\]
由 \(0\in D_\psi\) 得 \(0\le b\le t\)，故 \(0\le H\le t^2/4\)。令 \(e_N=1\) 当且仅当 \(b<t/2\)，或者这个原下确界由某个 \(\rho\) 达到。所有且仅有下列 \(\phi\) 产生非空自由单边域：
\[
\mathcal N_\psi(t)=(-\infty,H)
\ \cup\ \begin{cases}\{H\},&e_N=1,\\\varnothing,&e_N=0.\end{cases}
\tag{RC7}
\]

**证明。** 对 \(\phi\le t^2/4\)，(RC2) 等价于存在 \(\rho\) 使 \(f_t(\rho)\le B\)。函数 \(B\mapsto B(t-B)\) 在 \([t/2,\infty)\) 严格递减。若 \(B>\beta\)，有原候选 \(f_t(\rho)<B\)；若 \(B<\beta\)，无候选。\(B=\beta\) 时，\(b<t/2\) 自动给候选，否则恰需原下确界达到。这证明 (RC7)，也包含无实根情形。这里不能把原候选的存在改成前缀上确界达到某阈值；[C429](../../canonical/dd2_function_hypotheses.md#fh-generalized-step-inverse) 只保证下确界等值，不保证首端可行。证毕。

例如 \(t=\lambda=1\)，\(\psi(\rho)=\rho\) 对 \(\rho<1/2\)，其余为零，给 \(b=1/2\) 但下确界不达到。因此 \(\mathcal N_\psi(1)=(-\infty,1/4)\)，重根上端确实不能加入。取 \(c=1/2\) 时每个非空尺度值均安全，仍不产生上端的实际边。

### 3.2 三个显式下界条件

取严格坏输出的残差层
\[
E_c=\{\rho\in D_\psi:\psi(\rho)>c\},\quad
q=\lambda\inf E_c,
\tag{RC8}
\]
空层规定 \(q=+\infty\)。若 \(q<\infty\)，令 \(e=1\) 当且仅当 \(q/\lambda\in E_c\)。首端归属是额外信息，不能由 \(q\) 的数值恢复。

**定理 RC-B。** 若 \(q=+\infty\)，所有 \(\phi\in\mathcal N_\psi(t)\) 都允许。若 \(q<\infty\)，允许的 \(\phi\) 恰为 \(\mathcal N_\psi(t)\) 与以下三个集合之并的交集：
\[
\begin{aligned}
\mathcal H_1&=\{\phi:\ c\ge t/2,\quad \phi\ge c(t-c)\},\\
\mathcal H_2&=\{\phi:\ \phi\ge(t^2-c^2-q^2)/2\},\\
\mathcal H_3&=\{\phi:\ q\ge t/2,\quad
 \bigl(\phi>q(t-q)\ \text{或}\ [\phi=q(t-q),\ e=0]\bigr)\}.
\end{aligned}
\tag{RC9}
\]
当某个前置条件不成立，对应集合为空。因而答案是一个可能为空、可能仅一个点的区间，上端由 (RC7) 决定。若希望只写一个下端，取所有有效条件的阈值之最小值；存在至少一个达到最小阈值的闭条件时包含下端，否则不包含。此后仍须与 \(\mathcal N_\psi(t)\) 相交。

**证明。** 在非空域使用 (RC3)。有 \(M_{\phi,\psi}(t)>c\)，当且仅当
\[
B>c,\quad E>c^2+q^2,\quad
\bigl(q<B\ \text{或}\ [q=B,e=1]\bigr).
\tag{RC10}
\]
若 \(q<B\) 且第二个严格不等式成立，由下确界定义，严格坏层中有实际点满足 \(\lambda\rho<\min\{B,\sqrt{E-c^2}\}\)。若 \(q=B\)，必须且只须层本身含有首端；平方能量不等式仍须严格。反向由任一严格坏候选立即成立。这一论证用的是非空时的共同上确界；它没有把未经筛选的每一行当成实际边。

对 (RC10) 取否定。第一项的否定 \(B\le c\) 在 \(B\ge t/2\) 上恰是 \(\mathcal H_1\)；第二项的否定是 \(\mathcal H_2\)。第三项的否定为 \(B<q\) 或 \(B=q,e=0\)，由根上支的严格单调性恰是 \(\mathcal H_3\)。这给出全部三门，没有假设 \(\psi\) 非减或连续。证毕。

对整个窗，(RC6)–(RC9) 在每个 \(t\) 给出 \(\Phi(t)\) 允许集合；不额要求跨尺度连续性。若只研究非负缺陷 \(D=-\Phi\ge0\)，再取 \(\phi\le0\) 并反转符号即可。不能先用 \([-\Phi]_+\) 擦掉正下界。

<a id="dd2-compensation-calibration"></a>
## 4. 标尺与开闭端点

**线性真残差。** 设 \(D_\psi=[0,\infty),\psi(\rho)=\ell\rho,L=\ell/\lambda>0\)。在 \(\alpha\le c<B\) 中，RC-A 变为
\[
LB\ge\alpha,\qquad
L\min\{B,\sqrt{E-c^2}\}\le c.
\tag{RC11}
\]
第一式保证非空。第二式由危险前缀上线性函数的上确界给出，开端也取同一上确界。RC-B 中则有 \(b=t/(1+L)\)、\(q=c/L\)、\(e=0\)，其三门给出同一结果。

特别取 \(L=\lambda=1,c=3t/4\)。这时 \(H=t^2/4\) 且非空上端达到；(RC9) 的三个下端为 \(3t^2/16,-t^2/16,3t^2/16\)，故完整的有符号区间是
\[
-t^2/16\le\Phi(t)\le t^2/4.
\tag{RC12}
\]
限制为 \(\Phi=-D\le0\) 即 \(0\le D(t)\le t^2/16\)，与 C400/C428 的实际闭图校准一致。

**相同逆值，不同安全端点。** 令 \(t=\lambda=1,c=1/2\)，比较
\[
\psi_c(\rho)=\mathbf1_{[2,\infty)}(\rho),\qquad
\psi_o(\rho)=\mathbf1_{(2,\infty)}(\rho).
\]
两者 \(b=1,H=0,e_N=1,q=2\)，但 \(e\) 分别为 1、0。允许区间分别是 \((-2,0]\) 与 \([-2,0]\)。在 \(\Phi=-2\) 时，第一原模的最优输出为 1，第二为 0；[完整图见证](../../canonical/dd2_function_hypotheses.md#fh-generalized-inverse-contract)保留闭图、覆盖及真残差。因此只存首端数值会给出错误预算。

**平方能量等号端点应保留为安全。** 取 \(t=\lambda=1,\Phi=0,c=3/5\)，令 \(\psi(4/5)=1\)、其余为零。危险前缀是 \([0,4/5)\)，不限制 \(4/5\) 的值。令 \(S=\{0\},J=P_S\cup\{((4/5,3/5),(0,3/5))\}\) 并反演 \(F=J^{-1}-I\)。特殊边有 \(s=\rho=4/5,a=3/5,t=1\)，锚积为零。所有底图输出属于 \(S\)，完整输出纤维给上述真残差，因此是完整闭覆盖例。若把危险前缀右端闭合，会排除这个确实成功的原模。

<a id="dd2-compensation-scope"></a>
## 5. 必须保留的类与量词

RC-A、RC-B 在自由单边类是充要判定，其反向使用 C417/C421 的完整真残差实现。二维及以上，C426 允许把目标取成闭凸线段，甚至预先固定的同一射线，仍保这些单边标量。

若 \(\Phi\le0\) 于整个 \([0,R]\)，\(U=H\)，且无额外输出位置限制，那么投影底图与辅助前像在整个窗均符合锚条件；每个正尺度的非空性已由 \((s,a,\rho)=(t,0,0)\) 保证。任一个违反的正尺度都能由一个完整闭图、全域非空近端关系实现，见 [C426 全纤维证明](target_geometry.md#dd2-convex-complete-fibers)。因此此类中逐尺度交集也是整窗所有算子在全部正尺度的统一距离保证的充要条件。零尺度仍按 §1 独立核验。实现算子可以随失败尺度变化；这不声称一个固定算子沿同一轨道达到所有逐尺度最坏值。

一般有符号 \(\Phi\) 下，两向公式仍给整窗完整图的充分条件，单边必要性不能自动转授。以下在 \(U=H\)、全部距离不超过 1 的输入均受检时，把 [C417 正下界前像障碍](../../canonical/dd2_function_hypotheses.md#fh-raw-residual) 写成一个连续目标的明确分离：
\[
\lambda=R=1,\quad \Phi(t)=3t^2/16,\quad
\psi(\rho)=\rho/3\ (\rho\ne1/100),\quad
\psi(1/100)=1/2,\quad
A(t)=\min\{3t/4,1/4\}.
\tag{RC13}
\]
每个整窗完整图的每条受检边都满足 \(a\le A(t)\)。根界先给 \(a\le3t/4\)。若 \(a>1/4\)，非尖峰残差会给 \(a\le\rho/3\le s/3\le t/4\le1/4\)，矛盾。因此 \(\rho=1/100\)、\(a\le1/2\)。从完整纤维选 \(v\in F(y)\)，令 \(q_v=\|v\|<1/50\) 和 \(w=y+v\)。有 \(d(w,S)\in[a-q_v,a+q_v]\subset(0,1)\)，故 \(w\to y\) 是同一窗内受检边。对其满足锚下界的最近锚 \(p_w\)，平方展开及 \(\|y-p_w\|\ge a\) 给
\[
3(a-q_v)^2/16\le\langle v,y-p_w\rangle
\le\frac{d(w,S)^2-q_v^2-a^2}{2}\le aq_v.
\]
但 \(q_v/a<2/25\) 时，\(3(1-2/25)^2/16=1587/10000>2/25\)，矛盾。此类非空，例如 \(F=3I,S=\{0\}\) 满足全部条件。另一方面在 \(t=1\)，自由类有 \(a=1/2>A(1)\)；RC-A 的危险前缀包含 \(1/100\)，故其点态帽失败。这严格证明一般正下界完整窗的必要性不能沿用单边式。

若另要求 \(S=\operatorname{zer}F\) 且纤维闭，必须保留 \(\rho=0\Rightarrow a=0\)。本页默认子零集类的零残差行不能原样转入该版本。将计算所用的有效原模在零处置为 0、其余点保持 \(\psi\)，便准确删除这些行后复用同一公式；\(\psi(0)=0\) 本来就自动消除该差异。固定算子、指定仿射目标、一维和轨道长度也分别有额外结构；本页没有把目标距离界升级成长度结论。

全部 inf/sup 和首端归属都是精确数学信息。对任意函数，它们不自动构成有限次点值查询可执行的算法；有限精度计算仍使用 [C421 的表示合同](../../canonical/dd2_function_hypotheses.md#fh-envelope-computation)。本页证明补偿判据，不认定公开新颖性。
