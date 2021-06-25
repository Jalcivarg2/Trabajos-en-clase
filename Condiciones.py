# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:50:00 2021

@author: Jose Alcivar Garcia
"""

class condicion:
    contador =0 # variable de clases(opcional)
   # _init_ metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
   # e inicializar los atributos de la clase self es un objetivo que representa la clase 
    def _init_ (self,num1=0, num2=1):
    
        self.numero1= num1 #variable de instacia
        self.numero2=num2
        numero= num1+num2
        self.numero3= numero()
        #variables de instancia
    
    def usoIf(self):
        # if...elif...else...: permite condicionar la ejecucion de uno o varios bloques
        # de sentencias al cumplimiento de una o varias condiciones.
        if  self.numero1==self. numero2:
            print("numero1:{}, numero2:{}: son iguales". format(self.numero1, self.numero2))
        elif self.numero1== self.numero3:
            print("numero1:{}, numero3:{}: son iguales". format(self.numero1, self.numero3))
        else:
            print("no son iguales")

#usar clase
#cond1= condicion()
#print(cond1.numero1)
#print(cond1.numero2)

cond2= condicion(10,20)
cond2.usoIf()# llamada a un metodo de clase
print(cond2.numero1)#llamada a un atributo de clase
       
        