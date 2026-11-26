import sympy as sp
A, B, C = (sp.Matrix(v) for v in [(1,0,1),(2,1,1),(1,2,3)])
P = sp.Matrix([3, 1, 4])
n = (B-A).cross(C-A) / 2  # primitive normal (1,-1,1)
d = n.dot(A)
signed = sp.simplify(n.dot(P) - d)
Q = sp.simplify(P - signed/n.dot(n)*n)
distance = sp.simplify(abs(signed)/sp.sqrt(n.dot(n)))
print('Normal:', n.T, 'plane constant:', d)
print('Closest point:', Q.T)
print('Exact distance:', distance)
assert sp.simplify(n.dot(Q)-d) == 0
assert sp.simplify((P-Q).cross(n)) == sp.zeros(3, 1)
