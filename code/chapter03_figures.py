"""Original figures for Chapter 3; run from textbook project root."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
out=Path(__file__).resolve().parent.parent/'figures';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'figure.dpi':130,'savefig.bbox':'tight'})

def save(name):
    plt.savefig(out/name);plt.close()

x=np.linspace(-2,2,130);y=np.linspace(-2,2,130);X,Y=np.meshgrid(x,y)
Z=2+0.6*X**2+0.9*Y**2
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(projection='3d');ax.plot_surface(X,Y,Z,cmap='viridis',alpha=.9,rstride=3,cstride=3);ax.set(xlabel='x',ylabel='y',zlabel='f(x,y)',title='A function of two variables');save('ch3_surface.pdf')
fig,ax=plt.subplots(figsize=(6,5));co=ax.contour(X,Y,Z,levels=[2.2,2.5,3,3.8,5],cmap='viridis');ax.clabel(co);ax.set(xlabel='x',ylabel='y',title='Level curves of the same function',aspect='equal');save('ch3_contours.pdf')
# Path-dependent limit: xy/(x^2+y^2) along two paths
xx=np.linspace(-1,1,500);fig,ax=plt.subplots(figsize=(6.5,4));ax.plot(xx,np.zeros_like(xx),label='y = 0: f = 0');ax.plot(xx,np.full_like(xx,.5),label='y = x: f = 1/2');ax.set(xlabel='x (x ≠ 0)',ylabel='function value',ylim=(-.1,.7),title='Two paths toward (0,0)');ax.legend();save('ch3_path_limit.pdf')
# tangent plane for f=x^2+2y^2 at (1,.5)
X,Y=np.meshgrid(np.linspace(.2,1.8,45),np.linspace(-.25,1.25,45));Z=X**2+2*Y**2;T=1.5+2*(X-1)+2*(Y-.5)
fig=plt.figure(figsize=(7,5));ax=fig.add_subplot(projection='3d');ax.plot_surface(X,Y,Z,alpha=.68,cmap='viridis');ax.plot_surface(X,Y,T,alpha=.4,color='orange');ax.scatter([1],[.5],[1.5],color='black',s=32);ax.set(xlabel='x',ylabel='y',zlabel='z',title='Tangent plane as local linear model');save('ch3_tangent_plane.pdf')
# directional derivative as slope on contour
x=np.linspace(-2,2,220);y=np.linspace(-2,2,220);X,Y=np.meshgrid(x,y);Z=X**2+2*Y**2
fig,ax=plt.subplots(figsize=(6,5));cs=ax.contour(X,Y,Z,levels=np.arange(.5,9,.75),cmap='Blues');ax.clabel(cs,fontsize=7);p=np.array([.8,.6]);g=np.array([1.6,2.4]);u=np.array([1.,.4]);u=u/np.linalg.norm(u);ax.quiver(*p,*g,angles='xy',scale_units='xy',scale=1,color='crimson',label='gradient');ax.quiver(*p,*u,angles='xy',scale_units='xy',scale=1,color='darkgreen',label='unit direction');ax.set(xlim=(-1.6,2),ylim=(-1.6,2),xlabel='x',ylabel='y',aspect='equal',title='Gradient and a directional derivative');ax.legend(loc='upper left');save('ch3_directional.pdf')
# discontinuity and domain boundary
x=np.linspace(-1.7,1.7,350);y=np.linspace(-1.7,1.7,350);X,Y=np.meshgrid(x,y);mask=(X**2+Y**2<=1.8);F=np.where(mask,np.sqrt(np.maximum(1.8-X**2-Y**2,0)),np.nan)
fig,ax=plt.subplots(figsize=(6,5));im=ax.pcolormesh(X,Y,F,cmap='viridis',shading='auto');ax.contour(X,Y,X**2+Y**2,levels=[1.8],colors='black');fig.colorbar(im,ax=ax,label='sqrt(1.8 - x² - y²)');ax.set(xlabel='x',ylabel='y',aspect='equal',title='Domain and boundary of a square-root function');save('ch3_domain.pdf')
print('Generated six Chapter 3 figures.')
