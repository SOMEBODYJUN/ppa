"""Independent hostile checks; no functions imported from the proposing script.

LP tests are evidence checks, not substitutes for the analytic audit proofs.
Run: python output/verify_markov_conditional_repair_independent.py
"""
from itertools import product
import numpy as np
from scipy.optimize import linprog


def transport(p, q, cost):
    n, m = cost.shape
    rows = np.kron(np.eye(n), np.ones((1, m)))
    cols = np.tile(np.eye(m), (1, n))
    ans = linprog(cost.ravel(), A_eq=np.vstack((rows, cols)),
                  b_eq=np.r_[p, q], bounds=(0, None), method="highs")
    assert ans.success
    return ans.fun


def conditional_table(law, states):
    ans = np.zeros((len(states), states.shape[1]))
    for i in range(states.shape[1]):
        for j, x in enumerate(states):
            mask = np.all(np.delete(states, i, axis=1) == np.delete(x, i), axis=1)
            mass = law[mask].sum()
            ans[j, i] = law[mask & (states[:, i] == 1)].sum()/mass if mass else 0.
    return ans


def gibbs_matrix(conditional, states, probs):
    n, m = states.shape
    result = np.eye(n)*(1-sum(probs))
    for j, x in enumerate(states):
        for i in range(m):
            for bit in (0, 1):
                y = x.copy(); y[i] = bit
                k = np.flatnonzero(np.all(states == y, axis=1))[0]
                result[j, k] += probs[i]*(conditional[j, i] if bit else 1-conditional[j, i])
    return result


def independent_product_checks():
    states = np.array(list(product((0, 1), repeat=2)))
    cost = ((states[:, None, :]-states[None, :, :])**2).sum(axis=2)
    bits = np.array([.3, .7]); probs = np.array([.2, .55])
    beta = np.prod(np.where(states, bits, 1-bits), axis=1)
    kernel = gibbs_matrix(np.tile(bits, (4, 1)), states, probs)
    count = 0
    for a, b, c in product(range(9), repeat=3):
        if a+b+c > 8:
            continue
        mu = np.array([a,b,c,8-a-b-c])/8
        defect = (mu[:, None]*abs(conditional_table(mu, states)-bits)).sum(axis=0)
        e = transport(mu, beta, cost)
        ep = transport(mu@kernel, beta, cost)
        residual = defect@probs
        assert e <= residual/min(probs)+1e-10
        assert ep <= (1-min(probs))*e+1e-10
        count += 1
    print("Independent exhaustive binary-simplex laws:", count, "PASS")


def dependent_checks():
    rng = np.random.default_rng(11904)
    states = np.array(list(product((0, 1), repeat=3)))
    spins = 2*states-1
    interaction = np.array([[0,.12,-.08],[.12,0,.1],[-.08,.1,0]])
    beta = np.exp(np.einsum('ni,ij,nj->n', spins, interaction, spins)/2)
    beta /= beta.sum()
    cond_beta = conditional_table(beta, states)
    C = np.zeros((3,3))
    for i,j in product(range(3), repeat=2):
        if i == j:
            continue
        for k,x in enumerate(states):
            y=x.copy(); y[j]=1-y[j]
            ell=np.flatnonzero(np.all(states==y,axis=1))[0]
            C[i,j]=max(C[i,j],abs(cond_beta[k,i]-cond_beta[ell,i]))
    assert max(abs(np.linalg.eigvals(C))) < 1
    probs=np.array([.15,.3,.55]); B=np.eye(3)-np.diag(probs)+np.diag(probs)@C
    weights=np.ones(3)@np.linalg.inv(np.eye(3)-B)
    theta=max((weights-1)/weights)
    cost=(((states[:,None,:]-states[None,:,:])**2)*weights).sum(axis=2)
    kernel=gibbs_matrix(cond_beta,states,probs)
    for _ in range(150):
        mu=rng.dirichlet(np.full(8,.4))
        r=(mu[:,None]*abs(conditional_table(mu,states)-cond_beta)).sum(axis=0)
        e=transport(mu,beta,cost)
        ep=transport(mu@kernel,beta,cost)
        assert e <= weights@np.linalg.solve(np.eye(3)-C,r)+1e-9
        assert ep <= theta*e+1e-9
    print("Independent interacting Ising conditional EB/contraction: PASS; theta",theta)


def sqrt_spd(a):
    eig,vec=np.linalg.eigh(a)
    return (vec*np.sqrt(np.maximum(eig,0)))@vec.T


def gaussian_checks():
    rng=np.random.default_rng(2209)
    max_ratio=0.
    for _ in range(100):
        n=4; z=rng.normal(size=(n,n)); Q=z.T@z+np.eye(n)
        p=rng.dirichlet(np.ones(n)); D=np.diag(p/np.diag(Q)); qhalf=sqrt_spd(Q)
        eig,vec=np.linalg.eigh(qhalf@D@qhalf); zeta=eig[0]
        delta=np.linalg.solve(qhalf,vec[:,0])
        e_mean=delta@Q@delta; r_mean=delta@Q@D@Q@delta
        assert abs(r_mean/zeta-e_mean)<1e-9
        # Test the stronger, sharp EB on arbitrary Gaussian means/covariances.
        z=rng.normal(size=(n,n)); covariance=z.T@z+.2*np.eye(n)
        precision=np.linalg.inv(covariance); delta=rng.normal(size=n)
        normal_cov=qhalf@covariance@qhalf
        w2=delta@Q@delta+np.trace(normal_cov+np.eye(n)-2*sqrt_spd(normal_cov))
        rsq=0.
        for i in range(n):
            v=Q[i]/Q[i,i]-precision[i]/precision[i,i]
            discrepancy=(Q[i]@delta/Q[i,i])**2+v@covariance@v
            discrepancy+=(1/np.sqrt(precision[i,i])-1/np.sqrt(Q[i,i]))**2
            rsq+=p[i]*Q[i,i]*discrepancy
            A=np.eye(n)-np.outer(np.eye(n)[:,i],Q[i])/Q[i,i]
            assert np.linalg.norm(A.T@Q@np.eye(n)[:,i])<1e-10
        assert w2 <= rsq/zeta+1e-8
        max_ratio=max(max_ratio,w2*zeta/rsq)
    print("Independent coupled Gaussian EB sharpness and orthogonality: PASS; random max ratio",max_ratio)


def full_rfi_energy_check():
    us=np.r_[0.,2.**(-np.arange(1,18))]
    rates=np.r_[0.,2.**(-(np.arange(1,18)**2+4*np.arange(1,18)+4))]
    points=np.array([(u,b) for u in us for b in (0,1)])
    worst=0.
    for x,y in product(points,repeat=2):
        norm=np.sum((x-y)**2)
        if norm == 0: continue
        energy=(1-rates.sum())*norm
        for u,a in zip(us[1:],rates[1:]):
            for bit in (0,1):
                tx=x.copy();ty=y.copy()
                if x[0] == u: tx[1]=bit
                if y[0] == u: ty[1]=bit
                energy+=a/2*(np.sum((tx-ty)**2)+np.sum(((x-tx)-(y-ty))**2))
        worst=max(worst,energy/norm-1)
        assert energy <= (1+17/256)*norm+1e-13
    print("Independent full-map RFI energy enumeration: PASS; maximal excess",worst)


if __name__ == '__main__':
    independent_product_checks()
    dependent_checks()
    gaussian_checks()
    full_rfi_energy_check()
    print("ALL INDEPENDENT AUDIT CHECKS PASSED")
