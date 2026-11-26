"""Original reproducible figures for Chapter 1. Python 3, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
OUT=Path(__file__).resolve().parents[1]/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'figure.dpi':140,'savefig.dpi':180})

def save(name):
    plt.tight_layout();plt.savefig(OUT/name,bbox_inches='tight');plt.close()

# Three-dimensional vectors and vector addition
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d')
a=np.array([2.,1.,1.]);b=np.array([1.,2.,.5]);c=a+b
for vec,color,label in [(a,'#1b75bc',r'$\mathbf{a}$'),(b,'#dc6b19',r'$\mathbf{b}$'),(c,'#34824c',r'$\mathbf{a}+\mathbf{b}$')]:
    ax.quiver(0,0,0,*vec,color=color,arrow_length_ratio=.10,linewidth=2,label=label)
ax.plot([a[0],c[0]],[a[1],c[1]],[a[2],c[2]],'--',color='#dc6b19',alpha=.7)
ax.plot([b[0],c[0]],[b[1],c[1]],[b[2],c[2]],'--',color='#1b75bc',alpha=.7)
ax.set(xlim=(0,3.5),ylim=(0,3.5),zlim=(0,2.5),xlabel='x',ylabel='y',zlabel='z',title='Vector addition in three dimensions')
ax.legend(loc='upper left');save('vector_addition.pdf')

# Dot product and projection
fig,ax=plt.subplots(figsize=(7,4.6));u=np.array([4.,1.]);v=np.array([2.,3.]);proj=np.dot(v,u)/np.dot(u,u)*u
for vec,color,label in [(u,'#1b75bc','u'),(v,'#dc6b19','v'),(proj,'#34824c','proj_u(v)')]:
 ax.annotate('',xy=vec,xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=2.5,color=color));ax.text(*(vec+np.array([.1,.12])),label,color=color)
ax.plot([v[0],proj[0]],[v[1],proj[1]],'k--',lw=1.2);ax.scatter([proj[0]],[proj[1]],c='k',s=15)
ax.set(xlim=(-.4,4.8),ylim=(-.4,3.7),xlabel='x',ylabel='y',title='Orthogonal projection onto a vector');ax.set_aspect('equal');ax.grid(alpha=.25);save('projection.pdf')

# Cross product parallelogram
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d')
a=np.array([2.,0.,1.]);b=np.array([.4,2.,.3]);n=np.cross(a,b);n=n/np.linalg.norm(n)*2.2
poly=np.array([[0,0,0],a,a+b,b,[0,0,0]])
ax.plot(poly[:,0],poly[:,1],poly[:,2],color='#1b75bc',lw=2)
for vec,color in [(a,'#1b75bc'),(b,'#dc6b19'),(n,'#34824c')]:ax.quiver(0,0,0,*vec,color=color,arrow_length_ratio=.13,linewidth=2)
ax.text(*(n*1.12),'normal',color='#34824c');ax.set(xlabel='x',ylabel='y',zlabel='z',title='Cross product: oriented area and normal direction');save('cross_product.pdf')

# Plane and normal
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(111,projection='3d')
x,y=np.meshgrid(np.linspace(-1.6,1.6,30),np.linspace(-1.6,1.6,30));z=(4-2*x-y)/2
ax.plot_surface(x,y,z,alpha=.55,cmap='Blues',edgecolor='none');p=np.array([0.,0.,2.]);n=np.array([2.,1.,2.]);n=n/np.linalg.norm(n)*2
ax.quiver(*p,*n,color='#b34c30',linewidth=3,arrow_length_ratio=.18);ax.scatter(*p,color='black');ax.set(xlabel='x',ylabel='y',zlabel='z',title='Plane 2x + y + 2z = 4 and a normal vector');save('plane_normal.pdf')

# Distance to plane diagram 2D cross section
fig,ax=plt.subplots(figsize=(7,4.4));xx=np.linspace(-2,4,200);yy=(4-2*xx)/2
ax.plot(xx,yy,color='#1b75bc',lw=2,label='Plane cross-section');P=np.array([2.,3.]);normal=np.array([2.,2.]);Q=P-((np.dot(normal,P)-4)/np.dot(normal,normal))*normal
ax.scatter([P[0],Q[0]],[P[1],Q[1]],c=['#dc6b19','#34824c'],zorder=4);ax.plot([P[0],Q[0]],[P[1],Q[1]],'k--',lw=2)
ax.text(*(P+[.1,.12]),'P');ax.text(*(Q+[.1,-.25]),'Q (closest point)');ax.set(xlim=(-1,4),ylim=(-1,4),xlabel='x',ylabel='z',title='Shortest distance is measured along a normal');ax.set_aspect('equal');ax.grid(alpha=.25);save('point_plane_distance.pdf')
print('Created',len(list(OUT.glob('*.pdf'))),'figures')
