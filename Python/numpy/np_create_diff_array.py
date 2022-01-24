import numpy as np

# Erstellen
arr = np.array([1, 2, 3, 4])
arr = np.ones(42)
arr = np.zeros(42)
arr = np.arange(-42, 123, 3)
arr = np.arange(-42.5, 123.2, 3.1)  # Schrittweite
arr = np.linspace(-42.5, 1337.2, 100)  # Anzahl an Zahlen
# Überall spezifischer Wert
arr = np.full((2, 3), 42)
# diagonalmatrix mit 1 in Diagonale
arr = np.eye(5)
# zufällige Werte von 0..1
arr = np.random.random((2, 3))
# nicht zwingend empty -> daten die dort an der Speicheradresse standen
arr = np.empty((2, 3))

print(arr)

V = np.linspace(-42, 1337, 42)
M = np.eye(42)
# add, subtract, multiply, divide (prod->Matrixprodukt)
x = np.add(M, V)
x = np.add(V, V)
# sind, tan, cos, arcsin, ...
x = np.sin(V)
# exponent
x = np.exp(V) # e^V
x = np.exp2(V) # 2^V
x = np.power(V, 3) # v^3
x = np.log(V) # ln(v)
x = np.log2(V) # log_2(V)

# index des größten, kleinsten Elements
x = np.argmax(V)
x = np.argmin(V)
# max, min
x = np.max(V)
x = np.min(V)

# sortieren
V = np.random.random((5,))
# sortiert index nach größe der Werte
x = np.argsort(V)
print(V)
print(x)

# wird auf V gerechnet
# Index
idx = [x[0]] + [x[0], x[1], x[2]]
print(idx)
np.add.at(V, idx, 1) # unfunc
print(V)


