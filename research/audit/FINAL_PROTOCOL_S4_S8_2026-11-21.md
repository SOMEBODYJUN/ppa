# 原协议 §4–§8 最终数学验收审计（2026-11-21）

本文件固定 §4–§8 的题号、量词和状态。`Proved/Sharp/Recovered/Conditional/Partial/Open/Refuted/Invalid` 只指写明的对象类和工作窗；不能把几何层结果升级为任意算子层结果。

## §4 不同收敛结论

设允许轨道满足 (t_{k+1}le Q(t_k))，其中 (t_k=d(x^k,S))，并令 (s_k=|x^{k+1}-x^k|)。同一步平面引理或 C401 给出的是距离和步长的两种不同不等式。

1. **严格距离下降：Proved conditionally。** 只要逐尺度包络 (Q(t)<t)，则每一步严格下降。连续非减 (Q) 可沿轨道迭代；不连续或只在逐尺度成立时，不能自动得到统一比较函数。
2. **距离趋零：Proved conditionally。** 若 (Q) 连续非减、(Q(0)=0)、(Q(t)<t) 且轨道留在工作窗，则单调极限 (l) 满足 (lle Q(l)<l)，故 (l=0)。仅有 (Q(t)<t) 而无上半连续性时，可能有正极限，故原命题需加比较条件。
3. **点列收敛：Conditional。** 需要有限长度、全锚 Fejer/Opial，或另一个点列紧性和唯一聚点机制。距离趋零本身不排除沿非孤立零集漂移；core.md 的闭仿射切向漂移例给出反例。
4. **有限长度：Conditional。** C401 的 (Theta) 望远镜或同一步严格耗散给出 (sum s_k<infty)。严格距离下降没有这种结论，L=1、(A(t)=t/(1+t)) 的旋转图例有 (t_k	o0) 但 (sum s_k=infty)。
5. **渐近正则性：Proved conditionally。** 若有 (sum s_k^2<infty)，则 (s_k	o0)；这不推出 (sum s_k<infty) 或点收敛。
6. **残差趋零：Conditional。** 输出误差界和 (s_k	o0) 给 (a_k=d(y^k,S)	o0)，但 (r_F(y^k)	o0) 需要残差下界、图闭性或反向正则性；单独的上界 (alepsi(r_F)) 不能反推残差。
7. **极限属于指定 S：Conditional。** 需要 (S) 闭且 (d(x^k,S)	o0)，并且点列有极限/聚点；只得到 (operatorname{zer}F) 时不能识别较小的指定 (S)。
8. **无统一线性率：Proved conditionally。** 连续比较函数、积分势和非幂次 (Theta) 允许没有固定 (kappa<1) 的迭代。结论是比较级或势级率，而非自动的 Q-linear 率。
9. **变比率收敛：Proved conditionally。** 若 (Q(t)/t	o1) 但 (Theta) 可积，仍可得到距离和长度；若 (Theta) 不可积，只能保留距离/平方和结论。
10. **一般收敛过程：Partial。** 对数修正、分段、非幂次模可以由 Q 和 (Theta) 处理；任意振荡函数需非减上包络，统一分类尚未完成。

## §5 一般函数有限长度与 F1–F3 审查

令 (eta(s)=psi(s/lambda))、(chi(t)=inf{s:s+eta(s)ge t})。在标准负缺陷情形，若 (2D(t)le(1-delta)chi(t)^2)，则
[
 sgechi(t),qquad t^2-a^2gedelta s^2,qquad
 sle {2overdelta},[Theta(t)-Theta(a)],quad
 Theta(t)=int_0^t {u,duoverchi(u)}.
]
有限前缀 (sum sup s) 小于工作域余量时可迭代留域，(Theta(0)>-infty) 给尾长。

1. **势存在条件：Conditional/Proved。** 上式是直接充分条件；一般 gauge 只需可测正的 (chi) 和 (int_0^t u/chi(u),du<infty)。
2. **由 Phi,psi 构造：Proved for the dissipative class。** (chi=(I+eta)^{-1})，正缺陷时可用 (2Phi+deltachi^2>0) 的正耗散替代 (2D) 条件。没有正耗散时不能构造同一势。
3. **可计算积分判据：Proved conditionally。** (int_0^arepsilon u/chi(u),du<infty) 是该势证明的直接判据；它对任意轨道的必要性尚未证明。
4. **充分/必要：Partial.** 对同一步耗散证明是充分；在一维径向 sharp 模型中积分发散给无限长度反例，但一般算子类的必要性 Open。
5. **Theta 正则性：Conditional.** 绝对连续、非减即可作望远镜；凹性用于扰动的 (Delta_Theta) 控制，不是精确步定理的必要条件。
6. **非幂次/对数/振荡：Partial.** 单调对数修正可直接代入；振荡模需包络，包络可能丢失尖锐性。
7. **弱化可积性：Open in general.** 其他 Lyapunov 或 KL 机制可能比 (Theta) 强，但当前没有一般等价判据。
8. **有限长度而不满足候选势：Proved possible.** 可选的几何块/闭链势能给有限长度，未必写成 (u/chi(u)) 的单变量势；因此当前势不是必要条件。
9. **尾部最优性：Conditional.** C401 给势差尾预算；径向取等模型达到其阶，固定常数之外的全类最佳性 Open。
10. **其他证明机制：Proved examples/Partial general。** 全锚 Fejer、KL、闭链几何可独立给长度；尚无覆盖所有 DD2 gauge 的统一机制。

F1–F3 的独立结论：F1 是 (2Dle\chi^2/2)；F2 是 (b(t/2)=\lambda\psi^{-1}(t/2)le t/2)，只负责把逆模换成 (chi)；F3 是 (h(t)=2t/[mu(t)chi(t)]) 有非增可积上包络。三者合用是充分条件，不是必要条件；直接使用 C401 的 (chi) 条件可以去掉 F2 和二分步骤。F1/F2/F3 失败只说明该证明路线失效，不说明长度必失败。

## §6 幂次分类

设 (Phi(t)ge-Mt^p)、(ale K(s/lambda)^q)，写 (h=K/lambda^q)，(chi) 由 (t=s+hs^q) 定义。

1. **(0<q<1)：Proved for C399 class。** (chi(t)sim h^{-1/q}t^{1/q})，势积分有限当且仅当 (q>1/2)。若 (p>2/q)，或 (p=2/q) 且 (2M<h^{-2/q}=lambda^2K^{-2/q})，则有限长度；临界反向常数等号可由旋转图实现。
2. **(q=1)：Conditional/Proved split。** 若 (h<1)，三角形直接给 (ale h(t+a))，故局部 Q-linear、任意有限 (M) 均可吸收。若 (hge1)，回到能量门：(p>2)，或 (p=2) 且 (2M<h^{-2})；坏门允许保半径旋转。
3. **(q>1)：Proved local geometric mechanism。** 由 (ale h s^q) 与 (sle t+a) 先排除 (age2t)，再得 (ale h(3t)^q=o(t))，最终 (ale t/2)。因此任意有限 (M)、任意 (p>0) 在足够小工作窗内有几何收缩和有限长度；简单 (pq>2) 分区并非真实阈值。
4. **(pq>2)：Conditional.** 对 (q<1) 是 C399 的超临界门；对 (qge1) 需按上面两种机制处理，不能把乘积条件当统一必要条件。
5. **(pq=2)：Sharp in (0<q<1) class。** 常数门 (2M<h^{-2/q}) 精确；等号旋转保持半径或产生无穷长度。
6. **(pq<2)：Refuted as a universal finite-length claim。** 对 (q<1) 可取 (a=t)、(s=c t^{1/q})、(\Phi=-s^2/2=-c^2t^{2/q}/2)，得到半径不降旋转；对 (qle1/2) 即使 (M=0) 也有无限长度。
7. **(q=1/2) 反例：Sharp/Proved.** (H=\mathbb R^2)、(S=\{0\})、(T(y)=y+\|y\|Jy)、(F=(T^{-1}-I)/\lambda) 是全域单值闭图；输出满足 (a=\sqrt{r_F})，(D=0)，且 (s_k\asymp1/k)，所以 (t_k\to0) 而总长发散，量词是完整图而非选定支。
8. **(q<1/2)：Sharp failure.** 右三角径向旋转 (s=c t^{1/q})、(a=(t^2-s^2)^{1/2}) 给 (s_k\asymp t_k^{1/q})，长度积分发散。
9. **最优速率：Conditional.** (0<q<1)、超临界缺陷给 (t_{k+1}le t_k-c t_k^{2/q-1})，故 (t_k=O(k^{-q/(2-q)})) 在取等径向类中尖锐；(q>1) 局部几何级率；一般算子类仍需覆盖。
10. **从一般函数恢复：Proved for regular variation。** 把 (chi) 代入 (Theta) 即得上述指数；对任意非幂次函数只保留积分判据，不应强行写成 (pq) 分类。

这说明原先把 (pq>2,=2,<2) 作为所有 q 的统一分类是 **Invalid**；真实分区是 (0<q<1) 的乘积门、(q=1) 的线性门和 (q>1) 的超线性几何门。

## §7 实际算子类

1. **DD2 成立而 DD1 不成立：Proved examples。** C399 的非线性 gauge、C401 的一般势和非线性缺陷不满足固定线性 RLEB，但满足 DD2 条件。
2. **DD2 成立而旧完整 RLEB 不成立：Proved by selected/full-graph separation.** C408 的 (G(y)=\{y,y^3\}) 只选线性支时可满足选定关系，完整真残差界失败；故必须区分 selected 与 full graph。
3. **非单调算子：Proved example。** (F(y)=-r y+r^{1/3}Jy) 的连续单值 resolvent 在局部可逆，能给 (q=3/4) gauge 和 DD2 下降，但不走经典单调性路线。
4. **只有 Holder 界：Proved examples。** C399 的 (q\in(1/2,1)) 模型没有线性 metric subregularity，却有有限长度。
5. **非孤立零集：Proved.** 闭仿射零线的法向旋转和切向漂移例给非孤立 (S)。
6. **多值预解式：Conditional/Proved.** 允许关系可取任意子图；完整多值 resolvent 的全图覆盖需要额外闭图和非空条件。
7. **非凸零集：Proved.** 两点或离散闭目标的两锚构造满足 DD2；固定凸目标的 sharpness 不随之自动成立。
8. **真正非线性 Phi：Proved geometry/Conditional operator.** (Phi(t)=-Mt^p) 的 p 进入缺陷吸收和临界常数；实际算子达到需逐族构造。
9. **函数包络强于常数包络：Proved.** (M(t)) 的非线性正则项和 (chi(t)) 依赖尺度，能在小尺度满足可积势而任何统一线性常数都无法表达其临界行为。
10. **旧方法未处理而 DD2 可处理：Conditional.** C399/C405 给实际模型；与所有旧定理的严格不可比较关系尚未逐类闭合。

## §8 八个猜想的攻击

1. 严格下降必有限长度：**Refuted**，L=1 调和旋转例。
2. Hölder 误差界必有限长度：**Refuted**，q=1/2 完整图反例；q<1/2 更强。
3. 最近锚次单调性必 Fejer：**Refuted**，切向漂移和只对某个最近锚的两锚构形。
4. 约化收敛必完整 shadow 收敛：**Refuted**，非唯一 fiber、远 kernel 和投影闭性反例。
5. 正则性自动传所有约化算子：**Refuted**，只选近解 lift 或 (G(y)=\{y,y^3\}) 的完整真残差障碍。
6. 函数补偿判据必反向必要：**Refuted in general / Proved for free geometry**，固定算子 coverage、凸性和闭图会损失必要性。
7. 有限长度必有固定阶：**Refuted**，对数/振荡势和有限终止模型没有共同幂阶。
8. 改变松弛参数后原 DD2 仍充分：**Refuted**，(alpha=2eta) 的符号翻转、(alpha_k	o0) 的保半径轨道和临界旋转。

## §4–§8 总结

已严格裁决的核心边界是：距离下降、距离收敛、点收敛、平方可和、有限长度和残差趋零彼此独立；F1–F3 是一条充分证明路线；幂次分类只在 (0<q<1) 由 (pq) 控制；q=1 和 q>1 有不同机制。未完成的是任意振荡 gauge 的必要条件、固定凸/连续单值算子层的全局 sharpness、以及与所有旧 RLEB 定理的严格算子类包含关系。
