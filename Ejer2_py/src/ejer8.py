# -*- coding: utf-8 -*-
'''
Created on 26/01/2015

@author: karlosc
'''

#Tenía mal puestos los nombres de los ejercicios a importar
import ejer6
import ejer7

#No puedo usar las librerías de los caracteres
'''
from Tkconstants import CHAR
def Hola (nombre, password):
    ResultadoValidacion = False
    if ejercicio6(nombre) and ejercicio7(password):
        ResultadoValidacion = True
        
    return ResultadoValidacion
print Hola("hola","jolalls12")
'''
#Vuelvo a realizar el ejercicio de nuevo

#Solicito el nombre del usuario para realizar las comprobaciones
#Con respecto a los dos ejercicios anteriores

nombre = (raw_input ("Introduce tu nombre de usuario:"))
#Solicito el nombre para comprobarlo del ejercicio 6
if ejer6.Nombre(nombre):
    print "El nombre de este usuario es correcto"
else:
    print"El nombre del usuario es incorrecto"
    
cont= (raw_input("Introduce la contraseña: "))
#Solicito la contraseña para comprobarlo del ejercicio 7
if ejer7.Password(cont):
    print "la contraseña es correcta"
else:
    print"contraseña invalida"
