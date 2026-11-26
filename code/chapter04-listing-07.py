import sympy as sp
from scipy.optimize import minimize
x,y=sp.symbols('x y')
q=(x-2)**2+4*(y+1)**2+3
print([sp.diff(q,z) for z in (x,y)])
print(sp.hessian(q,(x,y)))
fun=lambda p:(p[0]-2)**2+4*(p[1]+1)**2+3
jac=lambda p:np.array([2*(p[0]-2),8*(p[1]+1)])
fit=minimize(fun,[0,0],jac=jac,method='BFGS')
print(fit.x,fit.fun)
assert np.allclose(fit.x,[2,-1],atol=1e-5)
