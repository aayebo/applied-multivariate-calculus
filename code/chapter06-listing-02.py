import numpy as np
from scipy.integrate import quad
a,b = 3.0,2.0
ellipse = quad(lambda t:a*b,0,2*np.pi)[0]
annulus = np.pi*(2**2-1**2)
def box(a,b,c):
    return a*a*b*c+a*b*b*c+a*b*c*c
print('ellipse',ellipse,'annulus',annulus,'box',box(2,3,4))
assert np.isclose(ellipse,2*np.pi*a*b)
assert np.isclose(annulus,3*np.pi)
assert np.isclose(box(2,3,4),216)
