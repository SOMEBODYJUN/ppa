# 闭球法锥：零系数残差与逆像不稳定的分离

<a id="bn-object"></a>
## 对象与来源

固定整数 \(m\ge1\)，\(B=\{x\in\mathbb R^m:\|x\|\le1\}\)，以通常凸分析法锥定义完整关系
\[
F=N_B,\qquad F(x)=
\begin{cases}\{0\},&\|x\|<1,\\
\{tx:t\ge0\},&\|x\|=1,\\
\varnothing,&\|x\|>1.
\end{cases}
\tag{BN1}
\]
参考点是**任意** \((\bar x,0)\) 且 \(\bar x\in B\)。这里零点集 \(S=B\) 有内点；若某个不等式仅在 \(x\in B\) 且距离两边都是零，它不提供零点附近的正残差增长。历史观察别名 GX-067，来源为 `history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip!/work/c_gx066_077.md` 的 GX-067。以下证明从完整图重写，不继承旧卡的 PASS 标签或外部先行性。

<a id="bn-geometry"></a>
## BN-GEOMETRY-v1：全对图、完整纤维与反射

直接由 (BN1) 得
\[
F^{-1}(0)=B,\qquad F^{-1}(y)=\{y/\|y\|\}\quad(y\ne0),
\qquad J_{\lambda F}=P_B,\quad R_{\lambda F}=2P_B-I
\tag{BN2}
\]
对每个 \(\lambda>0\) 和整个输入空间成立。最后两式通过 \(p-u\in\lambda N_B(u)\) 等价于 \(u=P_Bp\) 得到，并未选取法锥的某一支。

对任意两图点记 \(a=x-x',b=v-v'\)。法锥不等式相加给 \(\langle a,b\rangle\ge0\)。从不同的球内部点、各取零法向得 \(a\ne0,b=0\)，故任何统一 \(\mu>0\) 不可用于 \(\langle a,b\rangle\ge\mu\|a\|^2+\rho\|b\|^2\)；从同一个边界点取不同法向得 \(a=0,b\ne0\)，故任何 \(\rho>0\) 不可用。反之 \(\mu,\rho\le0\) 由单调性自动成立。因此完整二参数区域恰为
\[
\Sigma(F)=(-\infty,0]\times(-\infty,0].
\tag{BN3}
\]
这是允许负参数的数学区域；不能将边界 \((0,0)\) 误读为强单调或正 cocoercive。

投影的 firm nonexpansiveness 给任意 \(p,q\)
\[
\|Rp-Rq\|^2=\|p-q\|^2
-4\bigl(\langle Pp-Pq,p-q\rangle-\|Pp-Pq\|^2\bigr)
\le\|p-q\|^2.
\tag{BN4}
\]
内部输入上 \(R=I\)，故全域全对线性 RL 的最优常数是 \(L=1\)。沿同一射线令 \(p=te,q=se\) 且 \(t,s>1\)，有 \(R(te)=(2-t)e\)，所以无界全输入对上任何 \(0<\gamma<1\) 的有限 Hölder 常数都失败；有界窗的低指数继承不改变这项全域断言。

<a id="bn-regularity"></a>
## BN-REGULARITY-v1：固定零目标的真空界与两变量失败

采用 \(d(0,F(x))=+\infty\) 当 \(F(x)=\varnothing\) 的扩展残差约定。对 \(x\in B\) 有 \(d(x,S)=d(0,F(x))=0\)；对 \(x\notin B\) 残差无穷。因此在每个 \((\bar x,0)\) 的固定零目标 MSR 中，**每个正系数**都可行，最优系数下确界为 \(0\)；若只在 \(\operatorname{dom}F\) 或有限残差窗口陈述，系数 \(0\) 本身也可取。全邻域上不预设 \(0\cdot(+\infty)\) 的语义。任意正幂 gauge 同样只是域内两边为零或域外不评价的**真空界**，绝非逆像对扰动目标的稳定性。\(S=B\) 没有孤立点，所以要求局部唯一零点的 SMSR 与 inverse isolated calm 均失败。Inverse calm 的普通距离形式 \(d(z,F^{-1}(0))\le\kappa\|y\|\) 对全部 \(z\in F^{-1}(y)\) 取 \(\kappa=0\)，因为这些 \(z\) 都在 \(B\)；它也不推出 inverse Aubin。

所有参考点的**两变量** MR、固定输入的 hemiregularity 及 inverse Aubin 失败，须区分位置：

* 若 \(\|\bar x\|<1\)，取任意单位 \(e\) 和 \(y=t e\to0\)。则 \(d(\bar x,F^{-1}(y))=\|\bar x-e\|\ge1-\|\bar x\|>0\)，而 \(d(y,F(\bar x))=t\to0\)。Inverse Aubin 可用 \(z=\bar x\in F^{-1}(0)\) 作同一见证。
* 若 \(\bar x=e\in\partial B\)，**每个维数**取 \(y=-te\) 且 \(t\downarrow0\)；完整逆像是 \(\{-e\}\)，到 \(e\) 的距离为 2，而 \(\|y\|=d(y,F(e))=t\)。这一序列同时否定以 \(\|y\|^q\) 作分母的 HREG、以 \(d(y,F(e))^q\) 作分母的 UHREG/MR 及 inverse Hölder–Aubin 的每个 \(q>0\)。在 \(m\ge2\) 还可取近方向的 \(y=tz,z\to e\)：此时 \(d(e,F^{-1}(y))=\|e-z\|\)，而 \(d(y,F(e))=t\sqrt{1-\langle z,e\rangle^2}\)，两变量 MR 比值渐近 \(1/t\)；这个补充见证不代替上述 HREG 的同一分母论证。

这些反例同时排除每个正指数的相应两变量 Hölder MR / 固定输入 hemiregularity，当然也排除强版本。其机制是 \(F^{-1}(0)=B\) 的大纤维遇到非零目标骤缩为一个边界点；(BN4) 的全域反射非扩张与此完全相容。

<a id="bn-boundary"></a>
## 适用边界与独立审查义务

本卡的 MSR 系数下确界零依赖完整零集 \(S=B\) 与域外残差语义；把目标改为球心 \(\{0\}\) 或改成距离到边界是**新命题**。在边界，沿原方向的正小目标仍有逆点 \(e\)，故证明全指标的失败采用反向目标；高维近方向横向扰动另说明两变量的病态比例。本卡只证明此完整法锥例的代数与局部正则量词，尚未核其历史 VI 标签、全部其它性质及外部新颖性。
