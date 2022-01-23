# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden

import pytest

from ch07_recursion_advanced.solutions.ex02_edit_distance import edit_distance


@pytest.mark.parametrize("value1, value2, expected",
                         [("Micha", "Michael", 2),
                          ("Ananas", "Banane", 3)])
def test_edit_distance(value1, value2, expected):
    result = edit_distance(value1, value2)

    assert result == expected
