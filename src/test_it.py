from enum_constants import str_enum, int_flag
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


print(repr(THIS))
print(repr(F3 | F2), int(F3 | F2))
