import datetime
import pandas as pd
import numpy as np

dtf = pd.to_datetime([
    "1/1/1970",
    np.datetime64("2011-11-21"),
    datetime.datetime(2021, 1, 2)
])
# Range von Tage, mit startdatum
# periods: wieviel elemente
# freq: welche Abstände H: Stunde, S: sekunde, M: Monate allg. timeseries.offset_aliases
dtf = pd.date_range("2021-1-2", periods=7, freq='H')
# bei Monaten immer letzter Tag
dtf = pd.date_range("2021-1-2", periods=7, freq='M')
# deutsche Schreibweise
dtf = pd.date_range("13.12.2021", periods=7, freq="2D")

dtf = pd.to_datetime(["13.12.2021", "13-12-2021"])
# datumimporter - Zeit in s seit 1.1.1970, utc-timestamp
dtf = pd.to_datetime([1625823884], unit="s")


print(dtf)

dateframe = pd.DataFrame(
    np.random.randn(10000, 1),
    columns=["A"],
    index=pd.date_range("20211213", periods=10000, freq="H")
)
print(dateframe)

# spezielle Datumsräume zugreifen
print(dateframe["2021-12-28": "2022-01-15"])
# alle Daten aus 2022
print(dateframe.loc["2022"])
print(dateframe.loc["2022-01"])

# truncate - Zusammenschneiden
print(dateframe.truncate(before="2022", after="2022-02"))

delta = pd.Timedelta("1 days 01:00:00")
# 1.1.2021 + 1d1h
print(pd.to_datetime("2021") + delta)
# mit delta kann auch ein Dataframe verschoben werden
df2 = pd.DataFrame(pd.date_range("20220102", periods=100, freq="d"),
                   columns=["time"]
                   )
print(df2 + delta)
