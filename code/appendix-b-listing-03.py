import numpy as np
v = np.array([2.0, -1.0, 4.0])
w = np.array([1.0, 3.0, -2.0])
print(v[0])              # first entry: Python indexing starts at 0
print(v + w)             # componentwise sum
print(3 * v)             # scalar multiplication
print(np.dot(v, w))      # scalar dot product
print(np.cross(v, w))    # cross product in R^3
print(np.linalg.norm(v)) # Euclidean norm
