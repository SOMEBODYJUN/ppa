# SS1 §7 数值证据的来源与复跑边界

本记录只核 SS1 修订包 `solution_selection_revised_v1_delivery.zip!/research_note.md` 第 728–744 行的**有限数值观察**。该包只含文稿、审计及构建文件，不含所称的 `verify_research.py` 或结果表。可得的程序和三个结果文件位于另一个原件 `history/sources/次单调论文研究/正式后的研究/RLEB_solution_selection_2026-09-18.zip!/RLEB_solution_selection_2026-09-18/`。下表核的是可得程序与可得结果之间的关系，不把修订文稿的全部数值叙述认作由其自身附件提供。

| 对象 | 原件 SHA-256 | 本次复跑 |
| --- | --- | --- |
| `verify_research.py` | `3344b5059c62af5672c37e2d3136cb3e1a33dd326e013d5422b4b2e6227ef05c` | 原样提取到临时目录 |
| `results/verification_results.json` | `b9ed4af5035432b7dbd0edf49326b7ab5421b89757f6eb214ccfd76f618c9590` | 逐字节相同 |
| `results/geometric_phase.csv` | `d005a7c53de7993f0aafe705752999b5156cd247406e063c2466d25e5dab5735` | 逐字节相同 |
| `results/quadratic_phase.csv` | `ffc1be7eff83c774d7367c6419b854d65dff6281b185902c6af2e44b0cff8df9` | 逐字节相同 |

复跑环境为 Python 3.12.14、NumPy 2.3.5；从仓库根在临时目录原样提取脚本后执行 `python3 verify_research.py --out results`。程序内部固定 `seed=20260918`、每模型 `sample_count=100000`。JSON 报告两模型图身份最大绝对误差均为 `1.9081958235744878e-17`、双支逆向误差均为 `1.5265566588595902e-16`，抽样 EB 违反量为 0；几何模型固定 `R=0.01`、`L_R=2.97842712474619`、证书 `κ=0.5922945976483185`、实际距离因子 `0.25`。这些量与本库 C137 的 GC-3–GC-8 对象相符。旧脚本的 `quadratic` 分支及旧结果需保持它自己的模型身份，不能把它的残差或锐性移给 C137。

程序以双精度浮点运行；`geometric_phase` 在切换前用对数坐标，允许表示 `exp(-10^6)` 这类不可直接存成正常浮点的扰动。输出哈希相同仅说明在本环境可复跑这份旧程序的有限记录；这不是区间证明、全对 RL 的一般量词证明、文献优先权审查或修订包与旧程序之间的逐行版本同一性。数学结论仍需 [C137/C138 规范证明](../canonical/selection_geometric_cap.md#gc-object) 各自承担。下一步若引用修订 §7 中超出这三个结果文件的数值断言，应逐项标明程序版本和精确结果字段。
