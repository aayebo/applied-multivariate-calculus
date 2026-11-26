import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y:np.exp(x+2*y)
t1=lambda x,y:1+x+2*y
t2=lambda x,y:1+x+2*y+.5*(x+2*y)**2
print(f(.1,.05),t1(.1,.05),t2(.1,.05))
h=np.logspace(-3,-1,25)
plt.loglog(h,abs(f(h,h)-t2(h,h)),'o-')
plt.xlabel('Step size');plt.ylabel('Quadratic error')
