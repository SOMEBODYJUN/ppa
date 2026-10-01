# 正值正弦映射：临界反射模与非零目标的量词隔离

<a id="sin-object"></a>
## 完整对象与来源

固定完整单值映射 \(F:\mathbb R\to\mathbb R,\ F(x)=2+\sin x\)。
对每个 \(\lambda>0\)，令
\[
 g_\lambda(x)=x+\lambda F(x),\qquad
 c_\lambda(x)=x-\lambda F(x),\qquad
 J_{\lambda F}(p)=g_\lambda^{-1}(p).
\tag{SN1}
\]
全对 RL 在声明的图窗 \(W\) 上要求**每对** \(x,y\in W\) 满足
\(|c_\lambda(x)-c_\lambda(y)|\le L|g_\lambda(x)-g_\lambda(y)|^\gamma\)。
因 \(1\le F\le3\)，连续的 \(g_\lambda(x)-x\) 有界，故
\(g_\lambda\) 满射，每个完整 resolvent 输入均有输出，但在
\(\lambda>1\) 可多值。原算子零集 \(S=F^{-1}(0)=\varnothing\)。

来源为 9/01 ZIP `work/c_gx053_065.md` 的 GX-064 观察，精确成员
定位见[逐单元去向](../../audit/UNIT_DISPOSITIONS.tsv)。旧卡的
`C-DISAGREE-064` 标签只表示后来区分了两种局部常数；其
`work/c_consistency_audit.md` CCA-M08 已修为 `C-REFINE`，
不能说旧卡有一个被反例推翻的同一陈述。下文从完整映射重算。

<a id="sin-phase"></a>
## C81-v1：步长三相与临界全对常数

**\(0<\lambda<1\).** 每个不同 \(x,y\) 的正弦割线斜率
\(s=(\sin x-\sin y)/(x-y)\in[-1,1]\)，所以
\[
 { |c_\lambda(x)-c_\lambda(y)|\over
   |g_\lambda(x)-g_\lambda(y)|}
 ={1-\lambda s\over1+\lambda s}
 \le {1+\lambda\over1-\lambda}.                 \tag{SN2}
\]
\(g'_\lambda\ge1-\lambda>0\)，完整 \(J\) 全域单值；割线趋向
奇数倍 \(\pi\) 的负单位导数，证明全图线性 RL 锐常数
\((1+\lambda)/(1-\lambda)\)。

**\(\lambda=1\).** \(g'_1=1+\cos x\ge0\)，其零点离散，故
\(g_1\) 严格增且全域双射。固定任意 \(x_0=(2m+1)\pi\)，写
\(x=x_0+h,y=x_0+k\)。Minty 与 Cayley 差分别为
\(\phi(h)-\phi(k)\)、\(\psi(h)-\psi(k)\)，其中
\(\phi(t)=t-\sin t,\ \psi(t)=t+\sin t\)。
在 \(x_0\) 的任意充分小参数窗上，全对 \(\gamma=1/3\) 可行，
其**缩窗可行常数的下确界**恰为
\[
 L^*_{\rm all}=4\sqrt[3]{3},
 \qquad L^*_{\rm fixed\ base}=2\sqrt[3]{6}
 \quad (k=0).                                      \tag{SN3}
\]
证明不能只对固定 \(k/h\) 取 Taylor 极限。给任意
\(\varepsilon\in(0,1)\)，缩窗令
\(1-\cos t\ge(1-\varepsilon)t^2/2\)。对 \(h>k\) 置
\(d=h-k\)、\(s=h^2+hk+k^2\)。积分给
\(\phi(h)-\phi(k)\ge(1-\varepsilon)ds/6\)，
\(|\psi(h)-\psi(k)|\le2d\)，而 \(d^2\le4s\)。因此
\[
 {|\psi(h)-\psi(k)|^3\over\phi(h)-\phi(k)}
 \le {192\over1-\varepsilon}.                       \tag{SN4}
\]
取对称 \(k=-h\to0\)，该商趋于 192，给全对锐常数；固定
\(k=0\) 的比值趋于 \(2\sqrt[3]6\)。固定基点序列亦排除
\(\gamma>1/3\) 的局部有限常数。\(0<\gamma<1/3\) 可缩窗
获得常数下确界 0；(SN3) 不宣称在某个预定窗口上恰取常数。

全图的任何 \(0<\gamma<1\) 则对**每个** \(\lambda>0\)
失败：取 \(x=0,y=2\pi n\)，\(F(x)=F(y)\)，输入与反射增量
均为 \(2\pi n\)，商 \((2\pi n)^{1-\gamma}\to\infty\)。
在 \(\lambda=1\) 时 (SN3) 又排除全图线性 RL。

**\(\lambda>1\).** 存在 \(h\in(0,\pi)\) 解 \(h=\lambda\sin h\)：
\(\lambda\sin h-h\) 在零右方为正，在 \(\pi\) 为负。取
\(x=x_0+h,y=x_0-h\)，则
\(g_\lambda(x)-g_\lambda(y)=0\)，但
\(|c_\lambda(x)-c_\lambda(y)|=4h>0\)。完整图在同一输入
碰撞，所以任何零点消失的全图反射模均失败；这**不排除**
避开折点的较小局部分支具有 Lipschitz 界。

<a id="sin-target"></a>
## C82-v1：非零目标的锐半阶误差界

目标取 \((\bar x,\bar y)=(\pi/2,3)\)，与上面的临界图点
\((x_0,F(x_0))=(x_0,2)\) **不同**。在 \(\bar x\) 附近，
\(d(\bar x+h,F^{-1}(3))=|h|\)，
\(|F(\bar x+h)-3|=1-\cos h\sim h^2/2\)。因此固定目标
\[
 d(x,F^{-1}(3))\le K|F(x)-3|^q
\tag{SN5}
\]
的最高局部幂是 \(q=1/2\)，该幂缩窗系数下确界为
\(\sqrt2\)；\(q<1/2\) 时下确界为 0，\(q>1/2\) 时无有限
系数。两目标的 MR 型结论不能借此获得：令 \(x=\bar x\)、
\(y\downarrow3\) 且 \(y>3\)，则 \(F^{-1}(y)=\varnothing\)
而 \(|F(x)-y|\) 有限。这里所有残差均相对**非零目标 3**，
从未断言 \(d(x,S)\) 的零目标 EB。

<a id="sin-boundary"></a>
## 不能拼接成零点 PPA；实际路径的精确边界

\(S=\varnothing\)，所以 C81 临界全对证书与 C82 的非零目标
半阶 EB 没有共同零目标。任何固定 \(\lambda>0\) 的完整近端
路径 \(p_{k+1}\in J_{\lambda F}(p_k)\) 均满足
\[
 \lambda\le p_k-p_{k+1}=\lambda F(p_{k+1})\le3\lambda,
 \qquad p_0-3k\lambda\le p_k\le p_0-k\lambda.
\tag{SN6}
\]
因此**每条**无限合法选择路径趋向 \(-\infty\)。这条直接
推导不是来源中的收敛主张，更不能把非零目标的局部 EB 与
不同图点的局部 RL 相乘为零集收敛率。旧卡的其它 VI 标签、
二参数类、外部先行性与不同步长的局部最优常数未在本页验收。
