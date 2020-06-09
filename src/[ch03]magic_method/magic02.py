# Python Data Model = Special Method(Magic Method)

class Vector:
    """
    Title : 클래스 예제 2
    Author : Minwook Je
    Desc : 백터 계산
    Ex :
        > (5,2) + (4,3) = (9,5)
        > (10,3) * 5 = (50,15)
        > Max((5,10)) = 10
    """

    def __init__(self, *args):
        """Create a vector, example : v = Vector(5,10)"""
        if len(args) == 2:
            self._x, self._y = args
        else:
            self._x, self._y = 0, 0

    def __repr__(self):
        """Return the vector information"""
        return "Vector(%r, %r)" % (self._x, self._y)  # %r repr raw data

    def __add__(self, other):
        """Return the result of Vector addition about self and other"""
        return Vector(self._x + other.x, self._y + other.y)

    def __mul__(self, other):
        """Return the result of Vector multiplication about self and other"""
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        """Return the bool value about self coordinate is not (0,0) or not"""
        return bool(max(self._x, self._y))

    @property
    def x(self):
        """Getter for x"""
        return self._x

    @property
    def y(self):
        """Getter for y"""
        return self._y

    @x.setter
    def x(self, value):
        """Setter for x"""
        self._x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        self._y = value


# Vector Instance
v1 = Vector(5, 7)
v2 = Vector(23, 57)
v3 = Vector()
print(v1, v2, v3)

# __doc__
print(Vector.__doc__)
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)
print(Vector.x.__doc__)
print(Vector.y.__doc__)  # TODO: setter 호출하는방법이 있나?

# magic method
print(v1 + v2)
print(v1 * 3)

bool_printer = lambda x : print("Warning") if bool(x) == False else print(bool(x))
bool_printer(v1)
bool_printer(v2)
bool_printer(v3)
