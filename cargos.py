# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:00:37 2021

@author: Jose Alcivar Garcia
"""

class Cargo:
    secuencia=0
    def _init_{self,des="sin cargo"}:
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des
    
cargo1= Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2=cargo()
cargo2.descripcion="Director"
print(cargo2.codigo,cargo2.descripcion)
cargo3= Cargo("Analista")
print(cargo3.codigo, cargo3.descripcion)
# print (Cargo.secuencia)
# print(cargo1.secuencia)
# print(cargo2.secuencia)
# print(cargo3.secuencia)

        
               
    