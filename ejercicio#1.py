# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:46:13 2021

@author: Jose Alcivar Garcia 
"""

class Fraccion:
     def __init__(self,numerador,denominador):
         self.num = numerador
         self.den  = denominador
     def show(self):
         print(self.num,"/",self.den)
x = Fraccion(1,2)
y = Fraccion(2,3)
print(x.show())
print(x.show())

