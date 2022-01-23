import numbers
from math import sqrt
from functools import total_ordering



@total_ordering
class Vector2D:
    def __init__(self, x=0, y=0) -> None:
        # check Reale Zahlen --> Throw Fehler so früh wie möglich!
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass int/float values for x and y!')

    # wird verwendet wie ein __init__ zu späterem zeitpunkt. wird aufgerufen wenn die Funktion "gecallt wird"
    # beispielsweise um ein update o.ä. zu bekommen
    def __call__(self):
        print("Calling the __call__ function")
        print(self.__repr__())

    # Ausführliche für Developer
    def __repr__(self) -> str:
        return f'vector.Vector2D({self.x}, {self.y})'

    # Custom für User
    def __str__(self) -> str:
        return f'{self.x}, {self.y}'

    # trigger for if-Abragen: if Vector2d: blabla
    def __bool__(self):
        return bool(abs(self))

    #Betrag
    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    # check whether is correct type!
    def check_vector_types(self, vector2):
        if not isinstance(vector2, Vector2D):
            raise TypeError("Types have to pass in two instances of the vector class!")

    # Equal
    def __eq__(self, other_vector):
        self.check_vector_types(self, other_vector)
        if self.x == other_vector.x and self.y == other_vector.y:
            return True
        else:
            return False

    # only __eq__ and one of lt, le, gt, ge must be implemented. Rest can be calculated
    # with decorator total_ordering

    # lt = less than
    # le = less equal
    # gt = greater than
    # ge = grater equal
    def __lt__(self, other_vector):
        self.check_vector_types(self, other_vector)
        if abs(self) < abs(other_vector):
            return True
        else:
            return False


    def __add__(self, other_vector):
        self.check_vector_types(self, other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)
    # try (==1):
    # except(>= 1):
    # finally(optional):

    # als Alternative
    def __sub__(self, other_vector):
        try:
            x = self.x - other_vector.x
            y = self.y - other_vector.y
            return Vector2D(x, y)
        except AttributeError as aterr:
            print(e)
        except Exception as e:
            print(e)
        finally:
            print("finally block!")

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError('You must pass in either a vector instance or int/float number')

    # __div__ existiert seit Python2 nicht mehr!
    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError("You cannot divide by zero!")
        else:
            raise TypeError('You have to pass in an int/float value!')
