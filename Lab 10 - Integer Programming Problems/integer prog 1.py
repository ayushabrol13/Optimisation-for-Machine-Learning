from gekko import GEKKO
from numpy import *
m = GEKKO(remote=False)
c = array([[9],[5],[6],[4]])
A = array([[6,3,5,2],[1,0,0,1],[-1,0,1,0],[0,-1,0,1]])
b = array([[9],[1],[0],[0]])
z = m.Array(m.Var,4,integer=True,lb=0,ub=1)
#z1=m.array(m.Var,1,integer=False,lb=0,ub=1)
m.qobj(c,x=z,otype='max')
m.axb(A,b,x=z,etype='<=')
#m.axb(A,b,x=z1,type='<=')
m.options.SOLVER = 1
m.solve()
print('Objective: ', m.options.OBJFCNVAL)
print(z)
#print('x: ', z[0].value[0],z[1].value[0],z[2].value[0],z[3].value[0])
#print('y: ', z[1].value[0])