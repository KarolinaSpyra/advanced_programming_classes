# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:43:42 2021

@author: Wiewiorka
"""
import developer as dev
import mieszkanie as miesz
import dom as dom
from numpy import *

class Zamowienie:
    def __init__(self, ilosc_dom: int, ilosc_mieszkanie: int, cena: float, pokoje: int, metr_kw: float):
        self.ilosc_dom = ilosc_dom
        self.ilosc_mieszkanie = ilosc_mieszkanie
        self.cena = cena
        self.pokoje = pokoje
        self.metr_kw = metr_kw
        
    @property
    def ilosc_dom(self):
        return self.ilosc_dom
    @property
    def ilosc_mieszkanie(self):
        return self.ilosc_mieszkanie
    @property
    def cena(self):
        return self.cena
    @property
    def pokoje(self):
        return self.pokoje
    @property
    def metr_kw(self):
        return self.metr_kw
    
    @ilosc_dom.setter
    def ilosc_dom(self, value: int) -> None:
        self.ilosc_dom = value
    @ilosc_mieszkanie.setter
    def ilosc_mieszkanie(self, value: int) -> None:
        self.ilosc_mieszkanie = value
    @cena.setter
    def cena(self, value: float) -> None:
        self.cena = value
    @pokoje.setter
    def pokoje(self, value: int) -> None:
        self.pokoje = value
    @metr_kw.setter
    def metr_kw(self, value: float) -> None:
        self.metr_kw = value
    
    
    def wartosc(cena_a: float, cena_b: float) -> float:
        cena_a = miesz.cena
        cena_b = dom.cena
        cena_c = cena_a + cena_b
        return (cena_c, 2)
    def metry_kw(metry_kwa: float, met_kwb: float) -> float:
        metry_kwa = miesz.metry_kw
        metry_kwb = dom.metry_kw
        metry_kwc = metry_kwa + metry_kwb
        return metry_kwc
        
z = Zamowienie(2, 5, 4230400, 56, 12312)       
d = dev('Andrzej', 'Zawadzki', 'ORNX', 'Warszawa')
m = miesz('Modrzejowa', 12, 'Warszawa', 5, 60.0, 300500)
do = dom('Wejcherowa', 27, 'Warszawa', 8, 120.0, 900000)
print(dev)
print(z.wartosc) 
zam = Zamowienie(1, 0, 150000, 4, 25.5)
zam.cena = miesz.cena(15000)
print(zam.cena())        