# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:35:51 2021

@author: Jose Alcivar Garcia
"""

class For:
    def _init_ (self):
        pass
    #ciclo repetitivos de incrementos o decrementos se ejecuta mientras tenga valores
    
    def usoFor(self):
        datos= ["Daniel", 50,True]
        numeros=(2,5,6,4,1)
        docente={'nombre':"Daniel","edad":50,'fac':'faci'}
        listaNotas= [(30,40),[20,40],(50,40)]
        listaAlumnos=[{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #se ejecuta desde inicio hasta el limite
        #for i in range (5): #rango(0,1,2,3,4)
        #    print("i={}".format(i))
        #for i in range(2,10): # rango(2,3,4,5,6,7,8,9)
        #    print("i={}".format(i))
        #for i in range(4,10,2):# rango(4,6,8)
        #    print("i={}".format(i), end=" ")
        for i in range(12,3,-3):#rango(4,6,8)
            print ("i=´{}".format(i),end=" ")
        
        #longitud=len(datos)
        #print(datos[0])
        #print(datos[1])
        #print(datos[2])
        #j=0
        #while j < longitud:
        #    print("while",datos[j])
        #    j=j+1
        
        # for i in range(longitud-1,-1,-1):
        #    print ("for",datos[i])
        # for i, dato in enumerate(numeros):
        #    print("for",i,dato)
        # dato toma cade elemento de la coleccion numeros (cadena, listas, tupla)
        # for dato in numeros:
        #    print(dato)
        #for dato in ['H','O','L','A','que','tal']:
        #    print(dato)
        print("\nDiccionario de notas")
        # for clave, valor in docente.item():
        # print (clave,":",valor,end=" ")
        
        for alumnos in listaAlumnos:
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
            
bucle1= For()
bucle1.usoFor()


    