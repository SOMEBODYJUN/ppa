# LP22、P16、LMZ：解选择比较的规范一手接口

本页是规范层的原定理条件、对象映射与版本边界卡；`primary-checked` 只限明列版本/条目，`derived-checked` 另标本库直接推导。不以访问记录或历史审计替代数学接口。

证据来自三份实际 PDF 的正文及关键公式页渲染；规范页与单元表只用于确定待核问题，
没有把历史“已读全文”或审计报告当作论文证据。下文 `primary-checked` 指指定版本和条目；
从原式另行推出的共同域结论、参数换算和常数选择分别标为 `derived-checked`。

## 1. 版本与可重现定位

| 标签 | 实际核验版本 | 一手地址与范围 |
| --- | --- | --- |
| LP22 | arXiv:2004.02188v2；首页边栏 2020-04-14，文稿日期 2020-04-15；23 页，PDF 页与印刷页一致 | [固定 v2 PDF](https://arxiv.org/pdf/2004.02188v2)。Definition 2.1 pp.5–6；Lemma 2.2 p.7；Theorem 3.1 pp.12–14；Corollary 3.1 p.14；Proposition 3.1 pp.14–15。另核 [SIAM 官方书目](https://epubs.siam.org/doi/10.1137/20M1331901)：*SIAM J. Optim.* 32(1) (2022), 56–74，2022-01-05 在线发表；未将刊本数学编号视为已核 |
| P16 | arXiv:1412.2997v1；首页边栏 2014-12-09，文稿日期 2014-12-03；13 页，PDF 页与印刷页一致 | [固定 v1 PDF](https://arxiv.org/pdf/1412.2997v1)。另取得 [出版社正式 PDF](https://www.impan.pl/shop/publication/transaction/download/product/91474)：*Colloquium Math.* 144(2) (2016), 215–228，DOI [10.4064/cm6479-2-2016](https://doi.org/10.4064/cm6479-2-2016)；指定条目的跨版本差异见 §3 |
| LMZ | arXiv:2406.13207v1 | [固定 v1 PDF](https://arxiv.org/pdf/2406.13207v1)。精确版本日期、定义、定理页码及与项目步长的对应见 §4；[正式 DOI](https://doi.org/10.1287/moor.2024.0570) 的数学版本差异未核 |

三份输入 PDF 的 SHA-256（只识别所核文件，不赋予数学状态）：

```text
LP22 f58d0fdf9045de5940e5ea7d06e79f3e8e7a7c80a74a9d1eef17dc106e035131
P16  c686da4d9ebd3009c601fc5e936651504dd698914486b49a8eb29f171fdc3487
LMZ  617600f7d27a1fb35d6b4ace5d9ce0f91cc780dbd1cd5758f495cdbb9ff6b820
```

## 2. LP22：增长与闭半代数关系正则性

### 2.1 可直接导入的原陈述

**Lemma 2.2（p.7）。** 若 \(f:(0,\varepsilon)\to\mathbb R\) 半代数，且
\(f(t)\ne0\) 对所有 \(t\in(0,\varepsilon)\) 成立，则存在
\(a\ne0\)、\(\alpha\in\mathbb Q\)，使
\[
f(t)=a t^\alpha+o(t^\alpha)\quad(t\downarrow0).
\]
原假设没有另加连续性、正值、趋零或 \(\alpha>0\)。若在应用中已知
\(f>0\) 且 \(f\to0\)，才进一步有 \(a>0,\alpha>0\)。不能把这个结论
扩为任意非多项式有界 o-minimal 结构的同一有理幂主项。

**Proposition 3.1（pp.14–15，含 Definition 2.1(iii), p.5）。**
对闭图半代数关系 \(F:\mathbb R^n\rightrightarrows\mathbb R^m\)，每个
\(y_*\in\operatorname{ran}F\) 和每个紧集 \(K\subset\mathbb R^n\)，存在
\(c>0,\alpha>0\)，使
\[
\operatorname{dist}(x,F^{-1}(y_*))
\le c\,\operatorname{dist}(y_*,F(x))^\alpha\quad(x\in K).
\tag{LP-SR}
\]
这里 \(\operatorname{dist}(y,\varnothing)=+\infty\)。常数可依赖 \(F,y_*,K\)；
不是对全部目标值、全部紧集统一的常数，也没有给指定指数或最优系数。

**Theorem 3.1（pp.12–14）。** 对上述闭图半代数 \(F\)，下列条件等价：

1. \(F:\operatorname{dom}F\rightrightarrows\operatorname{ran}F\) 相对开，且
   \(\operatorname{ran}F\) 局部闭；
2. 每个 \(y_*\in\operatorname{ran}F\)、紧集 \(K\subset\mathbb R^n\) 都有
   \(\varepsilon,c,\alpha>0\)，满足
   \[
   \operatorname{dist}(x,F^{-1}(y))
   \le c\,\operatorname{dist}(y,F(x))^\alpha
   \quad(x\in K,\ y\in B_\varepsilon(y_*)\cap\operatorname{ran}F);
   \]
3. 逆关系 \(G=F^{-1}\) 为 pseudo-Hölder；准确量词为每个
   \(y_*\in\operatorname{dom}G\)、紧集 \(K\subset\mathbb R^n\)，存在
   \(\varepsilon,c,\alpha>0\)，使
   \[
   G(y_1)\cap K\subset G(y_2)+c\|y_1-y_2\|^\alpha B
   \quad(y_1,y_2\in B_\varepsilon(y_*)\cap\operatorname{dom}G);
   \tag{LP-PH}
   \]
4. 同一性质的 lower pseudo-Hölder 版本：左边固定为 \(G(y_*)\cap K\)，
   右边为 \(G(y)+c\|y-y_*\|^\alpha B\)。

该文 \(B_\varepsilon\) 为闭球。条件不要求基点在域或值域内点，也不要求
纤维有限。故单元 U060 的“有限图正则性”只宜解释成**有限维闭半代数关系**正则性，
不能读成“有限值图即自动 metrically regular”。后者仍需相对开性及局部闭值域。

**Corollary 3.1（p.14）。** 闭图半代数
\(G:\mathbb R^m\rightrightarrows\mathbb R^n\) 满足 (LP-PH)，当且仅当
\(\operatorname{dom}G\) 局部闭且原文称为 “continuous” 的条件成立：
值域内每个相对开集在 \(G\) 下的逆像，在 \(\operatorname{dom}G\) 内相对开。
这里按原文的集值逆像定义使用该术语，不额外声称 Hausdorff 连续或上下半连续同时成立。

### 2.2 与解选择稿的精确关系

这些是 **关系的半代数性已知时** 的有限维工具；它们不证明无限迭代极限的图半代数，
也不把单步映射半代数传给极限选择。它们提供存在性幂界，不给 SS 指定完整图的
数值 EB 系数、同图全对 RL 常数、可用共同窗或严格兼容不等式；这些仍须逐模型计算。
这个有限比较是从已核量词得出的 `derived-checked` 判断，不是对整篇论文的阴性结论。

AGM 的规范证明已由递推得到
\(M(1,\varepsilon)\asymp1/\log(1/\varepsilon)\)，再用非零多项式首项无法被
指数小项抵消，直接否定其图段半代数。因此 **Lemma 2.2 不是现有非半代数证明的必需依赖**。
若另用该引理作较短反证，须先在反设下确认 \(m(\varepsilon)=M(1,\varepsilon)\)
的一元图段半代数、\(m>0\)、\(m\to0\)；引理才给正有理幂主项，与对数下界矛盾。
这条可选证明不能反过来把整个极限图先当作半代数。

## 3. P16：共同速率、首轮边界与两初值模

### 3.1 函数类、原定理及版本差异

v1 p.3 的完整条件是区间 \(I\)、\(k\in\mathbb N\)、\(K>0\)，每个
\[
f_i\in\mathcal S_K(I),\quad
\mathcal S(I)=\{f\in C^2(I):f'\ne0,\ f''\text{ locally BV}\},\quad
\|f_i''/f_i'\|_\infty\le K.
\tag{P-SK}
\]
“导数不退化”在此是处处非零，不能无依据改成全区间统一下界。
局部有界变差条件不可从原文假设清单漏掉。令
\(T(x)=(f_i^{-1}(k^{-1}\sum_j f_i(x_j)))_{i=1}^k\)、
\(d_n=\max T^n x-\min T^n x\)、\(\alpha=(3+7e)/3\)。

| 原条目 | v1 准确接口／位置 | 正式版已核对应 |
| --- | --- | --- |
| Theorem 1 | p.4：\(0<\ell<1\)，\(n_0=\lceil\log_2((e^{Kd_0}-1)/(e^\ell-1))\rceil\)；对 \(n\ge n_0\) 打印 \(d_n<(\alpha K)^{-1}(\alpha\ell)^{2^{n-n_0}}\) | Theorem 3.2，PDF p.5／印刷 p.219，保留相同公式；正式版 §3 起首排除常向量，却仍未排除小非零直径导致 \(n_0<0\) |
| Theorem 2 | p.4：\(\mu=\min_{0<\ell<1}(\alpha\ell)^{(e^\ell-1)/2}\)，在 \(\ell=\xi\) 达到；打印 \(d_n<(\alpha K)^{-1}\mu^{2^n/(e^{Kd_0}-1)}\)，\(n\ge n_1=(\log_2 e)Kd_0-\log_2(e^\xi-1)+1\) | Theorem 3.3，PDF p.5／印刷 p.219；所列参数、阈值和包络相同 |
| Lemma 4.3 | p.11：\(d(x)<\min\{1/K,1\}\) 时，\(\lvert A_f(x)-\bar x\rvert<(\alpha K/2)d(x)^2\) | 仍为 Lemma 4.3，PDF p.10／印刷 p.224；改为 \(f\in\mathcal S_1(I)\) 的全直径式，对 \(d\ge1\) 补平凡估计，不能说两个版本逐字一致 |
| Theorem 3／§3.1 | pp.5–6，见下段的不变函数及同初值近似 | 指定章节检查及全文检索未找到正式对应；正式版没有此 \(\varphi\) 段，不授正式版这个定理 |
| §3.2 AGM | pp.6–7，生成元 \(t,\log t\)，\(K=1/x_{\min}\) | 正式 §5，PDF pp.12–13／印刷 pp.226–227；记较小初值为 \(y_0\)，\(K=1/y_0\) |

正式版函数类在 PDF p.4／印刷 p.218，把 locally bounded variation 称为 almost
bounded variation，并明释为每个紧区间上有限变差。本次只核上述跨版本接口，
没有声称全文差异已穷尽。正式 PDF 的 SHA-256 为
`22affac08a5450b43c173508b4e8363cb45f663e24b6b47144ad5a8b3c54dddc`。

### 3.2 原包络不能原样验收：负起步问题及安全替代

上表中的“原文打印”是 `primary-checked`，不等于原样公式已通过数学验收。
反例取 \(I=\mathbb R,K=1,f_\pm(t)=e^{\pm t}\in\mathcal S_1(I)\)，
初值 \(x=(d/2,-d/2)\)。其实际直径恰满足
\[
d_{n+1}=2\log\cosh(d_n/2),\qquad d_1\sim d^2/4\quad(d\downarrow0).
\]
固定 \(0<\ell<1/\alpha\) 时，打印的 \(n_0\to-\infty\)，且对合法的 \(n=1\)，
原右端为 \(O(e^{-c/d})=o(d^2)\)，与实际 \(d_1\) 矛盾。
对 Theorem 2 固定任一超过其极限阈值的整数 \(n\)，实际
\(d_n\sim4^{1-2^n}d^{2^n}\)，仍与打印的 \(e^{-c/d}\) 级右端冲突。
这不是浮点证据；严格 ceil 估计写于 [QA-FIRST-ROUND](selection_quasi_arithmetic_boundary.md#qa-first-round)。
判定限于所列公式和小非零直径量词，不称为正式勘误，不否定全文其它结论。

本次已独立证明可用的替代接口。**先固定**共同 \(K>0,D>0\)、
\(0<\ell<1/\alpha\)，令
\[
N=\max\left\{0,\left\lceil\log_2\frac{e^{KD}-1}{e^\ell-1}\right\rceil\right\}.
\]
则对所有 \(d(x)\le D\)、所有 \(n\ge N\)，
\[
\|T^nx-M(x)\mathbf1\|_\infty
\le d_n(x)\le\frac1{\alpha K}(\alpha\ell)^{2^{n-N}}.
\tag{P-safe}
\]
[QA-UNIFORM-TAIL](selection_quasi_arithmetic_boundary.md#qa-uniform-tail)
自足证明了该式及全步数 \(Ae^{-b2^n}\) 包络，处理 \(N=0\) 首轮、零直径、
\(K=0\) 的独立仿射情形，并保留首轮 \(1/(\alpha K)\) 与移位 \(n-N\)。
产品直径平方系数为 \(\alpha K\)；实际 \(\ell^\infty\) 点误差的安全平方系数为
\(4\alpha K\)，不能把两者混成同一常数。上述结论属 `derived-checked`，
不是把论文打印包络无说明地改成“原定理”。

### 3.3 任意复合、两初值模和 AGM 轴

v1 Theorem 3 的表示身份是：\(F\) 在各对角线点处连续且 \(F\circ T=F\)，
当且仅当 \(F=\varphi\circ M\)，其中 \(\varphi\) 连续，且
\(\varphi(t)=F(t,\ldots,t)\)。这里需要在对角点作为全域函数连续；仅
\(F|_\Delta\) 连续不足以沿轨道取极限。原陈述先写 \(F:I^k\to I\)，
其 Moreover 部分再允许 \(\varphi:I\to\mathbb R\) 并用连续模 \(\omega_\varphi\)。
对 \(n>n_1\)、每个坐标 \(i\)，打印的是
\[
|F(x)-\varphi([T^nx]_i)|
\le\omega_\varphi\!\left((\alpha K)^{-1}
\mu^{2^n/(e^{Kd(x)}-1)}\right).
\]
这是同一初值的有限迭代近似误差，且其定量部分继承上述包络漏洞；表示身份本身不受影响。
正确近似式可由 (P-safe) 直接替换得到。原证明 p.6 的起首 \(n\ge n_0\)
与陈述 \(n>n_1\) 不一致，调用时不沿抄这处符号。

“没有在这三个定理陈述两初值模”不意味着此模型没有好选择模。
[QA-SELECTION](selection_quasi_arithmetic_boundary.md#qa-selection)
另行证明在同一凸域 \(X_D=\{x:d(x)\le D\}\) 上
\[
|M(x)-M(y)|\le \exp(2(e^{KD}-1))\|x-y\|_\infty.
\tag{P-Lip}
\]
其导数乘积包含 \(j=0\) 首步，系数中的 2 来自
\(\sum_{j=0}^\infty2^{-j}=2\)。这是 `derived-checked`，不归作 P16 的原定理。
任意连续 \(\varphi\) 属于固定 \(M\) 的复合自由度，不授予 \(M\) 任意粗糙性。

AGM 的 \(P_{\log}(t)=-1/t\) 及 \(K=1/x_{\min}\) 已核。
固定正窗能给共同有限 \(K\)；包含轴时生成元不定义，且正窗靠轴时 \(K\) 发散。
因此正窗的共同二次／双指数尾不能拼接到含坏轴的初值域。

## 4. LMZ：实际点率、参数倒数及恒定选择

首页边栏是 **arXiv:2406.13207v1，2024-06-19**；首页文稿日期为 **2024-06-21**，
两者不混写。作者为 Guoyin Li、Boris Mordukhovich、Jiangxing Zhu，题名
*Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*。
33 页，PDF 页与印刷页一致；实际渲染核了首页、pp.3–4、7–11。

### 4.1 Theorems 4.3–4.4 的全部调用门

共同背景（pp.3–4、7）：\(f:\mathbb R^m\to(-\infty,+\infty]\) proper、l.s.c.、
下有界；\(\partial f\) 是 limiting/Mordukhovich 次微分，
\(\Gamma=\{x:0\in\partial f(x)\}\)。\(\Omega\) 是**所研究序列**的聚点集。
admissible 的原定义仅为 \(\varphi(0)=0\) 和
\(\varphi(t)\to0\Rightarrow t\to0\)，不自行加连续或凸。
\((x_k,e_k)\in\mathbb R^m\times\mathbb R_+\) 的基本条件是
\[
\begin{array}{ll}
\mathrm{H0}:&f(x_{k+1})\le f(x_k),\\
\mathrm{H1}:&\|x_{k+1}-x_k\|\le c e_k,\quad c>0,\quad e_k\to0,\\
\mathrm{H2}:&\exists w_{k+1}\in\partial f(x_{k+1}),\quad
 \|w_{k+1}\|\le b\beta(e_k),\quad b>0,\quad\beta\text{ admissible},\\
\mathrm{H3}:&x_{k_j}\to\widetilde x\ \Longrightarrow\
 \limsup_j f(x_{k_j})\le f(\widetilde x).
\end{array}
\tag{LM-BA}
\]

**Theorem 4.3**（陈述 p.8，证明 p.9，尾估计 p.10）还要求：某个
\(\mathcal L(f(x_{k_0}))=\{x:f(x)\le f(x_{k_0})\}\) 有界；固定
\(\bar x\in\Omega\subseteq\Xi\subseteq\Gamma\)、\(\Xi\) 闭；
\(\xi:[0,\eta)\to\mathbb R_+\) 非减连续、\(\xi(0)=0\)、\(\eta>0\)；
\(s_k\ge0,s_k\to0\)。\(\tau:\mathbb R_+\to\mathbb R_+\) 非减，并满足
\[
\tau(0)=0,\qquad
\limsup_{t\downarrow0}\sum_{j=0}^\infty\frac{\tau^j(t)}t<\infty,
\]
其中 \(\tau^j\) 是迭代复合，\(\tau^0(t)=t\)。存在
\(\ell_1\in[0,1),\ell_2,\ell_3\ge0,k_1\ge1\)，使每个
\(k\ge k_1\) 且 \(x_k\in B(\bar x,\eta)\) 都满足
\[
s_k\le\tau(s_{k-1}),\quad
e_k\le\ell_1e_{k-1}+\ell_2\Lambda_{k,k+1}+\ell_3s_k,
\quad
\Lambda_{k,k+1}=\xi(f(x_k)-f(\bar x))-\xi(f(x_{k+1})-f(\bar x)).
\]
结论是最终留在该邻域，\(\sum e_k<\infty\)、轨道有限长且整列
\(x_k\to\bar x\in\Xi\)。式 (4.12) 对充分大 \(k\) 给
\[
\|x_k-\bar x\|\le\frac c{1-\ell_1}
\left(\ell_1e_{k-1}+\ell_2\xi(f(x_k)-f(\bar x))
+\ell_3\sum_{j=0}^\infty\tau^j(s_k)\right).
\tag{LM-tail}
\]
所以 4.3 本身是有限长／收敛框架，不单独授予高阶 Q 点率。

**Theorem 4.4**（p.10）保留共同背景、(LM-BA)、上述有界 level set 和
\(\bar x\in\Omega\subseteq\Xi\subseteq\Gamma\) 的闭目标集；另要求
\(\psi,\beta\) 为 increasing admissible functions，以及
\[
\begin{split}
\psi(d(x,\Xi))&\le\gamma d(0,\partial f(x))
 &&\text{对每个 }x\in B(\bar x,\eta),\quad\gamma,\eta>0,\\
e_k&\le\ell d(x_k,\Xi)
 &&\text{对全部 }k\ge k_1,\quad\ell>0,\\
\tau(t)&=\psi^{-1}(\gamma b\beta(\ell t)),
 &&\limsup_{t\downarrow0}\tau(t)/t<1.
\end{split}
\tag{LM-rate-gates}
\]
结论是 \(x_k\to\bar x\in\Xi\) 及式 (4.15)
\[
\|x_k-\bar x\|=O\bigl(\tau(\|x_{k-1}-\bar x\|)\bigr).
\]
这是到**具体极限点**的误差，不仅是到目标集的距离；但数据属于给定序列及其聚点，
不能直接升级为跨初值共同窗、共同尾或两初值选择模。点态 subregularity 的“点态”
指固定基点的邻域版本；不把上式的全邻域点量词缩成仅沿轨道。

原文直接使用 \(\psi^{-1}\)，没有另定义广义逆；本次没有从 increasing admissible
自行推出连续、满射或全域反函数。具体应用须核所选反函数在相关输入有定义。
下例 \(\psi(t)=\tfrac32\sqrt t\) 的普通反函数明确，因此无此接口疑点。

**Remark 4.5**（p.11）指出对相应 proximal methods，选
\(e_k=\|x_{k+1}-x_k\|,\Xi=\Gamma\) 时目标集步界可自动成立；
\(\psi(t)=t^p,p\in(0,1)\) 给至少 \(1/p\) 阶超线性。
这仍在 Theorem 4.4 与相应算法背景下调用，不删去 (LM-BA)、level boundedness
等条件。本次未独立导入其参考文献 [5] 全算法框架或 Section 7 全部 Newton 结论。

### 4.2 Example 4.6：步长换算和唯一极限

原文 p.11 的打印对象为
\[
f(t)=|t|^{3/2},\quad t_0=1,\quad
t_{k+1}=\arg\min_{t\in\mathbb R}
\left\{|t|^{3/2}+\frac{\lambda_L}{2}(t-t_k)^2\right\},\quad\lambda_L>0.
\tag{LM-example}
\]
若项目步长 \(h\) 定义为 \(J_{hF}=(I+hF)^{-1}\)，则
\[
F=\partial f,\qquad h=1/\lambda_L.
\tag{LM-parameter}
\]
\(\lambda_L\) 是二次目标项系数，不是项目同名的 prox 步长。
原正轨道满足 \(t_k=t_{k+1}+\frac3{2\lambda_L}\sqrt{t_{k+1}}\)，且
\[
t_{k+1}=\left(\sqrt{t_k+\frac9{16\lambda_L^2}}-\frac3{4\lambda_L}\right)^2
=\left(\frac{t_k}{\frac3{4\lambda_L}+\sqrt{t_k+\frac9{16\lambda_L^2}}}\right)^2.
\tag{LM-update}
\]
原文明示 \(t_k\to0\) 且 \(t_{k+1}=O(t_k^2)\)。可以取
\(c=\ell=\gamma=1,b=\lambda_L,\beta(t)=t,\psi(t)=\frac32\sqrt t\)，从而
\(\tau(t)=\frac{4\lambda_L^2}{9}t^2\)。从已核显式更新另算出的精确系数是
\(\lim_k t_{k+1}/t_k^2=4\lambda_L^2/9=4/(9h^2)\)，这一等式标为本次推导。

完整关系
\(F(t)=\{\frac32\operatorname{sign}(t)\sqrt{|t|}\}\) 的零集恰为 \(\{0\}\)。
若把选择域扩为所有实初值，需补下列直接证明，不能冒称原例明写此量词：
每个 prox 目标连续、coercive、强凸，故全局极小点存在唯一；令
\(a=3/(4\lambda_L)\)，完整更新为
\[
T(t)=\operatorname{sign}(t)(\sqrt{|t|+a^2}-a)^2.
\]
它固定 0，对非零输入保号且严格缩小绝对值。因此绝对值趋于某个 \(r\ge0\)，
在关系式取极限得 \(r=r+\frac3{2\lambda_L}\sqrt r\)，故 \(r=0\)。
对每个实初值只有一条合法路径，且极限选择恒为 \(S(t_0)=0\)。
这是 `derived-checked` 的全实域扩展；原点 Q-二次不能据此推出选择粗糙性或该方面新颖性。

## 5. 精确单元接收建议与仍未关闭事项

表内 Uxxx 指来源稳定单元 `SS1-S6-Uxxx`；现行原子表已按这些范围同步，新增拆分为 U118/U119。表述是来源接口与剩余义务，不作全篇验收。

| 单元 | 本次可接收状态 | 明确保留的边界 |
| --- | --- | --- |
| U055 | v1 4.3 框架、4.4 实际点率接口 `primary-checked` | 4.3 与 4.4 作用分开；不授共同初值域或选择模 |
| U056 | v1 原例 \(t_0=1\) 的 Q-二次 `primary-checked` | \(h=1/\lambda_L\)；精确 Q 系数属本次推导 |
| U057 | 原例零集、打印轨道到 0 已核；全实初值／全路径扩展 `derived-checked` | 不把扩展量词冒称原例明述 |
| U058 | 恒定选择条件现已实例化，`derived-checked` | 不关闭新颖性 |
| U059 | v2 Lemma 2.2 `primary-checked` | 非零假设及有理指数范围；不是 AGM 直接反证的必需依赖 |
| U060 | v2 Prop.3.1／Th.3.1／Cor.3.1 `primary-checked` | 刊本数学跨号仍 `deferred`；“有限图”须改成有限维闭半代数关系 |
| U061 | 保持 AGM 自足推导的 `derived-checked` | 不改成论文证明的无限迭代闭包定理 |
| U062 | 已核存在性量词支持的有限比较 `derived-checked` | 未给具体图数值常数或严格兼容 |
| U066 | 拆成“原打印公式已核且存在小直径漏洞”与 C160 修复共同尾 `derived-checked` | **不能**把原 Theorem 2 包络全初值原样记为正确／已验收 |
| U067 | 两版本完整 \(\mathcal S_K\) 条件 `primary-checked` | 补回 \(f_i''\) 局部 BV；不误改为全域导数共同正下界 |
| U068 | 两版本 AGM 生成元、\(K=1/x_{\min}\) `primary-checked`；轴不统一为直接推论 | 不接收其继承有问题包络的全部定量式 |
| U069 | v1 的 \(\varphi\circ M\) 表示身份与对象 `primary-checked` | 定量式须用修复尾；正式版不授此 Theorem 3 |
| U070 | 固定 \(M\) 与任意 \(\varphi\) 的逻辑边界 `derived-checked` | 本次另有 (P-Lip)，不是原论文两初值定理 |
| U090 | `deferred` | LMZ 正式刊本正文、数学编号／增改未比对 |
| U107 | LP22 v2 身份／条目及 SIAM 正式书目 `primary-checked` | 刊本数学内容跨号未核，不称全文版本已核 |
| U112 | LMZ v1 身份、日期、指定条目 `primary-checked` | DOI 正式版书目详情／数学版本差异 `deferred` |
| U114 | P16 v1 及正式书目、表列跨号／差异 `primary-checked` | 不称全部差异穷尽，不把 v1 Th.3 归给刊本 |

三份原文的指定接口已经实际核过；仍未关闭的是各自明确保留的版本／应用桥，
以及有限阴性检索、精确联合贡献的新颖性和全球优先权。这些状态彼此独立。
未审计本文之外的文献条目，也没有把本次发现外推为作者全部结果的错误。
