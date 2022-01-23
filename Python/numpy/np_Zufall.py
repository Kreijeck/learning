import numpy as np
from numpy.random import choice, randint

choices = [
    "A",
    "B",
    "C",
]

# zusammen sollte wahrscheinlichkeit 1 ergeben
probability = [0.1, 0.1, 0.8]
# sind Randomwerte mit Gewichtung!
# default p: Gleichverteilt
# size: Größe als Shape
print(choice(choices, size=(2,2,3), p=probability))

# randint(start(inklusiv), stop(exclusiv), size=...): 
print(randint(1, 42, size=(3, 3)))