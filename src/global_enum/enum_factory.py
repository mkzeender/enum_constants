from __future__ import annotations
import enum
import sys
from functools import lru_cache
from typing import Any, Callable, Iterable

type DecoratorList[Enum: enum.Enum] = Iterable[Callable[[type[Enum]], type[Enum]]]


class EnumFactory[Enum: enum.Enum, DType]:
    def __init__(
        self,
        module_name: str,
        enum_cls: type[Enum],
        decorators: DecoratorList[Enum] = (),
        ignore: Iterable[str] = (),
        **options: Any,
    ) -> None:

        self.module_name = module_name
        self.enum_cls = enum_cls
        self.decorators = decorators

        self.module = sys.modules[module_name]
        self.ignores = set(self.module.__dict__.keys())
        self.ignores.update(ignore)
        self.options = options

    @lru_cache(1)
    def create(self) -> type[Enum]:

        opts = self.options
        metaclass: type = opts.pop("metaclass", type(self.enum_cls))
        class_name = self.module_name.split(".")[-1]

        # prepare the class namespace
        namespace = metaclass.__prepare__(class_name, (self.enum_cls,), **opts)

        # add the new fields to the namespace
        for k, v in self.module.__dict__.items():
            if k not in self.ignores and not isinstance(v, EnumFactory):
                namespace[k] = v

        # create a subclass of self.enum_t
        enum_cls: type[Enum] = metaclass(
            class_name, (self.enum_cls,), namespace, **opts
        )

        # mark it as having the correct module
        enum_cls.__module__ = self.module_name
        enum_cls.__qualname__ = self.module_name

        # decorate it with the decorators
        for dec in self.decorators:
            enum_cls = dec(enum_cls)

        # mark it as a global_enum, which it is by design!
        enum_cls = enum.global_enum(enum_cls)

        return enum_cls

    def export(self):
        enum_cls = self.create()

        # put the members into the global namespace of the module
        # overwriting the temporary field instances.
        self.module.__dict__.update(enum_cls._member_map_)

    def field(self, *field_values: DType | enum.auto) -> Enum:
        if len(field_values) == 0:
            return enum.auto()  # type: ignore
        elif len(field_values) == 1:
            return field_values[0]  # type: ignore
        else:
            return field_values  # type: ignore

    f = field

    def __enter__(self):
        return self

    def __exit__(self, etype, eval, etb):
        self.export()
        return False


# class _CallableField[ArgT, RetT](Protocol):
#     def __call__(self, *field_values: ArgT) -> RetT: ...
