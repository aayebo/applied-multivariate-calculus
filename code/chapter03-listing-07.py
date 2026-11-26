import numpy as np
import sympy as sp
u,v=sp.symbols('u v',real=True)
F=sp.Matrix([u*u-v*v,2*u*v]); J=F.jacobian([u,v])
assert sp.simplify(J.det()-4*(u*u+v*v))==0
assert J.det().subs({u:1,v:2})==20
Rg,n,V,Temp=8.314,1.,.025,300.
P=lambda v,t:n*Rg*t/v
dV,dT=.0001,2.
linear=(-n*Rg*Temp/V**2)*dV+(n*Rg/V)*dT
actual=P(V+dV,Temp+dT)-P(V,Temp)
print('linear, actual, error:',linear,actual,actual-linear)
t=10.**(-np.arange(1,7))
print('axis:',np.zeros_like(t),'diagonal:',np.ones_like(t)/2)
