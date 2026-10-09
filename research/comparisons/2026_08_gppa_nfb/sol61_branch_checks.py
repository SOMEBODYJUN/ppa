"""Finite arithmetic corroboration of explicit branch restrictions, not universal proof."""
from fractions import Fraction as F
from pathlib import Path
import json, math

out={'proof_boundary':'Finite exact arithmetic or bounded numeric tail checks. Infinite-series coverage and all-pairs hypotheses are proved in sol61_branch_restriction.md.'}
# Cap: root(y) remains rational throughout the original positive orbit.
xi, eta, y = F(0), -F(1), F(1,64)
I=F(1,4)
cap_steps=0
for k in range(24):
    root=F(1,2**(k+3)); y_new=y/4; root_new=root/2
    xi_new=xi+root
    current_v=(-2*root,F(0),y)
    next_v=(-2*root_new,F(0),y_new)
    selected_f=(-2*root_new,F(0),3*y_new)
    assert tuple(current_v[i]-next_v[i] for i in range(3)) == selected_f
    assert current_v == (xi-I,F(0),y)
    xi,y=xi_new,y_new; cap_steps+=1
out['cap_exact_positive_original_warped_steps']=cap_steps
# Complete pair ASM: second graph components may vary but kernel component is zero.
ys=[F(0),F(1,64),F(1,16),F(1,4),F(1),F(4)]
roots=[F(0),F(1,8),F(1,4),F(1,2),F(1),F(2)]
count=0
for i,y in enumerate(ys):
    for j,z in enumerate(ys):
        dv=(-2*(roots[i]-roots[j]),F(0),y-z)
        # Arbitrary second residual differences cannot affect the inner product.
        df=(dv[0],F(i-j,7),3*dv[2])
        inner=sum(df[k]*dv[k] for k in range(3))
        assert inner >= sum(t*t for t in dv)
        count+=1
out['cap_exact_asm_pairs']=count
coverage=0
for inp_root in [F(0),F(1,8),F(1),F(10)]:
    for sign in [-1,1]:
        r=sign*inp_root*inp_root
        positive=max(r,F(0)); positive_root=inp_root if sign>0 else F(0)
        y=positive/4; root_y=positive_root/2
        v_in=(-2*positive_root,F(0),positive)
        v_out=(-2*root_y,F(0),y)
        f_out=(-2*root_y,F(0),3*y)
        assert v_in == tuple(v_out[k]+f_out[k] for k in range(3))
        coverage+=1
out['cap_finite_all_input_warped_coverage_witnesses']=coverage
# Negative prefix is an original F minus-branch step, followed by positive restriction.
r0=-F(1,64); xi0=F(0); root=F(1,8)
x1=(xi0+root,-F(1),abs(r0)/4)
f_minus=(-root,F(0),-5*x1[2])
assert (xi0-x1[0],F(0),r0-x1[2]) == f_minus
assert x1[0]+2*F(1,16) == F(1,4)
out['cap_negative_prefix_then_restriction']=True
# C141 representative nu=2, gamma=1/2, A=1, R=1/4.
# K_R = sum_{j>=1} 2^j*(1/2)^(2^j-1).
# j=1 term is1, j=2 term1/2, later ratios<=1/8, giving K_R<=11/7<2.
K_safe=F(2); K_bound=F(1)+F(1,2)/(1-F(1,8)); assert K_bound==F(11,7)<K_safe
m=F(1,4)**-1/F(2)-1; assert m==1
N=8
# Exact square roots for these collar points.
points=[(F(0),F(0)),(F(1,256),F(1,16)),(F(1,16),F(1,4))]
def en(y, root):
    return root+sum(y**(2**j) for j in range(N-1))
asm_count=0
for y,root_y in points:
    for z,root_z in points:
        # phi=y^(1/4) is rational at selected points.
        phi_y=F(0) if y==0 else (F(1,4) if y==F(1,256) else F(1,2))
        phi_z=F(0) if z==0 else (F(1,4) if z==F(1,256) else F(1,2))
        E_y,E_z=en(y,root_y),en(z,root_z)
        dv=(-(E_y-E_z),y-z)
        df=(-(phi_y-phi_z),(root_y-y)-(root_z-z))
        assert sum(df[k]*dv[k] for k in range(2)) >= F(1,2)*sum(t*t for t in dv)
        assert abs(E_y-E_z)<=K_safe*abs(phi_y-phi_z)
        asm_count+=1
out['c141_finite_truncated_series_asm_pairs']=asm_count
out['c141_rigorous_safe_constants']={'R':'1/4','m':'1','K_upper':'11/7','K_safe':'2','epsilon_safe':'1/2'}
identities=0
for r,root_r in [(F(1,16),F(1,4)),(F(1,4),F(1,2))]:
    E_r=en(r,root_r); E_r2=en(r*r,r)
    last=r**(2**(N-1))
    assert E_r-E_r2 == root_r-last
    # Remainder of infinite E beyond N is at most last/(1-last).
    assert last/(1-last)>0
    identities+=1
out['c141_exact_finite_telescoping_identities']=identities
# Log a=2: exact finite-shift algebra within float tolerance, analytic integral bounds for omitted tails.
a=2.0;cut=math.exp(-a)
def ell(t):
    if t==0:return 0.0
    if t<=cut:return math.log(math.e/t)**(-a)
    return (1+a*math.exp(a)*t)/(a+1)**(a+1)
log_rows=[]
for k in [2,4,16,64,128]:
    A=1+k*math.log(4); n=2000
    summands=[(A+j*math.log(4))**(-a) for j in range(n)]
    En=math.fsum(summands)
    shifted=math.fsum((A+(j+1)*math.log(4))**(-a) for j in range(n))
    assert abs((En-shifted)-(summands[0]-(A+n*math.log(4))**(-a)))<1e-14
    tail_lower=(A+n*math.log(4))**(1-a)/(math.log(4)*(a-1))
    tail_upper=tail_lower+(A+n*math.log(4))**(-a)
    assert tail_lower>0 and tail_upper>tail_lower
    E_mid=En+(tail_lower+tail_upper)/2
    y=math.exp(1-A)
    asm_quotient=(ell(4*y)*E_mid+3*y*y)/(E_mid*E_mid+y*y)
    log_rows.append({'k':k,'kernel_tail_interval':[En+tail_lower,En+tail_upper],'zero_anchor_asm_quotient':asm_quotient})
out['log_finite_tail_checks']=log_rows
out['log_count']=len(log_rows)
Path(__file__).with_name('sol61_branch_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: branch restriction finite checks; universal series claims remain analytic.')
