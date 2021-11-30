# -*- coding: utf-8 -*-


def liczba(x: int) -> bool:
    y = x % 2 
    if y == 0:
        return True
    else:
        return False
    
z = liczba(21)

if z == True:
    print("Liczba parzysta")
elif z == False:
    print("Liczba nieparzysta")
        