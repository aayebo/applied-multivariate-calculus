from pathlib import Path
import nbformat as nbf
root=Path(__file__).resolve().parent.parent
n=nbf.v4.new_notebook()
n.cells=[
nbf.v4.new_markdown_cell('# Chapter 3 — Functions of Several Variables and Partial Differentiation\nOriginal computational companion for *Multivariable Calculus Using Python*. Run cells in order.'),
nbf.v4.new_code_cell('import numpy as np\nimport sympy as sp\nimport matplotlib.pyplot as plt\nsp.init_printing()\nx,y=sp.symbols("x y",real=True)'),
nbf.v4.new_markdown_cell('## 1. Symbolic partial derivatives\nCompute first and second derivatives, then compare the mixed partials.'),
nbf.v4.new_code_cell('f=x**2*sp.exp(x*y)+sp.sin(y)\nfx,fy=sp.diff(f,x),sp.diff(f,y)\ndisplay(fx,fy,sp.simplify(sp.diff(fx,y)-sp.diff(fy,x)))'),
nbf.v4.new_markdown_cell('## 2. Level curves and surface graphs'),
nbf.v4.new_code_cell('a=np.linspace(-2,2,120)\nX,Y=np.meshgrid(a,a)\nZ=2+.6*X**2+.9*Y**2\nfig,ax=plt.subplots()\nc=ax.contour(X,Y,Z,levels=10)\nax.clabel(c);ax.set_aspect("equal");plt.show()'),
nbf.v4.new_markdown_cell('## 3. Tangent-plane error\nFor $f(x,y)=x^2+2y^2$ at $(1,1/2)$, compare the exact function with its tangent plane.'),
nbf.v4.new_code_cell('xx,yy=np.meshgrid(np.linspace(.5,1.5,80),np.linspace(0,1,80))\nexact=xx**2+2*yy**2\nlinear=1.5+2*(xx-1)+2*(yy-.5)\nerr=exact-linear\nprint("Maximum error:",np.max(np.abs(err)))\nplt.contourf(xx,yy,err,levels=18);plt.colorbar(label="Exact - linear");plt.show()'),
nbf.v4.new_markdown_cell('## 4. Chain rule check'),
nbf.v4.new_code_cell('t=sp.symbols("t",real=True)\ng=x**2*sp.exp(x*y)+sp.sin(y)\npath={x:t**2,y:sp.sin(t)}\nby_substitution=sp.diff(g.subs(path),t)\nby_chain=sp.diff(g,x).subs(path)*2*t+sp.diff(g,y).subs(path)*sp.cos(t)\nassert sp.simplify(by_substitution-by_chain)==0\nprint("Chain rule verified")'),
nbf.v4.new_markdown_cell('## 5. Finite-difference convergence\nCompare the forward and centered approximations for $f_x(0.8,0.6)$.'),
nbf.v4.new_code_cell('fn=lambda a,b:a*a+2*b*b\nsteps=10.**(-np.arange(1,9,dtype=float))\nforward=np.array([(fn(.8+h,.6)-fn(.8,.6))/h for h in steps])\ncentral=np.array([(fn(.8+h,.6)-fn(.8-h,.6))/(2*h) for h in steps])\nplt.loglog(steps,np.abs(forward-1.6),"o-",label="Forward")\nplt.loglog(steps,np.maximum(np.abs(central-1.6),1e-16),"s-",label="Centered")\nplt.xlabel("Step size");plt.ylabel("Absolute error");plt.legend();plt.show()'),
nbf.v4.new_markdown_cell('## 6. Extended project\nInvestigate $f(x,y)=\\sin x\\cos y + x^2/4$ near the origin. Find its gradient and Hessian, construct linear and quadratic approximations, and compare maximal angular error for radii $0.4,0.2,0.1,0.05$.'),
nbf.v4.new_code_cell('F=sp.sin(x)*sp.cos(y)+x**2/sp.Integer(4)\ngrad=sp.Matrix([sp.diff(F,x),sp.diff(F,y)])\nH=sp.hessian(F,(x,y))\ndisplay(grad.subs({x:0,y:0}),H.subs({x:0,y:0}))\n# TODO: evaluate approximation errors on circles of decreasing radius')]
n.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'}}
nbf.write(n,root/'notebooks'/'chapter03.ipynb')
print('Notebook created')
