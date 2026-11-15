# 交叉审查：三个新候选

审查范围：

1. `repo/research/topics/path_dynamics/second_order_open_basin_candidate.md`；
2. `repo/research/discovery_a_gram_37.md` 与规范文件 `repo/research/canonical/gram_regression_gppa.md`；
3. `repo/research/candidates/monotone_antiwinding_gate.md`（内容与 `discovery_b.md` 相同）。

以下裁决均区分“有价值的候选”和“已达主要贡献标准”。三个候选当前都不能升级为后者。

## 1. 二阶 HJ 开盆域候选：首次离开 bootstrap

### 1.1 需要先固定的局部估计

取 HJ 螺旋管
\[
D=\{(r,\theta):\theta>\theta_*,\ b_1(\theta)<r<b_2(\theta)\},
\quad b_i(\theta)=1+c_i e^{-\theta},
\]
并令 (X=-\nabla f) 采用 HJ 的负梯度号。候选要从显式公式另证以下统一估计：存在 (A_0,A_1,A_2>0)，使所有 (	heta\ge\theta_*)、(r\in[b_1,b_2]) 有
\[
A_0\theta e^{-\theta^2}\le X_\theta(r,\theta)
 \le A_1\theta e^{-\theta^2},
\tag{HJ-1}
\]
且在两条边界，以内法向导数写成
\[
\nabla s_i\cdot X\ge A_2e^{-\theta^2+\theta},
\quad s_1=r-b_1(\theta),quad s_2=b_2(\theta)-r.
\tag{HJ-2}
\]
这里的常数必须对整个 (a)-区间统一。HJ 的法向公式只直接给边界符号；(HJ-1) 还需利用 (F\) 在 ([-\beta,\beta]) 上的正下界，控制 (hF'\partial_\theta a) 这一 (O(e^{-\theta^2})) 项，并让 (2\theta hF) 主导它。若将 HJ 文本中的 (X=\nabla f) 与公式负号混用，整个方向会翻转；必须先统一成 (X=-\nabla f) 或把 (f\) 整体换号。

由 (f\in C^\infty(\mathbb R^2)) 和物理闭管的紧性，
\[
\kappa=\sup_{\overline D}\lambda_{\max}(\nabla^2 f)<\infty.
\]
取 \(\alpha>\kappa\)、\(\delta=\alpha-\kappa\)。对
\[
\chi=\alpha f-\tfrac12|\nabla f|^2,
\qquad w=v+\nabla f(x),
\]
有精确系统
\[
x'=X(x)+w,
\qquad w'=(\nabla^2 f(x)-\alpha I)w,
\tag{HJ-3}
\]
从而只要轨道在 (D) 内，
\[
|w(t)|\le |w(0)|e^{-\delta t}.
\tag{HJ-4}
\]

### 1.2 选有限初始角带，得到真正的相空间开集

不能把所有 \(\theta>\theta_*\) 都放进同一个 (\varepsilon)-扰动管：(X_\theta\to0)，初始角速度没有统一正下界。选
\[
\theta_*<\Theta_0<\Theta_1<\infty,
\]
以及物理闭子带
\[
D_0=\{\Theta_0<\theta<\Theta_1,
 b_1(\theta)+\rho_0<r<b_2(\theta)-\rho_0\}
\Subset D,
\]
其中 (ho_0>0) 足够小。令 (w=v+\nabla f(x))，并取
\[
\mathcal U=\{(x,v):x\in D_0, |w|<\varepsilon\}.
\tag{HJ-5}
\]
这是四维相空间中的非空开集。后面的 \(\varepsilon\) 只依赖此有限初始带和固定常数。

### 1.3 先证角度不掉出入口，再证角度上界

设 \(\tau\) 是离开 (D) 或角坐标失效的首次时刻。由 (HJ-4)，记
\[
W(t)=\int_0^t\varepsilon e^{-\delta s}\,ds
\le w_*:=\varepsilon/\delta.
\]
因为 \(\theta'\ge-|w|\)，对 (t<\tau) 有
\[
\theta(t)\ge\theta(0)-W(t)\ge\Theta_0-w_*.
\tag{HJ-6}
\]
先取 (w_*<\Theta_0/4)，则始终 \(\theta\ge 3\Theta_0/4)。再增大 \(\Theta_0) 使其大于 1，令
\[
u(t)=\theta(t)-W(t)\ge \Theta_0/2.
\]
由 (HJ-1) 及 (s\mapsto se^{-s^2}) 在 ([1,\infty)) 上递减，
\[
u'(t)=\theta'(t)-W'(t)
\le A_1\theta e^{-\theta^2}
\le A_1u e^{-u^2}.
\]
写 (Y=u^2)，便有 (Y'\le2A_1Y e^{-Y})。于是
\[
\frac{d}{dt}e^{Y/2}
\le A_1Ye^{-Y/2}\le 2A_1/e,
\]
从而在整个首次离开区间
\[
e^{u(t)^2/2}\le e^{u(0)^2/2}+2A_1t/e.
\]
因此存在 (C_*,p<\infty)（例如增大常数后可取 (p=4)）使
\[
\theta(t)^2\le C_*+p\log(1+t).
\tag{HJ-7}
\]
这一步不需要预先假设管道不变性；只在首次离开区间内使用 (HJ-1)–(HJ-4)，因此是合法的 bootstrap 上界。

### 1.4 用上界关掉 shrinking barrier

由 (HJ-2) 和 (HJ-7)，对 (t<\tau)，
\[
m(\theta(t)):=A_2e^{-\theta(t)^2+\theta(t)}
\ge c_*(1+t)^{-p}
\tag{HJ-8}
\]
（减小 (c_*) 吸收有限初始时段）。而 (s_i) 的梯度在闭管上有统一界 (L_s)，所以沿边界接触前
\[
s_i'\ge m(\theta)-L_s\varepsilon e^{-\delta t}.
\tag{HJ-9}
\]
取
\[
M_p=\sup_{t\ge0}e^{-\delta t}(1+t)^p<\infty,
\qquad
\varepsilon\le\frac{c_*}{2L_sM_p},
\tag{HJ-10}
\]
并同时满足 (\varepsilon/\delta<\Theta_0/4) 及初始带的余量条件。于是边界接触时 (s_i'\ge c_*(1+t)^{-p}/2>0)，与从 (s_i>0) 的首次接触必须满足 (s_i'\le0) 矛盾。故不存在有限首次离开，轨道永远在 (D) 内。

注意 (HJ-10) 的选择顺序：先在假设首次离开的区间推 (HJ-7)，再用它估计 (m)，最后选 (arepsilon)；没有循环依赖。

### 1.5 证明角度真正趋于无穷

仅由 (HJ-8) 的粗下界 (c(1+t)^{-p})（(p>1)）不能直接积分推出发散。应保留 (HJ-1) 的角度因子。由 (HJ-7) 及 (HJ-6)，存在 (c_1>0,p_1<\infty) 使
\[
\theta(t)e^{-\theta(t)^2}\ge c_1(1+t)^{-p_1}.
\]
指数衰减最终小于此多项式下界；故存在 (T) 使 (t\ge T) 时
\[
\varepsilon e^{-\delta t}
\le \frac{A_0}{2}\theta(t)e^{-\theta(t)^2},
\]
从而
\[
\theta'(t)\ge \frac{A_0}{2}\theta(t)e^{-\theta(t)^2}>0.
\tag{HJ-11}
\]
若 \(\theta\) 在 (t\ge T) 有有限上界，右端在该紧区间有正下界，立即矛盾；所以 \(\theta(t)\to+\infty)。更精确地，
\[
\frac d{dt}e^{\theta(t)^2}
 =2\theta e^{\theta^2}\theta'
\ge A_0,
\]
故 (e^{\theta(t)^2}\ge e^{\theta(T)^2}+A_0(t-T))。

于是 (b_i(\theta(t))\to1)，而 (b_1<r<b_2)，所以 (r(t)\to1)。角度连续提升且趋于 (+\infty)，给出位置轨道的 omega-limit 正好是 (S^1)。

### 1.6 二阶候选裁决

上面的 bootstrap 说明候选的核心机制在补充 (HJ-1)–(HJ-2) 后是可闭合的，并未发现一个立即的动力学反例。但候选文件尚未给出这些统一常数、首次离开论证、有限初始角带或 PPA 离散桥，因此当前只能**继续验证**。最低改变证据是：一份从 HJ 显式 (F) 逐项导出 (HJ-1)–(HJ-2) 并证明 (HJ-3)–(HJ-11) 的正式引理；随后仍需说明与 PPA/GPPA 的精确离散联系。它尚未达到主要贡献标准。

## 2. Gram (3/7) 候选：横向弧攻击

### 2.1 已确实成立的锐性见证

对 (Z_t=[tc,0])、(Z_t'=[tc,\zeta t^7c])，输出缩放 \(\alpha=t^3U,\beta=t^3W\) 给出 (A4)–(A5)，并且输出差 \(\asymp t^3\)、输入差 \(\asymp t^7\)。故任何共同 Hölder 指数 (q>3/7) 均不可能。这一步是可靠的必要上界。

### 2.2 一个容易误判的横向弧

取基点 (a=t^A e_1,b=t^B e_2)（(B>A)），再把第一列加一条横向分量 
\(\Delta a=\varepsilon t^{A+E}e_2\)。此时
\[
\Delta k_e^{(1)}\asymp t^{A+B+E},
\qquad \|\Delta Z\|\asymp t^{A+E}.
\]
在输出第二列尚由第一项的线性正则化控制时，\(|\Delta\beta|\asymp t^{A+B+E-2B}=t^{A-B+E})，而该线性区的自洽条件为 (E>2(B-A))。在端点 (E=2(B-A))，输出/输入指数为 (B/(2B-A)\ge1/2)；在线性区内部比值更大。

在相反的立方根区，\(|\Delta\beta|\asymp t^{(A+B+E)/3})，指数
\[
\frac{A+B+E}{3(A+E)}
\]
不小于 (1/3)，且在可疑的临界区 (E\approx2(B-A)) 不低于 (1/2)。因此这条横向弧没有给出小于 (3/7) 的反例；它也说明“横向项不坏”需要实际按区间分解证明，不能从 GR4 的非负项一句话跳过。

### 2.3 真正尚未排除的横向问题

需要把上述尺度计算推广到：

* rank-two 的方向扰动（同时改变 (a\) 与 (b\) 的夹角）；
* rank-one 附近但 ​\(\alpha,\beta\) 具有不同主尺度的耦合；
* 输入差和输出差不沿单一幂次弧的半代数分支。

规范单调性只给
\[
c\|Y-Y'\|^4+\lambda\|\alpha-\alpha'\|^2
\le C_M\|Z-Z'\|\,\|Y-Y'\|,
\]
它仍仅推出 (1/3) 指数，不能自动补出 (7/3) 的差分下界。一个可执行的最小证明路线是：在非退化 stratum 上用 Lipschitz IFT；在 rank-one stratum 做正交约化并建立上述两区间；在原点用多项式半代数弧分类（或直接构造 Łojasiewicz 指数）。若存在一条横向弧使 (\|\Delta Z\|=o(\|\Delta Y\|^{7/3}))，候选即淘汰。

当前裁决：**继续验证**。它有真实的精确 sharpness 见证，但 (3/7) 上界还没有证明，也没有外部先行性核对，因而不能称主要贡献。

## 3. 单调 anti-winding gate：范围攻击

### 3.1 B1 在固定 radial twist 上正确

若对每个 (x=(1+t)p) 选定
\[
Jx=(1+qt)R_{\theta(t)}p,
\qquad v=(x-Jx)/\lambda,
\]
且所有这些图点属于同一单调关系，则同半径 (p,p') 的单调性给
\[
0\le\langle Jx-Jx',v-v'\rangle
 =\lambda^{-1}s(rs\cos\theta-s^2)\|p-p'\|^2,
\]
其中 (r=1+t,s=1+qt)，故
\[
\cos\theta(t)\ge s/r.
\]
因而 \(|\theta(t)|\le C\sqrt t\)，在 (t_k=q^kt_0) 上角度总和有限，固定 radial twist 的每条非零轨道收敛到一个圆点。这部分是可直接升格成一个有限长度定理，前提是把选择核/完整图的身份写清。

### 3.2 不能扩大到一般多值图或任意流形

B1 比较的是同半径、同一共同旋转角的两条**已选输出**。它没有给出：

* 一般多值预解式中所有输出分支的共同角参数；
* (S^1) 换成曲率非零 (C^2) 流形后，最近点纤维/法向框架的相同半径关系；
* 全 Minty coverage、最大单调性、真残差 EB 或跨半径的切向位移控制。

因此“单调 PPA 一般禁止非 Dini 绕行”仍是开放命题。把同半径计算直接写成一般流形切向定理会改变量词和对象。

### 3.3 非 Dini 逻辑的精确边界

B1 排除的是存在常数 (C) 使整个小窗内 (ω(t)\le C\sqrt t)。非 Dini 条件确实不能与这种**全窗**约束同时成立，因为该约束使 \(\int_0^\varepsilon\omega(t)dt/t\) 有限；但非 Dini 不必推出 \(\omega(t)/\sqrt t\to\infty\)。标准 \(1/\log(e/t)\) 例满足趋无穷，可用于直观攻击 C287 的具体剖面；一般结论应改成“不存在统一 (C\sqrt t) 上界”，而不能使用极限趋无穷这一更强句子。

当前裁决：**继续验证**，作为 C287 特定旋转族的结构性障碍；它目前不是主要贡献。最小改变证据是独立写出完整 radial theorem（包括所有 (t)-层、预解选支和有限长度），或构造一个满足同样 PPA 量词却避开共同角假设的单调反例。

## 总裁决

三个候选都保留为有价值的研究方向，但均有未闭的单一关键证明义务：二阶候选是统一 HJ 内部/边界估计与首次离开 bootstrap；Gram 候选是横向 rank-stratum 的 (3/7) 上界；anti-winding 候选是从共同角 radial 图推广或明确限制到可发表的精确子类。当前没有一个能独立支撑“数学四大主要贡献”裁决，也没有一个因已知反例立即淘汰。
