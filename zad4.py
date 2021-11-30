# -*- coding: utf-8 -*-


def suma(x: int, y: int, z: int) -> bool:
    if (x + y) >= z:
        return True
    else:
        return False

u = suma(1, 5, 11)
print(u)
