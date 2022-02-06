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
# print(perc)
# print(pd.value_counts(perc))

# Erstellen von Kategorien -> bei uns ACD
#ordered=True -> übernimmt dann unsere Ordnung
cat = pd.Categorical(
    list("ABCA"), categories=list("ACD"), ordered=False
)
print(cat)
# B war schon vorher weg
cat = cat.add_categories(['B'])

print(cat.remove_categories(["A"]))

#entfernt alle nicht verwendete Kategorien
cat = cat.remove_unused_categories()
print(cat)

# ordered=True -> übernimmt dann unsere Ordnung
# !! bla.sort_values, komischerweise ist ordered=True/False egal
cat2 = pd.Categorical(
    list("ABCADDEEA"), categories=list("CAD"), ordered=False
)
print("========ordered=========")
cat2.sort_values(inplace=True)
print(cat2)

