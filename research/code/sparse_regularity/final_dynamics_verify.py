"""Independent audit computation; no imports from the reviewed project."""
from fractions import Fraction as F
from math import sqrt
import json, platform

def binom(p,n):
    r=F(1)
    for j in range(n): r*= (p-j)/(j+1)
    return r

p=F(7,4); exponent=1/p
# f(u)=H(u^2); obtain coefficients from G H'=exponent G' H.
g=[binom(p,2*j) for j in range(31)]
c=[F(1)]
for n in range(1,31):
    c.append(exponent*g[n]+sum((((exponent+1)*i-n)*g[i]*c[n-i]
                                for i in range(1,n)),F(0))/n)
assert c[1]==F(3,8) and c[2]==-F(11,256)
r=F(7,8); v=F(1,196)
g_bound=F(21,32)*r*r+F(35,2048)*r**4/(1-r*r)
assert g_bound==F(214375,393216)<1
majorants=[2*r**-6/(1-v),
  2*r**-6*(6/(1-v)+2*v/(1-v)**2),
  2*r**-6*(30/(1-v)+26*v/(1-v)**2+8*v*v/(1-v)**3)]
assert all(a<b for a,b in zip(majorants,[5,28,140]))
star=F(95,1024)-F(11,8192)-(28+F(5,32))/961
assert star>F(1,32)
assert (2*F(9,64)**2+F(33,32)**4)/64<F(1,32)
assert F(3,7)+F(3,64)+F(5,2)<3
assert F(25,128**2*2)<F(1,32**2)
sign=F(3,124)+F(11,64*32**2)*F(32,31)**3+F(28,32**4)*F(32,31)**5
assert sign<F(1,32)
radial=-F(3,8)/4
quartic=2*radial**2+F(3,8)*radial+F(11,256)
tangent=F(3,4)*radial+F(11,64)
assert radial==-F(3,32) and quartic==F(13,512) and tangent==F(13,128)

R=2**(4/7)
cf=[float(a) for a in c]
def derivatives(h,t):
    s=1+h; u=t/s
    # Stable evaluation from the independently reconstructed exact series.
    vh=4*h+sum((2*j-1)*cf[j]*u**(2*j) for j in range(1,16))
    vt=.75*h*u-sum(2*j*cf[j]*u**(2*j-1) for j in range(2,16))
    fpp=sum(2*j*(2*j-1)*cf[j]*u**(2*j-2) for j in range(1,16))
    return vh,vt,4-u*u*fpp/s,u*fpp/s,.75-fpp/s

def step(h0,t0,lam):
    h,t=h0,t0
    for _ in range(8):
        vh,vt,hh,ht,tt=derivatives(h,t)
        k=lam*R/2
        a,b,d=1+k*hh,k*ht,1+k*tt
        eh,et=h+k*vh-h0,t+k*vt-t0
        det=a*d-b*b
        dh,dt=(d*eh-b*et)/det,(a*et-b*eh)/det
        h,t=h-dh,t-dt
        if max(abs(dh),abs(dt))<2e-18: break
    vh,vt,*_=derivatives(h,t)
    residual=max(abs(h+lam*R/2*vh-h0),abs(t+lam*R/2*vt-t0))
    return h,t,residual

def trajectory(h,t,lam,N):
    d0=sqrt(2*(h*h+t*t)); initial=[h,t]; mxerr=0.; maxrad=d0
    assert d0<=1/64
    for k in range(N):
        hn,tn,err=step(h,t,lam)
        assert t*tn>0
        newrad=sqrt(2*(hn*hn+tn*tn))
        assert newrad<=maxrad*(1+2e-15)
        maxrad=newrad; mxerr=max(mxerr,err)
        h,t=hn,tn
    vh,vt,*_=derivatives(h,t)
    # Cancellation-free exact expression for reciprocal-square difference.
    A=lam*R/2*vt/t
    slope=(2*A+A*A)/(t*t*(1+A)**2)
    target=13*lam*R/128
    return dict(initial=initial,lam=lam,N=N,h=h,t=t,w=h/t**2,
                target_w=-3/32,slope=slope,target_slope=target,
                slope_ratio=slope/target,implicit_residual=mxerr,
                sqrt_k_distance=sqrt(N)*maxrad,
                asymptotic_distance_constant=16/sqrt(13*lam*R))

results=[trajectory(.005,.005,1/128,10000),
         trajectory(-.005,-.009,1/128,10000),
         trajectory(.01,1e-8,1/128,4000),
         trajectory(-.002,.007,1/1024,15000)]
for z in results:
    assert abs(z['w']+3/32)<1e-5
    assert abs(z['slope_ratio']-1)<2e-4
h,t=.01,0.
for k in range(100): h,t,err=step(h,t,1/128)
axis_expected=.01/(1+2*R/128)**100
assert t==0 and abs(h-axis_expected)<1e-17
report=dict(python=platform.python_version(),
            exact_coefficients=[str(a) for a in c[:7]],
            cauchy_majorants=[float(a) for a in majorants],
            star_bracket=float(star),sign_bound=float(sign),
            geometric_axis_error=h-axis_expected,trajectories=results,
            scope='Finite computation corroborates arithmetic and actual implicit equations; analytic proof carries all quantifiers.')
print(json.dumps(report,indent=2))
