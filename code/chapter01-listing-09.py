import numpy as np
import sympy as sp
u = sp.Matrix([1, 2, 2])
v = sp.Matrix([2, 0, 1])
cos_theta = sp.simplify(u.dot(v) / (u.norm()*v.norm()))
print('Exact cosine:', cos_theta)
print('Angle (degrees):', float(sp.acos(cos_theta)*180/sp.pi))
u_np = np.array([1., 2., 2.])
v_np = np.array([2., 0., 1.])
cos_numeric = np.dot(u_np, v_np) / (
    np.linalg.norm(u_np)*np.linalg.norm(v_np))
angle = np.degrees(np.arccos(np.clip(cos_numeric, -1, 1)))
print('Numerical angle:', angle)
