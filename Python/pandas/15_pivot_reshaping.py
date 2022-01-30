import numpy as np
import pandas as pd

df = pd.DataFrame({
    "group": ['cat', 'dog', 'cat', 'cat', 'dog'],
    "group2": ['a', 'a', 'b', 'c', 'b'],
    "A": ['a', 'b', 'c', 'd', 'x'],
    "B": ['e', 'f', 'g', 'h', 'y'],
    "C": np.random.randn(5),
})

# PivotTable
#! Achtung doppelte Indizes nicht erlaubt
# Values können auch Liste enthalten -> damit dann Untertabellen -> mult DF
print(df.pivot(
    index="group",
    columns='group2',
    values='C'
))


#### Stack ###
idxs = list(
    zip(
        *[
            ["A", "A", "B", "B", "C", "C", "D", "D"],
            ["1", "2", "1", "2", "1", "2", "1", "2"],
        ]
    )
)
print(idxs)
index = pd.MultiIndex.from_tuples(idxs)
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["X", "Y"])
print(df)
# Führt nochmals Index hinzu um einen Index aus der Spalte in eine Zeile zu schieben
# Eventuell ergibt es eine Series -> falls nur noch eine Spalte
print(df.stack())
print(type(df.stack()))

# Unstacken
print(df.unstack())