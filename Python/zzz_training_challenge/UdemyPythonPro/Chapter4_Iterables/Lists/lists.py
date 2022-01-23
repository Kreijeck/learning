def main():
    my_list = [1, 2, 3]

    # Option 1: Single Value
    my_list.append(-10)
    print(my_list)

    # Option 2: List Concatenation
    my_list2 = [4, 5]

    my_list += my_list2
    print(my_list)

    # Option 3: Iterables
    #range: (start, stop, step)
    it = range(-2, 3, 1)
    # if wanna use a range: use extend
    my_list.extend(it)
    print(my_list)
    # my_list.append(it)
    # here result will be: [1, 2, 3, -10, 4, 5, range(-2, 3)]

    # Option 4: Insert at user-defined index
    my_list.insert(0, 'foo')
    print(my_list)

    # ungülitge Indizes: ganz vorne oder hinten!
    my_list.insert(30, 'foo')
    print(my_list)

    my_list.insert(-30, 'foo')
    print(my_list)

    # Remove values
    my_list.pop()
    print(my_list)

    # Remove at specific position
    idx = my_list.index('foo')
    my_list.pop(idx)
    print(my_list)

    # copy List für verschiedene Speicher
    # Testen ob manipulieren einer Liste die andere mit verändert????
    my_list2 = my_list.copy()

    # Reihenfolge drehen
    # inplace function
    my_list.reverse()
    print(my_list)
    #gleiche wie:
    print(my_list[::-1])

    # Count
    print(my_list.count(1))

    # Sort
    # inplace function
    # Sollte nur bei gleichen Typen verwendet werden
    # (numerisch und strings vergleichen ist schwer!)
    my_list.sort(reverse=False)






if __name__ == "__main__":
    main()
