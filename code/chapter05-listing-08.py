import numpy as np
vol=quad(lambda r:2*np.pi*(4-r*r)*r,0,2)[0]
rng=np.random.default_rng(2026);n=100000
xs=rng.random(n);ys=rng.random(n)
vals=np.where(xs+ys<=1,xs+2*ys,0)
print('volume',vol,'exact',8*np.pi)
print('MC estimate',vals.mean(),'SE',vals.std(ddof=1)/np.sqrt(n))
