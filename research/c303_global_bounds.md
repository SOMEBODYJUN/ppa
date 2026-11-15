# C303：HJ 全局导数与完整 resolvent 覆盖引理

状态：`derived-checked`（针对下列明确的 HJ 构造和参数约定）。本引理只关闭全局覆盖门，不关闭变量步惯性轨道的留域、角度发散或主要贡献裁决。

## 1. HJ 支撑的固定紧环带

HJ 对物理点 \(M=(r\cos\theta,r\sin\theta)\) 只在存在 \(p\ge0\) 使
\[
\gamma_1(\theta+2p\pi)\le r\le\gamma_2(\theta+2p\pi)
\]
时定义 \(\phi(M)\)，否则令 \(\phi(M)=0\)。对
\[
\gamma_1(t)=1+e^{-t},
\qquad
\gamma_2(t)=1+\mu e^{-t},
\qquad t\ge0,
\]
有 \(1<\gamma_1(t)\le2\)、\(1<\gamma_2(t)\le1+\mu\)。因此
\[
\operatorname{supp}\phi\subseteq\{x\in\mathbb R^2:1\le |x|\le1+\mu\}.
\tag{GB1}
\]
乘以任意 cutoff 因子 \(1-\Pi\) 不会扩大这个支撑。HJ 的构造把 \(f\) 在单位圆内定义为零，并在环带边界用平坦 bump \(F\) 连接；其 §2.1 的逐阶论证给出 \(f\in C^\infty(\mathbb R^2)\)。所以 \(f\) 及其各阶导数在固定紧集上有界，且在环带外为零：存在有限常数
\[
G=\sup_x\|\nabla f(x)\|,
\quad
M_2=\sup_x\|\nabla^2 f(x)\|,
\quad
M_3=\sup_x\|D^3 f(x)\|.
\tag{GB2}
\]
这里使用的是 HJ 的完整物理构造；只给管内局部公式而不验证全局延拓，不能调用 (GB2)。

## 2. \(\nabla\chi_a\) 的全局 Lipschitz 界

令
\[
\chi_a=a f-\tfrac12\|\nabla f\|^2,
\qquad
\nabla\chi_a=a g-Hg,
\quad g=\nabla f,\ H=\nabla^2 f.
\]
对方向 \(\xi\)，
\[
D(\nabla\chi_a)[\xi]
 =aH\xi-D^3f[\xi,\cdot]g-H^2\xi.
\]
由 (GB2) 得
\[
L_\chi:=aM_2+M_3G+M_2^2<\infty,
\qquad
\|\nabla\chi_a(u)-\nabla\chi_a(v)\|\le L_\chi\|u-v\|.
\tag{GB3}
\]

## 3. 每个小 resolvent 步的完整覆盖和唯一性

若 \(0<\lambda<1/L_\chi\)，则
\[
\langle u-v,(u+\lambda\nabla\chi_a(u))-(v+\lambda\nabla\chi_a(v))\rangle
\ge(1-\lambda L_\chi)\|u-v\|^2.
\tag{GB4}
\]
故 \(G_\lambda=I+\lambda\nabla\chi_a\) 强单调、连续且 coercive；有限维强单调连续映射的标准满射结论给出 \(G_\lambda(\mathbb R^2)=\mathbb R^2\)，并由强单调性给出单射。于是
\[
J_{\lambda\nabla\chi_a}=G_\lambda^{-1}
\]
是全域单值映射。对变量步 \(\lambda_k=h_k^2/(1+ah_k)\)，取 \(h_0\) 足够小即有 \(\lambda_k<1/L_\chi\) 对所有 \(k\)，所以惯性更新
\[
y_k=J_{\lambda_k\nabla\chi_a}(x_k+\beta_kv_k)
\]
具有完整输入覆盖；不存在未声明的局部根选择。

## 4. 范围边界

(GB1)--(GB4) 只处理完整图、全输入覆盖和统一导数常数。它们不证明：

1. \(y_k\) 和连续 \(\tau\)-resolvent 路径留在 HJ 尾管；
2. \(w_k=O(h_k)\) 及 \(\sup_\tau\|w_\tau\|=O(h_k)\) 的 uniform Taylor 估计；
3. 同一开相空间初集的有限前缀留域；
4. \(\omega(x_k)=S^1\) 的离散角度发散。

这些门仍由 [C303 v3/v4 桥](c303_discrete_bridge_v3.md)分别承担。

**来源**：Horsin--Jendoubi, *Non-genericity of initial data with punctual \(\omega\)-limit set*, Archiv der Mathematik 114 (2020), DOI [10.1007/s00013-019-01377-8](https://doi.org/10.1007/s00013-019-01377-8)，构造式 (5)--(8) 及 \(C^\infty\) 延拓论证。
