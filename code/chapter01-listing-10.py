import numpy as np
r = np.array([2., 0., 0.])
force = np.array([0., 3., 4.])
torque = np.cross(r, force)
print('Torque vector:', torque)
print('Torque magnitude:', np.linalg.norm(torque))
assert np.isclose(np.dot(torque, r), 0.0)
assert np.isclose(np.dot(torque, force), 0.0)
