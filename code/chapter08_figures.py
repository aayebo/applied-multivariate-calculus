"""Generate the six original figures for Chapter 8."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from chapter08_examples import heat_ftcs,laplace_jacobi

OUT=Path(__file__).resolve().parents[1]/'figures'
OUT.mkdir(exist_ok=True)

def save(name):
    plt.tight_layout();plt.savefig(OUT/name,dpi=180,bbox_inches='tight');plt.close()

x=np.linspace(-3,5,600)
plt.figure(figsize=(7,3.8))
for t in [0,.4,.8,1.2]:plt.plot(x,np.exp(-4*(x-2*t)**2),label=f't={t:g}')
plt.xlabel('position x');plt.ylabel('u(x,t)');plt.title('Transport: shape-preserving motion');plt.legend();plt.grid(alpha=.2)
save('ch08_transport.png')

x=np.linspace(0,1,400)
plt.figure(figsize=(7,3.8))
for t in [0,.03,.12,.35]:
    u=np.exp(-.1*np.pi**2*t)*np.sin(np.pi*x)+.5*np.exp(-.9*np.pi**2*t)*np.sin(3*np.pi*x)
    plt.plot(x,u,label=f't={t:g}')
plt.xlabel('x');plt.ylabel('temperature');plt.title('Heat diffusion: high modes decay rapidly');plt.legend();plt.grid(alpha=.2)
save('ch08_heat.png')

plt.figure(figsize=(7,3.8))
for n in [11,21,41]:
    xx,uu,r=heat_ftcs(lambda z:np.sin(np.pi*z),nx=n)
    plt.plot(xx,uu,'o-',markersize=2,label=f'{n} nodes')
plt.plot(x,np.exp(-.1*np.pi**2*.2)*np.sin(np.pi*x),'k--',label='exact')
plt.xlabel('x');plt.ylabel('u(x,0.2)');plt.title('FTCS versus exact heat solution');plt.legend();plt.grid(alpha=.2)
save('ch08_heat_error.png')

plt.figure(figsize=(7,3.8))
for t in [0,.2,.4,.6]:plt.plot(x,np.sin(np.pi*x)*np.cos(np.pi*t),label=f't={t:g}')
plt.xlabel('x');plt.ylabel('displacement');plt.title('Standing wave on a fixed string');plt.legend();plt.grid(alpha=.2)
save('ch08_wave.png')

xx,u,k=laplace_jacobi(n=51,tolerance=1e-7)
plt.figure(figsize=(6.3,4.5))
plt.contourf(xx,xx,u,levels=24,cmap='viridis');plt.colorbar(label='steady-state temperature')
plt.xlabel('x');plt.ylabel('y');plt.title('Laplace equation: heated upper edge')
save('ch08_laplace.png')

h=[];err=[]
for n in [11,21,41,81,161]:
    xx,uu,r=heat_ftcs(lambda z:np.sin(np.pi*z),nx=n)
    h.append(xx[1]-xx[0]);err.append(np.max(np.abs(uu-np.exp(-.1*np.pi**2*.2)*np.sin(np.pi*xx))))
plt.figure(figsize=(6.5,4))
plt.loglog(h,err,'o-',label='maximum error')
plt.loglog(h,np.array(h)**2*(err[0]/h[0]**2),'--',label='reference: $h^2$')
plt.xlabel('grid spacing h');plt.ylabel('maximum error');plt.title('Grid refinement for stable FTCS');plt.legend();plt.grid(alpha=.3,which='both')
save('ch08_convergence.png')
print('Generated six Chapter 8 figures; fitted slope',np.polyfit(np.log(h),np.log(err),1)[0])
