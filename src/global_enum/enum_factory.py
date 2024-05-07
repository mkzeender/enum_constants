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
        enum_type: type[Enum],
        decorators: DecoratorList[Enum] = (),
        ignore: Iterable[str] = (),
        **options: Any,
    ) -> None:

        self.module_name = module_name
        self.enum_type = enum_type
        self.decorators = decorators

        self.module = sys.modules[module_name]
        self.ignores = set(self.module.__dict__.keys())
        self.ignores.update(ignore)
        self.options = options

        self.is_created = False

    def create(self, export: bool = False) -> type[Enum]:

        if self.is_created:
            raise RuntimeError("Already Created")

        opts = self.options
        metaclass: type = opts.pop("metaclass", type(self.enum_type))
        enum_type_name: str = self.enum_type.__name__

        export_class: bool = (
            export
            and self.enum_type.__module__ == self.module_name
            and self.module.__dict__.get(enum_type_name) is self.enum_type
        )

        class_name: str = self.enum_type.__name__ if export_class else "_GlobalEnum"

        # prepare the class namespace
        namespace = metaclass.__prepare__(class_name, (self.enum_type,), **opts)

        # add the new fields to the namespace
        success = False
        for k, v in self.module.__dict__.items():
            if k not in self.ignores and not isinstance(v, EnumFactory | enum.EnumMeta):
                success = True
                namespace[k] = v
        if not success:
            raise RuntimeError(
                f"No fields detected! Make sure the fields are global constants in the module {self.module_name}."
            )

        # create a subclass of self.enum_type
        new_cls: type[Enum] = metaclass(
            class_name, (self.enum_type,), namespace, **opts
        )

        # decorate it with the decorators
        for dec in self.decorators:
            new_cls = dec(new_cls)

        # mark it as a global_enum, which it is by design!
        new_cls = enum.global_enum(new_cls)

        # mark it as having the correct module
        new_cls.__module__ = self.module_name

        # if it's a custom enum class defined in the same module, overwrite that class!
        if export_class:
            self.module.__dict__[enum_type_name] = new_cls
            new_cls.__qualname__ = self.enum_type.__qualname__

        else:
            new_cls.__qualname__ = self.module_name + "." + class_name

        if export:
            # put the members into the global namespace of the module
            # overwriting the temporary field instances.
            self.module.__dict__.update(new_cls._member_map_)

        self.is_created = True

        return new_cls

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
        self.create(export=True)
        return False
