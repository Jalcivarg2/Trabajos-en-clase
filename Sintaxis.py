# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:01:17 2021

@author: Jose Alcivar Garcia
"""

#num=20
#if type(num)==int:
#    print("respuesta: ", num*2)
#else:
#    print("el dato no es numerico")
#def mensaje(men):
#    print(men)
#mensaje("mi primer progama ")
#mensaje("mi segundo programa ")
class sintaxis:
    instancias =0 # variable de clases(opcional)
    _init_ 
    def _init_ (self, dato="inicializacion"):
        self.frase=dato #variable de instacia
        #sintaxis.instancia= sintaxis.instancia+1
    
    def usoVariable(self):
        edad, peso= 50, 70.5
        nombres= "Daniel Vera"
        tipo_sexo= "M"
        civil= True
        # tuplas=() son colecciones de datos de cualquier tipo inmutable
        usuario=()
        usuario= ('dchili', '1234', 'chiki@gmail.com', True)
        #usuario[3]="milagro"
        #listas=[] coleccione mutables
        materias=[]
        materias=['programacion web', 'PHP', 'POO']
        materias[1]="Python"
        materias.append("Go")
        #diccionario ={} colecciones de objetos clave: valor tipo json
        docente{}
        docente={'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        docente['carrera']="CS"
        # presentacion con format
        #print("""Mi nombre es {}, tengo{} años""".format(nombres, edad))
        #print(usuario, materia, docentes)
        #print(usuario, usuario[0], usuario[0:2], usuario[-1])
        print (materia, materias[2:], materias[:3], materias[:],materias[-2:])
        
        #print(docente, docente['nombre'])
        
     
       

ejer1= sintaxis()#se crea un objeto que es una instancia de la clase y se ejecuta el constructor
ejerc1.usoVariables()

        