from scipy.optimize import minimize, minimize_scalar
nonconvex=lambda p:(p[0]**2-1)**2+p[1]**2
starts=[[-2,1],[2,1],[-.7,-1],[.7,-1]]
print([minimize(nonconvex,s,method='BFGS').x for s in starts])
res=minimize_scalar(lambda t:-(np.cos(t)+2*np.sin(t)),
                    bounds=(0,2*np.pi),method='bounded')
print('disk maximum',-res.fun,'exact',np.sqrt(5))
res=minimize_scalar(lambda x:-x*(10-x),bounds=(0,10),
                    method='bounded')
print('fixed-sum optimum',res.x,10-res.x,-res.fun)
