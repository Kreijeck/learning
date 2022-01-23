# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden

import itertools

print(list(itertools.compress("ABCDEF", [1,0,1,0,1,0])))
