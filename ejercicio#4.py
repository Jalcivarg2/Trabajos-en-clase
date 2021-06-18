# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:13:34 2021

@author: Jose Alcivar Garcia 
"""

#for range(v)- range(vi, vf)- range(vi, vf, inc)

frase = input("ingrese frase: ")
for indice in range(len(frase)):
    print(indice,"=", frase[indice])
# for in cadena - in(tupla)-in[lista]
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in["A","E","I","O","U"]:
            continue
        else:
            cvoc= cvoc+1
print("cantidad vocales:{}".format(cvoc))
# comprehension - [var for var in datos condicion]
[car for car in["a","e","i","o","u"] if car not in ("a","i","o")]