import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(20, size=(3, 3)))
print(df)
print("df[0] ist:")
# col
print(df[0])
# row
print(df.loc[0])
# sum
print()
print(df[0].sum())

print(" === ")
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
print(df)
# Kann auch bestimmten Zeilen und Spalten auslesen: loc[list[Reihen, Spalten]]
print(df.loc[['a', 'b'], "B"])
# auf den Index zugreifen (nicht namen)
print(df.loc[df.index[[1, 2]], "B"])
print(df.iloc[[1, 2], 1])

# Index von Spalte über get_loc
print(f"Index von Spalte B: {df.columns.get_loc('B')}")

print("Dataframe erweitern:")
df.loc["e"] = 15
df["E"] = 12
print(df)

# Spezielles auswählen
# erst Zeile dann Spalte
print(df.at["a", "A"])
print(df.iat[2, 1])

# Bedingungen:
# Ganzes Dataframe erhält eine boolsche darstellun:
# <, > ==, isin,...
# bei Dataframe: alles false Werte werden zu NAN
# bei Series: Werte werden rausgenommen, alternativ s.where

print(df > 42)
print(df[df > 42])
print(df.isin([1, 2]))
# mit df.where und other= können alternative Werte gesetzt werden: NAN durch Ersatzwert ersetzt
print(df.where(df > 3, other=70))

# inplace ersetzt df = df[irgendwas]
df = pd.DataFrame(np.random.randint(10, size=[3,3]))
print(df)

df2 = df.where(df > 3)
print(df2)
print(df)
df.where(df >3, inplace=True)
print(df)
print(" === ")
print(df[df>5])