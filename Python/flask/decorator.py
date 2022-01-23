def outer(func):
    counter = 0

    def inner():
        # nonlocal bezeichnent das Variable nicht nur lokal vorhanden (1 Ebene darüber)
        nonlocal counter
        print(f"Funktion wurde {counter}x ausgeführt ")
        counter += 1
        func()

    return inner


# Funktion cached z.B. kompliziert berechnete Werte und muss dann nur einmal ausgeführt werden und speichert die Werte
def cached(func):
    cached = {}
    def inner(x):
        if x in cached:
            return cached[x]
        result = func(x)
        cached[x] = result
        return result

    return inner

# decorator ersetzt eine Funktion durch eine andere!!
@outer
def do_something():
    print("do_something wurde ausgegführt")

@cached
def calculate_something(x):
    print(f"calculate_something: {x}")
    return x * x


#
# print(calculate_something(5))
# print(calculate_something(5))
# print(calculate_something(12))
# print(calculate_something(5))


# Parameterübergabe
def repeat(n):
    def deco(func):
        def inner():
            for i in range(0, n):
                func()

        return inner
    return deco



@repeat(5)
def do_something():
    print(f"do something wurde ausgeführt")

do_something()


