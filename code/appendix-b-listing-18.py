def heat_solver(nx=80, alpha=0.1, T=0.1, mu=0.4):
    dx = 1.0/nx
    dt_target = mu*dx*dx/alpha
    steps = int(np.ceil(T/dt_target))
    dt = T/steps
    actual_mu = alpha*dt/dx**2
    assert actual_mu <= 0.5
    x = np.linspace(0, 1, nx+1)
    u = np.sin(np.pi*x)
    for _ in range(steps):
        new = u.copy()
        new[1:-1] = u[1:-1] + actual_mu*(
            u[:-2]-2*u[1:-1]+u[2:])
        u = new
    exact = np.exp(-alpha*np.pi**2*T)*np.sin(np.pi*x)
    return x, u, np.max(np.abs(u-exact))

x, numerical, error = heat_solver()
print("maximum error:", error)
