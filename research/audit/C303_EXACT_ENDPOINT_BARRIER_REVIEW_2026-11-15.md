# C303 exact endpoint barrier: independent review

日期：2026-11-15  
审查对象：research/c303_exact_endpoint_barrier.md

## 裁决

状态保持 **continue validation / partial replacement lemma**。EP1--EP3 的代数是正确的，EP4 是可复用的端点首接触障碍，EP7--EP8 在给定同一局部 lift 与 HJ 场界时可以替代导数型 CS5/TE2。EP6 的平面反例参数也正确，并确实说明 q_k 项和步长门不能从首接触论证中删除。当前没有致命代数错误；但该页仍不能单独闭合 C303，因为同伦存在性、端点位移自洽、动态面边界比较、全局 resolvent coverage 及统一 q_k 递推仍是外部 obligations。

## 1. EP1--EP3 的逐式复核

记 g=grad f, H=Hess f, F=a g-Hg, Y=-g,
beta=h/(1+ah), lambda=h beta。由
d=y-x=beta(v-hF(y)) 以及
wbar=beta^{-1}d-Y(y)=v-hF(y)+g(y)
和
g(y)-g(x)=H(y)d+R(x,y), w=v+g(x),
得到

    wbar=w+R+H(y)(d+h g(y))-ha g(y).

代入 d=beta(-g(y)+wbar)，并使用 h-beta=ah beta，恰有

    (I-beta H(y))(wbar+ha g(y))=w+R.

因此
wbar=ah Y(y)+A_y(w+R), A_y=(I-beta H(y))^{-1},
再由 d=beta(Y+wbar) 和 beta(1+ah)=h 得

    d=hY(y)+beta A_y(w+R),

即 EP1。另一方面

    wplus=d/h+g(y)
         = beta/h (wbar+ha g(y))
         = (1/(1+ah)) A_y(w+R),

即 EP2。若 ||d||<=D h，则

    R = integral_0^1 [H(x+s d)-H(y)]d ds,
    ||R|| <= (L3/2)||d||^2 <= (L3 D^2/2)h^2,

所以 EP3 正确。

这里的 wplus 只有在 C303 的算法定义 vplus=(y-x)/h 下才是下一步 normal error；这条对象对应关系应在正式合并处明确写出。

## 2. EP4 的首接触逻辑

若 s(y)=0、可行侧为 s>0，且 grad s(y) dot Y(y)>=mu(y)>0，由 EP1 对 x=y-d 展开 s(x)：

    s(x)=-h grad s(y) dot Y(y)+O(hq+h^2)
        <= -h[mu(y)-C(q+h)].

因此在同一紧 patch 上，只要 q+h<=mu(y)/(2C)，就不可能有一个 s(x)>0 的前驱端点落在 s(y)=0。该步不需要 y_tau 的导数。

对缩放同伦
y_tau+h_tau beta_tau F(y_tau)=x+beta_tau v,
h_tau=tau h, beta_tau=h_tau/(1+a h_tau),
首接触 tau*>0 可同样使用 EP4，前提是同伦分支存在且在首接触前落在该 patch。EP1 给出的自洽估计是

    u_tau=||y_tau-x||
       <= G h_tau+M h_tau(q+C_R u_tau^2).

在固定紧 patch、q 有界且 h0 足够小时，取 D>G+M q_max+1，由 u_0=0 的连续性和首个违反 u_tau<=D h_tau 的反证，可闭合 u_tau<=D h_tau，随后才可调用 EP3。该论证要求：

* global resolvent coverage/唯一分支，或明确的 continuation 论证；仅知道终点 y_1 存在、或仅知道单点 I-beta H(y_1) 可逆，不足以定义全 tau-path；
* I-beta_tau H(y_tau) 在所有 tau in [0,1] 和 patch 上统一可逆；
* Y,A_y,DH 的常数对整个 pre-contact patch 统一；
* C303 的 q_k bound 与面 margin 在同一停止域中同时成立。

首接触处的 mu(y_tau*) 必须与离散端点的 mu(theta_k) 比较。径向 margin m0 exp(-theta^2+theta) 需要 O(h_k(1+theta_k))->0；角度 margin phi(theta)=theta exp(-theta^2) 需要同样的 lift 位移控制。上述比较是 sharp schedule/共同停止域的输入，EP4 本身不提供。

## 3. EP7--EP8

若 Theta 是同一局部 polar lift，r>=1/2，则 grad Theta 及其 Hessian 在 patch 上有界。用 EP1 展开：

    Theta(y)-Theta(x)
      =h grad Theta(y) dot Y(y)
       +beta grad Theta(y) dot A_y(w+R)+O(h^2)
      =h grad Theta(y) dot Y(y)+O(hq+h^2).

若同一 patch 上
c phi(theta)<=grad Theta dot Y<=C phi(theta),
且 |Theta(y)-Theta(x)|<=C h，则 phi' 在 [1,infinity) 有界，可把 phi(Theta(y)) 换为 phi(Theta(x)) 而只损失 O(h) 乘在前面的 h 上。故 EP8 的双侧估计

    c h phi(Theta(x))-C hq-C h^2
      <= Theta(y)-Theta(x)
      <= C h phi(Theta(x))+C hq+C h^2

成立。正式使用时应明确 grad Theta dot Y=Y_theta/r 的 r^{-1} 归一化、局部 lift 不跨 2pi、以及 HJ cutoff 已在整个闭 pre-contact strip 消失。

## 4. EP6 反例

取 s(z)=z_2、f(z)=-mu z_2，则
g=-mu e_2, H=0, Y=mu e_2, F=-a mu e_2。令
x=delta e_2、v=(mu-q)e_2、w=-q e_2。由 resolvent 方程

    y-lambda a mu e_2=x+beta(mu-q)e_2

得到

    y_2=delta+beta(1+ah)mu-beta q
        =delta+h mu-beta q.

若 q>mu(1+ah)，则 beta q-h mu>0。取
delta=(beta q-h mu)/2
便有 x 严格位于 s>0，而
y_2=-(beta q-h mu)/2<0。

所以 q 项是真实的 outward defect。要把它准确称为 O(h) 缺陷，还应说明面 margin 也在 O(h) 量级（例如 mu=kappa h、q=kappa'(1+ah)h）；若 mu 固定而 h->0，满足条件的 q 不属于 O(h)。在 C303 的角面上 mu=c phi(theta_k)->0，临界 alpha=1/2 时 h_k/phi(theta_k) asymp sqrt(log k)，故 q_k=O(h_k) 可以超过 shrinking margin，EP6 的结论适用。

## 5. 记号与最小修补

1. EP4/EP5 里“径向面 mu=m(theta)”容易和 HJ 管中点 m(theta)=(gamma_1+gamma_2)/2 混淆；应改为 margin(theta)=m0 exp(-theta^2+theta) 或直接写 radial_margin。
2. “I-beta H(y) uniformly invertible”应明确对所有 beta_tau 和 tau-path 点成立，而非只对终点。
3. EP4 目前写“all constants on compact pre-contact patch”; 这应和 C303 的 global F-coverage、normal recursion、cutoff-free identity 作为显式 conjunctive assumptions 关联。
4. EP8 的 O(h^2) 需要 D^2 Theta 有界；r>=1/2 已足够，建议在条件中明写。
5. EP6 的 mu 是局部面 margin，与 HJ 的 mu（gamma_2=1+mu exp(-theta)）同名，建议改名避免跨页歧义。

## 最终裁决

EP1--EP4 可作为 CS5/TE2 的部分替代引理，EP7--EP8 可把双侧角度估计直接归结到端点方程；EP6 是精确、可复用的最小障碍。没有数学上致命的符号错误。整体仍是 **continue validation**，不能升级 major contribution，直到上述 global coverage、同伦量词、统一停止域和 shrinking-margin 比较全部写成 C303 的共同假设或独立证明。
