import numpy as np
from scipy.integrate import quad
a,b = 2.0,1.0/3.0
L_num = quad(lambda t: np.sqrt(a*a+b*b),0,2*np.pi)[0]
L_exact = 2*np.pi*np.sqrt(a*a+b*b)
print(L_num, abs(L_num-L_exact), a/(a*a+b*b), b/(a*a+b*b))
