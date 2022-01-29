import pandas as pd
import numpy as np

data = [22, 33, 41, 12]
index = ["A", "B", "C", "D"]
s = pd.Series(data, name='Age', index=index)
print(s)
print(s["B"])
print(s[2])

data_dict = {
    "A": 28,
    "B": 42,
    "C": 1337,
    "D": 43,
}

# index kann gesetzt werden und ändert auch die Reihenfolge und werte können
# wiederholt werden
s2 = pd.Series(data_dict, index=["A", 'B', 'D', 'E', 'C', 'A'])
print(s2)

#unnützer datatype wird zurückgesetzt
s3 = pd.Series(np.random.randn(10), dtype=np.int32)
print(s3)
s3 = pd.Series(np.random.randint(12, 25, 10), dtype=np.int32)
print(s3)

# Achtun slice: nicht möglich: s[1:3][0], da index beibehalten wird

# Filtern
print(s3[s3 < s3.mean()])
print(np.log(s3))
