import enum
from typing import Any, overload
from .enum_factory import DecoratorList, EnumFactory
from .protocols import Stringable, Intable


@overload
def define_enum[
    Enum: enum.StrEnum
](module_name: str, enum_type: type[Enum], /) -> EnumFactory[Enum, Stringable]: ...


@overload
def define_enum[
    Enum: enum.IntEnum
](module_name: str, enum_type: type[Enum], /) -> EnumFactory[Enum, Intable]: ...


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
    Enum: enum.Flag, DType: type[Intable]
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
) -> EnumFactory[Enum, Intable]: ...


@overload
def define_enum[
    Enum: enum.Enum, DType: type
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
    Enum: enum.Enum
](
    module_name: str,
    enum_type: type[Enum],
    /,
    *,
    boundary: enum.FlagBoundary = enum.KEEP,
    **kwds,
) -> EnumFactory[Enum, object]: ...


def define_enum(module_name, enum_type, /, data_type=object, **opts):
    return EnumFactory(module_name, enum_type, decorators=(), **opts)
