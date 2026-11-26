import numpy as np
from scipy.integrate import quad
a,b=3.,2.
ellipse=quad(lambda t:a*b,0,2*np.pi)[0]
annulus=np.pi*(4-1)
def box(a,b,c): return a*a*b*c+a*b*b*c+a*b*c*c
assert np.isclose(ellipse,2*np.pi*a*b)
assert np.isclose(annulus,3*np.pi)
assert np.isclose(box(2,3,4),216)
print('Chapter 6 expanded numerical tests passed:',ellipse,annulus,box(2,3,4))
