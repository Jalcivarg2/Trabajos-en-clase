# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:02:35 2021

@author: Jose Alcivar Garcia
"""
"""uso de while infinito"""

c=1
while True:
    print(c)
# while validacion
vocal= input("ingrese vocal: ")
while vocal not in ("a", "e","i","o", "u"):
    if vocal ==".":
        break
    vocal= input("vocal:")
print("su vocal o punto es:{}", format(vocal))
    
