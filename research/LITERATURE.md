# 一手文献事实与本项目的定理导入

本页只把已经读到原文的**确切语句**与本项目的解释分开记录。文献事实不证明项目稿件中的其他前提，也不判定新颖性。后续新增文献时给版本、页码、原定理假设和逐项对象映射。

<a id="lit-grn-2002"></a>
## LIT-GRN-2002 · Górniewicz–Rozpłoch-Nowakowska 的 morphism Lefschetz 定理

**Paper fact.** L. Górniewicz and D. Rozpłoch-Nowakowska, “The Lefschetz Fixed Point Theory for Morphisms in Topological Vector Spaces,” *Topological Methods in Nonlinear Analysis* **20** (2002), 315–333, [期刊原版 PDF](https://www.tmna.ncu.pl/static/files/v20n2-07.pdf), DOI [10.12775/TMNA.2002.039](https://doi.org/10.12775/TMNA.2002.039). 该文印刷页 327 的 Theorem 6.2：若 \(X\) 是 Klee-admissible 拓扑向量空间 \(E\) 中某个开集的 retract，且 \(\varphi\in M(X,X)\) 属于 \(CAC(X)\)，则其 Lefschetz 数有定义；若数不为零，\(\varphi\) 有固定点。印刷页 315–318 的 Definition 1.1、2.1–2.4 把 morphism 表示为 \(X\xleftarrow{p}\Gamma\xrightarrow{q}X\)：\(p\) 是 perfect surjection 且每个纤维在**有理 Čech homology with compact carriers** 下 acyclic，\(q\) 连续。印刷页 320–322 的 Definition 2.6、3.1 与紧类包含关系 \(K(X)\subset CAC(X)\) 表明紧 morphism 足以满足 Theorem 6.2 的动力条件。此定理本身不要求 morphism 的输出纤维 acyclic。

**Interpretation / C05 import check (2026-10-01).** 对 [9/25 候选稿 §8, Theorem 8.1](../history/sources/次单调论文研究/最新成果/2026_09_25_siopt_combined_candidate.pdf)，取 \(X=A\subset\mathbb R^n\)，\(\Gamma=\{(p,y):p\in A,y\in T(p)\}\)，\(p=\pi(p,y)\)，\(q=e_h(p,y)=y+\lambda h(y)\)。逐项门如下：

| 引文前提 | 稿件中对应的**额外假设或推导** |
| --- | --- |
| \(E\) Klee-admissible，\(X\) 为开集 retract | \(E=\mathbb R^n\)；\(A\) 是紧有限多面体，故是 Euclidean neighborhood retract。 |
| \(p\) Vietoris，\(q\) 连续 | \(A\) 紧、\(T\) 在邻域 usc、非空紧值，给紧图与 perfect surjection；\(T(p)\) 的有理 Čech acyclicity 给纤维条件。\(h\) 连续给 \(e_h\) 连续。注意原稿用 Čech **cohomology** 描述 acyclicity，需采用其对紧度量纤维的有理 homology 等价。 |
| \(q(\Gamma)\subset A\)，紧 morphism \(\subset CAC(A)\) | 原稿 (8.4) 的完整 shell/collar 和 (8.7) 保证每个 \(y\in T(p)\) 离 \(A^c\) 至少 \(m-\alpha\)；\(\sup_A\|h\|<(m-\alpha)/\lambda\) 故 \(e_h(\Gamma)\subset\operatorname{int}A\)。紧 \(\Gamma\) 的连续像紧，按原文 \(K(A)\subset CAC(A)\)。 |
| 非零 Lefschetz 数 | 原稿要求 \(b^*:H^j(B;\mathbb Q)\to H^j(A;\mathbb Q)\) 全阶满射，并用 \([p,y]\subset B\) 得 \(e^*=\pi^*\)；\(e_{th}\) 全在 \(A\) 中，同伦不改诱导映射。有限多面体上的有理同调与上同调维数有限，因此 \(\Lambda=\chi(A)\ne0\)。 |

**审查结论与边界。** 原引文确实适用于上述**紧 span**，不需要另证明非线性像 \(e_h(T(p))\) acyclic。这里关闭的是“[6, Theorem 6.2] 是否有 CAC/图/回缩适用门”这一个导入问题。整条 C05 仍是候选：有限观测不能证明整窗 (8.1)–(8.2)、\(T\) 的存在、usc 与 acyclicity，也没有逐行 referee 其余数值包络或核外部先行性。若换成非紧 \(A\)、放弃全部纤维 acyclicity、或只凭有限样本声称整窗条件，就不再是同一导入。稿件的 Čech cohomology/homology 等价是单独的标准拓扑事实，本次只在紧度量纤维范围使用，没有把它扩张到任意空间。
