import logging
from typing import Union


class CodingString:
    def __init__(self, hex_string: str, endian: str = "little") -> None:
        """
        Work with Hexstring
        :param hex_string:string Format shall be like "23A4", an hexstring has to be an even-number!
        :param endian: str: possible:   "little" - bit from right to left
                                        "big" - bit from left to right
                            other: left to right
        """

        if len(hex_string) % 2 != 0:
            raise ValueError("hex_string has to be an even-number")
        self.hex_string = hex_string
        self.endian = endian
        self.hex_list = self.__convert2hex(hex_string)
        self.binary_list = self.__convert2binary(hex_string)

        # endian
        self.little_endian = (self.endian == "little")
        self.big_endian = (self.endian == "big")


    def read_value(self, byte: int, bit: int, bit_length: int, convert_to_dec: bool =True):
        """
        Read Value from specific version
        :param byte:
        :param bit: int value 0...7
        :param length:
        :return: int: Value in decimal
        """
        byte_value = self.binary_list[byte]
        start_bit = bit
        if self.little_endian:
            # count negative (starts with -1, -(bit +1)
            # start bit has to be swapped to left on bit_length -1
            # start_bit = -(bit +1 + bit_length -1)
            start_bit = -(bit + bit_length)
            stop_bit = start_bit + bit_length
        elif self.big_endian:
            # count positive from bit : bit+bit_length
            start_bit = bit
            stop_bit = bit + bit_length
        else:
            raise AttributeError(f"Don't know the Endian {self.endian}")

        bit_value = byte_value[start_bit:stop_bit]
        # convert bit to dec:
        if convert_to_dec:
            return int(bit_value, 2)
        else:
            return bit_value

    def write_value(self, byte: int, bit: int, bit_length: int, value: int):
        """
        Write a value to Object
        :param byte:
        :param bit:
        :param bit_length:
        :return:
        """
        byte_value = self.binary_list[byte]
        start_bit = bit
        if self.little_endian:
            start_bit = -(1 + bit)
            stop_bit = start_bit - (bit_length -1)
        elif self.big_endian:
            start_bit = bit
            stop_bit = bit + (bit_length -1)
        else:
            raise AttributeError(f"Don't know the Endian {self.endian}")

        bit_value = byte_value[start_bit:stop_bit]
        return bit_value

    def combine_bytes(self, start_byte, number_of_bytes):
        bytes = self.binary_list[start_byte]

        for i in range(number_of_bytes - 1):
            bytes += self.binary_list[start_byte + i + 1]

        return bytes

    def __convert2hex(self, hex_string) -> list:
        """
        Split String in a list of hex : ["A5", "B3", "12"]
        :return: hexvalue
        """
        n = 2
        hexlist = [hex_string[i: i + n] for i in range(0, len(hex_string), n)]

        return hexlist

    def __convert2binary(self, hex_string) -> list:
        """
        Convert the hexstring to binary
        :return:
        """
        hex_scale = 16
        sign_in_byte = 8
        # remove 0b at first and fill bits to 8
        binary_list = [bin(int(myhex, hex_scale))[2:].zfill(sign_in_byte) for myhex in self.__convert2hex(hex_string)]
        return binary_list
