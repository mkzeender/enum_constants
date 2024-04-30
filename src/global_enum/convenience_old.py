import enum
from .enum_factory import EnumFactory


def enum_enum(module_name: str) -> EnumFactory[enum.Enum, object]:
    """
    Create an enum constants that are instances of enum.Enum

    with enum_enum(__name__) as e:
        AUTO_FIELD = e.f()    # defaults to ints starting at 1
        HELLO = e.f('hello')
        NUM = 42              # equivalent to e.f(42)
    """
    return EnumFactory(module_name, enum.Enum)


def int_enum(module_name: str) -> EnumFactory[enum.IntEnum, int]:
    """
    Create an enum of constant integers with extra properties (using an IntEnum).

    with int_enum(__name__) as e:
        FIELD_1 = e.f()
        FIELD_2 = e.f()   # automatic ascending order
        FIELD_42 = 42     # equivalent to e.f(42)

    assert FIELD_2 == 2
    assert repr(FIELD_2) == f"{__name__}.FIELD_2"

    """
    return EnumFactory(module_name, enum.IntEnum)


def str_enum(module_name: str) -> EnumFactory[enum.StrEnum, str]:
    """
    Create a series of constant strings, equal to their variable name in lowercase

    >>> with str_enum(__name__) as e:
    ...     THIS = e.f()       # equivalent to e.f("this")
    ...     IS = e.f()
    ...     CONVENIENT = e.f()
    ...
    >>> assert THIS == 'this'
    """
    return EnumFactory(module_name, enum.StrEnum)


def enum_flag(
    module_name: str, *, boundary: enum.FlagBoundary = enum.STRICT
) -> EnumFactory[enum.Flag, object]:
    return EnumFactory(module_name, enum.Flag, boundary=boundary)


def int_flag(
    module_name: str, *, boundary: enum.FlagBoundary = enum.KEEP
) -> EnumFactory[enum.IntFlag, int]:
    return EnumFactory(module_name, enum.IntFlag, boundary=boundary)
