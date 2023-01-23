from numpy import *
#def fun(x):
#   n=len(x)
#   g=1+9/(n-1)*sum([x[i] for i in range(1,n)])
#   h=1-pow(x[0]/g,2)
#   return h*g
def fun(x):
    return 0.5*(100*pow(x[0]-pow(x[1],2),2)+pow(9-x[0],2))
    #4*x[0]**2-3*x[0]*x[1]+2*x[1]**2-x[0]+2*x[1]
        #
def gradf(x):
    f0,n,h1=fun(x),len(x),pow(10,-5)
    g=zeros((n,1),dtype=float)
    for i in range(0,n):
        x1=x.copy()
        x1[i]=x1[i]+h1
       # print(x,x1)
        g[i]=(fun(x1)-f0)/h1
    return g
#(R,R+1), R is last two digits of your roll number
x0,beta1,beta2,r,eps,iter1,B0,countf,countg=array([[18.0],[18.0]]),pow(10,-4),0.9,0.5,pow(10,-3),0,\
                                            identity(2,dtype=float),0,0
f0,g0=fun(x0),gradf(x0)
countf+=1
countg+=1
while linalg.norm(g0)>eps and iter1<1000:
    d0,alpha=-dot(linalg.inv(B0),g0),1
    print(g0.T@d0)
    x1=x0+alpha*d0
    f1,g1=fun(x1),gradf(x1)
    countf += 1
    countg += 1
    while (f1>f0+alpha*beta1*g0.T@d0 or\
            dot(g1.T,d0)<beta2*dot(g0.T,d0)) and alpha>pow(10,-5):
        alpha=alpha*r
        x1 = x0 + alpha * d0
        f1, g1 = fun(x1), gradf(x1)
        countf += 1
        countg += 1
    dt1,s1=x1-x0,g1-g0
    B0=B0+1/(dt1.T@s1)*s1@s1.T-1/(s1.T@B0@s1)*B0@s1@s1.T@B0
    print(B0)
    print(alpha,fun(x0+alpha*d0)-fun(x0))
    x0,g0,iter1=x1,g1,iter1+1
print(x0,iter1,countf,countg)