from typing import Protocol


class Stringable(Protocol):
    def __str__(self) -> str: ...


class Intable(Protocol):
    def __int__(self) -> int: ...
