import enum
from enum_constants.enum_factory import EnumFactory


def enum_enum(module_name: str) -> EnumFactory[enum.Enum, object]:
    return EnumFactory(module_name, enum.Enum)


def int_enum(module_name: str) -> EnumFactory[enum.IntEnum, int]:
    return EnumFactory(module_name, enum.IntEnum)


def str_enum(module_name: str) -> EnumFactory[enum.StrEnum, str]:
    return EnumFactory(module_name, enum.StrEnum)


def enum_flag(
    module_name: str, *, boundary: enum.FlagBoundary = enum.STRICT
) -> EnumFactory[enum.Flag, object]:
    return EnumFactory(module_name, enum.Flag, boundary=boundary)


def int_flag(
    module_name: str, *, boundary: enum.FlagBoundary = enum.KEEP
) -> EnumFactory[enum.IntFlag, int]:
    return EnumFactory(module_name, enum.IntFlag, boundary=boundary)
