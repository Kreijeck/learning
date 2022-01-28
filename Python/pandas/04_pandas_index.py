import pandas as pd
import numpy as np

var = np.random.randint(10, size=(5,5))
df = pd.DataFrame(var, columns=['A', 'B', 'C','D', 'E'], index=['a', 'b', 'c', 'd', 'e'])

print(df)
print("")
# index col - row
print(df["A"]['b'])
# auf Zeilen zugreifen -> wird in Series umgewandelt
print(df.loc['b'])
# Zugriff auf die jeweilige Spalte -> kein Index immer nur die Anzahl
print(df.iloc[1])
#auch slicing möglich
print(df.iloc[1:3])

# kombiniere Dataframe
df2 = pd.DataFrame({"A": df["A"], "C": df["C"]})
print(df2)

# einzelne Spalten rauswerfen
print()
print(df.pop("B")) # Rückgabe: Entfernte Spalte
print(df) # in df: Spalte B wurde entfernt

# Spalte hinzufügen name=Werte <- für Werte lambda Funktion
df2 = df.assign(name=lambda x: (x["A"] + x["C"]))
print()
print(df2)