xx=np.array([0,1,2,3]); yy=np.array([1,2,2,4])
X=np.column_stack([np.ones_like(xx),xx])
beta=np.linalg.lstsq(X,yy,rcond=None)[0]
print('least squares',beta)
assert np.allclose(beta,[.9,.9])
P=lambda p:12*p[0]+10*p[1]-p[0]**2-2*p[1]**2-p[0]*p[1]
fit=minimize(lambda p:-P(p),[1,1],method='BFGS')
print('production optimum',fit.x,'exact',[38/7,8/7])
assert np.allclose(fit.x,[38/7,8/7],atol=1e-4)
