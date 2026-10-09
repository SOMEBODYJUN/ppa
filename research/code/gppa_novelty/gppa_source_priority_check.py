#!/usr/bin/env python3
"""Finite arithmetic checks for source-priority follow-up; not novelty/proof tests.
Run: python3 research/code/gppa_novelty/gppa_source_priority_check.py
Python 3 stdlib only; no external data, no randomness.
"""
from fractions import Fraction as Q
from math import sqrt
import json

# Nonmonotone, genuinely noninjective kernel example:
# v(r,s)=(r,0); F(r,s)={(a*r,0),(a*r,-s)}.
# Every value pair obeys ASM because kernel differences have zero second component.
a=Q(2)
grid=tuple(Q(i,2) for i in range(-4,5))
count=0
for r in grid:
    for s in grid:
        for u in grid:
            for t in grid:
                for f2 in (Q(0),-s):
                    for g2 in (Q(0),-t):
                        pairing=(a*r-a*u)*(r-u)+(f2-g2)*0
                        assert pairing==a*(r-u)**2
                        count+=1
# F not monotone; physical strong pair fails along a kernel fiber.
assert (Q(-1)-0)*(Q(1)-0)<0
# All physical selections (w1,s) using the zero second branch give the same kernel.
for gamma in (Q(1,4),Q(1),Q(3)):
    for r in grid:
        w1=r/(1+gamma*a)
        for s in grid:
            assert (1+gamma*a)*w1==r
            assert gamma*0==0
# Sharp standard strong-resolvent square factor improves printed T2 factor.
rates=[]
for t in (Q(1,100),Q(1,10),Q(1),Q(4),Q(5)):
    standard=1/(1+t)**2
    printed=1/(1+2*t)
    assert standard<printed
    old_ratio=1/(sqrt(1+2*float(t))-1)
    printed_coarse=2/float(t)
    assert (old_ratio<=printed_coarse+1e-12)==(t<=4)
    assert (1/(1+t))/(1-1/(1+t))==1/t
    rates.append({'gamma_epsilon':str(t),'standard_square':str(standard),
                  'printed_square':str(printed),'old_ratio_bound_valid':t<=4})
# Printed T4 source budget and tighter standard-contraction cancellation budget.
for L in (Q(0),Q(1),Q(3)):
    for epsilon in (Q(1,100),Q(1,10),Q(1)):
        for gamma in (Q(1,4),Q(1),Q(4)):
            a0=Q(2)
            b=L*epsilon/gamma**2+L*epsilon**2/gamma+epsilon*a0
            B=4*L*epsilon/gamma**2+3*L*epsilon**2/gamma+epsilon*a0
            assert B-b==3*L*epsilon/gamma**2+2*L*epsilon**2/gamma
            assert B>=b
# Physical point selections need not converge, though original distance contracts.
traj=[]
r=Q(1);gamma=Q(1)
for k in range(7):
    traj.append({'k':k,'kernel_first':str(r),'physical_second':((-1)**k)*k})
    r=r/(1+gamma*a)
print(json.dumps({'status':'finite checks passed','asm_value_pairs_checked':count,
                  'rate_comparison':rates,'nonconvergent_physical_selection':traj},indent=2))
