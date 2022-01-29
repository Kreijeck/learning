import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "id": [0, 1, 2, 3],
        "name": ["Thomas", "Kreijeck", "bla", None],
        "age": [29, 30, 32, 34]
    }
)

print(df)
# Gibt Beschreibung aus
print(df["age"].describe())


# Series
print(pd.Series([28,28,28,28], name='age'))