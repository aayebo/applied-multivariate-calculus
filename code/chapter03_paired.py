"""Chapter 3 paired numerical and symbolic calculations; original instructional example."""
import numpy as np
import sympy as sp
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

out=Path(__file__).resolve().parent.parent/'figures'
xg=np.linspace(-2,2,120); yg=np.linspace(-2,2,120)
X,Y=np.meshgrid(xg,yg); Z=20+3*X**2+2*Y**2
fig,ax=plt.subplots(); cs=ax.contour(X,Y,Z,levels=[22,24,26,30,34]); ax.clabel(cs)
ax.set_aspect('equal');ax.set_xlabel('x (m)');ax.set_ylabel('y (m)');fig.tight_layout()
fig.savefig(out/'chapter03_paired_temperature.pdf');plt.close(fig)
assert 20+3*1**2+2*(-2)**2==31
x,y=sp.symbols('x y',real=True)
f=sp.exp(x*y)+x**3*y
fx,fy=sp.diff(f,x),sp.diff(f,y)
fnum=sp.lambdify((x,y),f,'numpy')
h=1e-5
numeric_x=(fnum(1+h,.5)-fnum(1-h,.5))/(2*h)
assert abs(numeric_x-float(fx.subs({x:1,y:.5})))<1e-8
u,v=sp.symbols('u v',real=True)
F=sp.Matrix([u*u-v*v,2*u*v]);J=F.jacobian([u,v])
assert sp.simplify(J.det()-4*(u*u+v*v))==0
assert J.det().subs({u:1,v:2})==20
Rg,n,V,Temp=8.314,1.,.025,300.
P=lambda vol,t:n*Rg*t/vol
dV,dT=.0001,2.
linear=(-n*Rg*Temp/V**2)*dV+(n*Rg/V)*dT
actual=P(V+dV,Temp+dT)-P(V,Temp)
assert abs(linear-266.048)<1e-8
assert abs(actual-linear)<10
print('Gradient at (1,.5):',fx.subs({x:1,y:.5}),fy.subs({x:1,y:.5}))
print('Numerical x partial:',numeric_x)
print('Pressure predicted:',linear,'actual:',actual,'difference:',actual-linear)
print('All Chapter 3 Python checks passed')
