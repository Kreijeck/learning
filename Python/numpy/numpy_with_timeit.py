import numpy as np
import random
from timeit import Timer

sz = 1_000_000
X = [random.randint(0, 200) for _ in range(sz)]
Y = [random.randint(0, 200) for _ in range(sz)]
np_X = np.array(X, np.int64)
np_Y = np.array(Y, np.int64)

def py_add():
    res = [X[i] + Y[i] for i in range(sz)]
    return res

def np_add():
    res = np_X + np_Y

time_python = Timer("py_add()", setup="from __main__ import py_add").timeit(20)
time_numpy = Timer("np_add()", setup="from __main__ import np_add").timeit(20)
print(f"Python time: {time_python}")
print(f"Numpy time: {time_numpy}")
print(f"Damit ist Numpy {round(time_python/time_numpy, 2)}x schneller")
