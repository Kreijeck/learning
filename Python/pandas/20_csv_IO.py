import numpy as np
import pandas as pd

dateframe = pd.DataFrame(
    np.random.randn(100_000, 2),
    columns=[1, 2],
    index=pd.date_range("20211213", periods=100_000, freq="5min")
)
dateframe.to_csv("pandas/data.csv", sep=";", index_label="Datum")
print(dateframe)
# Index kann auch List von multi DF enthalten, index_col=Zahl -> von links nach rechts
#squeeze= gibt Series zurück (natürlich nur 1 Spalte!)
df = pd.read_csv("pandas/data.csv", sep=";", index_col="Datum")
print(df)
