'''Test suite.
'''
# diese Testklasse ruft alle Tests auf
import unittest
# für keine Warnung von Flake8: noqa: F401
from .test_vector import VectorTests  # noqa: F401


def main_tests() -> None:
    unittest.main()


if __name__ == "__main__":
    main_tests()
