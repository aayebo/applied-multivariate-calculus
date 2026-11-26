from scipy.optimize import minimize

def utility(z):
    x, y = z
    return 8*x + 6*y - x*x - 2*y*y - x*y

constraints = [{"type": "ineq", "fun": lambda z: 8-2*z[0]-z[1]}]
result = minimize(lambda z: -utility(z), x0=[1., 1.],
                  bounds=[(0, None), (0, None)],
                  constraints=constraints, method="SLSQP",
                  options={"ftol": 1e-12})
assert result.success
assert 2*result.x[0] + result.x[1] <= 8 + 1e-8
print("allocation:", result.x, "utility:", utility(result.x))
