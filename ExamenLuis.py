# -*- coding: utf-8 -*-
import random
    
veces = int(input("¿Cuántas veces deseas tirar los dados? "))
arreglo = []
arregloDos = [0,0,0,0,0,0,0,0,0,0,0,0,0]
a = 0
cont = 0
contDos = 0
    
for i in range(veces):
    valor1 = random.randrange(6)+1
    valor2 = random.randrange(6)+1
    suma = valor1 + valor2
    print "Dado 1 = "  ,valor1, " Dado 2 = " ,valor2, " Suma = " ,suma
    arreglo.append(suma)
for x in arreglo:
    a = x
    arregloDos[a] = arregloDos[a] + 1
    cont+=1
print 
for y in arregloDos:
    if arregloDos[contDos] != 0:
        print "El numero " ,contDos, " aparece " , arregloDos[contDos], " veces"
    contDos+=1
