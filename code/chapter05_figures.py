"""Generate original Chapter 5 figures. Run from textbook root."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Wedge, Arc
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
OUT = Path(__file__).resolve().parents[1] / 'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
# midpoint sampling
fig, ax = plt.subplots(figsize=(7,4.2))
n=7
for i in range(n):
 for j in range(n):
  x=(i+.5)/n; y=(j+.5)/n
  ax.add_patch(Rectangle((i/n,j/n),1/n,1/n,facecolor=plt.cm.viridis((1+x+2*y)/4),edgecolor='white',lw=1))
  ax.plot(x,y,'.',color='black',ms=2)
ax.set(xlabel='x',ylabel='y',title='Midpoint sampling: f(x,y) = 1 + x + 2y',xlim=(0,1),ylim=(0,1));ax.set_aspect('equal');fig.tight_layout();fig.savefig(OUT/'ch5_riemann.pdf');plt.close(fig)
# slicing region
fig,axs=plt.subplots(1,2,figsize=(9,3.7))
for ax in axs:
 ax.fill([0,1,1],[0,0,1],color='#c8e2ed');ax.plot([0,1,1,0],[0,0,1,0],color='#17476b');ax.set(xlim=(-.07,1.08),ylim=(-.07,1.08),xlabel='x',ylabel='y');ax.set_aspect('equal')
for x in np.arange(.15,.99,.14):axs[0].plot([x,x],[0,x],color='#a85234',lw=1.4)
for y in np.arange(.15,.99,.14):axs[1].plot([y,1],[y,y],color='#a85234',lw=1.4)
axs[0].set_title('Vertical slices: 0 ≤ y ≤ x');axs[1].set_title('Horizontal slices: y ≤ x ≤ 1');fig.tight_layout();fig.savefig(OUT/'ch5_regions.pdf');plt.close(fig)
# polar wedges
fig,ax=plt.subplots(figsize=(6,5))
for r in [.5,1,1.5,2,2.5]:ax.add_patch(plt.Circle((0,0),r,fill=False,ec='#b5c8d2',lw=.9))
for th in np.linspace(0,2*np.pi,13):ax.plot([0,2.5*np.cos(th)],[0,2.5*np.sin(th)],color='#b5c8d2',lw=.9)
ax.add_patch(Wedge((0,0),2,35,65,width=.5,facecolor='#5cacc4',edgecolor='#1e5b77',alpha=.8))
ax.text(1.7,1.85,r'$r\,\Delta r\,\Delta\theta$',ha='center');ax.set(xlim=(-2.7,2.7),ylim=(-2.7,2.7),xlabel='x',ylabel='y',title='Area scaling in polar coordinates');ax.set_aspect('equal');fig.tight_layout();fig.savefig(OUT/'ch5_polar.pdf');plt.close(fig)
# density
fig,ax=plt.subplots(figsize=(7,3.5)); xx=np.linspace(0,2,150);yy=np.linspace(0,1,90);X,Y=np.meshgrid(xx,yy);im=ax.pcolormesh(X,Y,1+X,cmap='YlGnBu',shading='auto');ax.plot(7/6,.5,'*',ms=15,color='#cc4d33',label='center of mass');ax.plot(1,.5,'o',ms=6,color='black',label='geometric center');ax.set(xlabel='x',ylabel='y',title=r'Density $\rho(x,y)=1+x$');ax.legend(loc='upper left');fig.colorbar(im,ax=ax,label='areal density');fig.tight_layout();fig.savefig(OUT/'ch5_density.pdf');plt.close(fig)
# surface and tangent vectors
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d');xx=np.linspace(-1,1,35);yy=np.linspace(-1,1,35);X,Y=np.meshgrid(xx,yy);Z=.35*X**2+.2*Y**2;ax.plot_surface(X,Y,Z,cmap='Blues',alpha=.6,edgecolor='none');p=np.array([.45,.35,.35*.45**2+.2*.35**2]);a=np.array([1,0,.7*.45]);b=np.array([0,1,.4*.35]);ax.quiver(*p,*a,length=.5,color='#b34030',linewidth=2);ax.quiver(*p,*b,length=.5,color='#27845b',linewidth=2);ax.scatter(*p,color='black',s=30);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Tangent directions on a surface');fig.tight_layout();fig.savefig(OUT/'ch5_surface.pdf');plt.close(fig)
# spherical coordinates
fig=plt.figure(figsize=(6.5,5));ax=fig.add_subplot(111,projection='3d');rho=2;phi=.8;theta=.7;p=np.array([rho*np.sin(phi)*np.cos(theta),rho*np.sin(phi)*np.sin(theta),rho*np.cos(phi)]);ax.plot([0,p[0]],[0,p[1]],[0,p[2]],color='#bc4435',lw=3);ax.plot([0,p[0]],[0,p[1]],[0,0],ls='--',color='#3b8498');ax.plot([p[0],p[0]],[p[1],p[1]],[0,p[2]],ls=':',color='#3b8498');t=np.linspace(0,2*np.pi,100);ax.plot(1.45*np.cos(t),1.45*np.sin(t),0,color='#b9c9d1',alpha=.7);ax.scatter(*p,color='#bc4435');ax.text(*(p*1.07),r'$(\rho,\phi,\theta)$');ax.set(xlim=(-2,2),ylim=(-2,2),zlim=(0,2.5),xlabel='x',ylabel='y',zlabel='z',title='Spherical coordinate geometry');fig.tight_layout();fig.savefig(OUT/'ch5_spherical.pdf');plt.close(fig)
print('Created six figures in',OUT)
