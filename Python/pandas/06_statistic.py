from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

var = np.random.randint(10, size=(5,5))
df = pd.DataFrame(var, columns=['A', 'B', 'C','D', 'E'], index=['a', 'b', 'c', 'd', 'e'])
print(f"Dataframe:\n {df}\n=====================\n")