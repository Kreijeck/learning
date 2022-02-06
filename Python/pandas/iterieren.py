import imp


import pandas as pd
import numpy as np

# !!!generell sollte über df und Series nicht drüberiterieren!!!

df = pd.DataFrame(np.random.randn(100_000, 3))

print(df)

# print die col_names
for col in df:
    print(col)

for idx, row in df.head().iterrows():
    print(f"Index:{idx}: Row:{row[1]}")

# in der for schleife: Werte werden nicht gespeichert -> zuweisungen vermeiden
# wurde hier nicht durchgeführt
for idx, row in df.head().iterrows():
    for i in row:
        print(i)

    print()
    if idx > 5:
        exit()


# über Tupel zugreifen -> gibt Tuple zurück
# row[0] liefert INDEX!
for row in df.itertuples():
    print(row)
    print(row[1])
    print(row._1)
    exit()