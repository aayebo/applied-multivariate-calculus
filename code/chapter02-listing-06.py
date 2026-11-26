import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,6*np.pi,500)
x,y,z = 2*np.cos(t),2*np.sin(t),t/3
fig,ax = plt.subplots(1,2,figsize=(9,3.5))
ax[0].plot(x,y); ax[0].set_aspect('equal')
ax[0].set_title('Top view')
ax[1].plot(t,z); ax[1].set_title('Height')
plt.tight_layout()
