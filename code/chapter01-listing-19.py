import numpy as np
air = np.array([12.,5.,0.]); wind = np.array([-2.,3.,0.])
ground = air + wind
print(ground, np.linalg.norm(ground), 45*ground)
