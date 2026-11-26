"""Reproducible symbolic and numerical checks for Chapter 3."""
import numpy as np
import sympy as sp
x,y,t=sp.symbols('x y t',real=True)
f=x**2*sp.exp(x*y)+sp.sin(y)
assert sp.simplify(sp.diff(f,x)-(2*x+x**2*y)*sp.exp(x*y))==0
assert sp.simplify(sp.diff(f,y)-(x**3*sp.exp(x*y)+sp.cos(y)))==0
# chain rule for x(t)=t^2, y(t)=sin(t)
curve={x:t**2,y:sp.sin(t)}
left=sp.diff(f.subs(curve),t)
right=(sp.diff(f,x).subs(curve)*2*t+sp.diff(f,y).subs(curve)*sp.cos(t))
assert sp.simplify(left-right)==0
# mixed partials and Hessian
q=x**2*y+sp.exp(x*y)
assert sp.simplify(sp.diff(q,x,y)-sp.diff(q,y,x))==0
# tangent plane and quadratic remainder for g=x^2+2y^2 at (1,1/2)
a,b=sp.Integer(1),sp.Rational(1,2)
g=x**2+2*y**2
lin=g.subs({x:a,y:b})+sp.diff(g,x).subs({x:a,y:b})*(x-a)+sp.diff(g,y).subs({x:a,y:b})*(y-b)
assert sp.simplify(g-lin-((x-a)**2+2*(y-b)**2))==0
# two-path failure of a limit
h=x*y/(x*x+y*y)
assert sp.simplify(h.subs(y,0))==0
assert sp.simplify(h.subs(y,x))==sp.Rational(1,2)
# directional derivative at (0.8,0.6)
pt={x:sp.Rational(4,5),y:sp.Rational(3,5)}
u=sp.Matrix([5/sp.sqrt(29),2/sp.sqrt(29)])
grad=sp.Matrix([2*x,4*y]).subs(pt)
print('Directional derivative:',sp.simplify(grad.dot(u)))
# numerical difference quotient convergence
v=lambda a,b: a*a+2*b*b
for step in [1e-2,1e-3,1e-4]:
    estimate=(v(.8+step,.6)-v(.8,.6))/step
    assert abs(estimate-1.6)<.011
print('Chapter 3 checks passed.')
