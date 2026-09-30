# Codex 独立证伪与优先权审计任务

请把本文件、`research_note.md`、`verify_research.py` 和原论文完整 TeX 同时交给 Codex。不要先接受证明正确；请优先寻找反例、遗漏假设和错误的最优性量词。

## 交付要求

请返回一份审计报告，按「致命错误／可修补漏洞／已独立复核／优先权对应／仍未解决」分类。每项问题应给出精确公式或最小反例。复述稿件、笼统赞同或仅给出随机测试不能算完成。

## 任务 A：两个显式算子的完整图验证

1. 独立证明 `research_note.md` (2.1) 与 (4.1) 的完整 resolvent，不能只从选中的分支验证正向 graph identity。尤其检查负输入、零输入、负切向坐标、cap 切换点及逆函数满射性。
2. 检查闭图、半代数、两值性和零集是否确如所述。
3. 独立验证所有跨分支 all-pairs RL，检查常数 $2\sqrt2+\frac32\sqrt R$ 和尖锐指数。不要把同分支估计或相对解集的点态估计当成 all-pairs 证明。
4. 检查 residual EB 使用的是整个多值算子的最小范数，而非选中残差；检查严格兼容条件和完整局部覆盖。
5. 解释几何例子的实际距离因子 $q=1/4$ 与保守 RLEB 证书极限 $\kappa_*=1/2$ 的区别，检查全文有没有混用。

## 任务 B：一般模传递定理与上下界

1. 重新证明几何尾界加 $\gamma$-Hölder 单步映射给出的 $(\log\log(1/\delta)/\log(1/\delta))^\beta$ 界；检查局部 Hölder 的尺度限制能否逐步闭合，是否偷偷用了全局 Hölder。
2. 从原论文的局部化预算严格推出一个共同初值邻域上的统一尾界。检查是否缺少共同吸引域假设。
3. 独立分析首次饱和时刻 $N$，验证 $N=(\log t-\log\log t)/\log(1/\gamma)+O(1)$。特别检查 $N$ 和 $N-1$ 的不等式方向与常数是否对 $\varepsilon$ 一致。
4. 检查任意 $\gamma,q\in(0,1)$ 的闭图二值实现是否确能同时严格兼容和达到相应指数；分清「固定实际 $q$」的最优性与「固定保守证书 $\kappa$」的最优性。
5. 检查超几何尾界的指数 $\alpha=\log\nu/\log(\nu/\gamma)$；独立核对反例的 overshoot 项，不能套用几何情形的 $p_N=O(r_N^\gamma)$。

## 任务 C：点收敛阶数与结构推论

1. 对二次模型独立证明的是点误差 $e_k=\|x_k-x_\infty\|$ 的 Q-二次，而非仅到解集距离的二次收敛。核对极限比值：$p_0\le0$ 时为 $1$，$p_0>0$ 时为 $1/\sqrt2$。
2. 区分固定解点处的 Hölder calmness 和完整邻域上两点 Hölder 连续性；寻找任何混淆二者的说法。
3. 用一元半代数增长二分严格检查极限映射非半代数推论。
4. 检查最后的切向充分条件只覆盖三角结构，不被扩张成原文所有 signed-Schur 图块。新反例不主张满足附录的强切向反演假设。

## 任务 D：定理级文献优先权核查

请独立检索并阅读原始论文，重点不是泛泛找到收敛文献，而是寻找相同定量结论。

关键词族：limit retraction；asymptotic phase；regularity of the limit map；uniform limits of iterates；Hölder iteration logarithmic modulus；semialgebraic iteration nonsemialgebraic limit；superlinear convergence unstable solution selection。

请分别核查：

- 抽象的统一尾界—极限模传递是否已有相同量级，尤其分子 $\log\log$ 和指数 $\beta$。
- 几何／超几何收敛与低于所有 Hölder 阶的初值稳定性分离是否已有先例。
- 闭图、半代数、二值、完整 proximal 解、严格 RLEB 兼容同时成立的构造是否已有。
- Q-二次点收敛与非 Hölder、非半代数算法极限选择同时出现是否已有。

已核对的起点文献：Luke–Tam DOI 10.1287/moor.2025.0863；Luke–Thao–Tam DOI 10.1287/moor.2017.0898 和 10.1007/s10013-018-0279-x；Li–Mordukhovich–Zhu DOI 10.1287/moor.2024.0570；Lee–Pham DOI 10.1137/20M1331901。

每个可能先例请给出准确题名、作者、DOI/arXiv、定理号、假设对应、已覆盖部分和未覆盖部分。「搜索没结果」不能作为首创证明。若抽象定理已有，应清楚拆分可保留的新内容，不要把整个方向一概判定为已知或全新。
