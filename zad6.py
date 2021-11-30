# -*- coding: utf-8 -*-


def dzialanie(x: list, y: list) -> list:
    
    for i in y:
        if i not in x:
            x.append(i)
    x = [i ** 3 for i in x]
    return x

q = dzialanie([3,6,9,2], [1,3,6,7])
print(q)