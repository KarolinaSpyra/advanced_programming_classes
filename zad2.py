# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:31:51 2021

@author: Wiewiorka
"""
name = []
liczby = []
ten = []

def imiona(name):
    print("Lista imion:")
    for i in range (len(name)):
        print(name[i])
    print("\n")


def num(liczby):
    print("Pomnożone liczby (for):")
    newLiczba = [l*2 for l in liczby]
    return newLiczba


def nums(liczby):
    print("Pomnożone liczby (lista składana):")
    newLiczby = []
    for i in range (len(liczby)):
        newLiczby.append(liczby[i] * 2)
    return newLiczby

def parzyste(ten):
    print("Liczby parzyste:")
    for i in range (len(ten)):
        if ten[i] % 2 == 0:
            print(ten[i])
def dwa(ten):
    print("Co druga liczba:")
    for i in range (len(ten)):
        if i % 2 == 0:
            print(ten[i]) 


x = [2, 10, 4, 20, 1]     
y = ['Ron', 'Ana', 'Emma', 'Tom', 'Andy']
z = [2, 10, 15, 8, 12, 24, 45, 50, 3, 1]
imiona(y)
print(num(x))
print("\n")   
print(nums(x))
print("\n")    
parzyste(z)
print("\n")
dwa(z)

 
    