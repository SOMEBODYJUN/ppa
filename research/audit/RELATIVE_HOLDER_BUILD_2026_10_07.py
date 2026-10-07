from pathlib import Path
import csv, hashlib, collections
ROOT=Path(__file__).resolve().parents[2]
p=next((ROOT/'history/sources').rglob('07_stage_synthesis.md'))
raw=p.read_bytes(); src=str(p.relative_to(ROOT)); ls=raw.decode('utf-8').split('\n')[:-1]
assert len(raw)==14130 and len(ls)==202 and raw.count(b'\n')==202 and raw.endswith(b'\n')
assert hashlib.sha256(raw).hexdigest()=='ba894d3dee5fabcdc29a312cf01f5383d53d7dbdda9028c511f185c8d164f906'
RH='research/canonical/relative_holder_thinness.md#'
AUD='research/audit/RELATIVE_HOLDER_COVERAGE_2026_10_07.md#rht-audit-source'
OC='research/canonical/operator_space_construction_frontier.md#'
CT='research/canonical/compact_t_observation.md#'
rows=[]
fields='unit_id source_locator line_start line_end source_label unit_type exact_payload evidence_state disposition canonical_anchor claim_ids reason remaining_obligation'.split()
def put(a,b,label,kind='mathematical',disp='deferred',anchor=AUD,claim='',ob=''):
    if disp=='deferred':
        assert ob,label
        ev='source-report'; reason='仅来源报告；准确断言：'+label+'。本次未以历史PASS、摘要或邻近定理补该原生范围。'
    elif disp=='nonmathematical':
        ev='nonmathematical'; reason='标题/排版或研究建议；不承担已完成数学结论：'+label; ob=ob or '无本条独立数学结案；相邻实质断言另列。'
    elif disp=='duplicate':
        ev='derived-checked'; reason='准确复用已存在规范结论；断言：'+label+'；沿所列锚点核同对象/量词，不升级更广来源报告。'
    else:
        ev='derived-checked'; reason='C186-v1独立直接推导并逐项核验；断言：'+label+'；RH1–11完整保值域、固定集、同尾及正Hölder资格。'; ob=ob or '本准确数学子句已重构；原生认证名称、一般母空间及历史证据仍分列未闭。'
    rows.append(dict(zip(fields,[f'RHT-SYN-U{len(rows)+1:04}',src,a,b,label,kind,'\n'.join(ls[a-1:b]) or '空LF行',ev,disp,anchor,claim,reason,ob])))
def defer(a,items,anchor=AUD,kind='mathematical'):
    for label,ob in items: put(a,a,label,kind,anchor=anchor,ob=ob)
def prop(a,label,anchor,claim='C186-v1',b=None): put(a,b or a,label,disp='rewritten',anchor=anchor,claim=claim)
def dup(a,label,anchor,claim,b=None): put(a,b or a,label,disp='duplicate',anchor=anchor,claim=claim,ob='无该已证精确子句的新义务；不认证同行更宽原生图或历史行为。')
def org(a,label,b=None): put(a,b or a,label,'organization','nonmathematical')
def strategy(a,label,anchor=OC+'ocf-specification'):
    put(a,a,label,'programme','nonmathematical',anchor=anchor,ob='这是开放研究要求而非已证成果；按该锚点保留准确前沿。')
# Opening source/provenance, separate conduct claims from mathematical reports.
org(3,'日期与综合主席角色标签')
defer(3,[('声称完整阅读本轮01–06','核对应阅读/审查行为记录，不能由本次读此摘要确认。'),('声称阅读上一阶段10_final_blueprint','核上一阶段具体版本及历史阅读证据。'),('数学状态沿用05审计§9交叉复核','逐命题检查其定义/证明；PASS并非本次独立证明。')],kind='historical-evidence')
org(3,'不另宣先行性清关、不重审未调用RLEB论文的范围声明')
strategy(7,'继续构建且不能只以LT在所有RLEB中第一纲为成功标准')
prop(9,'合法特例中正Hölder回缩类在自身拓扑第一纲',RH+'rht-perturbation')
defer(9,[('把该特例Hölder类直接称作RLEB并类','核完整源图上direct/energy证书定义、gauge、输入边界与Hölder等价；C186仅恢复明定反射模身份。')],RH+'rht-graph')
dup(9,'更宽exact-S连续层内满足全域正Hölder必要条件的两类同为第一纲','research/canonical/uniform_holder_thinness.md#uht-interfaces','C180-v1')
prop(9,'自第一纲分母无法仅凭第一纲标签区分其子集',RH+'rht-boundary')
org(9,'该尺度诊断不判理论价值或扩展成败')
defer(11,[('报告已获对象侧紧块表示','需在同一完整紧源图卡证明各原生认证类的紧预算块与可数等价耗尽。'),('报告保任意实步长的完整图闭块编码','核实步长作为紧参数的完整覆盖/全纤维EB与RL闭性。'),('报告任意紧局部步长谱实现','需完整原图构造及所有谱的正反包含证明。'),('报告整个函数结构层的受控变形定理','核该结构层所有函数的共轭、真实全纤维EB、RL和兼容保持。')])
strategy(11,'将各模块闭合到同一有鉴别力的比较体系')
strategy(13,'先仿射非点结构层、跨尺度与母空间位置，再推广弯曲C1')
org(13,'用户无需补假设及有条件的范围选择建议')
# A1 exact specification and distinct source theorems.
put(21,23,'P=(E,U,S,λ,B,W,r*,ω)中立规格','definition',ob='逐坐标恢复来源的可接受范围、域包含及完整图父空间，不能由参数元组推出Polish。')
defer(25,[('S为精确零集','在A1所指完整图层核zerF=S的定义与稳定性。'),('U上完整resolvent全输入覆盖','对所有U输入核全部原图纤维存在。'),('U上完整resolvent单值','核完整图全部输出，不是所选支。'),('U上完整resolvent连续','给原图空间到此局部映射的拓扑门。'),('B全初值轨道留于W紧含U','在同一λ/域核所有迭代存在与留域，不借尾标签。')])
put(27,30,'Dωλ(P)由全B全部m≥n的实际Cauchy尾定义','definition',ob='补源图/轨道良定前提、n的起点与是否另有到S距离条件，不能仅由显示Cauchy式推出极限落S。')
org(32,'定义分母不预设认证标签、Hölder指数或超吸引形式的设计口径')
defer(34,[('良定exact-S完整原图层为AW-Polish','明确完整图父空间与局部良定域条件，逐项证明Gδ/完备可分；C179不提供此身份。'),('留域条件相对闭','核源空间收敛是否控制全部所需完整近端输出和边界。'),('共同实际尾条件相对闭','核固定域上有限迭代连续及共同尾闭传递。'),('固定尾层完整图全时间拓扑等于AW拓扑','证明保留完整图坐标的两个方向拓扑比较；C06只为T-only。'),('相同局部T不能替代完整原图','源层的准确反例及其域外完整纤维需要匹配；保留原生身份门。'),('相同局部动力可有不同真实最小残差','核源完整关系对及残差inf的显式差值，不能以步长残差替代。')])
# A2
put(40,42,'固定λ完整F_T,K源图定义','definition','duplicate','research/canonical/uniform_holder_thinness.md#uht-source-card','C180-v1','图卡代数已恢复；本行不认证紧预算块或具体认证谓词。')
defer(44,[('direct-RLEB对象像Kσ','固定全部参数/规范gauge并证明同对象紧块与可数等价耗尽。'),('ordinary-gauge energy-RLEB对象像Kσ','核普通gauge全域与能量证书闭约束、参数紧化及对象投影。'),('LT公共all-pairs认证像Kσ','核LT完整定义和同图同域闭预算穷尽。'),('连续违约量完成证明','恢复所用违约泛函的连续性和全部图点量词。'),('参数紧化完成证明','核参数紧块确实覆盖所有实证书及边界严格不等式。'),('Arzelà–Ascoli完成证明','核同一对象块的统一模、有界性及闭性。')])
org(44,'不使用证书空间小即对象像小的推理')
defer(46,[('每个固定预算对象块有共同实际尾','各原生预算的兼容、留域与统一尾须逐类证明。'),('每个预算块在全时间拓扑紧','源块先证一致紧且有同一零尾；C06条件工具不能自动认证源块。')])
dup(48,'F_T,K是主动定义完整源图，不是裁剪既有F','research/canonical/uniform_holder_thinness.md#uht-source-card','C180-v1')
# A3, A4
for label,ob in [('固定锚允许缩域germ中LT像Fσ','先定义原germ空间、完整认证谓词及闭预算等价穷尽。'),('固定锚允许缩域germ中direct像Fσ','同一原生空间证明direct预算闭性与可数耗尽。'),('固定锚允许缩域germ中energy像Fσ','同一原生空间证明energy预算闭性与可数耗尽。'),('三个联合步长图Fσ','联合空间X×(0,∞)及完整实参数闭性另核；不能由各切片Fσ推联合。')]: defer(52,[(label,ob)],OC+'ocf-g')
defer(54,[('正实步长放入紧参数块后消去','逐类证明投影闭且等价可数耗尽，不凭参数域可σ紧就判认证像。'),('不需可用步长谱开放','给正确的紧实参数投影论证后方可省开放门。'),('实步长不必换成有理步长','核全部实λ量词与可数紧覆盖，不以稠密有理数替代存在。'),('闭块控制完整覆盖','覆盖和完整纤维存在的闭传递独立证明。'),('闭块控制全部图点RL','源图收敛下所有点对与同尺度闭传递。'),('闭块控制真全纤维EB','必须是inf残差且满足取到或gauge右连续门。')],OC+'ocf-g')
strategy(56,'germ缩域编码未关闭同宏观域/同尾/输出迹的统一编码',OC+'ocf-g')
for label,ob in [('每个非空紧A紧含(1,∞)可实现','构造依赖任意紧A且逐项验证，不以单点例替代全A。'),('实现者完整原图闭','全部参数端点/逃逸序列的闭图检查。'),('实现者零集固定且非点','完整零图点精确等式。'),('固定解点附近完整良定谱=A','A内全部覆盖/唯一/连续，A外完整碰撞或失覆盖。'),('LT认证谱=A','同一原图、同λ、同局部定义，证A内认证及A外排除。'),('direct认证谱=A','精确direct谓词和A内外双向证明。'),('energy认证谱=A','精确energy谓词和A内外双向证明。'),('全选择收敛谱=A','任意λ和全部完整路径的收敛/失败量词独立证明。')]: defer(60,[(label,ob)],OC+'ocf-g')
defer(62,[('谱可为无理单点','依赖上一全谱实现的准确构造，不能由摘要确认。'),('谱可为Cantor紧集','依赖任意紧A完整实现而非某一个可写公式例。'),('严格局部证书不保证开步长窗口','在同一完整原图上验证严格证书和孤立/非开谱，不由标签或近似步长推断。')],OC+'ocf-g')
org(62,'任意紧A仅声称闭图，不声称非半代数A实现为半代数')
defer(64,[('存在严格完整RLEB例','复核全部图纤维、真实EB、全对RL、coverage与严格兼容。'),('该同一例单值良定谱为单点','所有其他正步长完整碰撞/失覆盖；目标步长良定。'),('同一例每个正步长全部完整轨道收敛','步长全称、全部选择、存在轨道/留域与收敛分别验证。'),('例分离良定/实际收敛/理论认证三性质','须基于上述同对象反例，不能由名称差异推出严格分离。')],OC+'ocf-g')
defer(66,[('上述结果已作范围内复核','需历史审查记录及具体受审版本，非本次独立证明。')],kind='historical-evidence')
org(66,'原创性未清关声明')
# A5
put(72,75,'Lλ输入/输出图完整共轭定义','definition',ob='源Lλ=(u+λv,u)与反射坐标不同；固定同胚h、域和值域，不以名字合并两共轭。')
put(72,75,'完整J共轭恒等式','formula',ob='从源输入/输出Lλ共轭逐完整纤维证明JλFh=hJλFh逆及定义域，不能从反射坐标共轭直接推此式。')
defer(77,[('仿射解集/法向收缩/非退化切漂整个函数层','完整写出结构假设、参数统一性和内生层拓扑。'),('近恒等法向幂变形同时保持所列性质','对层内每个函数给变形并验证五个独立保持门，非一个例子。')],OC+'ocf-f')
defer(79,[('变形保持完整resolvent','新全图的同输入唯一/覆盖及精确反演。'),('变形保持精确零集','核h(S)=S及无新增零点。')],OC+'ocf-f')
defer(80,[('变形保持all-pairs RL','全部完整图点对、同λ、同尺度，不只锚定或沿轨道。')],OC+'ocf-f')
defer(81,[('变形保持整个逆纤维真实幂EB','对完整新图纤维求inf；不得用选中图值代替。')],OC+'ocf-f')
defer(82,[('变形保持严格RLEB兼容','写定新γ、真实EB幂与系数并核严格不等式。'),('变形保持共同小初值邻域','证明所有该邻域初值完整轨道留域且预算统一。')],OC+'ocf-f')
defer(83,[('同一新算子任意正步长无LT局部all-pairs认证','必须对全部正λ而非构造λ排除完整LT必要条件。')],OC+'ocf-f')
defer(85,[('声明范围内PASS','核历史受审稿版本及实际审核证据；不从标签推定理。')],kind='historical-evidence')
defer(85,[('覆盖任意结构函数不只是固定公式','结构条件下全称证明及各常数的依赖。')],OC+'ocf-f')
put(89,91,'实际尾仅从De映至D_(1+ε)e','formula',ob='核完整共轭的实际成对迭代尾及到S距离尾；不能把系数损失视为零。',anchor=OC+'ocf-f')
defer(93,[('新证书域可能缩小','具体来源构造中域半径与参数依赖仍待核。')],OC+'ocf-f')
strategy(93,'尚未证明变形在同宏观比较空间内',OC+'ocf-f')
# B1 LF97–104 deliberately untouched: existing table is the authority.
# B2 exact recovery, with independent theory-label gate.
put(107,111,'矩形K、底边S、全部连续一步回缩M_ret定义','definition','rewritten',RH+'rht-object','C186-v1')
prop(113,'M_ret为非空完备中立一步尾层',RH+'rht-retractions')
prop(113,'输出全在S且完整源图真EB左端为零',RH+'rht-graph')
defer(113,[('RLEB成员恰为某正Hölder回缩','指定direct/energy定义、gauge、全K量词及输入边界coverage；RH11只证明明定反射模等价。')],RH+'rht-graph')
prop(113,'正Hölder回缩并类在自身相对C0拓扑第一纲',RH+'rht-perturbation')
prop(115,'任何子集在H+这个环境中第一纲',RH+'rht-boundary')
prop(115,'LT子集相对第一纲无法在自第一纲分母衡量特别稀少',RH+'rht-boundary')
prop(117,'该矩形例不推出所有RLEB空间自第一纲',RH+'rht-boundary')
strategy(117,'选择分母须另验非空Baire或自身非第一纲',OC+'ocf-c')
# B3 split witnesses; existing C180 proves only singleton.
dup(121,'共同尾层可能只有一个对象','research/canonical/uniform_holder_thinness.md#uht-boundary','C180-v1')
dup(121,'S不能是连续回缩像时一致收敛到S层为空',CT+'ct-object','C06')
defer(121,[('共同尾层可为更大中立空间无处稠密边界','固定父层、精确Fix或只固定S、共同尾条件后给相对无内点构造。'),('同S一致收敛映射全时间任意接近却不在同预定尾预算','构造同K/S/全部尾量词的慢收缩族，并核全时间距及预算违反。')])
strategy(123,'尾层内类差必须同时报告非退化、母层位置与跨尺度转移')
# C table every attained and open gate separated.
defer(129,[('已有全图共轭模块','源变形对象和完整图坐标需核。'),('已有真实EB模块','全部逆纤维残差证明仍需源构造核验。'),('已有RL模块','全对同尺度保持需源证明。'),('已有严格兼容模块','新模与gauge系数需同域严格复核。'),('尾损失可任意近1','核ε量词与共同初值/证书域依赖。')],OC+'ocf-f')
strategy(129,'饱和en的同尾保持、预定宏观域证书仍开放；否则只跨层',OC+'ocf-f')
defer(130,[('已有对象侧闭紧预算块','需原生三类分别证明真实紧块。'),('已有整个RLEB并类Kσ','需同一对象空间可数等价耗尽。')],OC+'ocf-c')
strategy(130,'有鉴别力非退化相对分母待选证，不能默认整个RLEB Baire',OC+'ocf-c')
defer(131,[('法向收缩/非退化漂移层内通用变形已得','结构层全部函数和准确变形范围仍须独立核验。')],OC+'ocf-f')
strategy(131,'层闭包/内部/稠密/非第一纲/排斥区域及母层AW位置仍开放',OC+'ocf-specification')
org(133,'三项桥为同一比较定理承重点的研究判断')
defer(135,[('任意正步长LT推出线性位移必要条件','给完整LT all-pairs定义并证明同图任意正步长必要式。'),('必要条件覆盖局部仿射解集','精确局部域和全部完整纤维。'),('必要条件覆盖C1解流形','管状坐标、锚与线性误差估计独立核验。'),('保RLEB幂变形主定理仿射层完成','全层保持门及实际证明恢复，不能由必要条件推充分构造。')],OC+'ocf-f')
strategy(135,'C1必要条件不关闭弯曲流形构造',OC+'ocf-f')
# D1 intrinsic tails: exact canonical reuse, no complete-original-graph transfer.
dup(141,'紧自映射域无速率一致收敛到S且固定S的层',CT+'ct-object','C06')
put(143,148,'内生w_n为全部尾对差及全部尾到S距离最大值','definition','duplicate',CT+'ct-object','C06','仅CT1同T-only对象；原完整图版本另列。')
dup(150,'对象的w(T)属于c0',CT+'ct-object','C06')
dup(150,'w(T)由对象唯一决定不能随意重选',CT+'ct-object','C06')
put(152,154,'w在同全时间距离下2-Lipschitz','formula','duplicate',CT+'ct-proper','C06','两迭代差各损失d_all、距离项损失d_all；不替原AW度量。')
dup(156,'非增e共同尾条件等价w≤e',CT+'ct-proper','C06')
defer(156,[('完整原图局部B-trace版本保原图坐标','完整图父空间、局部trace连续性、良定与全纤维门另证；不由C06 T-only授予。')],OC+'ocf-b')
strategy(158,'建议用分层类别剖面而非单纲标签',OC+'ocf-b')
put(160,167,'Prof_C(e)登记相对内部、闭包、类别','definition','nonmathematical',OC+'ocf-b',ob='仅记录格式；各实际认证类剖面的数学取值与跨层传递仍开放。')
org(169,'同时登记非空/退化、解几何、认证域；Cat为状态记录非数值测度')
strategy(171,'跨尺度类别定理尚未证明，需核ce/时间平移/放宽保持',OC+'ocf-b')
defer(171,[('现有共轭给e到(1+ε)e受控映射','须先恢复源通用构造及实际预算估计；C186的零尾特例不替此全层结论。')],OC+'ocf-f')
dup(171,'连续映射本身不保证保纲',OC+'ocf-b','C06')
strategy(171,'层包含不自动提供类别转移',OC+'ocf-b')
# Compact object blocks only conditional.
defer(173,[('可后置采用固定证书闭紧对象层','实际原生证书块的闭性、紧性及同对象身份仍需验证。')],OC+'ocf-c')
put(173,173,'已证非空紧度量块是Baire这一条件事实','mathematical','duplicate',CT+'ct-proper','C06','只复用Baire基础事实；不认证源原生块真的闭紧、非空或非退化。')
strategy(173,'块非空/非退化/LT内点/母空间位置必须另验；不改称全体母空间',OC+'ocf-c')
# Each automatic route is a programme, attained clauses separate.
strategy(177,'仿射非点S欧氏几何首攻、内生结构分层与母体系',OC+'ocf-specification')
strategy(177,'登记变形前后层身份；粗糙变形可能出光滑层不推出内部稠密',OC+'ocf-f')
strategy(178,'同尾同域闭合或不可能/跨尺度定理；1+ε损失非零',OC+'ocf-f')
strategy(179,'分母闭/Polish或非空Baire及中立空间位置分别验',OC+'ocf-c')
strategy(180,'在验证的层内同时记录RLEB/LT/差集/两者未认证部分',OC+'ocf-specification')
strategy(180,'固定同一步长口径或另证全实步长原图编码',OC+'ocf-g')
org(180,'允许各层比较答案相反或双方皆小的研究策略')
defer(181,[('已有线性位移必要条件可复用','源条件精确对象与仿射/C1范围仍需独立证明。')],OC+'ocf-f')
strategy(181,'C1推广的管状几何/真残差/同域化/变形闭合分别证明',OC+'ocf-f')
org(181,'无限维Hilbert不是本阶段前置门槛')
org(183,'自动推进与用户范围选择建议，不是数学证明')
strategy(183,'将母空间位置列为不可删验收项',OC+'ocf-specification')
# E claims repeated accurately, plus publication/priority evidence not mathematics.
org(187,'可以入论文且不只是背景的价值判断')
defer(189,[('完整图紧证书投影是可陈述技术定理','逐三类原生预算闭紧及投影等价的源证明仍未核。'),('任意实步长Fσ编码是可陈述技术定理','原空间/闭预算/全实λ耗尽需独立重建。')],OC+'ocf-g')
defer(190,[('任意紧步长谱实现为边界定理','恢复完整构造及谱双向等式。'),('单值谱与全选择收敛谱分离','同一原图的所有正λ/全部路径核验。')],OC+'ocf-g')
defer(191,[('受控全图变形同时保真EB','完整逆纤维inf估计。'),('同变形保RL','全部图点对及同尺度估计。'),('同变形保严格兼容','与EB/RL同参数同域预算。')],OC+'ocf-f')
prop(192,'正Hölder回缩自第一纲特例给分母诊断',RH+'rht-perturbation')
dup(192,'尾层可退化为单点的反例','research/canonical/uniform_holder_thinness.md#uht-boundary','C180-v1')
org(192,'上述边界说明分层比较研究价值的解释')
strategy(194,'尚不能声称RLEB在中立算子世界覆盖绝大多数',OC+'ocf-specification')
org(194,'独立优先权未完成及不承诺期刊级别的范围声明')
org(196,'研究稿与理论论文定位、主结论/题目调整建议')
strategy(196,'C三门在非退化层闭合并联系中立母空间仍是义务',OC+'ocf-specification')
strategy(200,'同尾同域、非空Baire分母、结构层位置三桥仍须完成',OC+'ocf-specification')
org(200,'不要求用户提供点子/数据的任务安排')
strategy(202,'以有鉴别力分层分类替代预定LT第一纲结论；证明层位置和转移边界',OC+'ocf-specification')
# Every leftover physical LF is checked to be blank/headings/connecting prose.
covered=set(range(97,105))
for q in rows: covered.update(range(q['line_start'],q['line_end']+1))
allowed_connectors={19,25,38,70,77,87,141,150,158}
for i,line in enumerate(ls,1):
    if i in covered: continue
    assert not line.strip() or line.startswith('#') or i in allowed_connectors or line.startswith('| 瓶颈') or line.startswith('|---'), (i,line)
    org(i,'空行/标题/表头/不新增断言的引导语')
rows.sort(key=lambda x:(x['line_start'],x['line_end'],x['unit_id']))
# Keep stable independent IDs, schema and exact source payload (quoted TSV supports newlines).
out=ROOT/'research/audit/RELATIVE_HOLDER_UNITS_2026_10_07.tsv'
with out.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)
covered_new=set()
for q in rows: covered_new.update(range(q['line_start'],q['line_end']+1))
assert covered_new==set(range(1,97))|set(range(105,203))
old=list(csv.DictReader((ROOT/'research/audit/UNIFORM_HOLDER_B1_UNITS.tsv').open(encoding='utf-8',newline=''),delimiter='\t'))
assert not set(q['unit_id'] for q in rows)&set(q['unit_id'] for q in old)
assert covered_new|set(range(97,105))==set(range(1,203))
print({'new_rows':len(rows),'old_B1_rows':len(old),'full_rows':len(rows)+len(old),'new_dispositions':dict(collections.Counter(q['disposition'] for q in rows)),'covered':202,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
