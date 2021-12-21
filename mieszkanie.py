# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:43:42 2021

@author: Wiewiorka
"""

class Mieszkanie:
    def __init__(self, ulica: str, numer: int, miasto: str, pokoje: int, metr_kw: float, cena: float):
        self.ulica = ulica
        self.numer = numer
        self.miasto = miasto
        self.pokoje = pokoje
        self.metr_kw = metr_kw 
        self.cena = cena
        
    @property
    def ulica(self):
        return self.ulica
    @property
    def numer(self):
        return self.numer
    @property
    def miasto(self):
        return self.miasto
    @property
    def cena(self):
        return self.cena
    @property
    def pokoje(self):
        return self.pokoje
    @property
    def metr_kw(self):
        return self.metr_kw