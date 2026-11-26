"""Verified symbolic/numeric examples accompanying Chapter 2.
Run with: python code/chapter02_examples.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad

t = sp.symbols('t', real=True)
a, b = sp.symbols('a b', positive=True, real=True)
r = sp.Matrix([a*sp.cos(t), a*sp.sin(t), b*t])
v, acc, jerk = r.diff(t), r.diff(t, 2), r.diff(t, 3)
cross = v.cross(acc)
speed = sp.sqrt(sp.simplify(v.dot(v)))
kappa = sp.simplify(sp.sqrt(sp.simplify(cross.dot(cross))) / speed**3)
tau = sp.simplify(cross.dot(jerk) / cross.dot(cross))
assert sp.simplify(kappa - a/(a*a+b*b)) == 0
assert sp.simplify(tau - b/(a*a+b*b)) == 0
print('Helix curvature:', kappa, '; torsion:', tau)

L_exact = sp.sqrt(5)/2 + sp.asinh(2)/4
L_num, err = quad(lambda x: np.sqrt(1+4*x*x), 0, 1)
assert abs(float(L_exact) - L_num) < 1e-12
print('Parabola arc length:', L_num, '; quadrature error estimate:', err)

# Sphere parametrization: cross-product area scale
th, ph, R = sp.symbols('th ph R', real=True, positive=True)
surf = sp.Matrix([R*sp.sin(ph)*sp.cos(th), R*sp.sin(ph)*sp.sin(th), R*sp.cos(ph)])
c = surf.diff(th).cross(surf.diff(ph))
assert sp.simplify(c.dot(c) - R**4*sp.sin(ph)**2) == 0
print('Sphere area:', 4*sp.pi*R**2)

# Polygonal arc length converges from below for a helix
curve = lambda x: np.array([2*np.cos(x), 2*np.sin(x), .5*x])
true_length = 4*np.pi*np.sqrt(4.25)
errs=[]
for n in [20, 40, 80, 160, 320]:
    points = np.array([curve(s) for s in np.linspace(0, 4*np.pi, n+1)])
    approximate = np.linalg.norm(np.diff(points, axis=0), axis=1).sum()
    errs.append(true_length-approximate)
    print(f'N={n:3d}  length={approximate:.9f}  error={errs[-1]:.3e}')
assert all(e>0 for e in errs) and all(x>y for x,y in zip(errs,errs[1:]))
print('All Chapter 2 computational checks passed.')
