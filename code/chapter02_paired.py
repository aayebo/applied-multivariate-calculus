"""Chapter 2: paired R/Python computations, verified with Python."""
import numpy as np
import sympy as sp
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

out=Path(__file__).resolve().parent.parent/'figures'
t=np.linspace(0,6*np.pi,500)
x,y,z=2*np.cos(t),2*np.sin(t),t/3
fig,ax=plt.subplots(1,2,figsize=(9,3.5))
ax[0].plot(x,y);ax[0].set_aspect('equal');ax[0].set_title('Top view')
ax[1].plot(t,z);ax[1].set_title('Height')
fig.tight_layout();fig.savefig(out/'ch2_helix_projections.png',dpi=180);plt.close(fig)
s=sp.symbols('s',real=True)
r=sp.Matrix([s**2,3*s,2]);v=r.diff(s)
assert v.subs(s,2)==sp.Matrix([4,3,0])
assert sp.sqrt(v.dot(v)).subs(s,2)==5
a,b=2.0,1.0/3.0
L_num=quad(lambda q:np.sqrt(a*a+b*b),0,2*np.pi)[0]
L_exact=2*np.pi*np.sqrt(a*a+b*b)
assert abs(L_num-L_exact)<1e-11
assert np.isclose(a/(a*a+b*b),18/37)
assert np.isclose(b/(a*a+b*b),3/37)
x,y,z=3.,4.,5.
rho=np.sqrt(x*x+y*y+z*z);phi=np.arccos(z/rho)
assert np.isclose(rho*np.sin(phi)*np.cos(np.arctan2(y,x)),x)
area=quad(lambda q:2*np.pi*q*np.sqrt(1+4*q*q),0,1)[0]
exact=np.pi*(5**1.5-1)/6
assert np.isclose(area,exact)
print('Chapter 2 Python paired checks passed. Area:',area)
