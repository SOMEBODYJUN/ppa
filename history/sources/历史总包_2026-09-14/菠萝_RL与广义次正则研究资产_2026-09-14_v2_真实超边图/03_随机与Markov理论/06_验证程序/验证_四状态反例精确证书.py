"""Independent exact audit of a four-state Markov counterexample.

LP discovers dual contraction certificates; fractions.Fraction checks them
exactly. No symbolic algebra package or companion agent code is imported.
"""
import itertools
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog

pts=[Q(0),Q(1,2),Q(1),Q(2)]
img=[2,1,0,2]
P=[[Q(7,8)*(i==j)+Q(1,8)*(img[i]==j) for j in range(4)] for i in range(4)]
breaks=[Q(-7,4),Q(-5,4),Q(-3,4),Q(-1,4),Q(1,4),Q(3,4)]
F=[[min((x-y)**2+l*z for y,z in zip(pts[:3],[1,0,-1])) for x in pts] for l in breaks]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rowact(mu):return [sum(mu[i]*P[i][j] for i in range(4)) for j in range(4)]
def E(mu):return max(dot(f,mu) for f in F)
def quantile(mu,nu):
    left=list(mu);right=list(nu);out=[[Q(0)]*4 for _ in range(4)];i=j=0
    while i<4 and j<4:
        t=min(left[i],right[j]);out[i][j]+=t
        left[i]-=t;right[j]-=t
        if left[i]==0:i+=1
        if right[j]==0:j+=1
    assert sum(map(sum,out))==1
    return out
def cost(cpl):return sum(cpl[i][j]*(pts[i]-pts[j])**2 for i in range(4) for j in range(4))

def main():
    print('P =',P)
    print('six independent dual potential rows =',F)
    q=Q(15,16)
    four=[[Q(v,4) for v in row] for row in [[1,0,-1,3],[-1,0,1,5],[-3,-2,1,7],[-5,-4,-1,9]]]
    fourtheta=[[Q(9,10),Q(1,10),0,0],[Q(1,10),Q(9,10),0,0],[Q(2,15),0,Q(23,30),Q(1,10)],[Q(11,90),0,0,Q(79,90)]]
    expected=[[0,0,0,Q(1,8)],[0,0,0,0],[0,Q(3,64),0,0],[Q(1,8),Q(17,96),Q(9,64),0]]
    for j in range(4):
        g=[dot(row,four[j]) for row in P]
        slack=[q*sum(fourtheta[j][i]*four[i][k] for i in range(4))-g[k] for k in range(4)]
        assert slack==expected[j],(j,slack)
    print('all four proposed short rational certificates independently verified')
    for j in range(6):
        g=[dot(row,F[j]) for row in P]
        lp=linprog(np.zeros(6),A_ub=-float(q)*np.array(F,float).T,b_ub=-np.array(g,float),A_eq=np.ones((1,6)),b_eq=[1],bounds=(0,None),method='highs')
        assert lp.success,(j,lp.message)
        theta=[Q(float(v)).limit_denominator(1000000) for v in lp.x]
        slack=[q*sum(theta[i]*F[i][k] for i in range(6))-g[k] for k in range(4)]
        assert sum(theta)==1 and min(theta)>=0 and min(slack)>=0,(j,theta,slack)
        print(f'certificate {j+1}: theta={theta}, slack={slack}')
    deficit=[pts[i]-pts[img[i]] for i in range(4)]
    ratios=[]
    for i,j in itertools.combinations(range(4),2):
        dist=(pts[i]-pts[j])**2;td=(pts[img[i]]-pts[img[j]])**2
        ratios.append((Q(7,8)*dist+Q(1,8)*td+Q(1,8)*(deficit[i]-deficit[j])**2)/dist)
    assert max(ratios)==Q(3,2)
    print('pairwise expected firm ratios =',ratios)
    pi=[Q(1,2),0,Q(1,2),0]
    assert rowact(pi)==pi
    for t in [Q(1),Q(1,2),Q(1,10),Q(1,1000)]:
        mu=[Q(1,2),0,(1-t)/2,t/2]
        cpl=quantile(mu,pi)
        psi2=Q(1,8)*sum(cpl[i][j]*(deficit[i]-deficit[j])**2 for i in range(4) for j in range(4))
        assert psi2==0 and cost(cpl)==t/2
        assert cost(quantile(rowact(mu),pi))==t/2
        assert E(mu)==t/2 and E(rowact(mu))==Q(15,16)*E(mu)
        print('nonpara witness t=',t,'Psi^2=',psi2,'W2^2 to pi=',cost(cpl),'E=',E(mu))
    for t in [Q(1,4),Q(1,10),Q(1,1000)]:
        mu=[t,1-2*t,0,t];pi=[t,1-2*t,t,0]
        assert rowact(pi)==pi
        cpl=quantile(mu,pi)
        psi2=Q(1,8)*sum(cpl[i][j]*(deficit[i]-deficit[j])**2 for i in range(4) for j in range(4))
        assert psi2==0 and cost(cpl)==t and E(mu)==t
        assert E(rowact(mu))==Q(15,16)*t
        print('near-point-invariant witness t=',t,'Psi^2=',psi2,'E=',E(mu))
    print('ALL INDEPENDENT EXACT CHECKS PASSED')

if __name__=='__main__':main()
