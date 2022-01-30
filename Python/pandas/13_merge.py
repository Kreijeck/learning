import numpy as np
import pandas as pd

l = pd.DataFrame({
    "id": [0, 1, 3, 4],
    "A": ['a', 'b', 'c', 'd'],
    "B": ['e', 'f', 'g', 'h'],
})

r = pd.DataFrame({
    "id": [0, 1, 3, 4],
    "B": ['e', 'f', 'z', 'h'],
    "C": ['i', 'j', 'k', 'l'],
    "d": ['m', 'n', 'o', 'p'],
})

# when merge  on="id" Spalten werden sortiert, ohne on= wird auf Indizes (default sind diese gleich) zu mergen
df = pd.merge(l, r, on="id")
df2 = pd.merge(l, r)
df3 = pd.merge(l, r, on="id", how='outer')

# Auch mit mehrern Spalten kann gejoint werden -> Liste
# parameter für how: 
# inner: nur gleiche werden gesetzt
# outer: alle werden gesetzt und mit NAN aufgefüllt
# left: outer left
# right: outer right

# indicator gibt zusätzliche Info in neuer Spalte
df4 = pd.merge(l, r, on=["id",'B'], how='outer')
df5 = pd.merge(l, r, on=["id",'B'], how='inner')
df6 = pd.merge(l, r, on=["id",'B'], how='outer', indicator='indi')

# reindizieren des Index mit reset_index() setzt Index komplett neu:
df7 = pd.merge(l, r, on=["id",'B'], how='outer', indicator='indi').reset_index()

print(df)
print(df2)
print(df3)
print("id 3 ist in B nicht gleich, daher fliegt es raus")
print(df4)
print(df6)