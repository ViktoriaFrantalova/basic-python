from typing import Union, Optional

def foo(x: int) -> Optional[int]:
    if x > 0:
        return x
    else:
        return None

def fee(x: int) -> bool:
    return x%2 == 0

def fluff(x: None) -> None:
    return None

a = 2
b = foo(a)
if b is not None:
    c = fee(b)
else:
    c = False
