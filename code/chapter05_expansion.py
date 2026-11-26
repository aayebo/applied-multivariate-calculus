"""Chapter 5 expanded R/Python comparison benchmarks (Python edition)."""
import numpy as np
from scipy.integrate import quad

def midpoint(n):
    m=(np.arange(n)+0.5)/n
    xx,yy=np.meshgrid(m,m,indexing='ij')
    return float(np.mean(xx**2+yy**2))
for n in (4,8,16,32,64):
    e=abs(midpoint(n)-2/3)
    assert abs(e-1/(6*n*n))<1e-12
I=quad(lambda y:y*y*np.exp(y**3),0,1)[0]
assert abs(I-(np.e-1)/3)<1e-10
# nonuniform lamina moment of inertia about origin
I0=8.0
IC=I0-4*((7/6)**2+(1/2)**2)
assert abs(IC-14/9)<1e-12
# original chapter benchmarks
exec(open('code/chapter05_paired.py').read())
print('Expanded Chapter 5 mathematical benchmarks passed.')
