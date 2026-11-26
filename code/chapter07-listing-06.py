import numpy as np

def rhs(z):
    r, theta, vr, vt = z
    return np.array([vr, vt, r*vt**2, -2*vr*vt/r])

def rk4(n):
    h = 1/n
    z = np.array([1.,0.,0.,1.])
    error = 0.
    for i in range(1,n+1):
        k1 = rhs(z)
        k2 = rhs(z+h*k1/2)
        k3 = rhs(z+h*k2/2)
        k4 = rhs(z+h*k3)
        z += h*(k1+2*k2+2*k3+k4)/6
        t = i*h
        error = max(error,abs(z[0]*np.cos(z[1])-1),
                    abs(z[0]*np.sin(z[1])-t))
    return error
print([rk4(n) for n in (20,40,80,160)])
