from numpy import *
#from decimal import *
#getcontext().prec =50
def gradf(fun,x):
    n,h1=len(x),pow(10,-7)
    g=zeros((n,1),dtype=float)
    for i in range(0,n):
        x1,x2=x.copy(),x.copy()
        x1[i],x2[i]=x1[i]+h1,x2[i]-h1
       # print(x,x1)
        g[i]=(fun(x1)-fun(x))/(h1)
    return g
def quasi_newton(fun,con,x0):
    beta1,beta2,r,eps,iter1,n=pow(10,-4),0.9,0.5,pow(10,-5),0,len(x0)
    B0=identity(n,dtype=float)
    f0,g0=fun(x0),gradf(fun,x0)
    alpha=1
    while linalg.norm(g0)>eps and iter1<20000 and alpha>pow(10,-5):
        d0,alpha=-dot(linalg.inv(B0),g0),1
        #print(g0.T@d0)
        while max(con(x0+alpha*d0))>-0.000001:
            alpha=alpha*r
        #print(alpha)
        x1=x0+alpha*d0
        f1,g1=fun(x1),gradf(fun,x1)
        #print(f1-f0-alpha*beta1*g0.T@d0,dot(g1.T,d0)-beta2*dot(g0.T,d0))#or dot(g1.T,d0)<beta2*dot(g0.T,d0)
        while (f1>f0+alpha*beta1*g0.T@d0) and alpha>pow(10,-5):
            alpha=alpha*r
            x1 = x0 + alpha * d0
            f1, g1 = fun(x1),gradf(fun,x1)
        #print('f1=',f1)
        dt1,s1=x1-x0,g1-g0
        #print('xx=',dt1.T@s1,'alpha=',alpha)
        if dt1.T@s1>pow(10,-3):
            B0=B0+1/(dt1.T@s1)*s1@s1.T-1/(s1.T@B0@s1)*B0@s1@s1.T@B0
        #print(B0)
        # print(alpha,fun(x0+alpha*d0)-fun(x0))
        x0,g0,iter1=x1,g1,iter1+1
    if iter1>=20000:
        print('maximum iteration attains')
    #else:
    #    print('gg=',linalg.norm(g0))
    return x0
def interior_point_solver(obj_fun,con_fun,x0):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    sigma,opt_cond,iter1=10.0,1.0,0.0
    if max(con_fun(x0)) > -pow(10,-5):
        print('initial point is not strictly feasible. So starting phase 1')
        n = len(x0)
        y0 = zeros((n + 1, 1), dtype=float)
        y0[0:n], y0[n], sigma = x0, max(con_fun(x0) + 1), 10.0
        print(y0)
        def con_fun_phase_1(x):
            n = len(x)
            return con_fun(x[0:n]) - x[-1]
        while max(con_fun(y0[0:n])) > -0.001:
            def barr_phase_1(x):
                return x[-1] - 1 / sigma * sum(log(-con_fun_phase_1(x)))

            #y0 = optimize.fmin_cg(con_phase_1, y0,fprime= lambda x: gradf(con_fun_phase_1,x))
            y0 = quasi_newton(barr_phase_1, con_fun_phase_1, y0)
            #print(y0)
            sigma, iter1 = sigma * 10, iter1 + 1
        x0 = y0[0:n]
        print('Phase I complete')
        print('interior point=', x0,'\n','constraint_value=', con_fun(x0))
    else:
        print('initial approximation is an interior point so starting phase II directly')
    sigma=10
    opt_cond=1
    while len(con_fun(x0))/sigma > 0.00000001 and opt_cond >pow(10,-5):  # and max(con_fun(x0))<-0.00001:
        def barr_fun(x):
            return obj_fun(x) - 1 / sigma * sum(log(-con_fun(x)))
        x0 = quasi_newton(barr_fun, con_fun, x0)
        #print(obj_fun(x0), con_fun(x0))
        opt_cond = linalg.norm(gradf(barr_fun, x0))
        print(opt_cond)
        iter1+=1
        sigma=sigma*5
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(sigma)
    if len(con_fun(x0))/sigma <=0.00000001:
        print('maximum iterations attends')
    else:
        print('optimal solution found as norm KKT=',opt_cond,'<10^-7')
    return x0,obj_fun(x0), con_fun(x0),iter1, -10/sigma*1/con_fun(x0)
#########################################################################