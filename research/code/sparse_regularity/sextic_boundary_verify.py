"""Independent exact structural audit. Finite exact calculation; not a universal proof.
Scope: p-polynomial coefficient identities, endpoint finite series and C229 sextic coefficients.
"""
from fractions import Fraction as F

def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and a[-1] == 0: a.pop()
    return tuple(a)

class P:
    def __init__(self, a): self.a = trim(a if isinstance(a,(tuple,list)) else [a])
    def __add__(self, other):
        other = other if isinstance(other,P) else P(other)
        size = max(len(self.a),len(other.a))
        return P([(self.a[i] if i<len(self.a) else 0)+(other.a[i] if i<len(other.a) else 0) for i in range(size)])
    __radd__ = __add__
    def __neg__(self): return P([-a for a in self.a])
    def __sub__(self, other): return self+(-other if isinstance(other,P) else -P(other))
    def __rsub__(self, other): return P(other)-self
    def __mul__(self, other):
        other = other if isinstance(other,P) else P(other)
        out = [F(0)]*(len(self.a)+len(other.a)-1)
        for i,a in enumerate(self.a):
            for j,b in enumerate(other.a): out[i+j] += a*b
        return P(out)
    __rmul__ = __mul__
    def __pow__(self,k):
        out=P(1)
        for _ in range(k): out=out*self
        return out
    def __truediv__(self,scalar): return P([a/F(scalar) for a in self.a])
    def __eq__(self,other): return self.a==(other if isinstance(other,P) else P(other)).a
    def at(self,value): return sum(a*F(value)**i for i,a in enumerate(self.a))

p=P([0,1])
A=(p-1)*(p-2)*(p-3)/24
B=(p-1)**3/8
D=(p-1)*(p-2)**2/18
assert A-B==(p-1)*(3-2*p)*(p+1)/24
assert A-D==(p-1)*(2-p)*(p+1)/72
assert (A-D).at(F(3,2))==F(5,576)
assert (A-B).at(F(3,2))==0
assert A.at(F(3,2))==F(1,64)
print('Pearson decomposition and endpoint equality coefficient: PASS')

def binomial(a,k):
    out=F(1)
    for i in range(k): out *= (a-i)/(i+1)
    return out

def mul_series(a,b,order):
    out=[F(0)]*(order+1)
    for i,aa in enumerate(a):
        for j,bb in enumerate(b):
            if i+j<=order: out[i+j]+=aa*bb
    return out

def power_one_plus(v,exponent,order):
    out=[F(0)]*(order+1)
    power=[F(1)]+[F(0)]*order
    for k in range(order+1):
        coeff=binomial(exponent,k)
        out=[x+coeff*y for x,y in zip(out,power)]
        power=mul_series(power,v,order)
    return out

def symmetric_norm_series(exponent,order):
    v=[F(0) if k%2 else binomial(exponent,k) for k in range(order+1)]
    v[0]=0
    return power_one_plus(v,1/exponent,order)

endpoint=symmetric_norm_series(F(3,2),8)
assert endpoint[2]==F(1,4)
assert endpoint[3:6]==[0,0,0]
assert endpoint[6]==F(1,192)
assert endpoint[7]==0
print('Endpoint normalized series through degree 8:',endpoint)

c2=(p-1)/2
c4=A-(p-1)**3/8
assert c4==-(p-1)*(2*p-3)*(p+1)/24
assert 3*(p-1)*(-4*c4)==2*(2*p-3)*(p+1)*c2**2
assert -c4/2==(p-1)*(2*p-3)*(p+1)/48
print('Upper-family c4, alpha0, positive K formula: PASS')

c6=(p-1)*(p-2)*(p-3)*(p-4)*(p-5)/720-(p-1)**3*(p-2)*(p-3)/48+(p-1)**4*(2*p-1)/48
c6_factored=(p-1)*(p+1)*(16*p**3-30*p**2-19*p+45)/720
assert c6==c6_factored
K6=p*(p-1)*(p+1)*(2*p-1)*(p-2)/360
assert 4*c4**2-(p-1)*c6==(p-1)*K6
print('New alpha=alpha0 sextic reduced coefficient identity: PASS')
for value in [F(3,2),F(7,4),F(2),F(3),F(10)]:
    actual=symmetric_norm_series(value,6)
    assert actual[2]==c2.at(value)
    assert actual[4]==c4.at(value)
    assert actual[6]==c6.at(value)
    boundary_info = ('boundary K6/R='+str(K6.at(value))) if value>F(3,2) else 'alpha0 boundary not defined here'
    print('Finite spot p=',value,'c4=',actual[4],'c6=',actual[6],boundary_info)

# New concrete p=3 boundary family: substitute h=-2t^2-2t^4.
# The t^4 correction is checked by the radial derivative, and the
# objective's leading t^6 coefficient is independent of further terms.
order=8
hs=[F(0)]*(order+1)
hs[2]=hs[4]=F(-2)
ss=hs.copy()
ss[0]=F(1)
inverse_ss=power_one_plus(hs,F(-1),order)
inverse_ss2=mul_series(inverse_ss,inverse_ss,order)
u2=[F(0),F(0)]+inverse_ss2[:-2]
ff=power_one_plus([3*a for a in u2],F(1,3),order)
ff_minus=ff.copy()
ff_minus[0]-=1
norm_change=mul_series(ss,ff_minus,order)
hs2=mul_series(hs,hs,order)
Vnorm=[a/4-b for a,b in zip(hs2,norm_change)]
Vnorm[2]+=1
assert Vnorm[:6]==[0]*6
assert Vnorm[6]==F(1,3)
radial=[a/2 for a in hs]
# 1-f+u f' = u2-3u2^2+(25/3)u2^3+... for p=3.
u4=mul_series(u2,u2,order)
u6=mul_series(u4,u2,order)
radial=[a+b-3*c+F(25,3)*d for a,b,c,d in zip(radial,u2,u4,u6)]
assert radial[:6]==[0]*6
print('Concrete p=3 h_* coefficients through t^4, reduced leading R*t^6/3: PASS')

value=F(3,2)
v=[F(0)]+[binomial(value,k)/2 for k in range(1,5)]
line=power_one_plus(v,1/value,4)
assert line[3]==-F(1,32)
print('p=3/2 stationary saddle normalized norm cubic -1/32: PASS')
print('RUN SCOPE: exact p-polynomial identities and finite series; analytic reasoning carries all universal claims.')
