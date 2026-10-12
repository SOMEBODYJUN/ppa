# RP² 的显式保零完成与精确原管预算

本页固定 [C234 的完整模型](zero_preserving_completion.md#zpc-rp2)，关闭此前“实际方向延拓仍未知”的构造门，并计算原管数据的精确半范数。最小完成预算与端点达到性仍开放。[独立审查](../audit/RP2_EXPLICIT_COMPLETION_REVIEW_2026_10_12.md)与[有限复算](../code/rp2_explicit_completion/README.md)分别记录证明攻击和计算范围。

<a id="rec-object"></a>
## 共同对象

在 \(H=\operatorname{Sym}_0(3)\cong\mathbb R^5\) 使用 Frobenius 内积，设
\[
M=\{qq^\top-I/3:q\in S^2\},\qquad N_r=\{p:d(p,M)\le r\}.
\]
C234 已证明 \(\operatorname{reach}(M)\ge1/2\)，故 \(N_{1/4}\) 有唯一光滑投影 \(\Pi\)。令 \(s=d(p,M),m=\Pi(p)\)。指定整个 \(N_\rho,\rho=1/8\) 上
\[
T_0(p)=m+s^2(p-m),\qquad C_0(p)=m+(2s^2-1)(p-m). \tag{EC1}
\]
完成必须保留所有这些输入及其完整输出。任意固定 \(\lambda>0\) 时，全域完成对应完整关系
\[
\widehat T=(\operatorname{Id}+\widehat C)/2,\qquad
\operatorname{gph}\widehat F
=\{(\widehat T(p),(p-\widehat T(p))/\lambda):p\in H\}. \tag{EC2}
\]
因此完整 \(J_{\lambda\widehat F}=\widehat T\)，零集是 \(\operatorname{Fix}\widehat T\)。不要求 \(\widehat F\) 单值。

[C245](lipschitz_obstruction_budget.md#lob-object)需要实际方向场与 \(K_e\)，[C258](simplicial_sphere_budget_certificate.md#ssc-object)提供一般有限单纯形接口。本页直接给 RP² 的物理坐标公式，无需先剖分整个五维外域；C258 的一般用途保留。

<a id="rec-geometry"></a>
## 支持恒等式：法向弦与旋转交换子

固定 \(q_0=e_1,m_0=q_0q_0^\top-I/3\) 及单位角速度旋转生成元
\[
J=\begin{pmatrix}0&0&0\\0&0&-1\\0&1&0\end{pmatrix},
\qquad w(m)=Jm-mJ. \tag{EC3}
\]
对 \(m=qq^\top-I/3\)，设 \(u=1-(q\cdot q_0)^2,c=m-m_0\)。有
\[
\|c\|^2=\|w(m)\|^2=2u,\quad w\perp c,\quad w\perp N_mM,
\quad \|c_N\|^2=2u^2,\quad \|c_T\|^2=2u(1-u). \tag{EC4}
\]
证明：切空间是 \(qh^\top+hq^\top,h\perp q\)，而 \(w=(Jq)q^\top+q(Jq)^\top\) 属于其中；\(\|Jq\|^2=u\) 给范数。迹的循环性与 \([J,m_0]=0\) 给 \(w\perp c\)。写 \(q_0=a q+z,z\perp q,\|z\|^2=u\)，切向弦是 \(-a(qz^\top+zq^\top)\)，得到两分量范数。全部公式在 \(q\mapsto-q\) 下不变。

同样，对任意 \(m,m'\in M,n\in N_mM\)，
\[
|\langle n,m-m'\rangle|
\le\frac{\|n\|}{\sqrt2}\|m-m'\|^2. \tag{EC5}
\]
对 \(p=m+n,p'=m'+n'\in N_r,r\le1/4\)，其中 \(m=\Pi(p),m'=\Pi(p')\)，
\[
\langle p-p',m-m'\rangle\ge(1-\sqrt2r)\|m-m'\|^2,
\qquad \operatorname{Lip}(\Pi;N_r)\le\frac1{1-\sqrt2r}\le2. \tag{EC6}
\]
这是管上任意点对的欧氏界，不要求连接线段留在管内。

<a id="rec-construction"></a>
## C264-v1：显式全域完成及认证预算

在 \(\rho\le s\le1/4\) 定义
\[
\nu=(p-\Pi p)/s,\quad t=8(s-\rho),\quad
V(p)=(1-t)\nu+t(p-m_0)+t(1-t)w(\Pi p). \tag{EC7}
\]
设 \(N(z)=z/\|z\|\)，外球接缝用 \(\chi(p)=2(\|p\|-3/2)\)。在 \(W=\overline B_2\setminus\operatorname{int}N_\rho\) 取
\[
e(p)=\begin{cases}
N(V(p)),&\rho\le s\le1/4,\\
N(p-m_0),&s\ge1/4,\ \|p\|\le3/2,\\
N(p-(1-\chi(p))m_0),&3/2\le\|p\|\le2.
\end{cases} \tag{EC8}
\]
两 collar 不交，因为管上 \(\|p\|\le\sqrt{2/3}+1/4<5/4<3/2\)。公共边界公式一致。幅度与完成定义为
\[
a(p)=\frac{63}{512}+\frac{449}{512}
\operatorname{clip}\!\left(\frac{\|p\|-5/4}{3/4},0,1\right), \tag{EC9}
\]
\[
\widehat C(p)=\begin{cases}
C_0(p),&p\in N_\rho,\\
p-2a(p)e(p),&p\in W,\\
0,&\|p\|\ge2.
\end{cases} \tag{EC10}
\]
clip 截断到 \([0,1]\)。这是全域紧支撑保零完成，并满足
\[
\operatorname{Fix}\widehat T=M,\quad
\operatorname{Lip}(e;W)\le188,\quad
\operatorname{Lip}(\widehat C;H)\le\frac{3025}{64},\quad
[\widehat C]_\gamma\le4^{1-\gamma}\frac{3025}{64}\quad(0<\gamma<1). \tag{EC11}
\]
特别地半阶预算不超过 \(3025/32\)。这是认证上界，未声称它是实际半范数或最小完成预算。

### 原始向量的严格余量

EC4 给出，令 \(b=1-t+st\)，
\[
\begin{aligned}
\|V\|^2&\ge(b-\sqrt2tu)^2+2t^2u(1-u)+2t^2(1-t)^2u\\
&=b^2+u\{2t^2[1+(1-t)^2]-2\sqrt2bt\}.
\end{aligned} \tag{EC12}
\]
右侧关于 \(u\in[0,1]\) 仿射，只须核两个端点。\(u=0\) 时实际耦合 \(s=1/8+t/8\) 给 \(b=1-7t/8+t^2/8\ge1/4\)。\(u=1\) 时右侧为 \((b-\sqrt2t)^2+2t^2(1-t)^2\)。当 \(t\le1/4\)，第一项平方根至少 \(13/32\)；当 \(t\ge3/4\)，至少 \(5/16\)；中间区间第二项平方根至少 \(3\sqrt2/16>1/4\)。所以
\[
\|V(p)\|\ge1/4. \tag{EC13}
\]
在 \(m=m_0,s=1/4\) 达到。EC8 另外两段分别有原始向量余量 \(1/4\) 与 \(3/2-\sqrt{2/3}>2/3\)，不归一化零向量。

### 全对常数

对范数至少 \(\mu\) 的非零向量，
\[
\|N(z)-N(z')\|\le\|z-z'\|/\mu, \tag{EC14}
\]
因为 \(\|z-z'\|^2=(\|z\|-\|z'\|)^2+\|z\|\|z'\|\|N(z)-N(z')\|^2\)。
EC6 给 annulus 上 \(K_\nu\le24,K_w\le4,K_t\le8\)。先将 t 作为独立变量：固定 t 的空间界是
\((1-t)24+t+4t(1-t)\le24\)；时间差分系数是
\(c+(s-1)\nu+(1-t-t')w\)，其范数至多 \(7/8+2=23/8\)，因为 \(w\perp c,\nu\) 且 \(\|c\|=\|w\|\le\sqrt2\)。因此实际耦合后 \(K_V\le24+8(23/8)=47\)，EC13/14 给内 collar \(K_e\le188\)。中段 \(K_e\le4\)；外段原始常数 \(1+2\|m_0\|<8/3\)，余量 \(>2/3\)，同样 \(K_e\le4\)。

<a id="rec-gluing"></a>
### 有限闭覆盖粘接引理

凸域若由有限闭集 \(E_i\) 覆盖，各限制映射是全对欧氏 \(K_i\)-Lipschitz，并在交集上取一致迹，则全域常数至多 \(\max_iK_i\)。不要求闭块凸或块内路径常数。

证明：将连接两点的线段拉回 \([0,1]\)，各原像是有限闭覆盖 \(A_i\)。从当前时间选一个包含它、且最后接触严格更晚的块，跳到这个块的最后接触时间。若当前时间小于1，取右邻时间序列，有限鸽巢与闭性保证有一个当前块的最后接触严格更晚。每用一个块就到达其最大时间，此后它不再贡献非零跳跃；故至多块数次到1。每次跳跃两端在同一块，用该块全对界；长度总和恰为整条线段长度。证毕。

“全对欧氏”不能替换成仅局部导数或内在路径界。此引理允许 C245 的原欧氏合同取 \(G_W=1\)，但不删除 C258 从单纯形导数得到欧氏界时的 \(G_{\mathcal T}\)。

为对方向 e 使用此引理，在原管辅助定义向量 \((p-\Pi p)/\rho\)（常数至多24，不要求单位值），球外辅助定义 \(p/\|p\|\)（常数至多1/2）。迹与 EC8 一致；全空间粘接再限制到 W，得到方向常数188。

### 精确迹、无零与预算

内边界 \(s=\rho\) 时 \(e=\nu,a=63/512=(1-\rho^2)\rho\)，所以 EC10 恰为 EC1。\(s=1/4\) 时 \(e=N(p-m_0)\)；\(\|p\|=3/2\) 时 \(\chi=0\)；\(\|p\|=2\) 时 \(e=p/2,a=1\)，所以 \(\widehat C=0\)。全部接缝精确一致。

原管外球内的位移 \(p-\widehat T(p)=a(p)e(p)\) 范数至少 \(63/512\)，球外位移为 \(p/2\)；管内 EC1 只固定 M，因此没有新增完整零点。

幅度 \(K_a\le449/384,a\le1\)，内 collar 上恒为 \(63/512\)，故其 Cayley 常数至多
\[
1+2(63/512)188=3025/64. \tag{EC15}
\]
中段和外段各至多 \(1+2(449/384+4)<12\)。原管上 \(D_0=(1-s^2)(p-\Pi p)\)；径向函数 h(z)=(1−||z||²)z 在半径rho的凸球上导数范数至多1；结合 EC6 给 \(K_{D_0}\le3(1+\rho^2)=195/64\)，所以 \(K_{C_0}\le227/32\)（C265 另给精确更小值）。球外为零。五块闭覆盖
\(N_\rho,\{\rho\le s\le1/4\},\{s\ge1/4,\|p\|\le3/2\},\{3/2\le\|p\|\le2\},\{\|p\|\ge2\}\)
覆盖 H，粘接引理给全域 Lipschitz 界。

设该界为 K。球内两点距离 \(d\le4\)，差至多 \(K4^{1-\gamma}d^\gamma\)。一端球外、\(d\le4\) 时同样；若 \(d>4\)，球内端到球边界至多2，差至多 \(2K\le K4^{1-\gamma}d^\gamma\)；两端球外差为零。得全尺度 Hölder 界。

EC2 保留 C234 的整个局部唯一近端动力、三次距离与真实全纤维残差；管外前像不能降低残差仍由 C234 的 Z11 排除。C235 的全域吸引障碍仍成立。

<a id="rec-exact-budget"></a>
## C265-v1：原管数据的精确全对半范数

对每个 \(0<\rho\le1/8,0<\gamma\le1\)，在同一个 M 的整个 \(N_\rho\) 按 EC1 定义 \(C_0\)，则
\[
\boxed{[C_0]_{\gamma,N_\rho}
=\frac{\sqrt2+2\rho(1-2\rho^2)}{(\sqrt2-2\rho)^\gamma}.} \tag{EC16}
\]
半范数只取不同输入。端点 \(\gamma=1\) 是精确 Lipschitz 常数，不扩大次线性全域理论到该端点。

### 全对上界

写 \(p=m+u,q=n+v,r=\|u\|,s=\|v\|\le\rho\)，u,v 是各自法向。设
\[
c=m-n,\ A=\|c\|^2\le2,\ B=\|u-v\|^2,\ z=r+s,\ t=z/\sqrt2,\ k=1-t^2,
\quad \beta=(1-2r^2)u-(1-2s^2)v.
\]
输入差 \(c+u-v\)，输出差 \(c-\beta\)。EC5 及 \(4(r^3+s^3)\ge(r+s)^3\) 给
\[
\langle c,u-v\rangle\ge-tA,\quad
\langle c,\beta\rangle\ge-ktA,\quad B\le2t^2. \tag{EC17}
\]
设 \(a_r=1-2r^2,a_s=1-2s^2,d=(r-s)^2\)，精确恒等式为
\[
\|\beta\|^2=a_ra_sB-2(r^2-s^2)^2[1-2(r^2+s^2)]\le k^2B,\quad
k^2-a_ra_s=d[1+z^2/2-d/4]\ge0. \tag{EC18}
\]
因此
\[
\|C_0p-C_0q\|^2\le(1+2kt)A+k^2B,\qquad
\|p-q\|^2\ge(1-2t)A+B. \tag{EC19}
\]
退化情形先独立处理：t=0 时差商平方为 \(A^{1-\gamma}\le2^{1-\gamma}\)；A=0、t>0、p≠q 时至多 \(k^2B^{1-\gamma}\le2^{1-\gamma}\)。p=q 不进入半范数上确界。

以下 A,t>0。若 \(B<t^2A\)，置 \(b=\sqrt{B/A}<t<1\)，三角不等式与 EC18 给差商平方至多
\[
A^{1-\gamma}\frac{(1+kb)^2}{(1-b)^{2\gamma}}
\le2^{1-\gamma}\frac{(1+kt)^2}{(1-t)^{2\gamma}}. \tag{EC20}
\]
只用了 A≤2 及关于 b 单调。

若 \(B\ge t^2A\)，记 \(\alpha=1+2kt,a=1-2t>0\)。EC19 给上界
\(F(A)=(\alpha A+k^2B)/(aA+B)^\gamma\)。固定 B 时
\[
F'(A)=\frac{(1-\gamma)\alpha aA+(\alpha-\gamma a k^2)B}{(aA+B)^{\gamma+1}}>0,
\]
因 B>0、t>0 给 \(\alpha>1\)。代 \(A\le B/t^2\le2\)，得到
\[
F(A)\le(B/t^2)^{1-\gamma}\frac{(1+kt)^2}{(1-t)^{2\gamma}}
\le2^{1-\gamma}\frac{(1+kt)^2}{(1-t)^{2\gamma}}. \tag{EC21}
\]
\(1+kt=1+t-t^3\) 在 \(0\le t\le\sqrt2/8<1/\sqrt3\) 增加，\((1-t)^{-\gamma}\) 也增加。代 \(t\le\sqrt2\rho\)，开平方整理，得 EC16 上界。

### 真实达等点对

取正交基点 \(m_1=e_1e_1^\top-I/3,m_2=e_2e_2^\top-I/3\)，
\[
\nu=(m_2-m_1)/\sqrt2,\qquad
p=m_1+\rho\nu,\quad q=m_2-\rho\nu. \tag{EC22}
\]
这两个向量确为各自基点法向。对任意 \(m'\in M\)，EC5 给
\[
\|p-m'\|^2\ge\rho^2+(1-\sqrt2\rho)\|m_1-m'\|^2,
\]
因此唯一最近点确为 m1；q 的最近点同理为 m2。输入距离 \(\sqrt2-2\rho\)，反射输出距离 \(\sqrt2+2\rho(1-2\rho^2)\)，真实达到 EC16。不是代数松弛里不可实现的极值。

<a id="rec-failure"></a>
## 直线同伦失败与预算解释的边界

内边界 \(p=m+\rho\nu\) 的原方向 \(g=\nu\)，平移方向 \(e_0=N(p-m_0)\)。完整反向集合是
\[
q\perp q_0,\quad m=qq^\top-I/3,\quad \nu=(m_0-m)/\sqrt2. \tag{EC23}
\]
它是一条 RP¹。若 e0=−ν，则非零弦 m−m0 是法向；EC4 的切向分量要求 u=1，u=0 弦为零且方向相同，排除。反向符号强制 EC23，逆向直接验证。因此归一化直线同伦在这整条圈的中点无定义。旋转项在该圈非零并垂直另外两项，是本构造的排零机制。

在宽度1/8的指定物理法向 collar 中，从 g 接到指定 e0，沿 EC23 的直线两端方向反向；球面曲线长至少 π，所以方向常数 \(K_e\ge8\pi\)。这是该 collar 的成本，不能推出最小 Hölder 预算严格缺口。单位方向与幅度的精确关系是
\[
\|ae-bf\|^2=(a-b)^2+ab\|e-f\|^2\qquad(\|e\|=\|f\|=1). \tag{EC24}
\]
本构造把小幅度63/512置于细旋转区，避免将外部最大幅度1乘到所有方向变化。

<a id="rec-frontier"></a>
## 精确前沿

固定原压力测试 \(\rho=1/8,\gamma=1/2\)。定义 \(L_*\) 为全域半阶 Hölder 完成 \(\widehat C\) 中 \([\widehat C]_{1/2}\) 的下确界，要求 \(\widehat C|_{N_\rho}=C_0\) 且 \(\operatorname{Fix}((\operatorname{Id}+\widehat C)/2)=M\)，不预先要求紧支撑。现在有
\[
L_0=\frac{\sqrt2+63/256}{\sqrt{\sqrt2-1/4}}\approx1.5351441898897367,
\qquad L_0\le L_*\le3025/32=94.53125. \tag{EC25}
\]
下界由限制回原管，完成上界由 C264。大的上界不证明 gap；显式完成不证明 \(L_*=L_0\) 或端点达到。

下一动作是用 EC24 优化完整位移 D=ae 的全对 Hölder 相容性：固定整个原管，构造带可靠误差的真实覆盖证书，或解析严格缺口。先比较位移差商，再决定 collar 宽度、旋转权重与幅度；只降低归一化方向常数未必改善完成预算。一般 ENR 与全域吸引不由本轮结论授予。

本轮价值是关闭实际完成黑箱、给出精确原管标尺。内部证明成立不等于公开新颖性；未作足以认证这些公式首次发表的文献穷尽审查。

