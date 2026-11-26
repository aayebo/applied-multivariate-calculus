import numpy as np

def ftcs(N=40, T=.2, alpha=.1):
 x=np.linspace(0,1,N+1); h=1/N
 steps=int(np.ceil(T*alpha/(.4*h*h))); dt=T/steps; r=alpha*dt/h**2
 u=np.sin(np.pi*x)
 for _ in range(steps):
  v=u.copy();v[1:-1]=u[1:-1]+r*(u[:-2]-2*u[1:-1]+u[2:]);u=v
 exact=np.exp(-alpha*np.pi**2*T)*np.sin(np.pi*x)
 return h,r,float(np.max(np.abs(u-exact)))

if __name__=='__main__':
 results=[ftcs(N) for N in (20,40,80,160)]
 errors=np.array([a[2] for a in results]); orders=np.log2(errors[:-1]/errors[1:])
 for N,(h,r,e) in zip((20,40,80,160),results): print(f'N={N}, h={h:.6f}, r={r:.4f}, error={e:.8g}')
 print('orders',orders)
 assert all(r<=.5 for h,r,e in results)
 assert np.all((orders>1.8)&(orders<2.2))
 assert abs((np.pi/6)*(5**1.5-1)-5.330413500268973)<1e-10
 print('All Python checks passed')
