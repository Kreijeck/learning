import numpy as np
from sys import getsizeof
import random
from timeit import Timer

temp = [-1.5, -1.2, 0., 2.1, 24.2]
np_temp = np.array(temp)


def np_array():

    np_temp = np.array(temp)
    high_temp = 3*np_temp
    high_temp_list = [3*x for x in temp]

    # Datentyp festlegen -> Rechenfehler möglich!
    # int8: 1 2 4 8 16 32 64 Vorzeichen!
    #       1 2 3 4 5  6  7  8
    print("datentyp in numpy:", np.array([42, 254], np.int8))

    print(np_temp)
    print(temp)
    print("Kleine Liste:")
    print('numpy:', high_temp)
    print('normal:', high_temp_list)


def np_array_vs_list():
    # set temp as global
    global temp
    np_temp = np.array(temp)

    print(f"Size of python List: {getsizeof(temp)}")
    print(f"Size of numpy array: {getsizeof(np_temp)}")

    temp = [random.randint(0, 200) for _ in range(1_000_000)]
    np_temp = np.array(temp)
    print("große Liste: speziell für ints!")
    print(f"Size of python List: {getsizeof(temp)}")
    print(f"Size of numpy array: {getsizeof(np_temp)}")


def datatypes():
    # Wenn man einen speziellen Datentyp will:
    # Example: "<i4"
    # optional: < .. little endian, > ... big endian
    # i .. .integer (Großbuchstaben als unsigned), Zahl ...in byte
    # alternativ standardtypen: object, int, float, str, list, ...
    # rest nachlesen oder in tutorial numpy #3 von morpheus
    dt = np.dtype("i4")
    print(dt.itemsize)
    print(dt.name)
    print(np.dtype("i4") == np.int32)


def np_shapes():
    dt = np_temp
    print(dt.shape)

    # multi dimensionales Array
    multi_dim = [
        [
            [-1.5, -1.2, 0., 2.1, 24.2],
            [-1.5, -1.2, 0., 2.1, 24.2],
            [-1.5, -1.2, 0., 2.1, 24.2],
        ],
        [
            [-1.5, -1.2, 0., 2.1, 24.2],
            [-1.5, -1.2, 0., 2.1, 24.2],
            [-1.5, -1.2, 0., 2.1, 24.2]
        ]
    ]

    np_multi = np.array(multi_dim)
    print(np_multi.shape)
    print(np_multi.dtype)
    print(np_multi[0][2][4])

# Arrays müssen alle Zeilen gleich groß sein
# da Fehler wirft auskommentiert
# multi_dim = [[-1.5, -1.2, 0., 2.1, 24.2], [-1.5, -1.2, 0., 2.1]]
# np_multi = np.array(multi_dim)
# print(np_multi.shape)


def complex_dtypes():
    # eigener Datentyp: jedes dt ist damit (2,3) groß und hat int32
    dt = np.dtype((np.int32, (2, 3)))
    # größe definieren -> 2 * (2,3)
    arr = np.zeros((2), dtype=dt)
    print(arr)

    dt2 = np.dtype(('i4, (2,3)f8, f4', (2, 3)))
    arr2 = np.zeros((), dtype=dt2)
    print("\nMultidimensionales Array")
    print(arr2.shape)
    print(arr2)


def named_dtype():
    dic = {"Red": 233, "Green": 12, "Blue": 255, "Alpha": 255}
    # beispiel numpy array für Farben
    dt = np.dtype(('i4', [('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')]))
    print(np.zeros((), dtype=dt))
    print(np.zeros((), dtype=dt).dtype)

    print(np.zeros((), dtype=dt)['r'])

    # eine komplexe Zahl: (anm.: dieses mal wird ein dict verwendet)
    ## Schreibweise 1
    dt_complex = np.dtype(
        (np.int32, {'real': (np.int16, 0), 'imag': (np.int16, 2)}))
    ## Schreibweise 2
    dt_complex = np.dtype(
        (np.int32, [('real',np.int16), ('imag', np.int16)]))
    print("==Complex Dtype==")
    my_arr = np.zeros((2,3), dtype=dt_complex)
    print(my_arr)
    print(my_arr.dtype)
    # Zugriff auf spezielle Werte: Achtung dict steht am Anfang!
    print(my_arr['real'][0][1])

    print("Achtung numpy sieht kompletten datenty als int32")
    my_arr['real'][0][1] = 42
    my_arr['imag'][0][1] = 123

    print(my_arr['real'][0][1])
    print(my_arr['imag'][0][1])
    print(my_arr[0][1])


if __name__ == '__main__':
    # np_array()
    # np_array_vs_list()
    # datatypes()
    # np_shapes()
    # complex_dtypes()
    named_dtype()
