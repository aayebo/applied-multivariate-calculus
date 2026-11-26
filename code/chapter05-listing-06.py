import sympy as sp
from scipy.integrate import dblquad, quad
x,y=sp.symbols('x y',real=True)
exact=sp.integrate(sp.integrate(x+2*y,(y,0,1-x)),(x,0,1))
num=dblquad(lambda yy,xx:xx+2*yy,0,1,0,lambda xx:1-xx)[0]
print(exact,num)
assert exact==sp.Rational(1,2) and abs(num-.5)<1e-8
