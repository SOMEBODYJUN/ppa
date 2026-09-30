from pathlib import Path
import json, re, hashlib, shutil, base64, zipfile, datetime, collections, os

WORK = Path(__file__).resolve().parent
ROOT = WORK / '菠萝_RL与广义次正则研究资产_2026-09-14'
NAV = ROOT / '00_从这里开始'
OUT = WORK.parent / 'output'
V1ZIP = OUT / '菠萝_RL与广义次正则研究资产_2026-09-14.zip'
HTML_NAME = '研究资产统一超边知识图_v2.html'
sha = lambda b: hashlib.sha256(b).hexdigest()
def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

# Only the new extracted copy is edited. Baseline metadata is saved once.
for name, backup in [('manifest.json','历史manifest_v1.json'),('资产关系数据.json','历史资产关系数据_v1.json'),('README_研究资产导航.md','README_v1_历史导航.md')]:
    if not (NAV/backup).exists(): shutil.copy2(NAV/name, NAV/backup)
v1 = json.loads((NAV/'历史manifest_v1.json').read_text())
old = json.loads((NAV/'历史资产关系数据_v1.json').read_text())
assets = {x['id']:dict(x) for x in v1['files']}
oldnodes = {x['id']:x for x in old['nodes']}
texts={}
extraction=[]
for aid,a in assets.items():
    p=ROOT/a['path']
    if p.suffix in ['.md','.tex','.py','.sh','.bib','.bbl','.yaml','.csv','.json','.txt']:
        t=p.read_text(encoding='utf-8'); texts[aid]=t
        heads=[{'line':i+1,'text':line} for i,line in enumerate(t.splitlines()) if re.match(r'^#{1,6} |^\\(?:sub)*section|^\\(?:begin\{(?:theorem|lemma|proposition|definition|corollary)|label)',line)]
        extraction.append({'asset_id':aid,'path':a['path'],'sha256':sha(p.read_bytes()),'headings':heads})

def source(aid, needle=None, span=14):
    a=assets[aid]; lines=texts.get(aid,'').splitlines()
    if needle is None:
        idx=0; locator='文件级来源；未提供章节定位'
    else:
        hits=[i for i,l in enumerate(lines) if needle in l]
        assert hits, (aid,needle)
        idx=hits[0]; locator=lines[idx].strip()
    return {'asset_id':aid,'path':a['path'],'locator':{'heading':locator,'line_start':idx+1 if lines else None,'line_end':min(len(lines),idx+span) if lines else None},'excerpt':'\n'.join(lines[idx:idx+span]),'evidence_basis':'VERIFIED_USER_MATERIAL'}

S={
 'minty':source('rl_tex','Lemma 2.1 (coupled Minty chart)'),
 'rlmain':source('rl_tex','Theorem 3.2.',77),
 'rlgeneral':source('rl_tex','Lemma 3.1 (comparison-sequence localization)',66),
 'rllegacy':source('rl_chain','## 2. Theorem 3.1',40),
 'rlscope':source('rl_referee','### 0.3 合稿哪些部分可原样给 Pro',22),
 'rlaudit':source('rl_delta','## 1. 当前判定',16),
 'rlrepair':source('rl_referee','### 0.2 当前合稿需要修改的句子',13),
 'rlpower':source('rl_chain','## 3. Corollary 3.2',25),
 'rlsharp':source('rl_delta','## 3. scalar exact',33),
 'rlnatural':source('rl_tex','\\section{A support-function law',26),
 'rldirect':source('rl_tex','Proposition 5.4 (normal contraction',52),
 'rlreverse':source('rl_recheck','## 5. Reverse',8),
 'rlmodules':source('rl_tex','\\section{Independent verification',25),
 'rlshear':source('rl_delta','## 4. 额外 delta',9),
 'crsc':source('conic_tex','\\begin{definition}[Frozen minimal-face CRSC]',12),
 'rank':source('conic_core','### P1.',27),
 'normal':source('conic_core','### P5.',30),
 'mscq':source('conic_tex','\\begin{theorem}[MSCQ from amenability',42),
 'conicaudit':source('conic_core','## 1. 范围',20),
 'universal':source('conic_core','## 6. PROVED',11),
 'nicebad':source('conic_boundary','## 4. Paper-ready',20),
 'coneex':source('conic_examples','## 5. 常数',21),
 'transfer':source('conic_tex','\\section{A regularity and residual-transfer interface}',32),
 'conicgate':source('conic_ledger','### Current evidence and remaining gates',10),
 'priority':source('conic_priority','### 7.1 最终版差分',11),
 'finite':source('finite','### Theorem 1',17),
 'ot':source('finite','### Lemma 2',39),
 'fixed':source('finite','## 1. Outcome',50),
 'finiteaudit':source('finite_audit','## 1. Verdict',12),
 'lazy':source('finite_audit','### 6.3 No source-compatible',26),
 'countable':source('markov_counter','## 11. Addendum verdict',17),
 'noholder':source('markov_counter','### 13.6 No positive',19),
 'compactgauge':source('markov_counter','## 14. Additional corollary',29),
 'mass':source('mass','### Theorem 3.1',40),
 'coupling':source('mass','## Executive decision',25),
 'conditional':source('conditional_audit','## Executive verdict',21),
 'hls':source('correlation','### 6.1 HLS domination',24),
 'nonfeller':source('native','### Theorem 5.1',14),
 'selection':source('native','## 0. Decision',14),
 'nativeeb':source('native','### Corollary 5.2',19),
 'repr':source('open_plan','#### 本月首攻的新定理',29),
 'plan':source('open_plan','## 2. 当前项目总账',10),
 'rlgate':source('open_plan','#### 必须修复的结构',15),
 'markovgate':source('markov_journal','## 6. 最低剩余门',27),
 'lit':source('rl_lit','##',12),
 'frank':source('frankowska'),
}

E=[]
def entity(id,label,kind,project,layer,status,statement,refs,claim=False):
    E.append(dict(id=id,label=label,kind=kind,project=project,layer=layer,evidence_status=status,statement=statement,sources=[S[r] for r in refs],core=True,core_claim=claim,document_leaf=False))

specs=[
('r_problem','RL–PPA：哪些选择收敛？','research_question','RL','native','PENDING','需要区分图条件、独立证书、覆盖和轨道局部化；不是一个条件自动推出全轨道。',['plan','rlmain']),
('r_graph','AP-RL 图条件','definition','RL','certificate','PROVED','受控图块上任意点对的同一图值反射 Hölder 条件。',['minty']),
('r_minty','耦合 Minty 反射','definition','RL','certificate','PROVED','M+ 在指定图块上单射且耦合 Q Hölder；不自动给输入覆盖。',['minty']),
('r_coverage','允许选择 · 输入覆盖','assumption','RL','native','PROVED','每个邻域输入存在允许步；一条好分支不能替代完整 resolvent 的任意选择。',['rlmain']),
('r_nearest','同一步 · 同一最近目标','assumption','RL','certificate','PROVED','每个允许步存在 p∈P_S(x)，两个证书使用同一个 S、范数与实际残差。',['rlmain','rllegacy']),
('r_energy','反射恒等式 · B 与 E','proof_mechanism','RL','certificate','PROVED','B(t)=(t+ω(t))/2，E(t)=(t²+ω(t)²)/2；步长 cap 和能量必须区分。',['rlmain']),
('gauge','广义度量次正则 / gauge','definition','CROSS','certificate','PROVED','残差通过非降、零点消失的 gauge 控制集合距离；不同问题的残差和度量不能直接交换。',['rlmain','mscq','finite']),
('r_contraction','距离收缩 / 比较序列','conclusion','RL','result','PENDING','旧主定理的固定 κ 路线有审计；当前 TeX 新增比较序列 Lemma 3.1 须另作同版独立审计。',['rlgeneral','rllegacy','plan']),
('r_length','有限长度 · 点收敛','conclusion','RL','result','PROVED','可求和步长尾和加留域预算和覆盖，才能保证任意允许轨道续接并趋于闭目标集。',['rllegacy','rlscope']),
('r_main','RL 独立证书主定理','theorem','RL','result','PROVED','审计支持旧 T5 合稿 Theorem 3.1 的内部数学核心；当前 TeX 对应 Theorem 3.2，新加 Lemma 3.1 不冒充已同版审计。',['rllegacy','rlmain','rlscope'],True),
('r_power','幂型 γq 门槛 · 正半径','certificate','RL','certificate','PROVED','γq>1 给小半径；γq=1 要严格常数余量，且实际 β(r)<1；γq<1 只说明这一汇总不认证。',['rlpower']),
('r_sharp','二分支剪切 · 分母 2','example','RL','native','PROVED','固定 λ 的可达族证明统一临界充分界的分母 2 不可普遍增大；不是每个算子的最优率。',['rlsharp']),
('r_envelope','统一标量松弛包络','definition','RL','certificate','PROVED','exact 只相对保留 energy、B caps、EB 的标量信息类，不保证向量或算子可实现。',['rlsharp']),
('r_shear','实际收敛但无兼容 gauge','counterexample','RL','result','OBSTRUCTED','退化剪切反例排除指定位置无关的统一标量机制，不排除算法实际收敛及其他原生证明。',['rlshear','rlscope']),
('r_natural','支撑函数 × 法锥自然类','example','RL','native','PROVED','完整逆、跨活跃面 proximal 敏感性和独立 residual gap 分别给 RL 与 EB；目标非孤立。',['rlnatural','rlscope']),
('r_direct','正常收缩 + 切向求和','proof_mechanism','RL','result','PROVED','当前 TeX Proposition 5.4 无需聚合余量，从全空间输入收敛，保留分块信息的证明更强。',['rldirect']),
('r_reverse','反向 Minty collision','counterexample','RL','result','OBSTRUCTED','只排除 AP-RL；不排除弱 solution-comparison 接口或旧合稿 Theorem 3.1。',['rlreverse']),
('r_native','原生 RL / EB 验证器','proof_mechanism','RL','native','PENDING','Jacobian、coderivative、活动集和分支信息应独立产出几何与残差证书；不能把 coverage 放进待证前提。',['rlmodules','rlrepair','rlgate']),
('r_gate','RL 版本 · gauge 价值门','open_blocker','RL','result','PENDING','当前 T4 未闭合、T5 暂定；补同版主张账本、一般 gauge 实际价值及最近理论逐定理比较。',['plan','rlgate']),
('c_face','冻结最小面 F','definition','CONIC','native','PROVED','F=Fmin(range DG(x̄)∩C)，随后所有秩在固定子空间上比较。',['crsc']),
('c_crsc','冻结 CRSC · 闭像与常秩','assumption','CONIC','certificate','PROVED','参考点闭像，加整邻域 rank(DG(x)*|F⊥) 恒定；nice 锥范围不可丢。',['crsc','rank']),
('c_rank','固定子空间 rank squeeze','proof_mechanism','CONIC','certificate','PROVED','像包含加秩半连续夹逼得到相等，先推稳定乘子/最小面，再得到附近闭像；无 A1/A2 循环。',['rank']),
('c_normal','公共流形 · 两次修正','proof_mechanism','CONIC','certificate','PROVED','法向修正 b=4/(ση)，再在同一流形作相对内点修正 4/τ_F。',['normal','mscq']),
('c_amenable','参考面相对 C amenable','assumption','CONIC','certificate','PROVED','d(y,F)≤a_F d(y,C)，y∈span F；不是只说 F 自身作为独立锥 amenable。',['mscq','universal']),
('c_mscq','CRSC → 原残差 MSCQ','theorem','CONIC','result','PROVED','proper nice + 冻结 CRSC + 参考面 amenability 给 d(x,G⁻¹(C))≤κ d(G(x),C)，κ=b+4a_F(1+L_Gb)/τ_F。',['mscq','conicaudit'],True),
('c_universal','amenability ⇔ 普遍 MSCQ','theorem','CONIC','result','PROVED','固定 proper nice 锥内，对所有有限维 apex C1 系统的 CRSC→MSCQ 等价于锥 amenability；常数不要求系统间统一。',['universal']),
('c_nice_bad','nice 非 amenable 边界','counterexample','CONIC','result','OBSTRUCTED','常导数 / full facial CRCQ 仍可无 MSCQ；反例仅有真实残差正且 O(t⁵)，不夸为 Θ(t⁵)。',['nicebad','conicgate']),
('c_examples','耦合 SOC / 高维 PSD','example','CONIC','native','PROVED','联合常秩、公共方程和显式常数正例；不是每个单块分别检查即可推出联合条件。',['coneex']),
('c_transfer','输出局部残差转移','certificate','CONIC','certificate','PENDING','条件性接口本身成立：还需算子零集等价、残差比较和独立算法假设；当前不声称完成 RL 应用。',['transfer','conicgate']),
('m_kernel','固定 Markov 核 P','definition','MARKOV','native','PROVED','P 决定分布演化和不变律，不单独决定同步位移残差矩阵 R。',['fixed','finite']),
('m_repr','合法随机映射表示 q','definition','MARKOV','native','PENDING','q≥0、Σq=1、Σ_{a:T_a(i)=j}q_a=P_ij；优化表示的完整结构定理仍是研究目标。',['repr']),
('m_residual','原始嵌套同步残差 Ψ','definition','MARKOV','certificate','PROVED','对所有不变律取 inf，再对该实际输入/目标对的最优 OT 计划取 inf；不得偷换为任意耦合或最近不变律。',['fixed']),
('m_ot','OT tight-edge 多面体','proof_mechanism','MARKOV','certificate','PROVED','Kantorovich 对偶顶点与互补松弛给精确有限并，不是松弛的单一 LP。',['ot']),
('m_exact','exact-zero：Ψ⁻¹(0)=I','certificate','MARKOV','certificate','PROVED','识别正确不变集合是条件；存在假零时不能把到残差零集的次正则当成到 I 的误差界。',['finite','countable']),
('m_eb','有限状态 exact-zero ⇔ EB','theorem','MARKOV','result','PROVED','固定状态几何、映射与概率时，exact-zero 等价全局线性 W₂ EB；不需要混合或几何收敛假设。',['finite','finiteaudit'],True),
('m_lazy','lazy 四状态 OT 正例','example','MARKOV','native','PROVED','全局最优 K²=13/p，局部 K²=4/p；35 为顶点数，20 为满维 cells，不能混称区域。',['finiteaudit','lazy']),
('m_rate','EB ≠ 严格一步速率证书','obstacle','MARKOV','result','OBSTRUCTED','lazy 四状态可相对 R 线性收敛，却无任何兼容源公式的 general gauge；不排除多步/换度量。',['lazy']),
('m_countable','紧致可数：无 Hölder EB','counterexample','MARKOV','result','OBSTRUCTED','正确 exact-zero、连续 RFI 与统一相对线性收敛可同时存在，但所有正 Hölder EB 失败；某个非兼容 general gauge 仍存在。',['countable','noholder','compactgauge'],True),
('m_mass','小质量稀释 / 矩阶障碍','obstacle','MARKOV','result','OBSTRUCTED','点态高阶 q>1 不能直接抬成 full-law RMS EB；Lp/Lr 的普适提升恰需 pq≤r。',['mass']),
('m_coupling','同一个原生兼容耦合','assumption','MARKOV','certificate','PENDING','能量、输出比较与残差都要同一合法四变量耦合；两个各自好的耦合不够。有限长度指分布路径。',['coupling']),
('m_conditional','冻结纤维 · 相关性修复','proof_mechanism','MARKOV','certificate','PROVED','固定边缘的条件度量可修复看不见相关性的残差；高斯全局锐常数 1/√ζ。不得等同普通 W₂ 必要性。',['conditional']),
('m_hls','HLS / Dobrushin 旧机制','definition','MARKOV','certificate','ALREADY_COVERED','固定纤维上的随机二次近端正类已在 HLS 收缩机制内；条件化或换拓扑不自动产生新颖性。',['hls','conditional']),
('m_selection','多值全局 prox 的随机选择','example','MARKOV','native','PROVED','原生非可分 group-ℓ0 例子有闭的二值图和 Borel 选择核；图闭不意味着核 Feller。',['selection']),
('m_nonfeller','有限长却趋于非不变律','counterexample','MARKOV','result','OBSTRUCTED','指定非 Feller 选择核有唯一不变律却有邻近有限长轨道趋于非不变律；不反驳满足全部前提的 T5。',['nonfeller','nativeeb'],True),
('m_frontier','同核不同表示：证书边界','open_blocker','MARKOV','result','PENDING','尚待证明同一核的合法表示具有不同可认证性、锐最优值或全表示不可能性对偶证书；不是已完成结果。',['repr','markovgate'],True),
('x_geometry','多值 / 非孤立几何','definition','CROSS','native','PROVED','RL 的非孤立目标/跨分支图，与 Markov 随机选择共享几何议题；集合值图、选择核和不变律仍是不同对象。',['rlnatural','selection']),
('x_native','原生信息 → 证书 → 后果','research_question','CROSS','native','PENDING','三线共同的问题是哪些信息在汇总后被丢失，哪些证书真能支持收敛；这是研究结构归纳，不是跨项目蕴含定理。',['rlgate','conicgate','repr']),
('x_priority','优先权 / 正式版文献门','open_blocker','CROSS','result','PENDING','锥 M01 正式发表版逐定理差分、RL 最近理论比较、Markov source-specific 优先权与同版合并审计均未完成。',['priority','rlgate','markovgate']),
]
for s in specs: entity(*s)

TYPES={
'DEFINES':('定义','#3577a5'),'ASSUMES':('前提','#a18436'),'IMPLIES':('推出','#31867b'),
'PROVES':('证明','#25775c'),'VERIFIES':('验证','#4d8b2b'),'AUDITS':('审计','#9362a4'),
'APPLIES_TO':('应用接口','#517ab8'),'COUNTEREXAMPLE_TO':('反例','#bd4d57'),'LIMITS':('限制','#bd7a30'),
'DOMINATES':('支配/覆盖','#96547d'),'SUPERSEDES':('版本替代','#687789'),'EXTENDS':('扩展','#178c9d'),
'OPEN_BLOCKER':('未闭合门','#bb662e'),'SOURCE_FOR':('来源/结构联系','#7571a9')}
H=[]
def member(e,role,t='ASSUMES',out=False): return dict(entity_id=e,role=role,direction='relation_to_entity' if out else 'entity_to_relation',relation_type=t,evidence_status=next((x['evidence_status'] for x in E if x['id']==e),assets.get(e.removeprefix('doc__'),{}).get('evidence_status','REFERENCE')))
def rel(id,name,t,status,statement,ms,refs,project,cross=False,coverage=None):
    H.append(dict(id=id,name=name,relation_type=t,evidence_status=status,statement=statement,members=[member(*m) for m in ms],sources=[S[r] for r in refs],projects=project,cross_project=cross,evidence_coverage=coverage or [],layout_band='CROSS' if cross else project[0]))

rel('h01','AP-RL ⇔ 耦合 Minty 图','DEFINES','PROVED','在同一图块、同一 λ 和图值下 AP-RL 等价于 Minty 单射及反射 Hölder；明确不推出输入覆盖。', [('r_graph','等价条件','DEFINES'),('r_minty','耦合图表','DEFINES',True),('r_coverage','独立要求，不由本关系推出','LIMITS',True)],['minty'],['RL'])
rel('h02','RL–PPA 收敛机制','IMPLIES','PROVED','RL 解比较或更弱反射证书 + 同步 EB 给 B/E；另加收缩、可求和预算与覆盖，推出所有允许步的有限长点收敛。', [('r_problem','研究问题','SOURCE_FOR'),('r_graph','几何的充分来源'),('r_minty','同图值反射'),('r_nearest','每步最近目标'),('gauge','独立残差证书'),('r_energy','步长与能量机制','PROVES'),('r_coverage','coverage + 预算'),('r_contraction','额外轨道控制'),('r_length','有限长度结论','IMPLIES',True),('r_main','主定理','IMPLIES',True)],['rlmain','rllegacy','rlscope'],['RL'])
rel('h03','固定 κ → 一般比较序列','EXTENDS','PENDING','当前 TeX Lemma 3.1 使用 a(k+1)=min(B,Φ)(a(k)) 与 ΣB(a(k)) 留域；这是当前稿新增层，旧合稿审计不自动覆盖。',[('r_contraction','一般比较序列'),('r_energy','可求和步长'),('r_coverage','留域与覆盖'),('r_main','旧 κ 版对照','SOURCE_FOR'),('r_gate','当前稿同版审计缺口','OPEN_BLOCKER',True)],['rlgeneral','plan'],['RL'])
rel('h04','幂型阈值与可达锐性','PROVES','PROVED','在 γ<1 的冻结步长幂证书信息类，γq 与 β(r)决定能否认证；二分支族支持分母 2 的统一渐近不可改进性。',[('r_power','指数与有效正半径'),('r_energy','保留 full-step cap'),('gauge','ψ(s)=Ks^q'),('r_sharp','可达见证','VERIFIES'),('r_main','限定的定量后果','IMPLIES',True)],['rlpower','rlsharp'],['RL'])
rel('h05','标量 exact 的信息边界','LIMITS','OBSTRUCTED','标量包络 exact 不是 operator-exact；退化剪切保有实际收敛，但指定位置无关的 scalar-rate 兼容证书失败。',[('r_envelope','被审计的信息松弛'),('r_shear','障碍见证','COUNTEREXAMPLE_TO'),('gauge','兼容 gauge 的限制','LIMITS',True),('r_contraction','不能反推不收敛','LIMITS',True)],['rlsharp','rlshear'],['RL'])
rel('h06','自然类独立认证','VERIFIES','PROVED','支撑函数/法锥模型分别经跨活动面 prox 敏感性和 residual gap 认证 RL 与 EB；纯 shear 验证器不能不加假设覆盖全模型。',[('r_natural','原生模型'),('r_native','判别器的作用域','LIMITS'),('r_graph','几何输出','VERIFIES',True),('gauge','残差输出','VERIFIES',True),('x_geometry','非孤立和跨分支','APPLIES_TO',True)],['rlnatural','rlscope','rlrepair'],['RL'])
rel('h07','直接分块支配汇总应用','DOMINATES','ALREADY_COVERED','Prop. 5.4 对同一自然类无聚合余量、全局输入且给更强率；Cor. 5.3 应定位为信息损失诊断，不能作为独家主应用。',[('r_direct','更强证明','DOMINATES'),('r_natural','完全同一算法/模型','APPLIES_TO'),('r_power','被支配的聚合条件','DOMINATES',True),('r_gate','贡献重定位','OPEN_BLOCKER',True)],['rldirect','rlgate'],['RL'])
rel('h08','Minty collision 的排除范围','COUNTEREXAMPLE_TO','OBSTRUCTED','反向例只否定 AP-RL，不否定弱解比较主接口；正向指定 finite 测试失败也不等于所有旧理论失败。',[('r_reverse','反例','COUNTEREXAMPLE_TO'),('r_graph','被排除对象','COUNTEREXAMPLE_TO',True),('r_main','不得扩大的排除范围','LIMITS',True),('r_direct','幸存的强机制','SOURCE_FOR')],['rlreverse','rlscope'],['RL'])
rel('h09','冻结 CRSC 的秩夹逼','PROVES','PROVED','固定 F⊥ 与 span F△ 的像在参考点相等，经常秩和下半连续夹逼得到邻域相等；随后推乘子、面与闭像稳定。',[('c_face','固定参考面'),('c_crsc','参考闭像与整邻域常秩'),('c_rank','非循环证明机制','PROVES',True),('c_normal','公共流形后续入口','IMPLIES',True)],['crsc','rank'],['CONIC'])
rel('h10','锥 CRSC → MSCQ','IMPLIES','PROVED','proper nice 锥内，冻结 CRSC→rank squeeze→normal correction；加参考面相对 C amenability，再作同流形切向修正，得到原残差 MSCQ。',[('c_face','冻结最小面'),('c_crsc','常秩及参考闭像'),('c_rank','rank squeeze','PROVES'),('c_normal','normal + relative-interior correction','PROVES'),('c_amenable','残差比较'),('c_mscq','原残差误差界','IMPLIES',True),('c_examples','耦合 SOC 与 PSD 正例','VERIFIES'),('doc__conic_tex','当前论文','SOURCE_FOR'),('doc__conic_core','独立核心审计','AUDITS')],['mscq','conicaudit'],['CONIC'])
rel('h11','amenable 的精确普遍量词','PROVES','PROVED','固定 proper nice 锥的 amenability 等价于所有 admissible apex C1-CRSC 系统满足 MSCQ；反向用每个面的等距包含测试。',[('c_amenable','正向参考面性质'),('c_face','反向每个面包含测试'),('c_mscq','全系统 MSCQ 性质'),('c_universal','等价刻画','IMPLIES',True)],['universal'],['CONIC'])
rel('h12','nice 不能替代 amenability','COUNTEREXAMPLE_TO','OBSTRUCTED','nice 非 amenable 例即使导数常值、full facial CRCQ 仍不满足 MSCQ；证实附加面残差性质不能普遍删掉。',[('c_nice_bad','显式 apex 反例','COUNTEREXAMPLE_TO'),('c_crsc','反例仍满足的条件'),('c_mscq','无 amenability 的错误扩大','COUNTEREXAMPLE_TO',True),('c_universal','必要性界限','LIMITS',True)],['nicebad','universal'],['CONIC'])
rel('h13','锥误差界接入 RL 的缺口','APPLIES_TO','PENDING','仅在算子零集=局部可行集且 d(G(x),C)≤χ(residual) 等接口单独成立时，MSCQ 可输出复合 gauge；收敛还需独立 RL/算法假设。',[('c_mscq','已证明的 MSCQ 模块'),('c_transfer','待实例化的零集/残差比较'),('gauge','条件性复合 gauge','IMPLIES',True),('r_main','潜在算法消费者，不是已完成应用','APPLIES_TO',True),('x_native','需补原生接口','OPEN_BLOCKER',True)],['transfer','conicgate'],['RL','CONIC'],True)
rel('h14','核、表示与原始残差','DEFINES','PROVED','固定 T_a、权重与状态几何定义 P,C,R；Ψ 保留原文的两重最小化。一个 P 不能单独确定表示依赖的 R。',[('m_kernel','分布动力学'),('m_repr','表示数据，优化尚待证'),('m_residual','源残差的精确定义','DEFINES',True),('m_ot','必须保留实际输入 OT','ASSUMES',True)],['fixed','finite'],['MARKOV'])
rel('h15','有限 OT → exact-zero ⇔ EB','PROVES','PROVED','Kantorovich tight-edge 的精确有限并 + 零残差顶点识别，给全局线性 EB；Hoffman 为独立证明。无需收敛假设，常数依赖固定数据。',[('m_ot','精确有限多面体机制','PROVES'),('m_exact','正确零集前提'),('m_residual','同一源残差'),('m_kernel','固定实际数据'),('m_eb','exact-zero/EB 等价','IMPLIES',True),('m_lazy','严格 OT 正例','VERIFIES')],['ot','finite','finiteaudit'],['MARKOV'])
rel('h16','lazy cycle：EB 与速率分离','LIMITS','OBSTRUCTED','全局 K²=13/p、局部 4/p；源 almost-firm 参数与严格 scalar-rate 对 gauge 的上界互斥，但实际相对 R 线性混合仍成立。',[('m_lazy','有理数见证','COUNTEREXAMPLE_TO'),('m_eb','存在 EB 但不够'),('m_residual','固定源残差'),('m_rate','速率兼容性被阻断','LIMITS',True),('gauge','任意兼容 general gauge 亦不行','LIMITS',True)],['finiteaudit','lazy'],['MARKOV'])
rel('h17','有限/无限状态的边界','COUNTEREXAMPLE_TO','OBSTRUCTED','紧致可数模型有 exact zeros、连续 RFI 和统一相对线性率，却没有任何正 Hölder EB；紧致性仍允许某个一般 gauge，不能宣称所有 gauge 不存在。',[('m_countable','连续紧致可数反例','COUNTEREXAMPLE_TO'),('m_exact','保留正确零集'),('m_eb','有限状态结论不得外推','LIMITS',True),('m_rate','特定速率公式也受阻','LIMITS',True),('gauge','一般 gauge 与兼容 gauge 分离','LIMITS',True)],['countable','noholder','compactgauge'],['MARKOV'])
rel('h18','点态高阶 → 矩匹配门','LIMITS','OBSTRUCTED','普适 ||e||Lp≤K||c||Lr^q 当且仅当点态界且 pq≤r。RL 的 p=2 对 q>1 需要至少 2q 阶残差，不能以 RMS 替换。',[('r_power','点态高阶输入'),('m_mass','小质量稀释见证','COUNTEREXAMPLE_TO'),('gauge','不能无条件提升','LIMITS',True),('m_coupling','矩之外仍需相关性','ASSUMES',True)],['mass','coupling'],['RL','MARKOV'],True)
rel('h19','合法随机 RL 的匹配假设','ASSUMES','PENDING','同一四变量耦合要同时实现能量、输出最优参照和残差；原生兼容耦合的存在是主要未证输入，有限长证明本身已过有界审计。',[('m_coupling','关键未证输入'),('r_energy','合法类比的能量结构'),('gauge','同一残差的 EB'),('r_length','分布有限长，不是样本路','APPLIES_TO',True),('m_frontier','原生表示/耦合问题','OPEN_BLOCKER',True)],['coupling'],['RL','MARKOV'],True)
rel('h20','相关性修复改变了接口','EXTENDS','PROVED','冻结边缘的条件 transport 可保留相关性并给精确 EB；所用拓扑不同，不能回填到原普通 W₂ 残差的能量式。',[('m_residual','原残差的相关性盲区'),('m_conditional','新的固定纤维接口','EXTENDS',True),('m_coupling','必须重新匹配的耦合','ASSUMES',True),('gauge','高斯 1/√ζ 定量 EB','IMPLIES',True)],['conditional','hls'],['MARKOV'])
rel('h21','正类被旧机制覆盖','DOMINATES','ALREADY_COVERED','不一致随机二次近端冻结保守变量后已有 HLS domination；Dobrushin / weak-Poincaré 等旧机制必须扣除。局部锐常数优先权另待核。',[('m_hls','已有理论机制','DOMINATES'),('m_conditional','被覆盖的正机制，不否定所有细节','DOMINATES',True),('m_coupling','条件与全局耦合不能混同','LIMITS'),('x_priority','source-specific 逐式扣除','OPEN_BLOCKER',True)],['hls','conditional'],['MARKOV'])
rel('h22','多值图 ≠ 连续选择核','COUNTEREXAMPLE_TO','OBSTRUCTED','group-ℓ0 全局 prox 的闭多值图仍可产生不可 Feller 的随机选择；唯一不变律不能保证有限长极限不变。该例不满足已证 RL 主定理的全部前提。',[('m_selection','原生多值随机模型'),('x_geometry','共享的集合值几何'),('m_nonfeller','非不变有限长极限','COUNTEREXAMPLE_TO',True),('m_coupling','物理参照/吸收边界','LIMITS',True),('r_main','不是其前提完整反例','LIMITS',True)],['selection','nonfeller','nativeeb'],['RL','MARKOV'],True)
rel('h23','Markov 表示—证书边界','OPEN_BLOCKER','PENDING','计划要求固定核、优化合法随机映射表示，比较 R(q)、能量 A(q)、OT 顶点、exact-zero、EB 和严格速率；须得同核严格分离/锐最优值/全表示不可能性，不能只写 LP。',[('m_kernel','必须保持的核'),('m_repr','待比较的合法表示'),('m_residual','表示依赖 R(q)'),('m_ot','候选有限顶点机制'),('m_exact','正确零集门'),('m_eb','固定表示已有 EB 定理','SOURCE_FOR'),('m_rate','已知兼容性反例','COUNTEREXAMPLE_TO'),('m_frontier','下一步未证命题','OPEN_BLOCKER',True)],['repr','markovgate'],['MARKOV'])
rel('h24','广义次正则：三线共用接口','SOURCE_FOR','PENDING','三线都从原生残差控制集合距离，但 RL residual、原锥 residual 与 invariant-transport Ψ 不是同一量；这里是可比较框架，不是相互自动推出。',[('gauge','共用概念框架','SOURCE_FOR'),('r_main','确定性算法接口','APPLIES_TO',True),('c_mscq','锥可行性线性实例','APPLIES_TO',True),('m_eb','固定有限状态 W₂ 实例','APPLIES_TO',True),('c_transfer','跨域残差比较门','OPEN_BLOCKER'),('m_coupling','随机匹配门','OPEN_BLOCKER')],['rlmain','transfer','finite'],['RL','CONIC','MARKOV'],True)
rel('h25','多值 / 非孤立：共享而不等同','SOURCE_FOR','PROVED','非孤立目标、跨活动面和多值选择连接两条主线；RL 完整逆、随机选择策略、核连续性是三类不同的证明义务。',[('x_geometry','共同几何主题','SOURCE_FOR'),('r_natural','非孤立/跨活动面正例','APPLIES_TO',True),('r_reverse','跨图值 collision','LIMITS'),('m_selection','原生随机选择','APPLIES_TO',True),('m_nonfeller','图闭不足以传递不变性','LIMITS')],['rlnatural','rlreverse','selection'],['RL','MARKOV'],True)
rel('h26','原生信息 → 证书 → 收敛/障碍','SOURCE_FOR','PENDING','研究层归纳：RL 分块/分支、锥固定面/法向、Markov 核/表示，经不同证书产生收敛或障碍；汇总丢失相关信息是共通风险。',[('x_native','研究组织原则','SOURCE_FOR'),('r_native','分支验证器','SOURCE_FOR'),('c_face','面与法向数据','SOURCE_FOR'),('m_repr','表示耦合数据','SOURCE_FOR'),('r_main','条件性收敛终点','APPLIES_TO',True),('c_mscq','残差终点，不是收敛','APPLIES_TO',True),('m_frontier','未闭合证书终点','OPEN_BLOCKER',True),('m_mass','失效风险','LIMITS',True)],['rlgate','transfer','repr','mass'],['RL','CONIC','MARKOV'],True)
rel('h27','优先权 / 文献 / 版本硬门','OPEN_BLOCKER','PENDING','内部证明通过不等于正式版逐定理优先权通过。锥 M01 VOR、RL 最新比较、Markov 原始残差与表示文献，以及论文同版合并审计都需保留阻塞。',[('x_priority','全局未闭合门','OPEN_BLOCKER',True),('r_gate','RL 贡献与同版门','OPEN_BLOCKER'),('m_frontier','Markov 新定理和文献门','OPEN_BLOCKER'),('doc__rl_md','旧合稿，不冒充当前版','SOURCE_FOR'),('doc__rl_referee','RL 总审计','AUDITS'),('doc__conic_tex','当前锥稿','SOURCE_FOR'),('doc__conic_core','锥内部审计','AUDITS'),('doc__finite_audit','有限状态审计','AUDITS'),('doc__frankowska','原始论文参考，非充分优先权清单','SOURCE_FOR')],['priority','rlgate','markovgate','frank'],['RL','CONIC','MARKOV'],True)
rel('h28','后续工作基线覆盖历史验收','SUPERSEDES','PENDING','9月10日计划明确覆盖旧状态/历史任务的行动基线；这不是本图作出新的阶段验收。RL 旧稿审计不能自动传递给当前排版稿新增内容。',[('doc__open_plan','当前保守工作基线','SUPERSEDES'),('doc__oldstate','历史 passed 记录，不作现行许可','SUPERSEDES',True),('r_gate','当前 RL 未闭合','OPEN_BLOCKER',True),('m_frontier','本月未证目标','OPEN_BLOCKER',True),('x_priority','独立外部证据门','OPEN_BLOCKER',True)],['plan','conicgate'],['RL','CONIC','MARKOV'],True)
rel('h29','从原始来源到限定主张','SOURCE_FOR','REFERENCE','文献和审计是来源证据，不因包内存有一篇原始论文就得出新颖性已证；Frankowska 原件仅保留文件级定位，未伪造页码或定理应用。',[('doc__frankowska','可核查原始文献原件','SOURCE_FOR'),('doc__rl_referee','限制来源适用范围','AUDITS'),('gauge','广义正则性议题','SOURCE_FOR',True),('x_priority','优先权仍待核','OPEN_BLOCKER',True)],['frank','rlrepair','priority'],['RL','CONIC','MARKOV'],True)

def evidence(id,name,claim,proof,audit,example,code,final,refs,status):
    slots=[]; ms=[(claim,'受证据链约束的主张','PROVES',True)]
    types={'proof':'PROVES','independent_audit':'AUDITS','example_or_counterexample':'VERIFIES','validation_code':'VERIFIES','final_manuscript':'SOURCE_FOR'}
    labels={'proof':'证明文件','independent_audit':'独立审计','example_or_counterexample':'例子/反例','validation_code':'验证代码','final_manuscript':'最终稿位置'}
    for key,val in [('proof',proof),('independent_audit',audit),('example_or_counterexample',example),('validation_code',code),('final_manuscript',final)]:
        ids,note=val
        slots.append({'slot':key,'label':labels[key],'availability':'PRESENT' if ids else 'MISSING','asset_ids':ids,'note':note})
        for aid in ids:
            eid='doc__'+aid
            oldm=next((m for m in ms if m[0]==eid),None)
            if oldm:
                ms[ms.index(oldm)]=(eid,oldm[1]+'；'+labels[key],oldm[2])
            else:ms.append((eid,labels[key],types[key]))
    # Plan/source members are not mislabelled as a missing proof or audit.
    for ref in refs:
        eid='doc__'+S[ref]['asset_id']
        if len(ms)<3 and not any(m[0]==eid for m in ms): ms.append((eid,'待办定义/范围来源，不是证明','SOURCE_FOR'))
    # Each evidence hyperedge has one exact claim plus actual participating files.
    rel(id,name,'AUDITS',status,'证据完整性核对；代码只证明其实际覆盖的实例/代数检查，不代替一般定理。当前任务未执行数学研究脚本。',ms,refs,[next(e['project'] for e in E if e['id']==claim)],coverage=slots)
evidence('h30','证据包：RL 主定理','r_main',(['rl_md','rl_chain'],'旧合稿主定理及完整量词'),(['rl_delta','rl_referee'],'旧合稿审计存在；当前 TeX 新增 Lemma 3.1 未同版审计'),(['rl_recheck','rl_separate'],'例子/反例和常数复核'),(['rl_test'],'仅实例与常数验证；本轮 NOT_EXECUTED'),(['rl_tex','rl_pdf'],'当前 TeX §3 Theorem 3.2；旧 T5 为 Theorem 3.1，禁止混用行号'),['rllegacy','rlmain','rlscope'],'PROVED')
evidence('h31','证据包：锥 MSCQ','c_mscq',(['conic_tex'],'§4 theorem thm:mscq'),(['conic_core'],'PA-CORE §5，内部证明通过'),(['conic_examples','conic_boundary'],'SOC/PSD 正例与 nice 非 amenable 边界'),(['conic_test'],'实例常数核验，不是一般证明；本轮 NOT_EXECUTED'),(['conic_tex','conic_pdf'],'§4 Amenability and the original-residual error bound；标签 thm:mscq'),['mscq','conicaudit','coneex','nicebad'],'PROVED')
evidence('h32','证据包：有限状态分类','m_eb',(['finite'],'Theorem 1；§2–§6'),(['finite_audit'],'§3 general finite-state theorem；以 §6 修正为准'),(['finite','finite_audit'],'§10 OT-dependent 四状态；全局和局部常数分开'),(['finite_test','finite_exact'],'双程序已存；本轮 NOT_EXECUTED'),([], '缺失：尚无统一正式 Markov 论文；finite 文件只是当前研究主文'),['finite','finiteaudit','markovgate'],'PROVED')
evidence('h33','证据包：无限状态障碍','m_countable',(['markov_counter'],'§13 独立重建证明；原始提案全文未纳入 v1'),(['markov_counter'],'独立审计 §11–§14，证明与审计同一保留文件'),(['markov_counter'],'紧致可数构造及无 Hölder 见证'),(['markov_ext'],'投影与可数紧致扩展检查；本轮 NOT_EXECUTED'),([], '缺失：尚无统一正式稿中的定理位置'),['countable','noholder','compactgauge'],'OBSTRUCTED')
evidence('h34','证据包：随机选择障碍','m_nonfeller',(['native'],'Theorem 5.1、Corollary 5.2'),([], '缺失：文件声称兄弟审计已做，但 v1 未保留可单独对应的完整独立审计，不能充数'),(['native'],'非可分 group-ℓ0 原生二值图'),(['native_test'],'原生近端与吸收例检查；本轮 NOT_EXECUTED'),([], '缺失：未形成统一正式稿'),['selection','nonfeller','nativeeb'],'OBSTRUCTED')
evidence('h35','证据包：同核表示前沿','m_frontier',([], '缺失：计划中的目标尚未证明'),([], '缺失：没有该待证定理的独立通过审计'),(['finite_audit'],'现有 lazy 正/负基准不是同核不同表示严格分离的成品'),([], '缺失：没有完整表示优化/全表示不可能性的已验程序'),([], '缺失：没有正式稿位置'),['repr','markovgate'],'PENDING')

README='''# 研究资产统一超边知识图 v2

入口：[研究资产统一超边知识图_v2.html](研究资产统一超边知识图_v2.html)。完全离线，无 CDN、远程字体、网络依赖。单独 HTML 可浏览全部关系、准确来源摘录及下载 68 份保留的原始研究资产；解压 ZIP 后还能沿相对路径打开所有整理文件。旧版 [研究资产总览与超边图.html](研究资产总览与超边图.html) 仅作历史界面保留，不是 v2 的超边实现。

## 这是怎样的超图

采用严格的关联二部表示：圆角实体卡/圆标是实体，带名称的六边形是超边；每条超边连接至少三个不同实体。关联只发生于“实体↔超边”，没有把无标签分组轮廓假装为关系。每条成员关联都记录角色、方向、关系类型和状态；箭头指示实体输入关系，或关系输出到实体。点击六边形同时高亮所有成员、角色和方向；点击实体显示它参加的全部超边。

主图按“原生信息/问题 → 定义/证书 → 定理/收敛/障碍”分区，下方是证据文件。RL、锥、Markov 的分带只是空间导航，跨项目超边处于统一图中。关系数量、证据缺失、项目筛选不等于逻辑独立性。层级布局为人工语义定位；力导向是可选探索视图。

## 怎样回答关键问题

- RL 由什么推出：h02；幂率 h04；反例限制 h05/h08；为什么自然类应用被支配 h07；证明、审计、代码和版本差异 h30。
- 锥与 RL 为什么相关：h10 给 MSCQ，h13/h24 明示它接入 RL 仍需独立的零集和残差比较；不是已经完成的 RL 应用。
- Markov 为何相关：h15 是有限源残差 EB；h16/h17 区分 EB、exact-zero、兼容速率；h18/h19 给随机提升的矩阶与耦合门；h23 是待证的同核表示边界。
- 下一步卡在哪里：h27/h28/h35。内部数学证明、同版审计、原始文献优先权和应用价值是不同门。

## 操作

顶部可按关系类型、项目、证据状态筛选并搜索；下方关系列表可直接定位 35 条超边。证据类型过滤同时检查主关系与成员关联类型。语义层默认展示精选实体；“文档叶节点”显示参与关系的其他原件；文件层显示全部保留资产及映射，未直接作为核心数学证据的文件明确标为档案/构建/导航，不凭文件名推导数学关系。缩放、拖动节点、拖动画布、重置与迷你图均离线有效。点击“证据”会展开五类槽位，缺失就显示缺失。

## 证据与版本规则

PROVED 仅表示指定作用域下已有项目证明和对应内部审计支持，不表示全球首创或当前整稿已验收。PENDING、OBSTRUCTED、ALREADY_COVERED 分别对应未闭合、指定机制被阻断、具体正机制已被覆盖。REF/REFERENCE 是来源、组织材料；NOT_EXECUTED 是本轮未运行数学脚本。代码节点不会被标成证明通过。

RL 旧 Markdown 的 Theorem 3.1 对应当前 TeX 的 Theorem 3.2；当前 TeX 新增比较序列 Lemma 3.1 另列 PENDING，旧审计的 1881 行和哈希不能移植。锥正式版 M01 门仍待核。Markov 没有统一正式稿。随机选择障碍缺少包内独立完整审计；其状态仅沿用报告边界，不假造证据齐全。

所有来源定位来自真实文件的命中行与原始标题，保存于 JSON 的 sources 和 [标题与定位抽取记录_v2.json](标题与定位抽取记录_v2.json)。未定位的 PDF 只标文件级，不伪造页码。跨项目 SOURCE_FOR 归纳不是新数学蕴含。此任务不检索或更新外部文献、不改写原始研究正文、不运行研究数学脚本、不推进论文阶段。

## 完整性与复核

v1 的 68 个研究原件字节及中文映射 CSV 原样保留；旧图也保留。新增或替换的都是整理层文件。全部保留文件都在资产数据与 manifest 中映射。HTML 嵌入 JSON 与外部 [资产关系数据.json](资产关系数据.json) 完全一致。

运行 `python3 00_从这里开始/校验_v2.py` 做 JSON schema、实体引用、成员数/角色/方向、文档映射、原件 SHA256、HTML/JSON 一致性及相对链接检查；运行 `node 00_从这里开始/交互模拟测试_v2.cjs` 做离线 DOM 事件模拟，Node 语法检查由校验器执行。`sha256sum -c 00_从这里开始/SHA256文件校验清单.txt` 校验全包（清单不散列自身）；manifest 不自散列。最终 ZIP 另做实际解压逐文件核验。

本地没有可用 Chromium/Firefox/WebKit 二进制，没有安装浏览器；因此未做真实浏览器截图 QA、真实字体/高密度排版或物理指针交互验收。静态与模拟测试不能替代该项。
'''
(NAV/'README_研究资产导航.md').write_text(README,encoding='utf-8')
dump(NAV/'标题与定位抽取记录_v2.json',extraction)
for src,dest in [('build_v2.py','构建_v2.py'),('graph_template.html','图模板_v2.html'),('validate_v2.py','校验_v2.py'),('test_interactions.cjs','交互模拟测试_v2.cjs'),('schema_v2.json','资产关系_schema_v2.json')]:
    if (WORK/src).exists(): shutil.copy2(WORK/src,NAV/dest)

contract={'contract_version':'1.0','expert_skill':'sci-skills-scientific-figures','project_id':None,'paper_family':None,'stage_id':None,'task_id':None,'task_status':'COMPLETE','inputs_reviewed':['v1 ZIP / manifest / 中文映射','当前 RL TeX 与旧合稿独立审计','锥当前 TeX、核心/边界/正例/优先权审计','Markov 分类、正负结果与研究计划'],'outputs':[HTML_NAME,'资产关系数据.json','资产关系_schema_v2.json','校验_v2.py','交互模拟测试_v2.cjs'],'evidence_status':['VERIFIED_USER_MATERIAL','AI_INFERENCE: 跨项目结构性综合，不是新定理','NOT_EXECUTED: 数学脚本 / 浏览器截图'],'assumptions':['这是已获请求的导航解释图，不插入论文正文','图中 PROVED 为项目内作用域判断'],'author_input_needed':[],'manual_actions':[],'quality_checks':['参见 测试报告_v2.json'],'conflicts':['旧 RL 合稿审计与当前新增 Lemma 3.1 版本范围不同，显式分离','历史 passed 记录与 9月10日保守基线不同，按后续计划导航而不改阶段'],'conflict_resolution_status':'UNRESOLVED','merge_permission':'orchestrator_only','recommended_next_action':'用真实浏览器检查高密度图的字形与交互','stage_acceptance_recommendation':'NOT_ASSESSED'}
dump(NAV/'解释图执行契约_v2.json',contract)

# New organizer entries; no research file is fabricated or overwritten.
extra=[('v2graph',HTML_NAME),('v1manifest','历史manifest_v1.json'),('v1relations','历史资产关系数据_v1.json'),('v1readme','README_v1_历史导航.md'),('v2extraction','标题与定位抽取记录_v2.json'),('v2build','构建_v2.py'),('v2template','图模板_v2.html'),('v2validator','校验_v2.py'),('v2events','交互模拟测试_v2.cjs'),('v2schema','资产关系_schema_v2.json'),('v2contract','解释图执行契约_v2.json'),('v2tests','测试报告_v2.json')]
for aid,filename in extra: assets[aid]={'id':aid,'path':'00_从这里开始/'+filename,'type':'v2 整理层','evidence_status':'REFERENCE','source':'GENERATED:v2_真实超边图','authoritative':False}
core_docs={'rl_md','rl_referee','rl_test','conic_tex','conic_core','finite','finite_audit','frankowska','open_plan'}
for aid,a in assets.items():
    oldn=oldnodes.get(aid,{})
    p=ROOT/a['path']; israw=not a.get('source','').startswith('GENERATED:')
    project={'01':'RL','02':'CONIC','03':'MARKOV'}.get(a['path'][:2],'CROSS')
    a['project']=project;a['retained_from_v1']=aid in {x['id'] for x in v1['files']};a['research_original']=israw
    a['original_source']=a.get('source','');a['heading_count']=len(next((x['headings'] for x in extraction if x['asset_id']==aid),[]))
    a['mapped_hyperedges']=[h['id'] for h in H if any(s['asset_id']==aid for s in h['sources']) or any(m['entity_id']=='doc__'+aid for m in h['members'])]
    a['mapping_role']='直接证明/审计/来源' if a['mapped_hyperedges'] else ('保留研究资产；非精选核心证据' if israw else '构建/导航/历史整理层')
    a['sha256_original']=a.get('sha256') if israw else None
    kind='code' if p.suffix in ['.py','.sh'] else ('original_literature' if aid=='frankowska' else ('audit' if 'audit' in aid or aid in ['rl_referee','rl_delta','rl_recheck','conic_core','conic_boundary','mass'] else ('paper' if aid in ['rl_md','rl_tex','rl_pdf','conic_tex','conic_pdf','finite'] else 'document')))
    title=next((x['headings'][0]['text'].lstrip('# ') for x in extraction if x['asset_id']==aid and x['headings'] and p.suffix=='.md'),p.name)
    E.append({'id':'doc__'+aid,'asset_id':aid,'label':{'rl_md':'RL 旧 T5 合稿','rl_referee':'RL 总体独立审计','rl_test':'RL 实例验证代码','conic_tex':'锥 v04 当前 TeX','conic_core':'锥核心证明审计','finite':'有限状态分类证明','finite_audit':'有限状态独立审计','frankowska':'Frankowska 1989 原件','open_plan':'9月10日后续研究计划'}.get(aid,p.stem),'kind':kind,'project':project,'layer':'evidence','evidence_status':a.get('evidence_status','REFERENCE'),'statement':oldn.get('purpose','')+'；'+oldn.get('conclusion','')+'；原文标题：'+title,'sources':[source(aid)] if israw and (aid in texts or aid=='frankowska') else [],'core':aid in core_docs,'core_claim':False,'document_leaf':True})

# Deterministic semantic layout: native left; definitions/certificates middle;
# claims/limits right; visible named relations in dedicated incidence lanes.
band_y={'RL':245,'CONIC':770,'MARKOV':1200,'CROSS':60}
slots=collections.defaultdict(int)
for e in E:
    if e['layer']=='evidence': continue
    k=(e['project'],e['layer']);i=slots[k];slots[k]+=1
    if e['project']=='CROSS':
        e['x']={'native':150+280*i,'certificate':1110,'result':2140}[e['layer']];e['y']=80
    else:
        xs={'native':[150,390],'certificate':[1030,1280],'result':[1900,2150]}[e['layer']]
        e['x']=xs[i%2];e['y']=band_y[e['project']]+(i//2)*100
docs=[e for e in E if e['core'] and e['document_leaf']]
for i,e in enumerate(docs):e['x']=150+(i%9)*270;e['y']=1850
for i,e in enumerate(x for x in E if x['document_leaf'] and not x['core']):e['x']=140+(i%10)*245;e['y']=2000+(i//10)*86
relation_slots=collections.defaultdict(int)
for h in H:
    if int(h['id'][1:])>=30:
        i=int(h['id'][1:])-30;h['x']=240+i*415;h['y']=1715
    elif h['cross_project']:
        i=relation_slots['CROSS'];relation_slots['CROSS']+=1
        h['x']=2460;h['y']=245+i*140
    else:
        b=h['layout_band'];i=relation_slots[b];relation_slots[b]+=1
        h['x']=710 if i%2==0 else 1610;h['y']=band_y[b]+(i//2)*110+42

D={'schema_version':'2.0.0','representation':'directed_incidence_bipartite_hypergraph','snapshot_date':'2026-09-14','offline':True,'semantics':'六边形是带名称、方向和成员角色的多元关系。跨项目 SOURCE_FOR 是有来源的研究归纳，不等于定理蕴含。','evidence_scope':'项目内文档证据；未重做数学证明、文献搜索、研究脚本执行或阶段验收。','relation_types':{k:{'label':v[0],'color':v[1]} for k,v in TYPES.items()},'entities':E,'hyperedges':H,'assets':list(assets.values()),'core_entity_count':sum(e['core'] for e in E),'semantic_entity_count':sum(not e['document_leaf'] for e in E),'v1_original_count':v1['copied_original_count'],'v1_zip_sha256':sha(V1ZIP.read_bytes()),'missing_evidence_policy':'MISSING 显示为缺失；不通过添加假文件节点填满证据槽。'}
dump(NAV/'资产关系数据.json',D)
payload={}
for aid,a in assets.items():
    if a['research_original']:
        payload[aid]=base64.b64encode((ROOT/a['path']).read_bytes()).decode()
template=(WORK/'graph_template.html').read_text()
html=template.replace('__GRAPH_DATA__',json.dumps(D,ensure_ascii=False).replace('</',r'<\/')).replace('__ASSET_PAYLOADS__',json.dumps(payload,ensure_ascii=False))
(NAV/HTML_NAME).write_text(html,encoding='utf-8');(OUT/HTML_NAME).write_text(html,encoding='utf-8')

def finalize_manifest():
    paths={a['path']:a for a in assets.values()}
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():continue
        rp=p.relative_to(ROOT).as_posix();a=paths[rp]
        late=rp in ['00_从这里开始/manifest.json','00_从这里开始/SHA256文件校验清单.txt']
        files.append({'id':a['id'],'path':rp,'source':a['source'],'type':a['type'],'evidence_status':a['evidence_status'],'authoritative':a.get('authoritative',False),'sha256':None if late else sha(p.read_bytes()),'size_bytes':None if late else p.stat().st_size,'hash_note':'self/later-generated; see SHA256清单' if late else None})
    m=dict(v1);m.update(schema_version='2.0.0',file_count=len(files),files=files,v1_zip_sha256=D['v1_zip_sha256'],non_destructive=True,original_bytes_preserved=True,generated_count=len(files)-v1['copied_original_count'],hypergraph={'entities':len(E),'core_entities':D['core_entity_count'],'hyperedges':len(H),'cross_project_hyperedges':sum(h['cross_project'] for h in H)})
    dump(NAV/'manifest.json',m)
    lines=[sha(p.read_bytes())+'  '+p.relative_to(ROOT).as_posix() for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='SHA256文件校验清单.txt']
    (NAV/'SHA256文件校验清单.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
if not (NAV/'测试报告_v2.json').exists():dump(NAV/'测试报告_v2.json',{'status':'PENDING: run validator before packaging'})
finalize_manifest()
# ZIP v1 has future-dated 2026-09-14 entries relative to this runtime clock.
# Keep new organizer mtimes later than that baseline to prevent sync rollback.
sync_mtime=datetime.datetime(2026,9,15,tzinfo=datetime.timezone.utc).timestamp()
for a in assets.values():
    if not a['research_original']:
        p=ROOT/a['path'];os.utime(p,(sync_mtime,sync_mtime))
print(json.dumps({'core_entities':D['core_entity_count'],'semantic_entities':D['semantic_entity_count'],'all_entities':len(E),'hyperedges':len(H),'cross':sum(h['cross_project'] for h in H),'assets':len(assets)},ensure_ascii=False))
