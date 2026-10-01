# 绝对值次梯度：真算子残差跳跃与近端步残差

<a id="av-object"></a>
## 对象与证据范围

在实直线取**完整**凸次梯度图
\[
F=\partial|\cdot|,\qquad
F(x)=\begin{cases}\{-1\},&x<0,\\{}[-1,1],&x=0,\\\{1\},&x>0.\end{cases}
\tag{AV1}
\]
零集 \(S=F^{-1}(0)=\{0\}\)。来源观察别名 GX-077，见
[9/01 ZIP](../../../history/sources/次单调论文研究/monotonicity_regularity_research_2026-09-01.zip)
内 `work/c_gx066_077.md` 的 GX-077；下文从 (AV1) 独立计算，不继承来源的
`verified` 标签。这里的真残差始终对**全部**图值取下确界；近端步残差则是另一个对象。

<a id="av-operator"></a>
## AV-OP-v1：逆像钉住与固定零目标的零下确界模

完整逆像为
\[
F^{-1}(y)=\begin{cases}
\{0\},&|y|<1,\\{}[0,\infty),&y=1,\\(-\infty,0],&y=-1,\\
\varnothing,&|y|>1.
\end{cases}
\tag{AV2}
\]
对 \(x\ne0\)，\(r_F(x)=d(0,F(x))=1\)，而 \(r_F(0)=0\)。
于是任意 \(\varepsilon>0\) 和 \(K>0\)，在 \(|x|<\min\{\varepsilon,K\}\)
有 \(d(x,S)=|x|\le K r_F(x)\)；可取的局部线性固定零目标模的
**下确界**是 0，不是一个在固定邻域内以系数 0 成立的误差界。
同理，在 \((0,0)\) 附近固定任意小目标 \(|y|<1\)，逆像恒等于
\(\{0\}\)：局部逆选择是常值，故局部强度量正则（逆 Aubin）、
两变量度量正则和 hemiregularity 的最优下确界模均为 0。
这是值域残差与逆纤维的局部跳跃造成的强稳定性，绝不能把数值 0
解释成对任意大范围的全局估计。举例，MR 的约定是
\(d(x,F^{-1}(y))\le K d(y,F(x))\) 对靠近 \((0,0)\) 的所有 \(x,y\)；
当 \(x\ne0,|y|<1/2\) 时右侧至少 \(K/2\)，缩小输入邻域即可，
而 \(x=0\) 时左侧为零。任意 \(K>0\) 适用某个邻域。

这一零模不等于“真残差在 \(x\to0\) 时趋零”：实际 \(r_F(x)=1\)
对所有非零 \(x\) 成立。若 gauge 仅在 \([0,\eta)\)、\(\eta<1\)
定义，则其残差窗口内只含零点；这种真空陈述必须与这里的全邻域线性 EB 分开。

<a id="av-prox"></a>
## AV-PROX-v1：完整近端与固定点步残差的锐模 1

固定**任意** \(\lambda>0\)。逐段解
\(p-u\in\lambda F(u)\) 得到整个输入直线上的唯一输出
\[
J_{\lambda F}(p)=\operatorname{sgn}(p)(|p|-\lambda)_+,
\qquad \operatorname{Fix}J_{\lambda F}=\{0\}.
\tag{AV3}
\]
特别在 \(|p|<\lambda\)，\(J(p)=0\) 且
\[
d(p,\operatorname{Fix}J)=|p|=|p-J(p)|.
\tag{AV4}
\]
故固定点步残差的任意足够小输入球上的线性 EB 的**锐系数恰为 1**；
每个此球内的非零输入一步到零。原算子 \(r_F\) 的系数下确界为 0，
不能移植给 \(p-J(p)\)。全输入直线上不具有统一的步残差线性 EB：
\(|p-J(p)|=\lambda\) 当 \(|p|>\lambda\)，而 \(|p|\to\infty\)。

完整反射 \(C=2J-I\) 为
\[
C(p)=\begin{cases}p+2\lambda,&p<-\lambda,\\-p,&|p|\le\lambda,\\p-2\lambda,&p>\lambda.
\end{cases}
\tag{AV5}
\]
各段斜率的绝对值为 1 且拼接连续，故在**全部图点对**上
\(|\Delta u-\lambda\Delta v|\le|\Delta u+\lambda\Delta v|\)
且 \(L=1,\gamma=1\) 锐。无界仿射尾部排除任何有限常数的全图
\(0<\gamma<1\) 版本；有界输入窗口上可由 Lipschitz 继承次线性幂界，
不代表新的尖点机制。

<a id="av-boundary"></a>
## 适用边界与回收

同一图中，两水平支上的不同点给 \(\Delta v=0\)，零点竖支上的
两点给 \(\Delta u=0\)。凸次梯度的单调性给全部图点对
\(\Delta u\Delta v\ge0\)，因而强单调与正 cocoercive 最优模均为 0；
二参数不等式
\(\Delta u\Delta v\ge\mu(\Delta u)^2+\rho(\Delta v)^2\)
的精确区域是 \(\mu\le0,\rho\le0\)。这组图几何与 (AV2) 的
局部逆稳定、(AV4) 的近端步残差是三个不同命题坐标。

所有公式来自完整图及全纤维的解析计算，状态 `derived-checked`。
它是已知经典对象的一张辨析卡，不宣称新颖性、最优普遍定理或
GX-077 所在历史文件其它例卡已被验收。
