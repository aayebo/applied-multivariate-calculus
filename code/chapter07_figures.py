"""Original reproducible illustrations for Chapter 7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parents[1]/'figures'; OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'savefig.bbox':'tight'})

def save(name):
    plt.savefig(OUT/name, dpi=180); plt.close()

# Coordinate grid and non-unit polar basis
fig,ax=plt.subplots(figsize=(6.8,5.0)); theta=np.linspace(0,2*np.pi,350)
for r in [0.5,1,1.5,2]:ax.plot(r*np.cos(theta),r*np.sin(theta),color='#cad5de',lw=.8)
for t in np.linspace(0,2*np.pi,12,endpoint=False):ax.plot([0,2.1*np.cos(t)],[0,2.1*np.sin(t)],color='#cad5de',lw=.8)
t=.75;r=1.35;p=np.array([r*np.cos(t),r*np.sin(t)]);er=np.array([np.cos(t),np.sin(t)]);et=np.array([-np.sin(t),np.cos(t)])
ax.arrow(*p,*(.55*er),width=.018,color='#006d77',length_includes_head=True);ax.arrow(*p,*(.55*et),width=.018,color='#b24c36',length_includes_head=True)
ax.text(*(p+.65*er),r'$\mathbf{e}_r$',color='#006d77');ax.text(*(p+.65*et),r'$\mathbf{e}_\theta$',color='#b24c36');ax.scatter(*p,c='black');ax.set_aspect('equal');ax.set_xlim(-2.25,2.25);ax.set_ylim(-2.25,2.25);ax.set_title('Polar coordinate grid and orthonormal directions');save('ch7_polar_basis.pdf')

# Cylinder with tangent plane
u=np.linspace(0,2*np.pi,65);v=np.linspace(-1.5,1.5,35);U,V=np.meshgrid(u,v);fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d');ax.plot_surface(np.cos(U),np.sin(U),V,color='#75a9b5',alpha=.45,linewidth=0)
u0=.75;z0=.25;point=np.array([np.cos(u0),np.sin(u0),z0]);s,t=np.meshgrid(np.linspace(-.7,.7,12),np.linspace(-.8,.8,12));X=point[0]-np.sin(u0)*s;Y=point[1]+np.cos(u0)*s;Z=point[2]+t
ax.plot_surface(X,Y,Z,color='#edc56a',alpha=.58);ax.quiver(*point,*[-np.sin(u0),np.cos(u0),0],length=.85,color='#b24c36');ax.quiver(*point,*[0,0,1],length=.85,color='#006d77');ax.set(xlabel='x',ylabel='y',zlabel='z',title='Cylinder and its tangent plane');save('ch7_tangent_cylinder.pdf')

# Sphere great circle and non-geodesic latitude
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d');u=np.linspace(0,2*np.pi,75);v=np.linspace(0,np.pi,35);U,V=np.meshgrid(u,v);ax.plot_surface(np.sin(V)*np.cos(U),np.sin(V)*np.sin(U),np.cos(V),alpha=.16,color='#88b4c1',linewidth=0)
t=np.linspace(0,2*np.pi,400);ax.plot(np.cos(t),np.sin(t),0*t,lw=2.5,color='#b24c36',label='great circle (geodesic)');a=np.pi/4;ax.plot(np.sin(a)*np.cos(t),np.sin(a)*np.sin(t),np.cos(a)+0*t,lw=2,color='#006d77',label='latitude (not geodesic)');ax.legend(loc='upper left',fontsize=8);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Great circles versus latitude circles');save('ch7_sphere_geodesic.pdf')

# Gaussian curvature profiles
fig,axs=plt.subplots(1,3,figsize=(11,3.5),subplot_kw={'projection':'3d'});q=np.linspace(-1.2,1.2,55);X,Y=np.meshgrid(q,q)
for ax,Z,title in zip(axs,[np.zeros_like(X),.35*(X**2+Y**2),.4*(X**2-Y**2)],['Plane: K=0','Elliptic paraboloid: K>0','Saddle: K<0']):
 ax.plot_surface(X,Y,Z,cmap='viridis',linewidth=0,alpha=.85);ax.set_title(title,fontsize=10);ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([])
save('ch7_curvature_surfaces.pdf')

# Helix Frenet frame
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d');t=np.linspace(0,4*np.pi,400);ax.plot(np.cos(t),np.sin(t),.18*t,color='#274e68',lw=2);t0=2.3;p=np.array([np.cos(t0),np.sin(t0),.18*t0]);T=np.array([-np.sin(t0),np.cos(t0),.18])/np.sqrt(1+.18**2);N=np.array([-np.cos(t0),-np.sin(t0),0]);B=np.cross(T,N)
for w,c,l in [(T,'#006d77','T'),(N,'#b24c36','N'),(B,'#986bb0','B')]:ax.quiver(*p,*w,length=.8,color=c,linewidth=2);ax.text(*(p+.85*w),l,color=c)
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Frenet–Serret frame on a helix');save('ch7_frenet_helix.pdf')

# Metric deformation polar grid
fig,axs=plt.subplots(1,2,figsize=(10,4));r=np.linspace(.2,2,5);theta=np.linspace(0,2*np.pi,300)
for ax,stretch,title in [(axs[0],1,'Euclidean polar grid'),(axs[1],1.7,'Coordinate deformation')]:
 for a in r:ax.plot(a*np.cos(theta),stretch*a*np.sin(theta),color='#2d728f',lw=1)
 for b in np.linspace(0,2*np.pi,16,endpoint=False):ax.plot([0,2.1*np.cos(b)],[0,stretch*2.1*np.sin(b)],color='#a6b9c6',lw=.7)
 ax.set_aspect('equal');ax.set_xlim(-2.4,2.4);ax.set_ylim(-3.8,3.8);ax.set_title(title)
save('ch7_metric_grid.pdf')
print('Created 6 figures')
