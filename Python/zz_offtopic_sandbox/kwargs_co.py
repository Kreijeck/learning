def anything(**modenames):
    print(create_text(**modenames))


def create_text(first, second, **kwargs):
    text = f"{first} und danach {second}"
    text += "und danach:\n"
    for i in kwargs.values():
        text += f"{i}\n"
    return text


def nur_args(*args):
    print(create_text(*args))

anything(first="du", second="bar", nost="nirgends", manchmal="manchmal")

nur_args("du", "bar")