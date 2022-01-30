import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    "A": np.random.randint(10, size=(3)),
    "B": np.random.randint(10, size=(3)),
    "C": np.random.randint(10, size=(3)),
},
    index=[0, 1, 2]
)

df2 = pd.DataFrame({
    "A": np.random.randint(10, size=(3)),
    "B": np.random.randint(10, size=(3)),
    "C": np.random.randint(10, size=(3)),
},
    index=[0, 2, 5]
)

df3 = pd.DataFrame({
    "A": np.random.randint(10, size=(3)),
    "B": np.random.randint(10, size=(3)),
    "C": np.random.randint(10, size=(3)),
},
    index=[0, 4, 2]
)

print(df3)
print("===")
# ! Indizes oder Spalten sind nicht eindeutig
print(pd.concat([df1, df2, df3]))
print("===")
print(pd.concat([df1, df2, df3], axis=1))

# default join=outer - erweitern, inner - zusammenschneiden
print("===")
print(pd.concat([df1, df2, df3], axis=1, join='inner'))
print(pd.concat([df1, df2, df3], axis=0, join='inner'))

# append geht auch, aber concat ist mächtiger
print("===")
print(df1.append(df2))

# ignore_index=True vergibt neue Index
# theoretisch auch sort=True möglich zum sortieren (nach was ist nicht klar ...)
print("===")
print(pd.concat([df1, df2, df3], axis=0, join='outer', ignore_index=True))