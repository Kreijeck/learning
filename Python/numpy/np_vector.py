import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(42 + X)
print(42 * X)
print(2 ** X)

print(f"X + Y: {X + Y}")
print(f"X * Y: {X * Y}")

# Matrizen
X = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

Y = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

print("=======Matrizen=====")
print(f"X + Y: {X + Y}")
print(f"X * Y: {X * Y}")
print("Matrizen Produkt")
print(np.dot(X, Y))
print("Vergleiche")
print(X==Y)

F = X == Y
G = np.array([
    [True, False, True],
    [True, False, False],
    [True, True, True],
])

print(np.logical_or(G, F))
print(np.logical_and(G, F))


print("===Verschiedene Größen===")
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
])
v = np.array([1, 2, 3])

print(v*A)
# transponiere matrix -> in 1dimensionalen kein unterschied
print(f"v: {v}")
v = v.transpose()
print(f'v_transpose: {v}')
print(v*A)

# für 1 dimensional so:
v_trans = np.array([[1,2,3],]*3).transpose()

print(f"v_trans: \n {v_trans}")
print(f"normal: v*A:\n {v*A}")
print(f"transponiert: v_trans*A:\n {v_trans*A}")

################## Flatten und Shape verändern #######################
print("===================FLATTEN=======================")

# Alles in 1 "liste"
# order     C - default row vor column - links nach rechts, dann oben nach unten,
#           F - column vor row - oben nach unten, links nach rechts
#           A - nehme den letzten - macht irgendwie keinen Sinn
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))
# Alternative zu flatten: ravel
# bei Ravael verwendet gleichen Speicher für die Zahlen

b = A.ravel()
c = A.flatten()
# A wird geändert, ändert sich auch bei ravel
A[0][1] = 4
print(b)
print(c)

print("==================RESHAPE===================================")
to_shape = np.array(range(24))
print(to_shape.reshape((12,2)))
print(to_shape.reshape((2,4, 3)))
# Neue dimension muss nur für Anzahl der Elemente passen





