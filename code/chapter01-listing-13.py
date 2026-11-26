import numpy as np
A = np.array([[1, 1, 1], [1, -1, 1], [2, 1, -1]], dtype=float)
b = np.array([6, 2, 1], dtype=float)
solution = np.linalg.solve(A, b)
print(solution)  # [1. 2. 3.]
print('Residual norm:', np.linalg.norm(A @ solution - b))
