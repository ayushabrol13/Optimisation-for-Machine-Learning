"""
LAB - 10
Integer Programming Problem 

"""

from gekko import GEKKO
import numpy as np
import math


m = GEKKO(remote=False)
A = np.array([[5,7],[4,1],[3,-2],[-1, 0],[0, -1]], dtype=np.float64)
b = np.array([[27],[14],[9],[0],[0]],dtype=np.float64)
c = np.array([[7],[3]],dtype=np.float64)

z1=m.Var(1,integer=True,lb=0,ub=1)
z2=m.Var(1,integer=False,lb=0,ub=100)
z=[z1,z2]
print(z1,z2,z)

m.qobj(c,x=z,otype='max')
m.axb(A,b,x=z,etype='<=')
m.options.SOLVER = 1
m.solve()
print('Objective: ', m.options.OBJFCNVAL)
print(z)
print('x: ', z[0].value[0])
print('y: ', z[1].value[0])