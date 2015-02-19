# -*- coding: utf-8 -*-
'''
Created on 22/01/2015

@author: karlosc
'''

#Cambios en la identación
#Acoto dependiendo de la nota su calificación mediante ifs
def Notas (nota):  
    #Le pido al usuario la nota por teclado  
    nota=float(raw_input ("introduce la nota:")) 
    
    if nota<5:
        frase = "Suspenso"
    elif nota>=5 and nota<7:
        frase = "Aprobado"
    elif nota>=7 and nota<=8.5:
        frase = "Notable"
    elif nota>=8.5 and nota<10:
        frase = "Sobresaliente"
    elif nota==10:
        frase = "Matricula de Honor"
    else:
        frase = "Nota no valida"        
    return frase

#Imprimo la calificación de la nota que he introducido
print Notas(3)

#No he conseguido acoplar esta función sobre el ejercicio 2
'''
import Ejer2_py.ejercicio_4

aprobados=0
suspensos=0
cantidadapro=0
cabtidadsus=0
cont=0

cant=int(raw_input("Introduce la cantidad de notas que deseas introducir: "))


while cant!=cont:
     
    
    nota=int(raw_input ("Introduce la nota:"))

    if (nota<9):
    
        if (nota>=5):
            sumapro=cantidadapro+nota  
            apro=apro+1  
        
        else:
            cantidadsus=cantidadsus+nota  
            suspensos=suspensos+1 
    cont=cont+1  


print "la cantidad de Notas aprobadas  es : "+ str(apro)
print "la cantidad de Notas suspensas es : " + str(sus)   
    
    
 '''  
      
      
        
    
