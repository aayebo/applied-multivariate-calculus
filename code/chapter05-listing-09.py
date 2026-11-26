import numpy as np
from scipy.integrate import quad

def midpoint(n):
    m = (np.arange(n)+0.5)/n
    xx, yy = np.meshgrid(m,m,indexing='ij')
    return np.mean(xx**2+yy**2)

for n in [4,8,16,32]:
    err = abs(midpoint(n)-2/3)
    print('n =',n,'error =',err)
    assert abs(err-1/(6*n*n))<1e-12
I = quad(lambda y:y*y*np.exp(y**3),0,1)[0]
assert abs(I-(np.e-1)/3)<1e-10
