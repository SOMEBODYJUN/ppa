# 振荡剪切：粗全对指数与真实轨道阶分离

<a id="os-object"></a>
## OS-OBJECT · 完整三角图和局部零集

固定 \(q>1\)、\(0<\gamma<1\)、\(\beta=q/\gamma-1>0\)，令 \(P_q(t)=\operatorname{sign}(t)|t|^q\)。置
\[
h(0)=0,\qquad h(x)=|x|^q\sin(|x|^{-\beta})\ (x\ne0),
\quad J(x,y)=(P_qx,P_qy+h(x)),\quad F=J^{-1}-I,
\]
生成步长为 \(\lambda=1\)。\(J\) 是全域三角同胚：先由第一坐标反解 \(x\)，再由 \(P_qy\) 反解 \(y\)，故 \(F\) 为完整单值关系，\(J=J_F\)。

\(Jz=z\) 的第一坐标要求 \(x=0\) 或 \(|x|=1\)；若 \(x=0\)，第二坐标要求 \(y=0\) 或 \(|y|=1\)。因此 \(S=\operatorname{zer}F=\operatorname{Fix}J\) 在 \(B_{1/2}(0)\) 内恰为 \(\{0\}\)，所有其他零点离原点至少 1。对充分小 \(u\)，真实目标距离 \(d(u,S)=\|u\|\)；不能把全局零集直接写成 \(\{0\}\)。

<a id="os-scaling"></a>
## C43-v1 / OS-SCALING · 双边 \(q\)-阶轨道与真实残差

对**每个** \(z=(x,y)\in\mathbb R^2\)，
\[
2^{-1-q/2}\|z\|^q\le\|Jz\|\le\sqrt5\,\|z\|^q. \tag{1}
\]
故任取 \(0<\rho<1/2\) 满足 \(\sqrt5\,\rho^{q-1}<1\)，每个 \(z_0\in B_\rho(0)\) 的轨道留在此球并趋于零；非零轨道的距离满足同一双边 \(q\)-阶界。对完整原关系 \(F\)，在零点邻域有真残差幂误差界
\[
d(u,S)\le K r_F(u)^q
\]
（某个有限 \(K\)），且指数 \(q\) 不可提高。

**证明。** 记 \(a=|x|^q,b=|y|^q\)。\(|h(x)|\le a\)，故第一输出绝对值是 \(a\)，第二至少为 \((b-a)_+\)。若 \(b\le2a\)，输出范数至少 \(a\ge\max(a,b)/2\)；若 \(b>2a\)，第二输出至少 \(b-a>b/2\)。又 \(\max(a,b)\ge2^{-q/2}\|z\|^q\)，给下界。上界由 \(a\le\|z\|^q\)、\(|P_qy+h(x)|\le b+a\le2\|z\|^q\) 得出。

任意 \(u=Jz\) 只有一个原图残差 \(w=z-u=F(u)\)。由 (1)，\(\|w\|/\|z\|\to1\) 当 \(z\to0\)，而 \(u\to0\) 且局部目标距离为 \(\|u\|\)。于是 (1) 给 \(d(u,S)=\Theta(r_F(u)^q)\) 的统一邻域双边量级。取 \(x_n=(\pi n)^{-1/\beta},z_n=(x_n,0)\)，有 \(h(x_n)=0\)、\(u_n=(x_n^q,0)\)、\(r_F(u_n)=x_n-x_n^q\sim x_n\)，排除每个 \(p>q\) 的 \(d(u,S)\le K r_F(u)^p\)。不变球与轨道收敛由上界迭代直接得出。证毕。

<a id="os-reflection"></a>
## OS-REFLECTION · 局部全对指数恰为 \(\gamma\)

反射 \(C=2J-I\) 在任一有界输入窗口是 \(\gamma\)-Hölder；在含原点的任意二维邻域，其最大全对 Hölder 指数恰为 \(\gamma\)。下面的估计只证明指数，不声称最优有限常数。

**上界证明。** 对 \(x,y\) 近零置 \(r=\max(|x|,|y|)\)、\(\delta=|x-y|\)。若 \(\delta\ge r/2\)，
\[
|h(x)-h(y)|\le2r^q\le C\delta^q\le C\delta^\gamma
\]
（限制 \(\delta\le1\)）。若 \(\delta<r/2\)，两点同号且模可比。再分 \(\delta\ge r^{\beta+1}\) 与 \(\delta<r^{\beta+1}\)：前者由振幅界得 \(2r^q\le2\delta^{q/(\beta+1)}=2\delta^\gamma\)；后者用
\[
|h'(v)|\le C r^{q-1}+C r^{q-\beta-1}
\quad (r/2\le|v|\le r)
\]
得 \(|h(x)-h(y)|\le C r^{q-\beta-1}\delta\le C\delta^\gamma\)，因为 \(q=\gamma(\beta+1)\)。其余 \(P_q\) 与恒等坐标在有界域上 Lipschitz，可由有界直径降为 \(\gamma\)-Hölder。

**锐性证明。** 取 \(s_n=2\pi n+\pi/2\)、\(t_n=s_n+\pi\)、\(x_n=s_n^{-1/\beta}\)、\(y_n=t_n^{-1/\beta}\)。均为正且
\[
\delta_n=x_n-y_n\sim(\pi/\beta)s_n^{-1/\beta-1},\qquad
h(x_n)-h(y_n)\sim2s_n^{-q/\beta}.
\]
反射在点 \((x_n,0),(y_n,0)\) 的第二坐标差恰为 \(2[h(x_n)-h(y_n)]\)；第一坐标差是 \(O(\delta_n)\)，除以 \(\delta_n^\gamma\) 后趋零。故
\[
\frac{\|C(x_n,0)-C(y_n,0)\|}{\delta_n^\gamma}
\longrightarrow4(\beta/\pi)^\gamma>0.
\]
任何更高指数的商发散。证毕。

实际轨道的双边阶 \(q\) 严格高于 \(\gamma q\)，因为 \(\gamma<1\)。这里“阶 \(q\)”指对所有足够小非零状态的**双边幂量级**；振荡相位未证明归一化比值收敛，不写成精确 Q 因子。全对指数粗糙并不强迫轨道只达到由它产生的保守上界。

<a id="os-source"></a>
## 来源、状态与下一义务

从 [9/01 RL_foundations §9.3 / GX-072](../../../history/sources/次单调论文研究/RL_foundations.md) 重写映射、双边常数、真实残差、两尺度证明和锐相位序列。状态 derived-checked 限于本页计算；不对该构造的文献新颖性下结论。与 [GX-071](power_shear.md) 是两个不同的算子，前者保守指数、后者可达性，不能只按共享 \(q,\gamma\) 合并对象。GX-073 的定义域逃逸已有独立 [C44 对象卡](domain_escape.md#de-object)；其自然输入域和全纤维残差不能由本页转授。
