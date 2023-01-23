from numpy import *
def obj_fun(x):
    return pow(x[0]-3,2)+pow(x[1]-2,2)
def con_fun(x):
    g=zeros((4,1),dtype=float)
    g[0]=pow(x[0],2)+pow(x[1],2)-5
    g[1]=x[0]+2*x[1]-4
    g[2],g[3]=-x[0],-x[1]
    return g
from interior_point_solver import *
x0,fval,con_val,iter1,lagrange_mult=interior_point_solver(obj_fun,con_fun,10*ones((2,1),dtype=float))
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('optimalpoint=',x0,'\n')
print('objective value=',fval,'\n')
print('constraint value=',con_val,'\n')
print('no of iterations=',iter1)
print('Lagrange multiplier=',lagrange_mult)
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')