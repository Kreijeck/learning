import numpy as np
import pandas as pd

df = pd.DataFrame({
    "group": ['cat', 'dog', 'cat', 'cat', 'dog'],
    "group2": ['a', 'a', 'b', 'b', 'b'],
    "A": ['a', 'b', 'c', 'd', 'x'],
    "B": ['e', 'f', 'g', 'h', 'y'],
    "C": np.random.randn(5),
})


def foo(group):
    # blödes Beispiel aber funktioniert auch nur, da Zeilen und spalten gleich groß sind
    # ansonsten könnte DF so nicht erstellt werden
    d = pd.DataFrame({
            'group': group.columns,
            'mean': group["C"] * group["C"].mean()
        }, index=[0, 1, 2, 3, 4])
    return d


print(df)

# gruppe erstellen, auch mit mehreren Spalten
group_df = df.groupby(["group", "group2"])
group_df = df.groupby("group")
print("===\n")
# gibt Index der Gruppen aus
print(group_df.groups)

for name, group in group_df:
    print(f"Der Name ist: {name}")
    print(f"Und hier kommt die Gruppe:")
    print(group)


print("spezielle Gruppe auslesen")
print(group_df.get_group("cat"))

print("Size der einzelnen Gruppen auslesen")
print(group_df.size())
print("Durchschnitt natürlich nur für Zahlen möglich")
print(group_df.mean())

# Funktionen auf der Gruppe ausführen
print(group_df.apply(foo))
