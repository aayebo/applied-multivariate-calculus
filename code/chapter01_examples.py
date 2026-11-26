"""Executable Chapter 1 examples and exact/numerical assertions."""
import numpy as np
import sympy as sp

u = np.array([2., -1., 2.]); v = np.array([1., 3., -2.])
assert np.isclose(np.linalg.norm(u), 3)
assert np.allclose(u+v, [3, 2, 0])

us = sp.Matrix([1,2,2]); vs = sp.Matrix([2,0,1])
cos_theta = sp.simplify(us.dot(vs)/(us.norm()*vs.norm()))
assert sp.simplify(cos_theta-4/(3*sp.sqrt(5))) == 0
print('Angle:',float(sp.acos(cos_theta)*180/sp.pi))

r = np.array([2.,0.,0.]); f = np.array([0.,3.,4.])
torque=np.cross(r,f)
assert np.allclose(torque,[0,-8,6])

u=np.array([1,0,2]);v=np.array([0,2,1]);w=np.array([2,1,0])
assert np.dot(u,np.cross(v,w))==-9

A=np.array([[1,1,1],[1,-1,1],[2,1,-1]],float)
b=np.array([6,2,1],float)
assert np.allclose(np.linalg.solve(A,b),[1,2,3])

A,B,C=(sp.Matrix(q) for q in [(1,0,1),(2,1,1),(1,2,3)])
P=sp.Matrix([3,1,4]);n=(B-A).cross(C-A)/2;d=n.dot(A)
signed=n.dot(P)-d
Q=sp.simplify(P-signed/n.dot(n)*n)
assert Q==sp.Matrix([sp.Rational(5,3),sp.Rational(7,3),sp.Rational(8,3)])
assert sp.simplify(n.dot(Q)-d)==0
assert (P-Q).cross(n)==sp.zeros(3,1)
print('All Chapter 1 computational checks passed.')
