import sympy as sp
x,y=sp.symbols('x y',real=True)
f=sp.exp(x*y)+x**3*y
fx,fy=sp.diff(f,x),sp.diff(f,y)
print(fx,fy)
fnum=sp.lambdify((x,y),f,'numpy')
h=1e-5
numeric_x=(fnum(1+h,.5)-fnum(1-h,.5))/(2*h)
print('exact:',float(fx.subs({x:1,y:.5})))
print('numeric:',numeric_x)
