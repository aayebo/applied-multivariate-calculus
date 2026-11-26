import numpy as np
from scipy.integrate import quad
x,y,z = 3.,4.,5.
r = np.hypot(x,y); theta = np.arctan2(y,x)
rho = np.sqrt(x*x+y*y+z*z); phi = np.arccos(z/rho)
print(r,theta,z,rho,phi)
area = quad(lambda r: 2*np.pi*r*np.sqrt(1+4*r*r),0,1)[0]
exact = np.pi*(5**1.5-1)/6
print(area, exact)
