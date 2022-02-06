import pandas as pd
import numpy as np

# don't work because default index is 0,1,2,3 -> erwartet length von 8
# nur bei Series, wenn wie in a keine Series, dann setzt er selbst durch
var = {
    "a": [0, 1, 2, 3, 4, 5, 6, 7],
    "b": pd.Series([1, 2, 3, 4], index=["a", 'b', 'c', 'd']),
    "c": pd.Series([2, 3, 4, 5])
}

df1 = pd.DataFrame(var)
print(df1)

# es geht auch nur manche indizes zu belegen, aber normale Listen müssen gleiche Länge haben
dict_b = {'a': 42,
          'b': 123,
          1: 0
          }

var_2 = {
    'a': [0, 1, 2, 3, 4, 5, 6],
    'b': pd.Series(dict_b, index= ['a', 'b', 'c', 'd', 0 , 1, 2] )
}

df2 = pd.DataFrame(var_2)
print(df2)

var3 = np.zeros((2,), dtype=[('id', 'i8'), ('age', 'i8'), ('name', 'a10')])
df3 = pd.DataFrame(var3)
print(df3)

print("==================")

var4 = {
    ("a", "z"): {"A": 0, "B": 1},
    ("a", "y"): {"A": 0, "B": 1},
    ("a", "x"): {"A": 0, "B": 1},
    ("b", "z"): {"A": 0, "B": 1},
    ("b", "y"): {"A": 0, "B": 1},
    ("b", "x"): {"A": 0, "B": 1},
}
df4 = pd.DataFrame(var4)
print(df4)

print("------")
print(df4["a"])
print(df4["a"]["x"])
print(df4["a"]["x"]["A"])

# aber es geht nicht in anderer Reihenfolge, wie bspw
# df4["x"] <- nicht möglich!!
# Subindex auch in Reihen möglich
