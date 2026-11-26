import numpy as np

def heat_ftcs(N=41, alpha=0.1, T=0.2):
    x=np.linspace(0,1,N); h=x[1]-x[0]
    steps=int(np.ceil(T*alpha/(0.4*h*h)))
    dt=T/steps; r=alpha*dt/(h*h)
    u=np.sin(np.pi*x)
    for _ in range(steps):
        v=u.copy(); v[1:-1]=u[1:-1]+r*(u[:-2]-2*u[1:-1]+u[2:]); u=v
    exact=np.exp(-alpha*np.pi**2*T)*np.sin(np.pi*x)
    return h,float(np.max(np.abs(u-exact))),r

if __name__=='__main__':
    values=[heat_ftcs(N) for N in (21,41,81,161)]
    print('h, maximum error, stability number:')
    for v in values: print(v)
    assert all(0<v[2]<=0.5 for v in values)
    assert all(values[i+1][1]<values[i][1] for i in range(3))
    order=np.polyfit(np.log([v[0] for v in values]),np.log([v[1] for v in values]),1)[0]
    print('estimated convergence order:',order)
    assert 1.8<order<2.2
