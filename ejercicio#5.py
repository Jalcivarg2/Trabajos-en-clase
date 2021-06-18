# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:32:54 2021

@author: Jose Alcivar Garcia
"""

'''funciones sin retorno'''
def vocales (frase):
    for car in frase:
        if car in ("a","e","i","o","u"):
            print(car)
"llamada a funcion"
oracion = input("ingrese oracion:")
vocales(oracion.lower())
'''funcion con retorno de valor'''
def promedio(notas):
    summ= 0
    for n in notas:
        summ+=n
    return summ/len(notas)
# llamada a funcion
listanotas= [2,4,6,8,10]
prom= promedio(listanotas)
print("promedio:{}={}".format(listanotas,prom))
