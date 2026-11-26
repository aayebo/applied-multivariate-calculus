import numpy as np
r, theta = 2.0, np.pi/6
J = np.array([[np.cos(theta),-r*np.sin(theta)],
              [np.sin(theta), r*np.cos(theta)]])
g = J.T @ J
V = np.array([2.,3.])
V_lower = g @ V
assert np.allclose(g,np.diag([1.,4.]))
assert np.isclose(V @ V_lower,40.)
assert np.allclose(np.linalg.solve(g,V_lower),V)
R = 6371.
p, q = np.array([1.,0.,0.]), np.array([0.,1.,0.])
angle = np.arccos(np.clip(p @ q,-1,1))
distance = R*angle
assert np.isclose(distance,R*np.pi/2)
print('Metric:',g,'great-circle distance:',distance)
