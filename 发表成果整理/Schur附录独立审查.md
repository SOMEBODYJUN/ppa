# 第5节与 signed-Schur 附录独立审查

审查日期：2026-10-11。仅解析审查当前 `RLEB/sections/native_schur_verifier.tex`、`appendix_signed_schur.tex`，以及 `theorem_spine.tex` 的 RL 定义、J 侧等价形式、全对图块充分条件与推论。未读取历史稿、其他评审或根规范状态；未修改论文，未编译。审查依据为指定 academic-writing-skills 的数学证明审查与问题分级要求。

**结论：核心 signed-Schur 证明在其限定图块上成立；覆盖、排他、全点对模量与显示常数均可重建。当前有三处需要明确的假设/量词作用域，不能把结果读成任意所表示输入块或完整算子图上的无条件结论。** 下述问题均为 open；没有发现 S3/S4 级核心计算错误。本结论不构成全稿或投稿就绪认证。

## 一、已经核实的数学范围

令

\[
\mathcal G_{\mathrm{rep},r}
=\left\{g_\sigma(a,t):\|a\|\le R,\ 0\le t\le T,
\ PX_\sigma(a,t)\in B_r^{n-1},\ \sigma=\pm1\right\}.
\]

在 (S1)–(S6) 和 \(0<r<\mu R-HT\) 下，核实的结论是：

1. 所表示图覆盖 (S7) 的开输入域 \(U\)。这是一个包含输入缝 \((z,\nu(z))\) 的 collar；\(\nu\) 为 \(C^1\)，因此 \(U\) 确实开放。
2. \(\mathsf X\) 在 \(\mathcal G_{\mathrm{rep},r}\) 上排除碰撞，包括异支与缝端点。这里的唯一性属于所表示图，不自动属于完整 \(\operatorname{gph}F\)。
3. (S9) 对 \(\mathcal G_{\mathrm{rep},r}\) 的所有点对成立，同支与异支均已覆盖；无需把点对限制为与解的锚定比较。
4. (S10) 只把这些结论转移给 \(\mathcal G\cap\mathsf X^{-1}(U)\)。要获得完整 \(J_{\lambda F}\) 在 \(U\) 上的结论，必须在 \(U\) 上有完整算子纤维等式，而不能仅有图块包含关系。

这与 `theorem_spine.tex:19–86, 317–341, 372–398` 的 RL 定义、J 侧形式及完整图桥接条件一致。

## 二、明确问题

### SS-1：图值条件与邻域上的 C1 延拓必须分开陈述

- **定位：** `appendix_signed_schur.tex:25–32`；应用为 `:349–353`。
- **分级：** scope = validity/semantic；severity = S2；evidence = confirmed；status = open。
- **问题：** 定理目前说两张 graph parametrizations “are defined on a neighborhood of their displayed parameter domains and take values in gph F”。若 `take values` 也量化到该邻域，则 square-root 应用不满足假设。需要的实际假设应是：映射有邻域上的 \(C^1\) 延拓，但只有显示的闭参数域被要求落在图中。
- **验证：** square-root 参数在 \(t\ge0\) 有对偶变量第一分量 \(v_\xi(t)=-2t\)。任何经过缝点的图值延拓都须有 \(v_\xi(t)=-2\sqrt{u_y(t)}\le0\)。当 \(t<0\) 时，\(v_\xi(t)/t\ge0\)，故左导数不能等于右导数 \(-2\)。因此不仅显示的多项式延拓在负 \(t\) 不落于图中，任何图值 \(C^1\) 双侧延拓都不可能满足该缝导数。
- **修复：** 明写“two C1 maps defined on a neighborhood … whose restrictions to the displayed parameter domains take values in gph F”。证明所用的 IFT 只需要前者，图像结论只需要后者；不必加强应用。

### SS-2：(S10) 不能将结论转移到 U 外的局部化纤维

- **定位：** `appendix_signed_schur.tex:107–119`，尤其 `:116` 的 “then all conclusions apply to that localization of F”。第5节 `native_schur_verifier.tex:61–65` 的范围提醒方向正确。
- **分级：** scope = semantic/section；severity = S2；evidence = confirmed；status = open。
- **问题：** (S10) 的等式只在 \(\mathsf X^{-1}(U)\) 上成立，而第2、3项原本量化到整个 \(\mathcal G_{\mathrm{rep},r}\)，其法向坐标范围可能比 \(U\) 大。“all conclusions apply to that localization” 若按整个 \(\mathcal G\) 读取，就过强。
- **验证反例：** 取 \(n=2,\lambda=1,R=2,T=1,r=1\)，规定所表示枝的 Minty 坐标
  \[
  X_\pm(a,t)=(a,\pm t^2),\qquad Y_\pm(a,t)=(a,t).
  \]
  由 \(u=(X+Y)/2,v=(X-Y)/2\) 定义算子图。可取 \(\mu=1,H=B=0,K_z=K_+=K_-=1,h_\pm=t^2\)，而 \(U=(-1,1)^2\)。向 \(\mathcal G\) 加入两个图点，均有 \(X=(0,2)\)，但分别有 \(\mathsf Y=(0,0)\) 与 \(\mathsf Y=(0,1)\)。这不改变 (S10)，却在切向输入 \(0\in B_r\)、法向输入位于 \(U\) 外处制造碰撞，并使任何全对 RL 失败。
- **修复：** 将转移对象明确为 \(\mathcal G\cap\mathsf X^{-1}(U)\)，或说“all corresponding conclusions over U”。完整 resolvent 的结论也只指该输入域。

### SS-3：power 与 matched-jet 的 input block 必须继承切向域限制

- **定位：** `appendix_signed_schur.tex:230–234, 264–274`；对应第5节 `native_schur_verifier.tex:47–48`。
- **分级：** scope = validity/quantifier；severity = S2；evidence = confirmed；status = open。
- **问题：** “On every represented input block” 没有重申 (S9) 的切向输入 \(B_r^{n-1}\) 限制。定理前件虽然在完整参数域一致成立，但只保证 \(B_r\) 上的共同切向反演；全参数域的像不能自动满足同一全对 RL。matched-jet 的附加条件本身也只量化到 \(z\in B_r\)。
- **验证反例：** 取 \(R=2,T=1,\mu=H=1,r=1/2\)，令 \(q(z)=2\max\{z-2,0\}^2\)，并规定
  \[
  X_+(a,t)=(a+t,t^2),\quad X_-(a,t)=(a+t,q(a+t)-t^2),
  \qquad Y_\pm(a,t)=(a+t,\pm t).
  \]
  这给出 \(C^1\) 图参数；在 \(|a|\le2,0\le t\le1\) 上共同缝成立，且可取 \(B=4,K_z=K_+=K_-=1,h_\pm=t^2\)。两支 signed Schur 导数恰为 \(2t\)。然而在 \((a,t)=(2,1/2)\)，两枝输入都为 \((5/2,1/4)\)，而 \(Y\) 相差 \((0,1)\)。包含此输入的所表示块即使直径为零也不满足任何全对 RL。碰撞在 \(B_r\) 外，不反驳原定理，恰好说明不能省去其量词限制。
- **修复：** 明写输入块来自 \(\mathcal G_{\mathrm{rep},r}\)，或来自满足完整纤维等式的 \(U\)。更直接的表述是：对每个 \(D>0\)，\(\mathcal G_{\mathrm{rep},r}\) 在输入对距尺度 \(D\) 上满足所给 RL 常数；此说法不要求整个图块的直径都不超过 \(D\)。

## 三、计算与边界核查

| 项目 | 核查结果及理由 |
|---|---|
| 切向覆盖 | (S2) 沿线段积分给出强单调性。边界内积严格正，Brouwer 自映射论证有效；零点在开球内。\(\|f(0,t)\|\le HT\) 与半径余量使用正确。 |
| 反演与排他 | \(\operatorname{sym}A\succeq\mu I\) 保证 \(A\) 可逆；(S12) 的链式公式正确。固定 \(z\) 时正枝严格增、负枝严格减，即使 \(h'(0)=0\) 也因 \(h\) 严格增而排他。 |
| 凸增量 (S14) | 有效。对 \(q=t-s\)，\(h(t)-h(s)=\int_0^q h'(s+\tau)d\tau\ge\int_0^q h'(\tau)d\tau=h(q)\)。只用到了已给出的凸性及 \(h(0)=0\)。 |
| 同支点对 | 将法向差分在同一个切向坐标上比较，再用 \(B\|z-w\|\)；\(h_\sigma(|t-s|)\le C_Bd\)。单支分配 \((|t-s|,0)\) 或 \((0,|t-s|)\) 在 (S8) 中可行。 |
| 异支点对 | \(h_+(t)+h_-(s)\le C_Bd\) 的方向正确。经共同缝得到 \(K_+t+K_-s+K_z\|z-w\|\)，包含两个有序异支方向及缝端点。 |
| 全点对模量 | \(|\Delta n|+B\|\Delta z\|\le\sqrt{1+B^2}\,d\) 给出正确的 \(C_B\)。\(V\) 的可行域非空紧，随预算嵌套；两 \(h\) 严格增保证 \(V(0)=0,V(v)\to0\)。能量恒等式中的 \(1/2\) 正确。 |
| power 常数 | Hölder 对偶范数给出 \(V(v)\le C_pv^{1/p}\)；乘上 \(C_B^{1/p}=(1+B^2)^{1/(2p)}\) 正确。\(p=1\) 用 \(\max\{K_+/c_+,K_-/c_-\}\) 正确。 |
| 不同枝幂次 | \(t^{p_\sigma}\ge T^{p_\sigma-p}t^p\) 正确，足以在分配约束中得到该常数。这里是在比较积分增长函数；不应另外声称 (S6) 的原导数必然支配 \(p c_\sigma T^{p_\sigma-p}t^{p-1}\)。当前证明没有作此错误推断。 |
| matched jet | 同支界保持有效。异支通过较小参数的 mismatch 给出 \(K|t-s|+E\min\{t,s\}^p\)，再用 \(|t-s|\le(C_Bd/c)^{1/p}\) 与 \(\min\{t,s\}^p\le C_Bd/(2c)\)。\(1/(2c)\)、\(K=\max K_\sigma\) 和 \(D^{1-1/p}\) 均正确。 |
| jet 导数条件 | 对相同 \(z\) 从共同缝积分即可得到 \(Et^p\)。两枝导数须在各自 corrected parameters 上评价；当前文字已准确说明。 |
| 指数排他 | 固定切向输入的弧上，\(d\le Ct^p\) 与 \(\|\Delta Y\|\ge ct\) 排除任何 \(\theta>1/p\)。当 \(p>1\)，\(2\|\Delta u\|\ge ct-Ct^p\) 排除所表示单值 resolvent 的 calmness。该断言应始终读取为相关弧和缝点所属的同一局部化。 |
| square-root 例 | \(K_+=4\sqrt{1+T^2},K_-=4\sqrt{1+9T^2}\) 正确；基础常数为 \(\sqrt D+\sqrt{8+40T^2}\)。配对 mismatch 为 \((0,-8t^2)\)，故 \(E=8\)，jet 常数为 \(2\sqrt D+2\sqrt{1+9T^2}\)。完整纤维由 \(t<T,|a|<r+2T<R\) 确实得到。 |
| 渐近最优性 | 缝到正枝弧的 RL 比值为 \(\sqrt{16t^2+4t^4}/\sqrt{4t^2}=\sqrt{4+t^2}\to2\)，给出下界；jet 上界趋于2，故在含缝及非平凡该弧的收缩邻域上成立。并不是任意远离缝的子块都具有最优常数2。 |
| orientation 反例 | \(X_+=X_-=t^2,Y_\pm=\pm t\) 确实有同输入不同输出，枝上最优 \(1/2\) 逆模量不能拯救并图。可与切向直线作乘积得到 \(n=2\) 版本；反例无需满足主定理所有前件。 |
| 切向一致性反例 | \(X(a,t)=(a,t^3-at)\) 在任意小 \(a>0\) 的 \(t=0,\sqrt a\) 有输入碰撞，\(Y(a,t)=(a,t)\) 区分图点。它正确否定“单个缝点的 Taylor law 足够”的推断。 |

## 四、两个低级别接口提醒

1. **S1 / semantic / confirmed / open：** matched-jet 是另一个有效常数，不保证对所有参数都数值更小。\(p=1\) 时新常数为基础常数加 \(EC_B/(2c)\)，所以不会严格改善；\(p>1\) 且两 \(K_\sigma>0\) 时，主导 \(d^{1/p}\) 系数才严格低于基础的对偶范数系数。`appendix_signed_schur.tex:253` 与第5节 `:58–59` 宜避免把所有 \(p\ge1\) 的替换读成无条件 improvement。square-root 所声称的渐近改善本身正确。
2. **S1 / section / confirmed / open：** 与图块收敛推论连接时，不能仅写“再验证残差误差界”就认为前件已经齐备。`theorem_spine.tex` 的 (A1) 还要求同一图块包含每个所用输入的最近零点锚 \((p,0)\)；(A3) 的真残差评价窗、(A4) 的统一兼容和留域预算也仍须验证。第5节 `:67–72` 是简述，未作错误定理断言，但可补一句列明这些余下条件，防止将 signed-Schur 误读为独立的 PPA 收敛定理。

## 五、审查完整性回顾

- **已覆盖：** 指定第5节与附录全部正文、覆盖/唯一性/全点对几何、一般凸增长、power 与 mixed-power 常数、matched jet、指数排他、三个例子及与指定 RL 图块充分条件的接口。
- **权威及约束：** 使用指定当前文件；未借入历史稿、其他审查或未给出的全图条件。论文无改动。
- **对齐：** 核心数学链条成立；完整纤维转移域、图参数延拓域、后续常数量词需明确。残差条件与最近零点锚不由 Schur 数据自动产生。
- **方法及适用性：** 数学解析复核与反例攻击；未使用数值实验作为普遍结论依据。
- **未做/不适用：** 外部文献与新颖性调查、全稿引用/编号/语言审查、编译与版面核查均不在本次授权范围；未标记通过。
- **未解决问题：** S2 三项；S1 两项；S3/S4 未发现。审查可用于限定范围的数学修订；不能据此宣布全稿 ready。

本次读取版本的 SHA-256：

| 文件 | SHA-256 |
|---|---|
| `native_schur_verifier.tex` | `ef81577773927dbf77b02f662e147fe9612d69fefd2f2a0eaf48ff69b6c576f4` |
| `appendix_signed_schur.tex` | `9927b4006234fa5f435d831a8583c426311906ba8288a60894516f97cea829d2` |
| `theorem_spine.tex`（仅指定部分经过审查） | `dbf112109e61a608d45f7f715cf548b1de87ae865ee8d4a2118192023c5ba8fb` |

## 六、修订回归复查（2026-10-11）

本轮只读取当前两份 TeX，复查此前三项 S2、两项 S1 的修订，以及修订与此前已重建证明的衔接；没有重新审查其他章节、历史版本或项目规范。上文的 open 状态与 SHA 是首轮记录，以下为这些问题的当前状态。论文未修改，未编译。

**回归结论：五项均 closed；未发现由本轮修订引入的实际新问题。** 核心结论仍限于切向输入在 \(B_r^{n-1}\) 的所表示图；(S10) 的结论转移仍只发生在 \(U\) 内。完整 \(J_{\lambda F}\) 的结论仍须完整算子纤维等式。

| 首轮问题 | 当前状态 | 当前定位与复查证据 |
|---|---|---|
| SS-1：邻域延拓与图值条件 | **closed** | `appendix_signed_schur.tex:25–34` 已将邻域上的 \(C^1\) 映射延拓与显示参数域上的图值条件分开。该延拓足以支持 `:142–148` 的参数化 IFT；所有 Schur 条件及积分仍只在显示域内使用。square-root 多项式参数因而满足修订后的延拓要求，无需不可能的双侧图值延拓。 |
| SS-2：(S10) 的转移输入域 | **closed** | `appendix_signed_schur.tex:109–122` 明确把 covered-input 结论转移到 \(\mathcal G\cap\mathsf X^{-1}(U)\)。这正是 (S10) 能供应的等式范围，且不再声称 \(U\) 外的局部化纤维也排他。`native_schur_verifier.tex:62–66` 保持完整图桥接限制。 |
| SS-3：power/jet input block 的切向限制 | **closed** | `appendix_signed_schur.tex:233–234, 275–276` 均明确要求切向输入在 \(B_r^{n-1}\) 且直径不超过 \(D>0\)。因此这些常数严格继承 (S9) 的点对域；\(d\le D^{1-1/p}d^{1/p}\) 的使用保持有效。第5节 `:35–48` 在已覆盖 \(U\) 的上下文中陈述 input block，\(U\) 自身满足切向限制。 |
| S1：matched-jet 不保证总是改善 | **closed** | 命题标题 `appendix_signed_schur.tex:257` 改为 estimate；`:281–283` 明确说明常数为 alternative，并将主导系数的严格改善限于该命题共同 \(ct^p\) 假设下的 \(p>1,K_+,K_->0\)。此时 \(\|(K_+,K_-)\|_{p'}>\max\{K_+,K_-\}\)，所以改善断言有直接依据。第5节 `:58–60` 与此限定一致；square-root 渐近改善计算仍成立。 |
| S1：收敛接口的余下条件 | **closed** | `native_schur_verifier.tex:68–72` 已分别指出残差误差界、同一图中的最近零点锚、真残差评价窗、标量兼容与严格初值长度预算。该文字与首轮查明的图块充分条件接口相接，不再暗示只补一个误差界就能调用收敛定理。 |

本轮修改未改变 \(V\)、\(C_p\)、\(C_B\)、(S15)、(S17) 或 square-root 常数的公式；其已核实推导不因这些域与措辞修订失效。证明中的切向反演、共同缝、同支凸增量、异支分配及能量恒等式仍在同一个获准点对域内衔接。首轮两项范围反例现在都落在明示结论域之外，不再与当前陈述冲突。

本轮当前 SHA-256 已实际计算，并与指定目标 SHA 完全一致：

| 文件 | 当前 SHA-256 |
|---|---|
| `native_schur_verifier.tex` | `b8688f14343c6aecc42ee8cac4b6f79b67121d61f1157f339b47a16fbccff036` |
| `appendix_signed_schur.tex` | `961e5657ac8c59f0e5327b95f4b2006ae8c7606433cabe7720f165854585010e` |

**本轮完整性回顾：** 指定五项修订及其证明衔接已覆盖；原数学范围和常数保留；本轮 open 项为零，新实际问题为零。仅可报告这五项在以上当前版本已关闭；外部文献、其他章节、全稿回归、编译及版面未做，不能据此宣布全稿就绪。
