# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:51:01 2021

@author: Jose Alcivar Garcia 
"""

x= int (input("ingresa un numero entero: "))
if x < 0:
    x = 0
    print("negativo cambiado a 0")
elif x ==0:
    print("cero")
elif x==1:
    print("uno")
else:
    print("ninguna opcion")
print("ok") if type(x)== int else print(".")