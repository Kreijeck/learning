def calc_checksum(input):
    """
    calculate the checksum
    :param input: number as string, e.g. "12345"
    :return: int: checksum (1 * z1 + 2*z2 + 3*z3 + 4*z4 + ... + n*zn)%10
    """

    checksum = 0
    for i, val in enumerate(input):
        checksum += (i + 1) * int(val)

    return checksum % 10


print(calc_checksum("87654321"))
