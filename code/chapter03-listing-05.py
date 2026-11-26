import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2,2,120); y=np.linspace(-2,2,120)
X,Y=np.meshgrid(x,y)
Z=20+3*X**2+2*Y**2
plt.contour(X,Y,Z,levels=[22,24,26,30,34])
plt.gca().set_aspect('equal'); plt.xlabel('x (m)')
plt.ylabel('y (m)'); plt.tight_layout()
assert 20+3*1**2+2*(-2)**2==31
