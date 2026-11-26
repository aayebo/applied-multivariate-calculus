# Chapter 5 paired Python calculations
import numpy as np
import sympy as sp
from scipy.integrate import dblquad,quad
x,y=sp.symbols('x y',real=True)
exact=sp.integrate(sp.integrate(x+2*y,(y,0,1-x)),(x,0,1))
I=dblquad(lambda yy,xx:xx+2*yy,0,1,0,lambda xx:1-xx)[0]
E=dblquad(lambda yy,xx:2+.5*xx+yy**2,0,3,0,2)[0]
M=quad(lambda xx:1+xx,0,2)[0]
Mx=quad(lambda xx:xx*(1+xx),0,2)[0]
vol=quad(lambda r:2*np.pi*(4-r*r)*r,0,2)[0]
rng=np.random.default_rng(2026);n=100000
xs=rng.random(n);ys=rng.random(n)
vals=np.where(xs+ys<=1,xs+2*ys,0)
assert exact==sp.Rational(1,2)
assert abs(I-.5)<1e-8 and abs(E-24.5)<1e-8
assert abs(M-4)<1e-8 and abs(Mx/M-7/6)<1e-8
assert abs(vol-8*np.pi)<1e-8
print(dict(triangle=I,exposure=E,mass=M,xbar=Mx/M,volume=vol,MC=vals.mean(),MC_SE=vals.std(ddof=1)/np.sqrt(n)))
