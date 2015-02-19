# -*- coding: utf-8 -*-
'''
Created on 22/01/2015

@author: karlosc
'''

print 'Este programa averigua cu�l es tu letra del DNI a partir del n�mero d'

#Esta función halla la letra del número de DNI
def hallarLetra (DNI):   
    #Solicito al usuario el DNI completo como me decías en la correción
    DNI=int(raw_input ("Introduce solamente tu numero de dni:"))
    #Le meto las letras que se obtienen dependiendo del numero DNI  
    NIF = 'TRWAGMYFPDXBNJZSQVHLCKE'
    
    print "La letra del DNI es", NIF[DNI%23]
    
hallarLetra()


#Ahora el usuario si puede meter el DNI con su letra y compararla para saber si es correcta
Numero =int(raw_input ("Introduce tu numero de DNI:"))
Letra =raw_input ("Introduce la letra de DNI:")
NIF2='TRWAGMYFPDXBNJZSQVHLCKE'


if Letra==NIF2[Numero%23]:
    print "la letra es correcta"
else:
    print "la letra es incorrecta"
    
#Vale y siempre devuelve verdadero el true no es una asignación esta parte
#que está mal la dejo comentada
'''    
    return NIF[DNI % 23]
print HallarLetra(48546221)

def Letra (DNI, letra):     
    ObtenerLetra = Letra(DNI)
    return ObtenerLetra == letra.upper()
print Letra(48546221,'y')
'''