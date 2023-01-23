import numpy as np
import copy, sys
import pandas as pd

def calculate_f(x, weights, y):
    """
    x.shape = (N,1)
    w.shape = (3,1)
    """
    x = np.hstack([x**2, x, np.ones(x.shape,dtype=np.float64)])
    return ((np.dot(x,weights) - y)**2).sum() / (2 * x.shape[0])

def grad_f(x:np.array, weights:np.array, y:np.array) -> np.array:
    new_x = np.hstack([x**2, x, np.ones(x.shape,dtype=np.float64)])
    common_term = (np.dot(new_x,weights) - y) / x.shape[0]
    first_term = (x ** 2 * common_term).sum()
    second_term = (x * common_term).sum()
    third_term = (common_term).sum()
    return np.array([[first_term],[second_term],[third_term]],dtype=np.float64)

def check_armijo_wolf_cond(w_k, d_k, x,y, alpha, beta1, beta2):
    xk_alp_dk = w_k + alpha * d_k
    f_grad = grad_f(x, w_k, y)
    f_grad_alph = grad_f(x, xk_alp_dk, y)
    armijo_left = calculate_f(x, xk_alp_dk, y)
    armijo_right = calculate_f(x, w_k, y) + alpha * beta1*np.dot(f_grad.T,d_k)
    wolf_left = np.dot(f_grad_alph.T, d_k)
    wolf_right = beta2 * np.dot(f_grad.T,d_k)
    return (armijo_left <= armijo_right) and (wolf_left >= wolf_right)

def steepest_direction(w_k, d_k, x, y,beta1, beta2, r):
    alpha = 1
    while not check_armijo_wolf_cond(w_k, d_k, x, y, alpha, beta1, beta2):
        alpha = alpha * r
    return alpha

def find_w(w_0, x, y, beta1, beta2,epsilon, r):
    w_k = w_0
    d_k = -grad_f(x, w_k, y)
    norm_grad = np.linalg.norm(-d_k)
    iterations = 0
    while norm_grad > epsilon:
        alpha = steepest_direction(w_k, d_k, x, y, beta1, beta2, r)
        w_k = w_k + alpha * d_k
        d_k = -grad_f(x, w_k, y)
        norm_grad = np.linalg.norm(-d_k)
        iterations += 1
        if iterations == 1000:
            break
    return w_k, iterations

beta1 = 1e-4
beta2 = 0.9
epsilon = 0.01
r = 0.5
w_0 = np.array([[0],[0],[0]], dtype=np.float64)
data = pd.read_csv(sys.argv[1])
data = np.array(data)
x = data[:,:-1]
y = data[:,-1:]
w, iterations = find_w(w_0, x, y, beta1, beta2, epsilon, r)
# print('\n')
print(w)
print(f"total_iterations: {iterations}")
print(calculate_f(x, w, y))