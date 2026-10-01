# M1 显式映射的一个新 Sign 实现

<a id="sl-scope"></a>
## 身份、来源和限制

这是从已核的**外层单值映射** [M1-MAP-v1](m1_capture.md#m1-object) 反向构造的关系，不是历史多步札记所称的原生循环广义方程。历史 [9 月 9 日札记 §5](../../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/多步路径与有限捕获_RL研究札记_2026-09-09.md) 只展示了外层 $T$ 并称它来自一个 `Sign` 图；[较晚的旗舰札记 §2](../../../history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/03_判别方法与理论升级/RL旗舰升级_架构与待攻关接口.md) 也只对该 $T$ 重算一步因子。两份来源均未写出足以辨认原生循环方程全部允许路径的图。本页给出一个**存在性的构造**和完整纤维，不能给历史模型作身份认证。

为避免同名混合，历史 T5E §6 另有 $F(t,y)=\{(-\sqrt y,y),(-\sqrt y,-3y)\}$ 的 `M1/SO-06` Minty coverage benchmark；那是另一个算子，不是本页的有限捕获对象。

<a id="sl-inclusion"></a>
## 标量 Sign 方程

固定 $c=2/3$，约定 $\operatorname{Sign}(0)=[-1,1]$，非零处是普通符号。令

\[
A(h)=c\operatorname{Sign}(h)+\tfrac23h^3.
\]

对**每个** $s\in\mathbb R$，包含式 $s\in A(h)$ 有唯一解

\[
h=f(s)=\operatorname{sign}(s)
  \bigl[\tfrac32(|s|-c)_+\bigr]^{1/3},
  \qquad \operatorname{sign}(0)=0.
\tag{SL1}
\]

确实，$h=0$ 当且仅当 $s\in[-c,c]$；若 $h>0$，则 $s=c+2h^3/3>c$；若 $h<0$，则 $s=-c+2h^3/3<-c$。三个区域互不交叠，各侧的三次函数严格递增且覆盖对应半轴。端点 $s=\pm c$ 只对应 $h=0$，没有因 `Sign(0)` 的区间产生额外解。

<a id="sl-graph"></a>
## 完整图、自然域和所有纤维

在 $\mathbb R^2$ 上定义**新关系** $F_{\mathrm{lift}}$：若 $y=(u,v)$ 且 $v\ne0$，置 $F_{\mathrm{lift}}(y)=\varnothing$；若 $y=(u,0)$，则

\[
 F_{\mathrm{lift}}(u,0)
 =\left\{(h,q)\in\mathbb R^2:
       u+h-3q\in c\operatorname{Sign}(h)+\tfrac23h^3
   \right\}. \tag{SL2}
\]

这列出了每个输出位置的**全部**残差值。等价的逐分支公式为

\[
\begin{array}{ll}
h>0:&q=(u+h-c-2h^3/3)/3,\\
h<0:&q=(u+h+c-2h^3/3)/3,\\
h=0:&q\in[(u-c)/3,(u+c)/3].
\end{array} \tag{SL3}
\]

因此 $\operatorname{dom}F_{\mathrm{lift}}=\mathbb R\times\{0\}$，每个轴上输入 $u$ 都有真正多值的纤维，特别是 $h=0$ 的一整段残差；图是闭的（(SL2) 中的 Sign 图闭，坐标变换连续且可逆）。这里的**算子定义域**是一条轴，和下面 resolvent 的**自然输入域**不是一回事。

取近端步长 $\lambda=1$，定义 $J_{F_{\mathrm{lift}}}=(I+F_{\mathrm{lift}})^{-1}$。对任意输入 $z=(p,q)\in\mathbb R^2$，若 $y=(u,0)\in J_{F_{\mathrm{lift}}}(z)$，置 $h=p-u$。条件 $z-y=(h,q)\in F_{\mathrm{lift}}(y)$ 恰是

\[
p-3q\in A(h).
\]

(SL1) 唯一确定 $h=f(p-3q)$ 和 $u=p-h$，所以完整 resolvent 的每个纤维都是

\[
J_{F_{\mathrm{lift}}}(p,q)
 =\bigl\{(p-f(p-3q),0)\bigr\}=\{T(p,q)\}.
\tag{SL4}
\]

它的自然 Minty 输入域 $\operatorname{ran}(I+F_{\mathrm{lift}})=\mathbb R^2$，无漏点，也无隐藏的第二 resolvent 输出。反之，(SL2) 正是由所有 $z$ 的配对 $(Tz,z-Tz)$ 反演所得；若一个关系的**完整**单位步长 resolvent 在整个平面恰为这个 $T$，它的图必为 (SL2)。这项唯一性不适用于“$T$ 是多个原生隐式步组合的外层转移”或只在局部检验过外层公式的情形。

<a id="sl-zero-residual"></a>
## 零集与真实全纤维残差

由 (SL3) 可见 $0\in F_{\mathrm{lift}}(u,0)$ 当且仅当 $h=q=0$ 被允许，即 $|u|\le c$。故

\[
\operatorname{zer}F_{\mathrm{lift}}
 =[-c,c]\times\{0\}=\operatorname{Fix}T.
\tag{SL5}
\]

令 $r_F(y)=\inf\{\|\xi\|:\xi\in F_{\mathrm{lift}}(y)\}$，空值纤维按 $+\infty$ 处理。对 $0<\delta<1$，有精确的端点计算

\[
r_F(c+\delta,0)=\delta/3,
\qquad d((c+\delta,0),\operatorname{zer}F_{\mathrm{lift}})=\delta.
\tag{SL6}
\]

证明上界只须在 (SL3) 的 $h=0$ 区间取 $q=\delta/3$。下界：若 $|h|\ge\delta/3$，则 $\|(h,q)\|\ge\delta/3$；否则 $0<h<\delta/3<1/3$ 时，$q=(\delta+h-2h^3/3)/3\ge\delta/3$；$-\delta/3<h<0$ 时，$q=(2c+\delta+h-2h^3/3)/3>\delta/3$；$h=0$ 时 (SL3) 也给 $q\ge\delta/3$。左端点由 $(u,h,q)\mapsto(-u,-h,-q)$ 对称。故在轴上零集的足够小邻域，真实残差恰为 $d(y,\operatorname{zer}F_{\mathrm{lift}})/3$，线性误差界常数 $3$ 在端点锐利；幂次 $q>1$ 不能在端点成立。**这只关于新构造 $F_{\mathrm{lift}}$**，不是旧方程的残差核验。

<a id="sl-status"></a>
## 与现有结论及未闭义务

由 (SL4)，[C38 两步捕获](m1_capture.md#m1-capture)和[C39 锐一步集合距离因子](m1_capture.md#m1-sharp)可以对这个**新定义的完整 resolvent**直接调用；它们仍未自动给 $F_{\mathrm{lift}}$ 以外的旧循环模型。该构造也展示“原图多值”和“完整 resolvent 单值”可同时成立，但原图多值不等于可从同一输入任意选择多个近端输出。

仍须从历史原始算法找回它自己的广义方程、每个相位/参数、定义域、全部图纤维和每个允许选择，再证明外层路径的对应关系。若原生算法是组合映射，则仅由 (SL4) 的反演唯一性无法识别内部图；本页不得用于关闭 [C38 的原生桥](m1_capture.md#m1-obligation)。
