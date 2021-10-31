#!/usr/bin/python
#coding: utf-8

# Filename  : QuickSort.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/RadixSortPython
# pep8: 100%

#---- Importaciones ----
from functools import reduce

def ndigitos(lista):
    digitoMax = 0
    for num in lista:
        digitoMax = max(digitoMax, num)
    return len(str(digitoMax))
 

def flatten(lista):
    return reduce(lambda x, y: x + y, lista)
 
def RadixSort(lista):
    digitos = ndigitos(lista)
    for digito in range(0, digitos):
        t = [[] for i in range(10)]
        for elemento in lista:
            num = (elemento // (10 ** digito)) % 10
            t[num].append(elemento)
        lista = flatten(t)
    return lista
 
 
c = int(input("¿Cuántos datos deseas ingresar?\n >: "))
lista = []
for i in range(0, c):
    lista.append(int(input("Introduce un dato >: ")))
print("\n   +- Lista dada: ", lista)
print("\n   +- Lista ordenada: ", RadixSort(lista))