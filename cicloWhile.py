# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:24:54 2021

@author: Jose Alcivar Garcia
"""

class ciclos:
   
    def _init_ (self,num1=5):
    
        self.numero= num1 
    
    def usoWhile(self):
        #ciclo repetitivo que se ejecuta por verdadero y sale por falso
        car= input("ingrese vocal: ")
        car=car.lower()
        while car not in ('a','e','i','o','u'):
            car=input("ingrese vocal: ").lower()
        print("felicitaciones el caracter:{} es una vocal".format(car))
ciclo1=ciclos()
ciclo1.usoWhile()

        