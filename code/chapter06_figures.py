"""Original reproducible figures for Chapter 6. Run from textbook root."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
F = Path(__file__).resolve().parents[1]/'figures'
F.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'figure.dpi':120})

def save(name):
    plt.savefig(F/name, bbox_inches='tight'); plt.close()

x,y=np.meshgrid(np.linspace(-2,2,13),np.linspace(-2,2,13))
fig,axs=plt.subplots(1,2,figsize=(10,4.2))
for ax,U,V,title in [(axs[0],-y,x,'Rotational: F = (-y, x)'),(axs[1],x,y,'Radial: G = (x, y)')]:
    mag=np.hypot(U,V); ax.quiver(x,y,U/(mag+1e-8),V/(mag+1e-8),mag,cmap='viridis',pivot='mid')
    ax.set(xlim=(-2.25,2.25),ylim=(-2.25,2.25),title=title,xlabel='x',ylabel='y');ax.set_aspect('equal');ax.grid(alpha=.15)
fig.tight_layout();save('ch6_fields.pdf')

t=np.linspace(0,2*np.pi,300);fig,ax=plt.subplots(figsize=(5.7,5.4));ax.plot(np.cos(t),np.sin(t),color='#205c91',lw=2.5)
for tt in np.arange(0,2*np.pi,np.pi/4):
    xx,yy=np.cos(tt),np.sin(tt);ax.arrow(xx,yy,-.25*yy,.25*xx,width=.012,color='#a44124',length_includes_head=True)
ax.set(xlim=(-1.55,1.55),ylim=(-1.55,1.55),xlabel='x',ylabel='y',title='Positive circulation on the unit circle');ax.set_aspect('equal');ax.grid(alpha=.15);save('ch6_circulation.pdf')

fig,ax=plt.subplots(figsize=(7.5,5.1));t=np.linspace(0,2*np.pi,500)
ax.fill(2.2*np.cos(t),1.5*np.sin(t),color='#d7e7f4',alpha=.9)
ax.fill(.65*np.cos(t),.52*np.sin(t),color='white')
ax.plot(2.2*np.cos(t),1.5*np.sin(t),'#225b8b',lw=2);ax.plot(.65*np.cos(t),.52*np.sin(t),'#9a442a',lw=2)
for a,b,r,sign,color in [(2.2,1.5,1,1,'#225b8b'),(.65,.52,1,-1,'#9a442a')]:
    for tt in [0.5,2.4,4.5]:
        px,py=a*np.cos(tt),b*np.sin(tt);dx=-a*np.sin(tt)*sign*.13;dy=b*np.cos(tt)*sign*.13
        ax.arrow(px,py,dx,dy,color=color,width=.018,length_includes_head=True)
ax.text(1,0,'D',fontsize=15);ax.text(-2.5,1.75,'outer: CCW');ax.text(-.5,-.1,'hole');ax.set_aspect('equal');ax.set(xlim=(-2.8,2.8),ylim=(-2.05,2.05),xlabel='x',ylabel='y',title='Boundary orientations for a region with a hole');ax.grid(alpha=.1);save('ch6_green.pdf')

u=np.linspace(-1,1,36);v=np.linspace(-1,1,36);X,Y=np.meshgrid(u,v);Z=X**2+Y**2
fig=plt.figure(figsize=(7,5.3));ax=fig.add_subplot(projection='3d');ax.plot_surface(X,Y,Z,cmap='Blues',alpha=.78,edgecolor='none')
xx,yy=np.meshgrid(np.linspace(-.8,.8,5),np.linspace(-.8,.8,5));zz=xx**2+yy**2
ax.quiver(xx,yy,zz,-2*xx,-2*yy,np.ones_like(xx),length=.23,normalize=True,color='#a74624')
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Upward normal vectors on z = x² + y²');save('ch6_surface.pdf')

th=np.linspace(0,2*np.pi,80);rr=np.linspace(0,1,25);T,R=np.meshgrid(th,rr);X=R*np.cos(T);Y=R*np.sin(T)
fig=plt.figure(figsize=(10,4.6));a=fig.add_subplot(121,projection='3d');a.plot_surface(X,Y,0*X,color='#8dbbd5',alpha=.65,linewidth=0);a.plot(np.cos(th),np.sin(th),0*th,color='#a44224',lw=2);a.set(xlabel='x',ylabel='y',zlabel='z',title='Flat disk')
b=fig.add_subplot(122,projection='3d');b.plot_surface(X,Y,np.sqrt(np.maximum(0,1-R**2)),cmap='Blues',alpha=.85,linewidth=0);b.plot(np.cos(th),np.sin(th),0*th,color='#a44224',lw=2);b.set(xlabel='x',ylabel='y',zlabel='z',title='Upper hemisphere');fig.tight_layout();save('ch6_stokes.pdf')

fig,ax=plt.subplots(figsize=(6.2,5.7));t=np.linspace(0,2*np.pi,300);ax.plot(np.cos(t),np.sin(t),color='#205c91',lw=2)
for tt in np.arange(0,2*np.pi,np.pi/6):
    xx,yy=np.cos(tt),np.sin(tt);ax.arrow(.8*xx,.8*yy,.45*xx,.45*yy,color='#a74624',width=.015,length_includes_head=True)
ax.set_aspect('equal');ax.set(xlim=(-1.55,1.55),ylim=(-1.55,1.55),xlabel='x',ylabel='y',title='Outward flux across a circular boundary');ax.grid(alpha=.15);save('ch6_flux.pdf')
print('Created six Chapter 6 figures')
