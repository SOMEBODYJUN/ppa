#!/usr/bin/env python3
"""Finite arithmetic/back-substitutions; analytic proofs carry full quantifiers."""
from contextlib import redirect_stdout
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import io
import json
import math
import platform

import numpy as np


def inverse_scale(u):
    # Inverse of B(t)=t+sqrt(t); rationalized to avoid small-u cancellation.
    return (2*u/(1+math.sqrt(1+4*u)))**2


def W(t):
    return math.sqrt(abs(t)+Q(9, 16)*t*t)


def full_output(x, t, first_error):
    y = np.array([x[0]-first_error+math.sqrt(abs(t)), .25*t])
    w = np.array([-math.sqrt(abs(t)), .75*t])
    defect = x-y-w
    assert np.linalg.norm(defect-np.array([first_error, x[1]-t])) < 2e-13
    return y, w, defect


def main():
    result = {'scope': 'finite checks only; universal conclusions are analytic',
              'python': platform.python_version(), 'numpy': np.__version__,
              'seed': 'none; deterministic grids', 'decimal_precision': 100,
              'binary_float': 'IEEE binary64', 'tolerance': 2e-12}
    with localcontext() as context:
        context.prec = 100
        rho, radius, cap, theta = D('.01'), D('.001'), D('.05'), D('.8')
        qcap = (2*cap/(1+(1+4*cap).sqrt()))**2
        b_radius = radius+radius.sqrt()
        k0 = D('.25')*(1+rho.sqrt())**2
        assert b_radius < cap
        assert radius+theta*qcap < rho
        assert k0 < D('.5') < 1
        assert abs(qcap+qcap.sqrt()-cap) < D('1e-98')
        result['C275_common_window'] = {
            'rho': str(rho), 'R': str(radius), 'u_cap': str(cap),
            'theta': str(theta), 'kappa0': str(k0), 'kappa': '.5',
            'B_R': str(b_radius), 'Q_cap': str(qcap),
            'trust_sum': str(radius+theta*qcap)}
    # Joint inverse rule: all e_1 values at the full horizontal-fiber endpoints.
    cap = .05
    tcap = 2*cap**2/(1+math.sqrt(1+4*.75**2*cap**2))
    count, max_ratio, max_lower_excess = 0, 0., 0.
    for normal in (0., 1e-12, -1e-12, .0005, -.0005, .001, -.001):
        x = np.array([.13, normal])
        ts = sorted(set(np.linspace(-tcap, tcap, 501).tolist()+[0.,normal]))
        for t in ts:
            u = W(t)
            if u > cap*(1+1e-13):
                continue
            lower = inverse_scale(u)
            psi = .25*u*u
            budget = min(.8*lower, lower-psi/.5)
            second_error = normal-t
            if budget < abs(second_error):
                continue
            half = math.sqrt(max(0., budget**2-second_error**2))
            for first_error in (-half, -.5*half, 0., .5*half, half):
                y, w, defect = full_output(x,t,first_error)
                error = float(np.linalg.norm(defect))
                assert error <= budget+2e-12
                assert 0 <= lower-error+2e-12 <= abs(normal)+2e-12
                assert abs(y[1]) <= psi+2e-12
                assert psi <= .5*(lower-error)+2e-12
                assert abs(y[1]) <= .5*abs(normal)+2e-12
                if normal:
                    max_ratio=max(max_ratio,abs(y[1]/normal))
                else:
                    assert t==0 and np.linalg.norm(y-x)==0
                max_lower_excess=max(max_lower_excess,lower-error-abs(normal))
                count+=1
    result['C275_joint_rule_full_interval_checks'] = {
        'accepted_witnesses': count, 'max_normal_ratio': max_ratio,
        'max_lower_bound_excess': max_lower_excess,
        'cap_parameter_from_inverse_W': tcap}

    # A genuinely set-valued F: the normal cone to R x {0}.
    # Its true residual on every graph base is 0, despite nonzero selected w.
    count = 0
    for normal in (0., .01, -.01, .02, -.02):
        x=np.array([.2,normal])
        for selected in sorted(set(np.linspace(-.1,.1,401).tolist()+[normal,0.])):
            u=abs(selected)
            budget=.5*u  # Q=u, psi=.25u, kappa=.5, theta=.8
            second_error=normal-selected
            if abs(second_error)>budget:
                continue
            half=math.sqrt(max(0.,budget**2-second_error**2))
            for first_error in (-half,0.,half):
                y=np.array([x[0]-first_error,0.])
                w=np.array([0.,selected])
                defect=x-y-w
                assert np.linalg.norm(defect)<=budget+2e-12
                assert u-np.linalg.norm(defect)<=abs(normal)+2e-12
                if normal==0:
                    assert selected==0 and np.linalg.norm(y-x)==0
                count+=1
    result['set_valued_graph_checks']={
        'operator':'normal cone to R x {0}', 'accepted_witnesses':count,
        'true_residual_at_all_outputs':0, 'selected_norm_can_be_positive':True}

    # Generalized inverse across a jump: infimum can be unattained.
    def B_jump(t):
        return t+(.3 if t>.2 else 0.)
    def Q_jump(u):
        return u if u<=.2 else (.2 if u<=.5 else u-.3)
    for u in (0.,.1,.2,.3,.4,.5,.6):
        qi=Q_jump(u)
        for t in np.linspace(0,.8,801):
            if u<=B_jump(float(t)):
                assert qi<=t+2e-12
    for t in np.linspace(0,.8,801):
        assert Q_jump(B_jump(float(t))) <= t+2e-12
    assert .4>B_jump(Q_jump(.4))
    result['inverse_jump']={'u':.4,'Q_u':.2,'B_Q_u':.2,
                            'infimum_attained':False}

    # C276 exact critical full fiber, safe, endpoint, absorption, and far cases.
    T=Q(1,100)
    eta_conv=Q(3,4)/(1+Q(9,16)*T)
    eta_abs=1/(1+Q(9,16)*T)
    assert eta_conv<Q(3,4)<eta_abs
    result['exact_frontier_arithmetic']={
        'T':str(T), 'eta_conv':str(eta_conv), 'eta_abs':str(eta_abs),
        'asymptotic_power_coefficient':'3/4',
        'normalized_EB_coefficient':'3'}
    for t in (1e-8,-1e-8,.01,-.01):
        x=np.array([0.,.25*t])
        y,w,e=full_output(x,t,0.)
        assert np.linalg.norm(e)<=.75*np.linalg.norm(w)**2+2e-14
        assert y[1]==x[1] and y[0]>x[0]
    x=np.zeros(2);y,w,e=full_output(x,16.,0.)
    assert np.linalg.norm(e)==16 and np.dot(w,w)==160
    assert np.linalg.norm(e)==.1*np.dot(w,w)
    result['far_zero_input']={'input':[0,0],'output':y.tolist(),
                             'defect_norm':float(np.linalg.norm(e)),
                             'selected_squared_norm':float(np.dot(w,w))}

    # Exact orbit and conjugacy; verified on zero and both signs.
    coefficient=1/(1-math.sqrt(.25))
    for t0 in (0.,.01,-.01):
        state=np.array([.3,t0])
        for k in range(13):
            closed=np.array([.3+coefficient*math.sqrt(abs(t0))*(1-.25**(.5*k)),
                             .25**k*t0])
            assert np.linalg.norm(state-closed)<2e-12
            hstate=np.array([state[0]+coefficient*math.sqrt(abs(state[1])),state[1]])
            next_state=np.array([state[0]+math.sqrt(abs(state[1])),.25*state[1]])
            hnext=np.array([next_state[0]+coefficient*math.sqrt(abs(next_state[1])),
                            next_state[1]])
            assert np.linalg.norm(hnext-np.array([hstate[0],.25*hstate[1]]))<2e-12
            state=next_state
    result['exact_orbit_conjugacy']='passed for zero and both signs, k=0..12'

    # Natural cyclic benchmark; numerical diagonal enumeration and sharp attainer.
    P=np.array([[0.,1.,0.],[0.,0.,1.],[1.,0.,0.]])
    alpha,c=1.,3.
    mu=(math.sqrt(4*alpha*alpha+c*c)-c)/2
    minimum=math.inf
    for d1 in (1.,1.1,2.,10.,1000.):
        for d2 in (1.,1.1,2.,10.,1000.):
            for d3 in (1.,1.1,2.,10.,1000.):
                least=float(np.linalg.svd(np.diag([d1,d2,d3])+c*P,compute_uv=False)[-1])
                assert least>=mu-2e-12
                minimum=min(minimum,least)
    lam=5.
    q=(math.sqrt(4*(1+lam)**2+9*lam**2)+3*lam)/(2*(1+lam)**2)
    sigma=.25
    kappa=q*(1+sigma)/(1-q*sigma)
    assert kappa<1 and sigma<(1-q)/(2*q)
    result['cyclic_game_arithmetic']={'diagonal_cases':125,'lower_bound_mu':mu,
                                     'observed_min_sigma':minimum,'lambda':lam,
                                     'sharp_global_q':q,'sufficient_sigma':sigma,
                                     'all_output_kappa':kappa}
    # Run independent standard-library frontier verifier, preserving its stdout.
    previous=Path(__file__).parents[1]/'inexact_forcing_attack/check_frontier.py'
    spec=importlib.util.spec_from_file_location('frontier',previous)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    buffer=io.StringIO()
    with redirect_stdout(buffer):
        module.main()
    result['independent_frontier_verifier_stdout']=buffer.getvalue()
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['frontier_helper_sha256']=hashlib.sha256(previous.read_bytes()).hexdigest()
    Path(__file__).with_name('output.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'passed','joint_rule_witnesses':
                      result['C275_joint_rule_full_interval_checks']['accepted_witnesses'],
                      'set_valued_witnesses':count,'diagonal_cases':125,
                      'output':'research/code/inexact_ppa/output.json'},indent=2))


if __name__=='__main__':
    main()
