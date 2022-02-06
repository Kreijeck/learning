from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

var = np.random.randint(10, size=(1337,7))
df = pd.DataFrame(var)
print(f"Dataframe:\n {df}\n=====================\n")

# descripe: Statistische werte, Count, mean, ..., std: Standardabweichung
#25%, 50%, 75%: aller Werte sind unterhalb dieses Wertes
print(df.describe())

# Sonstige Funktionen:
print(df.sum())
print(" === ")
print(df.mean())
print(" === ")
print(df.abs())
print(" === ")
print(df.skew())
print(" === ")
# print min von Spalten
print(df.min())
# mit Index
print(df.idxmin())
print(" === ")

# Histogram -> nur über Series möglich
df = var = np.random.randint(100, size=1337)
print(pd.value_counts(df))