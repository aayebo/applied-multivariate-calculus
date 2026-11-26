import numpy as np
u = np.array([2.0, -1.0, 2.0])
v = np.array([1.0, 3.0, -2.0])
print('u + v =', u + v)
print('2u - v =', 2*u - v)
print('||u|| =', np.linalg.norm(u))
print('unit u =', u / np.linalg.norm(u))
assert np.isclose(np.linalg.norm(u / np.linalg.norm(u)), 1)
