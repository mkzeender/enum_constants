from enum import Enum, Flag, IntEnum, IntFlag
import pytest
from global_enum import define_enum, StrEnum, STRICT


def test_str_enum():
    global THIS
    global IS
    global NICE

    with define_enum(__name__, StrEnum) as e:

        THIS = e.f()
        IS = e.f("24.6")
        NICE = e.f("niceee")

    assert THIS == "this"
    assert repr(IS) == __name__ + ".IS"
    assert IS == "24.6"
    assert NICE == "niceee"


def test_int_enum():
    global INT1, INT2, INT3

    with define_enum(__name__, IntEnum) as e:

        INT1 = e.f()
        INT2 = e.f()
        INT3 = e.f()
    assert INT1 == 1
    assert repr(INT2) == __name__ + ".INT2"


def test_int_flag():
    global F1, F2, F3

    with define_enum(__name__, IntFlag, boundary=STRICT) as e:
        F1 = e.f()
        F2 = e.f()
        F3 = e.f(0x8)

    assert F1 == 0x1
    assert F2 == 0x2
    assert F3 == 0x8
    assert F1 | F2 == 0x3


class CustomEnum(Enum):
    pass


def test_custom_enum():
    global C1, C2, NORMAL1

    old_custom = CustomEnum
    old_enum = Enum

    with define_enum(__name__, Enum) as e:
        NORMAL1 = e.f()

    with define_enum(__name__, CustomEnum) as e:
        C1 = e.f()
        C2 = e.f()

    with pytest.raises(RuntimeError):
        with define_enum(__name__, Enum) as e:
            LOCAL_VAR = e.f()

    assert isinstance(C1, CustomEnum)
    assert type(C1) == CustomEnum
    assert old_custom != CustomEnum

    assert old_enum is Enum
    assert isinstance(NORMAL1, Enum)
    assert type(NORMAL1) != Enum

    assert C2.value == 2
    assert repr(C1) == __name__ + ".C1"
