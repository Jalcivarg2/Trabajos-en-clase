# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:09:39 2021

@author: Jose Alcivar Garcia 
"""

class Ordenar:
    def _init_ (self, lista):
        self.lista=lista
    def burbuja(self):
        for i in range (len(self.lista)):
            for j in range(i+1, len (self.lista)):
                if self.lista [i]> self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux
ord1= Ordenar([1,6,8,2,0])
ord1.burbuja()
print(ord1.lista)
                    