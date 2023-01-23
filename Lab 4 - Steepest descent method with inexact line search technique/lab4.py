import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import math
import autograd. numpy as au
from autograd import grad, jacobian 
import scipy

def q1(R):
    def objective_function(x):
        return 4*x[0]**2 + 3*x[0]*x[1]+ 2*x[1]**2 + x[0] + 2*x[1]

    def grad_function(x):
        f0,n,h1 = objective_function(x), len(x), math.pow(10,-5)
        g = np.zeros((n,1))
        for i in range(0,n):
            x1 = x.copy()
            x1[i]= x1[i] + h1
            g[i] = (objective_function(x1) - f0)/h1
        return g

    n = 25 + int(R%10)
    x0 = np.array([[float(R)],[float(R+1)]])
    beta_1 = math.pow(10,-4)
    beta_2 = 0.9
    r = 0.5
    eps = math.pow(10,-3)
    iter = 0
    while np.linalg.norm(grad_function(x0)) > eps and iter<1000:
        d0, alpha = -grad_function(x0),1
        while objective_function(x0 + alpha*d0) > objective_function(x0) + alpha*beta_1*np.dot(grad_function(x0).T,d0) or np.dot(grad_function(x0 + alpha*d0).T,d0) < beta_2*np.dot(grad_function(x0).T,d0):
            alpha = alpha*r
            # print(objective_function(x0 + alpha*d0) - objective_function(x0))
        print(alpha)
        x0, iter = x0 + alpha*d0, iter + 1
    print(x0, iter)

def q2(R):
    def objective_function(x):
        n = len(x)
        odd_num = [i for i in range(1,n) if i%2 != 0]
        sum = 0
        for i in range(len(odd_num)):
            sum = sum + (float(x[i]) - math.sin(6*math.pi*x[0] + i*math.pi/n))**2
        return x[0] + (2/len(odd_num))*sum

    def grad_function(x):
        f0,n,h1 = objective_function(x), len(x), math.pow(10,-5)
        g = np.zeros((n,1))
        for i in range(0,n):
            x1 = x.copy()
            x1[i]= x1[i] + h1
            g[i] = (objective_function(x1) - f0)/h1
        return g
    
    n = 25 + R
    x0 = np.ones((25,1), dtype=float)
    beta_1 = math.pow(10,-4)
    beta_2 = 0.9
    r = 0.5
    eps = math.pow(10,-3)
    iter = 0

    while np.linalg.norm(grad_function(x0)) > eps and iter<1000:
        d0, alpha = -grad_function(x0),1
        while objective_function(x0 + alpha*d0) > objective_function(x0) + alpha*beta_1*np.dot(grad_function(x0).T,d0) or np.dot(grad_function(x0 + alpha*d0).T,d0) < beta_2*np.dot(grad_function(x0).T,d0):
            alpha = alpha*r
        # print(objective_function(x0 + alpha*d0) - objective_function(x0))
        # print(alpha)
        x0, iter = x0 + alpha*d0, iter + 1
    print(x0, iter)

def q3(R):
    def objective_function(x):
        n = len(x)
        even_num = [i for i in range(1,n) if i%2 == 0]
        sum = 0
        for i in range(len(even_num)):
            sum = sum + (float(x[i]) - math.sin(6*math.pi*x[0] + i*math.pi/n))**2
        return x[0] + (2/len(even_num))*sum

    def grad_function(x):
        f0,n,h1 = objective_function(x), len(x), math.pow(10,-5)
        g = np.zeros((n,1))
        for i in range(0,n):
            x1 = x.copy()
            x1[i]= x1[i] + h1
            g[i] = (objective_function(x1) - f0)/h1
        return g

    n = 25
    x0 = np.ones((25,1), dtype=float)
    beta_1 = math.pow(10,-4)
    beta_2 = 0.9
    r = 0.5
    eps = math.pow(10,-3)
    iter = 0

    while np.linalg.norm(grad_function(x0)) > eps and iter<1000:
        d0, alpha = -grad_function(x0),1
        while objective_function(x0 + alpha*d0) > objective_function(x0) + alpha*beta_1*np.dot(grad_function(x0).T,d0) or np.dot(grad_function(x0 + alpha*d0).T,d0) < beta_2*np.dot(grad_function(x0).T,d0):
            alpha = alpha*r
        # print(objective_function(x0 + alpha*d0) - objective_function(x0))
        # print(alpha)
        x0, iter = x0 + alpha*d0, iter + 1
    print(x0, iter)


def main():
    # R = int(input("Last two digits of your roll no. --> "))
    # q1(R)
    R = int(input("Last digit of your roll no. --> "))
    # q2(R)
    q3(R)

if __name__ == "__main__":
    main()