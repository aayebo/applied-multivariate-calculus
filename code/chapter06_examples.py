"""Chapter 6: exact and numerical checks. Requires sympy, scipy, numpy."""
import numpy as np
import sympy as sp
from scipy.integrate import quad, dblquad
x, y, z, t, phi, theta = sp.symbols('x y z t phi theta', real=True)

# Fundamental theorem for line integrals
potential = x*x*y + 3*x + y*y
F = sp.Matrix([sp.diff(potential,x),sp.diff(potential,y)])
assert F == sp.Matrix([2*x*y+3,x*x+2*y])
assert sp.simplify(potential.subs({x:1,y:2})-potential.subs({x:0,y:0})) == 9

# Circulation of (-y,x) around the unit circle
r = sp.Matrix([sp.cos(t),sp.sin(t)])
rot = sp.Matrix([-y,x])
work = sp.integrate(rot.subs({x:r[0],y:r[1]}).dot(sp.diff(r,t)), (t,0,2*sp.pi))
assert sp.simplify(work-2*sp.pi)==0
numeric, err = quad(lambda tt: (-np.sin(tt))*(-np.sin(tt)) + np.cos(tt)*np.cos(tt),0,2*np.pi)
assert abs(numeric-2*np.pi)<1e-10

# Green's theorem on the unit disk: curl density 2
area_integral, _ = dblquad(lambda radius, angle: 2*radius,0,2*np.pi,lambda angle:0,lambda angle:1)
assert abs(area_integral-2*np.pi)<1e-10

# Divergence theorem for radial field on a sphere of radius 2
assert sp.diff(x,x)+sp.diff(y,y)+sp.diff(z,z)==3
radius = 2
outward_flux = 4*np.pi*radius**3
volume_flux = 3*(4*np.pi*radius**3/3)
assert abs(outward_flux-volume_flux)<1e-12

# Stokes theorem, unit disk vs hemisphere for F=(-y/2,x/2,0)
F3 = sp.Matrix([-y/2,x/2,0])
curl = sp.Matrix([sp.diff(F3[2],y)-sp.diff(F3[1],z),
                  sp.diff(F3[0],z)-sp.diff(F3[2],x),
                  sp.diff(F3[1],x)-sp.diff(F3[0],y)])
assert curl == sp.Matrix([0,0,1])
hemisphere = sp.Matrix([sp.sin(phi)*sp.cos(theta),sp.sin(phi)*sp.sin(theta),sp.cos(phi)])
normal = sp.diff(hemisphere,phi).cross(sp.diff(hemisphere,theta))
assert sp.simplify(curl.dot(normal)-sp.sin(phi)*sp.cos(phi))==0
hemi_flux = sp.integrate(sp.sin(phi)*sp.cos(phi),(phi,0,sp.pi/2))*2*sp.pi
assert sp.simplify(hemi_flux-sp.pi)==0
print('Chapter 6 checks passed: potentials, circulation, Green, divergence, Stokes.')
