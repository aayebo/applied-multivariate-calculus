"""Chapter 4 verification and computational examples."""
import numpy as np
import sympy as sp
from scipy.optimize import minimize
x,y=sp.symbols('x y',real=True)
f=sp.exp(x)*sp.cos(y)+x*y
H=sp.hessian(f,(x,y));g=sp.Matrix([sp.diff(f,v) for v in (x,y)])
v=sp.Matrix([x,y]);origin={x:0,y:0}
T=sp.expand(f.subs(origin)+(g.subs(origin).T*v)[0]+(v.T*H.subs(origin)*v)[0]/2)
assert sp.simplify(T-(1+x+x*x/2+x*y-y*y/2))==0
assert sp.simplify(sp.diff(f,x,y)-sp.diff(f,y,x))==0
p=np.array([-2.,2.]);alpha=.15
for _ in range(40):p=p-alpha*np.array([2*(p[0]-2),8*(p[1]+1)])
assert np.allclose(p,[2,-1],atol=1e-3)
def objective(v):return (v[0]-2)**2+4*(v[1]+1)**2
def grad(v):return np.array([2*(v[0]-2),8*(v[1]+1)])
r=minimize(objective,[-2,2],jac=grad,method='BFGS')
assert r.success and np.allclose(r.x,[2,-1],atol=1e-5)
xx=np.array([0.,1.,2.,3.]);yy=np.array([1.,2.,2.,4.]);A=np.column_stack([np.ones_like(xx),xx]);beta=np.linalg.lstsq(A,yy,rcond=None)[0]
assert np.allclose(beta,[.9,.9])
assert np.isclose(np.sum((yy-A@beta)**2),.7)
# Check the quadratic resource-allocation example.
assert np.isclose(6*3+4*1-3**2-2*1**2,11)
print('Symbolic, optimization, and least-squares checks passed.')
print('Second-order Taylor polynomial:',T)
print('BFGS optimum:',r.x,'least-squares coefficients:',beta)
