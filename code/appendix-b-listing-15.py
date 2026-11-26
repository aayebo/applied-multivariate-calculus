from scipy.integrate import dblquad
I, estimated_error = dblquad(lambda y, x: x+y,
                              0, 1, lambda x: 0,
                              lambda x: 1-x)
print("quadrature:", I, "estimated error:", estimated_error)
assert np.isclose(I, 1/3)

rng = np.random.default_rng(2026)
n = 100000
x = rng.uniform(0, 1, n)
y = rng.uniform(0, 1, n)
mc = np.mean((x+y)*(x+y <= 1))
print("Monte Carlo estimate:", mc)
