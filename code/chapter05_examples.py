"""Chapter 5: reproducible symbolic, numerical, and Monte Carlo checks."""
import numpy as np
import sympy as sp
from scipy.integrate import dblquad, tplquad
x,y,u,v=sp.symbols('x y u v', real=True)
assert sp.integrate(x*x+3*y,(y,0,1),(x,0,2)) == sp.Rational(17,3)
assert sp.integrate(x+y,(y,0,x),(x,0,1)) == sp.Rational(1,2)
assert sp.integrate((1+x),(y,0,1),(x,0,2)) == 4
assert sp.integrate(x*(1+x),(y,0,1),(x,0,2)) == sp.Rational(14,3)
assert sp.Matrix([u+v,u-v]).jacobian([u,v]).det() == -2
val,err=dblquad(lambda r,t:(4-r*r)*r,0,2*np.pi,lambda t:0,lambda t:2)
assert abs(val-8*np.pi)<1e-9
v3,err3=tplquad(lambda z,y,x:1,0,1,lambda x:0,lambda x:1-x,lambda x,y:0,lambda x,y:1-x-y)
assert abs(v3-1/6)<1e-10
rng=np.random.default_rng(2026);N=100000
xy=rng.uniform(-2,2,size=(N,2));r2=np.sum(xy**2,axis=1)
g=np.where(r2<=4,4-r2,0.0)
estimate=16*g.mean();se=16*g.std(ddof=1)/np.sqrt(N)
print('Exact paraboloid volume:',8*np.pi)
print('Polar quadrature:',val,'estimated error:',err)
print('Tetrahedron volume:',v3)
print('Monte Carlo:',estimate,'SE:',se)
assert abs(estimate-8*np.pi)<5*se
print('All Chapter 5 checks passed')
