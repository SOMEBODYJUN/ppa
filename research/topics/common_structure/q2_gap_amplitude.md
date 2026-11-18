# 二次移位 Fitzpatrick 间隙的 \(q=2\) 振幅截面

<a id="q2-gap-amplitude"></a>

在同一母面 \(g_a(z)=\mathfrak M_F^a(z,0)\) 上定义振幅
\[
\widetilde g_a(z):=\sqrt{g_a(z)}
\]
（在 \(D\cap\operatorname{dom}F\) 上 \(g_a\ge0\)）。若图截面满足
\(\beta\)-弱单调、\(a>2\beta\)，则
\[
g_a(z)\le\frac{r_F(z)^2}{2(a-2\beta)}. \tag{1}
\]
所以
\[
\widetilde g_a(z)\ge\gamma d(z,S)^2
\quad\Longrightarrow\quad
d(z,S)^2\le
\frac{1}{\gamma\sqrt{2(a-2\beta)}}\,r_F(z). \tag{2}
\]
这正是临界任务使用的 \(q=2\) 真残差端指数。

反向取完整近端根 \(z=y+\lambda v\)，假设输出窗有
\(d(y,S)^2\le K_{\rm EB}r_F(y)\) 且 \(\|v\|\le\bar r\)。由
\(r_F(y)\le\|v\|\) 和近端弦，
\[
d(z,S)\le\lambda\|v\|+\sqrt{K_{\rm EB}\|v\|},
\]
从而
\[
d(z,S)^2\le2(K_{\rm EB}+\lambda^2\bar r)\|v\|. \tag{3}
\]
另一方面母面在同一根上给
\[
g_a(z)\ge c_a\|v\|^2,\qquad
c_a=\lambda(1-a\lambda/2)>0.
\]
因此，在完整覆盖和共同图值帽下，
\[
\widetilde g_a(z)\ge
\frac{\sqrt{c_a}}{2(K_{\rm EB}+\lambda^2\bar r)}\,d(z,S)^2. \tag{4}
\]
这条反向只使用根覆盖；没有根覆盖，输出误差界不能生成输入 \(z\) 的母面见证。
大残差可用有限层分解处理，但不能不加条件地删去图值帽。

振幅截面把同一个 \(M\) 与 \(d^2\lesssim r_F\) 精确接上；它不把
\(q=2\) 的 value-weighted 曲率自动变成常数弱单调。要从临界曲率得到 PPA
收缩，仍需锚输运、正 reach 的切向估计，或另一个保留近端弦方向的结构门。

