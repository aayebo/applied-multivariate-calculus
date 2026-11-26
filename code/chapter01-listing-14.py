import numpy as np
points = np.array([
    [0, 0, 1.0], [1, 0, 3.1], [0, 1, 0.1],
    [1, 1, 2.0], [2, 1, 4.2], [1, 2, 1.0]
])
X = np.column_stack((points[:, 0], points[:, 1],
                     np.ones(len(points))))
coeff, residuals, rank, s = np.linalg.lstsq(
    X, points[:, 2], rcond=None)
a, b, c = coeff
print(f'Fitted plane: z = {a:.3f}x + {b:.3f}y + {c:.3f}')
print('Residual norm:', np.linalg.norm(X @ coeff - points[:, 2]))
