
def get_prime(max_value):
    counter = 0
    prime = [2]
    all_numbers = [i for i in range(3, max_value + 1) if i % 2 != 0]

    while all_numbers:

        n = all_numbers.pop(0)
        print(f"\r at the moment we are at prime_number: {n}", end="")
        prime.append(n)
        for val in all_numbers:
            counter += 1
            if val % n == 0:
                all_numbers.remove(val)
    print()
    print(f"Benötigte Anzahl an Schleifendurchgängen: {counter}")
    return prime

def get_prime_rekursive(max_value):

    def rek(all_numbers: list):
        n = all_numbers.pop(0)
        prime.append(n)
        for val in all_numbers:
            if val % n == 0:
                all_numbers.remove(val)
        if all_numbers:
            rek(all_numbers)

        return prime

    prime = [2]
    all_numbers = [i for i in range(3, max_value + 1) if i % 2 != 0]
    prime = rek(all_numbers)

    return prime

def prime_pairs(max_value):
    prime_numbers = get_prime_rekursive(max_value)
    twin_dict = {}
    cousin_dict = {}
    sexy_dict = {}
    for prime in prime_numbers:
        if prime + 2 in prime_numbers:
            twin_dict[prime] = prime + 2
        if prime + 4 in prime_numbers:
            cousin_dict[prime] = prime + 4
        if prime + 6 in prime_numbers:
            sexy_dict[prime] = prime + 6

    return twin_dict, cousin_dict, sexy_dict



if __name__ == '__main__':
    # for i in prime_pairs(50):
    #     print(i)
    #
    # prime_pairs(50)
    get_prime(500000)




