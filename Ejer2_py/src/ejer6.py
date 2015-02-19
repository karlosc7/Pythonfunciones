# -*- coding: utf-8 -*-
'''
Created on 26/01/2015

@author: karlosc
'''

#Este ejercicio estaba ya correcto
def Nombre (nombre):   
    Validacion = False
    if len(nombre)<6:
        print("El nombre de usuario debe contener al menos 6 caracteres")    
    elif len(nombre)>12:
        print("El nombre de usuario no puede contener mas de 12 caracteres")
    else:       
        if nombre.isalpha() or nombre.isdigit():
            print("El nombre de usuario puede contener solo letras y numeros")                  
        else:
            print("Validacion correcta")
            Validacion = True     
    return Validacion

