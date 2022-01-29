import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000,3))
df = df.reindex(index=range(10000, 1, -1), columns=[2,0,1])
print(df)

df = pd.Series(np.random.randint(0,42, size=1000))

histo = pd.value_counts(df)
histo = histo.reindex(range(0,42))
# print(histo)

# df.columns = [0, 2] -> umbenennen
# df.reindex -> Reihenfolge tauschen
