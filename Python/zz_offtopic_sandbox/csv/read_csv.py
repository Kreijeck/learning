import pandas as pd
import time

def read_csv(filename):

    return pd.read_csv(filename, sep=";", encoding="windows-1252")

# def testme():
#     df = pd.read_csv("Ranking HeiligsBlechle.CSV", sep=";", encoding='windows-1252')
#     for d in


def getPolePosition(dataframe, name):
    count = 0
    for data in dataframe[name]:
        if data == '1':
            count += 1

    return count


if __name__ == '__main__':
    start = time.time()
    race_df = read_csv("Ranking HeiligsBlechle.CSV")

    print(f"Andi: {getPolePosition(race_df, 'Andi')}")
    print(f"Strähli: {getPolePosition(race_df, 'Strähli')}")
    print(f"Baschdi: {getPolePosition(race_df, 'Baschdi')}")
    stop = time.time()

    print(f"time needed: {stop-start}")
