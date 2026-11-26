"""Generate original Chapter 4 figures. Run from the book project root."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P = Path(__file__).resolve().parent.parent / 'figures'
P.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 10, 'figure.dpi': 130, 'savefig.bbox': 'tight'})
def save(name):
    plt.savefig(P / f'ch4_{name}.pdf'); plt.close()

x=np.linspace(-2.3,2.3,240); y=np.linspace(-2.3,2.3,240); X,Y=np.meshgrid(x,y)
Z=12-2*X**2-Y**2+2*X*Y
fig,ax=plt.subplots(figsize=(6.4,5.0)); cs=ax.contour(X,Y,Z,levels=13,cmap='viridis');ax.clabel(cs,inline=True,fontsize=7)
a=np.linspace(-1.8,1.8,11); A,B=np.meshgrid(a,a); U=-4*A+2*B;V=2*A-2*B; N=np.hypot(U,V);N=np.where(N<1e-9,1,N)
ax.quiver(A,B,U/N,V/N,color='#b44e34',alpha=.72,pivot='mid');ax.set(xlabel='$x$',ylabel='$y$',title='Level curves and gradient directions');ax.set_aspect('equal');save('gradient')

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
u=np.linspace(-.9,.9,85); X,Y=np.meshgrid(u,u)
F=np.exp(X)*np.cos(Y)+X*Y;T=1+X+.5*X**2+X*Y-.5*Y**2
fig=plt.figure(figsize=(7.3,5.5));ax=fig.add_subplot(projection='3d');ax.plot_surface(X,Y,F,cmap='Blues',alpha=.75,linewidth=0);ax.plot_wireframe(X[::6,::6],Y[::6,::6],T[::6,::6],color='#a34132',alpha=.8,linewidth=.8)
ax.set(xlabel='$x$',ylabel='$y$',zlabel='$z$',title='Exact surface (blue) and quadratic approximation (red)');save('taylor')

fig,axs=plt.subplots(1,3,figsize=(10,3.4),constrained_layout=True); X,Y=np.meshgrid(np.linspace(-1.5,1.5,200),np.linspace(-1.5,1.5,200))
for ax,Z,title in zip(axs,[X**2+2*Y**2,-X**2-2*Y**2,X**2-Y**2],['Minimum','Maximum','Saddle']):
    ax.contour(X,Y,Z,levels=14,cmap='viridis');ax.plot(0,0,'o',color='#ae4338');ax.set_title(title);ax.set_aspect('equal');ax.set_xlabel('$x$');ax.set_ylabel('$y$')
save('stationary')

fig,ax=plt.subplots(figsize=(5.8,5.0));X,Y=np.meshgrid(np.linspace(-3.3,3.3,200),np.linspace(-3.3,3.3,200));ax.contour(X,Y,X+2*Y,levels=np.linspace(-8,8,13),cmap='viridis'); t=np.linspace(0,2*np.pi,400);ax.plot(3*np.cos(t),3*np.sin(t),'k',lw=2);q=3/np.sqrt(5)*np.array([1.,2.]);ax.scatter([q[0],-q[0]],[q[1],-q[1]],color='#c34a36',zorder=3);ax.set(xlabel='$x$',ylabel='$y$',title='Extrema of $x+2y$ on a disk');ax.set_aspect('equal');save('disk')

fig,ax=plt.subplots(figsize=(6.0,4.7)); t=np.linspace(0,2*np.pi,500);ax.plot(2*np.cos(t),np.sin(t),'k',lw=2,label='Ellipse constraint');X,Y=np.meshgrid(np.linspace(-2.5,2.5,240),np.linspace(-1.6,3.3,240));Z=X**2+(Y-3)**2;ax.contour(X,Y,Z,levels=[4,6,9,12,16],cmap='Blues');ax.scatter([0,0],[1,3],c=['#b64035','#1b668e']);ax.annotate('Closest point',(0,1),xytext=(.4,1.3),arrowprops={'arrowstyle':'->'});ax.set(xlabel='$x$',ylabel='$y$',title='Distance contours and ellipse');ax.set_aspect('equal');save('lagrange')

fig,ax=plt.subplots(figsize=(6.5,5));X,Y=np.meshgrid(np.linspace(-2.7,3,200),np.linspace(-2,2.7,200));Z=(X-2)**2+4*(Y+1)**2;ax.contour(X,Y,Z,levels=[.2,.8,2,5,10,20,35,50],cmap='viridis');p=np.array([-2.,2.]);path=[p.copy()]
for _ in range(20):p=p-.15*np.array([2*(p[0]-2),8*(p[1]+1)]);path.append(p.copy())
path=np.array(path);ax.plot(path[:,0],path[:,1],'-o',ms=3,color='#bd4438');ax.plot(2,-1,'k*',ms=11);ax.set(xlabel='$x$',ylabel='$y$',title='Gradient descent on a convex quadratic');save('descent')

fig,ax=plt.subplots(figsize=(6.4,4.6));x=np.array([0.,1.,2.,3.]);y=np.array([1.,2.,2.,4.]);xx=np.linspace(-.3,3.3,100);ax.plot(xx,.9+.9*xx,color='#21618c',label='$0.9+0.9x$');ax.scatter(x,y,color='#b33e33',zorder=3,label='Observations');
for xi,yi in zip(x,y):ax.plot([xi,xi],[yi,.9+.9*xi],color='gray',ls='--')
ax.set(xlabel='$x$',ylabel='$y$',title='Least squares and vertical residuals');ax.legend();save('leastsquares')
print('Generated 7 Chapter 4 figures')
