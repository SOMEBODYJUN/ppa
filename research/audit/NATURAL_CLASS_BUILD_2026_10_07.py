"""Reproduce this source's complete LF partition; does not edit shared registries."""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "history/sources/历史总包_2026-09-14/菠萝_RL与广义次正则研究资产_2026-09-14_v2_真实超边图/01_RL_PPA核心理论/05_实例与反例/支撑函数与法锥_自然类推导.md"
CAN = "research/canonical/support_normal_natural_class.md"
AUD = "research/audit/NATURAL_CLASS_COVERAGE_2026_10_07.md#sn-audit"
EXPECTED = "abe082412883506ab76bdcc2b653f7971ecacb82205dd7cbe632186c84e8c2c9"
data = (ROOT / SOURCE).read_bytes()
assert hashlib.sha256(data).hexdigest() == EXPECTED
assert data.endswith(b"\n") and b"\r" not in data
assert data.count(b"\n") == 528 and len(data) == 23025
lines = data.decode().split("\n")[:-1]
assert len(lines) == 528

# Each record is an independently disposable assertion or one contiguous proof
# of it. Formatting-only gaps receive explicit organization rows below.
# start,end,label,type,disposition,anchor,claims,reason,remaining
S = [
(1,3,"项目、日期与任务身份","provenance","deferred","sn-source","","保留来源自述；不回溯认证旧任务执行","历史任务及日期身份不参与数学证明"),
(5,5,"两类自足及未解决完整PDE的状态报告","status","deferred","sn-source","","新直接证明另行给出；旧审查状态不等于新接收","来源原审查行为未核，完整工程模型未匹配"),
(9,9,"自然来源及非固定shear的摘要","interpretation","superseded","sn-source","","保留显式原关系；自然性不是已核外部应用定理","四份原论文与完整工程方程另核"),
(13,13,"独立RL和完整存在系数摘要","theorem","rewritten","sn-triangular","C191-v1","SN2–8重构全输入法向逆及全活动面比较","无同对象数学缺口；先行性未核"),
(14,14,"独立高阶ordinary EB系数","theorem","rewritten","sn-triangular","C191-v1","SN9对完整图全部值取inf","不把最近距离和最远距离互换"),
(15,15,"两证书严格匹配门","corollary","rewritten","sn-compatible","C191-v1","SN10分开输入对尺度与实际距离窗","该门只是聚合证书充分条件"),
(17,17,"三个原生输入可分别判定","interpretation","rewritten","sn-compatible","C191-v1","RL上界、EB下界与法向强单调性分别证明","不声称一般模型自动可计算"),
(19,19,"反馈类的独立存在与EB摘要","theorem","rewritten","sn-feedback","C192-v1","SN13–16给全域存在和小条带唯一性","不把小条带单值性移至全域"),
(21,21,"两类一概排除固定旧证书但partial可用","boundary","superseded","sn-failures","C193-v1","A须C非零；C={0}时J为投影且τ=0有效；只定义SN17和直接更新界","旧命名PSM/almost-averaged定理未导入"),
(27,27,"Carpick原文及Hertz面积阶数paper fact","literature","deferred","sn-source","","本轮未读取该一手原页；不从源已核标签升级","原页版本、公式、量词和应用门待核"),
(29,29,"Gfrerer–Outrata–Valdman摘要paper fact","literature","deferred","sn-source","","本轮未重验摘要；不得据此导入coderivative定理","原始摘要及任何具体定理另核"),
(31,31,"Carstensen塑性支撑函数/法向律paper fact","literature","deferred","sn-source","","数学定义已独立证明；外部归属未本轮核验","指定全文式2.15–2.16及版本另核"),
(33,33,"Kanno完整接触模型及不冒称解决","literature","deferred","sn-source","","保留工程边界；本轮不认证论文数学陈述","原文模型与本页F的逐项身份桥未闭"),
(37,44,"reduced本构变量、外驱动、法向及应用边界","model-definition","superseded","sn-object","C191-v1;C192-v1","完整原图直接定义；变量解释不作原生工程已解身份","单位、边界条件、完整原方程和应用证据另核"),
(50,57,"紧凸D、支撑函数、f外点和d/R","definition","rewritten","sn-object","C191-v1","SN1分型d_D与R_D，支撑面在SN2–5直接证明","无"),
(59,63,"含0闭凸法向集和非对称强单调矩阵","definition","rewritten","sn-object","C191-v1","允许C={0}；对称部分强下界明确","障碍结论另加C非零"),
(65,75,"完整多值原算子A1","definition","rewritten","sn-triangular","C191-v1","SN6声明全部支撑面、全部法锥、域外空；图闭证明","无"),
(77,77,"法向逆及k的记号","definition","rewritten","sn-triangular","C191-v1","法向逆全部输入的存在另由SN2收缩构造","无"),
(79,79,"完整零集及非孤立性","theorem","rewritten","sn-triangular","C191-v1","切向严格分离及y=0完整图值给精确零集","m≥1已明示"),
(80,90,"A完整全输入唯一近端及s=0","theorem","rewritten","sn-triangular","C191-v1","SN7精确集合纤维等式；SN3–4处理s=0","不只认证一个选择"),
(92,102,"全部活动面图点对局部RL","theorem","rewritten","sn-triangular","C191-v1","SN8作用全部输入对距≤δ，任意中心","无界全尺度有限α常数不成立"),
(104,110,"全域ordinary真残差EB","theorem","rewritten","sn-triangular","C191-v1","SN9完整残差inf；空纤维单列扩展语义","无"),
(112,119,"临界聚合严格门A5","corollary","rewritten","sn-compatible","C191-v1","R_D k^α<d_D只用于SN10","不当作实际动力必要条件"),
(121,121,"非calm和最大RL指数的非零法向门","theorem","rewritten","sn-failures","C193-v1","携带C≠{0}；逐解输入序列证明","不能沿用至C={0}"),
(125,141,"法向全输入VI收缩与k界","proof","rewritten","sn-triangular","C191-v1","投影表征和几何Cauchy级数给全部输入唯一逆","不需M对称，不借未核最大单调定理"),
(143,143,"切向严格凸prox处理完整活动集","proof","rewritten","sn-elementary","C191-v1","SN3–4用到λsD的投影直接构造并证明极小性","无"),
(147,153,"参数化prox和固定参数反射非扩张","lemma","rewritten","sn-elementary","C191-v1","两次梯度不等式相加直接证明firm不等式","无"),
(155,167,"跨参数prox灵敏度A6","lemma","rewritten","sn-elementary","C191-v1","SN5以s(v−v′)分解，包含s=0","无"),
(169,183,"乘积反射与α模的全对组合","proof","rewritten","sn-triangular","C191-v1","固定参数乘积非扩张，再加参数差","量化跨全部活动面"),
(187,193,"全部图值下界和精确零集证明","proof","rewritten","sn-triangular","C191-v1","逐值下界保真残差inf","无"),
(195,195,"EB与法向参数独立","boundary","rewritten","sn-triangular","C191-v1","EB证明不使用M、a或近端反演","只对所声明D/f/载荷律"),
(199,207,"非calm输入序列与更高指数失败","proof","rewritten","sn-failures","C193-v1","C凸含0使εw可行；法锥0及切向分离给阶差","必须有非零w∈C"),
(213,225,"严格余量与先选输入对尺度","corollary","rewritten","sn-compatible","C191-v1","分清δ与r；不把Lδ小于阈值直接当所有半径兼容","无"),
(227,238,"实际距离窗上的κr合成","proof","rewritten","sn-compatible","C191-v1","SN10逐d≤r核非线性临界界","无"),
(240,240,"切向全局统一及截图留域","boundary","rewritten","sn-compatible","C191-v1","完整图取E；截图须重核纤维和预算","不能自动给任意截图完整路径"),
(244,251,"独立法向递推与切向步长","lemma","rewritten","sn-direct","C191-v1","SN11直接来自全部唯一输出","无"),
(253,263,"两坐标全路径长度上界","corollary","rewritten","sn-direct","C191-v1","SN12给全部尾，控制Euclidean长度","上界未称最优"),
(265,265,"距离Q因子与点R因子","corollary","rewritten","sn-direct","C191-v1","严格区分Q距离与R点尾；标量非负法向取等","不声称点Q因子"),
(267,267,"实际动力不需匹配门或f外点","boundary","rewritten","sn-direct","C191-v1","保留原生递推；无f外点时高阶EB与障碍不继承","非退化大小/新颖性另核"),
(271,282,"圆盘完整例与全部数据","example","rewritten","sn-compatible","C191-v1","完整图SN6的m维球特例，精确d/R/k","无"),
(284,284,"静止滑动完整面及非固定方向","example-property","rewritten","sn-compatible","C191-v1","支撑面完整定义含球和单点方向","不据此认证物理应用"),
(286,295,"圆盘完整shrink近端","example-property","rewritten","sn-compatible","C191-v1","SN3球投影直接给全部纤维","无"),
(297,303,"数值参数的精确兼容与法向率","calculation","rewritten","sn-compatible","C191-v1","用分数和幂精确重算L=5/2和κ=(3/4)^(3/2)","历史浮点执行未回溯认证"),
(307,315,"多面体支撑面、d/R及应用形态","example","rewritten","sn-compatible","C191-v1","凸组合支持面及最大距离在顶点证明；与圆盘同一定理","SOCP/工程具体数据不是此证明前件"),
(319,327,"反馈完整原图和全局a假设","definition","rewritten","sn-feedback","C192-v1","SN13声明完整半直线图及全局Lipschitz门","局部a版本须自映射等新门，未自动接纳"),
(329,334,"k/θ/β的反馈预算","definition","rewritten","sn-feedback","C192-v1","SN14分清条带Q、RL尺度δ及两个预算","无"),
(338,338,"双侧小条带完整唯一逆","theorem","rewritten","sn-feedback","C192-v1","全空间Φ收缩给全纤维唯一，不只构造一支","全域存在新增IVT证明；全域唯一有三输出反例"),
(340,347,"反馈全对RL系数B2","theorem","rewritten","sn-feedback","C192-v1","SN15–16核全部点对的分参数界","图块G_Q，不赋全图"),
(349,355,"反馈精确零集和真EB","theorem","rewritten","sn-feedback","C192-v1","与A同一切向全图值下界，单独核a连续","无"),
(357,357,"反馈先Q后δ的严格匹配","corollary","rewritten","sn-feedback","C192-v1","θ,β趋0后主项留严格余量，再选r","按同条带检查实际轨道"),
(361,375,"完整反馈方程等价与收缩存在唯一","proof","rewritten","sn-feedback","C192-v1","法向全部解反演；Φ定义在整个R^m","θ<1只用于唯一和定量比较"),
(377,386,"两输入的切向/法向灵敏度","lemma","rewritten","sn-feedback","C192-v1","SN16逐项保持相同Q和k","无"),
(388,395,"Euclidean反射预算及EB独立","proof","rewritten","sn-feedback","C192-v1","保持原λ；不采用源Q_F/J_F的省步长缩写","无"),
(397,404,"双侧输入的实际递推及有限长度","corollary","superseded","sn-feedback","C192-v1","负初值须用k(y_j)_+；全域IVT支持全部选择无限延续","不把全选择有限长解释为完整单值"),
(406,413,"反馈每个解输入的最大指数","proof","rewritten","sn-failures","C193-v1","a局部有界且t→p，法向渐近及切向下界","无"),
(417,417,"反馈本构解释与完整工程缺口","interpretation","deferred","sn-source","","不从本页理论F推出现存原论文使用同方程","完整应用模型身份逐项待核"),
(423,427,"投影分离方向","lemma","rewritten","sn-failures","C193-v1","SN2给面值统一负投影界","无"),
(429,439,"任意锚的趋零图点与两种阶","proof","rewritten","sn-failures","C193-v1","C191明确另加C非零；C192用半直线","源§1须修复退化遗漏"),
(441,441,"固定有限oblique二次项的失败","theorem","superseded","sn-failures","C193-v1","只排除明确SN17；包括τI与τ≥0；不代替外部命名定义","未知退化度量/变参数命名证书未排除"),
(445,445,"anchored calmness/almost-averaging范围","boundary","superseded","sn-failures","C193-v1","不calm直接证明；只排除确实推出calm的具体前提组合","命名竞品须另核原定义"),
(449,451,"partial可用与不得普遍排除","boundary","superseded","sn-feedback","C192-v1;C193-v1","直接法向更新足够；B联合全对法向单调性以−7反例否定","不授予未定义PSM类别身份"),
(455,457,"光滑零流形的局部逆筛选","lemma","superseded","sn-smooth","","补双侧局部逆J(G(u))=u；用图表示距离和收缩构造证明局部Lipschitz","不为原生KKT核流形/coverage；不判全球优先权"),
(461,468,"历史搜索行为和四条查询","search-provenance","deferred","sn-source","","保留可定位报告；本轮未执行或复原历史检索","不认证原执行平台、覆盖率或系统综述"),
(472,472,"用户材料VERIFIED标签","status","deferred","sn-source","","规范C185等另有精确身份，源状态不自动传递","历史用户输入范围不复原"),
(473,473,"Carpick验证状态重述","literature-status","deferred","sn-source","","同LF27未验一手事实","原页待核"),
(474,474,"接触摘要验证状态重述","literature-status","deferred","sn-source","","同LF29仅保留来源报告","原摘要待核"),
(475,475,"塑性全文验证状态重述","literature-status","deferred","sn-source","","同LF31仅保留来源报告","原页待核"),
(476,478,"定理A/B及代理审查执行标签","review-provenance","deferred","sn-source","","新规范直接证明独立于旧代理声称","历史代理审查行为未核"),
(479,479,"解析实例浮点与calmness旧执行报告","numerical-provenance","superseded","sn-compatible","C191-v1;C193-v1","常数和发散比的数学另直接证明；旧执行仍报告","旧程序、输入p/方向与执行输出身份未核"),
(480,480,"完整工程/PDE应用待核","open-obligation","deferred","sn-source","","保留实际模型身份未闭","逐方程与原数据核对"),
(481,481,"所有partial均失败已否定","boundary","rewritten","sn-direct","C191-v1;C192-v1","完整原图直接递推给独立有限长度","不将此事实包装为外部PSM定理"),
(483,492,"返回合同任务字段和PROVISIONAL","provenance","deferred","sn-source","","合同作为历史元数据，非当前研究权限或证据","历史任务行为不复原"),
(493,499,"历史输入及原文阅读清单","provenance","deferred","sn-source","","不读取历史聊天，不采信旧已读标签作paper fact","列举输入的旧审查范围未核"),
(500,505,"旧输出文件与三类证据字段","status","deferred","sn-source","","当前资产独立定义；工程身份仍未闭","原输出/外部访问执行不认证"),
(506,510,"合同中的共同假设摘要","definition-summary","duplicate","sn-object","C191-v1;C192-v1","完整假设已在SN1/SN6/SN13逐项承接","C非零只用于C193"),
(511,513,"作者应用选择和人工动作字段","organization","nonmathematical","sn-source","","研究建议不构成已证应用","无新增数学断言"),
(514,520,"六项旧质量检查自述","review-provenance","deferred","sn-source","","当前完整纤维/双证书/指数证明分别给出；旧检查日志未核","历史执行不回溯认证"),
(521,526,"旧冲突/合并/下一动作合同","organization","nonmathematical","sn-source","","历史合同无当前权限效力；保留原应用待核门","无新增数学断言"),
(528,528,"原稿下一步完整模型对照","open-obligation","deferred","sn-source","","数学已重构不等于原生工程模型身份已闭","应用原方程逐项核对仍开放"),
]
S.sort()
rows = []
cursor = 1
for record in S:
    start, end, label, typ, disp, anchor, claims, reason, obligation = record
    assert cursor <= start <= end <= len(lines), record
    if cursor < start:
        rows.append((cursor,start-1,"标题、空行、表头或连续排版","organization","nonmathematical",
                     "", "", "附随排版，不新增独立实质断言","无"))
    rows.append(record)
    cursor = end + 1
if cursor <= len(lines):
    rows.append((cursor,len(lines),"尾部排版","organization","nonmathematical","","","无新增断言","无"))
assert all(rows[i][1] + 1 == rows[i+1][0] for i in range(len(rows)-1))
header = ["unit_id","source_locator","line_start","line_end","source_label","unit_type",
          "exact_payload","evidence_state","disposition","canonical_anchor","claim_ids",
          "reason","remaining_obligation"]
output = ROOT / "research/audit/NATURAL_CLASS_UNITS_2026_10_07.tsv"
with output.open("w",newline="") as f:
    writer = csv.writer(f,delimiter="\t",lineterminator="\n")
    writer.writerow(header)
    for i,rec in enumerate(rows,1):
        start,end,label,typ,disp,anchor,claims,reason,obligation = rec
        target = CAN+"#"+anchor if anchor else AUD
        state = {"rewritten":"derived-checked","superseded":"derived-checked-with-source-scope-repair",
                 "duplicate":"same-canonical-identity","deferred":"source-report",
                 "nonmathematical":"nonmathematical"}[disp]
        payload = "\n".join(lines[start-1:end])
        writer.writerow([f"NAT-U{i:04}",SOURCE,start,end,label,typ,payload,state,disp,
                         target,claims,reason,obligation])
print(f"Read {len(data)} bytes / {len(lines)} LF; wrote {len(rows)} disjoint units with exact 1–528 partition.")
