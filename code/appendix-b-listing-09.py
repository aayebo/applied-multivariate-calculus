import sympy as sp
x, y, t = sp.symbols("x y t", real=True)
f = x**2*y + sp.sin(y)
grad_f = sp.Matrix([sp.diff(f, x), sp.diff(f, y)])
H = sp.hessian(f, (x, y))
print(grad_f)
print(H)
print(grad_f.subs({x: 2, y: 0}))
