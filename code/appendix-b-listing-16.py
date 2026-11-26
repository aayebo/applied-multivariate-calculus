from scipy.integrate import quad

def circulation_integrand(t):
    x, y = np.cos(t), np.sin(t)
    dx, dy = -np.sin(t), np.cos(t)
    P, Q = -y, x
    return P*dx + Q*dy

value, error = quad(circulation_integrand, 0, 2*np.pi)
assert np.isclose(value, 2*np.pi)
print("line integral:", value, "Green theorem:", 2*np.pi)
