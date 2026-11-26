"""Chapter 8: checked examples for Multivariable Calculus Using Python."""
import numpy as np
import sympy as sp
from scipy.integrate import quad

x, t, alpha = sp.symbols('x t alpha', positive=True)
u = sp.exp(-alpha*sp.pi**2*t)*sp.sin(sp.pi*x)
assert sp.simplify(sp.diff(u,t)-alpha*sp.diff(u,x,2)) == 0


def sine_coefficients(f, N, L=1.0):
    return np.array([2/L * quad(lambda z: f(z)*np.sin(n*np.pi*z/L),0,L)[0]
                     for n in range(1,N+1)])


def heat_series(x,t,b,alpha=.1,L=1.):
    n=np.arange(1,len(b)+1)
    return np.sin(np.outer(np.asarray(x),n*np.pi/L)) @ (b*np.exp(-alpha*(n*np.pi/L)**2*t))


def heat_ftcs(f,L=1.,alpha=.1,nx=51,final_time=.2,target_r=.45):
    xx=np.linspace(0,L,nx); h=xx[1]-xx[0]
    nsteps=int(np.ceil(final_time*alpha/(target_r*h*h)))
    dt=final_time/nsteps; r=alpha*dt/(h*h)
    if r>.5: raise ValueError('FTCS stability condition violated')
    y=np.asarray(f(xx),float).copy(); y[0]=y[-1]=0
    for _ in range(nsteps):
        v=y.copy(); v[1:-1]=y[1:-1]+r*(y[:-2]-2*y[1:-1]+y[2:]); y=v
    return xx,y,r


def laplace_jacobi(n=41,tolerance=1e-7,max_steps=100000):
    xx=np.linspace(0,1,n); u=np.zeros((n,n)); u[-1,:]=np.sin(np.pi*xx)
    for k in range(max_steps):
        v=u.copy()
        v[1:-1,1:-1]=.25*(u[2:,1:-1]+u[:-2,1:-1]+u[1:-1,2:]+u[1:-1,:-2])
        if np.max(np.abs(v-u))<tolerance: return xx,v,k+1
        u=v
    raise RuntimeError('Jacobi iteration did not converge')

if __name__=='__main__':
    b=sine_coefficients(lambda z:z*(1-z),12)
    assert abs(b[0]-8/np.pi**3)<1e-10
    assert abs(b[1])<1e-10
    xx,y,r=heat_ftcs(lambda z:np.sin(np.pi*z))
    exact=np.exp(-.1*np.pi**2*.2)*np.sin(np.pi*xx)
    err=np.max(np.abs(y-exact))
    assert err<1e-3 and r<=.5
    xx,v,k=laplace_jacobi()
    assert np.isfinite(v).all() and v[len(xx)//2,len(xx)//2]>0
    print('SymPy PDE residual: 0')
    print('Heat error:',err,'stable r:',r)
    print('Laplace iterations:',k,'center:',v[len(xx)//2,len(xx)//2])
    print('Chapter 8 checks passed')
