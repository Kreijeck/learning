import numpy as np

np.set_printoptions(suppress=True)

v = np.array([2, 4, 6])
w = np.array([1, 3, 5])

print(np.row_stack((v, w)))
print(np.column_stack((v, w)))

# sich selbst stacken:
print(np.row_stack((v, v, v)))

A = np.array([[1, 2],
     [3, 4],
     ])
B = np.array([[6, 7],
     [8, 9],
     ])

print(np.row_stack((A, B)))
# axis: n-1 dimension des arrays möglich
print(np.concatenate((A, B), axis=0))

print("=========Array Vervielfachen==========")
print(np.tile(A, 4))
print()
print(np.tile(A, (4,1)))
print()
print(np.tile(A, (3,3)))

print("=============teils auffüllen========")
res = np.zeros((50, 50))
res[:A.shape[0], :A.shape[1]] = A

print(res)

