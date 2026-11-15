# 二阶阻尼梯度系统的开盆域圆形非收敛：证明稿 v1

状态：candidate。本稿把 Horsin--Jendoubi 螺旋管的渐近估计和二阶首次离开 bootstrap 写成可逐项复核的证明。独立审查、外部优先性和期刊价值仍未完成；在此之前不把它升级为 derived-checked 或主要贡献。

## 1. 精确命题

设 \(f:\mathbb R^2\to\mathbb R\) 是 Horsin--Jendoubi 构造的 \(C^\infty\) 势。取其大角度螺旋管的一个物理分支，用连续提升角 \(\vartheta\) 写成
\[
D=\{(r,\vartheta):\vartheta>\vartheta_*,\ b_1(\vartheta)<r<b_2(\vartheta)\},
\]
其中
\[
\gamma _1(\vartheta)=1+e^{-\vartheta},\qquad
\gamma _2(\vartheta)=1+\mu e^{-\vartheta},\quad \mu>1,
\]
\(\Delta=\gamma _2-\gamma _1=(\mu-1)e^{-\vartheta}\)，并且 HJ 的两条内管边界满足
\[
b_i(\vartheta)=1+c_i e^{-\vartheta},\qquad 0<c_1<c_2.
\]
HJ 的 \(\Pi\) 是构造中的自由 cutoff。取它为紧支撑、支撑位于某个有限初始环带，
并增大 \(\vartheta_*\) 使
\(\operatorname{supp}\Pi\) 与闭管
\(\{b_1(\vartheta)\le r\le b_2(\vartheta):\vartheta\ge\vartheta_*\}\)
不相交；这是因为该闭管趋于 \(S^1\)，而 cutoff 可放置在 \(r\ge1+\eta\)
的有限区域。于是该管上 HJ 的 cutoff 恒等于一。令
\[
\chi_a(x)=a f(x)-\tfrac12\lVert\nabla f(x)\rVert^2,\qquad a>0.
\]
候选命题是：存在 \(a>0\) 和相空间非空开集 \(\mathcal U\subset\mathbb R^2\times\mathbb R^2\)，使每个
\[
x''+a x'+\nabla\chi_a(x)=0,\qquad (x(0),x'(0))\in\mathcal U
\]
的轨道全局存在、有界，并且 \(\omega(x)=S^1\)，所以 \(x(t)\) 不收敛。

## 2. HJ 管内估计

在 cutoff 为一的区域写
\[
q(r,\vartheta)=\frac{2r-\gamma _1(\vartheta)-\gamma _2(\vartheta)}{\Delta(\vartheta)},\qquad
f(r,\vartheta)=h(\vartheta)F(q(r,\vartheta)),\qquad h(\vartheta)=e^{-\vartheta^2}.
\]
HJ 选定的窄管使 \(q\in[-\beta,\beta]\Subset(-1,1)\)。因此
\[
F_*:=\min_{[-\beta,\beta]}F>0,\qquad
F^*:=\max_{[-\beta,\beta]}F<\infty,\qquad
G^*:=\max_{[-\beta,\beta]}|F'|<\infty.
\tag{2.1}
\]
由 \(\Delta'=-\Delta\)、\(\gamma_i'=O(e^{-\vartheta})\) 得
\[
q_r=2/\Delta=O(e^\vartheta),\qquad
q_\vartheta=q+\frac{-\gamma_1'-\gamma_2'}{\Delta}=O(1),\qquad
q_{\vartheta\vartheta}=O(1).
\tag{2.2}
\]
令 \(Y=-\nabla f\)。则
\[
Y_\vartheta=\frac{h}{r}\{2\vartheta F(q)-F'(q)q_\vartheta\}.
\]
增大 \(\vartheta_*\) 后，第一项统一主导第二项，故存在 \(0<c_0<C_0\) 使
\[
c_0\vartheta e^{-\vartheta^2}\le Y_\vartheta(r,\vartheta)
\le C_0\vartheta e^{-\vartheta^2}.
\tag{HJ-1}
\]

HJ 的边界 \(b_1,b_2\) 对应 \(q=-\beta,+\beta\)，且 \(F'(-\beta)<0<F'(\beta)\)。于是
\[
Y_r(b_1,\vartheta)=2h|F'(-\beta)|/\Delta,\qquad
Y_r(b_2,\vartheta)=-2h|F'(\beta)|/\Delta.
\]
令 \(s_1=r-b_1(\vartheta)\)、\(s_2=b_2(\vartheta)-r\)。在极坐标度量下
\[
\nabla s_1=e_r-\frac{b_1'}r e_\vartheta,\qquad
\nabla s_2=-e_r+\frac{b_2'}r e_\vartheta,
\]
而 \(b_i'=O(e^{-\vartheta})\)。利用 \(Y_\vartheta=O(\vartheta h)\) 和 \(\Delta\asymp e^{-\vartheta}\)，可取 \(m_0>0,L_s<\infty\) 使
\[
\nabla s_i\cdot Y\ge m_0 e^{-\vartheta^2+\vartheta}
\quad(s_i=0),\qquad
|\nabla s_i|\le L_s.
\tag{HJ-2}
\]

再由 (2.2)
\[
f_{rr}=O(e^{-\vartheta^2+2\vartheta}),\quad
f_{r\vartheta}=O(\vartheta e^{-\vartheta^2+\vartheta}),\quad
f_{\vartheta\vartheta}=O(\vartheta^2e^{-\vartheta^2}).
\tag{2.3}
\]
笛卡尔坐标变换只引入有界的 \(r^{-1},r^{-2}\) 因子。HJ 已证明 \(f\in C^\infty(\mathbb R^2)\)，物理闭管加极限圆是紧集，故
\[
K:=\sup_{x\in\overline D}\lambda_{\max}(\nabla^2f(x))<\infty.
\tag{2.4}
\]

## 3. 二阶系统的精确分解

取 \(a>K\)，令 \(\delta=a-K>0\)。对任意解设 \(v=x'\)、\(w=v+\nabla f(x)\)。直接代入
\[
\chi_a=a f-\tfrac12|\nabla f|^2
\]
得到
\[
x'=Y(x)+w,\qquad
w'=(\nabla^2 f(x)-aI)w.
\tag{3.1}
\]
只要 \(x(t)\in D\)，
\[
|w(t)|\le e^{-\delta t}|w(0)|.
\tag{3.2}
\]

## 4. 首次离开 bootstrap

选有限初始角带 \(\vartheta_*<\Theta_0<\Theta_1<\infty\)，并取闭子带 \(D_0\Subset D\)，使其到两边界有正距离。令
\[
\mathcal U=\{(x_0,v_0):x_0\in D_0,\ |v_0+\nabla f(x_0)|<\varepsilon\}.
\]
这是四维相空间中的非空开集。

设 \(\tau\) 是首次离开 \(D\) 的时刻。在 \(t<\tau\) 上 (3.2) 给出
\[
\vartheta(t)\ge\vartheta(0)-W(t)
\ge\Theta_0-C_1\varepsilon/\delta
>\Theta_0/2.
\tag{4.1}
\]
取 \(\Theta_0>4\)，并把 \(\varepsilon\) 取得足够小，使
\(C_1\varepsilon/\delta<\Theta_0/4\)。为吸收极坐标投影中 \(r^{-1}\) 的有界因子，
以下把扰动项统一记成 \(C_1|w|\)。令
\[
W(t)=C_1\int_0^t|w(s)|ds,\qquad u(t)=\vartheta(t)-W(t).
\]
则 \(W(t)\le C_1\varepsilon/\delta\)，且
\(u(t)=\vartheta(t)-W(t)>\Theta_0/2-C_1\varepsilon/\delta>1\)。
在任意首次接触上界的时刻，(HJ-1) 和
\(s\mapsto s e^{-s^2}\) 在 \(s\ge1\) 上递减给出
\[
u'\le C_0u e^{-u^2}.
\]
所以
\[
\frac d{dt}e^{u^2/2}
 =u e^{u^2/2}u'
\le C_0u^2e^{-u^2/2}
\le 2C_0/e.
\]
从而在 \([0,\tau)\) 上
\[
\vartheta(t)\le W(t)+\sqrt{C_*+2\log(1+t)}.
\tag{4.2}
\]
这是首次接触比较，只在假设轨道尚未离开 \(D\) 的区间内使用
(HJ-1)--(3.2)，没有循环假设不变性。结合 (4.1)--(4.2)，可取有限
\(p>1,c_1>0\) 使
\[
\vartheta(t)e^{-\vartheta(t)^2}\ge c_1(1+t)^{-p}.
\tag{4.3}
\]

由 (HJ-2)、(4.2) 得
\[
m(\vartheta(t)):=m_0e^{-\vartheta(t)^2+\vartheta(t)}
\ge c_*(1+t)^{-p}.
\tag{4.4}
\]
取 \(M_p=\sup_{t\ge0}e^{-\delta t}(1+t)^p\)，并令
\[
\varepsilon<\frac{c_*}{2L_sM_p}.
\tag{4.5}
\]
同时把 \(\varepsilon\) 取得更小，使
\[
C_1\varepsilon e^{-\delta t}
\le \tfrac12c_0\vartheta(t)e^{-\vartheta(t)^2}
\quad(t<\tau).
\tag{4.6}
\]
这由 (4.3) 和 \(\sup_{t\ge0}e^{-\delta t}(1+t)^p<\infty\) 保证。
因此 \(\vartheta'(t)>0\) 直到首次离开；特别是角坐标不会向下跌出所选 HJ 分支。
若 \(s_i\) 在 \(\tau\) 首次变成零，则
\[
s_i'(\tau)=\nabla s_i\cdot(Y+w)
\ge c_*(1+\tau)^{-p}-L_s\varepsilon e^{-\delta\tau}>0,
\]
与首次接触必须 \(s_i'(\tau)\le0\) 矛盾。因此 \(\tau=\infty\)，轨道永远留在 \(D\) 内。

## 5. 角度发散与 omega-limit

由 (4.6)，在整个轨道上
\[
\vartheta'(t)\ge \tfrac12c_0\vartheta(t)e^{-\vartheta(t)^2}>0.
\tag{5.1}
\]
若 \(\vartheta\) 有限上界，右端在该紧区间有正下界，矛盾；所以 \(\vartheta(t)\to+\infty\)。由 \(b_i(\vartheta)=1+O(e^{-\vartheta})\) 得 \(r(t)\to1\)。连续提升角趋于 \(+\infty\)，其模 \(2\pi\) 的投影访问每个相位，于是
\[
\omega(x)=S^1.
\]
物理轨道留在有界闭管，且 \(w\) 和 \(Y\) 有界，所以 \(v=x'=Y+w\) 有界；全局 \(C^\infty\) 向量场因此保证不存在有限时间爆炸。

## 6. 尚未关闭的验收门

1. 逐项核对 HJ 原文的 \(q,b_i,F'\) 符号；HJ 以 \(\nabla f\) 写边界式，本稿统一用 \(Y=-\nabla f\)。
2. 独立审查者需重构 (2.1)--(5.1)，特别是 \(q_\vartheta=O(1)\)、极坐标 Hessian 转换、有限初始角带和首次接触量词。
3. 外部优先性目前只核到 HJ Remark 3 的 open-problem 事实；近期一手全文仍需单独审计。
4. 这是二阶 ODE 结果，不自动给 PPA/GPPA 离散桥；若要成为 PPA 主贡献，还需建立与现有 RLEB/GPPA 对象的实质联系。
