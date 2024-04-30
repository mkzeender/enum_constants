import enum
from typing import Any, overload
from .enum_factory import DecoratorList, EnumFactory


@overload
def define_enum[
    Enum: enum.StrEnum
](module_name: str, enum_type: type[Enum], /) -> EnumFactory[Enum, str]: ...


@overload
def define_enum[
    Enum: enum.IntEnum
](module_name: str, enum_type: type[Enum], /) -> EnumFactory[Enum, int]: ...


@overload
def define_enum[
    Enum: enum.IntFlag
](
    module_name: str,
    enum_type: type[Enum],
    /,
    *,
    boundary: enum.FlagBoundary = enum.STRICT,
    **kwds,
) -> EnumFactory[Enum, int]: ...


@overload
def define_enum[
    Enum: enum.Flag, DType: type[int]
](
    module_name: str,
    enum_type: type[Enum],
    /,
    data_type: DType,
    *,
    boundary: enum.FlagBoundary = enum.KEEP,
    **kwds,
) -> EnumFactory[Enum, DType]: ...


@overload
def define_enum[
    Enum: enum.Flag
](
    module_name: str,
    enum_type: type[Enum],
    /,
    *,
    boundary: enum.FlagBoundary = enum.KEEP,
    **kwds,
) -> EnumFactory[Enum, int]: ...


@overload
def define_enum[
    Enum: enum.Enum, DType: type
](
    module_name: str,
    enum_type: type[Enum],
    /,
    data_type: DType,
    **kwds,
) -> EnumFactory[
    Enum, DType
]: ...


@overload
def define_enum[
    Enum: enum.Enum
](module_name: str, enum_type: type[Enum], /, **kwds,) -> EnumFactory[Enum, object]: ...


def define_enum(module_name, enum_type, /, data_type=object, **opts):
    return EnumFactory(module_name, enum_type, decorators=(), **opts)
