import numpy as np
from scipy.integrate import quad
a=2.0
circulation=quad(lambda t:a*a,0,2*np.pi)[0]
wire_mass=quad(lambda t:2*(1+2*np.sin(t)),0,np.pi)[0]
print(circulation,2*np.pi*a*a)
print(wire_mass,2*np.pi+8)
