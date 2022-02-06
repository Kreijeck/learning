from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

var = np.random.randint(10, size=(5,5))
df = pd.DataFrame(var, columns=['A', 'B', 'C','D', 'E'], index=['a', 'b', 'c', 'd', 'e'])
print(f"Dataframe:\n {df}\n=====================\n")

# Zeilen addieren
add_df = df.add(df.iloc[1])
print(add_df)
print("  ===  ")

# Spalten addieren, axis=1 default
add_df = df.add(df.iloc[1], axis=0)
print(add_df)

# unten oder oben die default: ersten/letzten 5 ausgeben:

print(df.head(2))
print()
print(df.tail(1))

# NAN werte mit Werten befüllen:
print(df.fillna("nix"))


# compare:
# all vergleicht alle Werte einer Spalte
# any irgendein Wert
# kombiniert: geht die reihenfolge durch -> erst any-df daraus dann all
print((df > 3).any())
print((df > 3).all())
print((df > 0).any().all())


df2 = pd.DataFrame(var, columns=['A', 'B', 'C','D', 'E'], index=['a', 'b', 'c', 'd', 'e'])
# kombinieren
# versucht überall das erste zu nehmen und die blinden Flecke werden mit df2 aufgefüllt
#  -> nochmals was schönes schreiben
df.combine_first(df2)

# convert with to_...
print("  ===  ")
print(df.to_numpy())
