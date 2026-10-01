"""Independent rational checks for projection and shrinking-block extensions.

Finite checks corroborate, not replace, the all-n dual proof in the audit.
"""
from fractions import Fraction as F
from itertools import combinations

P=[[F(7,8)*(i==j)+F(1,8)*([2,1,0,2][i]==j) for j in range(4)] for i in range(4)]
def act(mu):return [sum(mu[i]*P[i][j] for i in range(4)) for j in range(4)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cost2(x,y):return sum((a-b)**2 for a,b in zip(x,y))
def local_E(mu,eps):
    h=2-eps;pts=[F(0),F(1,2),F(1),h]
    bs=[-F(3,4),-F(1,4),F(1,4),F(3,4),h-F(3,4),h-F(1,4)]
    forms=[[min(x*x-l,(x-F(1,2))**2,(x-1)**2+l) for x in pts] for l in bs]
    vals=[dot(mu,v) for v in forms]
    return max(vals)

def main():
    q=F(15,16)/(1-F(1,100))**2
    assert q==F(3125,3267)<1
    print('uniform squared-distance factor =',q)
    firm=1+F(1,8)*(F(5,4)**2+F(9,4)**2-1)
    assert firm==1+F(45,64)
    # The natural correlated projection witness and its actual product limit.
    for t in [F(1,8),F(1,4),F(1,3)]:
        src=[(F(1,2)-t,0),(F(1,2)+t,1)]
        target=[(x,y) for x in [F(1,2)-t,F(1,2)+t] for y in [0,1]]
        # All extreme couplings: each source supplies two quarter-mass targets.
        costs=[]
        for first in combinations(range(4),2):
            cc=sum(F(1,4)*cost2(src[0 if j in first else 1],target[j]) for j in range(4))
            costs.append(cc)
        assert min(costs)==2*t*t
        pivot=[(F(1,2),0),(F(1,2),1)]
        assert sum(F(1,2)*cost2(src[i],pivot[i]) for i in range(2))==t*t
        print('projection witness t =',t,'actual-limit transport^2 =',min(costs),'nearest-anchor^2 =',t*t)
    blocks=[];labels=[]
    for n in range(1,13):
        tn=F(1,2**n);dn=F(1,2**(3*n+10));eps=dn**n;h=2-eps
        assert 0<eps<F(1,100)
        pts=[F(0),F(1,2),F(1),h];out=[F(1),F(1,2),F(0),F(1)]
        for x in pts:
            original=F(2) if x==h else x
            for y in [F(0),F(1,2),F(1)]:
                c=(x-y)**2;c0=(original-y)**2
                assert (1-eps)**2*c0<=c<=c0
        for i,j in combinations(range(4),2):
            dist=(pts[i]-pts[j])**2;outdist=(out[i]-out[j])**2
            rdiff=(pts[i]-out[i])-(pts[j]-out[j])
            ratio=(F(7,8)*dist+F(1,8)*outdist+F(1,8)*rdiff**2)/dist
            assert ratio<=firm
        mu=[F(1,4),F(1,2),F(0),F(1,4)]
        e=local_E(mu,eps)
        assert e==F(1,4)*(1-eps)**2
        assert local_E(act(mu),eps)<=q*e
        assert 0<dn*eps and dn*eps==dn**(n+1)
        current=[-dn,dn,dn*(1-eps)]
        assert len(set(current))==3 and not set(current).intersection(labels)
        labels.extend(current)
        blocks.append((tn,dn,eps,pts,out))
    for (tn,dn,en,xn,on),(tm,dm,em,xm,om) in combinations(blocks,2):
        gap=tn-(tm+dm*(2-em))
        assert gap>=4*(dn+dm)
        assert gap**2>=F(9,4)*dn**2+F(5,4)*dm**2
        assert gap**2>=F(9,4)*dm**2+F(5,4)*dn**2
        for i in range(4):
            for j in range(4):
                x=tn+dn*xn[i];y=tm+dm*xm[j]
                tx=tn+dn*on[i];ty=tm+dm*om[j]
                assert abs(tx-ty)<=F(5,4)*abs(x-y)
                dd=(x-y)**2;od=(tx-ty)**2;rd=(x-tx)-(y-ty)
                assert F(7,8)*dd+F(1,8)*od+F(1,8)*rd**2<=firm*dd
    # Check the positive mixture identity exactly at several k.
    for k in range(25):
        a=F(7,8)**k;r=F(3,4)**k
        assert a-r/2>=0
        assert (1-2*a)/2+(a-r/2)==(1-r)/2
        assert (1-2*a)/2+r/2==(1+r)/2-a
    print('12 rational blocks, all cross-block pairs, residual labels, cost bounds and mixture identities verified')
    print('ALL INDEPENDENT EXTENSION CHECKS PASSED')

if __name__=='__main__':main()
