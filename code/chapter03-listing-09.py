import numpy as np

def f(x, y):
    return x**2 + 2*y**2

h = np.array([0.2, 0.1, 0.05, 0.025])
k = h / 2
linear = 1.5 + 2*h + 2*k
error = np.abs(f(1+h, 0.5+k) - linear)
bound = 2*(h*h + k*k)
print(np.column_stack((h, k, error, bound)))
assert np.all(error <= bound + 1e-12)
