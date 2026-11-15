# C303 HJ source audit: cutoff support and vector-field identity

日期：2026-11-15
状态：**source-conditional / continue validation**

本页把 Horsin–Jendoubi 的一手构造与 C303 所需的 cutoff-free 尾管逐项对齐。网页 PDF 的可复核位置是 §2.1 的 (5)–(8)、全局 \(C^\infty\) 延拓段，以及 §2.2 的 (9)–(12)。

## 1. Paper Facts

1. 原文取

   \[
   1<\gamma_2(\theta+2\pi)<\gamma_1(\theta)<\gamma_2(\theta),
   \qquad \gamma_i(\theta)\to1,
   \]
   并在具体选择中使用
   \(\gamma_1(\theta)=1+e^{-\theta}\)、
   \(\gamma_2(\theta)=1+\mu e^{-\theta}\)。非重叠条件在 \(\theta=0\) 给出
   \(1<\mu<e^{2\pi}\)。

2. 原文规定 \(\theta_{\rm supp}\in(0,2\pi)\)，并要求 cutoff 的 support 连通、包含
   \(\gamma_1(0),\gamma_2(0)\) 作为内点，且对
   \(\theta>\theta_{\rm supp}\) 两条曲线不在该 support 内。

3. 原文公式 (8) 是
   \[
   f(x,y)=e^{-(\theta+2p\pi)^2}\,\phi(x,y)\,[1-\Pi(x,y)],
   \]
   随后声称由平坦端点和该构造得到 \(f\in C^\infty(\mathbb R^2)\)。

4. §2.2 的显式向量公式有径向主项
   \[
   -\frac{2h(\theta)}{\gamma_2(\theta)-\gamma_1(\theta)}
      F'(a(r,\theta))e_r,
   \]
   并证明大角度时
   \(X(b_1(\theta),\theta)\cdot n_1(\theta)<0\)、
   \(X(b_2(\theta),\theta)\cdot n_2(\theta)>0\)。

## 2. 文字身份与显式公式的不一致

原文在定义处写作 \(X:=\nabla f\)，但把 \(q=(2r-\gamma_1-\gamma_2)/(\gamma_2-\gamma_1)\) 代入后，
\[
\partial_r f=+\frac{2h}{\gamma_2-\gamma_1}F'(q),
\]
而原文随后显示的径向项是负号。因此 §2.2 的显式 \(X\) 与
\[
Y:=-\nabla f
\]
一致，而与“\(X=\nabla f\)”的字面身份不一致。

这一点不是可以静默忽略的排版差异：令
\[
s_1=r-b_1(\theta),\qquad s_2=b_2(\theta)-r,
\]
则在相应边界上（按极坐标切向因子）
\[
n_1=-b_1\nabla s_1,\qquad n_2=b_2\nabla s_2.
\]
于是原文的符号
\[
X\cdot n_1<0,\qquad X\cdot n_2>0
\]
只有在把显式 \(X\) 解释成 \(Y=-\nabla f\) 时，才等价于 C303 所需的
\[
\nabla s_i\cdot Y>0
\]
的两侧内向条件。

## 3. Cutoff 的可复核修补

`research/c303_hj_cutoff_construction.md` 已把原先过强的“任意外环 dumbbell”修补为 source-compatible 候选：

- 取 \(\theta_{\rm supp}=2\pi-\delta\)；
- 利用 \(\mu<e^{2\pi}\) 选
  \(\sup_{[2\pi-\delta,2\pi]}\gamma_2<R<2\)；
- 在 \(r>R\) 的窄正实轴角锥内取连接两初始点的紧连通 \(C^\infty\) dumbbell；
- 对 \(\theta_{\rm supp}<\theta<2\pi\)，曲线半径小于 \(R\)；对 \(\theta\ge2\pi\)，
  \(\gamma_2(\theta)\le\gamma_2(2\pi)<R\)；
- 再取 \(\theta_{\rm tail}\) 足够大，使整个闭 normalized outer strip 落在
  \(r<1+\eta_0/2\)，因而 cutoff 在该闭条带恒为零。

这修补解决了原先没有满足 \(\theta_{\rm supp}\in(0,2\pi)\) 的真实缺口，并保留 cutoff-free 尾部的边界符号。

## 4. 尚未闭合的 source obligations

1. 逐字确认原文对 \(\Pi\) 是否还隐含 \(C^\infty\)、值域或“在初始区域取 1”等条件；本页显式构造满足这些常见要求，但不能用“未搜索到”替代原文核对。
2. 在 C303 的定义中固定记号：\(F=\nabla\chi_a\)，而 HJ 的尾速度场应取显式公式对应的 \(Y=-\nabla f\)。所有 normal recursion、boundary sign 和 resolvent identity 必须使用同一身份。
3. 逐项重算 cutoff-free 尾管的 \(F=\nabla\chi_a\) 与 \(Y=-\nabla f\) 常数；不能因为 source 的“\(X:=\nabla f\)”文字 typo 就直接把符号导入惯性 PPA 桥。
4. 证明物理投影在闭 lifted tail 上的 lift/injectivity，并将
   \(\theta_{\rm supp}\)、\(\theta_{\rm tail}\)、finite-prefix 的 \(\theta_*\) 分开取值。

因此，source audit 改变了判断的精确内容：cutoff 的几何修补现在有可行构造，但 HJ 的向量场身份必须按显式公式统一，C303 仍是 conditional candidate，不能升级为无条件定理或主要贡献。
