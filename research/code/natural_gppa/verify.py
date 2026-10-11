import json, math, random, hashlib, sys
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal as D, getcontext
getcontext().prec=80
def bisect_decimal(fun, lo, hi):
    for _ in range(280):
        mid=(lo+hi)/2
        if fun(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2
random.seed(20261011)
R=1/128

def cb(a): return math.copysign(abs(a)**(1/3),a) if a else 0.
def inv(p,q):
    t=1+cb(q+p*p/2)
    return p*t,t

def prox(p,q):
    if q <= -1/8-p*p/18:
        return p/6, .5, p/3, -1/8-p*p/18
    lo,hi=.5,max(2.,1+cb(abs(q)+p*p/2))
    def d(t): return (t-1)**3-q-p*p/(2*(1+4*t)**2)
    while d(hi)<0: hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if d(mid)>0: hi=mid
        else:lo=mid
    t=(lo+hi)/2; a=p/(1+4*t)
    return a*t,t,a,q

xs=[-R,0,R]+[random.uniform(-R,R) for _ in range(2000)]
qs=[-1/16+1e-10,-1/64,0,1/64,1/16-1e-10]
err=0.; maxr=0.; maxanch=0.; mint=1.; eb=0.
for p in xs:
  for q in qs:
    x,t,a,b=prox(p,q)
    err=max(err,abs(p-a-4*x),abs(q-(t-1)**3+a*a/2))
    if p: maxr=max(maxr,abs(a/p)); maxanch=max(maxanch,abs(2*a-p)/abs(p))
    mint=min(mint,t); eb=max(eb,abs(a)-2*abs(x))
assert err<1e-14 and maxr<1/3 and eb<=1e-15 and mint>.5 and maxanch<=1
# Inspect singular first steps with 80-digit precision.
rows=[]
for j in range(1,11):
 a=D(10)**(-j); p=a; q=-a*a/2
 # use t=1-a^(2/3)*c, c near (12/25)^(1/3), to avoid flat root instability
 h=a**(D(2)/3)
 fun=lambda c: -c**3+D('0.5')-1/(2*(5-4*h*c)**2)
 c=bisect_decimal(lambda c:-fun(c),D('.7'),D('.9'))
 t=1-h*c; x=a*t/(1+4*t)
 df=(a*a-x*x)/2; st=(a-x)**2+(1-t)**2
 rows.append({'a':float(a),'t_shift_over_a_two_thirds':float((1-t)/h),'xplus_over_a':float(x/a),'objective_descent_over_step_squared':float(df/st)})
# Critical orbit q=0 gives asymptotic point-error ratio 5^(-2/3).
p=D(1)/64; ratios=[]
for k in range(12):
 t=1+(p*p/2)**(D(1)/3); x=p*t; e=(x*x+(t-1)**2).sqrt()
 # unknown ratio a/p in (0,1/3)
 ratio=bisect_decimal(lambda r:r*(5+4*(p*p*r*r/2)**(D(1)/3))-1, D('.15'),D('.25'))
 pp=p*ratio; tt=1+(pp*pp/2)**(D(1)/3); xx=pp*tt; ee=(xx*xx+(tt-1)**2).sqrt()
 ratios.append(float(ee/e)); p=pp
pair_holder_max=0.
for _ in range(20000):
 p,q=random.uniform(-R,R),random.uniform(-1/64,1/64)
 pp,qq=random.uniform(-R,R),random.uniform(-1/64,1/64)
 X=inv(p,q); XX=inv(pp,qq); Y=prox(p,q); YY=prox(pp,qq)
 delta=math.hypot(X[0]-XX[0],X[1]-XX[1])
 if delta: pair_holder_max=max(pair_holder_max,math.hypot(Y[0]-YY[0],Y[1]-YY[1])/math.sqrt(delta))
assert pair_holder_max<15
sharp_pairs=[]
for j in range(2,11):
 e=D(10)**(-j); K=(1-1/(5+4*e)**2)/2
 p2=e*((12-e)/K).sqrt(); t0=1+(12*e*e)**(D(1)/3)
 dx=t0*abs(p2-5*e); dy=((p2*(1+e)/(5+4*e)-e)**2+e*e).sqrt()
 sharp_pairs.append({'epsilon':float(e),'input_gap_over_epsilon_squared':float(dx/(e*e)),'output_gap_over_epsilon':float(dy/e),'half_holder_ratio':float(dy/dx.sqrt())})
# Complete boundary fibers, including equality and far inputs.
boundary_cases=0
for p0 in [-100., -3., -R, 0., R, 3., 100.]:
    qb=-1/8-p0*p0/18
    for offset in [-10., -1e-8, 0., 1e-8, 10.]:
        q0=qb+offset
        x,t,a,qout=prox(p0,q0)
        normal=(q0-qout)/4
        assert abs(p0-a-4*x)<1e-10
        if q0<=qb:
            assert t==.5 and normal<=1e-12
        else:
            assert t>.5 and abs(normal)<1e-12
            assert abs(q0-(t-1)**3+a*a/2)<1e-10
        boundary_cases+=1
assert Q(1,128)/4 < 1
assert 2*Q(1,128) < Q(1,16)-Q(1,32)
assert Q(5504) < Q(9)**4
# Direct physical-parent window: exact strict margins, independent of float roots.
physical_R=Q(1,10**9)
assert Q(1,2) < Q(4,5)**3
assert 2*physical_R < Q(13,10000)**3
assert Q(39,2000) < Q(1,8)
assert 4*physical_R/3 < Q(1,128)
assert Q(1,64)+8*physical_R**2/9 < Q(1,16)
assert Q(16,9)*(1+4*physical_R**2/9) < 4
physical_theta=3*(D(2)/D(10)**9)**(D(1)/3)/(1-D(2)**(-D(1)/3))
out={'seed':20261011,'precision_digits':80,'kernel_inputs_checked':len(xs)*len(qs),'max_equation_error':err,'max_normal_contraction':maxr,'minimum_output_t':mint,'max_EB_violation':eb,'max_anchor_ratio':maxanch,'singular_first_steps':rows,'critical_error_ratios':ratios,'critical_ratio_theory':5**(-2/3),'physical_pair_half_holder_max_bound_15':pair_holder_max,'sharp_half_holder_pairs':sharp_pairs}
out['complete_boundary_cases']=boundary_cases
out['tuple']={'R':R,'lambda':4,'gamma':1,'L':1,'bar_t':1,'kappa':.5,'psi':'2s'}
out['physical_parent_tuple']={'R':'1e-9','lambda':4,'a':'2r','omega':'q','h':'3q^(1/3)','psi':'q','bar_t':1,'kappa':.5,'Theta_R':str(physical_theta),'strict_rational_upper_bound':'39/2000','initial_t_distance_to_1_max':'1/8'}
out['python']=sys.version.split()[0]
out['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
out['scope']='Finite arithmetic, boundary reverse substitution, samples and asymptotics; universal conclusions use canonical proof.'
with open(Path(__file__).with_name('results.json'),'w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
