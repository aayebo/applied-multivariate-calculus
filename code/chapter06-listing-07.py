flux=quad(lambda r:2*np.pi*(4-r*r)*r,0,1)[0]
line=quad(lambda t:a*a/2,0,2*np.pi)[0]
cap=quad(lambda r:2*np.pi*r,0,a)[0]
print('paraboloid flux',flux,'exact',7*np.pi/2)
print('Stokes boundary',line,'cap',cap,'disk',np.pi*a*a)
assert abs(flux-7*np.pi/2)<1e-9
assert abs(line-cap)<1e-9
