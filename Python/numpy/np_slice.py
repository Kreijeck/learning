import numpy as np

temp = [-1.5, -1.2, 0., 2.1, 24.2, 12, 14., 5.4, 4.7]
np_temp = np.array(temp)


print(f"Original: {temp}")
print("Slice basic")
print(temp[1:7])
print(np_temp[1:7])
print("Slice with Steps:")
print(temp[1:7:2])
print(np_temp[1:7:2])
print("Slice revert")
print(temp[::-1])
print(np_temp[::-1])
print("")