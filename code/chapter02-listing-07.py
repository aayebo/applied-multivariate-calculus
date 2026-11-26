import sympy as sp
s = sp.symbols('s',real=True)
r = sp.Matrix([s**2,3*s,2])
velocity = r.diff(s)
print(velocity.subs(s,2), sp.sqrt(velocity.dot(velocity)).subs(s,2))
