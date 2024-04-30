import pytest
from global_enum import str_enum, int_flag, int_enum
from enum import STRICT

THAT: str = "cool"

# with EnumFactory[StrEnum, str](__name__, StrEnum) as e:
with str_enum(__name__) as e:

    THIS = e.f()
    IS = e.f()
    NICE = e.f("niceee")

with int_flag(__name__, boundary=STRICT) as e:
    F1 = e.f()
    F2 = e.f()
    F3 = e.f(0x8)

with int_enum(__name__) as e:
    INT1 = e.f()
    INT2 = e.f()


def test_str_enum():
    assert THIS == "this"
    assert repr(IS) == __name__ + ".IS"
    assert NICE == "niceee"


def test_int_enum():
    assert INT1 == 1
    assert repr(INT2) == __name__ + ".INT2"


def test_int_flag():
    assert F1 == 0x1
    assert F2 == 0x2
    assert F3 == 0x8
    assert F1 | F2 == 0x3


print(repr(THIS), THIS)
print(NICE.name, NICE)
print(repr(F3 | F2), int(F3 | F2))
print(repr(INT1), INT1)
