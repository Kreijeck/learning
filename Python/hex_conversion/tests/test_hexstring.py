import unittest
from coding_parser import CodingString


class HexStringTests(unittest.TestCase):

    def setUp(self) -> None:
        # bit order : "10101011", "00101110", "00000000", "00010101"
        # hex order: AB 2E 00 15
        self.hex_string = "AB2E0015"

    def test_read_hexlist(self):
        """
        Hexstring shall be converted to Hexlist
        """
        h1 = CodingString(self.hex_string)
        expected_result = ["AB", "2E", "00", "15"]
        self.assertEqual(h1.hex_list, expected_result)

    def test_read_binarylist(self):
        """
        Hexstring shall be converted to Binarylist
        """
        h2 = CodingString(self.hex_string)
        expected_result = ["10101011", "00101110", "00000000", "00010101"]
        self.assertEqual(h2.binary_list, expected_result)

    def test_read_bit_big_endian(self):
        byte = 1
        bit = 5
        bit_length = 2
        h3 = CodingString(self.hex_string, endian="big")
        value = h3.read_value(byte, bit, bit_length)
        self.assertEqual(3, value)

    def test_read_bit_little_endian(self):
        # byte1 = 00101110
        # little endian ist default
        h3 = CodingString(self.hex_string)

        byte, bit, bit_length = (1, 2, 2)
        # as binary
        value = h3.read_value(byte, bit, bit_length, convert_to_dec=False)
        self.assertEqual("11", value)
        # as decimal
        value = h3.read_value(byte, bit, bit_length)
        self.assertEqual(3, value)

        byte, bit, bit_length = (1, 4, 1)
        # as binary
        value = h3.read_value(byte, bit, bit_length, convert_to_dec=False)
        self.assertEqual("0", value)
        # as decimal
        value = h3.read_value(byte, bit, bit_length)
        self.assertEqual(0, value)

        byte, bit, bit_length = (1, 2, 4)
        # as binary
        value = h3.read_value(byte, bit, bit_length, convert_to_dec=False)
        self.assertEqual("1011", value)
        # as decimal
        value = h3.read_value(byte, bit, bit_length)
        self.assertEqual(11, value)

        byte, bit, bit_length = (1, 2, 4)
        # as binary
        value = h3.read_value(byte, bit, bit_length, convert_to_dec=False)
        self.assertEqual("1011", value)
        # as decimal
        value = h3.read_value(byte, bit, bit_length)
        self.assertEqual(11, value)

    def test_combine_bytes(self):
        h4 = CodingString(self.hex_string)
        current_result = h4.combine_bytes(1, 3)
        expected_result = "001011100000000000010101"

        self.assertEqual(expected_result, current_result)

        current_result = h4.combine_bytes(2, 2)
        expected_result = "0000000000010101"

        self.assertEqual(expected_result, current_result)

