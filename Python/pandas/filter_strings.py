import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": ["Hi", "Thomas ist", "Hans tut", "Martin tut", "Hans ist", "Hallo"],
    "B": np.random.randn(6)

})

print(df)

# search is regex, only fullmatch!!! 
search = '.*ist.*'
filtered_df = df[df["A"].str.match(search)]
print(filtered_df)

# string contains, param: regex can be said, whether regex is used
search="ist"
filtered_df = df[df["A"].str.contains(search, regex=False)]
print(filtered_df)
