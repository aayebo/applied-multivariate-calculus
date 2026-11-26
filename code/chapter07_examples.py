"""Executable exact and numerical checks for Chapter 7."""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

def connection(g, coords):
    """Levi-Civita coefficients Gamma[k][i][j] for a regular metric."""
    n = len(coords)
    gi = g.inv()
    return [[[sp.simplify(sum(gi[k,l]*(sp.diff(g[l,j],coords[i])
       +sp.diff(g[l,i],coords[j])-sp.diff(g[i,j],coords[l]))/2
       for l in range(n))) for j in range(n)] for i in range(n)]
       for k in range(n)]

r, th = sp.symbols('r th', positive=True)
g = sp.diag(1,r**2)
G = connection(g, (r,th))
assert G[0][1][1] == -r
assert G[1][0][1] == 1/r
assert G[1][1][0] == 1/r

u, v, a = sp.symbols('u v a', positive=True)
X = sp.Matrix([a*sp.cos(u),a*sp.sin(u),v])
J = X.jacobian((u,v))
assert sp.simplify(J.T*J-sp.diag(a*a,1)) == sp.zeros(2)
assert all(x == 0 for layer in connection(sp.diag(a*a,1),(u,v)) for row in layer for x in row)

vartheta, phi = sp.symbols('vartheta phi', real=True)
Gs = connection(sp.diag(1,sp.sin(vartheta)**2),(vartheta,phi))
assert sp.simplify(Gs[0][1][1]+sp.sin(vartheta)*sp.cos(vartheta)) == 0
assert sp.simplify(Gs[1][0][1]-sp.cot(vartheta)) == 0

x,y = sp.symbols('x y', real=True)
f = x*x-y*y
K = sp.simplify((sp.diff(f,x,2)*sp.diff(f,y,2)-sp.diff(f,x,y)**2)/(1+sp.diff(f,x)**2+sp.diff(f,y)**2)**2)
assert sp.simplify(K+4/(1+4*x*x+4*y*y)**2) == 0

t, aa, bb = sp.symbols('t aa bb', positive=True)
curve = sp.Matrix([aa*sp.cos(t),aa*sp.sin(t),bb*t])
vel,acc,jerk = (sp.diff(curve,t,i) for i in (1,2,3))
cr=vel.cross(acc)
kappa=sp.simplify(sp.sqrt(cr.dot(cr))/sp.sqrt(vel.dot(vel))**3)
tau=sp.simplify(sp.det(sp.Matrix.hstack(vel,acc,jerk))/cr.dot(cr))
assert sp.simplify(kappa-aa/(aa**2+bb**2)) == 0
assert sp.simplify(tau-bb/(aa**2+bb**2)) == 0

def rhs(t,y):
    rr,tt,vr,vt=y
    return [vr,vt,rr*vt*vt,-2*vr*vt/rr]
sol=solve_ivp(rhs,(0,1),[1,0,0,1],rtol=1e-10,atol=1e-12)
assert sol.success
xx=sol.y[0]*np.cos(sol.y[1]); yy=sol.y[0]*np.sin(sol.y[1])
assert np.max(np.abs(xx-1))<1e-7
assert np.max(np.abs(yy-sol.t))<1e-7
print('Chapter 7 symbolic and numerical checks passed.')
