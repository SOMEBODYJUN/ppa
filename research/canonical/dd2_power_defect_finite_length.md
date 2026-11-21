# DD2 的幂次缺陷、Hölder 误差界与有限长度

<a id="dd2-power-regime-mechanisms"></a>
## PM1 · 三个幂指数区间来自两种几何约束

本节的 \(q>0\) 始终是 \(\psi(\rho)=K\rho^q\) 的常数幂指数，
不是原 F1–F3 中记作 q(t) 的位移函数。
沿用 [E0](../topics/dd2/core.md#dd2-exact-contract) 的完整真残差、
同一最近输入锚、允许关系及零、覆盖和局部位置范围。
固定 \(K,\lambda>0,M\ge0,p>0\)，本节比较的是幂次子合同
\[
\Phi(t)\ge-D(t),\quad D(t)=Mt^p,\qquad
a\le K\rho^q,\quad 0\le\rho\le s/\lambda,\qquad
h=K/\lambda^q,\quad c=h^{-1/q}.
\tag{PM1}
\]
正向结论保原 signed \(\Phi\)；反向锐性只对原下界固定为
\(\Phi=-D\) 的自由闭目标类，不把更强正锚、固定目标几何或其他结构纳入坏侧。
这里的幂模在所用非负残差上有定义且非减，残差代换合法。
不把本节的三种情形称为一般 signed DD2 的全部分类。

同一最近输入锚既给平方能量，也给另一条步帽：
\[
a^2+s^2\le t^2+2D,\quad t\le a+s,\quad a\le hs^q,\qquad
s(s-t)\le D,\quad
s\le B_D(t):=\frac{t+\sqrt{t^2+4D(t)}}2 .
\tag{PM2}
\]
最后一式来自
\(\langle x-y,y-p_0\rangle
=\langle x-y,x-p_0\rangle-s^2\le ts-s^2\)，
不是把不同的两个最近锚误当成同一个锚，也没有假设 \(s\le t+a\)。

考察会破坏严格下降的 \(a\ge t>0\)，误差界强迫
\[
s\ge u(t):=c\,t^{1/q}.
\]
能量给 \(D\ge s^2/2\)，输入锚另给 \(D\ge s(s-t)\)。
这两个下界的最大值在 \(s>0\) 严格增，所以非降边的准确自由阈值为
\[
D_{\rm crit}(t)
=\max\{u(t)^2/2,\ u(t)(u(t)-t)\}
=\begin{cases}
u(t)^2/2,&u(t)\le2t,\\
u(t)(u(t)-t),&u(t)\ge2t.
\end{cases}
\tag{PM3}
\]
因此 \(D<D_{\rm crit}\) 保每条受检边 \(a<t\)。
等号已可有非降边；这里是严格下降门，不是任意预设 \(\varphi<t\) 的认证。

两支都有固定尺度的完整图见证。
若 \(u\le2t\)，在平面以 \(S=\{0\}\) 取两端 x、y 的半径均为 t、弦长为 u；
两向锚积都是 \(-u^2/2\)。
若 \(u\ge2t\)，在实线取 \(x=0,y=u,S=\{t,u-t\}\)，
两向各自的最近输入锚距输入 t，锚积都是 \(-u(u-t)\)；
\(u=2t\) 时两锚合并仍成立。
令 \(J=P_S\cup\{(x,y),(y,x)\}\)，
\(F=\lambda^{-1}(J^{-1}-I)\)，则 J 为全部完整近端、闭图且全域非空，
\(\operatorname{zer}F=S\)，零输入驻定。
两个特殊输出均在 S 外，只各有对侧特殊前像，
完整真残差为 \(u/\lambda\)，原幂界取等；
投影边输出距离和残差为0、锚积为0。
所以任意非负整窗预算在该尺度允许 \(D(t)\ge D_{\rm crit}(t)\) 时，
有同一完整图的真实二周期，且距离窗不变。
这是自由目标、无额外输出位置限制的固定尺度结论；
能量支通常用二维，不将其必要性转授一维全参数或任意预先固定 S。
已有 C399、DD1 临界图和 C416 另给各区间同一图的任意小坏初值。

若另给预设 \(0\le\varphi(t)<t\)，须按 [原反演式(8)](../topics/dd2/core.md#dd2-general-gauge)
再检查。置 \(w=(\varphi(t)/h)^{1/q}\)，准确的非负预算自由门为
\[
\bigl[w\ge t\ \text{且}\ D(t)\le w(w-t)\bigr]
\quad\text{或}\quad
D(t)\le\frac{w^2+\varphi(t)^2-t^2}{2}.
\tag{PM4}
\]
特别不能删去第一支的 \(w\ge t\)：\(\varphi(t)=0\) 时，
无护栏的最大值写法会把 \(D=0\) 错判为能保证一步到达。
下面的指数门只说明能够认证何种下降类型，不能替代具体 \(\varphi\) 的这一步核对。

## PM2 · 坏边尺度与一般积分下界是不同对象

令 \(H_q(s)=s+hs^q\)，\(\chi_\Sigma=H_q^{-1}\)。
三角和原误差界只给每条允许边 \(s\ge\chi_\Sigma(t)\)。
由 \(t=\chi_\Sigma+h\chi_\Sigma^q\) 直接得
\[
\begin{array}{c|c|c}
 &\chi_\Sigma(t)\ (t\downarrow0)&u(t)/t\\ \hline
0<q<1&\sim c\,t^{1/q}&\longrightarrow0\\
q=1&t/(1+h)&=c=1/h\\
q>1&\sim t&\longrightarrow\infty
\end{array}
\tag{PM5}
\]
\(\chi_\Sigma\) 是所有边的下界，u 是 \(a\ge t\) 才必须达到的步尺度。
尤其 \(q>1\) 时 \(\chi_\Sigma\sim t\) 不表示所有实际步都与 t 等价。
PM3 的能量支在 \(q<1\) 的零端活动；在 \(q>1\) 的零端活动的是输入锚步帽；
\(q=1\) 则由固定 h 决定，切换点是 \(h=1/2\)。
候选势 \(\Theta(t)=\int_0^t u/\chi_\Sigma(u)\,du\) 在 \(q<1\) 的被积函数
等价于 \(c^{-1}u^{1-1/q}\)，所以恰在 \(q>1/2\) 时零端可积，
且 \(\Theta(t)\sim t^{2-1/q}/[c(2-1/q)]\)。
\(q=1\) 时 \(\Theta(t)=(1+h)t\)，\(q>1\) 时 \(\Theta(t)\sim t\)。
这只是候选积分的计算，仍须核对应的单步吸收和轨道合同。

固定 \(K,\lambda\) 后，须先固定 q 再缩窗。
\(q>1\) 的阈值
\(c^2t^{2/q}-ct^{1+1/q}\) 中，第二项为零端下阶；
在 \(q=1\) 时两项同阶，不能再丢掉。
因此两侧按 \(u^2=c(q)^2t^{2/q}\) 归一后的零端常数 \(1/2\) 和1，
不能直接取 \(q\to1\) 代替线性定理。
相同问题也出现在 \(\chi_\Sigma/t\) 的三个不同极限；这些极限在 \(q=1\) 附近不一致。

## PM3 · 可保证的距离与长度机制

以下正面结论都须保零、实际覆盖和自己的局部初值预算。
当没有有限长度预算时，只对已合法续接的轨道谈距离极限，
或明确取 \(U=H\) 及全距离窗覆盖。
\(M=0\) 时 D 恒为0，p 无实际作用，不能因形式上 \(pq<2\) 判失败。

| 幂指数 | 幂预算的共同小窗正面门 | 产生下降的机制和可保证的长度 |
| --- | --- | --- |
| \(0<q<1\) | \(M=0\)，或 \(p>2/q\)，或 \(p=2/q,\ 2M<c^2\) | \(s\gtrsim t^{1/q}\)，缺陷能被 \(s^2\) 吸收；距离降幅为至少 \(t^{2/q-1}\) 阶。\(q>1/2\) 时由同一步凹势 \(t^{2-1/q}\) 支付有限长；\(q\le1/2\) 不由这些前件普遍保证有限长。 |
| \(q=1\) | \(M=0\)，或 \(p>2\)，或 \(p=2,\ M<T(h)\) | 输入、输出与步长在共同线性标尺上补偿，DD1 给统一比例与线性步帽；几何级数支付长度。 |
| \(q>1\) | \(M=0\)，或 \(p>2/q\)，或 \(p=2/q,\ M<c^2\) | 用输入锚上帽 \(s\le B_D\)，再以 \(a\le hB_D^q\) 压输出。共同距离收缩加可和的幂次步帽给有限长；正缺陷临界支一般只保证线性距离收缩。 |

这些纯预算自由类的坏侧由 PM3 及对应完整模型支持；
不等于每个固定好图都必须满足这组参数门。
线性临界函数准确为
\[
T(h)=
\begin{cases}
(1-h)/h^2,&0<h\le1/2,\\
1/(2h^2),&h\ge1/2.
\end{cases}
\tag{PM6}
\]
若 \(\theta=\sup_{0<t\le R}D(t)/t^2<T(h)\)，
令 \(b_\theta=(1+\sqrt{1+4\theta})/2\)，
\(\kappa_\theta=\min\{hb_\theta,h\sqrt{(1+2\theta)/(1+h^2)}\}<1\)，
则 \(s\le b_\theta t,\ a\le\kappa_\theta t\)。
尾长至多 \(b_\theta t_k/(1-\kappa_\theta)\)，初值用该预算严格留域。
这正是已核 DD1 的范围；逐尺度严格但没有共同余量的门不能充当统一 \(\kappa\)。
原 signed 数据也可直接按 \(\sup[-\Phi(t)]_+/t^2\) 核该门；
不能因较松的 M 预算失败就判更强原下界失败，原下界中Φ>0的信息仍由有符号根与几何保留。

在整个 \(0<q<1\)，先定义 \(\nu=2/q-2>0,\alpha=2-1/q\)。
PM5 使任意 \(0<b<c\) 的步下界 \(s\ge b t^{1/q}\) 在小窗成立。
选 \(0<\delta<1\) 并核 \(2Mt^p\le(1-\delta)b^2t^{2/q}\) 后，
直接有 \(t^2-a^2\ge\delta s^2\) 及
\(t-a\ge(\delta b^2/2)t^{2/q-1}\)。
因此这组充分证书认证任何 \(0<\gamma\le\delta b^2/2\) 的预设
\(\varphi_\gamma=t-\gamma t^{1+\nu}\)，再缩窗保持目标非负；
这不是给定 b、δ 下反演门的必要系数，也不默认任意指定 \(\gamma\) 兼容。
仅在 \(q>1/2\) 时调用 [C399/PR1–PR3](#dd2-power-explicit-rates) 的长度结论，
同一步势常数可取 \(2/(\alpha\delta b)\)，
距离比较界是 \(O(k^{-1/\nu})\)，点误差和尾长比较界是 \(O(k^{-\alpha/\nu})\)。
这些是上界；固定图可能更快或有限终止。
\(\varphi_\gamma(t)/t\to1\) 不是每条实际轨道比值都趋1；
已有完整剪切才提供实际慢率见证。
\(q\le1/2\) 时默认积分在零端发散，
例如 \(\lambda=K=1\) 的 C456 同原模径向与旋转却分别有限长和无限长，
全参数零缺陷统一类的必要性另见 C420，故既不把发散当作固定图反证，
也不把仅距离耗散提升成点收敛或长度。

对 \(q>1\)，[C416](#dd2-superlinear-power)取
\(\beta=\min\{1,p/2\}\)（\(M>0\)），而 \(M=0\) 时取 \(\beta=1\)。
有 \(s\le C_s t^\beta\)。
非临界好支 \(M=0\) 或 \(p>2/q\) 给 \(\omega=q\beta>1\) 和
\(a\le hC_s^q t^\omega\)，从而小窗可以认证任意固定 \(\kappa\in(0,1)\)。
若 \(p=2/q,0<M<c^2\)，则 \(\beta=1/q\)，
\[
\frac{hB_D(t)^q}{t}\longrightarrow r:=hM^{q/2}\in(0,1).
\tag{PM7}
\]
这里只据此认证预先取定的 \(\kappa\in(r,1)\)。
两种好支在各自已认证的共同 \(\kappa\) 下都给
\[
\sum_{j\ge k}s_j\le\frac{C_s t_k^\beta}{1-\kappa^\beta}.
\tag{PM8}
\]
先核 \(C_s t_0^\beta/(1-\kappa^\beta)<d(x^0,U^c)\)，
有限前缀含首出边的同一几何和保证留域，此后才续接全部允许轨道并取尾和。
有限长度及闭目标识别强极限于 \(S\cap U\)。
临界点误差由 PM8 有 R 线性上界，未据此声称点的 Q 线性或超线性；
距离几何收缩不要求线性步帽。
尤其临界 \(\beta<1\) 时，不能把 \(t^\beta\) 换成更小的 t。
非临界支还可独立把充分距离幂阶传到点误差：
若 \(e_k=\|x^k-x^\infty\|\)，
\(e_{k+1}\le C\,a^\beta\le C h^\beta s_k^\omega=o(s_k)\)，
而 \(|e_k-s_k|\le e_{k+1}\)，故未终止轨道 \(e_k/s_k\to1\)，
进而 \(e_{k+1}\le C'e_k^\omega\)。
这是充分 Q 阶，不声称最佳；临界 \(\omega=1\) 不能沿用这一步。

统一积分法不能代替所有分区的精确几何。
\(q<1\) 时 \(\chi_\Sigma\) 给的尺度吸收吻合上述能量门；
\(q=1\) 且处于二次幂 \(D=Mt^2\) 时，
默认 \(2D\le(1-\delta)\chi_\Sigma^2,\ \delta>0\) 只能覆盖
\(2M<(1+h)^{-2}\)，严格窄于 PM6。
\(q>1\) 时 \(\chi_\Sigma\sim t\)，这个统一净耗散机制还会遗漏
\(M>0,\ 2/q\le p<2\) 的正面区间。
也不能把 C399 的 \(t^\alpha\) 尾式直接外推到 \(q>1\)：
此时 \(\alpha>1\)，任一趋向 S 的轨道总长至少为初距 t，
所以全窗固定常数的 \(Ct^\alpha\) 根本不能作为一般总长上界。
一般原 \(\psi\) 仍可回到 C419/C429 的原域下界
\(b_\psi(t)=\inf_{\rho\in D_\psi}\max\{\lambda\rho,t-\psi(\rho)\}\)
并核它的正性、对应的严格吸收和积分合同，不能给任意原模硬贴一个幂指数。
[C451 的对数强化半阶](../topics/dd2/nonpower_rates.md#dd2-log-half-order)
在规定小窗和其余前件下，以原逆 \(w(t)=t^2[\log(1/t)]^\beta\)
得到 \(\beta>1\) 的积分门，说明纯幂的 \(1/2\) 端点不替代一般函数分析。

<a id="dd2-superlinear-critical-linear-chain"></a>
## PM4 · \(q>1\) 好临界区仍有真实线性轨道

这是 C416 的支持见证，不改变其原定理或宣称新的最优率。
固定 \(q>1,K,\lambda>0,0<M<c^2,p=2/q\)，令
\(r=hM^{q/2}\in(0,1)\)，预先选 \(\kappa\in(r,1)\)、
\(\varphi(t)=\kappa t\)。
由 PM7 先选工作半径 R，使原幂预算对全部自由边认证这个目标。
再取 \(0<t_0\le R\)，使 \(\sqrt M\,t_0^{1/q-1}>1+r\)。
在实线上定义
\[
t_k=r^kt_0,\quad s_k=\sqrt M\,t_k^{1/q},\quad
x_0=0,\quad x_{k+1}=x_k+s_k,\quad
x_\infty=\sum_{k\ge0}s_k,\quad
S=\{p_k=x_k+t_k:k\ge0\}\cup\{x_\infty\}.
\tag{PM9}
\]
因 \(1/q-1<0\)，全部 \(s_k>t_k+t_{k+1}\)。
所以 p_k 位于 \((x_k,x_{k+1})\)，严格递增至 \(x_\infty\)。
在 x_k 左侧最近的可能锚 p_{k-1}（若有）距离
\(s_{k-1}-t_{k-1}>t_k\)，右侧其余锚和 \(x_\infty\) 都比 p_k 更远。
故 p_k 是唯一最近锚，输入距确为 t_k。

令 \(U=V_\psi=\mathbb R\)，
\[
J=P_S\cup\{(x_k,x_{k+1}):k\ge0\},\qquad
F=\lambda^{-1}(J^{-1}-I).
\tag{PM10}
\]
S 紧，投影图闭；附加边只累积到已有的 \((x_\infty,x_\infty)\)。
因此 F 为完整闭图，\(J=J_{\lambda F}\) 全域非空、零集恰 S，零输入驻定。
原 F 允许空纤维，这不影响完整近端覆盖。
每个链输出 \(x_{k+1}\notin S\) 只有 x_k 这个前像，
故其完整真残差为 \(s_k/\lambda\)，而
\[
a=t_{k+1}=h s_k^q,\qquad
\langle x_k-x_{k+1},x_{k+1}-p_k\rangle
=-s_k(s_k-t_k)\ge-Mt_k^{2/q}.
\tag{PM11}
\]
投影边的输出距离、真残差和锚积均为0，全部边符合原幂数据。
实际每边还直接满足 \(a\le rt\)，但这项图级加强不冒称由共同幂预算本身认证；
本例保先指定且已认证的 \(\varphi=\kappa t\)。
每个选择要么沿链，要么某次投影后驻定，所以全部轨道有限长且距离窗不变。
持续沿链时，
\[
\|x_k-x_\infty\|=\sum_{j\ge k}s_j
=\frac{\sqrt M\,t_k^{1/q}}{1-r^{1/q}},\qquad
\frac{t_{k+1}}{t_k}=r,\qquad
\frac{\|x_{k+1}-x_\infty\|}{\|x_k-x_\infty\|}=r^{1/q}>0.
\tag{PM12}
\]
因此即使 q>1、满足好侧严格常数且实际有限长，也不能一概断言超线性。
同一图的后续 x_k 给任意小距离的这种非超线性轨道。

最后，幂指数是所选证书的参数，不是每个算子的唯一标签：
在 \(0\le\rho\le R_\rho<\infty\) 上，若 \(q_2>q_1>0\)，
\(a\le K_2\rho^{q_2}\) 也给
\(a\le K_2R_\rho^{q_2-q_1}\rho^{q_1}\)。
改变证书指数或放宽原模后，须重新核缺陷、预设目标和预算；
上述最坏类的指数机制不改变固定图原本的实际轨道。

<a id="dd2-power-length-threshold"></a>
## PL1 · 半阶端点的准确统一类命题

本节是 C420 的纯幂特化及 C456 的参数缩放补证，不改两者的原身份。
固定 \(q,K,\lambda,R>0\)，令
\[
\psi(\rho)=K\rho^q,\quad
h=K/\lambda^q,\quad c=\lambda K^{-1/q},\quad m=1/q,\qquad
\chi=(s\mapsto s+hs^q)^{-1}.
\tag{PL1}
\]
量化包含二维欧氏空间的有限维普通 PPA 类：非空闭
\(S\subseteq\operatorname{zer}F\)，完整输出真残差，
每条允许边存在同一个最近输入锚使内积非负，
且允许关系在 \(U=H\) 的整个距离窗 \(d(x,S)\le R\) 非空。
原模定义域为全部非负残差，\(V_\psi=H\)、没有额外输出位置筛选；
原锚下界固定为 \(\Phi=0\)。准确的逐边量词是
\[
\forall x\in U_R,\ \forall y\in\mathcal J(x)\subseteq J_{\lambda F}(x):
\quad a\le K\rho^q,\quad \rho=r_F(y),\qquad
\exists p\in P_S(x):\ \langle x-y,y-p\rangle\ge0 .
\]
则
\[
\boxed{\quad
\text{该类每个对象、每个 }t_0\le R\text{ 初值的全部允许轨道有限长}
\quad\Longleftrightarrow\quad q>1/2 .
\quad}
\tag{PL2}
\]
必要性已经在同一个二维单点目标、全域连续单值 F、唯一完整近端中成立，
不是只构造一串标量数，也不依赖多值选择或非凸零集。
局部开 U 的正面版另保下述初值预算；
不能在长度尚未证明时只靠距离下降假设物理位置留域。

为了保原 DD2 的先定目标顺序，可以预先指定
\[
T_m(a)=\sqrt{a^2+c^2a^{2m}},\qquad
\varphi_0=T_m^{-1}\quad\text{在 }[0,\infty)\text{ 定义，目标取 }[0,R]\text{ 上限制}.
\tag{PL3}
\]
原真误差界给 \(s\ge c a^m\)，故
\(T_m(a)^2\le a^2+s^2\le t^2\)，在 \(t>0\) 认证 \(a\le\varphi_0(t)<t\)，零尺度驻定。
PL3 既是所指定的曲线，也是这组原数据的准确最坏输出；
后一身份由下文完整旋转逐尺度取等单独证明。
若原先另给 \(\varphi\ge\varphi_0\)，同一必要见证仍符合目标；
若要求某处 \(\varphi<\varphi_0\)，必须强化前件或另给图结构，
不能把 PL2 的必要性自动授给被筛小的类。

## PL2 · 精确积分及正面支付

写 \(\mu=\chi(R)>0\)。由
\(1/\chi(t)=1/\mu+\int_{\chi(t)}^\mu s^{-2}\,ds\)，
乘 t 并交换非负积分，得到
\[
I_\chi(R):=\int_0^R\frac{t}{\chi(t)}\,dt
=\frac{R^2}{2\mu}
 +\frac12\int_0^\mu(1+hs^{q-1})^2\,ds.
\tag{PL4}
\]
这里 \(\chi(t)\le s\) 恰等价于 \(t\le s+hs^q\)。
因此 \(q>1/2\) 时有可直接核算的准确式
\[
I_\chi(R)=
\frac{R^2}{2\mu}+\frac{\mu}{2}
+\frac hq\mu^q
+\frac{h^2}{2(2q-1)}\mu^{2q-1},
\tag{PL5}
\]
而 \(0<q\le1/2\) 时该非负积分在每个正上限发散。
这一步只判积分；下文完整旋转把发散变成实际无限长度。
特别 \(q=1\) 得 \(I_\chi(R)=(1+h)R\)；
\(q>1\) 得 \(I_\chi(t)\sim t\)；
\(1/2<q<1\) 得
\(I_\chi(t)\sim t^{2-1/q}/[c(2-1/q)]\)。

当 \(\Phi=0\)，每条边都有 \(s\ge\chi(t)\) 与
\(t^2-a^2\ge s^2\)。对正输入，
\[
s\le \frac{t^2-a^2}{\chi(t)}
 \le 2\int_a^t\frac{u}{\chi(u)}\,du
=2[I_\chi(t)-I_\chi(a)].
\tag{PL6}
\]
零输入由锚能量强制零步；正步的 \(a<t\) 先于势差评价成立。
若 \(q>1/2\)，有限前缀含首条拟出界边的长度至多 \(2I_\chi(t_0)\)；
在局部 U 中要求
\(2I_\chi(t_0)<d(x^0,U^c)\)，即可先证明输出留域，再调用覆盖续接。
正距离极限会使 \(\chi(t_k)\) 有正下界，与平方距离耗散矛盾，
所以距离趋零。有限长度给强 Cauchy，闭 S 及严格位置预算给
\(x^k\to x^\infty\in S\cap U\)，且尾长至多 \(2I_\chi(t_k)\)。
全域 U 时位置条件自动满足。
这同时证明 q=1、q>1 的零缺陷正面支，未把 C399 的凹幂公式外推。

## PL3 · 任意 K、λ 的同一完整旋转与真实发散

先对任意 \(q>0\)、\(m=1/q>0\)，在 \(H=\mathbb R^2\) 取
\(S=\{0\}\)、\(U=V_\psi=H\)，Q 为直角旋转，定义
\[
F_\perp(0)=0,\qquad
F_\perp(y)=K^{-1/q}\|y\|^{m-1}Qy\quad(y\ne0).
\tag{PL7}
\]
这是全域连续单值 F，零集恰 S。
\(I+\lambda F_\perp\) 把输出半径 a 变成 \(T_m(a)\)，
方位角增加 \(\arctan(ca^{m-1})\)。
\(T_m\) 连续严格增加且从零满射至无穷；
先唯一反解半径，再反旋转，给全域连续逆，包括原点。
故完整 \(J_{\lambda F_\perp}\) 全域唯一、图闭，所有输出均被穷尽。
对任何完整近端边，
\[
a=\varphi_0(t),\qquad
\rho=K^{-1/q}a^m,\quad s=\lambda\rho=c a^m,\quad
K\rho^q=a,\qquad
\langle x-y,y\rangle=0 .
\tag{PL8}
\]
原误差界和原非负锚同时取等，零输入驻定，任一距离窗不变。
每个非负残差值都由某个输出半径实现，因而该原 \(\psi\)
在全输出域逐点最小；不能用“只是选了松模”解释反向。

任一 \(t_0>0\) 产生同一图中的实际轨道：
\[
t_k^2=t_{k+1}^2+c^2t_{k+1}^{2m},\qquad
s_k=c t_{k+1}^m .
\tag{PL9}
\]
半径严格下降；若正极限存在，上式的平方降幅不趋零，故 \(t_k\to0\)。
现在取 \(0<q\le1/2\)、\(m\ge2\)，令 \(\nu=2m-2>0\)。对每个正步，
\[
t_{k+1}^{-\nu}-t_k^{-\nu}
=t_{k+1}^{-\nu}
 \left[1-(1+c^2t_{k+1}^{\nu})^{-\nu/2}\right]
\longrightarrow \frac{\nu c^2}{2}.
\tag{PL10}
\]
对增量取平均，得到
\[
t_k\sim[(\nu c^2/2)k]^{-1/\nu},\qquad
s_k\sim c[(\nu c^2/2)k]^{-m/\nu},\qquad
\frac m\nu=\frac1{2(1-q)}\le1 .
\tag{PL11}
\]
所以每个非零初值的总长发散；q=1/2 时更有 \(s_k\sim1/(ck)\)。
实际点仍范数收敛到0，且 \(\sum s_k^2=t_0^2\)。
这证明 PL2 的必要侧，保同一算子、任意小正初值和全部近端量词；
初值零则是单独的驻定例外。

## PL4 · 放回幂缺陷与原预设目标

原负幂预算类固定 \(\Phi(t)=-Mt^p\)、\(M\ge0,p>0\)；
若实际原 \(\Phi\) 更强，下面只转授正面结论。
在 PM3 的好参数门内：
\(0<q<1\) 取 M=0，或 \(p>2/q\)，或 \(p=2/q,2M<c^2\)；
q=1 取 M=0，或 p>2，或 p=2 且 \(M<T(h)\)；
q>1 取 M=0，或 \(p>2/q\)，或 \(p=2/q,M<c^2\)。
于是 q>1/2 保全部局部轨道有限长，分别使用
C399 的 \(Ct^{2-1/q}\)、DD1 的线性几何尾、C416 的 \(Ct^\beta\) 几何尾，
每支按自己的严格初值预算先留域。
不能只因 PL5 可积就删去缺陷吸收，或在所有分区硬用同一个 \(\delta\) 门。

对 \(0<q\le1/2\) 及任一上述好幂预算，先指定
\[
\varphi_D(t)=T_m^{-1}\!\left(\sqrt{t^2+2Mt^p}\right).
\tag{PL12}
\]
它连续、非减、零点为零，在充分小的共同窗内
对 \(t>0\) 有 \(\varphi_D(t)<t\)，因为好门恰使 \(2Mt^p<c^2t^{2m}\)。
对该预算类每条实际边，
\[
T_m(a)^2\le a^2+s^2\le t^2+2Mt^p
\quad\Longrightarrow\quad a\le\varphi_D(t).
\tag{PL13}
\]
同一 PL7 旋转保原下界 \(-Mt^p\)，并有
\(a=\varphi_0(t)\le\varphi_D(t)\)，因而是该已认证目标下的完整无限长反例。
M>0 时在每个正尺度有 \(\varphi_D>\varphi_0\)：把原下界放宽后，不能仍宣称
较紧的 \(\varphi_0\) 是同一较松数据的统一认证。
确实，对目标 \(\varphi_0\) 归一化取
\(r=\varphi_0(t)/t\)、\(z=c\varphi_0(t)^m/t\)，有
\(r^2+z^2=1\) 及 \(1-r<z<1+r\)；
[原分段补偿式](../topics/dd2/core.md#dd2-main-theorem)给 \(\Sigma(r,z)=0\)，
而正尺度的 \(-\Phi(t)/t^2=Mt^{p-2}>0\)，已经越过该目标的准确自由门。
对任意另给更强目标，必要侧须重新核它是否保留见证；
本项不把上述明确曲线偷换成所有目标的共同结论。
故半阶端点是纯幂好预算统一保证的真实障碍，
而不是原 signed DD2 无条件的长度分界。

## PL5 · 不能从统一端点推出什么

对 \(0<q\le1/2\)，保同样的 \(q,K,\lambda\)、精确原模和指定 \(\varphi_0\)，取
\[
F_\parallel(y)=K^{-1/q}\|y\|^{m-1}y,\qquad F_\parallel(0)=0 .
\tag{PL14}
\]
半径方程为 \(t=a+c a^m\)，故完整近端全域唯一、与输入同射线，
真残差仍满足 \(K\rho^q=a\)，实际锚积为 \(c a^{m+1}\)，在正尺度严格为正。
它符合共同原下界 \(\Phi=0\)，但不与旋转共享最紧实际锚信息。
正尺度有 \(a<\varphi_0(t)\)，且半径方程使 \(t_k\downarrow0\)：正极限会使 \(c t_{k+1}^m\) 不趋零，与半径差趋零矛盾。
所有尺度有 \(s=t-a\)，所以全部轨道的准确尾长就是 t。
任何更高幂的局部真误差界均失败，因为
\(a/\rho^{q'}=K^{q'/q}a^{1-q'/q}\to\infty\) 对 \(q'>q\)。
本图还是凸函数
\(f(y)=K^{-1/q}\|y\|^{m+1}/(m+1)\) 的真实唯一全局最小化近端，
不只是驻点根：凸支撑式和 \(x-y=\lambda\nabla f(y)\) 给任意 z
\[
f(z)+\frac{\|z-x\|^2}{2\lambda}
-\left[f(y)+\frac{\|y-x\|^2}{2\lambda}\right]
\ge\frac{\|z-y\|^2}{2\lambda},
\]
直接证明全局唯一最优性。
这把“统一类必要”与“每固定图必要”直接分开。

其余边界也各有明确机制。
保 \(\Phi\ge0\) 而另由数据或结构认证 \(\varphi(t)\le\kappa t\)、\(\kappa<1\)，
则 \(s\le t\) 与几何距离直接给总长至多 \(t_0/(1-\kappa)\)，不需要半阶门；
不能在原零缺陷纯幂数据无法认证该目标时擅自加入它。
若保更强原下界 \(\Phi(t)\ge\gamma t^2\)、\(0<\gamma\le1/4\)，
则步长 s 和输出距离 a 均不超过根帽 \(b_\gamma t\)，
\(b_\gamma=(1+\sqrt{1-4\gamma})/2<1\)，也可给几何尾。
对输出帽，令 \(b=\|y-p\|\ge a\)，用
\(s\ge|t-b|\) 代入同一平方能量，即得 \(b^2-tb+\Phi(t)\le0\)。
此类并非空的：对任意本节低幂 q 和 K、λ，取 \(F(y)=y/\lambda\)，
在满足 \((R/2)^{1-q}\le K/\lambda^q\) 的小窗，
完整 \(J=I/2\) 保原幂界和 \(\Phi=t^2/4\)。

<a id="dd2-one-dimensional-nonnegative-length"></a>
一维还可固定任意非空闭 S，而不只单点。
某个最近输入锚 p 满足 \((x-y)(y-p)\ge0\)，就使 y 位于 x、p 之间。
于是
\[
a\le |y-p|=t-s,\qquad a\ge t-s
\quad\Longrightarrow\quad s=t-a .
\tag{PL15}
\]
第二式是距离函数的 Lipschitz 性。
所以实线中 \(\Phi\ge0\) 的全部合法有限前缀长度至多 \(t_0\)，
这一有限长度结论本身不需要误差界。
在一般局部 U 先用 \(t_0<d(x^0,U^c)\) 保证留域，再调用覆盖。
若还保本节纯幂误差界和合法无限续接，
\(s_k\to0\) 与 \(a_k\le K(s_k/\lambda)^q\) 使距离趋零，
总长及实际尾长便恰为 \(t_0\) 及 \(t_k\)，强极限属于 S。
PL15 不用 S 凸性，只用逐边存在一个实际最近锚；
这说明二维必要见证不能降成一般实线类的必要性。
反过来，裸 q>1/2 也不充分：
C400 的 q=1、预设 \(t/(1+t)\) 与其匹配的负缺陷已有真实无限长旋转，
它没有统一 DD1 余量，不反驳上述好幂门。
[C451](../topics/dd2/nonpower_rates.md#dd2-log-half-order) 的原逆
\(w(t)=t^2[\log(1/t)]^\beta\) 在 \(\beta>1\) 给有限长度，
同时其准确原模不满足任何更高于半阶的局部幂界；
这是保非幂修正后的另一合同，不能用纯幂 q 分类替代。
以上均为本端点的适用边界，不宣称新的公开优先性或更大的最优率分类。

<a id="dd2-power-defect"></a>
## C399-v1 · 普通 PPA 的同一步长度估计

固定有限维欧氏空间、\(\lambda>0\)、非空闭 \(S\subseteq\operatorname{zer}F\)、开集 \(U\) 和 \(R_0>0\)。设允许关系 \(\mathcal J(x)\subseteq J_{\lambda F}(x)\) 在 \(x\in U,\ d(x,S)\le R_0\) 时非空。要求对每个此类 \(x\) 及每个 \(y\in\mathcal J(x)\)，至少有一个最近锚 \(z\in P_S(x)\) 使

\[
\langle x-y,y-z\rangle\ge-Md(x,S)^p,
\qquad
d(y,S)\le K r_F(y)^q,\qquad r_F(y)=\inf_{v\in F(y)}\|v\|.
\tag{1}
\]

取 \(K>0,\ M\ge0,\ p>0,\ 1/2<q<1\)。若 \(M=0\)，或 \(p>2/q\)，或 \(p=2/q\) 且 \(2M<\lambda^2K^{-2/q}\)，则存在 \(0<R\le R_0\) 与 \(C,\gamma>0\)，使每条 \(d(x,S)\le R\) 的允许步满足

\[
\|x-y\|\le C[d(x,S)^\alpha-d(y,S)^\alpha],\quad
d(y,S)\le d(x,S)-\gamma d(x,S)^{1+\nu},
\qquad
\alpha=2-1/q,\quad \nu=2/q-2.
\tag{2}
\]

若 \(d_0=d(x^0,S)\le R\) 且 \(Cd_0^\alpha<d(x^0,U^c)\)，则每个允许选择轨道均可续接，且保持在工作窗。总长至多 \(Cd_0^\alpha\)，第 \(k\) 步起的尾长至多 \(Cd_k^\alpha\)，轨道收敛到 \(S\cap U\)。有 \(d_k=O(k^{-1/\nu})\) 及 \(\|x^k-x^\infty\|=O(k^{-\alpha/\nu})\)。

**证明。** 写 \(t=d(x,S)\)、\(a=d(y,S)\)、\(s=\|x-y\|\)、\(h=K/\lambda^q\)。平方展开与最近性给

\[
a^2+s^2\le t^2+2Mt^p,\qquad a\le h s^q,\qquad t\le a+s .
\tag{3}
\]

第一项使 \(s\) 随 \(t\downarrow0\) 一致趋零。对任意固定 \(0<c<h^{-1/q}=\lambda K^{-1/q}\)，缩窗使 \(h+s^{1-q}\le c^{-q}\)，由 \(t\le h s^q+s\) 得 \(s\ge c t^{1/q}\)。三种门中均可选定 \(c\)、\(0<\delta<1\) 及小窗，使 \(2Mt^p\le(1-\delta)c^2t^{2/q}\le(1-\delta)s^2\)。因此 \(t^2-a^2\ge\delta s^2\)。若 \(t>0\)，这给出严格下降及

\[
t-a\ge \frac{\delta c^2}{2}\,t^{2/q-1},\qquad
s\le\frac{2}{\delta c}t^{1-1/q}(t-a)
\le\frac{2}{\alpha\delta c}(t^\alpha-a^\alpha).
\]

最后一步用 \(u^\alpha\) 的凹性。当 \(t=0\)，(3) 强制 \(s=a=0\)。对任意有限前缀，(2) 的望远镜预算保证新输出仍在 \(U\) 且距离不增，故覆盖假设可归纳使用。全程留在以 \(x^0\) 为中心、半径 \(Cd_0^\alpha\) 的闭球内，球包含于 \(U\)。有限长度给 Cauchy 极限，距离递推及 \(S\) 闭给极限属于 \(S\)。对正距离用 \(u^{-\nu}\) 的凸性得 \(d_{k+1}^{-\nu}-d_k^{-\nu}\ge\nu\gamma\)。遇零后驻定。尾预算代入距离率即得点误差率。

这个证明使用同一步的实际 \(s\)。只将 (3) 的独立步长上包络 \(O(t)\) 与距离上界逐项相加，通常得不到这里的全指数范围。形式上的距离模可取 \(t-\gamma t^{1+\nu}\)，充分缩窗后它非负、非减，且其与 \(t\) 的比趋于 1。

<a id="dd2-power-explicit-rates"></a>
### 显式计步界及无固定比例的目标

保留 C399 的完整合同，令 \(\alpha=2-1/q\in(0,1)\)、\(\nu=2/q-2>0\)。预设幂次修正目标
\[
\varphi_\gamma(t)=t-\gamma t^{1+\nu},\qquad \gamma>0 .
\tag{PR1}
\]
上面的原 DD 推导提供一种充分认证：取
\(0<b<\lambda K^{-1/q}\)、\(0<\delta<1\)，缩窗使
\[
s\ge b t^{1/q},\qquad
2Mt^p\le(1-\delta)b^2t^{2/q},\qquad
0<\gamma\le\delta b^2/2 .
\]
其中第一式来自原 \(\psi(\rho)=K\rho^q\)、完整 \(\rho\le s/\lambda\)、三角及小窗，而非额外实际轨道假设。C399 的三种参数门保证存在这样的正 \(b,\delta,\gamma\)；对另行指定的 \(\gamma\)，须核上面的兼容不等式，未保证任意大的目标系数。再缩窗使
\((1+\nu)\gamma R^\nu\le1\)，则预设 \(\varphi_\gamma\) 是非负、非减的自映射，正尺度严格低于 \(t\)，且 \(\varphi_\gamma(t)/t\to1\)。可以取
\(C=2/(\alpha\delta b)\) 作为同一步长度势常数。

设 \(x^0\in U_R\)、\(0<t_0\le R\)，且初值满足原严格位置预算 \(Ct_0^\alpha<d(x^0,U^c)\)。有限前缀的实际步长望远镜先给全部允许选择留在 \(U_R\)，再由覆盖逐步续接；不先假定无限轨道。对任何两端距离 \(t_k,t_{k+1}>0\) 的步，
\[
t_{k+1}^{-\nu}-t_k^{-\nu}
=\nu\int_{t_{k+1}}^{t_k}u^{-1-\nu}\,du
\ge\nu t_k^{-1-\nu}(t_k-t_{k+1})
\ge\nu\gamma .
\tag{PR2}
\]
因此所有 \(k\ge0\) 均有
\[
\begin{split}
t_k&\le \mathcal R_{t_0}(k)
 :=(t_0^{-\nu}+\nu\gamma k)^{-1/\nu},\\
\mathcal L_k
 :=\sum_{j=k}^{\infty}\|x^{j+1}-x^j\|
 &\le C t_k^\alpha
 \le C\mathcal R_{t_0}(k)^\alpha,\\
\|x^k-x^\infty\|&\le\mathcal L_k .
\end{split}
\tag{PR3}
\]
遇零后由原零输入合同驻定，实际量全为零，故 (PR3) 继续成立；若 \(t_0=0\)，直接使用驻定，不评价 \(0^{-\nu}\)。极限 \(x^\infty\in S\cap U\)，因为完整初始长度预算的闭球包含于 \(U\)，距离趋零且 \(S\) 闭。

这给显式的距离指数 \(1/\nu=q/[2(1-q)]\) 和点误差／尾长指数
\(\alpha/\nu=(2q-1)/[2(1-q)]\)，均只在 \(1/2<q<1\) 的本合同使用。没有统一 \(\kappa<1\) 的是目标比例；每条实际轨道的比值未必趋 1，可能更快或有限终止。是否真实达到慢率由下述完整剪切核验。\(q=1/2\) 的 \(\alpha=0\) 与 \(q=1\) 的 \(\nu=0\) 不能代入这份正参数证明；其独立结论另用原对应版本。

<a id="dd2-power-witnesses"></a>
## 边界与严格实例

**临界缺陷常数。** 设 \(0<q<1\)，\(c_*=\lambda K^{-1/q}\)，固定小 \(\varepsilon>0\) 使 \(c_*\varepsilon^{1/q-1}<2\)。在平面上以 \(R_\theta\) 表示旋转，取

\[
T(x)=R_{\theta(\|x\|)}x,\qquad
\theta(r)=2\arcsin\bigl(c_*\min(r,\varepsilon)^{1/q-1}/2\bigr),\qquad
F=(T^{-1}-I)/\lambda .
\]

\(T\) 保半径，逐圆反向旋转即得连续全域逆。原算子连续单值，唯一零点为 \(0\)，完整 \(J_{\lambda F}=T\)。在 \(0<t\le\varepsilon\) 时，\(a=t,\ s=c_*t^{1/q}\)，故 (1) 的 EB 取等，内积为 \(-c_*^2t^{2/q}/2\)。当 \(p=2/q,\ 2M\ge c_*^2\) 时立即满足 (1)。当 \(p<2/q,\ M>0\) 时缩窗也满足 (1)。所有任意小非零轨道保半径。它复用 [C392 的保半径构造](../topics/common_structure/angle_residual_exponent_balance.md#angle-residual-exponent-balance)，这里固定的是输入距离幂次缺陷及其常数。

**半阶端点。** 取 \(\lambda=K=1\)，\(F(y)=\|y\|Jy\)，其中 \(J\) 是逆时针直角旋转。\(S=\{0\}\)，零锚内积恒为零，完整真残差为 \(\|y\|^2\)。\(\|y+F(y)\|=\|y\|\sqrt{1+\|y\|^2}\) 严增且值域为 \([0,\infty)\)，每个半径上的映射是旋转，因此全域近端唯一。非驻定轨道的正半径 \(d_k\downarrow0\) 且

\[
d_{k+1}^{-2}-d_k^{-2}=(1+d_{k+1}^2)^{-1}\longrightarrow 1,\qquad
\|x^{k+1}-x^k\|=d_{k+1}^2\sim 1/k .
\]

故轨道收敛而无限长。缩到残差不超过 1 后同一模型满足每个 \(0<q\le1/2\) 的误差界。

**超出线性正则与固定收缩的非单调实例。** 取 \(\lambda=1,\ S=\{0\}\) 及 \(F(y)=-r y+r^{1/3}Jy\)，\(r=\|y\|\)。真残差为 \(r^{4/3}\sqrt{1+r^{4/3}}\)，故 \(q=3/4,\ K=1\) 成立，线性误差界失效。内积 \(\langle F(y),y\rangle=-r^3\) 说明 \(F\) 非单调。输入半径为

\[
H(r)=r\sqrt{(1-r)^2+r^{2/3}}.
\]

\(H(r)\ge r^{4/3}\) 排除小输入的远根。\(H'(r)\to1\) 给小半径严格增性与覆盖，其方位关系为旋转，故充分小输入的完整近端唯一。小正 \(r\) 有 \(H(r)>r\) 和 \(H(r)/r\to1\)，所以 \(p=3,\ M=1\) 成立，且每个充分小非零轨道的距离比趋于 1。取对数后用 Cesàro 平均得 \(d_k^{1/k}\to1\)，故 R 线性距离率也失效。输入侧残差 \(r_{\mathrm{Id}-J_F}(x)\) 与输出侧残差 \(r_F(y)\) 相同地为 \(o(d(x,S))\)。该例分离的是线性速率假设及结论。它的 \(\langle F(y),y\rangle/\|F(y)\|^2\to0\)，故局部允许任意小的负弱 Minty 常数。

## 与相关定理的范围

- [C309](ppa_nonlinear_gauge_and_coupled_obstruction.md#c309-theorem) 接受已经给定的距离模和独立尾和条件。这里从同一步的锚定缺陷和输出真残差直接推出幂势。一般函数包络的存在与沿轨道有限长度仍是两个证明义务。
- [C212](generalized_ppa_modulus.md#gpm-strict) 的非负锚定壳层估计与 Li–Mordukhovich 2012 的极大单调 PPA 已能推出 \(q>1/2\) 的有限长度。此处确定的是一个允许负缺陷的输入距离条件、其临界常数及同一步尾势。对完整公开文献的优先性未判定。[一手定位与比较](../LITERATURE.md#lit-alcantara-dd)
- [C285](rleb_sharp_linear_frontier.md#rsl-threshold) 的任意闭集固定二次分段锐门仍独立成立。这里的幂次有限长度结论限于普通 PPA，退化 PPPA 的核方向恢复另需条件。

<a id="dd2-sublinear-power-rates"></a>
## C399 的速率与尾长见证

把 [C393 的零缺陷剪切](../topics/common_structure/angle_residual_exponent_balance.md#planar-two-fixed-zero-convergence) 缩放到任意 \(\lambda,K>0\)，并令 \(m=1/q>1,\ c=\lambda K^{-1/q}\)。在 \(\mathbb R^2\) 取 \(S=\mathbb R\times\{0\}\) 及

\[
\lambda F(u,v)=\bigl(-c|v|^m,\ c^2\operatorname{sgn}(v)|v|^{2m-1}\bigr).
\]

\(I+\lambda F\) 的竖坐标严格递增且满射，给定竖坐标再反解横坐标，故预解式全域唯一。完整零集是 \(S\)，真残差至少为 \(c|v|^m/\lambda\)，故满足所定的 \(q,K\) 界。以实际输入最近零锚计算，内积为 \(-c^2|v|^{2m}+c^2|v|^{2m}=0\)，因此见证在 C399 每个充分的 \(p,M\) 区间都合格。

从正高度开始，距离满足 \(t_k=t_{k+1}+c^2t_{k+1}^{2m-1}\)。序列严格下降到零，且 \(t_{k+1}/t_k\to1\)。令 \(\nu=2m-2\)，则
\[
t_{k+1}^{-\nu}-t_k^{-\nu}
=t_{k+1}^{-\nu}
 \bigl[1-(1+c^2t_{k+1}^{\nu})^{-\nu}\bigr]
\longrightarrow\nu c^2 .
\tag{PR4}
\]
对这些增量求平均，得到实际等价式
\(t_k\sim(\nu c^2 k)^{-1/\nu}\)。每个正初值轨道的比值趋 1，故任何 \(\kappa<1\) 都不能成为其尾部逐步收缩系数。完整所选向量唯一，故
\[
\rho_k=\frac{s_k}{\lambda},\qquad
s_k=c t_{k+1}^m\sqrt{1+c^2t_{k+1}^{2m-2}},
\qquad u_{k+1}-u_k=c t_{k+1}^m>0 .
\tag{PR5}
\]
这里 \(u_k\) 是迭代点的横坐标。零输入驻定，正高度和每个距离窗不变，所有计算属于实际完整近端。

取 \(1<m<2\)，令 \(\alpha=2-m>0\)。对单步区间有
\[
I_k:=\int_{t_{k+1}}^{t_k}v^{1-m}\,dv
 \sim t_{k+1}^{1-m}(t_k-t_{k+1})
 =c^2 t_{k+1}^{m},
\qquad
\frac{s_k}{I_k}\longrightarrow\frac1c,\quad
\frac{u_{k+1}-u_k}{I_k}\longrightarrow\frac1c .
\tag{PR6}
\]
任意给定相对误差 \(\epsilon>0\)，这两个比例在整个足够晚的尾部都落在
\((1-\epsilon)/c\) 与 \((1+\epsilon)/c\) 之间，故可以对全部尾步求和。由于
\(\sum_{j\ge k}I_j=t_k^{2-m}/(2-m)\)，得到真实有限长度和极限
\(x^\infty=(u_\infty,0)\)，以及
\[
\mathcal L_k\sim u_\infty-u_k
\sim \|x^k-x^\infty\|
\sim\frac{t_k^{2-m}}{c(2-m)}
\sim\frac{(\nu c^2 k)^{-(2-m)/\nu}}{c(2-m)} .
\tag{PR7}
\]
点误差被横向尾移和实际尾长夹住；也可用 \(t_k=o(t_k^{2-m})\) 直接核验。这是同一完整图的实际渐近式，不是仅由一个 \(O\) 上界判断慢速。因此 C399 的距离指数 \(1/\nu\)、长度势指数 \(2-m\) 和计步点误差／尾长指数 \((2-m)/\nu\) 在其统一类中均不能提高；固定图可能更快，不能得到每个图的最优性。剪切锚积为零，所以在 C399 任何给定的充分 \(p,M\) 区间都满足该缺陷下界。

若 \(m\ge2\)，(PR6) 对任意有限尾段仍成立，而
\(\int_0^{t_k}v^{1-m}\,dv=\infty\)。因此横向位移不可和，点列沿目标线无界漂移，给出 \(q\le1/2\) 时邻近任意小正距离的更强失败；此时不使用有限的 (PR7)。

<a id="dd2-superlinear-power"></a>
## C416-v1 · \(q>1\) 的锐缺陷常数与完整图临界二周期

沿用 C399 的空间、闭目标、允许关系、最近输入锚、局部覆盖及真残差条件 (1)。本节取 \(q>1\)，记 \(h=K/\lambda^q\)、\(c=h^{-1/q}\)。从 \(t=d(x,S)>0\) 出发，设输出距离为 \(a\)，位移为 \(s\)，缺陷预算为 \(D\ge0\)。令 \(u=c t^{1/q}\)，并取尺度足够小使 \(u>2t\)。此时，在任意闭目标的自由几何类上，所有允许边严格下降的精确条件是

\[
D<u(u-t)=c^2t^{2/q}-c\,t^{1+1/q}.
\tag{4}
\]

对于 \(D(t)=Mt^p\)，该条件在某个共同小尺度窗内成立，当且仅当 \(M=0\)，或 \(p>2/q\)，或 \(p=2/q\) 且 \(M<c^2=\lambda^2K^{-2/q}\)。这些参数还保证一致距离收缩，并在如下初值预算下保证所有允许轨道可续接、留域、有限长且收敛到 \(S\cap U\)。失败侧在一个全域有根、完整闭图的近端关系上有任意小初值的二周期。

**一步门。** 令 \(v=x-y\)。锚定不等式与 Cauchy–Schwarz 给

\[
-D\le\langle v,x-p_1\rangle-s^2\le ts-s^2.
\]

因此 \(s\le B_D(t)=(t+\sqrt{t^2+4D})/2\)。若 \(a\ge t\)，输出真误差界给 \(s\ge u\)，于是 \(D\ge s(s-t)\ge u(u-t)\)。反之，当 \(D\ge u(u-t)\)，在实线上取 \(x=0\)、\(y=u\)、\(S=\{t,u-t\}\)。最近锚分别为 \(t\) 和 \(u-t\)，故两端距离均为 \(t\)，位移为 \(u\)，锚定内积恰为 \(-u(u-t)\)，输出界 \(a=h u^q\) 取等。反向边亦然。

**轨道证明。** 当 \(M>0\) 时取 \(\beta=\min\{1,p/2\}\)，当 \(M=0\) 时取 \(\beta=1\)。有 \(s\le B_D(t)\le t+\sqrt{D}\le C t^\beta\) 于足够小的窗。若 \(M=0\) 或 \(p>2/q\)，则 \(q\beta>1\)，从而 \(a\le hC^q t^{q\beta}\)，在小窗给可任取固定 \(\kappa\in(0,1)\) 的收缩。若 \(p=2/q\) 且 \(0<M<c^2\)，则

\[
\lim_{t\downarrow0} h B_D(t)^q/t=hM^{q/2}<1,
\]

故可取任意 \(\kappa\in(hM^{q/2},1)\) 缩窗得到 \(a\le\kappa t\)。在此临界充分区，\(s=B_D(t)\)、\(a=hB_D(t)^q\) 同时达到自由几何上界。因为 \(B_D(t)/t\to\infty\)、\(a/B_D(t)\to0\)，可取两个共线锚，在相距 \(B_D(t)\) 的两端内侧分别距输入 \(t\) 及输出 \(a\)，并有 \(a<B_D(t)-t\) 和 \(t<B_D(t)-a\)。两端最近性和锚定等号都成立。

对 \(t=0\)，锚定能量强制零位移。在任一合法有限前缀上，第 \(k\) 步起的长度和至多 \(C t_k^\beta/(1-\kappa^\beta)\)。若 \(C t_0^\beta/(1-\kappa^\beta)<d(x^0,U^c)\) 且初始尺度在小窗，有限前缀归纳给覆盖和留域，长度界及闭目标给点收敛。\(q=1,M=0\) 则直接由 C400 得到 \(s\le t\)、\(a\le (h/\sqrt{1+h^2})t\)，同理有限长。

**一个完整闭图上的全部坏尺度。** 若 \(p=2/q,M\ge c^2\)，或 \(p<2/q,M>0\)，则 \(D(t)\ge u(u-t)\) 对所有充分小的 \(t>0\) 成立。取 \(d_j=2^{-j}\)，选 \(t_j\downarrow0\) 使 \(2t_j<u_j=c t_j^{1/q}<d_j/8\)。将上述两端 \(x_j,y_j\) 对称放在 \(d_j\) 两侧，间距 \(u_j\)，并置两锚 \(x_j+t_j,y_j-t_j\)。这四点位于 \([d_j-d_j/16,d_j+d_j/16]\) 内。较大的区间 \((d_j-d_j/8,d_j+d_j/8)\) 两两不交，且外部点到两端的距离大于 \(t_j\)。因此把所有锚及 \(0\) 合成闭集 \(S\) 后，每对两端的最近距离仍是 \(t_j\)。

置 \(J=P_S\) 加全部双向边 \(x_j\leftrightarrow y_j\)，以 \(F=(J^{-1}-I)/\lambda\) 定义原算子。投影图闭，附加边只累积到已有的 \((0,0)\)，故 \(J\) 和 \(F\) 闭图，且 \(J=J_{\lambda F}\) 全域非空，\(\operatorname{zer}F=S\)。每条投影边选投影输出作最近锚，输出距离与缺陷均为零。每个特殊端点在 \(S\) 外，唯一完整入边来自相对端点，所以其真残差为 \(u_j/\lambda\)，输出界取等。全部图边均满足 (1)。每个二周期保半径 \(t_j\) 且步长恒为 \(u_j>0\)，故距离收敛与有限长度均无法在原点任何邻域内对全部选择保证。

除以各自的 \(c(q)^2=\lambda^2K^{-2/q}\) 后，这里的临界常数为1，
而 \(0<q<1\) 能量支的归一常数为 \(1/2\)；不能忽略 c 对 q 的依赖。
证明只判定指定的完整闭图类，连续单值预解式、指定凸目标及其他额外结构下的必要性需另验。
[PM4 的完整好侧链](#dd2-superlinear-critical-linear-chain)还说明：
正缺陷临界严格侧可以全部有限长，同时存在真实距离和点误差都仅线性的轨道。

<a id="dd2-vanishing-budget"></a>
## 次阶缺陷余量的长度充要判据

设 \(\lambda=1\)、\(1<m<2\)，输出真误差界为 \(a\le r_F(y)^{1/m}\)。固定半径 \(R>0\) 下的正连续函数 \(w:(0,R]\to(0,\infty)\)，使 \(w(t)\le t^{2m}\)，并且有同一常数 \(K\ge1\) 使
\[
K^{-1}w(t)\le w(u)\le K w(t)\quad(t/2\le u\le t\le R).
\]
设 \(D(0)=0\)、\(2D(t)=t^{2m}-w(t)\)。写 \(H(t)=t^2+t^{2m}\)，假设 \(A_*(t)=H^{-1}(H(t)-w(t))\) 在小窗严格递增，且缩小 \(R\) 使下文旋转三角对所有 \(0<t\le R\) 成立。考虑有限维普通 PPA 类，闭非空目标 \(S\subseteq\operatorname{zer}F\)，整个距离窗 \(d(x,S)\le R\) 非空覆盖，每条允许边有最近锚下界 \(\langle x-y,y-p\rangle\ge-D(t)\) 和所述真输出误差界。下列两件事等价：

1. \(\displaystyle\int_0^R u^{m+1}/w(u)\,du<\infty\)。
2. 在这个固定缺陷与误差模的统一类内，每个算子的全部允许轨道从 \(t_0\le R\) 出发均有限长。

**充分性。** 记 \(s=\|x-y\|\)、\(\Delta=t^2-a^2\)。由 \(a^m\le s\) 和平方展开，\(H(a)\le H(t)-w(t)\)，故 \(a\le A_*(t)<t\)。在平方坐标对 \(v+v^m\) 取差，得 \(w(t)\le (1+mR^{2m-2})\Delta\)。又有 \(s^2\le\Delta+t^{2m}\)。当 \(\Delta\le t^{2m}\)，用 \(s\le\sqrt2t^m\) 及 \(w(t)\lesssim\Delta\)。当 \(\Delta\ge t^{2m}\)，用 \(s\le\sqrt{2\Delta}\le\sqrt2\Delta/t^m\) 和 \(w(t)\le t^{2m}\)。两种情形均得
\[
s\lesssim \Delta\,t^m/w(t)\lesssim\int_a^t u^{m+1}/w(u)\,du.
\]
后一估计在 \([\max(a,t/2),t]\) 积分，区间长度至少 \(\Delta/(2t)\)，用 \(w\) 的统一比较即可。零输入由 \(D(0)=0\) 强制驻定。覆盖及距离递减给续接。有限前缀求和给尾长，并由强极限和距离趋零识别零点。距离趋零也直接来自连续 \(A_*(t)<t\)。局部工作域版本可用同一长度预算小于边界余量保证留域。

**必要性。** 在平面取 \(S=\{0\}\)、\(a=A_*(t)\)、\(s=a^m\)。平方差 \(\Delta_* =t^2-A_*(t)^2\asymp w(t)\)，因此 \(a/t\to1\)、\(t-a=O(t^{2m-1})=o(a^m)\)，且 \(s=o(t)\)。小窗有 \(|t-a|<s<t+a\)。定义
\[
J(x)=\frac{a}{t}R_{\vartheta(t)}x,\qquad
\cos\vartheta(t)=\frac{t^2+a^2-s^2}{2ta},\quad t=\|x\|>0,\qquad J(0)=0 .
\]
角度取连续的 \([0,\pi]\) 分支。在窗外将半径延为 \(A_*(R)t/R\)、角度冻结为 \(\vartheta(R)\)。由半径严格递增及连续，全域 \(J\) 是连续双射，其唯一固定点为零。令 \(F=J^{-1}-I\)，即得全域连续单值原算子，完整预解式恰为 \(J\)。所有窗内图边的真残差为 \(s=a^m\)，锚定内积恰为 \(-D(t)\)。其正半径轨道 \(t_{k+1}=A_*(t_k)\downarrow0\)，两相邻半径之比趋于 \(1\)。在每段 \([A_*(t),t]\) 用 \(w\) 的比较和 \(t-A_*(t)\asymp w(t)/t\)，有 \(\int_{A_*(t)}^t u^{m+1}/w(u)\,du\asymp t^m\asymp s\)。分割求和，积分发散即实际长度发散。

例如 \(w(t)=2ct^{2m+\gamma}\)（\(c,\gamma>0\)）满足前件，\(A_*\) 的严格递增由 \(H-w\) 的导数在零附近为正得到。长度充要门为 \(m+\gamma<2\)。保持同一 \(\psi\) 与同一主阶 \(D(t)\sim t^{2m}/2\)，在 \(m+\gamma=2\) 令 \(w(t)=2ct^{2m+\gamma}[\log(1/t)]^b\)，长度充要门变成 \(b>1\)。这两族把一步严格下降与实际有限长度的边界分开，并定量说明缺陷消耗几乎全部主阶正则性余量时，剩余尺度怎样决定长度。


**S05.04：同一步常数及原目标范围补证。** 令 \(C_H=1+mR^{2m-2}\)、\(\Delta=t^2-a^2\)。上述两种情形统一给
\(s\le\sqrt2 C_H\Delta t^m/w(t)\)。在 \([\max(a,t/2),t]\) 上，长度至少 \(\Delta/(2t)\)，且 \(u^{m+1}\ge(t/2)^{m+1}\)、\(w(u)\le Kw(t)\)，故
\[
 \int_a^t\frac{u^{m+1}}{w(u)}\,du
 \ge\frac{\Delta t^m}{2^{m+2}Kw(t)},\qquad
 s\le 2^{m+2}\sqrt2KC_H
       \int_a^t\frac{u^{m+1}}{w(u)}\,du.
\]
这给可用于严格局部位置预算的明确常数，不声称最优。对取等旋转有
\(w/C_H\le\Delta_*\le w\)、\(w/(2C_Ht)\le t-a\le w/t\)，因此充分小窗中 \(a\ge t/2\)，同一壳的积分与 \(a^m\) 具有统一两侧常数，必要性不依赖数值近似。\(A_*\) 是由固定原数据推出且同图达到的包络；若预设 \(\varphi\ge A_*\)，取等见证也符合该目标。要求更小的目标时须强化数据或另证图限制，不能自动继承本统一类必要性。
