# 原 F1–F3 的精确作用、等价可积性与条件删减

本页沿用 [E0](core.md#dd2-exact-contract)，原 \(\Phi\) 为同一最近输入锚的有符号下界，原 \(\psi\) 在完整真残差 \(\rho=r_F(y)\) 处评价，\(\rho\le s/\lambda\)。预设目标 \(\varphi\) 不由长度势替换。作者原 F1–F3 的现存转录和来源身份见[审计 §5.1](../../audit/FINAL_PROTOCOL_S4_S8_2026-11-21.md#dd2-original-f1-f3)；以下是独立推导，不声称本次重新取得了历史 509 行原附件。

<a id="dd2-original-f1-absorption"></a>
## FA1 · 原 F1 的版本、符号与本次核验对象

本节只核 S05.F1 的缺陷吸收，不提前签收 F2、F3 或整段望远镜任务。
当前可直接读取的版本记录是 [core §5](core.md#dd2-source) 与
[审计 §5.1](../../audit/FINAL_PROTOCOL_S4_S8_2026-11-21.md#dd2-original-f1-f3)：
它们将原式归于作者 509 行一般函数稿的“一般函数有限长度条件”一节，
登记原稿 SHA-256 为
 c834aeee5e134d3968a26d49ddec7b3ed416576b2806bf93b6267722d0d65213。
本次原字节及历史版本查核的结果在[专项来源记录](../../audit/FINAL_PROTOCOL_S4_S8_2026-11-21.md#dd2-f1-source-and-absorption)单列；
下面严格区分仓库存录公式与独立证明，不把本库弱化版追认成原稿。

据现存转录，原稿把普通逆模记为 \(\chi\)。本节为避免和函数逆混名，固定
\[
b_{\rm inv}(u)=\lambda\psi^{-1}(u),\qquad
q(t)=b_{\rm inv}(t/2),\qquad
\boxed{\text{原 F1：}\ D(t)\le\tfrac14q(t)^2
 =\tfrac{\lambda^2}{4}[\psi^{-1}(t/2)]^2.}
\tag{FA1}
\]
这里 \(\psi^{-1}\) 是原零点严格递增分支的普通逆；
半尺度在逆函数内，\(\lambda\) 在取逆后乘入，随后整体平方。
它不是 \((\operatorname{id}+\psi(\cdot/\lambda))^{-1}\)，
也不是给完整真残差换了定义。

## FA2 · 原域阈值先于吸收

保 E0 的同一实际允许边、同一最近输入锚 \(p\in P_S(x)\)，
\(\rho=r_F(y)\in D_\psi\)、\(a\le\psi(\rho)\)、\(\rho\le s/\lambda\)。
设 \([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在此连续严格增、
\(\psi(0)=0\)，且 \(R/2\le\psi(r_*)\)。
不限制原模在较大残差处的行为，不从一条选中图值反改完整纤维。
给定非负预算 \(D\)，保 \(\Phi\ge-D\)、FA1 于 \(0<t\le R\)。
同锚平方恒等式和 \(\|y-p\|\ge a\) 给下式的第一项；
距离函数的1-Lipschitz性独立给第二项：
\[
a^2+s^2\le t^2+2D(t),\qquad
t\le a+s .
\tag{FA2}
\]

对 \(0<v\le R/2\)，若 \(a\ge v\)，必有
\[
s\ge b_{\rm inv}(v).
\tag{FA3}
\]
否则真正的 \(\rho\le s/\lambda<\psi^{-1}(v)\le r_*\)
已经落在原严格分支里，故 \(a\le\psi(\rho)<v\)，矛盾。
这里在该反证分支才确定评价域；无需对任意大 s 在 \(s/\lambda\) 处代入原模。
这也是 FI13 的独立重构。

## FA3 · 原组合中的二分之一净余量

据现存转录的原 F1–F3 证明先利用 F2 缩窗。对本项所需的精确前件，
只写已取得的窗口不等式
\[
q(t)\le t/2\qquad(0<t\le R).
\tag{FA4}
\]
F2 如何保证此式、能否删去 F2 是各自的后续题与 C453；
本项不把 FA4 冒称 F1 本身的结论。

若 \(s<q(t)\)，三角式给 \(a\ge t-s>t/2\)，
而 FA3 用 \(v=t/2\) 又给 \(s\ge q(t)\)，矛盾。
因此每条正尺度允许边都有
\[
s\ge q(t)>0,\qquad
2D(t)\le\tfrac12q(t)^2\le\tfrac12s^2,\qquad
t^2-a^2\ge s^2-2D(t)\ge\tfrac12s^2\ge\tfrac12q(t)^2>0 .
\tag{FA5}
\]
这就是原 F1 如何吸收缺陷：其系数 \(1/4\) 经平方能量中的因子2，
留下统一净余量 \(1/2\)。F3 没有参与这个逐边代数；
有限长度还需自己的可积性和同一步支付，不由 FA5 自动取得。
式中 D 可取 \([-\Phi]_+\) 或已声明的更大非负预算；
不是把给定有符号 \(\Phi\) 的正信息认作不存在。
这个常数不是“保有某个正净余量”的必要系数：
在同一 FA4 窗内，若另取 \(D\le c q^2\)、\(0\le c<1/2\)，
同一代数给净余量 \(1-2c>0\)。这是另外的充分版本；
不把它改写为原 F1，也不据此认定任何精确最优常数。

零尺度另核：若 \(D(0)=0\) 且 \(\Phi(0)\ge-D(0)\)，则 p=x，
\(-s^2=\langle x-y,y-x\rangle\ge\Phi(0)\ge0\)，故 \(s=a=0\)。
正尺度 FA1 本身不补零输入条件。
反之，零输出 \(a=0\) 因 \(y\in S\subseteq\operatorname{zer}F\) 给 \(\rho=0\)；
若 \(t>0\)，仍有 \(s\ge t>0\)，
所以不能把零真残差误作零步。实际允许边的存在、全窗覆盖、
开工作域的位置预算和指定目标 \(a\le\varphi(t)\) 也仍各自核验。
FA5 给严格距离下降，不擅自把它改写为预先指定的某个更强目标。

## FA4 · 单有 F1 时能说什么，不能说什么

若删 FA4，仍可分两类得到 \(a<t\)：当 \(a\ge t/2\)，
FA3 给 \(s\ge q(t)\)，FA5 的净余量链在这类边上成立；
当 \(a<t/2\)，严格距离下降已成立，但不能沿用 \(s\ge q(t)\)。
因此“F1 给全部边统一平方余量 \(1/2\)”实际使用了缩窗前件。
原组合的证明没有循环地先假定 \(a<t\)，再评价输出尺度的函数。

这个限制是实际完整图上的现象。
复用 [C453/FI5](#dd2-f1-mixed-potential-example) 的
\[
H=U=V_\psi=\mathbb R^2,\quad S=\mathbb R\times\{0\},\quad\lambda=1,\quad
F(u,v)=(-\sqrt{|v|},7v),\quad
\psi(\rho)=\rho^2,\quad D(t)=t/8,\quad\Phi(t)=-t/8 .
\tag{FA6}
\]
完整 \(I+F\) 先由竖坐标 \(8v\) 反解，横坐标再唯一解出；
故 F 连续单值，完整近端全域唯一，零集精确 S，零输入驻定。
对正距离输入 t 的输出，
\[
a=t/8,\quad \rho=s,\quad
s^2=t/8+49t^2/64,\quad q(t)^2=t/2,\quad D=q^2/4 .
\tag{FA7}
\]
原误差界因 \(\rho^2=a+49a^2\ge a\) 成立，
实际最近锚内积为 \(-t/8+7t^2/64\ge\Phi(t)\)，
故这个窗的实际最小非负缺陷为 \(D_*(t)=t/8-7t^2/64<D(t)\)；
任意 \(0<R\le1/8\) 的距离带全覆盖且不变。
在这个窗，原数据本身也认证预设 \(\varphi(t)=t/2\)：
若 \(a\ge t/2\)，则 FA5 的高输出分支给
\(t^2-a^2\ge q(t)^2/2=t/4\)，
而 \(t^2-a^2\le3t^2/4<t/4\)，矛盾。
其实际平方降幅满足
\[
\frac{t^2-a^2}{s^2}
 =\frac{63t}{8+49t}\longrightarrow0\quad(t\downarrow0).
\tag{FA8}
\]
所以单有原 F1、完整真残差和覆盖，连任意正的共同平方余量都不能保证。
这里实际全轨有限长由 C453 的混合支付另证；
没有把统一平方余量失败说成真实有限长度失败。

## FA5 · 与和函数逆的合法对照

定义 \(H_\Sigma(s)=s+\psi(s/\lambda)\) 于原局部分支
\([0,\lambda r_*]\)，其像是 \([0,\lambda r_*+\psi(r_*)]\)，
\(\chi_\Sigma=H_\Sigma^{-1}\)。FA4 给
\(H_\Sigma(q(t))=q(t)+t/2\le t\)；
当 t 同时属于这个像时，可得
\[
q(t)\le\chi_\Sigma(t).
\tag{FA9}
\]
若 t 不在这个局部像内，不评价该逆；FA3–FA5 的直接残差证明仍有效。
原 F1 于是给 C401 同形的尺度吸收 \(2D\le\chi_\Sigma^2/2\)，
但这不把两个逆函数视为同一个函数，也不把这个更宽的吸收条件称为原 F1。
上述阈值、原系数和完整剪切只补核既有身份，不另登记同义 Claim。

<a id="dd2-original-f2-role"></a>
## FB1 · 原 F2 的精确对象与等价零端条件

沿用 [S05.F1 的来源界限](../../audit/FINAL_PROTOCOL_S4_S8_2026-11-21.md#dd2-f1-source-and-absorption)：
历史提交 d32b3f2e691c93f38a55fcee8ecda6ac46802546 的审计 §5.1
把原名 \(\chi\) 重标为 b，并存录 F2 为 \(b(u)=o(u)\)。
这里仍记 \(b_{\rm inv}(u)=\lambda\psi^{-1}(u)\)，
不将来源指纹记录当成本轮取得了原509行附件。

明确原分支：\(r_*>0\)，\([0,r_*]\subseteq D_\psi\)，
\(\psi:[0,r_*]\to[0,v_*]\) 连续严格增，\(\psi(0)=0\)，
\(v_*=\psi(r_*)>0\)，\(\lambda>0\) 固定。
普通逆定义在 \([0,v_*]\)。原 F2 及其等价写法是
\[
\boxed{b_{\rm inv}(u)=o(u)\quad(u\downarrow0)}
\quad\Longleftrightarrow\quad
\frac{\psi(r)}r\longrightarrow+\infty\quad(r\downarrow0)
\quad\Longleftrightarrow\quad q(t)=o(t).
\tag{FB1}
\]
第一项的 u 是误差界的值域尺度，r 是原残差尺度，不互换自变量。
证明只需
\[
\frac{b_{\rm inv}(\psi(r))}{\psi(r)}
 =\frac{\lambda r}{\psi(r)},\qquad
\frac{q(t)}t=\frac12\,\frac{b_{\rm inv}(t/2)}{t/2}.
\tag{FB2}
\]
连续严格增及零值保证 \(r\downarrow0\) 与 \(u=\psi(r)\downarrow0\)
双向对应。固定正 λ 不改变真假，但所得工作窗会依赖 λ；
不能据此自动处理没有共同上界的变参数。
F2 是所选原模的性质，不替代实际误差界 \(a\le\psi(\rho)\)，
也不要求原模在这个分支之外单调。

## FB2 · 小 o 提供窗口，但窗口不要求小 o

F2 保证对每个 \(\epsilon>0\)，存在兼容原逆域的 \(R_\epsilon>0\)，
使全部 \(0<t\le R_\epsilon\) 有 \(q(t)\le\epsilon t\)。
原证明取 \(\epsilon=1/2\)。对任一固定 \(R\le2v_*\)，准确等价为
\[
q(t)\le t/2\quad(0<t\le R)
\quad\Longleftrightarrow\quad
\psi(r)\ge\lambda r\quad
 (0<r\le\psi^{-1}(R/2)).
\tag{FB3}
\]
这是直接令 \(t/2=\psi(r)\) 换元得到的全窗非严格比较。
由 FB1 可先选 \(r_0\le r_*\)，使这项比较对 \(0<r\le r_0\) 成立，
再取 \(R'\le\min\{R_{\rm work},2\psi(r_0)\}\)，并把闭端点留在已知有效区间内。
它仅给存在足够小的窗，不替未给出有效模的任意函数提供数值认证半径。

在 FB3 的窗内，[FA3–FA5](#dd2-original-f1-absorption)从原真残差
证明 \(s\ge q(t)\)，然后原 F1 才给
\(t^2-a^2\ge s^2/2\)。原阈值
\(a\ge v\Rightarrow s\ge b_{\rm inv}(v)\)（\(0<v\le R/2\)）、同锚平方能量、
零输入驻定的单独前件都不使用 F2。
有限长度与可继续留在物理工作域仍需要其余前件，
也不能从 \(q=o(t)\) 推出某个统一 \(\kappa<1\)。

反向不成立：\(\psi(r)=\lambda r\) 时，
\(b_{\rm inv}(u)=u\)、\(q(t)=t/2\) 满足整个 FB3 窗，F2却失败。
因此不能把原证明使用的非严格窗条件改写成小 o 的必要性。

## FB3 · 两个逆的小 o 等价，不是两个逆的数值相等

定义
\[
H_\Sigma(s)=s+\psi(s/\lambda)\quad(0\le s\le\lambda r_*),\qquad
\chi_\Sigma=H_\Sigma^{-1}
 \quad\text{于 }[0,\lambda r_*+v_*].
\tag{FB4}
\]
设 t 同时满足 \(t/2\le v_*\) 和 \(t\le\lambda r_*+v_*\)。
由于 \(H_\Sigma(q(t))=q(t)+t/2\)，严格保序给
\[
q(t)\le\chi_\Sigma(t)
\quad\Longleftrightarrow\quad q(t)\le t/2.
\tag{FB5}
\]
原逆域条件 \(R/2\le v_*\) 本身不保证 t 在和函数的像内。
若另外 \(t\le v_*\)，则 \(H_\Sigma(b_{\rm inv}(t))=b_{\rm inv}(t)+t\)，
故 \(\chi_\Sigma(t)\le b_{\rm inv}(t)\)。
这些是不等式，不是把普通逆改名为和函数逆。

在各自零端的共同小窗，令 \(t=\lambda r+\psi(r)\)，直接有
\[
\frac{\chi_\Sigma(t)}t
 =\frac{\lambda}{\lambda+\psi(r)/r}.
\]
因此 F2 也等价于 \(\chi_\Sigma(t)=o(t)\)。
但不能进一步无条件声称 \(\chi_\Sigma(t)\sim b_{\rm inv}(t)\)。
下面给一个精确纯函数反例，不将它冒充实际轨道反例。

取 \(\lambda=1,c_n=2^{-n},h_n=c_n^2\)，\(n\ge2\)。
令 w(0)=0，在按自变量排列的全部节点
\[
(c_n,h_n),\qquad(c_n+h_n,2h_n)
\tag{FB6}
\]
之间线性插值，并在最右节点之后以正斜率线性延拓至无穷。
因 \(c_{n+1}+h_{n+1}<c_n\)、
\(2h_{n+1}=h_n/2<h_n\)，w 全域连续严格增且满射。
对 \(c_{n+1}\le u\le c_n\)，
\(0<w(u)/u\le h_n/c_{n+1}=2c_n\)，
所以 \(w(u)=o(u)\)。取原 \(\psi=w^{-1}\)，则 \(b_{\rm inv}=w\) 满足 F2。
然而在 \(t_n=c_n+h_n\) 上，
\[
\chi_\Sigma(t_n)=h_n,\qquad b_{\rm inv}(t_n)=2h_n,\qquad
\frac{\chi_\Sigma(t_n)}{b_{\rm inv}(t_n)}=\frac12.
\tag{FB7}
\]
因为 \(h_n+\psi(h_n)=h_n+c_n\)，这些等式是准确的。
靠近相同自变量不允许在任意单调逆内丢掉差值。
C458 的积分首项有自己的可积窗和积分比较证明，并未依赖这条错误点态等价。

## FB4 · 原 F2 不等于正则性强弱或有限长度门

对原幂模 \(\psi(\rho)=K\rho^\nu\)，\(K,\nu>0\)，
\[
\frac{b_{\rm inv}(u)}u
 =\lambda K^{-1/\nu}u^{1/\nu-1}.
\tag{FB8}
\]
当 \(0<\nu<1\) 时 F2 成立；\(\nu=1\) 时该比值为正的常数，
F2失败而 FB3 恰等价 \(K\ge\lambda\)，含等号；
\(\nu>1\) 时比值趋无穷，F2及任意充分小窗的FB3均失败。
同一残差上的 \(\psi\) 越小，输出误差界越强；
F2 的 \(\psi(r)/r\to\infty\) 正是所选上界在零端比每个固定线性上界更大。
它不证明原算子没有另一条更强线性界，
也不是一个“正则性越强越满足”的内在收敛条件。

以下完整模型分别划清必要性和充分性，均具有完整真残差、明确的指定目标和覆盖范围。

- \(H=\mathbb R^2,\lambda=1,F=I,S=\{0\},U=V_\psi=H\)，取
  \(\psi(\rho)=\rho,\Phi=D=0\)，预先 \(\varphi(t)=3t/4\)。
  完整近端 \(y=x/2\)，\(a=s=\rho=t/2\)，全域唯一且实际总尾为 t。
  原数据本身由 \(2a^2\le t^2\) 认证该目标。
  原 F1 和 F3（\(t/q(t)=2\)，常数主函数）成立，F2失败；
  原缩窗吸收仍成立。这已经排除 F2 对有限长度的必要性。
- [C453/FI5 的完整剪切](#dd2-f1-mixed-potential-example)进一步给
  \(\psi(\rho)=\rho^2\)、\(q(t)=\sqrt{t/2}\)，
  F2 和任意充分小窗的 FB3 都失败，但全部真实轨道有限长。
  其实际步为 \(\sqrt t\) 阶，原 P 差仅 \(t^{3/2}\) 阶。
  C453 保原 F1，并用与原 F3 等价的 \(P(R)<\infty\)，
  改用 \(W=\alpha P+\beta q\) 的三分支证明，
  是不同的充分版本；局部初值须重新核 \(W(t_0)<d(x^0,U^c)\)，
  不宣称全部旧 P 预算的初点自动适用新预算。
- [C456 的二维完整旋转](finite_length_countermodels.md#dd2-sharp-gauge-finite-length-pair)
  取 \(m=2,\lambda=1,F(y)=\|y\|Qy,S=\{0\},\psi(\rho)=\sqrt\rho,\Phi=D=0\)，
  保其预设 \(\varphi=(a\mapsto\sqrt{a^2+a^4})^{-1}\)。
  全域完整唯一近端有 \(s=a^2\)、\(t^2=a^2+a^4\)，
  F1、F2均成立，但每个正初距轨道点趋0而总长无限。
  原被积函数为 \(t/q(t)=4/t\)，所以 F3 失败；
  不能由 F2 单独、甚至 F1+F2，推出有限长度或统一距离比例。

普通逆的存在来自原分支的连续严格增合同；F2是在这个对象已定义后加的尺度条件。
一般 DD2 的非单调原 \(\psi\) 不必有这个普通逆，
可用 C419/C429 的原域残差下界；不能为了套 F2 默默更换原模和预设目标。
本节只签逆模条件的身份、作用和上述边界，不提前签 F3 或原望远镜专门条目。

<a id="dd2-original-f3-role"></a>
## FC1 · 原 F3 的精确被积函数与量词

沿用 FA1、FB1 已固定的来源层级：可读 Git 转录
d32b3f2e691c93f38a55fcee8ecda6ac46802546 的审计 §5.1
写的是普通逆 \(b_{\rm inv}(u)=\lambda\psi^{-1}(u)\)，及
\[
\boxed{\text{原 F3：}\quad
g(t):=\frac{t}{b_{\rm inv}(t/2)}
=\frac{t}{\lambda\psi^{-1}(t/2)}
\le\bar g(t)\quad(0<t\le R),\qquad
\bar g\text{ 非增且 }\int_0^R\bar g(t)\,dt<\infty.}
\tag{FC1}
\]
准确量词是存在同一个主函数支配整个工作窗；不是逐点选一个有限数，
也不是只在某条已选轨道上支配。主函数取在 \((0,R]\)，正点有限，
不另要求其在0有有限值；由 \(g>0\) 它亦为正。
“在零点可积”按非负反常积分理解；在正紧段不存在额外奇点。
不要求原 g 本身非增，不要求原 \(\bar g\) 连续或可微。

这里 \(r_*>0,\lambda>0\) 固定，
\([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在该分支连续严格增且 \(\psi(0)=0\)，
\(R>0,\ R/2\le\psi(r_*)\)。所以 \(q(t)=b_{\rm inv}(t/2)\)
在 \([0,R]\) 连续严格增，\(q(0)=0\)，正点为正；
原模在分支外的行为不参与普通逆的定义。
精确换元是
\[
P(R)=\int_0^R\frac{t}{q(t)}\,dt
=\frac4\lambda\int_0^{R/2}\frac{v}{\psi^{-1}(v)}\,dv.
\tag{FC2}
\]
半尺度在逆函数内；移到积分变量时会出现因子4和端点 \(R/2\)。
固定正 λ 不改变积分的敛散，但会改变势值及随后的局部预算。

下面 FI1 对更宽的正有限非减 q 证明 F3 与 \(P(R)<\infty\) 等价，
同时核最小非增主函数及其整窗常数；FI2 再核它与和函数逆积分的零端等价。
这些纯函数结论不使用 F1、F2 或实际轨道。
它们不把两套缺陷吸收前件视为相同，也不替代原完整真残差、预设目标和覆盖。

<a id="dd2-original-integrability-equivalence"></a>
## FI1 · 非增上包络与原积分的可积性等价

先只固定正、有限、非减的 \(q:(0,R]\to(0,\infty)\)，记
\[
g(t)=\frac{t}{q(t)},\qquad P(t)=\int_0^t g(u)\,du .
\tag{FI1}
\]
这里及下文积分在零端按非负反常积分理解，不要求被积函数在零点有限。
若存在非增、正点有限的 \(\bar g\ge g\) 且 \(\int_0^R\bar g<\infty\)，显然 \(P(R)<\infty\)。
反向若 \(P(R)<\infty\)，取
\[
h(t)=2\int_{t/2}^R\frac{dv}{q(v)},\qquad
\bar g_*(t)=\sup_{t\le u\le R}\frac{u}{q(u)} .
\tag{FI2}
\]
正下界 \(q(t/2)>0\) 使 h 在正点有限且连续，h 非增。对任意 \(u\in[t,R]\)，
\[
h(t)\ge2\int_{u/2}^u\frac{dv}{q(v)}
       \ge\frac{u}{q(u)};
\]
所以 \(h\ge\bar g_*\ge g\)。Tonelli 给
\[
\int_0^R h(t)\,dt
=2\int_0^R\frac{\min\{2v,R\}}{q(v)}\,dv
\le4P(R).
\tag{FI3}
\]
最小非增主函数的身份可以直接核验：
\(0<\bar g_*(t)\le R/q(t)<\infty\)，它非增，故可测。
任意非增的 \(\bar g\ge g\) 对 \(u\ge t\) 都有
\(\bar g(t)\ge\bar g(u)\ge g(u)\)，于是 \(\bar g\ge\bar g_*\)。
它还有更紧的整窗比较。对 \(t\le u\le R\)，由 \(1/q\) 非增，
\[
\frac{u}{q(u)}
\le\frac{t}{q(t)}+\int_t^u\frac{dv}{q(v)}
\le g(t)+\int_t^R\frac{dv}{q(v)}.
\]
取上确界并用 Tonelli，得
\[
P(R)\le\int_0^R\bar g_*(t)\,dt\le2P(R).
\tag{FI3a}
\]
常数2在上述正非减分母类不能降低：\(q\equiv c>0\) 给等号。
即使限于连续严格增且延零的普通逆型分母，取 \(R=1,q(t)=t^\alpha\)，
\(0<\alpha<1\)，也有 \(\bar g_*\equiv1,\ P(1)=1/(2-\alpha)\)，
比值 \(2-\alpha\uparrow2\)。这里没有假定 F2；
这是主函数积分的整窗常数，不是实际轨道长度的最佳常数。

因此三种条件等价：原 g 可积；其最小非增上包络可积；存在原 F3 所需的非增可积主函数。
对任一合格 \(\bar g\)，
\(G(t)=\int_0^t\bar g(u)\,du\) 在 \([0,R]\) 连续、严格增、凹，\(G(0)=0\)；
它在整个 \([0,R]\) 绝对连续，且对 \(0\le a\le t\le R\) 有
\(G(t)-G(a)\ge P(t)-P(a)\)。
最后这一差分比较来自被积函数的支配，不能仅从 \(G\ge P\) 的点态大小推出。
构造的 h 连续，故其 G 在 \((0,R)\) 为 \(C^1\)，R 端取左导数。
原普通逆使 q 连续时，g 连续，紧段上的尾最大值 \(\bar g_*\) 也连续：
把两下端点间删去的一小段用该紧段上 g 的一致连续模控制即可。
于是最小主函数积分在原合同下也为正窗 \(C^1\) 的凹势。
一般有跳跃的非减 q 不自动给这一连续性。

FI3 的四倍和 FI3a 的两倍都只比较同一整个 R 窗的积分；
不能把固定 h 或固定 \(\bar g_*\) 的较小尾段直接写成至多 \(4P(t)\) 或 \(2P(t)\)。

这是 [C406](inexact.md) 与 [PR4a–PR4b](potential_regularity.md#dd2-potential-regularity) 的同一支配机制。删除证明中的“非增上包络”步骤，使前提更便于核验，但在这个正非减分母范围内没有扩张零端可积的函数类。若另要求 \(\bar g(0)\) 为有限值，则已加入更强条件，不属于这里的等价。

## FI2 · 原 F3 积分与和函数逆积分

设 \([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在该区间连续严格增，\(\psi(0)=0\)，\(\lambda>0\)。只在这一分支定义
\[
b_{\rm inv}(v)=\lambda\psi^{-1}(v),\quad
q(t)=b_{\rm inv}(t/2),\quad
H(s)=s+\psi(s/\lambda)\quad(0\le s\le\lambda r_*).
\tag{FI4}
\]
H 连续严格增，其像为 \([0,\lambda r_*+\psi(r_*)]\)。在共同小窗
\[
0<R_0\le\min\{R,\psi(r_*)\}
\]
定义 \(\chi_\Sigma=H^{-1}\) 和 \(I_\Sigma(t)=\int_0^t u/\chi_\Sigma(u)\,du\)。
此处 R 是 q 的工作上限，须有 \(R/2\le\psi(r_*)\)。原模在 \([0,r_*]\) 以外可另有行为，不在此处作连续非减延拓。

对 \(0<t\le R_0\)，令 \(m=\min\{t/2,q(t)\}\)。它在 H 的定义域且 \(H(m)\le t\)，从而
\[
\min\{t/2,q(t)\}\le\chi_\Sigma(t),\qquad
\chi_\Sigma(t/2)\le q(t).
\tag{FI5}
\]
第二式由 \(H(q(t))=q(t)+t/2\ge t/2\) 得到；这里没有在超出定义域的 t 处评价 H。于是
\[
I_\Sigma(R_0)\le2R_0+P(R_0),\qquad
P(R_0)\le4I_\Sigma(R_0/2).
\tag{FI6}
\]
因为分母正且非减，离零紧段上的两个积分均有限。因此原 F3、\(P(R)<\infty\) 和和函数逆的零端可积性等价，完全不使用 F2 \(b_{\rm inv}(t)=o(t)\)。这不等于两套长度定理的全部前提等价：它们吸收同一 D 的条件还不同。

即使原模在较大残差处不单调，\(\chi_\Sigma\) 仍是上述局部尺度的有效步下界。若 \(s<\chi_\Sigma(t)\)，则真正
\(\rho\le s/\lambda<\chi_\Sigma(t)/\lambda\le r_*\)，所以此时才可在原分支比较
\(t\le a+s\le\psi(\rho)+s\le H(s)<t\)，矛盾。这不许可对一般大 s 无条件作 \(\psi(s/\lambda)\) 替换。

## FC2 · 原 F3 的端点、单调性与尾段边界

**被积函数无需非增，主函数也无需零点有限。** 取
\[
q(t)=t^{3/2}(2+\sin\log t),\qquad t>0,\quad q(0)=0.
\tag{FC3}
\]
它连续严格增，因为
\(q'(t)=t^{1/2}[3+\tfrac32\sin\log t+\cos\log t]
\ge(3-\sqrt{13}/2)t^{1/2}>0\)，且 \(q(t)=o(t)\)。
但
\[
g'(t)=-\frac{t^{-3/2}[1+\tfrac12\sin\log t+\cos\log t]}
                 {(2+\sin\log t)^2}
\]
在 \(\log t=7\pi/6-2\pi n\) 处为正，在 \(\log t=-2\pi n\) 处为负。
因此任意充分小窗内 g 都不是非增函数。
另一方面 \(\tfrac13t^{-1/2}\le g(t)\le t^{-1/2}\)，
\(\bar g(t)=t^{-1/2}\) 就是可积非增主函数。
若强加非增 \(\bar g(0)<\infty\)，会要求全部正点值不超过该有限数，
与 \(g(t)\to\infty\) 矛盾。
这个例子确属原普通逆型：固定 \(\lambda=1,R>0,r_*=q(R)\)，
取 \(\psi(r)=q^{-1}(r)/2\) 于 \([0,r_*]\)，即得
\(\psi^{-1}(t/2)=q(t)\) 和 \(R/2=\psi(r_*)\)。

**固定光滑主函数的尾可能明显放大。** 取 \(R=1\)，
\(q(t)=t/\log(e/t)\) 于 \((0,1]\)，延 \(q(0)=0\)。
它连续严格增且 \(o(t)\)，仍可按上式给出原普通逆分支。
此时 g 本身已非增，但 FI1 中式 (FI2) 的固定构造 h 给
\[
\begin{aligned}
g(t)&=\log(e/t),&
P(t)&=t[\log(e/t)+1],\\
h(t)&=\log^2(2e/t)-1,&
\int_0^t h(u)\,du
 &=t[\log^2(2e/t)+2\log(2e/t)+1].
\end{aligned}
\tag{FC4}
\]
因此 \(\bigl(\int_0^t h(u)\,du\bigr)/P(t)\to\infty\)；不是仅仅常数4不够。
其机制由精确恒等式
\[
\int_0^t h(u)\,du
=4P(t/2)+2t\int_{t/2}^R\frac{dv}{q(v)}
\]
看清：同一个 h 保留了较大尺度的贡献。
可以在较小窗重新构造主函数，但不能说那仍是原固定 h。
这里另选最小主函数 \(\bar g_*=g\) 就不会放大，
所以反例不否定存在更精细的主函数。
固定最小主函数也没有普遍的尾常数2：
\(q(t)=\sqrt t,R=1\) 给 \(\bar g_*\equiv1\)，
\(\bigl(\int_0^t\bar g_*(u)\,du\bigr)/P(t)=3/(2\sqrt t)\to\infty\)。

**删除分母保序会使等价失败。** 这是原严格逆类之外的纯函数边界。
令 \(R=1,c_n=2^{-n},\epsilon_n=2^{-3n},H_n=2^n/n\)，\(n\ge2\)，
\[
g(t)=t^{-1/2}
 +\sum_{n\ge2}H_n
 \max\{1-|t-c_n|/\epsilon_n,0\},\qquad q(t)=t/g(t).
\tag{FC5}
\]
尖峰支撑两两不交，正紧段上只有有限项，故 g、q 在正窗连续，
\(q>0\) 且 \(q(t)\le t^{3/2}=o(t)\)，可连续延零。
三角峰的面积是 \(H_n\epsilon_n=2^{-2n}/n\)，所以 \(\int_0^1g<\infty\)。
任意非增 \(\bar g\ge g\) 在 \((c_{n+1},c_n]\) 上至少为 \(H_n\)，
故其积分至少为 \(\sum_{n\ge2}(c_n-c_{n+1})H_n
=\sum_{n\ge2}1/(2n)=\infty\)。
这里 q 确实不非减：在峰左端 \(q(c_n-\epsilon_n)=(c_n-\epsilon_n)^{3/2}\)，
而 \(q(c_n)\le n2^{-2n}\)，两者之比后者/前者趋0。
这不反驳 FI1 的带保序命题，也不能给一般非单调原 \(\psi\) 擅造一个普通逆。

以上三例的结论均在纯函数层，不冒称完整近端轨道反例。
在轨道层，F3 是所选积分证书的门，不能视为固定图有限长度的内在必要条件。
[C456 的两个完整模型](finite_length_countermodels.md#dd2-sharp-gauge-finite-length-pair)
共用 \(\lambda=1,\psi(\rho)=\sqrt\rho,\Phi=D=0\) 和已认证的同一预设目标，
有 \(q(t)=t^2/4,\ g(t)=4/t\)，所以 F3 均失败；
对任一正初距，径向图的真实总长却恰为初距，旋转图的真实总长无限；
零输入在两个模型中均驻定。
普通逆、和函数逆及主函数的比较没有消除这种固定图与全部数据类的区别。
本项只验 F3 的原式、函数条件与这些边界；原组合的同一步支付、
望远镜求和及物理留域在 S05.TELESCOPE 独立验收。

<a id="dd2-original-f1-without-f2"></a>
## FI3 · C453-v1：保持原 F1 不变的混合支付势

**状态：derived-checked。** 三席分别独立重构原逆域、积分等价和三分支支付，并复读实际终稿、完整剪切、身份与图边；零尺度、窗口、原目标及历史来源范围已核，无未关闭实质异议。

固定实 Hilbert 空间、非空闭 \(S\subseteq\operatorname{zer}F\)、\(\lambda>0\)、开工作域 U 和距离半径 \(R>0\)。允许关系在
\(U_R=\{x\in U:d(x,S)\le R\}\) 非空；对每条受检边保原 E0，包括最近输入锚存在、完整真残差属于 \(D_\psi\) 及原误差界。
设 \([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在该区间连续严格增、\(\psi(0)=0\)，且
\[
R/2\le\psi(r_*),\quad q(t)=\lambda\psi^{-1}(t/2)\ (0\le t\le R),\quad
P(t)=\int_0^t\frac{u}{q(u)}\,du,\quad P(R)<\infty .
\tag{FI7}
\]
q 在原窗连续严格增且 \(q(0)=0\)。保留作者原 F1 常数和同一 D：
\[
D(0)=0,\quad D(t)\ge0,\quad
\Phi(t)\ge-D(t)\quad(0\le t\le R),\qquad
D(t)\le\frac14q(t)^2\quad(0<t\le R).
\tag{FI8}
\]
不假设 F2，不限制原模在其余评价域的单调性。定义
\[
\alpha=\frac{16\sqrt3}{3},\quad
\beta=3+2\sqrt3,\qquad
W(t)=\alpha P(t)+\beta q(t).
\tag{FI9}
\]
则每条允许边满足
\[
a<t\quad(t>0),\qquad
s\le W(t)-W(a),\qquad
s=a=0\quad(t=0).
\tag{FI10}
\]
W 非负、连续、严格增且零端归零。对已从原数据另行认证的预设目标仍保 \(a\le\varphi(t)\)；FI10 不把 W 冒充目标。若
\[
x^0\in U_R,\qquad W(t_0)<d(x^0,U^c),
\tag{FI11}
\]
则全部允许轨道可续、留在 \(U_R\)，趋于 \(S\cap U\) 中一点，并满足
\[
\sum_{j\ge k}\|x^{j+1}-x^j\|\le W(t_k)\longrightarrow0.
\tag{FI12}
\]
在 \(U=H\) 无位置边界。上述常数是明确充分常数，不声称最优。

### FI4 · 原域反推与三种步的完整证明

**阈值引理。** 对 \(0<v\le R/2\)，若 \(a\ge v\)，则
\[
s\ge b_{\rm inv}(v).
\tag{FI13}
\]
否则真正 \(\rho\le s/\lambda<\psi^{-1}(v)\le r_*\)，已自动落在原严格分支中，于是
\(a\le\psi(\rho)<v\)，矛盾。没有在较大残差处代换原 \(\psi\)，也没有预先假定 \(a\le R\)。

同一锚的平方展开和原 F1 给
\[
a^2+s^2\le t^2+\tfrac12q(t)^2.
\tag{FI14}
\]
若 \(a\ge t/2\)，FI13 先给 \(s\ge q(t)>0\)，故
\(\Delta=t^2-a^2\ge s^2/2>0\)，证明 \(a<t\)。另一种情况 \(a<t/2\) 自带严格下降。所以先证明了 \(a<t\le R\)，才在后面评价 q(a) 和 P(a)。再由 FI13 用 \(v=a/2\) 得 \(q(a)\le s\)；a=0 时亦成立。

1. 若 \(a\ge t/2\)，q 非减和上式给
   \[
   P(t)-P(a)\ge\frac{\Delta}{2q(t)}
                 \ge\frac{s^2}{4q(t)}\ge\frac{s}{4}.
   \tag{FI15}
   \]
2. 若 \(a<t/2\) 且 \(q(t)\le2t\)，FI14 给 \(s\le\sqrt3t\)，而
   \[
   P(t)-P(a)\ge\int_{t/2}^t\frac{u}{q(t)}\,du
       =\frac{3t^2}{8q(t)}\ge\frac{3t}{16}.
   \tag{FI16}
   \]
   故 \(s\le\alpha[P(t)-P(a)]\)。
3. 若 \(a<t/2\) 且 \(q(t)>2t\)，置 \(\theta=\sqrt3/2<1\)。FI14 给
   \(s\le\theta q(t)\)，而 \(q(a)\le s\le\theta q(t)\)，从而
   \[
   s\le\frac{\theta}{1-\theta}[q(t)-q(a)]
        =\beta[q(t)-q(a)].
   \tag{FI17}
   \]

三种情况都被 FI9 支付。零输入时最近锚 p=x，
\(-s^2=\langle x-y,y-p\rangle\ge-D(0)=0\)，所以驻定。
有限前缀望远镜给总长至多 W(t0)，FI11 支付第一条拟出界边，因而所有选择留在 U，严格降距保距离窗。非空覆盖遂给续接。

若距离极限为 \(\ell>0\)，相邻距离比趋于1，最终全属第一种情况；那时
\[
t_k^2-t_{k+1}^2\ge\tfrac12q(t_k)^2
                       \ge\tfrac12q(\ell)^2>0,
\]
矛盾。因此 \(t_k\to0\)，W 的零端连续性给 FI12。有限长度给范数 Cauchy；S 闭和距离趋零识别目标，严格位置预算把极限留在 U。不需要 F 本身闭图。

在 E0 和上述局部原逆合同内，原 F1 已足以独立认证连续的安全目标
\[
A_{F1}(t)=\max\left\{\frac t2,
       \sqrt{\bigl[t^2-\tfrac12q(t)^2\bigr]_+}\right\}<t
       \quad(t>0),\qquad A_{F1}(0)=0 .
\tag{FI18}
\]
它不必非减。若先指定 \(\varphi\ge A_{F1}\)，上述原数据认证该目标；更小的预设目标必须另核。证明用实际净下降而非盲目复合 FI18。

<a id="dd2-f1-mixed-potential-example"></a>
## FI5 · 完整连续剪切说明 F2 可删而势的修正有内容

取 \(\lambda=1,H=\mathbb R^2,U=V_\psi=H,D_\psi=[0,\infty)\)，
\[
S=\mathbb R\times\{0\},\quad
\psi(\rho)=\rho^2,\quad \Phi(t)=-t/8,\quad D(t)=t/8,\quad
R=1/8,\quad \varphi(t)=t/2 .
\tag{FI19}
\]
原 \(b_{\rm inv}(v)=\sqrt v\)、\(q(t)=\sqrt{t/2}\) 满足 F1 等号；F2
\(b_{\rm inv}(t)=o(t)\) 失败。原
\[
P(t)=\frac{2\sqrt2}{3}t^{3/2}
\tag{FI20}
\]
有限，且 \(t/q(t)=\sqrt{2t}\) 被常数 \(\sqrt{2R}\) 非增主函数支配。
预设 \(\varphi=t/2\) 由同一数据认证全部 E0 边：若 \(a\ge t/2\)，FI15 前的能量给
\(t^2-a^2\ge t/4\)，但左侧至多 \(3t^2/4<t/4\) 于 \(0<t\le R\)，矛盾。

定义完整全域连续单值算子
\[
F(u,v)=(-\sqrt{|v|},\,7v),\qquad
J_{\!F}(u,v)=(u+\sqrt{|v|/8},\,v/8).
\tag{FI21}
\]
\(I+F\) 是全域同胚，故第二式确为全部近端且唯一；精确零集就是 S。
对输出 \(y=(u,v)\)，令 \(a=|v|\)，则输入
\(x=(u-\sqrt a,8v)\)、\(t=8a\)，最近输入锚 \(p=(u-\sqrt a,0)\)。直接算出
\[
\rho=s=\sqrt{a+49a^2},\quad
a\le\psi(\rho),\quad
\langle x-y,y-p\rangle=-a+7a^2\ge-t/8 .
\tag{FI22}
\]
零输入驻定、全部输入覆盖、正距离窗不变；实际 \(a=t/8<\varphi(t)\)。
沿任意 \(t_0>0\) 的真实轨道，\(t_k=8^{-k}t_0\)，并有
\[
\frac{\sqrt{t_k}}{\sqrt8-1}
\le\sum_{j\ge k}s_j
\le
\sqrt{1+49t_k/8}\,
\frac{\sqrt{t_k}}{\sqrt8-1}.
\tag{FI23}
\]
故真实尾长等价于 \(\sqrt{t_k}/(\sqrt8-1)\)。横向尾移恰为该无额外根因子的量；点极限及长度都存在。

然而 \(s\ge\sqrt{t/8}\)，\(P(t)-P(t/8)=O(t^{3/2})\)，所以任何固定有限倍的原 P 都不能支付这个同一图的全部小尺度边。新 q 项恰有实际需要的 \(\sqrt t\) 量级。
同一数据的 \(\chi_\Sigma+\chi_\Sigma^2=t\) 给 \(\chi_\Sigma\le t\)，原 C401 吸收条件也失败。甚至对这个固定图，任一有效步下界 \(\widetilde b(t)\le s(t)\) 都不能修复它：
\[
2D(t)=t/4>s(t)^2=t/8+49t^2/64
\quad(0<t\le R<8/49).
\tag{FI24}
\]
所以不只是默认候选选得不佳。这里放宽的是原 F2 及统一严格吸收所用的机制，FI1–FI6 的零端可积性本身未变。该结果不替代 C424 的消失余量判据，也不宣称公开新颖性、最优常数或原 F1 的必要性。

<a id="dd2-original-telescope"></a>
## FT1 · 原 F1–F3 的同一步势与轨道合同

本节独立重构仓库存录组合的数学充分性；来源和原附件未重获的边界仍同 FA1、FB1、FC1。
先直接用普通逆构造 P，再恢复原主函数积分 G；不要求借道和函数逆或扩张原 \(\psi\) 的定义域。
采用 [E0](core.md#dd2-exact-contract) 及其已核的 [Hilbert 正向传递](core.md#dd2-exact-versions)：
实 Hilbert 空间 H、非空范数闭 \(S\subseteq\operatorname{zer}F\)、固定 \(\lambda>0\)，
开工作域 U、\(R>0\)、\(U_R=\{x\in U:d(x,S)\le R\}\)。
对每个 \(x\in U_R\) 的每个允许输出 \(y\in\mathcal J(x)\subseteq J_{\lambda F}(x)\)，
保完整真残差、原误差界及某个同一最近输入锚的有符号下界。
最近锚的存在是逐边前件；无限维中不由 S 闭自动取得。
若另有输出位置窗 \(V_\psi\)，E0 对这些全部输出已有效，不能等到证明 \(y\in U\) 后才补误差界。
本段不预设 \(y\in U_R\)。

固定 \([0,r_*]\subseteq D_\psi\)，原 \(\psi\) 在此连续严格增且 \(\psi(0)=0\)，令
\[
R/2\le\psi(r_*),\qquad q(t)=\lambda\psi^{-1}(t/2),\qquad
q(t)\le t/2\quad(0<t\le R).
\tag{FT1}
\]
q 在 \([0,R]\) 定义，连续严格增且 \(q(0)=0\)。
原 F2 保证可缩窗取得最后一式；缩窗后的初值也须满足 \(t_0\le R\)。
取非负 D，使
\[
\Phi(t)\ge-D(t)\quad(0\le t\le R),\quad D(0)=0,\qquad
D(t)\le\tfrac14q(t)^2\quad(0<t\le R).
\tag{FT2}
\]
保原 F3 的同一非增可积主函数 \(\bar g\ge g=t/q(t)\)，并记
\[
P(t)=\int_0^t\frac{u}{q(u)}\,du,\qquad
G(t)=\int_0^t\bar g(u)\,du,\qquad P(0)=G(0)=0.
\tag{FT3}
\]
两者均有限、非负、连续且严格增；以下 B 固定选 \(4P\) 或 \(4G\)，不可在支付与预算间换对象。
所有允许边满足
\[
a<t,\quad s\le B(t)-B(a)\quad(t>0),\qquad
a=s=0\quad(t=0).
\tag{FT4}
\]
另有 \(\mathcal J(x)\ne\varnothing\) 对全部 \(x\in U_R\) 时，
任一初值 \(x^0\in U_R\) 满足
\[
B(t_0)<d(x^0,U^c),\qquad t_0=d(x^0,S),
\tag{FT5}
\]
则每种允许选择都可无限续接、始终留在 \(U_R\)，有限长并强收敛至 \(S\cap U\) 中一点。
约定 \(d(x^0,\varnothing)=+\infty\)，所以 \(U=H\) 时无位置预算限制。
若预设 \(\varphi\) 已由原数据或另一个有效证明认证，则同时保 \(a\le\varphi(t)\)；
本节的势和推导出的降距界均不替换该预设目标。

## FT2 · 先取得输出尺度，再证明差分支付

对 \(t>0\)，假设 \(s<q(t)\)。
这时才有 \(\rho\le s/\lambda<\psi^{-1}(t/2)\le r_*\)，
真实残差自动落入原严格分支，故 \(a\le\psi(\rho)<t/2\)。
另一方面 \(t\le a+s\)、\(q(t)\le t/2\) 给 \(a\ge t-s>t/2\)，矛盾。
并没有预设所有实际残差都在这个分支。
同一最近输入锚的平方展开遂给
\[
s\ge q(t)>0,\qquad
\Delta:=t^2-a^2\ge s^2-2D(t)\ge\tfrac12s^2
\ge\tfrac12q(t)^2>0.
\tag{FT6}
\]
先得到 \(0\le a<t\le R\)，才评价 q(a)、P(a)、G(a)。
由 q 非减，
\[
P(t)-P(a)
\ge\frac{t^2-a^2}{2q(t)}
\ge\frac{s^2}{4q(t)}
\ge\frac{s}{4}.
\tag{FT7}
\]
当 \(a=0\) 时仍是合法的零端积分，不能把 \(P(0)\) 与 \(g(0)\) 混为一谈。
原 \(\bar g\ge g\) 给 \(G(t)-G(a)\ge P(t)-P(a)\)。
也可独立使用原 F3 的非增性：
\[
G(t)-G(a)\ge\bar g(t)(t-a)\ge\frac{t(t-a)}{q(t)}
>\frac{\Delta}{2q(t)}\ge\frac{s}{4}.
\tag{FT8}
\]
这条 G 差分支付在取得 FT6 后不需 q 保序；直接 P 路线用的是 q 保序。
距离趋零所需的正紧段下界仍另核：原 q 非减给出该下界，
或由 \(g(t)\le\bar g(t)\) 和 \(\bar g\) 非增得到
\(q(t)\ge\ell/\bar g(\ell)>0\) 于 \(t\in[\ell,R]\)，\(\ell>0\)。
两者不能同时随意删除各自的比较前件。
系数4是这里的明确充分常数，不宣称长度最优。

零输入时 \(p=x\)，
\(-s^2=\langle x-y,y-x\rangle\ge\Phi(0)\ge0\)，所以 \(s=a=0\)。
正输入若直接落到 S，虽然 \(a=\rho=0\)，仍有 \(s\ge t>0\)；
FT7、FT8 没有把这种终止步漏掉。零驻定和输出真残差0是不同断言。

## FT3 · 有限前缀留域、距离极限及点识别

先取任意有限允许段 \(x^0,\ldots,x^N\)，只假设其输入
\(x^i\in U_R\) 对 \(0\le i<N\) 成立，不预设末输出在 U。
逐边 FT4 已使全部末尺度都落在 \([0,R]\)，故
\[
\|x^N-x^0\|
\le\sum_{i=0}^{N-1}s_i
\le B(t_0)-B(t_N)
\le B(t_0)<d(x^0,U^c).
\tag{FT9}
\]
因此 \(x^N\in U_R\)，这时才调用该点覆盖选择下一步。
这个归纳包含第一条拟出界边，适用于每种有限选择，因而可续接全部允许轨道。
仅在已假定无限合法轨道上求和，不能替代这一步。

对这些已经证明合法的轨道，任意 \(N>k\) 有
\[
\sum_{i=k}^{N-1}s_i\le B(t_k)-B(t_N)\le B(t_k).
\tag{FT10}
\]
非负和取极限给有限长度和每尾预算。
距离 \(t_k\) 非增；若其极限 \(\ell>0\)，
FT6 给每步平方降幅至少 \(q(\ell)^2/2>0\)，与平方距离非负矛盾。
故 \(t_k\to0\)，再由 B 零端连续，尾预算 \(B(t_k)\to0\)。
有限长度使 \(x^k\) 为范数 Cauchy，Hilbert 完备性给强极限 \(x^\infty\)；
S 范数闭且距离趋零给 \(x^\infty\in S\)。
同一个 FT9 的严格内含闭球给 \(x^\infty\in U\)，因此
\[
\sum_{i\ge k}s_i\le B(t_k),\qquad
\|x^k-x^\infty\|\le B(t_k),\qquad
x^\infty\in S\cap U.
\tag{FT11}
\]
实际输出真残差还满足 \(\rho_k\le s_k/\lambda\to0\)，但点识别没有依赖 F 的闭图。
若某步 \(t_k=0\)，后续由零驻定恒定，上述证明仍适用。
只有受检范围内全部原近端输出均被允许并满足前件时，才能转授给全部原近端选择；
\(\mathcal J=J_{\lambda F}\) 在整个 \(U_R\) 上成立是一个明确充分保证。

**原公式的预算等号也可处理。** 原 q 严格递增，
FT7 的第一个积分比较对每条正尺度边严格，故
\(s<B(t)-B(a)\) 对 \(B=4P\) 成立；\(B=4G\) 亦由 FT8 严格。
如果把 FT5 换成 \(B(t_0)\le d(x^0,U^c)\)，
对 \(t_0>0\) 任意选出的第一边记
\[
\epsilon=B(t_0)-B(t_1)-s_0>0.
\tag{FT12}
\]
所有包含它的前缀（含只走第一步的段）和极限位移都至多
\(B(t_0)-\epsilon<d(x^0,U^c)\)。
所以原公式保此严格支付时，非严格初始预算也是充分版本。
\(\epsilon\) 可以依赖第一边，不宣称它对全部选择有共同正下界。
\(t_0=0\) 由开域和驻定直接处理。
这个变体不把任意抽象的非严格支付都升级为边界安全，也不认证预算最佳。

**闭目标的另一个替代合同。** 原 E0 仍保 S 闭。
若明确改为任意非空 S，但保全部 \(U_R\) 上覆盖、逐边最近锚及已证极限在 U，
则对任意 \(z\in\overline S\cap U\)，有 \(d(z,S)=0\)，
覆盖取得一条边，其最近输入锚 p 必满足 \(\|z-p\|=0\)，所以 \(z\in S\)。
也就是说这些全窗前件已强制 S 在 U 内相对闭，足以识别同一极限。
该替代版本甚至无需先规定窗外的 \(S\subseteq\operatorname{zer}F\)：
在 \(z\in S\cap U\) 调用覆盖、零驻定及 \(\mathcal J\subseteq J_{\lambda F}\)，就有 \(0\in F(z)\)。
它不推出任何窗外包含；也不能在只给沿途覆盖、未覆盖限点时使用。
FT2 的零输出 \(\rho=0\) 说明按原 E0 保留；该说明不是支付和留域证明的前提，
在此替代合同下只在锁定输出位置并核过覆盖后使用局部识别。

## FT4 · 哪些条件可省，哪些必须换证明或换预算

以下均保具体受检对象和原预设目标；“可替代”不表示回改历史原式。

| 条件或辅助对象 | 本次核定的准确作用与删改范围 |
| --- | --- |
| 原 F2 的小 o | 系数4证明只需 FT1 的实际窗口，或已独立证明全部受检边 \(s\ge q(t)\)。小 o 不是这些结论的必要条件。 |
| 实际 \(q\le t/2\) 窗口 | 有共同有限 \(q(t)\le Kt\) 时还可用同一 P、但需下面的新系数；无任何替代时，C453 剪切反驳任何固定倍的原 P 通用支付。C453 的混合 W 是另一已证充分选择，不断言所有可用势都必须采用该形式。 |
| 原 F1 及系数 \(1/4\) | 不能无替代删除缺陷控制。\(D\le c q^2,\ 0\le c<1/2\) 加原窗口给净余量 \(1-2c\) 和支付系数 \(2/(1-2c)\)；须用这个新系数核预算，不称其为原 F1。也可另证真实净耗散或支付。 |
| 非负预算 D | 这是保 signed 下界的辅助记号。可直接写 \(\Phi(t)\ge-q(t)^2/4\) 及零条件；不能把原正 \(\Phi\) 误作只有负部。 |
| F3 的显式非增主函数 | P 路线只需 \(P(R)<\infty\)。FI1 证明这在原分母类与 F3 等价，所以不是严格放宽可积性。G 路线可用原主函数保序；若从 P 差转授，仅需可积密度逐点支配。 |
| 积分的有限性 | 保证本势有限和零端归零。不能从“被积函数在每个正点有限”代替零端积分，也不能无替代删去并声称全类有限长；C456 正初距旋转反驳。它不对每个固定好图必要。 |
| 和函数逆、全域 \(\psi\) 正则性 | 本证明不使用 \(\chi_\Sigma\)，不需原分支外单调、连续或延拓。删普通逆分支本身须改用 C419/C429 已证有效步下界，不能保符号而删定义。 |
| \(\varphi\) 的连续性或非减性 | 本长度证明不使用它们；原指定 \(a\le\varphi(t)\) 的认证仍须保留，不能由此认证任意更强目标。 |
| 零驻定 | \(\Phi(0)\ge0\) 可由实际允许零边恒等替代；仅 \(\varphi(0)=0\) 不能替代。若命中 S 就停止，应明确是另一算法约定。 |
| 覆盖、位置和闭性 | 已知合法无限路径可只验路径估计；从初值保证可续须核覆盖。给定初值可只在全部可达合法前缀末输入核覆盖，限点识别的替代则还要覆盖限点。已知全选择留域可替换预算的留域用途，但极限在开 U 内仍另核；FT12 和相对闭性给出这里可用的具体加强。 |
| 维数、图闭、单值性与残差取到 | 本正向证明不需有限维、F 闭图、F 单值或真残差达到，但保 Hilbert 完备性和逐边最近锚。只取某个非最近零锚不能替代同一最近输入锚。 |

共同线性帽的系数可以直接复算。保原 F1、F3，设 \(q(t)\le Kt\)，\(0<K<\infty\)；
FA4 节（删除窗口）的高低输出分支先给 \(a<t\)。
当 \(a\ge t/2\) 时仍有 \(s\le4[P(t)-P(a)]\)；
当 \(a<t/2\) 时
\[
s\le\sqrt{1+K^2/2}\,t,\qquad
P(t)-P(a)\ge\frac{3t^2}{8q(t)}\ge\frac{3t}{8K}.
\tag{FT13}
\]
故 \(C_K=\max\{4,(8K/3)\sqrt{1+K^2/2}\}\) 是同一 P 的明确充分系数。
用 \(C_KP(t_0)<d(x^0,U^c)\) 重做 FT9–FT11 即得相应结论；
距离正极限也由高分支的 q 正下界或低分支的至少减半排除。
该系数不声称最优。无共同有限 K 时，C453 使用
\(W=(16\sqrt3/3)P+(3+2\sqrt3)q\)，按其自身严格位置预算核初值；
不能把旧 P 预算的全部初点自动转授给新 W。

## FT5 · 与删项一一对应的完整边界

**零驻定不能由正尺度 F1–F3 补出。**
复用[两零点完整投影加交换边](../../canonical/dd2_function_hypotheses.md#fh-zero)：
\(\lambda=1,H=U=\mathbb R,S=\{-1,1\}\)，
\(J=P_S\cup\{(-1,1),(1,-1)\}\)，\(F=J^{-1}-I\)。
图闭、全部近端覆盖、零集恰为 S；每个输出都在 S，完整真残差都是0。
将该图原误差模明确换成 \(\psi(\rho)=\rho^{2/3}\)，不会改变任何受检误差界。
取 \(R\le1\)、预设 \(\varphi(t)=t/2\)，正 t 上 \(\Phi(t)=D(t)=0\)，
但零点 \(\Phi(0)=-4,D(0)=4\)。
于是正尺度 F1、F2、F3 和 \(q(t)=(t/2)^{3/2}\le t/2\) 全成立，
零输出目标也成立，却有 s=2 的实际零距离二周期。
缺的正是零端驻定下界；这不是原 FT2 的反例。

**F2、F3 和严格目标不能替代缺陷吸收。**
复用 [C401 严格余量门的完整临界旋转](../../canonical/dd2_function_hypotheses.md#fh-length-boundaries)，
固定 \(H=U=V_\psi=\mathbb R^2,\lambda=1,\psi(\rho)=\rho^{2/3},0<R\le1\)，
令 \(c+c^{3/2}=t,\ D(t)=c^3/2,\ \Phi=-D\)，并明确指定
\(\varphi(t)=A(t)\)，其中 \(A(t)^2+A(t)^3=t^2+c^3\)。
所有同数据原边都满足 \(a^3\le s^2\) 和
\(a^2+s^2\le t^2+c^3\)，故原目标认证，且 \(A(t)<t\)。
该源构造的全域同胚 J 反演出连续单值完整 F，精确零集为 \(\{0\}\)，
全部受检输入唯一覆盖且窗口不变；实际
\(a=A(t),\rho=s=a^{3/2}\)，锚积恰为 \(-D\)。
本节原普通逆给
\[
q(t)=(t/2)^{3/2},\quad g(t)=2^{3/2}t^{-1/2},\qquad
D(t)\ge t^3/16>q(t)^2/4=t^3/32.
\tag{FT14}
\]
因此保 F2、F3 和实际缩窗，但违反原 F1。
对任一正窗初距，真实 \(t_k\to0\)，且
\(\log(t_k/t_{k+1})\le6\,2^{3/2}s_k\)；
对数差求和发散，故真实长度无限。
这里只否定无任何替代吸收地删 F1，不声称原 \(1/4\) 是必要常数。
反向删 F3 的完整见证仍是 C456 的 \(m=2\) 旋转，
取 \(0<t_0\le R\le1\) 保实际 \(q(t)=t^2/4\le t/2\) 窗；
去掉 F2 且没有线性帽的原 P 支付障碍仍是 C453 的剪切。

**位置留域与极限位置是两个问题。**
以下两个定位例均取 \(\lambda=R=1,S=\{0\},V_\psi=H\)，
\(\psi(\rho)=\rho^{2/3},\Phi=D=0\)。
它们都满足正尺度 F1–F3、实际 \(q\le t/2\) 及完整近端覆盖。

- 在 \(\mathbb R^2\) 取 \(Q(u,v)=(-v,u)\)、\(F=Q\)，
  完整 \(J=(I+Q)^{-1}\)，预设 \(\varphi(t)=t/\sqrt2\)。
  实际 \(a=\rho=s=t/\sqrt2\le1\)，故原误差界成立，锚积为0。
  取开域 \(U=\mathbb R\times(-1/4,1/4)\)，
  \(x^0=(1,0)\in U_R\) 的第一步为 \((1/2,-1/2)\notin U\)。
  距离下降及完整覆盖并不补物理位置预算。
- 在 \(\mathbb R\) 取 \(F=I,J=I/2,U=(0,1)\)，
  预设 \(\varphi(t)=t/2\)，实际 \(a=\rho=s=t/2\)。
  每个允许输入的输出仍在 U，所有选择始终留域。
  然而 \(0<x^0\le1/2\) 的极限为 \(0\in S\setminus U\)，
  真实总长恰等于 \(x^0=d(x^0,U^c)\)。
  这时原 \(4P(x^0)=16\sqrt{2x^0}\) 预算不通过，
  所以不反驳 FT12 的原公式等号版本；
  它反驳从抽象总长非严格边界或全程留在开域直接推限点在域内。

**只沿途覆盖不能替代非闭目标的限点识别。**
这是明确改动 E0 的目标闭性和全窗覆盖后的对照。
取 \(H=U=\mathbb R^2,\lambda=R=1\)，完整连续单值
\[
F(u,v)=(v,v),\qquad J(u,v)=(u-v/2,v/2),\qquad
S=(\mathbb R\setminus\{0\})\times\{0\}.
\tag{FT15}
\]
允许关系只在输入第一坐标 \(u\ne0\) 时采用这个唯一完整输出，其余输入为空。
对受检边，最近锚 \(p=(u,0)\in S\)，
\(t=|v|,\ a=t/2,\ \rho=s=t/\sqrt2\)，锚积为0。
\(\psi(\rho)=\rho^{2/3},\Phi=D=0,\varphi(t)=t/2\)，
因 \(\rho\le1\) 有 \(\psi(\rho)\ge\rho\ge a\)，
在该窗给原正尺度 F1–F3；受检零输入也驻定。
从 \(x^0=(t_0,t_0)\)、\(0<t_0\le1\) 出发，
所有有限输入都有允许边，轨道为 \(x^k=2^{-k}x^0\)，有限长，
却趋于 \((0,0)\notin S\)。
限点没有允许边且没有最近 S 锚，正是 FT3 的相对闭性替代所不能丢掉的部分。
完整 F 与允许子关系始终分别给出，不把未受检的完整输出冒充已满足 E0。
