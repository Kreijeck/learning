from flask import Flask, render_template, request

app = Flask(__name__)


class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


@app.route('/')
def hello_world():  # put application's code here
    items_class = [Item("Apfel", 1),
                   Item("Birne", 3),
                   Item("Banane", 4),
                   ]
    items_list = ["Computer", "Mac", "Game"]
    items_dict = [{"name": "Apfel", "amount": 4},
                  {"name": "Traube", "amount": 3},
                  {"name": "Kiwi", "amount": 1},
                  ]

    items_tuple = ("Max", "Mustermann")

    return render_template("index.html",
                           name="Thomas",
                           items_class=items_class,
                           items_list=items_list,
                           items_dict=items_dict,
                           items_tuple=items_tuple)


@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    print(f"Age: {age}")
    return render_template("test.html", name=name, age=age)


if __name__ == '__main__':
    app.run()


class Krypto:
    def __init__(self, amount, spread, transaction):
        try:
            self.amount = float(amount)
            self.spread = float(spread)
            self.transaction = transaction
            self.price = float(self.calc_price())
        except:
            raise "Do not work"
        #     self.amount = None
        #     self.spread = None
        #     self.transaction = None
        #     self.price = None

    def calc_price(self):
        if self.amount == None or self.spread == None:
            return 0
        if self.transaction == "buy":
            return round(self.amount * (1 + self.spread / 100), 2)
        elif self.transaction == "sell":
            return round(self.amount * (1 - self.spread / 100), 2)
        else:
            # raise KeyError(f"{self.transaction} does not exist for transaction")
            return None


values = []


@app.route("/krypto")
def krypto():
    betrag = request.args.get("betrag", "0")
    spread = request.args.get("spread", "0.75")
    transaction = request.args.get("transaction", "buy")

    values.append(Krypto(betrag, spread, transaction))

    return render_template("krypto.html", values=values, last_amount=betrag, last_spread=spread,
                           last_transaction=transaction)
