import unittest
import chapter_02.grundrechenarten as basic
import chapter_02.prime_number as prime
import chapter_02.checksum as checksum


class TestGrundrechenarten(unittest.TestCase):

    def test_1a(self):
        self.assertEqual(basic.calc(6, 7), 0)

    def test_1b(self):
        self.assertEqual(basic.calc(5, 5), 5)

    def test_1c(self):
        self.assertEqual(basic.calc_sum_and_count_all_numbers_div_by_2_or_7(3), ([2], [], 1, 2))

    def test_1d(self):
        self.assertEqual(basic.calc_sum_and_count_all_numbers_div_by_2_or_7(8), ([2, 4, 6], [7], 4, 19))

    def test_1e(self):
        self.assertEqual(basic.calc_sum_and_count_all_numbers_div_by_2_or_7(15),
                         ([2, 4, 6, 8, 10, 12, 14], [7, 14], 8, 63))

    def test_2a(self):
        self.assertEqual(basic.number_as_text(7), "SEVEN")

    def test_2b(self):
        self.assertEqual(basic.number_as_text(42), "FOUR TWO")

    def test_2c(self):
        self.assertEqual(basic.number_as_text(24680), "TWO FOUR SIX EIGHT ZERO")

    def test_2b(self):
        self.assertEqual(basic.number_as_text(13579), "ONE THREE FIVE SEVEN NINE")

    def test_3a(self):
        self.assertEqual(basic.calc_perfect_numbers(1000), [6, 28, 496])

    def test_3b(self):
        self.assertEqual(basic.calc_perfect_numbers(10000), [6, 28, 496, 8128])

class TestPrime(unittest.TestCase):

    def test_4a(self):
        self.assertEqual(prime.get_prime(15), [2, 3, 5, 7, 11, 13])

    def test_4b(self):
        self.assertEqual(prime.get_prime(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_4c(self):
        self.assertEqual(prime.get_prime(50),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] )

class CheckSum(unittest.TestCase):
    def test_6a(self):
        self.assertEqual(checksum.calc_checksum("11111"), 5)

    def test_6b(self):
        self.assertEqual(checksum.calc_checksum("87654321"), 0)
