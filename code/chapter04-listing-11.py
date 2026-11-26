import numpy as np
q = lambda z: (z[0]-2)**2 + 4*(z[1]+1)**2
grad = lambda z: np.array([2*(z[0]-2),8*(z[1]+1)])
z = np.array([0.,3.]); alpha = 1/8
path = [z.copy()]
for k in range(100):
    z = np.maximum(0,z-alpha*grad(z))
    path.append(z.copy())
print('solution:',z,'objective:',q(z))
assert np.allclose(z,[2,0],atol=1e-10)
