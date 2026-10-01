# 斜等距加紧正对角：锐逆像、近端收缩与非 rectangularity

<a id="scd-object"></a>
## 完整对象

在实 Hilbert 空间 \(H=\ell^2(\mathbb N)\) 上令
\[
D(x_n)=(x_n/n),\qquad
B(x_1,x_2,x_3,x_4,\ldots)=(-x_2,x_1,-x_4,x_3,\ldots),
\qquad F=D+B.
\tag{SD1}
\]
这是定义在**全部** \(H\) 上的有界单值线性完整关系，不是只取
有限块的近似；\(B^*=-B,B^*B=I\)。第 \(k\) 块设
\(a=(2k-1)^{-1},b=(2k)^{-1}\)，则 \(a-b=ab\) 且
\[
F_k=\begin{pmatrix}a&-1\\1&b\end{pmatrix},\quad
F_k^{-1}=\frac1{1+ab}\begin{pmatrix}b&1\\-1&a\end{pmatrix}.
\tag{SD2}
\]
来源线索是 9/01 ZIP `work/c_gx053_065.md` §2 的 GX-059；精确
成员见[逐源去向](../../audit/UNIT_DISPOSITIONS.tsv)。本卡直接重算
非 rectangularity，不导入来源的 BWY 等价定理；外部先行性未核。

<a id="scd-inverse"></a>
## C102-v1：完整逆像锐界与非 rectangularity 并存

由 \(a-b=ab\) 可直接乘出
\[
F_k^*F_k=I+\begin{pmatrix}a\\-b\end{pmatrix}(a,-b),
\quad 1+a^2+b^2=(1+ab)^2.
\tag{SD3}
\]
每块奇异值恰为 \(1,1+ab\)。统一下界和 (SD2) 的统一有界
逆矩阵使 \(F:H\to H\) 是双射，\(\|F^{-1}\|=1\)、
\(\|F\|=3/2\)、\(S=F^{-1}(0)=\{0\}\)。因此对**全部**
\(x,y\in H\)，完整逆纤维 \(F^{-1}(y)=\{F^{-1}y\}\)，且
\[
d(x,F^{-1}(y))=\|F^{-1}(Fx-y)\|\le\|Fx-y\|.
\tag{SD4}
\]
系数 1 全局及每个参考图点的局部下确界都锐：每个块中
\((b,a)\) 是 (SD3) 的奇异值 1 方向，任意缩放保取等。
这是原算子的 MR/MSR/SMR/SMSR 线性距离界，不是近端步残差界。

对 \(h\ne0\)，\(\langle h,Fh\rangle=\sum_nh_n^2/n>0\)，故
严格单调，并由零配对只可 \(h=0\) 直接得 paramonotonicity。
若 \((x,v)\) 与全图单调相关，对任意 \(h\) 及任意实 \(t\)，
把图点取为 \((x+th,Fx+tFh)\) 得
\(-t\langle h,v-Fx\rangle+t^2\langle h,Fh\rangle\ge0\)；
令 \(t\) 从两侧趋零得 \(v=Fx\)，所以 \(F\) 极大单调。
但强单调模为零（\(h=e_n,n\to\infty\)）；正 cocoercivity
模也为零，因为对 \(h=e_{2k}\)，
\(\langle h,Fh\rangle/\|Fh\|^2=b/(1+b^2)\to0\)。

为直接检验 rectangularity，采用全域单调关系的精确条件
\(\inf_z\langle x-z,v-Fz\rangle> -\infty\) 对所有
\(x\in\operatorname{dom}F,v\in\operatorname{ran}F\)。取
\(x=0\)、\(v=(1/n)_n\in H=\operatorname{ran}F\)，
以及有限支撑 \(z^{(N)}_n=1/2\) 当 \(n\le N\)，否则为零。
利用 \(\langle z,Bz\rangle=0\)，恰有
\[
\langle-z^{(N)},v-Fz^{(N)}\rangle
=-\frac14\sum_{n=1}^N\frac1n\longrightarrow-\infty.
\tag{SD5}
\]
故此完整、满值域、极大单调且锐逆像线性的图仍**不是
rectangular**。这里没有把有限维截断的行为当无限维证明。

<a id="scd-prox"></a>
## C103-v1：全域近端严格收缩而反射不严格收缩

每个固定 \(\lambda>0\)，块矩阵 \(I+\lambda F_k\) 的行列式
\(\delta_k=(1+\lambda a)(1+\lambda b)+\lambda^2>0\)，
其逆块范数统一有界。因此完整 \(J_{\lambda F}=(I+\lambda F)^{-1}\)
在**全部** \(H\) 单值且有覆盖。对所有 \(x\in H\)，
\[
\|(I+\lambda F)x\|^2
=\|x\|^2+2\lambda\langle x,Dx\rangle+\lambda^2\|Fx\|^2
\ge(1+\lambda^2)\|x\|^2.
\tag{SD6}
\]
高编号块趋向斜等距 \(B_k\)，故下界可被单位向量序列逼近；
从而 \(\|J_{\lambda F}\|=(1+\lambda^2)^{-1/2}<1\)。
同理对每个固定整数 \(m\ge0\)，由高块收敛到
\((I+\lambda B_k)^{-m}\) 得
\(\|J_{\lambda F}^{m}\|=(1+\lambda^2)^{-m/2}\)；
每条完整近端路径全域合法并有几何有限长度。

反射 \(R_{\lambda F}=(I-\lambda F)(I+\lambda F)^{-1}\) 满足
\[
\|(I+\lambda F)x\|^2-\|(I-\lambda F)x\|^2
=4\lambda\langle x,Dx\rangle\ge0.
\tag{SD7}
\]
所以全域 all-pairs 线性 RL 的常数不超过 1；高块的斜等距
Cayley 极限给锐常数恰为 1。在无界全图上非零线性反射不能有
有限的 \(0<\gamma<1\) 全局 Hölder 常数。近端的严格收缩
不能直接转授为同参数反射的严格收缩，反射非严格也不阻止
这里的每条近端路径收敛。
