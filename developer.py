# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:31:02 2021

@author: Wiewiorka
"""

class Developer:
        def __init__(self, imie: str, nazwisko: str, nazwa_firmy: str, miasto: str):
            self.imie = imie
            self.nazwisko = nazwisko
            self.nazwa_firmy = nazwa_firmy
            self.miasto = miasto
        
        @property
        def imie(self):
            return self.imie
        @property
        def nazwisko(self):
            return self.nazwisko
        @property
        def miasto(self):
            return self.miasto
        @property
        def nazwa_firmy(self):
            return self.nazwa_firmy

       