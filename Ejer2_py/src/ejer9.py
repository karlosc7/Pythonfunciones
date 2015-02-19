# -*- coding: utf-8 -*-
'''
Created on 26/01/2015

@author: karlosc
'''

# Pedimos un número binario, sólo puede ser binario
#El ejercicio estaba correcto
def EsONoBinario ():
    NumBinario = str(input("Numero Binario: "))
    for digito in NumBinario: 
        if digito != "0" and digito != "1": 
            print"El número", NumBinario,"no es un número binario"
            return False
    print(NumBinario)
    print"El numero", NumBinario, "es binario"
    return True
print EsONoBinario()
    
def Decimal (Binario):
    BinarioADec = int(str(Binario), 2)    
    return BinarioADec
print Decimal(101)

def Binario (Decimal):
    DecimalABin = int(bin(Decimal)[2:])
    return DecimalABin
print Binario(5)

def Hexa (Decimal):
    DecimalAHexadecimal = hex(Decimal)[2:]
    return DecimalAHexadecimal
print Hexa(5)
    
def EsHexa (Hexa):
    ValoresHexadecimales = set("0123456789abcdefABCDEF")
    for digito in Hexa:
        if not (digito in ValoresHexadecimales):
            print"El n�mero",Hexa,"no es un n�mero hexadecimal"
            return False
    print"El numero",Hexa,"es un n�mero hexadecimal"
    return True
print EsHexa('A')

def DecHexa (Decimal):
    DecimalAHexadecimal = str(int(Decimal, 16))
    return DecimalAHexadecimal
print DecHexa('5')
