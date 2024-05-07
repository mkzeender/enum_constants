# Global-Enum
Create groups of global constants that behave like Enums

```python
from global_enum import define_enum, StrEnum

with define_enum(__name__, StrEnum) as e:
    FIELD1 = e.f() # 
    FIELD2 = e.f()
    FIELD3 = e.f()

print(FIELD1)
print(repr(FIELD1))

# output:
# field1
# your_module.FIELD1
```
