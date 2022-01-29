import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(100_000, 3))[0]
print(f"\n====\n{df}")
print(df.describe())
# cut nur bei 1 dimeonsionalen Array
# df wird in x gleichgroße Stücke aufgeteilt, ( -> inklusive, [ -> exclusive
# Werte werden in Kategorien gepackt, tatsächliche Werte NICHT in df
print("======================")
cats = pd.cut(df, 20)
print(cats)
print(f"===\n{cats[0]}")
print(pd.value_counts(cats))

# teilt in einer liste die x-größten Werte in bins
# also in diesem Beispiel: 0 -> 0.1(10%), 0.1 -> 0.2(10%-20%),...
# quantile list muss von range[0, 1] sein
perc = pd.qcut(df, [0, 0.1, 0.2, 0.5, 0.75, 1])
print("===================")
print(perc)
print(pd.value_counts(perc))
