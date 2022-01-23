from copyreg import pickle
import numpy as np
import os

A = np.random.randint(1, 42, size=(200, 200))
file = os.path.join(os.path.dirname(__file__), "A.txt")
file_conv = os.path.join(os.path.dirname(__file__), "A_conv.bin")
print(A)
print(file)

np.savetxt(file, A, fmt='%i', delimiter=",")
# np.savetxt(file, A, fmt='%.2f', delimiter=",")

A = np.loadtxt(file, delimiter=",", dtype=np.int32)
print(A)

# Achtung: gibt noch A.toFile() allerdings wird es im binären Format gespeichert
# und kann Probleme bei anderen Systemen beim laden haben

A.tofile(file_conv)
A = np.fromfile(file_conv)
# kommt ganz schöner Stuss raus!
print(A)