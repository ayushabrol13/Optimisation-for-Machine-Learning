"""
LAB - 10
Integer Programming Problem 

"""

from gekko import GEKKO
import numpy as np
import math

m = GEKKO(remote=False)
A = np.array([[3,-2],[-8,10],[-1, 0]], dtype=np.float64)
b = np.array([[-1],[10],[-0.3]],dtype=np.float64)
c = np.array([[1],[1]],dtype=np.float64)

z1=m.Var(1,integer=False,lb=0.3,ub=1000)
z2=m.Var(1,integer=True,lb=0,ub=1)
z=[z1,z2]
print(z1,z2,z)

m.qobj(c,x=z,otype='min')
m.axb(A,b,x=z,etype='<=')
m.options.SOLVER = 1
m.solve()
print('Objective: ', m.options.OBJFCNVAL)
print(z)
print('x: ', z[0].value[0])
print('y: ', z[1].value[0])