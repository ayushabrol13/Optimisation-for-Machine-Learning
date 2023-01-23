from numpy import *


def fun(x):
    return 4*x[0]*2 - 3*x[0]*x[1] + 2*x[1]*2 - x[0] + 2*x[1]


def gradf(x):
    f0, n, h1, = fun(x), len(x), pow(10, -5)
    g = zeros((n, 1), dtype=float)
    for i in range(0, n):
        x1 = x.copy()
        x1[i] = x1[i] + h1
        # print(x,x1)
        g[i] = (fun(x1)-f0)/h1
    return g


# (52,53) R=52
x0, beta1, beta2, r, eps, iter1 = array(
    [[52.0], [53.0]]), pow(10, -4), 0.9, 0.5, pow(10, -3), 0
print(gradf(x0))
