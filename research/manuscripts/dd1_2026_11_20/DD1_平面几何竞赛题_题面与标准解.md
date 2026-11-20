---
title: "DD1 平面几何竞赛题：题面与标准解"
date: 2026-11-20
tags:
  - DD1
  - 平面几何
  - 竞赛题
  - 标准解
status: contest-style-draft
---

# 题目

在平面内取一个非空闭集 \(S\)。设
\[
P_1\in P_S(X),\qquad P_2\in P_S(Y),
\]
即 \(P_1,P_2\) 分别是 \(X,Y\) 到 \(S\) 的最近点。记
\[
a=XP_1,\qquad b=YP_1,\qquad s=XY,\qquad t=YP_2.
\]

设 \(\rho>0\)、\(\sigma\ge 0\)，并满足
\[
 s^2+b^2\le (1+2\sigma)a^2, \tag{1}
\]
\[
 t\le \rho s. \tag{2}
\]
由于 \(P_1,P_2\) 是最近点，另有
\[
 t\le b,\qquad a\le XP_2. \tag{3}
\]

求关于 \(\rho\) 的最大函数 \(T(\rho)\)，使得当
\[
\sigma<T(\rho)
\]
时，对所有满足上述条件的构形均有
\[
YP_2<XP_1.
\]
并证明所得函数是锐的。

---

# 标准解

令 \(M\) 为 \(XP_1\) 的中点。

由阿波罗尼斯中线定理，
\[
XY^2+YP_1^2=2YM^2+\frac12 XP_1^2. \tag{4}
\]
因此 (1) 等价于
\[
YM^2\le \left(\sigma+\frac14\right)XP_1^2. \tag{5}
\]
特别地，当 \(\sigma=0\) 时，\(Y\) 位于以 \(XP_1\) 为直径的圆内；边界情形由泰勒斯定理给出直角。

另一方面，等式
\[
YP_2=\rho\,XY
\]
是以 \(X,P_2\) 为两个定点、比值为 \(\rho\) 的阿波罗尼斯圆。因此 (2) 给出该圆盘的一侧。

再由 \(t\le b\)，点 \(Y\) 位于 \(P_2\) 相对于 \(P_1\) 的沃罗诺伊最近区域内。下面只需估计 \(t/a\) 的最大值。

## 第一种估计

由反三角不等式，
\[
b\ge |a-s|.
\]
代入 (1)，得到
\[
s^2+(a-s)^2\le (1+2\sigma)a^2.
\]
令 \(u=s/a\)，则
\[
u^2-u-\sigma\le0.
\]
所以
\[
\frac{s}{a}\le \frac{1+\sqrt{1+4\sigma}}2.
\]
结合 (2)，有
\[
\frac{t}{a}\le
\frac{\rho(1+\sqrt{1+4\sigma})}{2}. \tag{6}
\]

## 第二种估计

由 (3) 中的 \(t\le b\) 和题设中的 \(t\le\rho s\)，得
\[
\frac{t^2}{\rho^2}\le s^2,\qquad t^2\le b^2.
\]
相加可得
\[
\left(1+\frac1{\rho^2}\right)t^2\le s^2+b^2.
\]
再使用 (1)，得到
\[
\frac{t}{a}\le
\rho\sqrt{\frac{1+2\sigma}{1+\rho^2}}. \tag{7}
\]

由 (6)、(7)，
\[
\boxed{
\frac{YP_2}{XP_1}\le
\min\left\{
\frac{\rho(1+\sqrt{1+4\sigma})}{2},\quad
\rho\sqrt{\frac{1+2\sigma}{1+\rho^2}}
\right\}. }\tag{8}
\]

要使右端严格小于 \(1\)，第一项给出
\[
\sigma<\frac{1-\rho}{\rho^2},\qquad 0<\rho<1, \tag{9}
\]
第二项给出
\[
\sigma<\frac1{2\rho^2}. \tag{10}
\]
比较 (9)、(10)，得到
\[
\boxed{
T(\rho)=\begin{cases}
\dfrac{1-\rho}{\rho^2},&0<\rho\le \dfrac12,\\[8pt]
\dfrac1{2\rho^2},&\rho\ge \dfrac12.
\end{cases}}\tag{11}
\]
因此，当 \(\sigma<T(\rho)\) 时，必有
\[
YP_2<XP_1.
\]

## 锐性

先令 \(XY=1\)。

当 \(0<\rho\le \frac12\) 时，取
\[
X=(0,0),\qquad Y=(1,0),\qquad
P_1=(\rho,0),\qquad P_2=(1+\rho,0).
\]
此时
\[
XP_1=YP_2=\rho,\qquad YP_1=1-\rho,\qquad YP_2=\rho\,XY,
\]
且在
\[
\sigma=\frac{1-\rho}{\rho^2}
\]
时，(1) 取等号。因此第一段临界值不能提高。

当 \(\rho\ge\frac12\) 时，取
\[
X=(0,0),\qquad Y=(1,0),\qquad
P_1=P_2=\left(\frac12,\sqrt{\rho^2-\frac14}\right).
\]
此时
\[
XP_1=YP_2=\rho,\qquad YP_1=YP_2,\qquad YP_2=\rho\,XY,
\]
且在
\[
\sigma=\frac1{2\rho^2}
\]
时，(1) 取等号。因此第二段临界值也不能提高。

故 (11) 是锐的。

\[
\boxed{\text{证毕。}}
\]

---

## 讲解者备注（不放入正式题面）

这份标准解只在证明中调用三个几何背景：

1. **阿波罗尼斯中线定理 / 泰勒斯定理**：处理第一条平方距离约束；
2. **阿波罗尼斯圆的轨迹性质**：处理距离比约束；
3. **沃罗诺伊最近区域**：处理最近点条件。

正式题面不提前告诉读者这些名称；读者先面对一个自然的四点构形，证明过程中再识别出三个经典结构。DD1 的新内容是三种局部几何规则共同产生的分段锐补偿函数 \(T(\rho)\)。
