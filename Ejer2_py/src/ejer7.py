# -*- coding: utf-8 -*-
'''
Created on 26/01/2015

@author: karlosc
'''

#A mi no me da ningún fallo de identación
def Password (password):
    ContieneMinuscula = False
    ContieneMayuscula = False
    ContieneNumero = False
    ContieneAlfanumerico = False
    ContieneEspacio = False
    ResultadoValidacion = False
    
    #Tenía un error en este if, no era "<8"
    if len(password)>=8:
        ResultadoValidacion = True

#Aquí era donde tenía errores de identación y de devolución
        for h in password:
            if h.islower():
                ContieneMinuscula = True
            if h.isupper():
                ContieneMayuscula = True
            if h.isdigit():
                ContieneNumero = True 
            if h.isalnum():
                ContieneAlfanumerico = True
            if h.isspace() == False:
                ContieneEspacio = True
    
        if ResultadoValidacion == False:
            print"El nombre de usuario debe contener al menos 6 caracteres o es insuficiente" 
        if ContieneMinuscula == False:
            print"La contraseña debe contener mayúsculas"
        if ContieneMayuscula ==False:
            print"La contraseña debe contener minúsculas"
        if ContieneNumero ==False:
            print"La contraseña debe contener al menos un número"   
        if ContieneAlfanumerico ==False:
            print"La contraseña debe contener un caracter alfanumérico"
        if ContieneEspacio == False:
            print"La contraseña debe contener al menos un espacio"
        
        #Este return estaba mal y no estaba bien indentado
        return ResultadoValidacion and ContieneMayuscula and ContieneMinuscula and ContieneNumero and ContieneAlfanumerico and ContieneEspacio == False