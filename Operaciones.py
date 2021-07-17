# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 12:08:13 2021

@author: Jose Alcivar Garcia 
"""

class Operaciones:
    def _init_(self , num1, num2):
        self.numero1=num1
        self.numero2=num2
    
    def suma(self):
        suma=self.numero1 + self.numero2
        return suma
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        return self.numero1 / self.numero2
    
    def divisionEntera(self):
        if self.numero2 !=0: return self.numero1 // self. numero2
        return 0
    
    def reciduo(self):
        return self.numero1 % self.numero2
    
    def exponente(self):
        return self.numero1 ** self.numero2
    
    def mostrar(self):
        print("operando1={}, operando2={}", format(self.numero1, self.numero2))
        
print("Menu operaciones matematicas")
print("1) suma\n2) resta\n3) multiplicacion\n4) division\n5) division entera\n6) reciduo\n7) exponente\n8")
opc= '0'

while opc != '8':
    if opc == '1':
        num1= int(input("ingrese numero1: "))
        num2= int(input("ingrese numero2: "))
        opc = Operaciones(num1, num2)
        if opc == '1':
            print("{}+{}={}".format(opc.numero1, opc.numero2, opc.suma()))
        elif opc == '2':
            print("{}-{}={}".format(opc.numero1, opc.numero2, opc.resta()))
        elif opc == '3':
            print("{}-{}={}".format(opc.numero1, opc.numero2, opc.multiplicacion()))

print("gracias por su visita: ")











