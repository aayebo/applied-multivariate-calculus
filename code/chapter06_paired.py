import numpy as np
from scipy.integrate import quad
a=2.0
circulation=quad(lambda t:a*a,0,2*np.pi)[0]
wire_mass=quad(lambda t:2*(1+2*np.sin(t)),0,np.pi)[0]
flux=quad(lambda r:2*np.pi*(4-r*r)*r,0,1)[0]
line=quad(lambda t:a*a/2,0,2*np.pi)[0]
cap=quad(lambda r:2*np.pi*r,0,a)[0]
for actual,exact in [(circulation,2*np.pi*a*a),(wire_mass,2*np.pi+8),(flux,7*np.pi/2),(line,4*np.pi),(cap,4*np.pi)]:
    assert abs(actual-exact)<1e-9,(actual,exact)
print('Green circulation:',circulation)
print('Semicircular wire mass:',wire_mass)
print('Paraboloid flux:',flux)
print('Stokes line / cap / disk:',line,cap,np.pi*a*a)
