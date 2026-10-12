"""C259-C263 finite arithmetic and reverse substitution; not universal proofs."""
from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, math, random, sys
getcontext().prec=80
R=Q(1,10**12)
rootR=Q(1,10**6)
# Exact inequalities used in global localization and joint constants.
assert Q(4,27)<Q(77,200)**2
assert Q(11,26)-Q(77,200)==Q(99,2600)>Q(1,27)
assert Q(26)<Q(51,10)**2
assert 54+353430*R<55
assert 110+2*R<111<121
assert 1+1493284*R<Q(1001,1000)
assert 11+Q(1001,1000)*rootR<Q(11001,1000)
assert Q(1001,1000)+Q(1,2)*Q(11001,1000)**2<62
assert 6*11*62==4092
p_coefficient=Q(51,110)+4092*rootR
assert p_coefficient<Q(469,1000)
assert Q(469,1000)<Q(137,200)**2
assert 2*Q(137,200)+Q(969,500)*rootR<Q(1371,1000)<Q(3,2)
compat=Q(11,40)*(Q(3,2)+rootR)**2
assert compat<Q(619,1000)<Q(3,4)
assert Q(3,4)<Q(7,8)**2
assert 2*R+6*rootR<Q(1,2)-R
assert 100*Q(469,1000)*R<Q(1,11)**2
assert (R+Q(3,2)*rootR)/2<1
# Same original circle window has a shorter independent energy certificate.
assert Q(98)-Q(201,2)/16>90
assert Q(1,3)-Q(1,200)>Q(1,4)
energy_quadratic=Q(6)+Q(8*10**6,24300)
assert energy_quadratic<336
assert Q(1,135)+336*Q(3,10**6)<Q(1,100)
# Feedback energy alternative really uses the newly proved geometry.
Tmax=Q(9,2*10**18)
cube_bound=Q(1651,10**9)
assert cube_bound**3>Tmax
alpha=Q(51,110)+4092*cube_bound
assert alpha<Q(471,1000)<Q(687,1000)**2
assert Q(471,1000)*Q(687,1000)+(1+11*Q(471,1000))**3*Tmax<Q(324,1000)
# Uniform C1-obstruction auxiliary predecessors, for all declared test tuples.
aux=[]
for gamma in (0,10,99):
    A=1+gamma
    for rr in (Q(1,10**12), min(Q(1,100),Q(1,A))):
        pp=rr**2/4
        assert pp+A*A*pp*pp<=5*rr*rr/16<rr*rr
        assert pp+gamma*gamma*pp*pp<=2*pp
        assert A*(pp/A)<rr
        aux.append({'Gamma':gamma,'R':str(rr),'Pstar':str(pp)})

def sincos(x):
    s=D(0);c=D(0);ts=x;tc=D(1)
    for j in range(110):
        s+=ts;c+=tc
        ts*= -x*x/D((2*j+2)*(2*j+3))
        tc*= -x*x/D((2*j+1)*(2*j+2))
    return s,c

def norm(v): return sum(t*t for t in v).sqrt()
def dot(a,b): return sum(x*y for x,y in zip(a,b))
sharp=[]
max_reverse=D(0)
s=D(3025)/5408
for j in (3,4,5,6,7,8,9):
    theta=D(10)**(-j);sn,cs=sincos(theta);r=1-s*theta**4
    z=[r*cs,r*sn];v=[z[0]-1,z[1]];ell=norm(v)
    p=[ell*t for t in v];P=norm(p);g=[-2*(1-r*r).sqrt()*t for t in z]
    e=[-5*g[1],5*g[0]];b=[g[i]+e[i]+11*p[i] for i in range(2)]
    max_reverse=max(max_reverse,abs(dot(e,g)),abs(norm(e)-5*norm(g)),norm([p[i]/P.sqrt()-v[i] for i in range(2)]))
    outdist=((1-r)**2+P*P).sqrt();indist=norm(b)
    sharp.append({'theta':str(theta),'distance_ratio':str(outdist/indist),'anchor_coefficient':str(norm([2*v[0],2*v[1],2*p[0]-b[0],2*p[1]-b[1]])/indist.sqrt())})
assert max_reverse<D('1e-60')
# Both directions of the H1-only obstruction: exact rational circle points.
chord_cases=[]
for gamma in (0,10,99):
    A=1+gamma
    for sign in (-1,1):
        tt=sign*Q(1,10**8)
        zx=(1-tt*tt)/(1+tt*tt);zy=2*tt/(1+tt*tt)
        assert zx*zx+zy*zy==1
        zc=[D(zx.numerator)/zx.denominator,D(zy.numerator)/zy.denominator]
        vc=[zc[0]-1,zc[1]];lc=norm(vc);pc=[lc*x for x in vc];Pc=norm(pc)
        assert A*Pc<D('1e-12')
        rr=norm([pc[i]/Pc.sqrt()-vc[i] for i in range(2)])
        assert rr<D('1e-60')
        assert sign*pc[1]/Pc>D('.999999999999')
        chord_cases.append({'Gamma':gamma,'direction':sign,'P':str(Pc),'signed_tangent_limit':str(pc[1]/Pc),'reverse_error':str(rr)})
# Exact off-window global implicit energy-increase witness.
z=[(D(26)/29).sqrt(),D(0)]
t=2*D(78).sqrt()/319;p=[t,5*t];P=norm(p)
witness_P=P
a=[z[i]-p[i]/P.sqrt() for i in range(2)]
g=[-2*D(78).sqrt()/29,D(0)]
e=[D(0),5*g[0]]
reverse=norm([g[i]+e[i]+11*p[i] for i in range(2)])
a2=dot(a,a);Ein=D(2)/3*abs(a2-1)**(D(3)/2)
Eout=D(2)/3*((D(3)/29)**(D(3)/2)+P**(D(3)/2))
assert D('.98')<a2<1 and D('.28')<P<D('.283')
assert Eout>49*Ein and reverse<D('1e-70')
# True full-ball residual projection and pointwise skew representation.
random.seed(20261012)
residual_cases=0;max_res_error=0.;max_skew_error=0.;max_cubic_violation=0.
for dimension in (4,8,14):
    c=[1.]+[0.]*(dimension-1)
    for _ in range(240):
        z=[random.uniform(-2,2) for _ in range(dimension)]
        # Realification of u=e1, complex projection occupies first two entries.
        ss=sum(x*x for x in z);alpha2=z[0]**2+z[1]**2
        q=math.sqrt(max(0.,ss*ss+1-2*alpha2))
        g=[2*(ss*x-(x if i<2 else 0.))/math.sqrt(q) for i,x in enumerate(z)]
        G=math.sqrt(sum(x*x for x in g));p=[random.uniform(-.1,.1) for _ in z]
        P=math.sqrt(sum(x*x for x in p));nu=[x/G for x in g]
        pg=sum(x*y for x,y in zip(p,nu));perp=[x-pg*y for x,y in zip(p,nu)]
        pn=math.sqrt(sum(x*x for x in perp))
        efactor=min(10.,5*G/pn) if pn else 0.
        e=[-efactor*x for x in perp]
        actual=P+sum((g[i]+10*p[i]+e[i])**2 for i in range(dimension))
        formula=P+(G+10*pg)**2+max(10*pn-5*G,0.)**2
        max_res_error=max(max_res_error,abs(actual-formula)/max(1.,formula))
        eg=sum(x*y for x,y in zip(e,g))
        Kg=[(e[i]*G*G-g[i]*eg)/(G*G) for i in range(dimension)]
        max_skew_error=max(max_skew_error,max(abs(Kg[i]-e[i]) for i in range(dimension)))
        ell=math.sqrt(sum((z[i]-c[i])**2 for i in range(dimension)))
        bound=sum(g[i]*(z[i]-c[i]) for i in range(dimension))+2/(3*math.sqrt(3))*ell**3
        max_cubic_violation=max(max_cubic_violation,-bound)
        residual_cases+=1
assert max_res_error<3e-14 and max_skew_error<3e-14 and max_cubic_violation==0.
# Polarization normalization and cross-sign convention.
polarization_cases=0
for _ in range(100):
    aa=complex(random.uniform(-2,2),random.uniform(-2,2));bb=complex(random.uniform(-2,2),random.uniform(-2,2))
    real=(abs(aa+bb)**2-abs(aa)**2-abs(bb)**2)/2
    imag=(abs(aa+1j*bb)**2-abs(aa)**2-abs(bb)**2)/2
    assert abs(real-(aa*bb.conjugate()).real)<1e-13
    assert abs(imag-(aa*bb.conjugate()).imag)<1e-13
    polarization_cases+=1
# Larger complete window: three absorptions, inf-EB and full budget.
large_R=Q(1,10000); large_root_R=Q(1,100)
assert 54+353430*large_R<Q(90)
assert 2*(54+353430*large_R)+2*large_R<180
assert 180*large_R<Q(135,1000)**2
assert 1+11*Q(135,1000)*181<270
absorption_margins=[]
for p_bound, six_l, g_bound, cauchy, next_p in (
    (180,Q(81,100),270,Q(935,1000),36),
    (36,Q(36,100),26,Q(589,1000),1),
    (1,Q(6,100),Q(122,100),Q(468,1000),Q(1,2))):
    assert Q(26,121)+six_l**2<cauchy**2
    margin=(1-six_l)*next_p-cauchy-six_l*g_bound**2*large_R
    assert margin>0
    absorption_margins.append(str(margin))
assert absorption_margins[0]=='1/10000'
assert Q(122,100)**2*large_R+Q(1,2)<Q(501,1000)
assert Q(1,2)+Q(3,2)**2*large_R<Q(501,1000)
assert 2<Q(142,100)**2 and Q(142,100)+2*large_root_R<Q(3,2)
assert 100*Q(1,2)*large_R<Q(1,11)**2
large_compat=Q(11,40)*(Q(3,2)+large_root_R)**2
assert large_compat==Q(250811,400000)<Q(3,4)
assert 2*large_R+6*large_root_R==Q(301,5000)<Q(1,2)-large_R
assert (large_R+Q(3,2)*large_root_R)/2==Q(151,20000)<1
assert Q(1,2)<Q(7072,10000)**2
assert Q(1,2)*Q(7072,10000)+Q(122,100)**3*Q(1,10**6)<Q(354,1000)
# Dense microinterval and artificial KL-energy constants, not subgradient proof.
assert 1/(1-Q(1,128))<Q(4,3)
assert Q(4,3)/32==Q(1,24)
assert Q(23,24)-Q(501,1000)>Q(9,10)*Q(501,1000)
# Sharp full zero-fiber boundary, both complex signs and actual reverse input.
critical_cases=[]; critical_reverse=D(0)
mm=D(2)/(3*D(3).sqrt())
for eta in map(D,('0','1','-1','2','-2','5','-5','10','-10','.5','-.5')):
    dd=eta*eta+4; dd32=dd*dd.sqrt(); aa=mm*(1+eta*eta)
    zz=[(eta*eta-2)/dd,3*eta/dd]
    pp=[-18/dd32,9*eta/dd32]
    ell=norm([zz[0]-1,zz[1]]); pnorm=norm(pp)
    qq=1-dot(zz,zz)
    gg=[-2*qq.sqrt()*v for v in zz]
    ee=[-eta*gg[1],eta*gg[0]]
    rev=norm([gg[i]+ee[i]+aa*pp[i] for i in range(2)])
    kin=norm([pp[i]/pnorm.sqrt()-(zz[i]-(1 if i==0 else 0)) for i in range(2)])
    err=max(rev,kin,abs(dot(ee,gg)),abs(norm(ee)-abs(eta)*norm(gg)),abs(pnorm-9/dd))
    assert err<D('1e-65')
    critical_reverse=max(critical_reverse,err)
    critical_cases.append({'eta':str(eta),'A_boundary':str(aa),'z':[str(v) for v in zz],'P':str(pnorm),'reverse_error':str(err)})
assert mm*26<11 and mm*26>10
assert D(26).sqrt()<6<mm*26

out={'python':sys.version.split()[0],'seed':20261012,'decimal_digits':80,'tuple':{'R':'1e-12','lambda':1,'gamma':.5,'L':1.5,'psi':'1.1t^2','bar_t':1,'kappa':.75,'input_domain':'dist(a,M)<1/2','relation':'complete orthogonal-feedback ball'},'strict_fraction_bounds':{'P_coefficient_upper':str(p_coefficient),'compatibility_upper':str(compat),'energy_quadratic_upper':str(energy_quadratic),'energy_new_geometry_upper':str(Q(471,1000)*Q(687,1000)+(1+11*Q(471,1000))**3*Tmax)},'large_window':{'R':'1e-4','absorption_margins':absorption_margins,'compatibility':str(large_compat),'distance_upper':'.501','step_squared_coefficient_upper':'.501','budget_upper':'.0602','artificial_KL_H1_alpha':'.9'},'critical_zero_fiber_cases':critical_cases,'critical_zero_fiber_maximum_reverse_error':str(critical_reverse),'auxiliary_predecessor_tuples':aux,'H1_two_sided_chord_cases':chord_cases,'sharp_reverse_cases':sharp,'sharp_ratio_theory':str(D(26).sqrt()/11),'maximum_decimal_reverse_error':str(max_reverse),'global_energy_witness':{'input_radius_squared':str(a2),'P':str(witness_P),'Ein':str(Ein),'Eout':str(Eout),'ratio':str(Eout/Ein),'reverse_error':str(reverse),'scope':'outside certified local window'},'full_ball_residual_cases':residual_cases,'maximum_residual_relative_error':max_res_error,'maximum_skew_representation_error':max_skew_error,'maximum_cubic_violation':max_cubic_violation,'polarization_cases':polarization_cases,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite boundary arithmetic, exact reverse-defined witnesses and deterministic samples. Full fibers, all-feedback/all-input quantifiers, sharp bounds, infinite orbits, limiting subgradients/KL and smooth/strong-chain-rule nonexistence use canonical analytic proofs.'}
Path(__file__).with_name('results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('full_ball_residual_cases','polarization_cases','maximum_decimal_reverse_error','maximum_residual_relative_error','script_sha256')},indent=2))
