# 衰减切向敏感度恢复极限选择稳定性

<a id="tc-triangle"></a>
## C140：三角动力学与全域条件

取 Euclidean \(\mathbb R^m\times[0,R]\)，\(m\ge1\)、
\(0<R<\infty\)、\(0<q<1\)、\(C,H,\eta>0\)、
\(0<\gamma\le1\)。设
\[
T(a,r)=(a+B(a,r),qr),\qquad
B:\mathbb R^m\times[0,R]\longrightarrow\mathbb R^m,
\]
且对**全部** \(a,b\in\mathbb R^m\)、\(r,s\in[0,R]\)
一致满足
\[
B(a,0)=0,\qquad
\|B(a,r)-B(b,r)\|\le Cr^\eta\|a-b\|,\qquad
\|B(a,r)-B(a,s)\|\le H|r-s|^\gamma.                 \tag{TC-1}
\]
此页不要求 \(T\) 已表示为某个完整近端；它是可以**另行**
用于该种三角表示的动力学充分条件。全切向域自动留域，
若只在子域认证 (TC-1)，须再证明所有比较轨道留在该域。

<a id="tc-proof"></a>
## 有限长度、统一尾与混合 Hölder 估计

\(B(a,0)=0\) 与第三式给 \(\|B(a,r)\|\le Hr^\gamma\)。
对任意初值 \((a,r)\)，令 \((a_k,r_k)=T^k(a,r)\)，则
\(r_k=q^kr\)，而
\[
\sum_{k\ge0}\|T^{k+1}(a,r)-T^k(a,r)\|
\le\frac{Hr^\gamma}{1-q^\gamma}+r.               \tag{TC-2}
\]
因此存在 \(\Pi(a,r)=(\Pi_a(a,r),0)\)；它固定零平面，
且每个 \(k\) 的点尾至多
\[
\|T^k(a,r)-\Pi(a,r)\|
\le\frac{Hr^\gamma q^{\gamma k}}{1-q^\gamma}+rq^k.
                                                               \tag{TC-3}
\]

比较另一初值 \((b,s)\)，设
\(u_k=\|a_k-b_k\|\)。在同一 \(k\) 先改变切向点、
再改变法向参数，(TC-1) 给
\[
u_{k+1}\le(1+Cr^\eta q^{\eta k})u_k
 +Hq^{\gamma k}|r-s|^\gamma.                        \tag{TC-4}
\]
每段有限递推的乘积不超过
\(K=\exp(CR^\eta/(1-q^\eta))\)。变常数并求和，取
\(k\to\infty\)，得到对全部初值对的**混合**估计
\[
\|\Pi_a(a,r)-\Pi_a(b,s)\|
\le K\left(\|a-b\|+
\frac{H}{1-q^\gamma}|r-s|^\gamma\right).       \tag{TC-5}
\]
当 \(\gamma=1\) 它是全局 Lipschitz；当 \(\gamma<1\)，
仅在输入点对尺度 \(\delta\le D\) 可写成普通
\(\gamma\)-Hölder 系数
\(K[D^{1-\gamma}+H/(1-q^\gamma)]\)。在无界全切向域
不可声称全局纯 \(\gamma\)-Hölder，因为 \(\Pi_a(a,0)=a\)。

<a id="tc-boundary"></a>
## 尖点模型不满足此充分门

对 [C139](selection_parameter_family.md#pf-object) 的完整近端，
限制在不变的 \(r\ge0\) 子域，切向量为 \(a=(z,p)\)，
\(\mathcal B(a,r)=(Ar^\gamma,B\min\{p_+,r\}^\gamma)\)。
固定任意 \(r>0\)，取 \(a=(0,\varepsilon),b=(0,0)\)，
\(0<\varepsilon<r\)，则
\[
\frac{\|\mathcal B(a,r)-\mathcal B(b,r)\|}{\|a-b\|}
=B\varepsilon^{\gamma-1}\longrightarrow\infty.
\]
因此 (TC-1) 的**同法向切向 Lipschitz 不等式**在此例失败，C137 是
\(\gamma=1/2,q=1/4,A=B=1\) 的同一特例。这个计算只定位
一种**充分条件**缺失；不声称它对所有稳定模型必要，也
不把带 \(q|r|\) 的全符号法向映射误读为本页的 \(qr\)。

**来源与范围。** SS1 修订包 `research_note.md` §5.2
（608–641 行）是重写线索；(TC-2–5) 的统一常数、全域
量词和纯 Hölder 的输入尺度在此独立明确。一般曲面或
耦合法向动态、对原生完整算子模型的认证与外部先行性
均不在本命题范围。
