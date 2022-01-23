import json

data = {"v1": "Foo",
     "v2": "Bar"}


class Krypto:
    def __init__(self, name: str, kurs: float, spread=0.75):
        """

        :param name: name of krypto
        :param kurs: current amount
        :param spread: spread in %
        """
        self.name = name
        self.kurs = round(kurs, 2)
        self.spread = spread
        self.buy_value = self.buy()
        self.sell_value = self.sell()

    def buy(self) -> float:

        return round(self.kurs * (1 + self.spread/100), 2)

    def sell(self) -> float:

        return round(self.kurs * (1 - self.spread/100), 2)


krypto = Krypto("Ethereum", 3601.13)

# d = {"name": krypto.name,
#      "kurs": krypto.kurs,
#      "buy": krypto.buy_value,
#      "sell": krypto.sell_value,
#      }

data = { krypto.name:
        {
            "kurs": krypto.kurs,
            "buy": krypto.buy_value,
            "saell": krypto.sell_value,
        }
     }

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)


with open("data.json", "r", encoding='utf-8') as file:
    loader = json.load(file)

print("Loader:", loader)
