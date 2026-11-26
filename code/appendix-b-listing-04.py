A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])
x = np.linalg.solve(A, b)
print(x)                 # [2., 3.]
print(np.allclose(A @ x, b))
print(np.linalg.det(A))
print(np.linalg.eigvalsh(A))
