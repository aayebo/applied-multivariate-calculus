import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import minimize, minimize_scalar
f=lambda x,y:np.exp(x+2*y)
t1=lambda x,y:1+x+2*y
t2=lambda x,y:1+x+2*y+.5*(x+2*y)**2
print(f(.1,.05),t1(.1,.05),t2(.1,.05))
h=np.logspace(-3,-1,25)
plt.loglog(h,abs(f(h,h)-t2(h,h)),"o-")
plt.xlabel("Step size");plt.ylabel("Quadratic error")
plt.savefig("figures/ch4_r_python_error.pdf");plt.close()
x,y=sp.symbols("x y")
q=(x-2)**2+4*(y+1)**2+3
print([sp.diff(q,z) for z in (x,y)])
print(sp.hessian(q,(x,y)))
fun=lambda p:(p[0]-2)**2+4*(p[1]+1)**2+3
jac=lambda p:np.array([2*(p[0]-2),8*(p[1]+1)])
fit=minimize(fun,[0,0],jac=jac,method="BFGS")
print(fit.x,fit.fun)
assert np.allclose(fit.x,[2,-1],atol=1e-5)
nonconvex=lambda p:(p[0]**2-1)**2+p[1]**2
starts=[[-2,1],[2,1],[-.7,-1],[.7,-1]]
print([minimize(nonconvex,s,method="BFGS").x for s in starts])
res=minimize_scalar(lambda t:-(np.cos(t)+2*np.sin(t)),bounds=(0,2*np.pi),method="bounded")
print("disk maximum",-res.fun,"exact",np.sqrt(5))
res=minimize_scalar(lambda x:-x*(10-x),bounds=(0,10),method="bounded")
print("fixed-sum optimum",res.x,10-res.x,-res.fun)
xx=np.array([0,1,2,3]); yy=np.array([1,2,2,4])
X=np.column_stack([np.ones_like(xx),xx])
beta=np.linalg.lstsq(X,yy,rcond=None)[0]
print("least squares",beta)
assert np.allclose(beta,[.9,.9])
P=lambda p:12*p[0]+10*p[1]-p[0]**2-2*p[1]**2-p[0]*p[1]
fit=minimize(lambda p:-P(p),[1,1],method="BFGS")
print("production optimum",fit.x,"exact",[38/7,8/7])
assert np.allclose(fit.x,[38/7,8/7],atol=1e-4)
