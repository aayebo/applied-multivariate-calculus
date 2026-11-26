import numpy as np

def heat_ftcs(N=41, alpha=0.1, T=0.2):
    x = np.linspace(0, 1, N)
    h = x[1]-x[0]
    steps = int(np.ceil(T*alpha/(0.4*h*h)))
    dt = T/steps
    r = alpha*dt/(h*h)
    u = np.sin(np.pi*x)
    for _ in range(steps):
        v = u.copy()
        v[1:-1] = u[1:-1]+r*(u[:-2]-2*u[1:-1]+u[2:])
        u = v
    exact = np.exp(-alpha*np.pi**2*T)*np.sin(np.pi*x)
    return h, np.max(np.abs(u-exact)), r

print(heat_ftcs())
assert heat_ftcs()[2] <= 0.5
