# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:21:17 2021

@author: Jose Alcivar Garcia
"""

from cargos import cargos


class Empleado:
    secuencia=0
    def _init_ (self, nom, ced,sue,cargos):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargos
    def mostrar (self):
        print ("codigo: {} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descri))
    
    def  generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    
    
cargo1= Cargo("Docente")
emp1= Empleado("Daniel","0914",500,cargo1)
emp1.mostrar()
cargo2= Cargo("Analista")
emp2= Empleado("Ana","0914",500, cargo2)
emp2.mostrar()