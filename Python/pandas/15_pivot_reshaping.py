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