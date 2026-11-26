import numpy as np

def heat_ftcs(N=40, T=0.2, alpha=0.1):
    x = np.linspace(0.0, 1.0, N+1)
    h = 1.0/N
    steps = int(np.ceil(T*alpha/(0.4*h*h)))
    dt = T/steps
    r = alpha*dt/(h*h)
    u = np.sin(np.pi*x)
    for _ in range(steps):
        v = u.copy()
        v[1:-1] = u[1:-1] + r*(u[:-2]-2*u[1:-1]+u[2:])
        u = v
    exact = np.exp(-alpha*np.pi**2*T)*np.sin(np.pi*x)
    return h, r, np.max(np.abs(u-exact))

print(heat_ftcs())
