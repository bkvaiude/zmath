from zmath import extras
from zmath.zmathplus import divide
from zmath.zmathplus.divide import divide as div
from zmath.zmathplus.extras.multiply import multiply
from zmath.add import add

from zmath.extras import subtract


from zmath.zmathsquare.extras.sqroot import sqroot
from zmath.zmathsquare.sq import square


def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(-1, -2) == -3


def test_subtract():
    assert subtract.subtract(1, 2) == -1


def test_multiply():
    assert multiply(1, 2) == 2


def test_sq():
    assert square(2) == 4


def test_sqrt():
    assert sqroot(4) == 2


def test_divide():
    assert divide.divide(1, 2) == 0.5
    assert div(1, 2) == 0.5


def test_zmath():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_sq()
    test_sqrt()
    print("All tests passed!")


if __name__ == "__main__":
    test_zmath()
