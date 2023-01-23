"""
LAB - 10
Integer Programming Problem 

"""

import numpy as np
from gekko import GEKKO
import sys

m = GEKKO(remote=False)
abc_matrix = {"1": {"A": np.array([[6, 3, 5, 2], [1, 0, 0, 1], [-1, 0, 1, 0], [0, -1, 0, 1]], dtype=np.float64), "b": np.array([[10], [1], [0], [0]], dtype=np.float64), "c": np.array([[9], [5], [6], [4]], dtype=np.float64)}, "4": {"A": np.array(
    [[55, 45, 60, 50, 30], [40, 35, 25, 35, 30], [25, 20, 0, 30, 0], [0, 0, 1, 1, 0]], dtype=np.float64), "b": np.array([[150], [110], [60], [1]], dtype=np.float64), "c": np.array([[120], [85], [105], [140], [70]], dtype=np.float64)}}
question_no = sys.argv[1]
A = abc_matrix[question_no]['A']
b = abc_matrix[question_no]['b']
c = abc_matrix[question_no]['c']

z = m.Array(m.Var, c.shape[0], integer=True, lb=0, ub=1)

m.qobj(c, x=z, otype='max')
m.axb(A, b, x=z, etype='<=')
m.options.SOLVER = 1
m.solve(disp=False)
print("Objective: ", m.options.OBJFCNVAL)
print(z)
