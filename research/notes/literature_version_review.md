# LMZ/MOR 版本与引用边界审计

日期：2026-11-17  
审计对象：`research/LITERATURE.md`、`research/audit/PPA_NEXT_STAGE_2026-11-17.md`、`research/notes/target2_kl.md` 及其所引用的 Li–Mordukhovich–Zhu (LMZ) 文献。  
范围：只审查 paper fact、正式版与 arXiv v1 的版本边界、定理编号归属及引用是否过度；不修改 `CLAIMS.md` 或任何 canonical claim。

## 1. 本轮可核对的一手记录

### 1.1 正式 INFORMS 页面

已核对出版社页面：

`https://pubsonline.informs.org/doi/10.1287/moor.2024.0570`

该页面目前明确显示：

- 题名 *Generalized Metric Subregularity with Applications to High-Order Regularized Newton Methods*；
- 作者 Guoyin Li、Boris Mordukhovich、Jiangxing Zhu；
- DOI `10.1287/moor.2024.0570`；
- Received 2024-06-19、Accepted 2026-03-02、Published Online 2026-04-07；
- 状态为 Articles in Advance，`Cite as` 显示 *Mathematics of Operations Research* `0(0)`，未给卷号、期号或页码；
- 正式摘要把压缩感知模型称为 **Hadamard reparameterized compressed sensing model**，并列出新的资助信息（包括 DP250101112）；
- 页面可核的只是元数据、摘要、关键词、致谢和文章状态。

当前工具打开出版社 PDF 链接仍被重定向到摘要/访问页，未取得可搜索的正式刊本全文。因此出版社页面**不能**核定 Definition 3.1、Theorem 4.3–4.4、Theorem 5.1–5.2、Remark 5.3 在正式版中的编号、假设、常数、证明或页码。

### 1.2 arXiv v1

已核对 arXiv 固定版本：

`https://arxiv.org/abs/2406.13207v1` 及 `https://arxiv.org/pdf/2406.13207v1`

该记录明确显示：

- Submitted on 19 Jun 2024；
- submission history 只有 `[v1] Wed, 19 Jun 2024 04:36:32 UTC`；
- 33 pages (including appendix), 2 figures；
- v1 PDF 首页日期为 June 21, 2024，页脚标为 `arXiv:2406.13207v1 [math.OC] 19 Jun 2024`；
- v1 的摘要使用 **over-parameterized compressed sensing model**；
- v1 HTML/PDF 明确出现 `Definition 3.1`、`Theorem 4.3`、`Theorem 4.4`、`Theorem 5.1`、`Theorem 5.2` 和 `Remark 5.3`，以及相应的 Section 3–5。

因此下列编号和页码（例如 Definition 3.1、Theorem 4.3–4.4、Theorem 5.1–5.2、Remark 5.3，及 v1 页码 4、8–13 一类定位）只能标为 **arXiv:2406.13207v1 的版本事实**。目前不能把它们自动写成正式 MOR 刊本的编号或页码。

## 2. 与三份项目文件的逐项核对

### 2.1 `target2_kl.md`

该文件的版本边界基本正确：它把 `mor/paper.txt` 和 `lmz-src/main_update.tex` 明确固定为 arXiv v1 抽取，并在“正式出版版本检索状态”中说明出版社全文不可得、正式版定理级差异为 unknown。它还正确记录正式摘要从 “over-parameterized” 改为 “Hadamard reparameterized”，并记录正式版资助信息变化。

需保留的审计结论：

1. `Theorem 4.3/4.4/5.1/5.2` 的详细公式、H0–H3、(H1')、(5.1)、`2σ` 根方程、Remark 5.3 速率式，均是 v1 paper fact；正式版只能称“元数据/摘要已核，公式级版本未知”。
2. `mor/official.pdf` 是 cookie/访问 HTML，不是正式 PDF；不能把它当作正式全文差异证据。
3. 普通 exact PPA 的接口映射是本库的 **PPA transfer/derived result**，不是出版社摘要直接宣称的结论；调用时仍须补 level boundedness、accumulation point、H3、解存在/选取等前件。

该文件的主要风险不是数学内容，而是后续引用者若只读摘要，可能把 v1 的定理编号或 PPA transfer 当成正式版或论文摘要事实。建议在引用定理的段首再次写明“以下均归属于 arXiv v1”。

### 2.2 `PPA_NEXT_STAGE_2026-11-17.md`

第 2.1 节把正式页面列为 paper fact，并把 v1 定理编号单独列出，整体分层正确。建议理解为：

- “正式版本（Paper fact）”只覆盖题名、作者、DOI、日期、Article in Advance 状态和摘要；不覆盖正式版定理内容；
- 表格中 Definition 3.1、Theorem 4.3–4.4、Theorem 5.1 的编号和页码须加上 `arXiv:2406.13207v1` 标签；
- “不用传统 MSR 的有限长度证明”应保留 H1'、H2、H3、bounded level set、accumulation point 和 (5.1) 的限定，不能简化成“KL 单独给出有限长度”。

第 6 节将“正式 LMZ 刊本全文的公式级版本差异仍未核对”列为未完成义务，这一点与本轮官方页面复核一致，应继续保留。

### 2.3 `research/LITERATURE.md` LMZ 段落

该段的定理编号和内容抽取与 v1 一致，但标题式开头

> `Paper fact（版本已核）`

容易被读成“正式刊本与 v1 已完成版本核对”。现有证据只支持“正式版元数据/摘要已核，v1 全文已核，正式版定理级差异未知”。建议将其解释或未来改写为：

> **Paper fact（正式元数据已核；定理级以 arXiv:2406.13207v1 为准，正式版未知）**

该段还有一个文字/条件问题：

- “Theorem 5.1 在 H11 下降、H2 相对误差、H3 连续性和 KL 条件下……”中的 `H11` 应为论文记号 **(H1')**（或 `(H1\textquotesingle)`），不是新的假设名；
- Theorem 5.1 的摘要式压缩还省略了 bounded level set、accumulation point、`φ,β` increasing 及混合条件 (5.1)。若把这句话用于“论文定理”引用，可能过度概括；
- “Theorem 5.2 再给超线性速率”不是无条件结论。v1 还要求由 Theorem 5.1 定义的 `ξ` increasing 且 `ξ(t)/t→0`，并分别需要 eventual `e_k≤r‖x_{k+1}-x_k‖` 或 `e_k≤ℓ d(x_k,Ξ)` 才得到 (5.8)/(5.10) 型率；
- 由 v1 Remark 5.3 读出的显式子线性尾率，若继续保留本库对 `1-α` 的疑似笔误审查，应明确这是 **对 v1 文字的内部公式检查**，而不是对正式 MOR 版的断言。

此外，正式页面摘要虽宣称在严格互补条件下对 Hadamard reparameterized compressed sensing model 有全局收敛和二次局部率，但没有给出 theorem number 或全部假设。该摘要事实不能反向证明 v1 Section 7 的定理编号、条件和正式版措辞完全不变。

## 3. 推荐的引用分层（不改变 canonical claim）

| 说法 | 当前证据允许的身份 | 不应写成 |
| --- | --- | --- |
| 题名、三位作者、DOI、Received/Accepted/Online 日期、Article in Advance、摘要关键词 | 正式 INFORMS 页面 metadata/abstract fact | 正式版的卷页或定理编号 |
| Definition 3.1、Theorem 4.3–4.4、Theorem 5.1–5.2、Remark 5.3 的具体公式、证明、页码 | arXiv:2406.13207v1 paper fact | “MOR 2026 Theorem 5.1”而未注明版本 |
| exact global PPA 自动满足 H1'/H2 的映射 | 本库 PPA transfer / derived result，基于 v1 接口 | LMZ 正式摘要已证明任意 PPA |
| v1 使用 over-parameterized compressed sensing model | arXiv v1 摘要/正文 fact | 正式版仍使用同一模型名称 |
| 正式摘要使用 Hadamard reparameterized compressed sensing model | INFORMS metadata/abstract fact | 正式版正文具体模型公式或定理内容 |
| Theorem 5.1/5.2 的详细适用条件、常数和速率式在正式版的状态 | unknown，直到取得正式全文 | “与 v1 完全相同” |

## 4. 结论

本轮没有发现需要推翻 `target2_kl.md` 核心版本判断的证据。最需要修正的是文献地图中的措辞精度：把 `版本已核` 限定为“正式 metadata/abstract + v1 全文”，把所有 Section 3–5 定理编号明确归属于 `arXiv:2406.13207v1`，并把 Theorem 5.1/5.2 的条件写全或至少注明“摘要式省略”。在取得出版社可搜索全文前，正式 MOR 版的编号、常数、假设和 Remark 5.3 速率式继续记为 **unknown**。

