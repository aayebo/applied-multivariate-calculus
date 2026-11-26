"""Original, reproducible diagrams for Chapter 2."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
OUT = Path(__file__).resolve().parents[1] / 'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.titlesize':11,'savefig.bbox':'tight'})
def save(name):
    plt.savefig(OUT/name, dpi=180); plt.close()

# 1 Helix, tangent, normal, and binormal (at t=1.5)
t=np.linspace(0,4*np.pi,450); a=.35
r=lambda t:np.array([np.cos(t),np.sin(t),a*t]); v=lambda t:np.array([-np.sin(t),np.cos(t),a]);
t0=1.5; p=r(t0); T=v(t0)/np.linalg.norm(v(t0)); N=np.array([-np.cos(t0),-np.sin(t0),0]); B=np.cross(T,N)
fig=plt.figure(figsize=(6.7,5));ax=fig.add_subplot(projection='3d');ax.plot(np.cos(t),np.sin(t),a*t,color='#174b76',lw=2)
for w,c,label in [(T,'#c35b31','T'),(N,'#198675','N'),(B,'#8e58a5','B')]:
    ax.quiver(*p,*w,length=.85,normalize=True,color=c,linewidth=2);q=p+.94*w;ax.text(*q,label,color=c,fontsize=12,weight='bold')
ax.scatter(*p,color='black',s=23);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Helix and the Frenet frame');ax.view_init(24,52);save('helix_frenet.pdf')

# 2 tangent line and curvature for parabola
x=np.linspace(-1.6,1.8,400);x0=.7;y0=x0*x0
fig,ax=plt.subplots(figsize=(6.4,4.2));ax.plot(x,x*x,lw=2,color='#174b76',label=r'$y=x^2$');ax.plot(x,y0+2*x0*(x-x0),'--',color='#c35b31',label='tangent');ax.scatter([x0],[y0],color='black');ax.set(xlabel='x',ylabel='y',title='Tangent line to a parametrized curve');ax.legend();ax.set_aspect('equal',adjustable='datalim');ax.grid(alpha=.2);save('tangent_curve.pdf')

# 3 polar coordinates grid
fig,ax=plt.subplots(figsize=(5.8,5.1));tt=np.linspace(0,2*np.pi,500)
for rr in [.5,1,1.5,2]:ax.plot(rr*np.cos(tt),rr*np.sin(tt),color='#b8cbd6',lw=.9)
for th in np.arange(0,2*np.pi,np.pi/6):ax.plot([0,2.1*np.cos(th)],[0,2.1*np.sin(th)],color='#b8cbd6',lw=.9)
th=np.pi/3;rr=1.6;ax.plot([0,rr*np.cos(th)],[0,rr*np.sin(th)],color='#c35b31',lw=2.5);ax.scatter([rr*np.cos(th)],[rr*np.sin(th)],color='#174b76',s=35);ax.text(.86,1.48,r'$(r,\theta)$');ax.set(xlabel='x',ylabel='y',title='Polar coordinates');ax.set_aspect('equal');ax.set_xlim(-2.2,2.2);ax.set_ylim(-2.2,2.2);ax.grid(alpha=.15);save('polar_grid.pdf')

# 4 cylindrical coordinates helix
fig=plt.figure(figsize=(6.3,4.8));ax=fig.add_subplot(projection='3d');tt=np.linspace(0,3*np.pi,400);ax.plot(1.2*np.cos(tt),1.2*np.sin(tt),.32*tt,color='#174b76',lw=2);ax.plot(1.2*np.cos(tt),1.2*np.sin(tt),0,'--',color='#198675',alpha=.7);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Cylindrical coordinates: fixed radius');ax.view_init(23,42);save('cylindrical_helix.pdf')

# 5 spherical coordinates wire sphere and radius
fig=plt.figure(figsize=(6.3,4.8));ax=fig.add_subplot(projection='3d');u=np.linspace(0,2*np.pi,70);v0=np.linspace(0,np.pi,35);X=2*np.outer(np.cos(u),np.sin(v0));Y=2*np.outer(np.sin(u),np.sin(v0));Z=2*np.outer(np.ones_like(u),np.cos(v0));ax.plot_wireframe(X,Y,Z,rstride=9,cstride=6,color='#7cabc5',linewidth=.5,alpha=.5)
phi=np.pi/3;theta=np.pi/4;p=2*np.array([np.sin(phi)*np.cos(theta),np.sin(phi)*np.sin(theta),np.cos(phi)]);ax.plot([0,p[0]],[0,p[1]],[0,p[2]],color='#c35b31',lw=2.7);ax.scatter(*p,color='black',s=25);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Spherical coordinates: radial segment');ax.view_init(20,36);save('spherical_coordinates.pdf')

# 6 surface of revolution
u=np.linspace(0,2*np.pi,90);v=np.linspace(-1.5,1.5,60);U,V=np.meshgrid(u,v);R=1+.22*V**2;X=R*np.cos(U);Y=R*np.sin(U);Z=V
fig=plt.figure(figsize=(6.3,4.8));ax=fig.add_subplot(projection='3d');ax.plot_surface(X,Y,Z,cmap='viridis',alpha=.82,linewidth=0,rstride=2,cstride=2);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Parametrized surface of revolution');ax.view_init(25,42);save('surface_revolution.pdf')

# 7 hyperbolic paraboloid
u=np.linspace(-1.5,1.5,65);X,Y=np.meshgrid(u:=u[:1]*0+np.linspace(-1.5,1.5,65),v:=np.linspace(-1.5,1.5,65));Z=X**2-Y**2
fig=plt.figure(figsize=(6.3,4.8));ax=fig.add_subplot(projection='3d');ax.plot_surface(X,Y,Z,cmap='coolwarm',alpha=.9,linewidth=0);ax.set(xlabel='x',ylabel='y',zlabel='z',title=r'Saddle surface $z=x^2-y^2$');ax.view_init(25,50);save('saddle_surface.pdf')

# 8 osculating circle for parabola at origin, kappa=2 radius .5
fig,ax=plt.subplots(figsize=(6.0,4.5));xx=np.linspace(-.85,.85,400);ax.plot(xx,xx**2,color='#174b76',lw=2.4,label=r'$y=x^2$');th=np.linspace(0,2*np.pi,500);ax.plot(.5*np.cos(th),.5+.5*np.sin(th),'--',color='#c35b31',lw=1.8,label='osculating circle');ax.scatter([0],[0],color='black');ax.scatter([0],[.5],color='#c35b31');ax.set(xlim=(-.9,.9),ylim=(-.12,1.2),xlabel='x',ylabel='y',title='Curvature and the osculating circle');ax.set_aspect('equal');ax.legend();ax.grid(alpha=.15);save('osculating_circle.pdf')
print('Created 8 original figures in',OUT)
