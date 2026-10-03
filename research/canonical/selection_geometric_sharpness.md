# 几何 cap 图的首次切换与极限选择锐模

<a id="gs-sharp"></a>
## C138：同一完整近端的配对下界

对象严格沿用 [C137 的完整 \(F,T,S\)](selection_geometric_cap.md#gc-object)，
不改变图、步长或残差。固定任意 \(0<r_0<1\)，比较
\[
x_0=(0,0,r_0),\qquad x_\varepsilon=(0,\varepsilon,r_0)
\quad(0<\varepsilon<\varepsilon_0(r_0)).
\]
两条轨道的第一、第三坐标完全相同。零初始第二坐标的轨道
始终为零；正初始第二坐标的轨道满足
\[
p_{k+1}=p_k+\sqrt{\min\{p_k,r_k\}},\quad
p_0=\varepsilon,\quad r_k=r_0\,4^{-k}.                         \tag{GS-1}
\]
令 \(\Pi\) 为同一完整 \(T\) 的极限选择。存在仅依赖 \(r_0\)
的 \(c,C,\varepsilon_0>0\)，使
\[
c\,\frac{\log\log(1/\varepsilon)}{\log(1/\varepsilon)}
\le\|\Pi(x_\varepsilon)-\Pi(x_0)\|
\le C\,\frac{\log\log(1/\varepsilon)}{\log(1/\varepsilon)}.
                                                                    \tag{GS-2}
\]
所以对任意 \(\theta>0\)，此比值除以
\(\|x_\varepsilon-x_0\|^\theta=\varepsilon^\theta\) 发散。
这是**指定配对**的锐阶，不声称归一化比值有极限。
若要把它读作 [C137 的同一局部 RLEB 证书](selection_geometric_cap.md#gc-certificates)
内的锐性见证，另选 \(0<r_0\le R<R_*=
[2(4-2\sqrt2)/5]^2\)；任意 \(r_0<1\) 的公式本身不依赖
该证书半径。

### 自足的首次切换证明

取足够小 \(\varepsilon<r_0\)，令
\[
t=\log(1/\varepsilon),\qquad
N=\min\{k\ge0:p_k\ge r_k\}.
\]
\(N\ge1\) 且有限：若一直未切换，则 \(p_k\ge\varepsilon\)
而 \(r_k\to0\)。固定有限 \(k\) 时，(GS-1) 的迭代随
\(\varepsilon\downarrow0\) 连续趋向零，而 \(r_k>0\)，故
\(N\to\infty\)。对 \(k<N\)，有 \(0<p_k<r_k\le r_0<1\)，
于是 \(\sqrt{p_k}\le p_{k+1}\le2\sqrt{p_k}\)。
从 \(p_0=e^{-t}\) 归纳得到包括 \(k=N\) 的统一界
\[
e^{-t2^{-k}}\le p_k\le4e^{-t2^{-k}}
\qquad(0\le k\le N).                                         \tag{GS-3}
\]
上界的常数 4 不随 \(N,t\) 变化。

令 \(A=t2^{-N}\)、\(a=\log4\)。由 \(p_N\ge r_0\,4^{-N}\)
与 (GS-3) 的上界，以及 \(p_{N-1}<r_0\,4^{-(N-1)}\)
与其下界，分别得到
\[
\frac{(N-1)a-\log r_0}{2}<A
\le Na+\log(4/r_0).                                          \tag{GS-4}
\]
故 \(A=\Theta(N)\)，其中常数依赖固定 \(r_0\)；
恒等式 \(t=A2^N\) 给
\(\log t=N\log2+\log N+O(1)\)，从而
\[
N=\frac{\log t-\log\log t}{\log2}+O(1),
\qquad 2^{-N}=\Theta(\log t/t).                               \tag{GS-5}
\]

切换后 \(p_k\) 不减、\(r_k\) 递减，故以后一直处于饱和段；
因此有**精确**尾公式
\[
p_\infty=p_N+\sum_{k=N}^{\infty}\sqrt{r_k}
=p_N+2\sqrt{r_0}\,2^{-N}.                                  \tag{GS-6}
\]
在切换前一步，
\(p_N=p_{N-1}+\sqrt{p_{N-1}}
<r_{N-1}+\sqrt{r_{N-1}}
\le(4\sqrt{r_0}+2)\sqrt{r_N}\)；
另一方面 (GS-6) 给 \(p_\infty\ge2\sqrt{r_N}\)。
故 \(p_\infty=\Theta(2^{-N})\)，由 (GS-5) 即为 (GS-2)。
两轨道其余极限坐标相同，极限差的 Euclidean 范数恰为
\(p_\infty\)。最后
\((\log t/t)e^{\theta t}\to\infty\) 证明任意正阶 Hölder 失败。

**来源与范围。** SS1 修订包 `research_note.md` §3 定理 3
（294–358 行）给出路线。本页重新固定首次切换的两侧不等式、
有限前缀的**同一**常数、饱和后的精确尾及与 C137 证书半径的
身份关系。它不核文献先行性、一般参数族或 §5.2 推论。
