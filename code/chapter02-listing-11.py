import numpy as np
from scipy.integrate import quad
area_num, error_est = quad(
    lambda r: 2*np.pi*r*np.sqrt(1+4*r*r), 0, 1)
area_exact = np.pi*(5**1.5-1)/6
assert abs(area_num-area_exact) < 1e-8
print(area_num, area_exact, error_est)
