t = sp.symbols("t", real=True)
c = sp.Rational(1, 2)
r = sp.Matrix([sp.cos(t), sp.sin(t), c*t])
r1, r2, r3 = r.diff(t), r.diff(t, 2), r.diff(t, 3)
cross = r1.cross(r2)
kappa = sp.simplify(sp.sqrt(cross.dot(cross)) /
                    sp.sqrt(r1.dot(r1))**3)
tau = sp.simplify(cross.dot(r3) / cross.dot(cross))
print("curvature:", kappa, "torsion:", tau)
assert sp.simplify(kappa - sp.Rational(4, 5)) == 0
assert sp.simplify(tau - sp.Rational(2, 5)) == 0
