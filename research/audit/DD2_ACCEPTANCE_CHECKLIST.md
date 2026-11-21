# DD1–DD2 最终验收清单

**当前认领** `待认领`

这是当前主任务的工作清单，也是最终应交给作者的完整答卷。题面来自[作者原协议](../topics/dd2/DD2_FINAL_ACCEPTANCE_PROTOCOL.md)。225 项主问题与交付物保留原文及次序，55 项明确补列公式检查、恢复类别、分支审查等原协议义务。每项有自己的勾选框。以前的[总索引及分节审计](FINAL_PROTOCOL_MASTER_2026-11-21.md)只提供复核所需证据。新会话先读 [GPT Pro 开工提示词](DD2_PRO_START_HERE.md) 的核心说明并完成自检，再继续首个未勾项。

## 逐项执行

1. 恢复并安全同步 PPA 仓库。通读原协议的假设、公式、质量要求及 README、RESEARCH_STATE、CLAIMS、FAILED_ROUTES。运行 `git fetch origin main` 和 `python3 research/code/dd2/verify_acceptance_checklist.py`。认领第一项未勾任务，把顶部「当前认领」改为该编号。每次只认领一项。可以研究当前项需要的后续依赖，勾选仍按清单顺序。
2. 写出当前题的精确数学问题和答案，核对原量词、适用域和边界。成立须有完整证明；不成立须有严格反例或足以裁决原问题的精确错误证明；文献须定位一手证据；交付物须实际完成且可复核。原题若要求条件或分类，必须给出原范围内该问要求的条件及证据。复用旧证明时逐项独立核对，引用到具体正文，必要时补证明或反例。
3. 在该项下面填写四个字段，以本页为答卷。裁决只接受 `Proved`、`Sharp`、`Strict Extension`、`Equivalent / Recovered`、`Refuted`、`Invalid`、`Verified` 或 `Delivered`。末两种用于经过核实的文献或审查事实及实际交付物。合理的附加条件须写在结论和证明里。用以下缩进格式填写，证据链接相对于此 Markdown 文件。

   ```markdown
     - **裁决** Proved
     - **结论** 写出对原题的完整答案和适用范围
     - **证据** [证明](../topics/dd2/core.md#dd2-reverse)
     - **复核** 写出已重构的关键推导、核实的边界和对异议的裁决
   ```

4. 有了完整证据才打勾，并把顶部恢复为「待认领」。把这一项的答卷和证据一起暂存，运行 `python3 research/code/dd2/verify_acceptance_checklist.py --staged`。以 `DD2 <编号>: <实质结果>` 为标题单独 commit。push 后再次 fetch，确认该项及证据已进入远端 `main`，才能认领下一项。提交标题由 Git 记录，按题号可以定位相应提交。
5. 若缺证明，继续研究当前题。可以换路线或严谨地证伪，不能换掉原问题。仅有 `Open`、`Partial`、候选、未排除的致命异议、链接指向概述，或缺少同量词证据时，当前框保持未勾。必要时做保留该认领编号的中途 checkpoint，恢复后继续同一项。
6. 全部勾完后，执行 `git fetch origin main` 和 `python3 research/code/dd2/verify_acceptance_checklist.py --final`。逐项复核实际数学证据，把**远端完整清单（所有题号、勾选、结论、证据与复核）**原样作为最终答卷交还作者，同时给出最终提交。中途暂停只能报告当前题号、已勾数量和具体研究进展。脚本检查任务覆盖、记录格式、证据文件与单项提交历史；数学验收依赖每项的证明、反例和复核。

## §1 DD2 的数学身份是否已经完全固定？

- [x] `S01.01` DD2 究竟削弱了 A、B 中的哪一个？是否同时推广了二者？
  - **裁决** Proved
  - **结论** DD1 和 DD2 都允许一般有符号零锚函数 \(\Phi\)。DD1 讨论稿在线性输出真误差界下给出统一比例的 A 与输入型 \(B_\Phi\)。DD2 从把 A 改为指定的逐尺度目标 \(a\le\varphi(t)\) 出发，再反推允许的锚定缺陷或所需的误差界强度。DD2 允许一般输出真残差误差界 \(\psi\)，而 C400 固定 \(\ell\) 算出了精确反演特例。C401 在一般 \(\psi\) 下用附加耗散和可积性获得同一步长度势。如果 B 特指原稿 \(s\le B_\omega(t)\) 或 DD1 的 \(s\le B_\Phi(t)\)，该输入步长根界仍由 \(\Phi\) 决定。输出误差界 \(\psi\) 是另一项前提。老师提出的 \(s\le C a\) 另有自身量词。
  - **证据** [原 A 与输入 B 的定义](../canonical/ppa_ab_necessary_bounds.md#ab-scope)、[DD1 作者讨论稿第七及十三节](../manuscripts/dd1_2026_11_20/DD1_2026-11-20_教师讨论稿.md)、[C400 固定线性误差界反演](../topics/dd2/core.md#dd2-reverse)、[C401 一般误差界和长度势](../topics/dd2/core.md#dd2-general-gauge)。
  - **复核** 固定 \(L=\ell/\lambda\)，C400 逐尺度只把目标 \(r\) 换成 \(A(t)/t\)，没有改变输出误差界及同一输入锚。取 \(A(t)=\kappa t\) 即为统一比例版本。锚定内积展开后仍给 \(s^2-ts+\Phi(t)\le0\)，与 \(\psi\) 无关。C401 则用 \(t\le a+s\le s+\psi(s/\lambda)\) 得到位移下界，再与平方能量配合推导长度势。两条推导明确区分 A、输入步长上界和输出误差界。
- [x] `S01.02` DD2 的一般下降函数与旧 A 的固定收缩因子之间是什么关系？
  - **裁决** Proved
  - **结论** 旧 A 是 \(A(t)=\kappa t\) 的特例。在共同距离窗 \(0<t\le R\)，给定下降函数 \(A\) 能由某个统一 \(\kappa<1\) 控制，充要条件是 \(\sup_{0<t\le R}A(t)/t<1\)。DD2 允许 \(A(t)<t\) 而该上确界为 1。这里判断的是从指定比较曲线能否推出统一比例，固定算子的实际率有时更强。
  - **证据** [C400 的目标比率和旋转取等例](../topics/dd2/core.md#dd2-trajectory)。
  - **复核** 逐尺度除以 \(t>0\) 即得上确界条件。取 \(A(t)=t/(1+t)\)、\(L=\lambda=1\) 和旋转角 \(\cos\theta(t)=(1+t)/2\)。余弦定理给 \(s=a=A(t)\)，径向严格增的完整近端使 \(r_F(y)=a\)，且锚定内积为 \(t^2/2-a^2\)。实际比率 \(a/t=1/(1+t)\to1\)，所以在线性真误差界仍取等时，也有任何统一 \(\kappa<1\) 都失败的 DD2 算子。
- [x] `S01.03` DD2 的步长控制究竟是一般函数包络，还是直接的有限长度耗散不等式？
  - **裁决** Proved
  - **结论** DD2 保有输入型逐步上包络 \(s\le B_D(t)=(t+\sqrt{t^2+4D(t)})/2\)，对有符号下界可用较精确的 \(B_\Phi\)。在有限长度层，可以用上包络加可和的比较迭代，也可以由 C401 的净耗散直接得到 \(s\le(2/\delta)[\Theta(t)-\Theta(a)]\)。下降 \(a\le A(t)\) 与这两个长度充分机制分别判定。
  - **证据** [C400 输入步长与轨道例](../topics/dd2/core.md#dd2-trajectory)、[C401 同一步耗散和积分势](../topics/dd2/core.md#dd2-general-gauge)。
  - **复核** 在 C401 的前提下，\(s\ge\chi(t)\) 及 \(t^2-a^2\ge\delta s^2\) 给 \(s\le(t^2-a^2)/(\delta\chi(t))\le(2/\delta)\int_a^t u/\chi(u)\,du\)，第二步用 \(\chi\) 非减。反之，仅用 C400 的 \(A(t)=t/(1+t)\) 取等实例，沿真实轨道 \(s_k=t_{k+1}=(k+1+t_0^{-1})^{-1}\)，总长发散。
- [x] `S01.04` DD2 对算子 `F`、目标集 `S`、近端参数 `\lambda`、投影点、合法近端对有哪些精确要求？
  - **裁决** Proved
  - **结论** 普通 DD2 固定欧氏空间 \(H\)、关系 \(F:H\rightrightarrows H\)、闭非空 \(S\subseteq F^{-1}(0)\)、\(\lambda>0\)、开集 \(U\) 及 \(R>0\)。对 \(x\in U_R=\{x\in U:d(x,S)\le R\}\) 和每个 \(y\in\mathcal J(x)\subseteq\{z:x-z\in\lambda F(z)\}\)，要求某个 \(p\in P_S(x)\) 满足同边锚定下界，并在实际输出上核 \(a\le\psi(\inf_{v\in F(y)}\|v\|)\)。一步版只量化已有边；轨道版另要求 \(\mathcal J(x)\ne\varnothing\) 和留域。若输出误差界局部有定义，需对实际 \(y\)、\(r_F(y)\)，以及使用单调比较时的 \(s/\lambda\)，逐一检查评价窗。
  - **证据** [对象、复合图与误差域](../canonical/ppa_ab_necessary_bounds.md#ab-scope)、[C400 基本量词](../topics/dd2/core.md#dd2-reverse)、[C401 工作窗及留域预算](../topics/dd2/core.md#dd2-general-gauge)、[C414 有符号正尺度版本](../canonical/dd2_general_phi_exact.md)。
  - **复核** 边包含式给实际图值 \((x-y)/\lambda\in F(y)\)，所以 \(0\le r_F(y)\le s/\lambda\)，不要求残差下确界达到。锚的距离是输入尺度 \(t\)，误差界使用输出距离 \(a\)。C414 原陈述只取 \(t>0\)。在 C400/C401 的 \(D(0)=0\) 下，\(t=0\) 时唯一最近锚是 \(x\)，锚定内积为 \(-s^2\)，因此只能驻定。有限前缀长度严格小于工作域余量时，下一输入仍在 \(U_R\)，于是可以再次调用覆盖。
- [x] `S01.05` 是所有合法近端输出满足条件，还是只要求存在某个选择？
  - **裁决** Proved
  - **结论** 在所声明的已覆盖关系 \(\mathcal J\) 中，每个受检输入的每个允许输出都须满足两个条件，因而轨道定理量化 \(\mathcal J\) 上的所有选择。若对每个输入只找到一条好边，可以用好边构成非空允许子关系；结论只覆盖这个子关系。当且仅当使用完整关系作允许关系时，定理的量词才覆盖全部原近端输出。
  - **证据** [完整窗与允许图的定义](../canonical/ppa_ab_necessary_bounds.md#ab-scope)、[C400 每边锚条件](../topics/dd2/core.md#dd2-reverse)、[C408 分支及完整残差覆盖](../../CLAIMS.md#c408)。
  - **复核** 取 \(\lambda=1,S=\{0\},F(y)=\{y,-2y\}\)。直接解包含式得 \(J_F(x)=\{x/2,-x\}\)，且 \(r_F(y)=|y|\)。好支 \(y=x/2\) 的锚内积为 \(x^2/4\) 并严格收缩；坏支 \(y=-x\) 的内积为 \(-2x^2\)，且非零轨道在两点间来回切换。即使完整真误差界成立，选定好支仍不能支撑完整关系的收敛结论。
- [x] `S01.06` 零点锚定条件对所有最近点成立，还是仅对某个最近点成立？
  - **裁决** Proved
  - **结论** 锚定条件的确切量词为 \(\forall x\in U_R\ \forall y\in\mathcal J(x)\ \exists p\in P_S(x)\)。其中 \(p\) 可随该边变化。要求对每个最近锚或每个目标零点都成立，是更强的假设。
  - **证据** [C400 的逐边最近锚](../topics/dd2/core.md#dd2-reverse)、[C414 的有符号锚条件](../canonical/dd2_general_phi_exact.md)、[C400 由有限零集加边反演完整图](../topics/dd2/core.md#dd2-geometry)。
  - **复核** 在实线上取 \(S=\{-1,1\}\)、\(x=0,y=1/2\)。最近输入锚有两个。取 \(p=1\) 得内积 \(1/4\)，取 \(p=-1\) 得 \(-3/4\)，所以 \(\Phi=0\) 仅在一个最近锚成立。取 \(\lambda=1,J=P_S\cup\{(0,1/2)\}\) 再反演原算子，所有投影边可用自身输出作锚；特殊输出的真残差为 \(1/2\)，其距离也是 \(1/2\)。反例保留了完整闭图、覆盖和真输出界。
- [x] `S01.07` DD2 是否要求预解式单值、局部存在、满射性、连续性、闭图或其他结构？
  - **裁决** Proved
  - **结论** 一步 DD2 不要求 \(J_{\lambda F}\) 单值、连续、闭图或全域非空；计算以受检的已有边为对象。欲对实际选择轨道保证续接，必须有局部允许边覆盖及留域，或直接已知所研究的轨道一直合法。有限长度分支由完备性和已声明的 \(S\) 闭性识别点极限；普通版本不另外使用原算子闭图。\(I+\lambda F\) 的全域满射等价于完整预解式全域非空，只是较强的覆盖方式。
  - **证据** [一步版的允许关系](../topics/dd2/core.md#dd2-reverse)、[C401 局部覆盖、留域与点极限](../topics/dd2/core.md#dd2-general-gauge)、[由近端关系反演 F](../canonical/ppa_ab_necessary_bounds.md#ab-scope)。
  - **复核** 例如 \(\lambda=1,S=\{0\}\)，取 \(J(x)=\{x/2\}\)，仅对 \(x>1\) 再加 \(x/3\)。反演所得完整图多值且不闭，因附加边趋于未包含的 \((1,1/3)\)。每条边的锚内积非负，\(r_F(y)=|y|\)，且 \(a\le t/2\)、\(s\le t\)，故覆盖、距离和有限长度仍成立。若仅在某个小窗取 \(J(x)=\{x/2\}\)，窗外为空，反演同样给出小窗内结论而无全局覆盖。
- [x] `S01.08` 对有限维欧氏空间与一般 Hilbert 空间，哪些结论仍然有效？
  - **裁决** Proved
  - **结论** 实 Hilbert 空间在同样的近端边、最近锚、输出误差界、覆盖与留域前提下，保留普通 DD2 的一步估计、比较递推和 C401 有限长度及强点收敛。自由目标类的二维几何取等可嵌入任一维数至少二的实 Hilbert 空间。非空范数闭集在有限维有最近点，一般无限维需要另验；闭凸目标可用 Hilbert 投影。近似锚、弱聚点和物理 shadow 各按对应版本验收。
  - **证据** [C400 欧氏证明和二维构形](../topics/dd2/core.md#dd2-geometry)、[C401 耗散、留域与 Cauchy 极限](../topics/dd2/core.md#dd2-general-gauge)、[Hilbert 最近锚反例和约化条件](../topics/dd2/pppa_recovery.md)。
  - **复核** 平方展开、三角不等式、残差比较和势积分都不调用维数或紧性。有限前缀受控后，尾长趋零使轨道为 Cauchy，完备性给强极限，范数闭的 \(S\) 以距离趋零识别极限。\(\ell^2\) 中 \(S=\{(1+1/n)e_n:n\ge1\}\) 的不同点彼此至少隔 \(\sqrt2\)，故范数闭，\(d(0,S)=1\) 却不达到。这个反例排除了从一般 Hilbert 范数闭性直接获得最近锚的推断。
- [x] `S01.09` 原来的 `B_\omega`、新的 `B_\Phi`、输出相对步长条件是否被严格区分？
  - **裁决** Proved
  - **结论** 旧 \(B_\omega(t)=(t+\omega(t))/2\) 是输入尺度的实际步长上界。DD1 的 \(B_\Phi(t)=(t+\sqrt{t^2-4\Phi(t)})/2\) 同样控制输入尺度，在存在合法锚定边的尺度上使用。若以 \(D=[-\Phi]_+\) 代入，则得到放宽上界 \(B_D(t)\)，正 \(\Phi\) 时一般变松。老师提出的 \(s\le C a\) 使用输出距离，方向也与 \(a\le Ls\) 不同。
  - **证据** [原输入 B 与量词](../canonical/ppa_ab_necessary_bounds.md#ab-scope)、[DD1 作者讨论稿第七及十三节](../manuscripts/dd1_2026_11_20/DD1_2026-11-20_教师讨论稿.md)、[C414 精确有符号根界](../canonical/dd2_general_phi_exact.md)。
  - **复核** 对同一个最近输入锚 \(p\) 展开，\(\|2y-x-p\|^2=t^2-4\langle x-y,y-p\rangle\)。因此锚定反射界 \(\omega(t)\) 对应 \(\Phi_\omega(t)=(t^2-\omega(t)^2)/4\)，代入恰得 \(B_{\Phi_\omega}=B_\omega\)。这是同一锚的等价式，输入步长上界本身不会反推出反射条件。取完整 \(J=P_{\{0\}}\)，非零输入有 \(s=t>0\) 与 \(a=0\)，可满足输入步长界及 \(a\le Ls\)，而 \(s\le C a\) 对任何有限 \(C\) 都失败。
- [x] `S01.10` DD2 所有函数的定义域、连续性、单调性、非负性、可逆性要求是否真正必要？
  - **裁决** Proved
  - **结论** 按一步、整窗、标量递推和长度版本逐项裁决。\(\Phi\) 的有限逐尺度几何不需跨尺度连续、单调、非负或可逆；有边强制 \(\Phi(t)\le t^2/4\)。原 \(\psi\) 只在真残差域评价；对所有残差点对直接换成 \(\psi(s/\lambda)\) 的标量代换需要非减，保留 \(\rho\) 的联合域则允许不连续和振荡。上半连续足以保证直接位移模的最大值，任意模用原可行域的上确界及超水平端点，严格逆非必要。全部标量递推趋零等价于 \(A(0)=0,A(t)<t\) 及每个正 \(l<R\) 有右邻域使 \(A(u)\le l\)；连续性和非减性均非必要，非减收敛主曲线另需 \(\sup_{u\le t}A(u)<t\)。实际零输入吸收、评价域、正位移下界和有限前缀留域仍独立核验。C419 用任意原 \(\psi\) 的 \(b_\psi(t)=\inf_\rho\max\{\lambda\rho,t-\psi(\rho)\}\) 给一般充分长度版本，不要求势凹或零点可微。C401 的耗散门非普遍必要，\(\delta=0\) 即使积分有限仍可失败；给定模的积分非固定图必要，但 C420 证明连续非减模的零缺陷统一类中它充要。各版本分别登记 C417–C420，不改旧 C400/C401/C414 身份。
  - **证据** [函数评价域与零尺度](../canonical/dd2_function_hypotheses.md#fh-domains)、[原真残差域及完整前像分离](../canonical/dd2_function_hypotheses.md#fh-raw-residual)、[最值和广义逆端点](../canonical/dd2_function_hypotheses.md#fh-sup-inverse)、[标量充要判据及完整图反例](../canonical/dd2_function_hypotheses.md#fh-distance)、[任意模的长度充分证明](../canonical/dd2_function_hypotheses.md#fh-general-length)、[临界与非必要性反例](../canonical/dd2_function_hypotheses.md#fh-length-boundaries)、[零缺陷统一类积分充要证明](../canonical/dd2_function_hypotheses.md#fh-zero-defect-sharp)、[精确 Claim 身份](../../CLAIMS.md#c417)。
  - **复核** 分工独立重建后交叉攻击实际正文：核 \(a=0\Rightarrow\rho=0\)、\(s=0\)、精确零集/子零集及不闭纤维；核上确界不达到不能闭合出可行边；用 \(\Phi=3t^2/16\)、单点突升的 \(\psi\) 证明单边可达 \(1/2\) 而完整整窗最优 \(1/4\)。标量右侧条件的反向递归选点、正距离极限闭图链，以及固定图精确包络不合该条件却全轨道有限长的例子均已逐式重构。长度复核含 \(\eta=s^{2/3}\)、\(2D=\chi^2\) 的完整连续单值无限长例；C420 另逐一核平台、有界模、全部前像、真残差最小端、图闭、全域唯一近端及 \(b/2\le\int_a^t u/b(u)\,du\le b\)。没有把安全上界、统一标量必要性或固定模统一类必要性升级为任意固定算子结论。
- [x] `S01.THEOREM` 交出 Exact Theorem Statement，写清对象、量词、定义域、工作区域、零点集、投影选择、参数依赖与结论，并记录假设变化对应的版本。
  - **裁决** Delivered
  - **结论** 正式陈述已并入核心正文 §0：公共对象固定完整 \(F\)、\(S\subseteq\operatorname{zer}F\)、\(\lambda>0\)、\(U_R\) 及允许子关系，量词为每个受检输入的每个允许输出存在一个最近输入锚，误差界在实际输出和完整真残差上评价。G/R/L 分别陈述直接位移几何、原真残差联合域、线性反向预算；D/L-tail/F/F-raw 分别陈述距离、比较级数、原积分势及非规则模长度。Z 单列零缺陷统一类的积分充要性。每个版本列清函数域、零尺度、覆盖与初值预算、结论及证明位置，版本表保留原 Claim 身份；Hilbert 传递沿用 S01.08 并显列最近锚前件。没有将单边尖锐性、完整窗尖锐性和实际轨道必要性合并。
  - **证据** [Exact Theorem Statements](../topics/dd2/core.md#dd2-exact-statements)、[公共对象与量词](../topics/dd2/core.md#dd2-exact-contract)、[一步三版本](../topics/dd2/core.md#dd2-exact-one-step)、[轨道与长度各版本](../topics/dd2/core.md#dd2-exact-dynamics)、[版本表及 Hilbert 传递](../topics/dd2/core.md#dd2-exact-versions)、[C417–C420 完整证明](../canonical/dd2_function_hypotheses.md)、[已同步的 §1 审计](FINAL_PROTOCOL_S1_S3_2026-11-21.md)。
  - **复核** 三路先独立重构再读实际陈述，修正原模与抽象位移模的精确性范围、线性模全残差域、自由输出位置窗和二维锐性维度；一维 \(D=0,L=1\) 的最优值为 \(t/2\)，故不能套二维 \(t/\sqrt2\) 的反向必要性。检查 \(U_t\) 仅在根区间上评价、空根/空联合域不提供覆盖、\(a=0\Rightarrow\rho=0\) 与精确零集加闭纤维的反向条件分别成立。轨道证明先估当前边，再以严格有限前缀预算留域及调用覆盖；极限也严格位于 \(U\)。\(\delta\in(0,1]\)、\(b(0)=0\) 的公式延拓、\(H_Q(t),P(t)\) 的域和固定 \(\lambda\) 均已显写。原先 §1.9/§1.10 审计摘要与表内过时状态同步到已验收版本。

## §2 一般函数补偿关系是否真正得到完整刻画？

- [x] `S02.01` 对一般 `\Phi,\psi`，是否存在显式、可计算的一步下降上包络？
  - **裁决** Proved
  - **结论** 存在不单调化原 \(\psi\) 的显式一维上确界。对 \(t>0,\Phi(t)\le t^2/4\)，令 \(B=(t+\sqrt{t^2-4\Phi})/2,h=|B-t|,\alpha=(t-B)_+,E=B^2+h^2\)，在 \(\mathcal R_t=\{\rho\in D_\psi\cap[0,B/\lambda]:\psi(\rho)\ge\alpha\}\) 上取 \(M_R=\sup\min\{\psi(\rho),\sqrt{E-\max(h,\lambda\rho)^2}\}\)。对自由单边、\(S\subseteq\operatorname{zer}F\)、\(0\in D_\psi\) 类准确；空域就是无边。严格下降另需 \(M_R\le\varphi<t\)。任意函数仅靠有限点值查询没有统一精度保证，连续性本身也不足；若原模有有效连续模与认证求值，可用明确误差的有限网格逼近，允许非单调。非减模另有无需连续性的右端网格证书。有效常数、合法评价域、非空证明及精确等号的额外证据分别保留。
  - **证据** [原残差一维消元及取等证明](../canonical/dd2_function_hypotheses.md#fh-envelope-explicit)、[两种有限精度证书和查询反例](../canonical/dd2_function_hypotheses.md#fh-envelope-computation)、[C421 精确身份](../../CLAIMS.md#c421)、[已修正的旧审计入口](FINAL_PROTOCOL_S1_S3_2026-11-21.md)。
  - **复核** 独立重建 \(U_t\) 在 \(h\) 取峰 \(B\) 的两种符号分支，逐残差用 \(q=\max\{h,\lambda\rho,t-\psi(\rho)\}\) 验证几何可行性与目标值不变；零输出的真残差限制由独立零边处理，未把零候选当成同残差见证。核重根 \(\Phi=t^2/4\)、三角截断、空超水平域及不达到情形。计算证书由 \(|\sqrt u-\sqrt v|\le\sqrt{|u-v|}\) 推出 \(\sqrt{2B\lambda\delta}\)，与原模连续误差或右端非减比较合并；非空时无约束样点不抬高最优值。窄峰反例逐项核完整闭图、精确零集、全域覆盖及真残差，另核已知 Lipschitz 模仍不能仅靠有限查询统一判断精确等号。一般正 \(\Phi\) 的完整整窗最优不由此升级。
- [x] `S02.02` 该上包络究竟是最优的，还是只是一条方便的充分上界？
  - **裁决** Proved
  - **结论** G 在维数至少二的自由两锚几何类中、R/C421 在同维自由闭目标原真残差单边类中，都是逐尺度最小共同上界；不达到仍是锐上确界。整个窗 \(\Phi\le0\)、允许 \(S\subseteq\operatorname{zer}F\) 且无额外输出位置限制时，R 也对完整覆盖闭图类精确。一般正 \(\Phi\) 的完整窗只获得安全界，已有同数据 \(1/2\) 对 \(1/4\) 的严格差距；固定图、目标和一维也可更小。C422 证明原域非空时前缀几何与原残差的最优上确界相同，不能把端点可行性损失误写成数值必然变松。真正把完整输出前件换为前缀误差界则可严格放宽。正部替换和遗漏三角截断一般不锐；原两项全域上确界可用残差坐标认证安全，未经核验的物理位移 G 代换却可低估实际值。
  - **证据** [最优性定义、C422 等值证明及范围表](../canonical/dd2_function_hypotheses.md#fh-envelope-optimality)、[G 每点两锚实现](../canonical/dd2_general_phi_exact.md)、[完整覆盖实现](../canonical/dd2_function_hypotheses.md#fh-raw-residual)、[正下界完整窗严格分离](../canonical/dd2_function_hypotheses.md#fh-positive-fibers)、[C422 精确身份](../../CLAIMS.md#c422)。
  - **复核** 独立从 \(b=\max\{a,|t-s|\}\) 重建全部三角点、第二锚距离及真残差前像；非正下界用垂直锚差的辅助方向保全部边合格，零残差的额外恒等边只在子零集类调用。正下界反证核近极小真实图值所生输入仍在窗内，未假设残差达到。前缀等值逐点使用 \(g_t(\rho)\ge a\) 并取前缀上确界，另给原 \(3/4\) 不达到而前缀达到的非空例。固定 \(F=I\) 与一维为 \(t/2\)，二维自由为 \(t/\sqrt2\)；固定单点目标的另一例为 \(1/3\)，自由两锚为 \(1/2\)。完整窗改用前缀的 \(1/4\to1/2\)、错误物理 G 返回零却有真实 \(1/2\) 均由完整闭图核验。见证按尺度及近优精度量化，未宣称同一轨道逐步取等。
- [x] `S02.03` 是否真正使用了全部四点几何限制？
  - **裁决** Proved
  - **结论** 是，准确 G/R 域在维数至少二的自由闭目标、固定正尺度类中使用了全部四点几何在 \((t,s,a)\) 上的限制。四个角色为 \(x,y,p,q\)，其中 \(p\in P_S(x),q\in P_S(y)\)，允许重合；令 \(b=\|y-p\|,c=\|x-q\|\)。输入最近性 \(c\ge t\) 配 \(c\le s+a\) 给三角下界，输出最近性 \(b\ge a\) 配 \(b\le t+s\) 给三角上界；同锚能量与 \(b\ge a\)、\(b\ge|t-s|\) 分别给平方能量和步长根。反向平面坐标同时补全两锚间距离与全部欧氏相容性。只保留平方能量并未使用全部信息，固定目标、锚间距离或凸性也不属于该自由几何合同。
  - **证据** [四点对应、G1–G6 坐标证明与退化核验](../canonical/dd2_general_phi_exact.md#dd2-four-point-geometry)、[原真残差在同一几何域上的额外条件](../canonical/dd2_function_hypotheses.md#fh-raw-residual)、[C414 身份保持](../../CLAIMS.md#c414)。
  - **复核** 独立重建全部四个三角与两处最近性，再以 \(b=\max\{a,|t-s|\}\)、\(z=(t^2+s^2-b^2)/(2s)\) 检查 \(|z|\le t\)、两项距离及内积符号；第二锚 \(q=(s+a)e_1\) 使 \(\|x-q\|\ge t\) 且 \(d(y,S)=a\)，并非只凭三角列表假设六边可实现。核 \(s=0,a=0,b=0\)、共线、锚重合和重根；零尺度另由 \(p=x\) 处理。用合法 \((t,s,a,b)=(1,2,1/2,1)\) 排除暗加 \(b=a\) 或 \(s\le t+a\)。四组精确伪数据逐一满足其余限制但违反被删除项，证明根、三角上下端及能量各有实际约束作用。Hilbert 正向不暗加输出投影存在，完整真残差和整窗前像量词单列。
- [x] `S02.04` 是否存在没有被当前平方能量推导捕获的额外几何信息？
  - **裁决** Proved
  - **结论** 有，但须按层次回答。裸平方能量遗漏步长根与距离三角；C414 的完整自由四点标量域则无遗漏。C426 证明在维数至少二时，每组该域数据都可由紧凸线段、甚至同一固定射线实现；指定凸四点仍有法向限制，却不降低自由单边最优值。C427 证明自由仿射类的准确附加条件为 \(\lvert t-a\rvert\le s\) 及 \(s^2+a^2+(s^2-(t+a)^2)_+\le t^2-2\Phi(t)\)，输出到输入锚的最小平方距离比自由类多 \(2t(s-t-a)_+\)。在 \(\lambda=1,\Phi=-2t^2,\psi=r/4\) 下，自由闭／凸／固定射线、自由仿射和指定单点的锐值依次为 \(t/2,(1+\sqrt{193})t/32,t/3\)。原真残差通过完整纤维核验；在 \(U=H\)、无附加输出位置限制及 \(0\in D_\psi\) 的非正整窗，逐边可实现完整覆盖闭图；精确零集和闭纤维另需 \(\rho=0\Rightarrow a=0\)。固定图、正下界整窗及动态达到性不由单边实现自动取得。
  - **证据** [裸能量与完整几何的严格差距](../topics/dd2/target_geometry.md#dd2-energy-versus-geometry)、[凸线段与指定四点条件](../topics/dd2/target_geometry.md#dd2-convex-scalar-realization)、[固定射线和完整纤维](../topics/dd2/target_geometry.md#dd2-fixed-ray-realization)、[仿射域及全域线性锐例](../topics/dd2/target_geometry.md#dd2-affine-exact-geometry)、[动态边界](../topics/dd2/target_geometry.md#dd2-target-dynamic-boundary)、[C426](../../CLAIMS.md#c426)、[C427](../../CLAIMS.md#c427)。
  - **复核** 独立从两处凸投影重建线段、固定射线坐标及全部边界；用法向射线添加前像后逐一核完整 \(F(y)\)、零残差、精确零集和窗内每条边。仿射法切分解给 \(b^2=a^2+d^2,s^2=\|u-v\|^2+d^2\)，单点和直线分别达到两支；二维固定直线的严格域差另有精确反例。对 \(r_*=(1+\sqrt{193})/32\) 核 \(16r_*^2=3+r_*\)、\(J(u,v)=(-r_*u,v+d_*u)\) 的逆和真残差，锚内积逐点等于 \(-2t^2\)。动态复核明确 \(t_0>0\)：自由 \(1/2\) 取等强制 \(s=2t,b=t>a\)，总长 \(4t_0\) 与 C413 的闭凸收敛锚障碍冲突。正式 Claim 与实际正文经分工独立复读，未把指定四点限制、逐边存在算子或自由仿射维数误写为共同轨道或任意固定目标结论。
- [x] `S02.05` 如果允许 `\Phi` 变号、不连续、非单调或局部振荡，结论如何变化？
  - **裁决** Proved
  - **结论** 有限 \(\Phi\) 的逐尺度 G/R 域不需连续、可测、非减或可逆；变号时保留 \(E=t^2-2\Phi(t)\) 及正下根，正部替换一般只给较松充分界。\(\Phi(t)>t^2/4\) 表示无边；只有认证域内实际存在该尺度的输入时才与覆盖矛盾。跨尺度最优值可以不连续、非单调，必须分别核共同收缩余量、C418 的正距离右侧门及实际长度证书。C428 在线性标尺 \(\lambda=1,\psi(r)=r,\Phi(0)=0,\Phi(t)\le t^2/4\) 下证明完整覆盖闭图类的逐尺度精确值为 \(\sqrt{t^2/2-\Phi(t)}\)，共同 \(\kappa<1\) 恰需 \(\inf_{0<t\le R}\Phi(t)/t^2>-1/2\)。密集变号不连续例仍统一有限长；逐点严格下降的闭图例则可使距离趋于正极限，连续下界也可伴无限长度。闭图不能将原证书自动上半连续化。一般原 \(\psi\) 的正下界完整前像障碍、零尺度吸收和局部留域各自保留。
  - **证据** [符号、根域与同尺度偏序](../canonical/dd2_function_hypotheses.md#fh-irregular-phi)、[C428 精确公式和完整图取等](../canonical/dd2_function_hypotheses.md#fh-signed-linear-calibration)、[密集变号及错误闭包的完整反例](../canonical/dd2_function_hypotheses.md#fh-oscillatory-phi-example)、[右侧门、连续下界与长度边界](../canonical/dd2_function_hypotheses.md#fh-irregular-phi-dynamics)、[零尺度反例](../canonical/dd2_function_hypotheses.md#fh-zero)、[C428 身份](../../CLAIMS.md#c428)。
  - **复核** 三路独立核符号根、真残差与动态量词。对固定 \(t\) 的坐标 \(x=te_1,y=(t/2)e_1+\sqrt{m^2-t^2/4}e_2\) 验得 \(a=s=m\)、锚积恰 \(\Phi(t)\)；在 \(J=I/2\) 加这条边后，每个完整输出的全部前像都给 \(r_F(z)=\|z\|\)，未遗漏基线前像或退化重合。密集例的两值为 \(\sqrt{3/8}t,\sqrt{5/8}t\)，根给统一 \(s\le(1+\sqrt{3/2})t/2\)，故长度用几何级数而非不成立的 C401 严格余量。C418 的实际 \(t_k\downarrow1\) 和 C400 调和旋转分别复核，未将标量必要性授予固定图。零点 \(-s^2\ge\Phi(0)\)、正重根还须原残差可行、上半连续闭包会排除真实孤立边均独立检查。
- [x] `S02.06` 如果 `\psi` 不能严格求逆，能否使用广义反函数而保持定理成立？
  - **裁决** Proved
  - **结论** 可以，但须保持用途与端点。精确自由单边反演用 \(E_>(c)=\{\rho\in D_\psi:\psi(\rho)>c\}\)、\(E_\ge(c)=\{\rho\in D_\psi:\psi(\rho)\ge c\}\) 的首端 \(q=\inf E\) 及标记 \(q\in E\)，空层取 \(+\infty\)；前缀 \([0,v]\) 命中恰当且仅当 \(v>q\) 或 \(v=q\in E\)。代回 C417 的两支坏边条件即保充要性，无需原模单调或可逆。在整个非负半轴连续非减且零处为零的 \(\eta\) 有平台也不妨碍 \(I+\eta\) 的普通逆；一般已核直接模的广义逆由固定超水平集嵌套自动非减可测。原非单调 \(\psi\) 的长度下界则用 C429：\(b_\psi(t)=\inf_{\rho\in D_\psi}\max\{\lambda\rho,t-\psi(\rho)\}=\inf\{s\ge0:s+\sup_{\rho\in D_\psi,\lambda\rho\le s}\psi(\rho)\ge t\}\)，保留固定 \(D_\psi\ni0\)，允许前缀不达或无穷。它非减且 \(1\)-Lipschitz；继续保留正性、严格耗散、积分、零吸收和覆盖留域，才保长度结论。广义逆数值不恢复非单调函数在指定点的值，也不自动给正下界完整窗最优。
  - **证据** [严格／非严格层集与端点的准确合同](../canonical/dd2_function_hypotheses.md#fh-generalized-inverse-contract)、[原残差位移下确界的等值与正则性](../canonical/dd2_function_hypotheses.md#fh-generalized-step-inverse)、[直接位移逆的独立前件及错误代换反例](../canonical/dd2_function_hypotheses.md#fh-direct-step-inverse)、[C429 精确身份](../../CLAIMS.md#c429)、[C419 长度合同](../canonical/dd2_function_hypotheses.md#fh-general-length)。
  - **复核** 独立重建前缀命中证明，核空层、零首端、未达首端、平台、跳跃、局部域和非单调层集。\(\psi_{\rm c}=\mathbf1_{[2,\infty)},\psi_{\rm o}=\mathbf1_{(2,\infty)}\) 的同首端 2 分别给完整图锐值 1 与 0，全部前像与零集已核；平台例单独否定将 \(>c\) 改为 \(\ge c\)。C429 两向证明分别用候选步长 \(\max\{\lambda\rho,t-\psi(\rho)\}\) 和前缀 \(\epsilon\)-近优残差；非减及 Lipschitz 比较由同一指标集传递。未达例明确两集合只在首端不同，不能据前缀截窗非空判原域非空。零点跳跃可使位移下界为零，原非单调模的错误物理逆可超过真实步长；这些边界均阻止无条件套长度势。复核按默认子零集、精确零集与闭纤维分别保留残差限制。
- [x] `S02.07` 是否能构造显式双向补偿关系：给定 `\Phi` 求允许的 `\psi`，给定 `\psi` 求允许的 `\Phi`？
  - **裁决** Proved
  - **结论** 可以。C430 固定 \(t,\lambda>0,c=A(t)\ge0\)，允许任意有限有符号 \(\Phi(t)\) 和任意非负原 \(\psi:D_\psi\to[0,\infty),0\in D_\psi\)。给定 \(\Phi\)，先核实根及原可行行；\(c<\alpha=(t-B)_+\) 无非空成功，\(c\ge B\) 自动达标，其余恰需 \(\psi\le c\) 于 \(D_\psi\cap[0,B/\lambda]\cap[0,\sqrt{E-c^2}/\lambda)\)。同一 \(\psi\) 的整窗允许帽是逐尺度帽的点态交集，原域非空逐点另核。给定 \(\psi\)，其原位移下确界给准确非空上端；严格坏层 \(\{\psi>c\}\) 的首端 \(q=\lambda\inf\{\psi>c\}\) 及首端归属给三个显式下界条件，取并后与非空区间相交即为允许的 \(\Phi(t)\)。一般正下界完整窗仅直接继承充分性；非正整窗、\(U=H\)、无附加输出位置限制的自由子零集类有全部正尺度的完整闭图统一必要性。零尺度吸收另核。精确零集且闭纤维另保 \(\rho=0\Rightarrow a=0\)。
  - **证据** [对象与非空原域](../topics/dd2/reverse_compensation.md#dd2-compensation-contract)、[给定锚界求原模帽](../topics/dd2/reverse_compensation.md#dd2-compensation-psi-cap)、[给定原模求有符号区间](../topics/dd2/reverse_compensation.md#dd2-compensation-phi-budget)、[线性与端点见证](../topics/dd2/reverse_compensation.md#dd2-compensation-calibration)、[完整窗范围及严格分离](../topics/dd2/reverse_compensation.md#dd2-compensation-scope)、[C430 精确身份](../../CLAIMS.md#c430)。
  - **复核** 三路分别从准确原残差行、最小几何代价及坏层首端重构反演，并核实际正文与注册表。非空门通过 \(f_t(\rho)=\max(\lambda\rho,t-\psi(\rho))\) 和根上支严格递减性得到，不能以前缀上确界虚补原候选；坏边恰需 \(B>c,E>c^2+q^2\) 及 \(q<B\) 或 \(q=B\) 且首端属于坏层，取反给三门。核 \(c=0\)、重根、空坏层、未达首端、两门相等及无非空成功。\(L=1,c=3t/4\) 得完整区间 \([-t^2/16,t^2/4]\)，限制非负缺陷才是 \(D\le t^2/16\)。两阶跃模的开闭预算及平方能量边界的闭覆盖例单独复算；正下界连续目标的分离用完整近极小前像证明，没有把标量必要性转授给固定图或长度。
- [x] `S02.08` 哪些条件是充分的？哪些是必要的？哪些是充要的？
  - **裁决** Proved
  - **结论** 必须固定对象类与结论量词。正尺度有边要求 \(\Phi\le t^2/4\)，但根存在不保证原误差界兼容。C414/C417 的完整标量域对实际边必要、对自由类存在实现充要；非空自由类的指定非严格目标 \(\forall a\le A(t)\) 恰等价准确 \(M_R\le A\)，所以 C430 两向门充要。非正整窗在 \(U=H\)、无额外输出位置限制、自由子零集完整闭覆盖类中保全部正尺度必要性；一般正下界完整窗、固定图、指定受限目标和一维仅直接继承充分性，严格反例已核。精确零集且闭纤维先以有效 \(\psi(0)=0\) 过滤零残差行。每边严格 \(a<c\) 允许 \(M=c\) 不达到；共同 \(\kappa<1\) 则恰需 \(\sup M(t)/t<1\)。原模非减只在对全部标量点对直接代换残差时必要，R 版无需它。C418 的充要性属于全部标量路径，C419 长度门充分但非必要，C420 在固定连续非减模、零缺陷、\(U=H\)、有窗内覆盖且含二维的统一算子类中证明积分充要。新反例 C431 证明逐尺度非空且统一达标仍不保证完整整窗存在，同一组数据却有固定闭图的允许选择实现。
  - **证据** [对象类、精确上确界及条件表](../topics/dd2/reverse_compensation.md#dd2-compensation-necessity)、[C430 两向充要证明](../topics/dd2/reverse_compensation.md#dd2-compensation-phi-budget)、[目标类严格差距](../topics/dd2/target_geometry.md#dd2-affine-sharp-example)、[固定图标量必要性失败](../canonical/dd2_function_hypotheses.md#fh-positive-limit)、[长度门的范围](../canonical/dd2_function_hypotheses.md#fh-length-boundaries)、[C420 统一类积分充要](../canonical/dd2_function_hypotheses.md#fh-zero-defect-sharp)、[C431 完整窗兼容反例与允许图正面](../topics/dd2/reverse_compensation.md#dd2-compensation-compatibility-obstruction)、[C431 身份](../../CLAIMS.md#c431)。
  - **复核** 三路独立从类的实际输出值集核必要性，逐一复读构造及全部纤维。RC17 以 \(\psi(0)=0,\psi(r)=\sqrt{(1-r^2)_+}\ (r>0)\) 给精确零集闭覆盖类的未达 \(M(1)=1\)，但任一 \(a=1\) 都会强制 \(s=\rho=0\) 而矛盾。C431 高段重根给 \(a=s=t/2\)，低段正输出给 \(a^2\le t^2-1/64\le3t^2/4\)；单位输入的近极小完整图值产生 \(1/3<\|w\|<2/3\) 的前像，被迫同时有位移小于及大于 \(1/6\)。环域两组前像的固定闭图则使允许选择全部合格，明确只把闭性授予完整 \(J,F\)。核零尺度仅在实际受检输入使用、原残差无须达到、空域非覆盖、一般必要性不能从较大对象类或较松证书移植。有限长度反例保持工作窗和覆盖前件，未提前授予后续条目验收状态。
- [x] `S02.09` 哪些边界是逐尺度尖锐的？哪些只有统一充分性？
  - **裁决** Proved
  - **结论** C414/C421 的自由几何／原残差上确界及 C430 的两向补偿在所声明的非空自由类逐尺度尖锐；不规则模不保证最值达到。非空原残差自由域的物理上根 \(s=B\) 可达到，正下根还须额外误差界行。C400 的固定线性两支预算可取等并在坏侧有完整闭覆盖见证；C428 在 \(\lambda=1,\psi(r)=r,\Phi(0)=0,\Phi(t)\le t^2/4\) 下保一般有符号整窗逐尺度取等。C426 非正整窗的凸／固定射线实现、C427 仿射及固定单点锐值均有各自完整证据；任意正下界完整窗和未另证的受限对象通常只继承充分性。预算边界精确不等于存在 \(a=A(t)\) 的端点边。C419 的一般耗散、积分和开窗预算是充分机制，非一般锐门；C420 的固定连续非减模、零缺陷、\(U=H\)、覆盖且含二维的统一类另有积分充要边界。C400 和 C411 已核子构造保留动态取等，但新 C434 严格区分每尺度另选算子、同图各尺度取等及实际轨道连续取等；不改变 C411 总账的候选状态。
  - **证据** [尖锐性定义、范围表及线性证据](../topics/dd2/reverse_compensation.md#dd2-compensation-sharpness)、[预算锐而输出无取等](../topics/dd2/reverse_compensation.md#dd2-sharp-budget-without-equality)、[C434 取等量词分离](../topics/dd2/reverse_compensation.md#dd2-sharpness-quantifier-separation)、[球域留域反例](../topics/dd2/reverse_compensation.md#dd2-local-budget-not-necessary)、[固定曲线完整旋转](../topics/dd2/core.md#dd2-trajectory)、[目标结构锐值及动态障碍](../topics/dd2/target_geometry.md#dd2-affine-sharp-example)、[C413 闭凸收敛锚障碍](../topics/dd2/lowL_dynamic_sharpness.md#dd2-low-l-convex)、[C420 统一长度边界](../canonical/dd2_function_hypotheses.md#fh-zero-defect-sharp)、[C434 身份](../../CLAIMS.md#c434)。
  - **复核** 独立重算线性两支预算差 \(((1+L)r-L)((1-L)r-L)/(2L^2)\)、全部最近锚及唯一输出前像。原模 \(\mathbf1_{(2,\infty)}\) 在 \(t=\lambda=1,c=1/2,\Phi=-2\) 给 \(M=0\)，每个 \(\Phi<-2\) 由 RC23 完整图给 \(a=1\)，所以不能虚构临界输出等号。C434 密集例取无理尺度近优边趋向正有理尺度，有限维、固定单点和完整图闭性迫使违反小上界的极限；固定射线例核 \(t,a,s,\rho\)、精确零集及全部后继，虽同图全尺度取等却至多两条非驻定边，而且任意该射线的锐边都从端点投影转入相对内部，不能连续。RC24 以 \(a\le t/\sqrt2,s\le t\) 归纳整个类自动留球，初值预算 \(3>1/4\) 的失败并不影响实际成功。各反例与非空类、零尺度、原残差和覆盖条件均逐项核对；没有将空完整类、单边上确界或结构验证脚本当成动态尖锐性证明。
- [x] `S02.10` 是否存在比目前 DD2 更强、更简洁的共同关系式？
  - **裁决** Proved
  - **结论** C435 在二维及以上自由单边类给原真残差的精确共同式 \(2\Phi(t)+Q_t(a,\lambda\rho)\le t^2\)，\(Q=\max\{a^2+(t-a)^2,a^2+(\lambda\rho)^2,(\lambda\rho)^2+(\lambda\rho-t)_+^2\}\)，另保残差域、原误差界及零输出条件。它同时给最大可实现锚积、最小物理步长与全部可实现步长区间，等价恢复 C421/C430，严格改进原正部及缺少输出帽的候选；不能降低同一个已准确自由类的锐值。C436 在 \(U=H\)、所有窗内完整前像受检且包含零尺度时再给真残差的右闭包必要门；合取原误差界后，在非空完整类实例中把 \(t=1\) 的自由锐值 \(1/2\) 严格降为 \(1/4\)，由 \(F=3I\) 达到。该新门没有被升为一般完整整窗兼容或动态实现的充要刻画。
  - **证据** [C435 精确代价和实现](../topics/dd2/joint_relation.md#dd2-joint-exact-cost)、[逐行投影及全部位移](../topics/dd2/joint_relation.md#dd2-joint-projection)、[原候选严格比较与线性校准](../topics/dd2/joint_relation.md#dd2-joint-candidate-comparison)、[C436 完整前像证明](../topics/dd2/joint_relation.md#dd2-complete-fiber-filter)、[非空完整类的严格增益](../topics/dd2/joint_relation.md#dd2-complete-fiber-strict-gain)、[不闭纤维端点反例](../topics/dd2/joint_relation.md#dd2-complete-fiber-right-endpoint)、[C435–C436 身份](../../CLAIMS.md#c435)。
  - **复核** 三席先独立重构再逐式复读实际稿。核 \(s^2+\max\{a^2,(s-t)_+^2\}\) 在 \(s\ge|t-a|\) 严格递增、三项展开、锚上限的分段替换、全部位移区间和完整真实纤维补全；\(t=0,a=\rho=0\) 可在不同零点间移动，精确零集闭纤维另加反向零过滤。原候选比较始终使用残差坐标，不误加物理下根。完整门逐一审查窗外分支、窗内最近锚、从右近极小值、残差达到及零输出；JR14 的异常行违反 \(u\ge a/3\)，而完整 \(F=3I\) 达界。JR15 的真残差 \(1/4\) 未达且前像集合为 \((1/4,\infty)\)，全部窗内边、零集和覆盖均核准，图明确非闭。原误差界前件、非空性和自由／完整量词在正文与总账已对齐，没有用单纯代数改写代替实质加强。
- [x] `S02.F01` 公式在所声明的定义域上良定；
  - **裁决** Invalid
  - **结论** 原正部候选的字面 max 在一般局部残差域及任意有限非负原模下不普遍良定：可能评价域缺值，或有限上确界不达到。根号本身对全部 \(s\in[0,B_+]\) 均良定，不能将非锐、正部信息损失或算子前件不相容混称为根号错误。保留 \(t\ge0,\lambda>0\)、有限有定义的 \(\Phi(t)\)，将公式改为 \(\rho\in D_\psi\cap[0,B_+/\lambda]\) 上的 sup，在该前缀非空时必为有限非负实数，无需原模连续、单调、可逆、可测或局部有界。精确有符号 G/R 版本另先核实根、直接模评价域及准确可行集非空；C421/JR9 只在其精确非空域读作最优值。零尺度独立判定，空域不得伪装成零输出或覆盖。
  - **证据** [WD1–WD7 的参数、根号、评价域及空域合同](../canonical/dd2_function_hypotheses.md#fh-formula-well-defined)、[原残差联合域](../canonical/dd2_function_hypotheses.md#fh-raw-residual)、[C421 精确非空域及数值式](../canonical/dd2_function_hypotheses.md#fh-envelope-explicit)、[C435 逐行和零尺度](../topics/dd2/joint_relation.md#dd2-joint-projection)。
  - **复核** 三席独立后实际逐段核稿。由 \(B_+^2-tB_+=D_+\) 得 \(E_+-B_+^2=(B_+-t)^2\)，故根号全区间非负，能量帽保证有限 sup，即使 \(\psi\) 在有界前缀不有界。完整 \(F=I\) 在单位输入窗配 \(D_\psi=[0,1/2],\psi(r)=r\) 满足全部前件，却使字面原式评价缺值；全域阶跃原模给未达 \(\sqrt3/2\)，同数据完整 \(J\equiv0\) 确保算子类非空。正重根搭配连续非减 \(\psi(r)=\min(r/2,1/4)\) 时两种未滤公式给 \(1/4\)，实际域却空，明确区分数值存在与前件相容。另核整窗评价域的并集、\(\Phi\) 点点有限不保证共同有界、\(\Phi(0)\) 三种符号和不达到的零残差候选过滤；未提前授予后续达到、统一上界或最优性条目。
- [x] `S02.F02` 最大值是否确实达到；
  - **裁决** Proved
  - **结论** 一般不保证达到。C437 给正部数值式、直接位移 G、原真残差 R 各自上确界的准确命中条件。对已核非空的默认自由 R，\(m=M_R>0\) 达到恰需原非严格超水平层 \(\{\psi\ge m\}\) 命中 \([0,\min\{B,\sqrt{E-m^2}\}/\lambda]\)，首端相等时必须真属于该层；\(m=0\) 则已达到。其实际输出值集为 \([\alpha,m)\) 或 \([\alpha,m]\)。紧残差前缀与相对上半连续模是充分条件，非必要；精确零集加闭纤维须删正高度的零残差行，并重新求该类的值。连续原模也可能在此加强后只有不达上确界。固定图自身的最大值另需实际边集紧性；有限维紧输入层加相对闭边集充分，无界零集或一般 Hilbert 空间有完整闭图反例。数值达到、真残差达到、单边输出达到、同图全尺度达到和轨道取等分别保留量词。
  - **证据** [AT1–AT3 精确条件及输出区间](../canonical/dd2_function_hypotheses.md#fh-attainment-exact)、[紧性证明及三个边界](../canonical/dd2_function_hypotheses.md#fh-attainment-compactness)、[AT5 精确零集与闭纤维严格分层](../canonical/dd2_function_hypotheses.md#fh-attainment-closed-fiber)、[AT6–AT7 固定图紧性正反证](../canonical/dd2_function_hypotheses.md#fh-attainment-fixed-graph)、[C437 身份](../../CLAIMS.md#c437)、[F154 失败机制](../../FAILED_ROUTES.md#f154)。
  - **复核** 三席独立后复读实际稿，逐项重构几何帽和原层交集，核 \(m=\alpha\)、\(m=0\)、空弱层、首端归属和零尺度。紧性证明只对补回零输出删行的松弛集取极值，再按正最大或零最大回到真实域，没有误称原联合域紧。阶跃、开残差前缀、非上半连续但仍达到的例子均有完整真实纤维。AT5 同一 \(\Phi=-2\tau^2,\psi=(2-r)_+\) 下，正步长 1 的输出 2 可由额外零点或未达零残差实现；精确零集闭纤维使 \(\rho>0\)，只能由真残差 \(r\) 的闭图族逼近。AT6 逐式反演连续单值图并核其自身 \(t/2\) 未达，AT7 以统一范数分离核闭图、单前像和 \(1/\sqrt2\) 未达。全部原模、目标、覆盖和完整前像条件均已检查，未提前验收后续统一界或最优性条目。
- [x] `S02.F03` 该表达式是否给出所有合法近端步的统一上界；
  - **裁决** Proved
  - **结论** 是，对同一组前件实际认证的全部边成立。WD5 的真残差前缀 sup 总是安全；字面原 max 在其评价域完整且确有最大值时与之同值，故也安全。任意非单调原 \(\psi\) 不影响该正向结论，因为在实际 \(u=\lambda r_F(y)\le s\) 处取样，未将原残差替换为物理步长。保留符号与输出帽的 (UB3) 给更小或相同的统一界；把它命名为精确 \(M_R\) 时仍保 C421 的正尺度、含零域及非空自由类合同。输入覆盖、残差达到、图闭和输出留域均不用于一步证明，Hilbert 中只需实际最近输入锚存在。若要由本证明保证完整近端的全部选择，前件也须对这些完整输出逐边核准；只认证允许子关系时结论只覆盖该关系，完整真残差定义不变。
  - **证据** [UB1–UB3 的全部受检边证明](../canonical/dd2_function_hypotheses.md#fh-uniform-upper-bound)、[UB4 非单调残差与错误物理筛选](../canonical/dd2_function_hypotheses.md#fh-uniform-upper-bound)、[UB5 允许图与完整输出范围](../canonical/dd2_function_hypotheses.md#fh-uniform-upper-bound)、[原公式的良定前件](../canonical/dd2_function_hypotheses.md#fh-formula-well-defined)、[原残差与数值放宽的既有分层](../canonical/dd2_function_hypotheses.md#fh-envelope-optimality)。
  - **复核** 三席分别重构并逐段复读实际稿。同锚展开、\(a\le\|y-p\|\)、反三角给 \(s^2+a^2\le E\)、物理根；距离 1-Lipschitz 再给输出根 \(a^2-ta+\Phi\le0\)，故 \(a,u\le B\) 与 \(a^2+u^2\le E\)。比较 \(B\le B_+,E\le E_+\) 后直接在真实 \(\rho\) 取样，未使用单调性或最值达到。UB4 的完整纤维为 \(\{e_1/2,e_2/100\}\)，全部边合格且正确界 \(1/2\)，错误 G 才只剩零输出；UB5 的额外输出 2 真残差为 1、输出误差界成立但锚积 \(-2\) 失效，证明只认证好选择不能凭此推全输出。另核零尺度三分支、局部域、允许图不改变完整残差，以及不含零残差域的正向安全与 C421 精确身份的区别。没有将不锐或未达当成不安全。
- [x] `S02.F04` 它是否为相应几何模型的精确最优值；
  - **裁决** Refuted
  - **结论** 原正部两项式的一般精确性被否证；它只对 OP1 删除若干几何约束后的标量域精确。修订后的 G 与 R 在各自自由单边类中给最小共同上界，非正整窗另有完整闭覆盖实现。保留 C421 含零残差域及准确非空条件时，\(\Phi\le0\) 给 \(M_R=\min\{B_+,W_+\}\)，故原式精确恰需 \(W_+\le B_+\)。一般符号的 OP3 用所有严格低于 \(W_+\) 的水平命中原残差三帽精确判定等值，允许上确界未达。零尺度分开处理。正下界既有严格损失也有等值例；固定对象、仿射、一维及正下界完整窗必须保留自己的域，二维自由最优值不能自动转授。
  - **证据** [OP1–OP3 的模型与精确比较](../canonical/dd2_function_hypotheses.md#fh-formula-exact-optimum)、[G 同平面两锚实现](../canonical/dd2_general_phi_exact.md#dd2-four-point-geometry)、[R 完整真残差实现](../canonical/dd2_function_hypotheses.md#fh-raw-residual)、[C435 的精确投影及候选严格差距](../topics/dd2/joint_relation.md#dd2-joint-candidate-comparison)、[完整窗额外约束](../topics/dd2/joint_relation.md#dd2-complete-fiber-strict-gain)、[固定对象和目标范围](../canonical/dd2_function_hypotheses.md#fh-envelope-optimality)。
  - **复核** 三席先独立推导再逐式复读实际稿。逐行上界与反向取值证明 OP1 恰为放宽域；G 的输入最近性、输出最近性及退化同时实现，R 从投影底图加主边，在必要时补最短前像，零输出及额外零点另行核准。非正整窗全部边认证没有由闭图或覆盖替代。OP3 用严格超水平存在性处理未达值及 \(c<\alpha\)，没有误检最优端点。完整 \(F=I\) 给 \(2t/\sqrt5>t/2\)，完整 \(F=-I/2\) 给 \(4\sqrt{5/17}\,t>2t\)；正重根配截顶模在单位尺度两式同为 \(1/2\)，三例的全部纤维与窗内前件均核准。另核 \(t=0\) 的原域、零输出过滤及 \(\Phi(0)\le0\) 时的同一截帽式；Hilbert 自由锐性用二维嵌入，固定闭目标仍需实际输入锚。没有把最大值未达、不安全与不精确相互混同。
- [x] `S02.F05` 何时有 `\varphi(t)<t`；
  - **裁决** Proved
  - **结论** C438 在含零原残差域给准确严格门：原两项上确界 \(W_+(t)<t\) 恰需原模在 \(\lambda\rho\le\min\{B_+,\sqrt{2D_+}+\varepsilon\}\) 的前缀上确界随 \(\varepsilon\downarrow0\) 的极限严格小于 \(t\)。无需原模单调、连续或最大值达到。准确非空 R 在 \(\Phi>0\) 时由 \(B<t\) 自动严格，\(\Phi\le0\) 时与原式同判。每条边严格下降的较弱弱层判据另列，允许未达 \(M_R=t\)。指定 \(A=\varphi\) 仍须验 \(M_R\le A<t\)，不能用诱导曲线替换预先目标；跨尺度统一 \(\kappa\) 另需 \(\sup M_R(t)/t<1\)。线性原模严格恢复 \(D_+/t^2<T(L)\) 两段门，临界等号有真实输出 \(a=t\)。G 保自己的物理筛选，零尺度及空域独立处理。
  - **证据** [C438 的 SC1–SC4 充要证明与正则性化简](../canonical/dd2_function_hypotheses.md#fh-strict-decrease)、[SC5–SC7 逐边严格、同一连续图及右侧跳跃](../canonical/dd2_function_hypotheses.md#fh-strict-edge-versus-margin)、[指定目标、G 筛选、跨尺度余量与线性校准](../canonical/dd2_function_hypotheses.md#fh-strict-target-calibration)、[C438 精确身份](../../CLAIMS.md#c438)、[F155 失败机制](../../FAILED_ROUTES.md#f155)。
  - **复核** 三席独立重构后复读实际稿。核膨胀前缀含零、非闭原域、无穷原上确界、根截断与开能量端；反向只在 \(q+\varepsilon<B_+\) 时用能量根，未偷补评价点。SC5 同残差降至 \(a=t\) 由 C435 实现，默认子零集与精确零集闭纤维过滤未混同。SC6 的完整 \(F(u,z)=(0,z/(1+u^2))\) 全窗每边严格，但沿无界目标有固定图上确界 \(t\)；SC7 的真残差 \(r\downarrow1/2\) 逼出未达 1，临界闭前缀却恒零。正下界完整 \(F=I\) 证明正部可漏共同余量；连续原模 \(\sqrt r\) 又证明 \(\mathcal H_t/t=0\) 不给统一比例。线性 \(L=1/2\)、退化 \(\ell=0\)、准确非空门、零尺度三支均核准，未把本项提前升级为距离趋零或长度结论。
- [x] `S02.F06` 何时有 `\varphi^{\circ n}(t)\to0`；
  - **裁决** Proved
  - **结论** 先核同一函数的自映射和评价合同。C439-A 在 \(A(0)=0,A(t)<t\) 下给纯复合趋零的充要条件：每个正门槛的某右邻域内，每个初值都能在依该点而定的有限步内降到门槛；等价有限逆像层穷尽或整数退出秩。一般自映射另有前向不变小集及最终进入的完整判据。全部 \(t_{n+1}\le A(t_n)\) 路径仍由 C418 的一步右侧门充要刻画；非减时纯复合与该门等价，可合法归纳比较。一般非单调时不能这样替换。C439-B 给两个同函数、同完整图单步标量数据、同处处达到最优包络的闭图；纯复合一致几何趋零，但一个图全部轨道趋零，另一个有距离趋 1 的真实链。合法无限路径、覆盖和物理留域分别核验；不从本项推点收敛或长度。
  - **证据** [复合的函数域及一般自映射合同](../topics/dd2/scalar_iteration.md#dd2-scalar-iteration-contract)、[有限步越过、逆像层和秩的充要证明](../topics/dd2/scalar_iteration.md#dd2-composition-exit)、[非减比较与右极限等号](../topics/dd2/scalar_iteration.md#dd2-monotone-composition)、[两个完整图的全部坐标与真纤维](../topics/dd2/scalar_iteration.md#dd2-same-envelope-different-trajectories)、[危险前缀及留域合同](../topics/dd2/scalar_iteration.md#dd2-composition-applications)、[C439 身份](../../CLAIMS.md#c439)、[F156 失败机制](../../FAILED_ROUTES.md#f156)。
  - **复核** 三席先独立推导再逐段复读实际稿。核退出步数的量词、阈值吸收、有限链反例及非减归纳，两个同右极限例区分等号实际命中；\(W_+\) 前缀非空与准确 R 原域非空分别保留。两图以全域双射底图保证每个输出有前像，所有完整入边满足 \(s=a\)，故真 \(\rho=a\) 且包含窗外前像。角式 \(\cos\gamma_k=1/2+1/((k+4)(k+6))\)、预算裕量 \(b_k^2-a_k^2>1/((k+4)(k+5))>h_k^2/2\)、反射保锚与四点距离、沿零集逃逸保闭性均独立核准。好图影子半径只可能匹配下一标记却高度不同，坏图链才可持续；单输入四元组、固定图最大值、原字面 max 与自由 \(M_R\) 逐一核等。原始 A 未被换成其非减化，位置窗反例、零尺度及全部允许选择范围已检查。
- [x] `S02.F07` 何时可以构造非减的下降模函数；
  - **裁决** Proved
  - **结论** C440 在有限闭窗自映射合同内给最小非减上界 \(Q_b(t)=\sup_{u\le t}b(u)\)。它零吸收且正尺度严格下降恰需 \(b(0)=0,Q_b(t)<t\)；在逐点 \(b<t\) 下，后者等价每个正点含右端的左上极限严格低于该点。存在非减且复合趋零的主曲线还需 C418 的一步右侧门，等价全部标量不等式路径对全窗初值和选择一致趋零。需要连续、右连续严格主曲线，或严格递增且复合趋零的主曲线时，准确条件是右连续上界 \(Q_b^+(0)=0,Q_b^+(t)<t\)，并给显式连续构造。非减化保持最坏一步比例，不能自动创造 DD1 统一收缩。预设目标仍是 \(A\)；需要 \(b\le\widehat b\le A\) 时另核 \(Q_b\le A\)，计算界和固定图必要性保持原范围。
  - **证据** [MM1–MM4 三层存在判据及全窗一致性](../topics/dd2/scalar_iteration.md#dd2-monotone-majorant)、[MM5–MM7 连续条件与构造](../topics/dd2/scalar_iteration.md#dd2-continuous-majorant)、[MM8–MM10 左右障碍及完整闭图实现](../topics/dd2/scalar_iteration.md#dd2-majorant-obstructions)、[指定目标与部分域合同](../topics/dd2/scalar_iteration.md#dd2-majorant-target-scope)、[C440 身份](../../CLAIMS.md#c440)、[F157 失败机制](../../FAILED_ROUTES.md#f157)。
  - **复核** 三席先独立重构再逐式复读实际稿，核前缀未达、闭窗右端、C418 右门的等号、任意长倒排有限链及全窗一致量词。连续构造用非负下半连续 \(\gamma\) 的紧最小值和 \(1/2\)-Lipschitz 估计；严格递增必要性无需偷加连续。MM10 指定主值 arccos，左端回全域底图，临界尺度沿零集逃逸，右端实含；全体完整入边 \(s=a\) 保真 \(\rho=a\)，包括窗外前像，原式与准确包络均逐尺度取等。零点另核，C439 右侧障碍的复合精确趋 1。固定图好轨道反证一般必要性外推，连续构造未被宣称保持任意预设 \(A\)，空域未被补零。
- [x] `S02.F08` 反向刻画是否成立；
  - **裁决** Proved
  - **结论** 原两项式自身有 C441 的精确数值反演：指定 \(c=A(t)\)，原模须在闭根前缀且满足 \((\lambda\rho)^2+c^2<E_+\) 的原残差点不超过 \(c\)。固定原模后，以严格危险层首端 \(q\) 及其归属 \(e\) 得能量／根两道预算；分界 \(q=t+c\) 保安全等号，根支端点由 \(e\) 决定。准确有符号自由 R 仍用 C430 的三门及非空上端；直接 G 保物理筛选。非正 \(\Phi\) 且 \(c<t\) 时，虽然原式未必是准确值，\(M_R=\min(B_+,W_+)\) 仍使两种目标反演等价；在已声明的非正完整闭覆盖统一类也有实际坏尺度见证。一般正下界、任意固定图或未过滤的精确零集类不具有原式必要性，均有完整反例。预设目标不被诱导界替换，零尺度、严格目标及完整窗存在另核。
  - **证据** [C441 的 RV1–RV6 数值逆、预算分段与目标恢复](../topics/dd2/reverse_compensation.md#dd2-original-envelope-inverse)、[准确原模帽](../topics/dd2/reverse_compensation.md#dd2-compensation-psi-cap)、[有符号三门及非空上端](../topics/dd2/reverse_compensation.md#dd2-compensation-phi-budget)、[完整统一类及正下界分离](../topics/dd2/reverse_compensation.md#dd2-compensation-scope)、[逐尺度非空与完整窗不相容](../topics/dd2/reverse_compensation.md#dd2-compensation-compatibility-obstruction)、[C441 精确身份](../../CLAIMS.md#c441)。
  - **复核** 三席独立推导后逐式复读实际 RV1–RV6，核原域含零、严格坏层为空、\(q=0,q=t,q=t+c\)、负能量预算及零尺度；根换元保 \(q\ge t\)，不凭广义逆值猜首端归属。能量等号用 \(a=3/5,s=\rho=4/5\) 的完整投影添边验证，根端用两个开闭阶跃原模验证。正重根 \(F=I\) 分离正部式与准确目标，零下界同图另分离固定图与统一类；\(\psi(0)=1\)、其余零的闭纤维精确零集例核过滤必要。RC13 非空完整类与 C431 不存在性未混同。严格目标使用该类自身 \(M_{\mathcal C}\) 加排除等号，未达上确界不伪造等号边；非正坏尺度经过实际全纤维实现，不把数值逆直接称为算子最优，也未推出共同轨道或长度。
- [x] `S02.F09` 相关临界界是否存在可实现的取等构型。
  - **裁决** Proved
  - **结论** 可实现性有准确条件，不能全称肯定。C435/C437 给任意正目标高度 \(c\) 的同一原残差证书：\(\alpha\le c\le B\)，且 \(\{\psi\ge c\}\) 命中 \([0,\min(B,\sqrt{E-c^2})/\lambda]\)；全部真实步长为 EQ2，两个最近锚和完整纤维可同时实现。先证 \(M_R\le c\) 再命中才是安全且取等。原字面 max 达到只判其放宽域；甚至 \(W_+=M_R\) 且原 max 已达，准确真实上确界仍可能未达，EQ3 给同数据正下界完整闭覆盖类的实际证明。C441 的被包含有限预算端点化成弱层命中 \([0,q/\lambda]\)，相同严格危险层和预算可分别有、没有目标等号。线性能量／步长两支有完整取等图；非空上端、零尺度、精确零集过滤、完整整窗和共同轨道各保原量词。
  - **证据** [EQ1–EQ4 同原残差取等、全部步长及完整反例](../topics/dd2/reverse_compensation.md#dd2-attainment-certificate)、[C437 的原达到条件](../canonical/dd2_function_hypotheses.md#fh-attainment-exact)、[C435 的同锚代价及步长区间](../topics/dd2/joint_relation.md#dd2-joint-projection)、[C400 两支同构形](../topics/dd2/core.md#dd2-geometry)、[预算尖锐但输出不取等](../topics/dd2/reverse_compensation.md#dd2-sharp-budget-without-equality)、[C434 两次量词分离](../topics/dd2/reverse_compensation.md#dd2-sharpness-quantifier-separation)、[C437 补证记录](../../CLAIMS.md#c437)、[F154 失败机制](../../FAILED_ROUTES.md#f154)。
  - **复核** 三席独立重构并逐式复读实际稿。核同一四点的两处最近性、残差点与实际步长的区别、闭弱层与反演严格层、根端和零端。EQ3 的 \(I/4\) 底图、闭球短支及两附边逐一核全部纤维，包含窗外前像；每个固定 \(F_r\) 的单位层最大值为 \(r<1/2\)，只有类上确界逼近 \(1/2\)，不虚构固定图未达。另核唯一最优残差 \(1/10\) 不能作物理步长、同 \(q=2,e=0,d_*=2\) 的改模取等构型、两个完整线性／射线见证。C426 非正整窗的附加前件显写，C434 保固定单点和固定射线范围；正下界完整兼容、任意模共同轨道仍未被升级为已解。复用既有 Claim 并补证据，无额外重复命题。

## §3 DD2 是否严格恢复 DD1 的全部分段机制？

- [x] `S03.01` DD2 的假设能否容纳 DD1 的完整假设？
  - **裁决** Proved
  - **结论** DD1 教师稿第七节的一般有符号 \(\Phi\)、每条允许边存在某个最近输入锚及完整真残差线性界，取 \(\psi(r)=\ell r\) 即原样进入 DD2 E0，正尺度兼容另行携入。R/G 保留原符号，L 可在正尺度选统一二次副证书及某个共同目标 \(A=\kappa t\)。但原正尺度上确界不控制零输入；C442 的完整闭图反例否定未经补充的含零比例界和全部留域路径有限长度。受检零输入驻定恰是将比例步长界延到零处的条件，\(\Phi(0)\ge0\) 为充分证书；原稿、修订合同与原协议二次校准分别保留。F 的耗散条件、L-tail 所需的工作窗覆盖和位置预算不能冒充 DD1 原前件。
  - **证据** [源文身份及 D1H1–D1H2](../topics/dd2/dd1_recovery.md#dd1-assumption-source)、[E0/R/G/L/L-tail 逐项映射](../topics/dd2/dd1_recovery.md#dd1-dd2-assumption-map)、[D1Z1–D1Z5 完整闭图、任意小二周期及最小零修订](../topics/dd2/dd1_recovery.md#dd1-zero-obstruction)、[局部化与反射版本](../topics/dd2/dd1_recovery.md#dd1-localization-scope)、[C442 精确身份](../../CLAIMS.md#c442)、[F158 失败机制](../../FAILED_ROUTES.md#f158)。
  - **复核** 三席先完成四项开工自检，分别独立重读原教师稿、重建版本映射及攻击零尺度，再复读实际 D1H1–D1Z5、C442、F158。核源提交与 blob、\(\forall\)边\(\exists\)锚、原完整输出纤维、允许子图和认证窗；核反例的全域覆盖、闭图、精确零集、每条完整边及任意小正初值周期。有符号根仍有效，受检零边的驻定充要性不外推未受检分支；只给正初值、\(A(0)=0\) 或 \(\psi(0)=0\) 不替代修订。旋转例仅排除 F 及以 \(b_\psi\) 为指定下界的 F-raw 门，不否定另证更强实际位移下界。未将全部路径已知留域升级为自动留域，未提前签收后续因子或算法恢复。
- [x] `S03.02` DD2 的结论是否恢复 DD1 的统一收缩及步长估计？
  - **裁决** Equivalent / Recovered
  - **结论** 在原正尺度前件下，固定 \(\sigma_R\le\theta<T(L)\)，DD2 恢复 \(\kappa_\theta=\min\{Lb_\theta,L\sqrt{(1+2\theta)/(1+L^2)}\}\in(0,1)\)，其中 \(b_\theta=(1+\sqrt{1+4\theta})/2\)。这正是源稿 (7.1)；DD2 的额外根项因 \(b_\theta\ge1>\kappa_\theta\) 在下降区不改变因子。实际边保原有符号 \(s\le B_\Phi(t)\)，正尺度再有 \(B_\Phi(t)\le b_\theta t\)，对应 (7.2)。受检零边补 C442 的驻定后，\(a\le\kappa_\theta t,s\le b_\theta t\) 延至零，合法路径尾长至多 \(b_\theta t_k/(1-\kappa_\theta)\)，并收敛到闭 \(S\) 中一点。原 \(\Phi(0)<0\) 时根函数仍可能正值，不能把实际驻定写成原根归零。全部选择自动续接和极限在 \(S\cap U\) 另核覆盖及严格位置预算；未修订含零原句仍由 C442 限制。
  - **证据** [D1R1–D1R4 同一统一因子与反向预算恢复](../topics/dd2/dd1_recovery.md#dd1-uniform-recovery)、[D1R5–D1R10 原符号根、比例步长、完整反例及尾长](../topics/dd2/dd1_recovery.md#dd1-step-and-tail)、[C400 原三项式和线性反演](../topics/dd2/core.md#dd2-reverse)、[C442 零合同](../topics/dd2/dd1_recovery.md#dd1-zero-obstruction)、[C400 补证记录](../../CLAIMS.md#c400)。
  - **复核** 三席分别独立重构因子、步长与轨道，再逐式复读实际 D1R1–D1R10 及原稿 (7.1)/(7.2)。核完整 \(\rho\le s/\lambda\)、同一最近锚、固定 \(\theta\) 与上确界不必达到；步长严格门先核 \(0<L<1\) 再平方，能量门和并集比较无遗漏。核 \(\theta=0,L=1/2\)、任意固定正 \(L\)、正 \(\Phi\) 的判别式及空尺度；显示因子门不被当成固定图必要条件。另给目标时先核 \(\kappa\ge r_0\)，原更强有符号数据可另证。完整 \(F=I\) 的跳跃 \(\Phi(0)\) 例区分原根和实际驻定，完整 \(J\equiv0\) 反驳输出比例 \(s\le Ca\)。几何级数按实际路径求和，开域留存用有限前缀归纳，未先假设无限续接；无须 \(F\) 闭图。没有提前签收后续临界锐性。
- [x] `S03.03` 两段临界边界分别由什么几何机制决定？
  - **裁决** Proved
  - **结论** 固定正尺度和 \(r_0\le r\le1\) 的目标高度 \(a=rt\)，写 \(q=r/L\)、同一输入锚距 \(h=\|y-p\|\)。完整线性误差导出 \(s\ge a/L\)，同锚最小能量在 \(s=qt,h=t\max\{r,q-1\}\) 达到。\(q\le1+r\) 时可共锚，\(h=a\)，平方能量给 \(\Sigma_E\)；\(q>1+r\) 时共锚三角不容那么长的步，一般须 \(h\ge s-t>a\) 并换输出锚，最小预算处 \(h=s-t\)，步长根给 \(\Sigma_B\)。固定目标的分界是 \(L=r/(1+r)\)；固定 \(0<L<1\) 改缺陷时，因子两项换序于 \(\sigma_*=L/(1-L)^2\)。在临界高度 \(a=t\)，比较 \(t/L\) 与 \(2t\) 才得到低 \(L<1/2\) 的 \((1-L)/L^2\) 和高 \(L>1/2\) 的 \(1/(2L^2)\)，端点两者同为 2。严格换锚可由紧凸线段实现，不要求非凸目标；小 \(L\) 不表示所有缺陷下都由步长项支配。
  - **证据** [D1G1–D1G7 同锚最小代价、构形及三条分界](../topics/dd2/dd1_recovery.md#dd1-two-branch-mechanisms)、[C400 反向预算与原两项因子](../topics/dd2/core.md#dd2-reverse)、[C426 紧凸线段实现](../topics/dd2/target_geometry.md#dd2-convex-scalar-realization)、[C400 机制补证](../../CLAIMS.md#c400)。
  - **复核** 三席先独立重建代价和三角障碍，再逐式复读实际 D1G1–D1G7。核 \(r\ge r_0>L/(1+L)\) 使另一三角端不活动，\(f_r\) 在允许半轴严格递增，预算等号仍排除 \(a>rt\)。能量支取等时须输入锚本身也是输出最近锚；严格步长支有 \(h>a\)，凸线段两端分别投影，不能直接凸化源稿放在输出外侧的旧第二锚。核预算差、步长候选平方前的 \(r\ge L\)、\(\sigma_*\) 的相减方向及其相对 \(T(L)\) 的三种位置；根门在不支配区仍可有效，原“高参数不可用”的解释已修正。取等属于含二维平面的自由闭目标类，未外推任意固定图；\(r<r_0\) 是统一保证失败而非高度不可实现。完整纤维、全部最近点和局部算子锐性未被提前验收。
- [x] `S03.04` 两类极值构型是否满足全部最近点约束？
  - **裁决** Proved
  - **结论** 在 \(t>0,L>0,r_0\le r\le1\) 的相应分支域内，两类坐标确实同时实现两处最近点及全部四组三角。教师稿 \(s=1\) 的低支六距为 \((t,a,s,h,c,d)=(L,L,1,1-L,1+L,1)\)，高支为 \((L,L,1,L,L,0)\)。一般能量支用同一真实三角与单点目标；步长支的外侧有限两点、内侧有限两点及内侧整段各有完整证书。外侧两点不能直接凸化，必须改变第二锚才能保留正输出距离。二维固定射线也逐边实现两支并核对其全部点；不据此外推任意指定目标或共同算子。\(L=1/2\) 的旧外侧锚可并列而不重合，内侧段则退化；正高度族、零输入与维数边界均另明。
  - **证据** [D1N1–D1N6 原坐标、一般三角、六距和整个目标的投影](../topics/dd2/dd1_recovery.md#dd1-nearest-point-audit)、[C414 的全部四点约束](../canonical/dd2_general_phi_exact.md#dd2-four-point-geometry)、[C426 的内侧线段](../topics/dd2/target_geometry.md#dd2-convex-scalar-realization)、[固定射线](../topics/dd2/target_geometry.md#dd2-fixed-ray-realization)、[C427 的仿射限制](../topics/dd2/target_geometry.md#dd2-affine-exact-geometry)、[C400 最近点补证](../../CLAIMS.md#c400)。
  - **复核** 三席分别从教师稿原坐标、整个目标集和边界攻击独立重算，再复读实际 D1N1–D1N6。核源几何参数为 \(L\) 而非真残差，所有六距来自同一坐标，交叉最近性对两点集足够但不自动覆盖更大集合。核根号的乘积分解、\(r=r_0\) 的直角、\(s=t+a\) 的共线与并列、\(L=1/2\) 旧标签不必重合；线段和固定射线分别对全体参数点证明距离最小。目标扩大以 D1N6 保距离，精确零集身份仍须单独排除所有外部零点；仿射的正交限制不被凸线段例掩盖。有限/线段低支可一维，固定射线严格低支用二维；正输入的 \(s=0\) 与线性界矛盾，\(a=0\) 不是正高度极值。未把几何取等当作完整残差或整窗算子证明。
- [x] `S03.05` 在 `L=1/2` 处是否连续，是否存在结构切换？
  - **裁决** Proved
  - **结论** \(T(1/2)=2\) 且两侧极限同为 2，但左、右导数为 \(-12,-8\)，连续而不可微。正尺度临界高度 \(a=t\) 的低侧取 \(h=s-t>a\) 并换输出锚，高侧取 \(h=a\) 且共锚三角非退化；端点 \(s=2t,h=a=t\)，两组边界同时取等。结构切换针对临界边，不表示每个严格可行实例在此换支：固定 \(0\le\sigma<2\) 时附近始终由能量项支配。固定 \(0<r<1\) 的可保证域为 \(0<L\le r/\sqrt{1-r^2}\)，切点是 \(L_r=r/(1+r)<1/2\)；\(r=1/\sqrt5\) 时 \(1/2\) 只是零预算的域右端。二维自由目标中可选连续相接的内侧凸段/单点代表，旧外侧标签仍可能只对输出并列最近，不推出固定算子或轨道的参数连续性。
  - **证据** [D1C1–D1C5 极限、导数、活跃约束、有效域及连续几何族](../topics/dd2/dd1_recovery.md#dd1-critical-half-continuity)、[D1G 的三个分界](../topics/dd2/dd1_recovery.md#dd1-two-branch-mechanisms)、[D1N 的原坐标及内侧替代](../topics/dd2/dd1_recovery.md#dd1-nearest-point-audit)、[C400 原分段门](../topics/dd2/core.md#dd2-reverse)、[C400 连续性补证](../../CLAIMS.md#c400)。
  - **复核** 三席分别独立微分、重建临界几何和攻击参数量词，再逐式复读实际 D1C1–D1C5。核 \(t>0\)、\(\sigma_*\) 仅在 \(0<L<1\) 存在、左右取等余量消失以及 \(K_{1/2}(\sigma)=\sqrt{(1+2\sigma)/5}\) 的严格预算范围。对固定目标分别核 \(r>1/\sqrt5\) 的双侧平滑能量域、等号的单侧可行域及低目标的统一认证失败。连续代表在平面中保 \(x=0,y=e_1,t=a=L,s=1\)，两侧 Hausdorff 距离分别为 \(1/2-L\) 和 \(\sqrt{L^2-1/4}\)；原外侧集合极限不同，未伪造标签合并。共锚表示认证输入锚也最近于输出，不要求所有标记输出锚重合。只签收本题的函数及几何连续性，严格门与实际算子按后项验收。
- [x] `S03.06` 严格不等号能否放宽？
  - **裁决** Sharp
  - **结论** 原固定二次校准的自由完整局部类中，\(\sigma<T(L)\) 不能改成 \(\sigma\le T(L)\) 而保留共同收缩、距离趋零、点收敛或有限长度。临界只普遍保 \(a\le t\) 及 \(t/(1+L)\le s\le b_{T(L)}t\)，已知合法且零驻定的路径有限长当且仅当 \(\sum t_k<\infty\)。对每个固定 \(L>0\)，高支完整旋转或低支在非孤立闭零集上的投影增边图在等号给任意小正距离的真实不收敛轨道；更宽预算也包含这些例子。一般 \(\Phi\) 的逐尺度 \(\sigma(t)<T(L)\) 只给逐边严格，不能替代 \(\sup\sigma<T(L)\)。指定严格目标 \(r_0\le r<1\) 的预算 \(\sigma_R\le\Sigma_L(r)\) 却允许等号。固定图可以越过类门仍收敛，即使两条单项常数各自准确；零合同、维数与局部留域范围另明。
  - **证据** [D1S1–D1S11 正面估计、全部纤维和实际轨道](../topics/dd2/dd1_recovery.md#dd1-strict-critical-gate)、[完整临界图和不变局部窗](../topics/dd2/dd1_recovery.md#dd1-critical-full-operators)、[逐尺度严格及固定图边界](../topics/dd2/dd1_recovery.md#dd1-pointwise-strict-boundaries)、[C285 原临界见证](../canonical/rleb_sharp_linear_frontier.md#rsl-threshold)、[C400 指定目标与长度分离](../topics/dd2/core.md#dd2-trajectory)、[C418 正极限完整图](../canonical/dd2_function_hypotheses.md#fh-positive-limit)。
  - **复核** 三席先独立推导门、重构完整图及攻击动态量词，再逐式复读实际正文。高支核 \(\eta=1/L\le2\)、旋转角、单点纤维与恒定步长；低支核全体锚、双向唯一前像、精确零集、闭性、覆盖及 \(U_N=(-r_N,r_N)\) 的全部输出不变性，残差帽与坏周期能同时保留。核旧反射常数不是当前 \(L\)，核 C400 调和路径、C418 逃逸链的预算间隙和完整真残差。正距离输出与非零向量已区分；临界 \(\sigma_R=T\) 可以不达到，缩窗恢复统一证书须 \(\limsup_{t\downarrow0}\sigma(t)<T\)。\(\operatorname{diag}(1,-3)\) 以不同轴分别达到最优误差界与缺陷常数，却有真实因子 \(1/2\)，阻止将类的必要性转授固定图。未提前签收后项的全参数锐性分类。
- [x] `S03.07` 分段曲线是否对整个四点几何类尖锐？
  - **裁决** Sharp
  - **结论** 是，精确范围为 \(t>0,L>0,\sigma\ge0,\Phi(t)=-\sigma t^2\)、\(a\le Ls\)，维数至少二且目标 \(S\) 自由选择的闭非空四点几何类。D1F2 是全部最近性与欧氏相容条件的准确消元，输出投影恰为 \([0,m_L(\sigma)t]\)，其中 \(m_L=\min\{b,Lb,L\sqrt{(1+2\sigma)/(1+L^2)}\}\)、\(b=(1+\sqrt{1+4\sigma})/2\)。能量、步长与输出锚距三支以及全部交界均有真实坐标取等；故指定 \(r_0\le r<1\) 的 \(\Sigma_L(r)\) 是闭的准确预算，任意超预算都有 \(a>rt\)，并有 \(m_L(\sigma)<1\iff\sigma<T(L)\)。自由闭凸类也达到；一维和任意指定目标不自动继承同一锐值，几何结论不代替完整纤维或轨道认证。
  - **证据** [D1F1–D1F9 准确全域、三个最大构形及反演](../topics/dd2/dd1_recovery.md#dd1-four-point-whole-class)、[严格坏侧与对象边界](../topics/dd2/dd1_recovery.md#dd1-four-point-reverse-sharp)、[C414 全四点消元](../canonical/dd2_general_phi_exact.md#dd2-four-point-geometry)、[C400 原反演](../topics/dd2/core.md#dd2-reverse)、[C426 固定射线与凸目标](../topics/dd2/target_geometry.md#dd2-fixed-ray-realization)。
  - **复核** 三席先独立消元、构造各支并攻击受限类，再逐式复读实际 D1F1–D1F9。平方根、交叉最近性及未指定六距由同一坐标核实；每个 \(0\le v\le m\) 以 \(u=\max\{v/L,|1-v|\}\) 回到准确域。能量三角用 \((b^2-u^2)(b^2-v^2)\ge0\) 核实，步长支内侧两锚可填成整段，输出锚距支在 \(L>1\) 的非下降区才活动。全包络分界 \(\tau_L=L/(1-L)^2\) 与旧两因子换序的范围分别注明，\(L=1\) 始终能量支；核零预算、零输出、共线交界、严格坏侧、各最大构形可外置输出锚使四标签互异，以及平方前的 \(r\ge L\)。一维 \(\sigma=0,L=1\) 的最大值 \(t/2\) 排除无维数限定的锐性；没有将所有目标都凸或固定的范围混入自由类。
- [x] `S03.08` 是否对完整局部 PPA 算子类尖锐？
  - **裁决** Sharp
  - **结论** 是，范围为维数至少二、固定 \(\lambda,\ell>0\)、目标自由的完整闭图类，锚下界为非正 \(-D\)，按每个受检输入的全部完整近端输出核某个最近锚及完整真残差。D1O1–D1O2 把全部单尺度可行数据放入同一给定 \(D\) 轮廓的完整图；最大值和反演坏侧保持。固定二次数据另有 C443：同一个完整图、固定零点射线，在每个正尺度达到三项包络取小所得的最优输出距离 \(m_L(\sigma)t\)。任意小坏尺度则能拼入一个固定图，并有任意小的完整不变局部窗和正位置/残差/使用图值帽。固定 \(\sigma\) 的轨道严格门之必要性由真实临界旋转/二周期独立给出，不能用只走一条坏边就投影结束的图替代。任意指定目标、一维、正 \(\Phi\)、连续单值或全对约束不自动继承该必要性。
  - **证据** [D1O1–D1O12 完整图及全部局部量词](../topics/dd2/dd1_recovery.md#dd1-complete-local-sharpness)、[C443 同一固定射线图的全尺度取等](../topics/dd2/dd1_recovery.md#dd1-homogeneous-fixed-ray-attainment)、[精确间隔、完整纤维及不变窗](../topics/dd2/dd1_recovery.md#dd1-local-sharp-gluing)、[实际临界轨道](../topics/dd2/dd1_recovery.md#dd1-critical-full-operators)、[C443 精确身份](../../CLAIMS.md#c443)、[C426 固定射线几何](../topics/dd2/target_geometry.md#dd2-fixed-ray-realization)。
  - **复核** 三席先重构补全、局部拼接与量词攻击，再逐式复读实际正文。核 \(J_{\lambda F}=J\)、闭图剪切、精确零集、零输入驻定、正距离输出唯一完整前像及零输出残差为零；严格输出锚距支未误写误差界取等。C443 核 \(\gamma\in[0,\pi]\)、射线缩放、所有前像及 \(t>0\) 的单点纤维。拼接用 \(c_n=4^{-n}\)、块半径 \(c_n/8\)，核全部跨块最近性、\(19/32\) 间隙、\(U_N=B(0,c_N/3)\) 和 \(R_N=b_*t_{N+1}\le c_N/64\) 的全部输出不变性。保给定轮廓的 \(\sigma_nt_n^2\le D(t_n)\)；剪归一化预算到 \(T(L)\) 只保严格坏侧，未冒充原最大值。整窗共同因子的充要性显式排除额外帽，并给残差帽反例；任意小局部构造仍适配正帽。真残差始终评价未截断的完整 \(F\)，同图全尺度与共同轨道继续分开。
- [x] `S03.09` 是否可以构造达到临界边界的实际算子？
  - **裁决** Sharp
  - **结论** 可以，原一般完整局部类的每个 \(L>0\) 均有精确 \(\Phi=-T(L)t^2,\psi(\rho)=\ell\rho\) 的实际失败算子。\(L>1/2\) 用二维连续单值线性旋转，\(L=1/2\) 用一维反射，\(L<1/2\) 用同一完整闭图上的任意小二周期；低支零集闭且在原点聚集。坏边同时取 \(a=t=\ell\rho\) 与锚积 \(-Tt^2\)，两个常数均最优，坏轨道始终留在完整不变小窗。另有 C444：在 \(n\ge2\) 中，每个 \(L\) 的固定射线完整图每尺度临界取等且两个常数同边最优，所有轨道却至多两条非驻定边结束，总长准确上界为 \((1+1/L)t_0\)。临界实际取等与存在持续不收敛轨道必须分开证明。
  - **证据** [实际算子分类及全部量词](../topics/dd2/dd1_recovery.md#dd1-critical-operator-classification)、[完整临界旋转／二周期](../topics/dd2/dd1_recovery.md#dd1-critical-full-operators)、[C444 同边最优而全轨道两步终止](../topics/dd2/dd1_recovery.md#dd1-critical-finite-termination)、[精确身份](../../CLAIMS.md#c444)。
  - **复核** 先独立重构临界算子再逐式对照实际源，核完整图坐标反演、所有纤维、精确零集、逐边锚、双向边及全部选择覆盖。低支 \(0\) 是聚点，已更正旧“离散闭目标”措辞；允许投影选择收敛不妨碍坏二周期反驳全选择保证。C444 用锥距离齐次性排除特殊输出成为特殊输入，核全初值与全选择、\(L=1/2\)、两项常数同边最优及总长取等；\(R<\epsilon/\max\{1,1/L-1\}\) 保不变小窗，全部残差用未截断完整纤维。位置帽先缩开球、数值帽再缩距离窗的审查异议已修复并复读。两组例子没有被误写为同一零集或同一逐输入数据。
- [x] `S03.10` 是否存在更强的第三分支或目前未发现的约束？
  - **裁决** Proved
  - **结论** 原二维及以上自由类的全参数第三项 \(b\) 在 \(L>1,\sigma>L/(L-1)^2\) 严格活动，边界与能量支并列；其值大于 1，不能改变严格下降的两段 \(T(L)\)。完整连续线性 \(J=bI\) 达到，\(L=2,\sigma=6\) 的准确值为 3 而旧两项给 \(\sqrt{52/5}\)。准确标量投影及完整图逐点实现排除了原同组前件下再删点或降低最大值的遗漏约束；固定图、目标、轨道与附加帽另验。维数限制有真实强化：C445 给一维自由闭目标的准确 \(m^{(1)}=\max\{L/(1+L),\min(Lb,b-1),\min(L(b-1),b)\}\) 及三段 \(T_1\)，在 \(L>1/2\) 严强于原 \(T\)，并有同一完整图的任意小临界二周期。该一维新身份不改原 C400，不暗加凸性。
  - **证据** [第三项分区及实际完整图](../topics/dd2/dd1_recovery.md#dd1-third-branch-and-scope)、[C445 一维准确域及三段门](../topics/dd2/dd1_recovery.md#dd1-one-dimensional-exact)、[一维真实临界轨道及全部选择不变窗](../topics/dd2/dd1_recovery.md#dd1-one-dimensional-critical-cycles)、[C445 精确身份](../../CLAIMS.md#c445)、[固定仿射目标的额外代价](../topics/dd2/target_geometry.md#dd2-affine-exact-geometry)。
  - **复核** 三路先独立推分支、受限几何和量词，再交叉核实际源。三项排序保 \(L=1\)、双项并列和第三项非下降域；双值完整纤维例核真残差可能严格小于所用图值范数 \(s/\lambda\)，截支图与全域扩张的动态不互移。一维归一最近锚后按三个输出位置穷尽，负向候选不可行时严格被基线压住；小预算平台未误当严格单调。临界两向块逐边核完整前像、精确零集、跨块最近性、闭图和 \(U_N,R_N\) 全选择不变，零尺度显式使用二次下界。另核一维凸例 \(\sqrt5-1\) 对 \(2/3\)，没有把二维凸自由锐性或一维闭目标三段门外推成任意固定目标的结论。
- [x] `S03.GATE` 在原协议指定换参下严格恢复 DD1 临界函数 T(L)，同时给出严格门的正面证明与等号或越界的实际失败证据。
  - **裁决** Sharp
  - **结论** 固定原非负二次校准，C285 的反射参数 \(c_\sigma=\sqrt{1+4\sigma}\)、\(\eta=1/L\) 恰恢复 \(T(L)=(1-L)/L^2\)（\(L\le1/2\)）或 \(1/(2L^2)\)（\(L\ge1/2\)）。\(\sigma<T(L)\) 给原两项的最小值 \(\kappa_\sigma<1\)、\(s\le b_\sigma t\) 及已知合法轨道的有限长和尾长；自动全选择续接另核覆盖及 \(b_\sigma t_0/(1-\kappa_\sigma)<d(x^0,U^c)\)。每个 \(\sigma\ge T(L)\) 都有实际最小缺陷系数恰为 \(\sigma\) 的完整闭图坏轨道：\(\sigma\le2\) 为定角旋转，\(\sigma\ge2\) 为同图任意小二周期。原自由类的严格门不能放宽；固定图成功、一般 \(\Phi\) 零合同及一维 \(T_1\) 各保独立身份。
  - **证据** [D1K1–D1K5 换参、原因子与合法路径](../topics/dd2/dd1_recovery.md#dd1-final-calibrated-gate)、[D1K6–D1K8 精确临界及越界失败](../topics/dd2/dd1_recovery.md#dd1-exact-supercritical-failure)、[C285 原参数门](../canonical/rleb_sharp_linear_frontier.md#rsl-threshold)、[原教师稿第七节](../manuscripts/dd1_2026_11_20/DD1_2026-11-20_教师讨论稿.md)、[全部参数最大值](../topics/dd2/dd1_recovery.md#dd1-four-point-reverse-sharp)、[C400 的指定目标反推](../topics/dd2/core.md#dd2-reverse)。
  - **复核** 三路独立重建代数、实际路径和量词，再对照实际源。核正数平方的分区、非空门、\(L=1/2\)、\(\sigma=0\)、二次零驻定、源中距离和反射符号；C285 旧候选包络不误当全参数准确 \(M\)。严格侧先估有限前缀再用覆盖，不用结论预设留域。坏侧核全部前像、真残差、\(\sigma=2\) 合锚、全选择不变窗及每条周期边的精确缺陷；帽为 \(\mu R/\lambda\) 或 \(\sqrt{2\sigma}R/\lambda\)，未把残差与步长混同。坏例只证明类保证的必要性，未声称所有坏侧图或全部选择必失败。
- [ ] `S03.SCOPES` 分别验收自由四点几何与完整局部 PPA 算子类的尖锐性，核对构造满足各自全部假设。

## §4 不要求统一 `\kappa<1`，究竟能够证明多强的收敛结论？

- [ ] `S04.01` DD2 在什么条件下只有严格距离下降？
- [ ] `S04.02` 何时能够保证距离趋于零？
- [ ] `S04.03` 何时能够保证点列本身收敛？
- [ ] `S04.04` 何时能够保证有限长度？
- [ ] `S04.05` 何时只有渐近正则性？
- [ ] `S04.06` 何时能够保证残差趋于零？
- [ ] `S04.07` 何时能确认极限属于指定的 `S`，而不只是 `\operatorname{zer}F`？
- [ ] `S04.08` 是否能够允许没有传统线性收敛率的迭代？
- [ ] `S04.09` 是否能够覆盖有收敛率但没有固定收缩系数的情况？
- [ ] `S04.10` 是否能够得到更一般的、无法由简单幂次描述的收敛过程？
- [ ] `S04.IMPLICATIONS` 给出严格距离下降、距离趋零、点收敛和有限长度之间的精确蕴含关系，逐条给出所需附加条件或反例。

## §5 有限长度是否有真正的一般函数型判据？

- [ ] `S05.01` 什么条件保证这样的 `\Theta` 存在？
- [ ] `S05.02` 能否直接由 `\Phi,\psi` 构造？
- [ ] `S05.03` 所需条件是否可以写成可计算的积分判据？
- [ ] `S05.04` 积分判据是充分、必要，还是某个函数类中的充要条件？
- [ ] `S05.05` `\Theta` 是否需要单调、连续、凹或可微？
- [ ] `S05.06` 是否允许非幂次、对数修正、振荡模函数？
- [ ] `S05.07` 是否可以弱化当前的可积性假设？
- [ ] `S05.08` 是否存在具有有限长度、却不满足当前候选势函数判据的例子？
- [ ] `S05.09` 是否可以建立最佳或近最佳的尾部长度包络？
- [ ] `S05.10` 有没有不使用这类势函数、却能得到更强结论的证明机制？
- [ ] `S05.F1` 定位作者原稿 F1 的精确版本并独立核验它如何吸收缺陷。
- [ ] `S05.F2` 定位作者原稿 F2 的精确版本并独立核验逆模条件及其作用。
- [ ] `S05.F3` 定位作者原稿 F3 的精确版本并独立核验被积函数和单调上包络条件。
- [ ] `S05.TELESCOPE` 独立重构原 F1–F3 对应的同一步长度势、望远镜求和与局部留域，逐项注明可以省去的条件。

## §6 幂次情形是否已经完整分类？

- [ ] `S06.01` `q>1`、`q=1`、`0<q<1` 的机制有什么本质区别？
- [ ] `S06.02` `q>1/2` 是否为有限长度的真正临界范围？
- [ ] `S06.03` `q=1/2` 的反例是否满足全部算子与近端量词？
- [ ] `S06.04` `q<1/2` 是否存在更强的失败机制？
- [ ] `S06.05` `pq=2` 时的尖锐常数是什么？
- [ ] `S06.06` `pq>2` 是否能够进一步削弱？
- [ ] `S06.07` 是否存在使当前指数条件成为必要条件的明确算子子类？
- [ ] `S06.08` 在 `p,q` 固定时，能否刻画最优收敛速率？
- [ ] `S06.09` 是否能够构造达到速率上界的算子？
- [ ] `S06.10` 是否能够从一般函数判据直接恢复幂次分类，而不是分别重复证明？
- [ ] `S06.ABOVE` 针对原协议的幂次误差界，在 \(pq>2\) 区域按 \(q\) 分区验收距离、点与有限长度结论。
- [ ] `S06.CRITICAL` 在 \(pq=2\) 区域逐分支证明临界常数、严格侧和等号侧的结论与构造。
- [ ] `S06.BELOW` 在 \(pq<2\) 区域逐分支验收正面结果、失败范围和实际近端反例。
- [ ] `S06.TAIL` 独立复核 \(\alpha=2-1/q\) 的实际总长度估计，明确 \(q\) 的范围、常数选择、局部不变性及边界。

## §7 DD2 是否真正扩大了可处理的算子类？

- [ ] `S07.01` 是否存在 DD2 成立、DD1 不成立的算子？
- [ ] `S07.02` 是否存在 DD2 成立、旧完整 RLEB 不成立的算子？
- [ ] `S07.03` 是否存在非单调算子，满足 DD2 但不满足经典单调性路线？
- [ ] `S07.04` 是否存在只有 Hölder 误差界、没有线性度量次正则性的算子？
- [ ] `S07.05` 是否存在非孤立零点集实例？
- [ ] `S07.06` 是否存在多值预解式实例？
- [ ] `S07.07` 是否存在非凸零点集实例？
- [ ] `S07.08` 是否存在真正利用非线性 `\Phi` 形状的实例，而不是只把它压成一个常数？
- [ ] `S07.09` DD2 的函数型补偿是否在某些算子类中比所有常数型包络更强？
- [ ] `S07.10` 是否存在旧方法无法处理、而 DD2 能证明有限长度的实际模型？
- [ ] `S07.EXAMPLES` 逐一核验关键实例的完整定义、参数、零点集、工作域、所有合法输出、失效的旧假设及新结论。

## §8 哪些结论不能进一步加强？

- [ ] `S08.01` 一般严格下降是否必然产生有限长度；
- [ ] `S08.02` Hölder 误差界是否足以保证有限长度；
- [ ] `S08.03` 零点锚定次单调性是否足以保证 Fejér 单调性；
- [ ] `S08.04` 约化收敛是否足以保证完整 shadow 收敛；
- [ ] `S08.05` 正则性是否会自动传递到所有约化算子；
- [ ] `S08.06` 一个函数型补偿判据是否必然具有反向必要性；
- [ ] `S08.07` 有限长度是否必然伴随某种固定收敛阶；
- [ ] `S08.08` 改变松弛参数后，原来的 DD2 条件是否仍然充分。
- [ ] `S08.ROTATION` 严格复核原二维旋转反例，核对所有近端与算子量词。
- [ ] `S08.POWER` 严格复核非单调幂次例子，核对完整真残差与轨道。
- [ ] `S08.BOUNDARY` 给八个猜想补齐实际边界攻击，保存已反驳版本的精确反例及失败机制。

## §9 约化前向表示是否真正完成？

- [ ] `S09.01` 在什么条件下存在 `P=CC^*` 的有效分解？
- [ ] `S09.02` 约化空间如何定义？
- [ ] `S09.03` 原始近端关系怎样精确转化为约化前向迭代？
- [ ] `S09.04` 约化映射何时单值、多值、局部有定义？
- [ ] `S09.05` 约化零点集与原始零点集之间究竟是什么关系？
- [ ] `S09.06` 目标集经 `C^*` 映射后是否闭合？
- [ ] `S09.07` 投影算子何时存在？
- [ ] `S09.08` 原始次单调性函数如何传递到约化空间？
- [ ] `S09.09` 原始正则性函数如何传递到约化空间？
- [ ] `S09.10` 在投影、核空间及非满射情形下，是否存在失效机制？
- [ ] `S09.11` 传递结论是否仍保留一般非线性模函数？
- [ ] `S09.12` 是否可以恢复 Alcantara 的已知二次参数版本？
- [ ] `S09.SOURCE` 逐式核对 Alcantara 原文的空间、逆算子、预条件器和约化表示，注明版本和位置。
- [ ] `S09.DOMAINS` 逐式核对约化表示的定义域、图对应、完整或允许纤维以及适用量词。

## §10 Shadow recovery 是否能够形成独立的完整定理？

- [ ] `S10.01` 约化极限如何与原始零点联系？
- [ ] `S10.02` 为什么有界 recovery 不自动意味着完整 shadow 收敛？
- [ ] `S10.03` 为什么 demiclosedness 不自动保证极限唯一？
- [ ] `S10.04` 如何保证所有弱聚点落在正确的 fiber？
- [ ] `S10.05` fiber 不唯一时能得到什么最强结论？
- [ ] `S10.06` 在什么条件下获得强收敛？
- [ ] `S10.07` Lipschitz recovery 是否保证 shadow 的有限长度，而不仅仅是收敛？
- [ ] `S10.08` Hölder recovery 是否也能保留有限长度？若不能，缺少什么？
- [ ] `S10.09` DD2 的尾部误差率能够传递多少？
- [ ] `S10.10` 哪些 recovery 条件可以从算子结构本身验证？
- [ ] `S10.11` 有限维情况下哪些假设可以自动化简？
- [ ] `S10.12` 是否存在更弱而仍然充分的恢复机制？
- [ ] `S10.R01` projected convergence；
- [ ] `S10.R02` projected zero identification；
- [ ] `S10.R03` bounded recovery；
- [ ] `S10.R04` weak shadow convergence；
- [ ] `S10.R05` strong shadow convergence；
- [ ] `S10.R06` Lipschitz recovery；
- [ ] `S10.R07` nonlinear/Hölder recovery；
- [ ] `S10.R08` shadow finite length；
- [ ] `S10.R09` tail-error transfer。
- [ ] `S10.SCOPES` 逐条注明九类恢复的对象为实际 shadow、投影 shadow 或指定 recovery selection，独立核验局部有界性、Lipschitz 与全选择量词。

## §11 双重残差和正则性传递是否真正形成新结论？

- [ ] `S11.01` 两种残差是否定义在不同位置？
- [ ] `S11.02` 两者是否存在严格的图对应？
- [ ] `S11.03` 原算子误差界是否蕴含辅助算子误差界？
- [ ] `S11.04` 反向蕴含何时成立？
- [ ] `S11.05` 线性、Hölder、一般 gauge 三类误差界如何分别传递？
- [ ] `S11.06` 两种残差能否共同产生严格更强的下降包络？
- [ ] `S11.07` 是否存在一个误差界很弱、另一个误差界很强的实际算子？
- [ ] `S11.08` 能否建立直接可检验的联合补偿判据？
- [ ] `S11.09` 该判据能否恢复 DD1 和 Alcantara Proposition 3.4？
- [ ] `S11.10` 有哪些传递结论只依赖代数恒等式，哪些依赖闭图、局部可逆或正则性？
- [ ] `S11.GRAPH` 交出双残差与正则性传递的精确逻辑关系图，给每个箭头附条件、证明或反例。

## §12 DD2 是否能够提供真正完整的迭代分析？

- [ ] `S12.01` 能否得到 Fejér 或 quasi-Fejér 型估计？
- [ ] `S12.02` 能否建立实际步长的有限长度？
- [ ] `S12.03` 能否得到残差平方可求和？
- [ ] `S12.04` 能否得到残差的一般非线性可求和估计？
- [ ] `S12.05` 能否得到 best-iterate 收敛率？
- [ ] `S12.06` 能否得到 ergodic 收敛率？
- [ ] `S12.07` 能否得到 pointwise 残差率？
- [ ] `S12.08` 能否建立明确的复杂度界？
- [ ] `S12.09` 哪些速率是尖锐的？
- [ ] `S12.10` 哪些收敛结论需要附加有界性或紧性？
- [ ] `S12.11` 什么时候可以得到 Q-linear、R-linear、次线性或超线性收敛？
- [ ] `S12.12` 哪些结论能够在没有统一 A 的情况下继续成立？
- [ ] `S12.RATES` 逐个区分迭代点、零集距离、残差、best-iterate 与 ergodic average 的速率对象、量词及边界。

## §13 自适应松弛与非精确算法是否完成？

- [ ] `S13.01` 松弛参数的真实可行区域是什么？
- [ ] `S13.02` 如何从一般 `\Phi` 推导对应能量不等式？
- [ ] `S13.03` 是否存在显式的自适应选择规则？
- [ ] `S13.04` 当 `\alpha_k\to0` 或接近边界时会发生什么？
- [ ] `S13.05` 是否需要统一正下界？
- [ ] `S13.06` 哪些结论对超松弛仍然成立？
- [ ] `S13.07` 一般下降函数是否能够在松弛迭代中保持？
- [ ] `S13.08` 有限长度是否仍然成立？
- [ ] `S13.09` 可求和误差、相对误差以及不可求和误差分别允许到什么程度？
- [ ] `S13.10` 是否能够保留原来的收敛速率和 shadow recovery？
- [ ] `S13.11` 是否可以构造误差条件不充分的严格反例？
- [ ] `S13.12` 是否存在比既有自适应规则更宽的可行参数区域？
- [ ] `S13.VERSIONS` 分别登记精确算法与非精确算法的 Claim 版本并核对二者的假设、输出和误差量词。

## §14 Chambolle–Pock、Douglas–Rachford 等应用是否真正落地？

- [ ] `S14.01` 原始问题是什么？
- [ ] `S14.02` 算子分裂如何定义？
- [ ] `S14.03` DD2 应施加在哪个算子或哪个约化变量上？
- [ ] `S14.04` 如何验证非线性次单调性？
- [ ] `S14.05` 如何验证非线性正则性？
- [ ] `S14.06` 如何计算或估计补偿函数？
- [ ] `S14.07` 近端或分裂子问题是否良定？
- [ ] `S14.08` 约化有限长度是否成立？
- [ ] `S14.09` 原始变量和对偶变量是否都收敛？
- [ ] `S14.10` 是否有完整 shadow recovery？
- [ ] `S14.11` 能否得到残差与收敛速率？
- [ ] `S14.12` 与原有算法定理相比，是否获得严格更弱的假设、更强的结论或新的可验证模型？
- [ ] `S14.CP` 汇总并复核 Chambolle–Pock 对原 §14 十二问的逐项具体验证。
- [ ] `S14.DR` 汇总并复核 Douglas–Rachford 对原 §14 十二问的逐项具体验证。
- [ ] `S14.THEOREM` 提交至少一个具有完整对象、条件与证明的实际算法应用定理及可核算子实例。
- [ ] `S14.APPLICABILITY` 逐一验收其余被声称覆盖的算法。仅有候选机制的算法按原协议列为潜在应用。

## §15 我们究竟恢复了哪些已有理论？

- [ ] `S15.01` 原论文真正证明了什么？
- [ ] `S15.02` 精确假设是什么？
- [ ] `S15.03` 我们的哪个定理可以恢复它？
- [ ] `S15.04` 恢复是完全的，还是只恢复其某个特殊结论？
- [ ] `S15.05` 哪些假设无法恢复？
- [ ] `S15.06` DD2 是否真的给出了严格推广？
- [ ] `S15.07` 如果只是另一个充分条件，如何证明两者不可比较？
- [ ] `S15.08` 是否存在实际算子证明严格分离？
- [ ] `S15.09` 哪些数学机制相同，哪些机制不同？
- [ ] `S15.10` 是否存在更早的等价结果？
- [ ] `S15.L01` Luke–Tam 的次单调性及 PPA 收敛结果；
- [ ] `S15.L02` 旧 RLEB 的非线性 RL 主定理；
- [ ] `S15.L03` Alcantara 2026 的普通 PPA、约化前向和 shadow 理论；
- [ ] `S15.L04` 既有 Hölder metric subregularity 理论；
- [ ] `S15.L05` gauge 型误差界与非线性下降理论；
- [ ] `S15.L06` 相关的 KL、Lyapunov、有限长度及分裂算法理论。

## §16 DD2 的新颖性必须拆分验收

- [ ] `S16.A` 新公式。是否只是已有等式的代数改写？
- [ ] `S16.B` 新定理。是否在精确量词和假设下产生此前没有得到的结论？
- [ ] `S16.C` 新刻画。是否真正建立了必要、充分、尖锐或可反解的结构关系？
- [ ] `S16.D` 新算子类。是否严格包含旧理论未覆盖的算子？
- [ ] `S16.E` 新收敛机制。是否摆脱了统一线性收缩，并获得独立的有限长度证明？
- [ ] `S16.F` 新算法应用。是否解决了此前算法定理无法处理的具体模型？
- [ ] `S16.G` 新方法。四点几何是否带来了传统能量估计没有捕获的真实约束？
- [ ] `S16.H` 新临界现象。二次缺陷、Hölder 指数、有限长度阈值是否具有独立的尖锐数学意义？

## §17 每条重要定理必须通过哪些审查？

- [ ] `S17.01` 对象是否良定；
- [ ] `S17.02` 量词是否正确；
- [ ] `S17.03` 所有隐含假设是否已经列出；
- [ ] `S17.04` 边界情况是否遗漏；
- [ ] `S17.05` 空输出或空图导致的真空成立是否排除；
- [ ] `S17.06` 定理引用的全部适用条件是否满足；
- [ ] `S17.07` 局部条件能否沿轨道持续使用；
- [ ] `S17.08` 是否出现循环证明；
- [ ] `S17.09` 能否用低维算子构造反例；
- [ ] `S17.10` 能否用非单调、多值、非孤立零点集攻击；
- [ ] `S17.11` 证明是否混淆必要性与充分性；
- [ ] `S17.12` 最优性是否有独立取等或逼近构造；
- [ ] `S17.13` 计算实验能否复现；
- [ ] `S17.14` 是否存在另一条独立证明路线；
- [ ] `S17.15` 是否存在尚未解决的致命 objection。
- [ ] `S17.REVIEW` 按具体 Claim 版本保存独立重推、反例攻击和 15 项审查结果，逐一裁决所有仍成立的致命异议及其影响。

## 第八部分 · 28 个深层问题

- [ ] `Q01` DD1 与 DD2 的最强共同数学结构是什么？
- [ ] `Q02` DD2 是否能够定义一个真正统一的补偿泛函？
- [ ] `Q03` 这个泛函是否具有天然的逆映射或对偶描述？
- [ ] `Q04` 能否定义最优正则性强度或最优次单调性缺陷？
- [ ] `Q05` 这种最优性是否仅在特定函数类中成立？
- [ ] `Q06` DD1 的分段结构在一般函数情形中如何体现？
- [ ] `Q07` 是否存在新的分段、相变或临界函数？
- [ ] `Q08` 一般函数补偿能否完整刻画某一类 PPA 算子的下降行为？
- [ ] `Q09` 固定线性收缩究竟可以削弱到什么程度？
- [ ] `Q10` 在什么意义下有限长度是比统一 A 更弱的目标？
- [ ] `Q11` 是否存在一般函数条件下有限长度的最优判据？
- [ ] `Q12` 有限长度与残差可求和之间有哪些必要关系？
- [ ] `Q13` 哪些非线性收敛率可以由补偿函数直接计算？
- [ ] `Q14` 是否存在不能用通常幂次衡量的收敛机制？
- [ ] `Q15` 如果未来放弃有限长度，现有 DD 框架能保留多少数学信息？
- [ ] `Q16` 约化 PPPA 在什么条件下完整继承 DD2？
- [ ] `Q17` 哪些条件会在降维中丢失？
- [ ] `Q18` 原空间与约化空间的函数指标能否双向传递？
- [ ] `Q19` Shadow recovery 的最弱可验证机制是什么？
- [ ] `Q20` 一般函数补偿在 primal-dual 算子中是否具有组合规律？
- [ ] `Q21` 是否可以建立可复用的 DD2 splitting calculus？
- [ ] `Q22` 是否存在具体应用证明这种 calculus 超过现有定理？
- [ ] `Q23` 哪些结论已经尖锐？
- [ ] `Q24` 哪些临界边界仍没有算子构造？
- [ ] `Q25` 哪些候选命题已经被反例否定？
- [ ] `Q26` 哪些路线只是证明技术不足，而不是命题错误？
- [ ] `Q27` 还有哪些尚未发现的几何约束可能改善当前边界？
- [ ] `Q28` 最终真正限制 DD2 继续推广的数学障碍是什么？

## 第九部分 · 10 项强制交付物

- [ ] `D01` Canonical Theorem Statements。包括 DD1、DD2、有限长度、约化传递、shadow recovery、算法应用等真正已经证明的结果。
- [ ] `D02` 完整证明。每个结果给出独立可审查的证明，而非证明概要。
- [ ] `D03` Dependency Graph。明确每个定理依赖哪些定义、引理、文献事实和附加假设。
- [ ] `D04` Counterexample and Sharpness Atlas。系统整理有效反例、边界构型、严格分离例子及其攻击目标。
- [ ] `D05` Literature Comparison Matrix。逐项比较旧 RLEB、Luke–Tam、Alcantara 以及其他相关理论。
- [ ] `D06` Operator-Class Inclusion Map。明确不同理论所处理算子类的严格包含、非严格包含和不可比较关系。
- [ ] `D07` DD Functional Compensation Map。展示 `\Phi,\psi`、下降函数、有限长度势函数、残差和收敛率之间的真实数学关系。
- [ ] `D08` Algorithm Transfer Dossier。完整记录从普通 PPA 到约化 PPPA，再到 shadow recovery 和分裂算法的传递条件。
- [ ] `D09` Reproducible Experiments。若使用计算实验，保存代码、参数、精度、版本、随机种子及实际输出。实验只能作为证据，不能替代证明。
- [ ] `D10` Research Frontier Report。明确剩余的 proof obligations、致命障碍、竞争机制与下一阶段最有价值的问题。

## 最终六问

- [ ] `Z01` 我们现在到底证明了什么？ 给出 DD1、DD2 及全部推广结果的精确数学结论，而不是概念描述。
- [ ] `Z02` 我们究竟理解了什么？ 说明次单调性、正则性、下降模函数、有限长度及算法恢复之间真实的数学机制。
- [ ] `Z03` 我们究竟推广了什么？ 严格展示相对于旧 RLEB、Luke–Tam、Alcantara 和其他相关文献的恢复、严格推广、不可比较关系与新增算子类。
- [ ] `Z04` 我们究竟能处理什么算法？ 明确哪些普通 PPA、预条件 PPA、原始—对偶及分裂算法已有完整定理，哪些仍只有候选机制。
- [ ] `Z05` 我们的边界究竟在哪里？ 给出尖锐界、反例、不可推出性质以及尚未解决的 proof obligations。
- [ ] `Z06` 如果继续研究，最值得突破的是什么？ 必须依据已经确认的数学事实提出下一阶段真正有信息价值的问题，而不是机械增加定理数量。

## 总目标与项目验收复核

- [ ] `META.STATES` 按第十部分复查全部成果的数学状态，保留真值、范围和可靠性边界。
- [ ] `META.CLAIMS` 核实每个重要 Claim 都有原协议列出的 Exact Statement、Objects、Domain、Quantifiers、Assumptions、Conclusion、Dependencies、Evidence、Counterevidence、Status 和 Related Files。
- [ ] `META.PERSISTENCE` 复核第十一部分的可恢复性，从远端 main 与研究地图重建已验收结果，核查逐项提交、持久化与证据定位。
- [ ] `META.GOAL` 用可复核的数学证据直接回答原协议开篇的核心问题，交代统一理论的成立范围、严格新结果、既有机制和已证明的障碍。
