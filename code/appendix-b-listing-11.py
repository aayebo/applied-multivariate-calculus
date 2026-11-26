a = np.array([2., -1., 4.])
b = np.array([1., 3., -2.])
projection = (a @ b)/(b @ b)*b
normal = np.cross(a, b)
print("projection:", projection)
print("normal:", normal)
assert np.isclose(normal @ a, 0)
assert np.isclose(normal @ b, 0)
