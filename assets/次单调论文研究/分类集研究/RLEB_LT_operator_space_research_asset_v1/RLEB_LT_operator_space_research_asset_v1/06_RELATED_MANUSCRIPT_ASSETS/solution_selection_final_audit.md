# Solution-selection 新研究稿最终审计报告

审计日期：2026-09-19。对象：2026-09-18 版《RLEB–PPA 中解选择映射的最优稳定性》（`research_note.md`）及新增构造。

**结论：数学审计为 `ABC_PASS_AFTER_REPAIR`。主模定理、匹配下界、完整显式算子和 Q-二次点收敛均可保留；一般 RLEB 推论有一个必须修补的局部／完整 resolvent 接口漏洞。优先权审计为 `PARTIAL-PRIOR`：方法与若干宽泛现象明确已有；本次未找到覆盖精确联合结果的同一定理或构造，但没有证明全球首创。修补并重写相关工作后，可以作为研究稿继续推进。**

这不是“原文无条件全通过”，也不是“发现部分先例，所以整体已知”。下文分别给出错误的反例、修补后的证明、先例的精确覆盖范围和未关闭项目。

范围及证据约定：

- 原 RLEB 作为已建立基础；仅检查实际调用的 RL、局部映射、A1–A4、一步界、局部长度预算、residual-growth 及强切向／完整纤维接口，没有重审无关原稿。
- 先完成 A、B、C，继而进行两轮反例／量词压力审查，并由 `ABC_gate_adjudication.md` 准入 D；随后完成 D1–D4 及第二轮优先权压力审查。未用随机测试、审核人数或“搜索未命中”代替证明。
- 本终审完整读取用户任务、新稿、A/B/C、两份 ABC 压力报告、数学门终裁、D1–D4、`D_claim_scope_audit.md` 和 `D_adversarial_priorart_stress.md`；直接复核关键公式、反例、原 RLEB 接口，并抽核 Wiśnicki Lemma 1、Brent (4.16)–(4.18)、Bauschke–Moursi–Wang Fact 2.1、Lee–Pham Lemma 2.2 原文。其他文献对应合并 D 专项记录的原文阅读；这不冒称主席逐篇重新通读全部文献。没有取得原文的入口明确留在第五类。
- 新稿与 zip 同文副本经前序审计核对一致，SHA-256 为 `42cd0a2a7bbf91e105f37f450b239d1b839fa67159a079f5b880acf2710934b7`。本报告没有修改新稿或原 RLEB 稿。
- 新稿位置用节号和公式号；原稿位置用 TeX 文件及定理标签。本文用 \(q\) 表示实际统一距离因子、\(\kappa\) 表示 RLEB 证书因子、\(\sigma\) 表示点尾因子，三者不互换。

## 一、致命错误

### F1．未发现要求撤回修补后主结果的致命数学错误

没有发现必须更换两个显式算子、删除 \(\log\log\) 分子、改变 \(\beta\) 或 \(\alpha\)、撤回点误差 Q-二次或撤回非半代数结论的反例。第三类给出支持这一结论的独立证明链，而非只复述定理。

但是，**未经修补的一般断言“原 A1–A4 自动使完整 \(J_{\lambda F}\) 成为单值迭代”是假的**。第二类 R1 给出一维最小反例。把它列为可修补漏洞的理由是：局部版本、抽象模传递和全部具体完整 proximal 构造都保留原结论；不是因为错误无关紧要。

### F2．未发现足以判定精确联合包整体已知的先例；宽泛首次宣告则不可成立

经典 AGM 已包含“半代数快速迭代与非 Hölder、非半代数极限选择并存”的数学内容；Wiśnicki／Pérez García–Fetter Nathansky 已有有限前缀与统一尾平衡的定量方法；一般逆图 resolvent 编码也已知。若改稿后把这些分别宣称为首次，会有明确反证。

**现稿已经声明全球优先权未确认，不能把上述假想的扩大宣告虚算成作者现有错误。**真正待保护的内容是精确量级、实际参数类别中的匹配下界，以及严格 RLEB 条件内的完整有限分支实现；第四类分别判断它们。

## 二、可修补漏洞

### R1．唯一实质接口漏洞：局部 \(J_{\mathcal G}\) 不能无条件升级成完整 \(J_{\lambda F}\)

位置：新稿 §0 的一般约定 \(T=J_{\lambda F}\)、§1 推论 1；原稿 `sections/theorem_spine.tex` 中局部映射定义、`ass:local-rleb`、`thm:two-branch-RLEB`。

原接口只保证

\[
J_{\mathcal G}(x)=\{u:(u,(x-u)/\lambda)\in\mathcal G\}
\]

在 \(U_R\) 上有且只有一个值。A1 是“图块内至少一个解”，A2 是“图块内同输入不碰撞”，不排除全图的图块外解。

**最小反例。**在 \(\mathbb R\) 上令

\[
F(u)=\{u,-u\},\quad \mathcal G=\{(u,u):u\in\mathbb R\},
\quad S=\{0\},\quad\lambda=1.
\]

取 \(U=\mathbb R,R=1,\gamma=1/2,L=0,\bar t=1,\psi(t)=t,\kappa=1/2\)。图块的输入映射为 \(u\mapsto2u\)，任意图对有 \(a=b\)，故反射差为零；整个算子的最小残差为 \(r_F(u)=|u|\)，且

\[
\psi\bigl((d+Ld^\gamma)/2\bigr)=d/2=\kappa d.
\]

A1–A4 与 gauge domain 全成立，但

\[
J_{\mathcal G}(x)=x/2,\qquad
J_F(x)=\begin{cases}\{x/2\},&x\ne0,\\ \mathbb R,&x=0.\end{cases}
\tag{R1.1}
\]

所以完整 \(J_F\) 不是可直接迭代的单值映射。

**充分修补，任选其一：**一般推论取 \(T=J_{\mathcal G}\)；若仍要称完整 PPA，则另要求

\[
J_{\lambda F}(x)=J_{\mathcal G}(x)\quad(x\in W),
\tag{R1.2}
\]

其中 \(W\) 是由原长度预算预先确定的共同轨道输入区域，具体见 B2。只在初值球上检查相等不够，因为轨道可以切向漂移出初值球。两个显式模型和参数族已经独立反演全图，故它们实际满足所需完整性，不必降格为“选中分支”的例子。

### R2．几何模型的“任意尺度 RL”不等于“任意尺度严格兼容”

位置：新稿 (2.3)–(2.5)。确切的严格兼容范围是

\[
\kappa_R=\frac{(2\sqrt2+\tfrac52\sqrt R)^2}{16}<1
\iff
0<R<\left[\frac{2(4-2\sqrt2)}5\right]^2.
\tag{R2}
\]

取 \(R=1\) 即否定不加半径限制的读法。稿件已给有效的 \(R=0.01\)，因此仅须把小尺度量词写进陈述，不改变局部结果。

### R3．二次 collar 的 all-pairs 陈述须保留输入对尺度

位置：定理 4 及其证明。给定 \(|r|,|r'|\le R_0\)，还须指定有限 \(D>0\)，对 \(\delta=\|x-x'\|\le D\) 使用

\[
L_{R_0,D}=2\sqrt2+(1+4R_0)\sqrt D.
\tag{R3}
\]

反例是 \(x=(0,0,0),x'=(M,0,0)\)：反射差为 \(M\)，固定有限 \(L\) 不可能对任意 \(M\) 满足 \(M\le L\sqrt M\)。原 RL 定义及新稿证明已有尺度限制；应使定理正文与证明一致。

### R4．非半代数证明须明确所取的是标量切片

位置：§5.1。“限制整个 \(\Pi\) 得到正且趋零的一元函数”不够准确。几何例的第一极限坐标恒为 \(2\sqrt{r_0}\)，不趋零。所需函数应写为

\[
f(\varepsilon):=\pi_2\Pi(0,\varepsilon,r_0)
=\|\Pi(0,\varepsilon,r_0)-\Pi(0,0,r_0)\|.
\tag{R4}
\]

二次例同理。这个补齐使原增长二分证明完全成立；不削弱非半代数结论。

### R5．三角充分条件须明确切向定义域或留域保证

位置：§5.2。无条件无限迭代版本可直接指定 \(a\in\mathbb R^m\)、\(r\in[0,R]\)。若只在有界切向开集给条件，必须同时控制轨道留域。例如仅在 \(a\in(0,1)\) 定义 \(B(a,r)=\sqrt r\)，所列切向／法向差分条件都成立，但 \((a_0,r_0)=(0.9,0.04)\) 一步就得到 \(a_1=1.1\)。

当前稿没有声称这一被削弱的局部版本，因此 R2–R5 是有限的量词／表述补齐，与 R1 的真实接口缺失严重性不同。

### R6．相关工作须补入直接前身，并保留现有正确边界

位置：§6 及投稿摘要／贡献段。应补入第四类中的旧回缩截断引理、经典 AGM、标准逆图编码；原五篇起点不足以呈现新对象的文献背景。这是本轮发现后的必要定位修订，不要求撤回已证数学结果。

同时明确：任意实 \(\gamma,q\) 的族是闭图至多二值；有理 \(\gamma\) 才保证该几何族半代数，一般超几何族还需有理 \(\nu\)。固定解点 calmness 与邻域两点非 Hölder、实际 \(q\) 与保守 \(\kappa\)、几何量级锐性与超几何指数锐性，须继续分别陈述。原文这些边界大多已经做对，不能在摘要压缩时删除。

## 三、已独立复核

### A1．完整反演：负输入、零输入、负切向、cap 接点与满射性均闭合

对应任务 A1–A2；新稿 (2.1)、(2.2)、(4.1)、(4.2)。令

\[
g(\eta)=\frac{\sqrt{1+4\eta_+}-1}{2},\qquad
\phi_a(\eta)=\eta-\min\{\sqrt a,g(\eta)\},\quad a\ge0.
\]

对 \(a>0\)，由 \(g(\eta)^2+g(\eta)=\eta\) 得

\[
\phi_a(\eta)=
\begin{cases}
\eta,&\eta\le0,\\
g(\eta)^2,&0\le\eta\le a+\sqrt a,\\
\eta-\sqrt a,&\eta\ge a+\sqrt a.
\end{cases}
\tag{A1.1}
\]

三段严格递增，像依次为 \(( -\infty,0]\)、\([0,a]\)、\([a,\infty)\)，接点值一致。因此它是整条实轴的连续双射，且

\[
\phi_a^{-1}(p)=p+\sqrt{\min\{p_+,a\}}.
\tag{A1.2}
\]

\(a=0\) 时为恒等。\(p=0,p=a\) 处相邻表达式一致，没有多出的逆值；负 \(p\) 给 \(\eta=p\)。

在几何模型完整 inclusion \(x-u\in F(u)\) 中，两支法向方程是 \(r=4y\) 与 \(r=-4y\)，故唯一 \(y=|r|/4\)。二次模型两支是 \(r=\sqrt y\) 与 \(r=-\sqrt y\)，故唯一 \(y=r^2\)。非零输入的符号唯一指定分支；零输入强制 \(y=0\)，此时两支合并。其余坐标由 (A1.2) 唯一确定，得到

\[
T(z,p,r)=\bigl(z+\sqrt{|r|},\ p+\sqrt{\min\{p_+,|r|\}},\ |r|/4\bigr),
\tag{A1.3}
\]
\[
\widetilde T(z,p,r)=\bigl(z+\sqrt{|r|},\ p+\sqrt{\min\{p_+,|r|\}},\ r^2\bigr).
\tag{A1.4}
\]

反向任取任一全图点及任一分支值，令输入为 \(x=u+u^*\)，以上法向方程和标量逆函数严格恢复 \(u\)。这证明的是全部纤维的存在与唯一性，不仅是所选公式的正向 graph identity。

两支在闭半空间 \(y\ge0\) 上连续，有限并图闭；根式、正部、min 和有限并保持半代数性。两支差分别为 \(8y\)、\(2\sqrt y\)：\(y>0\) 恰两值、\(y=0\) 一值、\(y<0\) 空。第一残差分量在 \(y>0\) 非零，因此零集严格是 \(S=\mathbb R^2\times\{0\}\)。

### A2．真正跨分支 all-pairs RL、最大指数及渐近常数

对应任务 A3；新稿 (2.3) 及定理 4。令 \(\delta=\|x-x'\|\)、\(m(p,r)=\min\{p_+,|r|\}\)。有

\[
|m(p,r)-m(p',r')|\le\max\{|p-p'|,|r-r'|\}\le\delta,
\quad |\sqrt s-\sqrt t|\le\sqrt{|s-t|}.
\]

两项切向根式差的欧氏合并范数至多 \(\sqrt2\sqrt\delta\)。几何反射的法向部分 \(f(r)=|r|/2-r\) 对所有符号均 \(3/2\)-Lipschitz；跨零时 \(|f(r)-f(r')|\le3|r-r'|/2\) 仍成立。因此

\[
\|\Delta(2T-I)\|\le2\sqrt2\sqrt\delta+\tfrac32\delta
\le(2\sqrt2+\tfrac32\sqrt R)\sqrt\delta\quad(\delta\le R).
\tag{A2.1}
\]

A1 的完整参数化将任意两图点——含异支图点——还原为这个输入对，故确是全图 RL。二次法向部分满足

\[
|(2r^2-r)-(2r'^2-r')|\le(1+4R_0)|r-r'|,
\]

给出 (R3)，同样包含跨分支与 cap 配对。

取 \(x_t=(0,t,t),x_t'=(0,t,0)\)，两输入相距 \(t\)，几何及二次模型分别满足

\[
\|\Delta(2T-I)\|^2=8t+t^2/4,
\qquad
\|\Delta(2\widetilde T-I)\|^2=8t+(2t^2-t)^2.
\tag{A2.2}
\]

因此任何指数 \(>1/2\) 都失败；指数 \(1/2\) 的小尺度最小可能常数极限至少 \(2\sqrt2\)，与上界一致。没有证明给定有限 \(R\) 时所列 \(L_R\) 就是最小常数。

### A3．残差 EB 确实取整个多值算子的最小范数

对应任务 A4；新稿 (2.4)、(4.3)。两模型的两支范数平方分别是

\[
4y+D_y(\eta)^2+9y^2,\qquad 4y+D_y(\eta)^2+25y^2,
\]

及

\[
\sqrt y+\widetilde D_y(\eta)^2+(\sqrt y-y)^2,
\quad
\sqrt y+\widetilde D_y(\eta)^2+(\sqrt y+y)^2.
\]

所以真实最小残差满足

\[
r_F^2=4y+D_y(\eta)^2+9y^2\ge4y,
\quad
r_{\widetilde F}^2=\sqrt y+\widetilde D_y(\eta)^2+(\sqrt y-y)^2\ge\sqrt y.
\tag{A3}
\]

结论分别为 \(y\le r_F^2/4\)、\(y\le r_{\widetilde F}^4\)。负 proximal 输入实际选择较大残差支，并不改变以上 min-norm EB。\(\eta\le0,y\downarrow0\) 还给出几何系数 \(1/4\) 与二次系数 \(1\) 的渐近精确性。

### A4．严格兼容和完整局部覆盖能同时实现

几何模型取全图、\(U=\mathbb R^3\)。每个输入的完整纤维唯一；其到 \(S\) 的投影零图点全部存在。取 (R2) 内半径及 \(\bar t\ge(R+L_R\sqrt R)/2\)，对全部 \(0<d\le R\)，

\[
\frac{\psi((d+L_R\sqrt d)/2)}d
=\frac{(\sqrt d+L_R)^2}{16}\le\kappa_R<1.
\tag{A4.1}
\]

二次模型取完整图块 \(\mathcal G_{R_0}=\operatorname{gph}\widetilde F\cap\{0\le y\le R_0^2\}\)，其输入像恰为 \(\mathbb R^2\times[-R_0,R_0]\)。令 \(0<R\le R_0<1\)、\(U=\mathbb R^3\)，则完整 \(U_R\) 纤维均在该块内，且 collar 前向不变。以 \(L_R=2\sqrt2+(1+4R_0)\sqrt R\)、\(\psi(t)=t^4\) 得

\[
\sup_{0<d\le R}\frac{\psi((d+L_R\sqrt d)/2)}d
\le\frac{R[2\sqrt2+(2+4R_0)\sqrt R]^4}{16}\longrightarrow0.
\tag{A4.2}
\]

故可选一个固定小半径，使覆盖、比较尺度、gauge domain 与严格兼容同时成立；不是只写 \(O(d^2)\) 而缺统一半径。

### A5．实际 \(q=1/4\) 与证书极限 \(\kappa_*=1/2\) 不能互换

几何模型精确有 \(d(Tx,S)=d(x,S)/4\)。证书则先粗估切向步长，再使用残差上界，得到 \(\kappa_R\downarrow1/2\)，有限 \(R>0\) 下仍 \(\kappa_R>1/2\)。因此

\[
\beta_{\rm actual}=\frac{\tfrac12\log4}{\log2}=1,
\qquad
\beta_{\rm cert}(R)=\frac{\log(1/\kappa_R)}{2\log2}\longrightarrow\frac12.
\tag{A5}
\]

新稿 §0、§2、§3 已区分两者；没有发现用实际 \(q\) 的下界冒充固定保守 \(\kappa\) 类别的锐性。

### B1．两个抽象模传递定理成立，局部 Hölder 尺度可逐步闭合

对应任务 B1；新稿 (1.1)–(1.6)。写 \(\delta=e^{-t}\)，令 \(e_j=\|T^jx-T^jy\|\)，取 \(A\ge\max\{1,H^{1/(1-\gamma)}\}\)。只要 \(e_j\le R\)，有

\[
e_j\le Ae^{-t\gamma^j}\Longrightarrow
e_{j+1}\le HA^\gamma e^{-t\gamma^{j+1}}\le Ae^{-t\gamma^{j+1}}.
\tag{B1.1}
\]

几何尾 \(M\sigma^n\) 下，取

\[
b=\log(1/\gamma),\quad\beta=\frac{\log(1/\sigma)}b,\quad D=\beta+1,
\quad n=\left\lfloor\frac{\log[t/(D\log t)]}b\right\rfloor.
\]

对所有 \(j\le n\)，候选界均不超过 \(At^{-D}\)。先令 \(t\) 足够大使它小于 \(R\)，再归纳使用 (B1.1)，所以没有偷用全局 Hölder。取整给

\[
t\gamma^n\ge D\log t,\qquad
\sigma^n\le\sigma^{-1}(D\log t/t)^\beta.
\]

加两条统一尾界得到

\[
\|\Pi(x)-\Pi(y)\|\le At^{-D}+2M\sigma^{-1}(D\log t/t)^\beta
\le C(\log t/t)^\beta.
\tag{B1.2}
\]

超几何尾 \(Me^{-c_0\nu^n}\) 下取 \(n=\lfloor\log t/\log(\nu/\gamma)\rfloor\)，有

\[
t\gamma^n\ge t^\alpha,\quad\nu^n\ge\nu^{-1}t^\alpha,
\qquad\alpha=\frac{\log\nu}{\log(\nu/\gamma)}.
\]

以 \(Ae^{-t^\alpha}<R\) 同样闭合局部归纳，得到 \(Ce^{-ct^\alpha}\)。两种结论的常数及小尺度阈值与所比初值对无关。

### B2．共同初值球与统一尾界确由原局部化预算推出

对应任务 B2；新稿推论 1；原稿 `eq:direct-localization`、`eq:direct-tail`。采用 R1 修补后映射，固定 \(\bar x\in S\cap U\)，取 \(B_\rho(\bar x)\subset U\)，令

\[
\mathcal L(d)=\frac12\left(\frac d{1-\kappa}+\frac{Ld^\gamma}{1-\kappa^\gamma}\right).
\]

选 \(0<\varepsilon\le R\) 使 \(\varepsilon+\mathcal L(\varepsilon)<\rho\)，并预先定义

\[
W=U_R\cap\overline B_{\varepsilon+\mathcal L(\varepsilon)}(\bar x).
\tag{B2.1}
\]

每个 \(x\in B_\varepsilon(\bar x)\) 同时满足 \(d(x,S)\le\varepsilon\) 及
\(\operatorname{dist}(x,U^c)>\rho-\varepsilon>\mathcal L(d(x,S))\)。原定理的部分轨道长度界使所有迭代点留在 \(W\)，故共同区域是预算的结论，不是补入的未知吸引域。若 (R1.2) 在 \(W\) 上成立，完整轨道逐步等于局部轨道。

令 \(H=(R^{1-\gamma}+L)/2\)，有单步两点界与步长界

\[
\|Tx-Ty\|\le H\|x-y\|^\gamma\ (\|x-y\|\le R),
\qquad\|Tx-x\|\le Hd(x,S)^\gamma.
\]

因此整球统一满足

\[
\|T^kx-\Pi(x)\|\le\frac{H\varepsilon^\gamma}{1-\kappa^\gamma}\kappa^{\gamma k}.
\tag{B2.2}
\]

若另证整球统一 \(d(T^kx,S)\le Dq^k\)，可改用 \(HD^\gamma q^{\gamma k}/(1-q^\gamma)\)。不得将逐初值常数冒充统一常数。

超几何递推 \(d_{k+1}\le Kd_k^\nu\)、\(K>0\) 时，缩球使 \(K^{1/(\nu-1)}d_0\le\vartheta<1\)。置 \(C_K=K^{-1/(\nu-1)}\)、\(a=-\gamma\log\vartheta\)，用 \(\nu^{k+j}\ge\nu^k+j(\nu-1)\) 得

\[
\|T^kx-\Pi(x)\|
\le\frac{H C_K^\gamma}{1-e^{-a(\nu-1)}}e^{-a\nu^k}.
\tag{B2.3}
\]

\(K=0\) 是一步到解的退化情形。原 residual-growth 的 \(r_F\ge m d^a\)、\(m>0\)、\(0<a<\gamma\) 给 \(\nu=\gamma/a\)，于是 \(\alpha=\log(\gamma/a)/\log(1/a)\)。没有剩余的共同吸引域缺口。

**防止错误推广的压力反例。**统一收敛不能代替单步 all-pairs。令闭图四值算子在 \(y\ge0\) 为
\(F_*(u,y)=\{(\pm2\sqrt y,3y),(\pm2\sqrt y,-5y)\}\)，在 \(y<0\) 为空，则

\[
J_{F_*}(z,r)=\{(z\pm\sqrt{|r|},|r|/4)\}.
\]

所有允许轨道都有统一几何尾，但按 \(z\ge0\) 选正号、\(z<0\) 选负号得到
\(\Pi_*(z,r)=(z+2\operatorname{sgn}_+(z)\sqrt{|r|},0)\)，固定 \(r>0\) 时在 \(z=0\) 不连续。这个选择不满足单步 Hölder，完整多值图也不满足 all-pairs。它不反驳新稿，而明确说明不能把原稿较弱的 selection-uniform 收敛扩展偷换进本推论。

### B3．首次饱和时刻和几何下界：\(N\)、\(N-1\) 方向正确，常数一致

对应任务 B3；新稿 (3.1)、(3.3)–(3.8)。设

\[
p_{k+1}=p_k+B\min\{p_k,r_k\}^\gamma,\quad p_0=\varepsilon>0,
\quad r_k=r_0q^k,\quad N=\min\{k:p_k\ge r_k\},\quad t=\log(1/\varepsilon).
\]

\(p_k\ge\varepsilon\)、\(r_k\to0\) 保证 \(N<\infty\)；有限步对 \(\varepsilon=0\) 的连续性保证 \(N\to\infty\)。未饱和递推是

\[
\log p_{k+1}=\gamma\log p_k+\log(B+p_k^{1-\gamma}).
\]

取
\(C_0=\max\{|\log B|,|\log(B+r_0^{1-\gamma})|\}/(1-\gamma)\)，则

\[
\log p_k=-t\gamma^k+E_k,\qquad |E_k|\le C_0\quad(0\le k\le N).
\tag{B3.1}
\]

它包括 \(k=N\)，因为生成 \(p_N\) 的前一步仍未饱和。记 \(a=\log(1/q)\)，在 \(N\) 用 \(p_N\) 上界、在 \(N-1\) 用 \(p_{N-1}\) 下界，得到

\[
t\gamma^N\le aN+C_0-\log r_0,
\qquad t\gamma^{N-1}>a(N-1)-C_0-\log r_0.
\tag{B3.2}
\]

因此 \(t\gamma^N=\Theta(N)\)。取对数、先得 \(N=\Theta(\log t)\) 再代回，得

\[
N=\frac{\log t-\log\log t}{\log(1/\gamma)}+O(1),
\qquad\gamma^N=\Theta(\log t/t).
\tag{B3.3}
\]

全部常数仅依赖固定模型，不依赖 \(\varepsilon,N\)。饱和后始终饱和，且

\[
p_\infty=p_N+\frac{B r_N^\gamma}{1-q^\gamma},\qquad
p_N\le q^{-1}r_N+Bq^{-\gamma}r_N^\gamma=O(r_N^\gamma).
\]

故

\[
p_\infty=\Theta\!\left((\log t/t)^{\gamma\log(1/q)/\log(1/\gamma)}\right).
\tag{B3.4}
\]

显式平方根例给 \(\beta=1\)，确实不能删除 \(\log t=\log\log(1/\varepsilon)\) 分子。结论为 \(\Theta\)，没有冒称离散切换后的归一化比值必有极限。

### B4．任意实际 \((\gamma,q)\) 的闭图二值严格兼容实现成立

对应任务 B4；新稿 (3.6)–(3.7)。\(G_a(p)=p+B\min\{p_+,a\}^\gamma\) 在三个分段上连续严格递增，左右趋向两端无穷，故为实轴双射。其逆 \(\tau_a\) 在所有接点连续，且 \(|\tau_a(\eta)-\eta|\le Ba^\gamma\) 保证连续延拓到 \(a=0\)。

令 \(a=y/q\)，取两支

\[
F(\xi,\eta,y)=\{(-Aa^\gamma,\tau_a(\eta)-\eta,a-y),
(-Aa^\gamma,\tau_a(\eta)-\eta,-a-y)\}.
\tag{B4.1}
\]

法向输入 \(r=\pm a\) 与唯一标量反演给完整全空间 resolvent
\(T(z,p,r)=(z+A|r|^\gamma,p+B\min\{p_+,|r|\}^\gamma,q|r|)\)。闭图、值数及零集的论证与 A1 相同。真实最小残差与全对常数为

\[
r_F^2=A^2a^{2\gamma}+(\tau_a(\eta)-\eta)^2+(1-q)^2a^2,
\quad L_R=2\sqrt{A^2+B^2}+(1+2q)R^{1-\gamma}.
\]

用 \(\psi(s)=q(s/A)^{1/\gamma}\)，兼容商上界是

\[
\kappa_R=q\left(\frac{\sqrt{A^2+B^2}+(1+q)R^{1-\gamma}}A\right)^{1/\gamma}.
\tag{B4.2}
\]

先固定 \(0<B/A<\sqrt{q^{-2\gamma}-1}\)，再固定

\[
R^{1-\gamma}<\frac{Aq^{-\gamma}-\sqrt{A^2+B^2}}{1+q},
\tag{B4.3}
\]

即可严格兼容，再令敏感初值 \(\varepsilon\downarrow0\)。没有让模型或证书随 \(\varepsilon\) 改变。结合 B3，固定实际 \((\gamma,q)\) 的锐性成立。

\(B>0\) 时 \(\kappa_*=q(1+(B/A)^2)^{1/(2\gamma)}>q\)，故不等于固定保守 \(\kappa=q\) 类别的锐性。几何族有理 \(\gamma\) 时半代数；实系数 \(q,A,B\) 不必有理。无理幂 \(r^\gamma\) 的一元增长指数不是有理数，所以不能把这一个显式族的半代数性扩大到全部实指数。

### B5．超几何指数正确，overshoot 被独立控制

对应任务 B5；新稿 §4。取 \(r_k=e^{-a\nu^k}\)、\(a>0,\nu>1\)。式 (B3.1) 不变，交叉条件变成

\[
t\gamma^N\le a\nu^N+C_0,
\quad t\gamma^{N-1}>a\nu^{N-1}-C_0.
\]

因此

\[
N=\frac{\log t}{\log(\nu/\gamma)}+O(1),\qquad
t\gamma^N,\nu^N=\Theta(t^\alpha),
\quad\alpha=\frac{\log\nu}{\log(\nu/\gamma)}.
\tag{B5.1}
\]

直接在 \(k=N\) 用 (B3.1) 得 \(p_N=e^{-\Theta(t^\alpha)}\)。饱和尾另有

\[
B e^{-a\gamma\nu^N}
\le B\sum_{j\ge0}e^{-a\gamma\nu^{N+j}}
\le\frac{B}{1-e^{-a\gamma(\nu-1)}}e^{-a\gamma\nu^N}.
\tag{B5.2}
\]

两项相加给 \(p_\infty=e^{-\Theta(t^\alpha)}\)。这排除任意 \(\alpha'>\alpha\) 的统一 \(Ce^{-ct^{\alpha'}}\) 上界，但不提供指数前最优常数，也不等于某个固定 \(c_*\) 下的 \(\Theta(e^{-c_*t^\alpha})\)。

**几何 overshoot 估计在这里确实可能为假。**固定 \(c\in(0,1)\)，令 \(h(s)=s+Bs^\gamma\)、\(\varepsilon_N=h^{-(N-1)}(cr_{N-1})\)。此前切向值更小、阈值更大，所以首次饱和在充分大时正是 \(N\)，而

\[
\frac{p_N}{r_N^\gamma}
\sim Bc^\gamma r_{N-1}^{-\gamma(\nu-1)}\longrightarrow\infty.
\tag{B5.3}
\]

新稿没有使用这个错误替代估计。把 (B4.1) 的 \(a\) 改成 \(y^{1/\nu}\) 给完整实现；\(r_F\ge Ay^{\gamma/\nu}\)，兼容商为 \(O(d^{\nu-1})\to0\)，固定 collar 覆盖及 all-pairs 仍闭合。有理 \(\gamma,\nu\) 时该族半代数。

### C1．证明的是到实际极限点的 Q-二次，两个比值正确

对应任务 C1；新稿定理 4。取 \(0<|r_0|<1\)，\(k\ge1\) 时设 \(b_k=\sqrt{r_k}\)，则 \(b_{k+1}=b_k^2\)。对 \(0<b<1\)，令

\[
S(b)=\sum_{j\ge0}b^{2^j},\qquad0\le S(b)-b\le\frac{b^2}{1-b}.
\]

第一切向尾精确等于 \(S(b_k)\)。若 \(p_0\le0\)，第二切向尾为零；若 \(p_0>0\)，最终饱和后第二切向尾也等于 \(S(b_k)\)。因此对充分大 \(k\)，

\[
e_k^2=\|x_k-x_\infty\|^2=mS(b_k)^2+b_k^4,
\quad m=\begin{cases}1,&p_0\le0,\\2,&p_0>0,\end{cases}
\]

从而

\[
\lim_{k\to\infty}\frac{e_{k+1}}{e_k^2}=m^{-1/2}
=\begin{cases}1,&p_0\le0,\\1/\sqrt2,&p_0>0.\end{cases}
\tag{C1}
\]

负 \(r_0\) 只影响第一步；\(r_0=0\) 是驻点，已排除无意义的 \(0/0\)。各轨道最终饱和时刻可以依赖初值，不等于存在所有初值共同的二次渐近起点；共同超几何尾由另一条统一估计保证。

### C2．解点 Hölder calmness 与完整邻域两点非 Hölder 完全相容

对应任务 C2。固定解点 \(s\)，由预算与 \(\Pi(s)=s\)，

\[
\|\Pi(x)-s\|\le\|x-s\|+\mathcal L(d(x,S))
\le C_s\|x-s\|^\gamma.
\tag{C2.1}
\]

反例却固定非解点 \(x_0=(0,0,r_0)\)、\(r_0>0\)，比较 \(x_\varepsilon=(0,\varepsilon,r_0)\)。还可不用精细饱和渐近式独立反证：对每个固定整数 \(m\)，充分小 \(\varepsilon\) 的前 \(m\) 步未饱和，所以

\[
f(\varepsilon)\ge p_m\ge\varepsilon^{2^{-m}}.
\]

给定 \(\theta>0\) 先选 \(2^{-m}<\theta\)，便有
\(f(\varepsilon)/\varepsilon^\theta\to\infty\)。任意原点完整邻域可容纳这样的固定小 \(r_0\)，故没有统一两点正阶 Hölder 界。不能将其改称解点 calmness 失败或极限不连续。

### C3．非半代数结论由一元增长二分严格推出

对应任务 C3；新稿 §5.1。取 (R4) 的标量切片。两模型均有

\[
0\le p_\infty(\varepsilon)-p_k(\varepsilon)
\le\sum_{j\ge k}\sqrt{r_j}\longrightarrow0,
\]

右端与 \(\varepsilon\) 无关，故连续有限步函数统一收敛到连续 \(f\)，且 \(f(0)=0\)、\(f(\varepsilon)>0\)。若 \(\Pi\) 在原点某完整邻域半代数，则该直线限制与坐标投影也半代数。一元增长二分给

\[
f(\varepsilon)=c\varepsilon^a+o(\varepsilon^a),
\qquad c>0,\ a\in\mathbb Q_{>0},
\]

与 C2 中取 \(\theta=a\) 的发散矛盾。工具来源为第四类 Lee–Pham 的 Lemma 2.2；这是标准事实的应用，不是新增长定理。结论是非半代数，不是“在任何 o-minimal 结构都不可定义”。

### C4．三角恢复条件正确，不能升级为一般 signed-Schur 结论

对应任务 C4；新稿 (5.1)。在 \(\mathbb R^m\times[0,R]\) 上，\(B(a,0)=0\) 给 \(\|B(a,r)\|\le Hr^\gamma\)，故总长度至多 \(Hr^\gamma/(1-q^\gamma)+r\)。两轨道切向差满足

\[
u_{k+1}\le(1+CR^\eta q^{\eta k})u_k+Hq^{\gamma k}|r-s|^\gamma.
\]

用 \(\prod_k(1+CR^\eta q^{\eta k})\le e^{CR^\eta/(1-q^\eta)}\) 得

\[
\|\Pi_a(a,r)-\Pi_a(b,s)\|
\le e^{CR^\eta/(1-q^\eta)}
\left(\|a-b\|+\frac H{1-q^\gamma}|r-s|^\gamma\right).
\tag{C4}
\]

新反例在固定 \(r>0\)、\(0<h<r\) 时切向增量差商为 \(h^{-1/2}\to\infty\)，不满足这里的条件。自然输出坐标的输入反演还满足

\[
\frac{dp}{d\eta}=1-\frac1{\sqrt{1+4\eta}}\downarrow0,
\]

不提供原附录 (S2)、(S4) 要求的统一强切向反演和导数控制。新稿明确不调用这些强假设，也没有把三角法向递推替换成一般耦合法向动力学。本审计不额外宣称排除所有重新参数化。

## 四、优先权对应

### D0．分项裁决及证据含义

`KNOWN` 表示有明确旧结论或经典公式的直接推论；`PARTIAL-PRIOR` 表示覆盖方法或真子命题；`NO-EXACT-PRIOR-FOUND` 只表示本次列明原文范围内未定位同一精确结果，不是“证明没有先例”。

| 对象 | 本轮裁决 | 必须保留的区别 |
| --- | --- | --- |
| 有限前缀加统一两尾、再平衡截断步数 | KNOWN | 不能把证明模板称全新原理 |
| 局部单步 \(\gamma<1\)-Hölder 的几何模 \((\log\log/\log)^\beta\)、超几何模及 \(\alpha\) | NO-EXACT-PRIOR-FOUND；属旧机制的定量扩展候选 | U1、U2 未关闭；短证明不等于精确结论已经发表 |
| 统一几何快收敛、半代数单步与非 Hölder／非半代数极限并存 | 经典 AGM 已覆盖宽泛现象 | AGM 的量级为 \(1/\log\)，不是匹配 \(\log\log/\log\) |
| 把迭代写成完整 resolvent、由图线性变换继承闭图／半代数 | KNOWN | 严格 RL–EB 数值匹配不会自动继承 |
| 固定实际 \((\gamma,q)\) 的尖锐量级、严格 RLEB、完整闭图至多二值实现 | NO-EXACT-PRIOR-FOUND | 有理幂时半代数；不包括固定保守 \(\kappa\) 的锐性 |
| 共同超几何尾、坏参照轨道自身 Q-二次、邻域两点非 Hölder／非半代数、完整严格 RLEB 构造同时成立 | NO-EXACT-PRIOR-FOUND | AGM 正初值二次和轴上坏选择不能拼成这个联合量词 |

### D1．抽象模传递的直接前身：有旧方法，但未核到相同退化量级

**Andrzej Wiśnicki，*Hölder continuous retractions and amenable semigroups of uniformly Lipschitzian mappings in Hilbert spaces*.** TMNA 43 (2014), 89–96；DOI **10.12775/TMNA.2014.006**；[arXiv:1204.6464v2，Lemma 1](https://arxiv.org/html/1204.6464v2)。该引理假设完备有界度量空间、单步 \(k\)-Lipschitz 和共同增量 \(c\rho^n\)，证明使用

\[
d(Rx,Ry)\le\frac{2c\rho^n}{1-\rho}+k^n d(x,y).
\tag{D1.1}
\]

它覆盖截断方法与 Lipschitz 情形的 Hölder 极限；不含本稿的 \(A\delta^{\gamma^n}\)、两个指定非幂模或匹配构造。此处是 `PARTIAL-PRIOR`，不能把 \(k\) 换成 Hölder 常数后忽略复合指数。

**Víctor Pérez García、Helga Fetter Nathansky，*Fixed points of periodic mappings in Hilbert spaces*.** Ann. UMCS A 64(2) (2010), 37–48；[原文 Lemma 2.1(c)](https://journals.umcs.pl/a/article/download/3985/2887)。原刊 DOI **10.2478/v10062-010-0013-y**，现期刊网页另列 **10.17951/a.2010.64.2.37-48**。连续 \(T\) 的辅助映射 \(u\) 满足残差缩小 \(a<1\)、步长控制，且 \(u\) 为 \(p\)-Lipschitz；\(R=\lim u^n\) 的 Hölder 指数为

\[
\theta=\frac{\log(1/a)}{\log p+\log(1/a)}.
\]

它是更早的定量前身；不能误说周期映射 \(T\) 自身按此结论收敛。仍没有本稿 \(\gamma^n\) 的退化量级。Wiśnicki 还引用 Benyamini–Lindenstrauss Proposition 1.10；其原页尚缺，见 U1。

本稿包络为 \(Ae^{-t\gamma^n}+2M\sigma^n\) 或 \(Ae^{-t\gamma^n}+2Me^{-c_0\nu^n}\)。上界的显式平衡并不自动证明存在实现下界的算法；后者由 B3–B5 的构造独立完成。这是不能被“方法已有”抹掉的部分。

### D2．经典 AGM：宽泛坏选择已知，精确新联合包未被其覆盖

原始定位：

- **Richard P. Brent，*Fast Multiple-Precision Evaluation of Elementary Functions*.** JACM 23 (1976), 242–251；DOI **10.1145/321941.321944**；[作者提供原刊全文，§4，(4.16)–(4.18)，§5](https://maths-people.anu.edu.au/~brent/pd/rpb034.pdf)。
- **David A. Cox，*The Arithmetic-Geometric Mean of Gauss*.** L’Enseignement Mathématique 30 (1984), 275–330；DOI **10.5169/seals-53831**；Theorem 1.1 与 §1 的 AGM 迭代；[原刊扫描／OCR](https://www.researchgate.net/publication/248675540_The_Arithmetic-Geometric_Mean_of_Gauss)。不把后期重印 DOI 当成 1984 原刊标识。

以下非 Hölder／非半代数措辞是审计从经典公式推导的对应，不假称原文已使用本稿术语。令

\[
G(a,b)=\left(\frac{a+b}2,\sqrt{ab}\right),\quad
\Pi_G(a,b)=(M(a,b),M(a,b)).
\]

对 \(0\le b\le a\le R\)，令 \(d_n=a_n-b_n\)。有

\[
d_{n+1}=\frac{d_n^2}{2(\sqrt{a_n}+\sqrt{b_n})^2}\le d_n/2,
\quad b_n\le M\le a_n,
\]

故整域共同点尾 \(\|G^n(a,b)-\Pi_G(a,b)\|\le R2^{-n}\)。单步在有界域半代数且 \(1/2\)-Hölder。经典积分恒等式及端点渐近给

\[
M(1,\varepsilon)=\frac{\pi}{2K(\sqrt{1-\varepsilon^2})}
\sim\frac{\pi}{2\log(1/\varepsilon)},\qquad M(1,0)=0.
\tag{D2.1}
\]

因此选择差除以任意 \(\varepsilon^\theta\) 发散，并由增长二分非半代数。取绝对值延拓
\(\widehat G(a,b)=((|a|+|b|)/2,\sqrt{|ab|})\) 即可补为全欧氏域的同类宽泛现象，不能只用原 AGM 在正锥上来排除先例。

但三个差别是精确的：

1. AGM 给 \(1/\log\)，没有本稿 \(\log\log/\log\) 的匹配下界。
2. 坏参照轨道 \(G^n(c,0)=(c2^{-n},0)\) 只有线性点收敛，不可能位于共同 \(Ce^{-c_0\nu^n}\) 尾域内；任意逼近该轴的域也不能具有同组超几何常数。
3. 正非固定初值的 AGM 确实是**点误差** Q-二次，\(e_{n+1}/e_n^2\to1/(4\sqrt2M)\)，但该结论不能与轴上的坏稳定性拼接为本稿“坏参照轨道自身也 Q-二次”。本稿二次例参照点 \(p_0=0,r_0>0\) 的比值仍为 \(1\)。

因此 AGM 为强 `PARTIAL-PRIOR`，不是整个联合包的相同先例。

### D3．标准逆图编码已知；严格兼容的实现仍须单独判断

**Heinz H. Bauschke、Walaa M. Moursi、Xianfu Wang，*Generalized monotone operators and their averaged resolvents*.** DOI **10.1007/s10107-020-01500-6**；[arXiv:1902.09827v1，Fact 2.1](https://arxiv.org/html/1902.09827v1)。任意 \(T:D\to X\) 令 \(F=T^{-1}-I\)，即有 \(J_F=T\)。不要求单调性。线性同构 \((x,u)\mapsto(u,x-u)\) 保持闭图和半代数，且 \(\#F(u)=\#T^{-1}(u)\)。这些不能算新构造原理。

对最危险的 AGM 直接编码，\(W=\{(s,t):s\ge t\ge0\}\)、\(d=\sqrt{s^2-t^2}\) 给

\[
F_{\rm AGM}(s,t)=\{(d,s-t-d),(-d,s-t+d)\}.
\tag{D3.1}
\]

它闭图、半代数、至多二值，\(J_F=G\) 的完整输入域恰为 \(\mathbb R_+^2\)。不能说 AGM 无法写成二值 resolvent。可是

\[
r_F(h,0)=h,\qquad d((h,0),\operatorname{zer}F)=h/\sqrt2,
\]

迫使任何有效输出 gauge 满足 \(\psi(h)\ge h/\sqrt2\)。固定小 \(c>0\) 的输入对 \((c,t),(c,0)\) 又迫使全对反射模

\[
\omega(t)\ge\|(t,2\sqrt{ct}-t)\|\ge\sqrt{ct}\quad(0<t\le c).
\]

故其直接 RLEB 兼容商满足

\[
\frac{\psi((t+\omega(t))/2)}t
\ge\frac{\sqrt c}{2\sqrt2\sqrt t}\longrightarrow\infty.
\tag{D3.2}
\]

这严格排除**该直接编码**在坏选择对应零点的严格兼容，而非因旧文没用“RLEB”这个名称就排除。它不排除全部 lift、变量变换或其他 AGM 改造。

原 RLEB 二维基例本已有 \(J_{F_0}(z,r)=(z+\sqrt{|r|},|r|/4)\)、\(\Pi_0=(z+2\sqrt{|r|},0)\)。新稿不能再把基例性质算作本次首次；新增增量是 cap 切向放大、匹配选择下界及超几何变体与全部严格接口的同时实现。

### D4．用户指定起点的逐定理对应

表中编号均按明确注明的原文版本；“未覆盖”针对所列定理、例子及相关论证，不是凭某个关键词没出现就宣布全文无关。

| 文献、标识和定位 | 假设对应及已覆盖部分 | 未覆盖部分 |
| --- | --- | --- |
| **D. Russell Luke、Matthew K. Tam，*Generalized Monotonicity and the Proximal Point Algorithm***；[DOI 10.1287/moor.2025.0863](https://pubsonline.informs.org/doi/10.1287/moor.2025.0863)。正式全文 Proposition 1、Proposition 4、Lemma 2、Assumption 2、Theorem 2；Example 2。 | 局部 submonotonicity、metric subregularity、覆盖和严格常数给局部 PPA R-线性；Lemma 2 从距离与步长给点尾。Example 2 非 Lipschitz 的对象是 \(F\)，不是自动为 \(J_F\)。 | 没有本稿两初值极限差的指定模或坏选择构造。点态 almost-averaged 条件不能当成整个工作域 all-pairs；本稿平方根反射也不满足有限常数全对 Lipschitz。 |
| **D. Russell Luke、Nguyen H. Thao、Matthew K. Tam，*Quantitative Convergence Analysis of Iterated Expansive, Set-Valued Mappings***；DOI **10.1287/moor.2017.0898**；[arXiv:1605.05725v2](https://arxiv.org/pdf/1605.05725v2)。v2 Theorems 2.15、2.18、Corollary 2.19；正式版对应 Theorems 2.1–2.2、Corollary 2.3。 | pointwise almost averaged 加环带／gauge 次正则给距离因子 \(\sqrt{1+\epsilon-(1-\alpha)/(\kappa^2\alpha)}\) 及收敛率。 | 没有 \(\gamma^n\) 复合退化或本稿两个极限模；多值迭代映射与“底层 \(F\) 二值、完整 \(J_F\) 单值”也不能互换。 |
| **同三位作者，*Implicit Error Bounds for Picard Iterations on Hilbert Spaces***；Vietnam J. Math. 46 (2018), 243–258；[DOI 10.1007/s10013-018-0279-x](https://link.springer.com/article/10.1007/s10013-018-0279-x)。[作者上传正式全文](https://www.researchgate.net/profile/Hieu-Thao-Nguyen/publication/323317906_Implicit_Error_Bounds_for_Picard_Iterations_on_Hilbert_Spaces/links/5a8eb28eaca27214055d9692/Implicit-Error-Bounds-for-Picard-Iterations-on-Hilbert-Spaces.pdf)，Theorems 1–4、Remark 1。 | Th1 非扩张、渐近正则与 bounded-set EB；Th2 averaged 与 gauge EB 给 \(\|x_n-x_*\|\le2\varphi^n(d_0)\)，\(\varphi(t)=\sqrt{t^2-\eta[\kappa^{-1}(t)]^2}\)。Th4 从统一距离收缩导出 EB，**Th4 本身不要求非扩张**。 | Th1–2 的单值非扩张迭代若收敛，极限由逐次非扩张继承 1-Lipschitz。Th4 不提供坏极限选择或指定模。原研究阶段只读摘要的缺口已由本轮团队补齐。 |
| **Guoyin Li、Boris S. Mordukhovich、Jiangxing Zhu，*Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods***；DOI **10.1287/moor.2024.0570**；[arXiv:2406.13207v1](https://arxiv.org/html/2406.13207v1)，Theorems 4.3–4.4、Remark 4.5、Example 4.6。 | 下降／步长代理／相对误差／连续性与广义次正则给有限长度和高阶实际点收敛。例 4.6 的 \(f(t)=\lvert t\rvert^{3/2}\) PPA 已有 Q-二次。 | 示例唯一极限为 0，选择映射恒定；没有本稿坏选择合取。正式刊本与 v1 增改尚未关闭，故不冒称这些是已核正式编号，见 U2。 |
| **Jae Hyoung Lee、Tiến-Sơn Phạm，*Openness, Hölder Metric Regularity, and Hölder Continuity Properties of Semialgebraic Set-Valued Maps***；SIOPT 32(1) (2022), 56–74；DOI **10.1137/20M1331901**；[arXiv:2004.02188v2](https://arxiv.org/html/2004.02188v2)，Lemma 2.2、Proposition 3.1、Theorem 3.1、Corollary 3.1。 | 一元半代数幂增长；闭图半代数 Hölder 次正则；相对开性／正则性／逆映射 pseudo-Hölder 等价。 | 不保证无限迭代极限半代数；一般存在某个 EB 指数／常数，不等于本稿实现指定指数、系数和严格兼容。增长二分工具是 KNOWN。 |

### D5．扩展引用链：同对象的前身、强结构对照和未构成精确先例的原因

这些条目用于说明已实际排查的范围；没有将题名相似当成覆盖，也没有将所有邻近工作一概排除。标为“原文无编号定理”的项目给出公式／节位置；没有核到 DOI 的不编造标识。

| 文献、DOI/arXiv 与准确位置 | 假设／已覆盖 | 未覆盖的关键条件 |
| --- | --- | --- |
| **Rafał Kapica、Janusz Morawiec，*Limits of random iterates***，Publ. Math. Debrecen 75 (2009), 137–148；DOI **10.5486/PMD.2009.4344**；[原文](https://publi.math.unideb.hu/paper/1391/download/)，Proposition 3.1、Corollary 3.2、Proposition 3.3、Corollary 3.4、Propositions 3.5–3.6。 | 有限步概率连续性与局部一致概率／\(L^p\) 极限推出连续性；单点概率空间包含确定迭代。 | 没有指定尾函数、\(\gamma^n\) 退化或本稿精确量级和构造。 |
| **Krzysztof Pupka，*Fixed points of periodic and firmly lipschitzian mappings in Banach spaces***，CMUC 53(4) (2012), 573–579；[原文](https://ftp.gwdg.de/pub/misc/EMIS/journals/CMUC/pdf/cmuc1204/pupka.pdf)，Lemma 3、Corollary 1。未核到 DOI/arXiv。 | 引用 Pérez García–Fetter Nathansky 的 Lipschitz 回缩引理。 | 是同一方法引用链的旁证，不是新增 \(\gamma<1\) 精确模先例。 |
| **Wolf-Jürgen Beyn，*On Smoothness and Invariance Properties of the Gauss-Newton Method***，NFAO 14 (1993), 503–514；DOI **10.1080/01630569308816536**；[原刊全文](https://noah.nrw/ubbihs/download/pdf/5114560)，Theorems 2.1–2.2、3.1，(2.1)。 | \(F\in C^{k+1}\)、满行秩 regular zero；Gauss–Newton 有共同 \(C\alpha^{2^n}\) 点尾，极限映射 \(C^k\)，等极限纤维光滑。 | 相同初值—极限对象的真实前身，但强满秩光滑结构给良好稳定性，不是坏选择；本稿不满足这些强假设。 |
| **Ruda Zhang，*Newton Retraction as Approximate Geodesics on Submanifolds***；[arXiv:2006.14751v1](https://arxiv.org/pdf/2006.14751)，§2.2、Definition 2.6、Theorems 2.9、2.11。 | 满秩流形方程、Hölder Jacobian 和伪逆控制；Newton 极限及 \(1+\alpha\) 点阶。 | second-order retraction 指测地线近似阶，不等于点误差 Q-二次；无非 Hölder 选择。 |
| **Yitian Qian、Shaohua Pan，*A Superlinear Convergence Framework for Kurdyka-Łojasiewicz Optimization***；[arXiv:2210.12449v3](https://arxiv.org/pdf/2210.12449v3)，H1–H3、Theorems 3.1–3.2、Remark 3.1。 | 充分下降 \(\|\Delta x\|^{p+1}\)、相对次梯度误差 \(\|\Delta x\|^p\)、KL 指数 \(\theta\in(0,p/(p+1))\) 给 Q 点阶 \(p/[\theta(1+p)]\)。 | 纯速率侧先例，不给两个初值的坏选择或本稿完整图／严格兼容合取。 |
| **Shixiang Chen、Yixiao He、Wen Huang，*Retractions by Alternating Projections***；[arXiv:2605.17384v2](https://arxiv.org/pdf/2605.17384v2)，Assumptions 1–3、Proposition 2、Theorems 2–3、Lemma 4.9。 | 光滑流形 clean intersection、投影迭代及切／法导数控制给共同尾与 \(C^1/C^2\) 极限回缩。 | 额外导数结构不由弱 Hölder RL 推出；不提供坏选择和本稿模。二阶回缩仍不是 Q-二次的同义词。 |
| **Dengyu Zheng、Shixiang Chen，*A Regularized Newton-Type Method for Manifold–Affine Intersection Problems under Intrinsic Transversality***；[arXiv:2606.31738v3](https://arxiv.org/html/2606.31738v3)，Assumptions 2、7；Theorems 16、18、26–27。 | Th16 在 \(\mu_k=cr_k^\rho\)、\(0<\rho\le1\) 给至少 \(1+\rho\) 点阶；Th18 估计极限与最近点的差。 | Th26–27 的光滑极限回缩限于 \(\rho=0\)，不能与 \(\rho=1\) 二次率拼接；无目标坏选择。题名及定理号按 v3。 |
| **Paweł Pasteczka，*Iterated Quasi-Arithmetic Mean-Type Mappings***，Colloq. Math. 144 (2016), 215–228；DOI **10.4064/cm6479-2-2016**；[arXiv:1412.2997v1](https://arxiv.org/html/1412.2997v1)，Theorems 1–3、Lemma 4.3、§3.2。 | \(C^2\) 生成元、\(f_i'\ne0\)、\(\lvert f_i''/f_i'\rvert\le K\) 给均值跨度的共同双指数尾。 | Th3 中任意连续 \(\varphi\) 属 \(\varphi\circ M\)，不是极限均值 \(M\) 任意粗糙。AGM 应用的 \(K=1/x_{\min}\) 在坏边界不统一。第二轮由导数积 \(\|D\mathbf A^n\|\le\exp(K\sum_jw(\mathbf A^jx))\) 独立证明固定紧内部域的极限 Lipschitz。 |
| **Paweł Pasteczka，*On the new smoothness class of means and its impact to mean-type mappings***；[arXiv:2406.12491v2](https://arxiv.org/html/2406.12491v2)，Theorem 3.1、(3.1)、结语 7–8。 | 残差均值的方差比极限 \(\operatorname{Var}M^{n+1}/(\operatorname{Var}M^n)^2\)。 | 不是实际点误差比，更无目标坏选择；结语的正则性问题不能当作已证反例。 |
| **Janusz Matkowski、Paweł Pasteczka，*Mean-type mappings and invariance principle***，MIA 24 (2021), 209–217；DOI **10.7153/mia-2021-24-15**；[原文](https://files.ele-math.com/articles/mia-24-15.pdf)，Theorems 1–2、Examples 1–2、Proposition 2。 | 不变均值唯一性和迭代收敛；起始收缩时刻可依初值无界；也有不连续单步而极限良好的例子。 | 不给共同尾与坏极限的当前定量合取。 |
| **Matthew Kvalheim、Shai Revzen，*Reverse-engineering invariant manifolds with asymptotic phase***；[arXiv:1608.08442v1](https://arxiv.org/html/1608.08442v1)，Theorem 1、Proposition 1、§3.2.2、Propositions 6、8、Theorem 2。 | 逆向构造预设光滑相位／submersion；法向支配下扰动相位 \(C^{r-2}\)。一般 NHIM Proposition 1 先只给连续性。 | 不能概括为全篇只研究光滑相位；但 \(C^0\) 保证不是非任意 Hölder 的存在反例，也没有目标模。该原文缺口已在第二轮关闭。 |
| **Alina Luchko、Igor Parasyuk，*On asymptotic phase of dynamical system hyperbolic along attracting invariant manifold***；[arXiv:1810.00268v1](https://arxiv.org/pdf/1810.00268v1)，Theorem 1、§4。 | \(C^2\) 向量场、紧吸引不变流形和双曲结构保证渐近相位与连续叶族。 | 相位跟随运动轨道，不是共同点尾下收敛到静止解；无两个精确模及有限图构造。 |
| **Alexandre Mauroy、Igor Mezić，*Extreme phase sensitivity in systems with fractal isochrons***，Physica D 308 (2015), 40–51；DOI **10.1016/j.physd.2015.06.004**；arXiv:1408.2363；[作者稿](https://orbi.uliege.be/bitstream/2268/182791/1/fractal_iso5_submitted.pdf)，§IV (9)–(16)、Appendix A；无对应编号定理。 | 平均相位敏感性 \(\langle f(x,\varepsilon)\rangle\sim\varepsilon^{N-D}\)，分形等时相。 | 无相位集上相位不定义，靠近它过渡时间不一致；不等于共同邻域连续极限选择的最坏两点模。 |
| **Jorge Antezana、Enrique R. Pujals、Demetrio Stojanoff，*The iterated Aluthge transforms of a matrix converge***；[arXiv:0711.3727v1](https://arxiv.org/pdf/0711.3727v1)，Theorem 4.3.1、Proposition 5.1.1、Theorem 5.2.4、§6.1。 | 迭代收敛；极限在单位矩阵邻域不能 \(C^1\)，在可逆矩阵上连续；指数速度依赖谱。 | 非 \(C^1\) 远弱于非任意 Hölder；谱退化附近没有所需共同尾，不给目标模。 |
| **Jonathan M. Borwein、Guoyin Li、Matthew K. Tam，*Convergence rate analysis for averaged fixed point iterations in the presence of Hölder regularity***；[arXiv:1510.06823](https://arxiv.org/pdf/1510.06823)，Theorem 3.3、Corollaries 3.8–3.10。 | averaged／quasi-cyclic 迭代、Hölder EB 给多项式或线性轨道率。 | Hölder 修饰的是 EB，不是单步弱连续性；没有目标极限选择模。 |
| **R. A. Poliquin、R. T. Rockafellar，*Prox-Regular Functions in Variational Analysis***；DOI **10.1090/S0002-9947-96-01544-9**；[作者全文](https://sites.math.washington.edu/~rtr/papers/rtr157-ProxRegular.pdf)，Theorems 3.2、4.4、Proposition 4.3。 | attentive localization、弱单调和小参数给单值局部 Lipschitz proximal，联系子微分 resolvent 与 argmin。 | 不是本稿退化平方根 resolvent；本稿也未证明自己的 \(F\) 是某势函数子微分。 |
| **Minh N. Dao、Matthew K. Tam，*Union Averaged Operators with Applications to Proximal Algorithms for Min-Convex Functions***；DOI **10.1007/s10957-018-1443-x**；[arXiv:1807.05810v2](https://arxiv.org/pdf/1807.05810v2)，Definition 3.1、Theorem 4.2、Proposition 5.2(b),(f)。 | 有限 averaged 分支、active selector、min-convex proximal 的有限并与局部收敛。 | 分支数主要约束迭代映射；本稿是 \(F\) 两值、\(J_F\) 单值且分数阶，无该下界及兼容常数。 |
| **Brecht Evens、Pieter Pas、Puya Latafat、Panagiotis Patrinos，*Convergence of the Preconditioned Proximal Point Method and Douglas–Rachford Splitting in the Absence of Monotonicity***；DOI **10.1007/s10107-024-02182-0**；[arXiv:2305.03605v2](https://arxiv.org/pdf/2305.03605v2)，Theorems 2.13、3.6。 | oblique weak Minty、次正则、连续广义 resolvent 给线性收敛，含 piecewise-polyhedral 非单调 DRS。 | 不给 cap 图的分数阶全对常数、坏选择下界或目标合取；“非单调 PPA”标签不足以判同。 |
| **Guoyin Li、Boris S. Mordukhovich，*Hölder Metric Subregularity with Applications to Proximal Point Method***；DOI **10.1137/120864660**；[作者预印本](https://optimization-online.org/wp-content/uploads/2012/02/3340.pdf)，Theorems 7.2–7.3。 | 最大单调 PPA、Hölder EB 与距离速率。 | resolvent 非扩张，其已存在极限继承非扩张；无坏选择。该文 \(q\) 为 EB 阶，不能当新稿的实际距离因子。 |

### D6．可安全保留的最小贡献，与禁止主张清单

当前可保留、并值得作为研究稿主体的最小包是：

1. 在共同局部化区域与共同点尾假设下，对仅 \(\gamma<1\)-Hölder 的单步迭代给出两个**精确显式量级**；承认截断方法已有，不将方法本身称新。
2. 在每个固定实际 \((\gamma,q)\) 类内构造严格兼容、完整闭图至多二值实现，达到 \((\log\log/\log)^\beta\)；半代数实现按有理幂限定。由实际轨道下界说明 \(\log\log\) 不能删，不只是优化一个上界包络。
3. 在共同超几何尾下达到 \(e^{-\Theta((\log(1/\delta))^\alpha)}\)，从而 \(\alpha\) 不能提高；二次特例在坏参照轨道自身仍 Q-二次，并与邻域两点非 Hölder、非半代数选择和严格完整 RLEB 接口同时成立。

即使将来 U1 证实抽象上界是旧一般定理的特化，第 2–3 项也必须单独判断；不能一并宣告已知。反之，没找到精确抽象先例也不能使逆图编码、AGM 宽泛现象或高阶收敛组件变成全新。

以下主张本轮不予支持：

- “首次研究初值到最终解”“首次快速半代数迭代有非 Hölder／非半代数极限”“全新截断原理”“首次将迭代写成 resolvent”。
- “全部实指数族均半代数”“\(F\) 每点恰二值或全域非空”“已经实现某函数的 \(\operatorname{prox}_f\)”；目前是算子 inclusion 意义的 PPA。
- “原 A1–A4 自动保证完整 \(J_F\) 单值”“selection-uniform 收敛自动给连续初值选择”。
- “固定保守 \(\kappa\) 的最差模已尖锐”“有限 \(R\) 的 \(L_R\) 已最小”“超几何指数前常数已最优”“\(\Theta\) 已证明归一化极限”。
- “固定解点不 Hölder calm”“极限不连续”“所有 signed-Schur 图块均已由三角命题解决”“非半代数等于任何 o-minimal 结构都不可定义”。
- “AGM 的所有改造均不可能满足严格 RLEB”或“AGM 只是少一个条件，所以本稿必然重大创新”。本轮只排除已明确算出的直接编码。
- “已证明全球首次”或根据本次有界优先权检索直接保证录用／期刊层级。

## 五、仍未解决

### U1．最直接的旧一般命题原页未取得

**Yoav Benyamini、Joram Lindenstrauss，*Geometric Nonlinear Functional Analysis, Volume 1***，AMS Colloquium Publications 48 (2000)，**Proposition 1.10**。[AMS 书目](https://www.ams.org/books/coll/048/)和 Wiśnicki 的直接引用已定位，但命题及证明原页未取得。

待核问题不是“书里有没有类似词”，而是该命题是否允许任意有限步连续模和尾函数，是否已直接涵盖或显式算出本稿两种量级。不能因为 Wiśnicki 只使用 Lipschitz 版本，就推断书里也只有 Lipschitz。此缺口限制抽象定理的首创强度，不否定 B1 的正确性，也不自动覆盖构造下界。已遇访问限制，没有绕过；需合法取得原页再关闭。

### U2．Li–Mordukhovich–Zhu 正式刊本与公开 v1 的增改、编号未闭合

对应 DOI **10.1287/moor.2024.0570**。本轮实质核查依据为 **arXiv:2406.13207v1**。正式 PDF 入口未返回可读正文，故不能断言正式终稿绝无新增极限映射内容，也不能把 v1 的定理号写成已核刊本号。公开 v1 的逐定理对应仍有效；这个缺口既不是发现相同先例，也不是首创证据。

### U3．部分相位／回缩引用链仍缺原始全文

**Carmen Chicone、Weishi Liu，*Asymptotic phase revisited***，J. Differential Equations 204 (2004), 227–246；以及 **Flaviano Battelli、Kenneth J. Palmer，*Smoothness of Asymptotic Phase Revisited*** 的原文未完整取得。当前没有可据以裁定的定理号、假设全表和覆盖结论；DOI/arXiv 未在本轮证据中核准，不编造。它们是未排除入口，不是已经发现或已经排除的精确先例。

Kvalheim–Revzen **arXiv:1608.08442v1** 的旧缺口已在第二轮关闭，不再列为“未取得原文”。其他未取到的来源也不能靠摘要或题名完成定理级判断。

### U4．超出已证范围的数学／优先权问题

固定保守 \(\kappa\) 类别的同量级锐性、超几何最优前常数、一般 signed-Schur 的极限稳定性、AGM 的所有有限维增强实现都未被本稿或本轮解决。它们不是现有主结果成立所必需的新假设，不应为了继续推进当前稿件而强迫另造新理论；也不能写入已证摘要。

同样，本轮没有穷尽所有均值迭代、非光滑动力系统、Newton 吸引域及渐近相位文献。`NO-EXACT-PRIOR-FOUND` 的外延就是列明的原文与引用链；阴性检索不构成世界范围的否定证明。

### U5．稿件修补尚未实际落实；数学通过不等于立即投递

本次授权是审计，不是改稿。本报告给出了充分修补，但原文件尚未修改。下一版至少应落实 R1–R6，并在摘要中使用 D6 的限定贡献口径；随后只需对改动接口、主张和引用做针对性复核，无须重审无关原 RLEB。

**最终直接回答：**

- **主结果成立吗？** 在 R1 的明确修补后成立；两个显式完整 proximal 构造本身不需更换，两个连续模、匹配下界、点误差 Q-二次与非半代数结论均保留。正式数学标签为 **`ABC_PASS_AFTER_REPAIR`**。
- **是否全部已知？** 不是。本次没有发现覆盖精确联合包的同一定理或构造；但方法、编码和宽泛坏选择现象有必须承认的先例。
- **是否已经证明首创？** 没有。尤其 U1、U2 仍未关闭，不能发放无保留的全球首创认证。
- **修改后能否作为研究稿继续推进？** **可以。** 应以“精确最坏模及严格完整 RLEB 类内的尖锐实现”为主线推进，补齐接口与相关工作；当前不应因局部先例否定整体，也不应把有限检索当成已获投稿／录用许可。
