# C219-v1：临界对数螺旋的完整共振长度判据

- **Status**：`derived-checked`；[独立敌对审查](../novelty/2026_10_09/new_claim_review.md)及[独立总复核](../novelty/2026_10_09/independent_review.md)分别重构相邻逆尾、全部余项常数及共振径向主步。本页不宣称全球新颖性。
- **对象身份**：保持 [C214 的完整关系、完整 warped resolvent 与物理拉回](../comparisons/2026_08_gppa_nfb/gppa_physical_transfer.md#gp-spiral)。只细化其中 \(a=2\) 的尾轨道和任意 twist 常数；不改变 C214 已校准的 \(c=\pi/(\log4)^2\) 结论。
- **新增内容**：校准外的临界参数分类、整圈共振时的可控余项与有限长度。几何半阶有 [Fraser 的先行定理](../novelty/2026_10_09/physical_prior_art.md#ppa-frase)；本页不能把该指数重新作为创新点。

<a id="gsr-statement"></a>
## 1. 精确陈述

令 \(h=\log4\)，\(0<y_0\le e^{-2}\)，\(q=\log(e/y_0)/h\ge3/h>1\)，并使用 C10 的同一个完整剖面

\[
\ell_2(t)=[\log(e/t)]^{-2}\quad(0<t\le e^{-2}),\qquad
\ell_2(t)=\frac{1+2e^2t}{27}\quad(t\ge e^{-2}),\qquad \ell_2(0)=0.
\tag{SR1}
\]

因此整条尾 \(y_k=4^{-k}y_0\) 始终处在对数公式段，且

\[
u_k=k+q,\qquad
\rho_k=\sum_{j=k}^{\infty}\ell_2(y_j)
=h^{-2}T(u_k),\qquad
T(u)=\sum_{j=0}^{\infty}(u+j)^{-2}.
\tag{SR2}
\]

对任意 \(c\in\mathbb R\)，置 \(g_c(z)=e^{ic/|z|}z\)（\(z\ne0\)）与 \(g_c(0)=0\)，并取 C214 的完整数据

\[
G_2(w_1,w_2,y)=\{(-\ell_2(4y),0,3y),(-\ell_2(4y),0,-5y)\}\ (y\ge0),
\qquad G_2=\varnothing\ (y<0),
\]
\[
v_c(x_1,x_2,y)=(g_c^{-1}(x_1+ix_2),y),\qquad F_{2,c}=G_2\circ v_c,
\qquad \lambda=1.
\tag{SR3}
\]

则 \(w_k=(-\rho_k,0,y_k)\)、\(x_k=(g_c(-\rho_k),y_k)\) 是同一完整 GPPA 的合法轨道，核有限长、物理点趋零；物理长度具有精确判据

\[
\boxed{\ \sum_{k=0}^{\infty}\|x_{k+1}-x_k\|<\infty
\quad\Longleftrightarrow\quad c(\log4)^2\in2\pi\mathbb Z.\ }
\tag{SR4}
\]

更精确地，令 \(L=ch^2\)。若 \(L\notin2\pi\mathbb Z\)，则

\[
\|x_{k+1}-x_k\|\sim
\frac{2|\sin(L/2)|}{h^2(k+q)}.
\tag{SR5}
\]

若 \(L\in2\pi\mathbb Z\)（含 \(c=0\)），则

\[
\|x_{k+1}-x_k\|\sim\frac1{h^2(k+q)^2}.
\tag{SR6}
\]

对原 C214 的 \(c>0\)，共振集合恰为 \(c=2\pi n/h^2\)、\(n\ge1\)。\(c=0\) 是恒等核的退化边界，最佳几何指数为 1；不把它称为半阶 twist。

<a id="gsr-em"></a>
## 2. Euler–Maclaurin 的显式余项

以下不是只有形式展开的渐近证明。对 \(f(x)=x^{-2}\)，无穷区间 Euler–Maclaurin 的前两个偶 Bernoulli 修正给

\[
T(u)=\frac1u+\frac1{2u^2}+\frac1{6u^3}-\frac1{30u^5}+R_{\rm EM}(u),
\quad |R_{\rm EM}(u)|\le\frac1{30u^5}\quad(u>0).
\tag{SR7}
\]

可直接检查余项界：周期 \(B_4(t)=t^2(t-1)^2-1/30\) 在 \([0,1]\) 满足 \(|B_4|\le1/30\)，而

\[
\frac{\|B_4\|_\infty}{4!}\int_u^\infty|f^{(4)}(x)|\,dx
\le\frac{1/30}{24}\int_u^\infty120x^{-6}\,dx
=\frac1{30u^5}.
\]

所以可写

\[
T(u)=u^{-1}+\tfrac12u^{-2}+\tfrac16u^{-3}+R(u),
\qquad |R(u)|\le\tfrac1{15}u^{-5}.
\tag{SR8}
\]

尾恒等式 \(T(u+1)=T(u)-u^{-2}\) 给

\[
D(u):=u^2T(u)T(u+1)=1+\frac1{12u^2}+E(u),
\qquad |E(u)|\le\frac{169}{900}u^{-4}\quad(u\ge1).
\tag{SR9}
\]

确实，令 \(A(u)=\tfrac16u^{-3}+R(u)\)，则

\[
T(u)T(u+1)=(u^{-1}+A(u))^2-\tfrac14u^{-4},
\quad E(u)=2uR(u)+u^2A(u)^2.
\]

由 \(|A(u)|\le(7/30)u^{-3}\)，得到 \(2/15+49/900=169/900\) 的界。
积分比较还给 \(T(u)\ge1/u\)、\(T(u+1)\ge1/(u+1)\)，故 \(D(u)\ge1/2\)（\(u\ge1\)）。置 \(X(u)=1/(12u^2)\)，则

\[
\frac1{D(u)}-(1-X(u))
=\frac{X(u)^2+(X(u)-1)E(u)}{D(u)}.
\]

因此得到可控的 **相邻逆尾** 估计

\[
\left|\left(\frac1{T(u+1)}-\frac1{T(u)}\right)
-1+\frac1{12u^2}\right|
\le\frac{701}{1800}u^{-4}\quad(u\ge1).
\tag{SR10}
\]

其中逆尾差恰为 \(1/D(u)\)。使用精确相邻恒等式避免把两个独立 \(O(u^{-3})\) 余项作差并丢掉更强的控制。

<a id="gsr-proof"></a>
## 3. 完整轨道、非共振发散与共振有限长

由 SR2 有 \(\rho_k-\rho_{k+1}=\ell_2(y_k)=h^{-2}u_k^{-2}\)。C214 的完整核 resolvent

\[
J_{G_2}(p_1,p_2,r)=(p_1+\ell_2(|r|),p_2,|r|/4)
\]

遂给 \(w_{k+1}=J_{G_2}w_k\)。双射 \(v_c\) 给物理完整纤维共轭，故没有删支或选择不完整纤维。\(\rho_k\to0\)、\(y_k\to0\) 给物理点趋零。

记切向步 \(s_k=|g_c(-\rho_{k+1})-g_c(-\rho_k)|\) 与相邻角差

\[
\Delta\theta_k=c(\rho_{k+1}^{-1}-\rho_k^{-1}).
\]

SR10 直接给

\[
\Delta\theta_k=L\left(1-\frac1{12u_k^2}+\varepsilon_k\right),
\qquad |\varepsilon_k|\le\frac{701}{1800}u_k^{-4}.
\tag{SR11}
\]

两点弦长恒等式为

\[
s_k^2=h^{-4}u_k^{-4}
+4\rho_k\rho_{k+1}\sin^2(\Delta\theta_k/2).
\tag{SR12}
\]

若 \(L\notin2\pi\mathbb Z\)，SR11 给 \(|\sin(\Delta\theta_k/2)|\to|\sin(L/2)|>0\)；积分比较给 \(\rho_k\sim h^{-2}u_k^{-1}\)。径向平方项阶更小，故得 SR5 的切向版本。正常步 \(3y_k/4\) 为几何小量，不改变等价式。因此调和比较给无限物理长度。

若 \(L\in2\pi\mathbb Z\)，SR11 给

\[
|\Delta\theta_k-L|\le\frac{|L|}{2u_k^2}\quad(u_k\ge1),
\tag{SR13}
\]

因为 \(1/12+701/1800=851/1800<1/2\)。于是角弦相对于径向步的比值趋零，SR12 得 \(s_k\sim h^{-2}u_k^{-2}\)，正常几何步仍阶更小，证明 SR6。

也有可直接用于留域的显式实际步上界。由 \(\rho_k\le h^{-2}(u_k^{-1}+u_k^{-2})\le2h^{-2}u_k^{-1}\) 及 \(|\sin(t/2)|\le|t|/2\)，SR12 和 SR13 给

\[
\|x_{k+1}-x_k\|\le h^{-2}u_k^{-2}+|c|u_k^{-3}+\tfrac34y_k.
\tag{SR14}
\]

从任意 \(K\ge0\) 的剩余物理总长度因而满足

\[
\sum_{k=K}^{\infty}\|x_{k+1}-x_k\|
\le h^{-2}(u_K^{-1}+u_K^{-2})
+|c|(\tfrac12u_K^{-2}+u_K^{-3})+y_K.
\tag{SR15}
\]

这是一条实际变换步界；共振时即使半阶逆的统一复合 Dini 包络发散，此轨道仍有限长。因而它与 C210“充分包络、不是个别轨道必要条件”的范围完全一致。

## 4. 接收、计算与先行性边界

[标准库 Decimal 复算](../code/gppa_novelty/spiral_resonance_check.py) 在 90 位精度下使用精确 Bernoulli 系数和带解析截断界的 Euler–Maclaurin 尾；结果存于 [JSON](../code/gppa_novelty/spiral_resonance_check.json)。计算核对相邻恒等式、SR8–10 的余项、非共振调和常数及共振平方常数，不承担无穷级数判据的证明。

本页只分类 SR2–3 的指定临界轨道。它不宣称任意逆 Hölder GPPA、任意 twist 功率或任意物理初值都有同一必要门。C214 中 \(a=2,c=\pi/h^2\) 的无限长结论原样成立；SR4 恰解释为何 \(c\) 的校准不可省略。几何螺旋参数化、半阶指数和通用模求和已有先行接口，精确 GPPA 编码与本页离散共振细化的全球优先性继续开放。
