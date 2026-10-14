# 次单调路线比较的局部接收记录

日期：2026-10-14 UTC。基线提交 0347b57c681bf71b34a9df332952eb52f1e8dbf2。本轮为比较研究和论文定位：不改变既有 Claim、主稿、摘要、编号或原投稿包。报告级 GU1/GU3 保留 candidate，不授予新公开首创或新主定理。

## 实际研究与独立接收

用户明确请求 teamwork。五路分别审原变量/函数结构、逆图耗散、半单调/矩阵、一般预算、变分序；第六路 GPT-6 Astra 在事先独立判准与攻击后全文冷读五份实际报告。原变量、半单调、一般预算与独立反审均为 Astra ultra；逆图与变分序为 GPT-6.1-sol ultra。根代理实际读取当前协议、已有 C249/C250、参数字典、Spingarn作者定义和SC14候选结构，全文读取六路报告与综合报告，并逐式重构最强比较。

根代理独立重开 LT 正式PDF Definition2/Proposition4/Assumption2/Theorem2、Otero–Iusem2010作者稿Def2/Prop5及后续正则化接口、DG作者稿一阶式及Thm2、Evens固定v2 Def2.1/AssumptionI/Thm2.4/Def4.1、CP作者稿。Rolewicz扫描、DM、prox-regular、BMW、CP矩阵和其他原模型文献的额外实际读取归各分工，不倒写为根代理逐篇全文审查。版本/DOI/定位和未取得全文均在分报告及文献表。

[综合报告](../../发表成果整理/本轮重构/不同次单调与一般模路线_比较研究_2026-10-14.md)已交独立Astra实际全文冷读：OI同类、diag任意合法scalar范围、GU3固定物理C250排除、inverse临界点收敛/无限长度、全零锚凸性以及最终建议均无fatal objection。采用其建议，将“有势函数时用…”收窄为先认证势函数/曲率前件。

## 实际纠正与限定

1. 变分序旋转例原见证的 y 符号写错，改为 y=(0,−2) 得内积−6；验证器增加整数精确断言并复跑。点收敛和无限长度证明不变。
2. 一般预算报告修正了黏连的 LaTeX 命令和控制字符。初稿GU2标准投影父定理因与SC14–SC15重复删除，只保留实际结构比较；独立报告记录该去重，不能仍指向不存在的独立单元。
3. LT Assumption2(d)(ii) 的同一句确实同时包含coverage与兼容；统一用“Assumption2(d)显示兼容门”避免误读，不把原编号判为源事实错误。
4. 半单调的足够负临界参数可使任何图满足不等式；非Lip反例只排有用非退化参数、同一步长和相同图量词，不能宣布它不属于任何半单调类。
5. 新一般D不是获胜框架。即便D仅保两范数，仍可与独立EB假组合；关键是保法向/分支/输出距离的相关性。可和实际物理步长及零输入驻定门不可删。
6. 全零锚weakMinty的凸性结论有convS覆盖和lambda+rho>0门；它不向单锚或局部管外推。全图正则性与零锚算法合同分层，现C249/C250本来允许多值。

## 执行、持久出处与资产范围

实际执行 python3 research/code/submonotonicity_routes/run_all.py，六个脚本返回码全部0；完整stdout/stderr、Python版本与脚本hash见 [all_verifiers_output.json](../code/submonotonicity_routes/all_verifiers_output.json)。根脚本另外反算714个同图换参、500个平移Cayley恒等式和6138个完整分支转移；有理数精确计算与浮点实例分开。所有全称由正文解析证明承担，不由数值数量决定。

下载的一手全文仅作临时取证，已移至本地 tmp；不提交外文全文。持久出处为报告中的公共URL、固定版本、定义页和hash。保留少数未读正式刊本/全文的边界，不据摘要判包含。此前 INEXACT / STRUCTURAL / NOVELTY_DEVELOPMENT manifests 保持原字节；本轮 [新manifest](SUBMONOTONICITY_ROUTES_MANIFEST_2026_10_14.json)单独绑定实际文件。

只更新文献、活跃障碍、失败路线、代码登记和README导航。没有新canonical节点/边，权威图与三个离线视图不变；链接/状态/图一致性校验与diff检查用于结构验收，不替数学或价值判断。全球先行性、自然认证成本优势、新方向性父定理仍未完成。
