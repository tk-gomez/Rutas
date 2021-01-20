# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:08:04 2021

@author: 52557
"""

import itertools

totalRutas=[]
tipos= itertools.permutations('12345',5)
for i in tipos:
    print(i)
    totalRutas.append(i)

print("\n\t====CANTIDAD TOTAL DE RUTAS====")
print(len(totalRutas))  #CANTIDAD DE RUTAS
print("\n\t====RUTAS====")
print(totalRutas)


print("\n\t====BUSCAR POSIBLES RUTAS====")
inicio = input("Rutaaaaa Inicial: ")
final = input("Rutaaaaa final: ")
i= 0
casillas = []



while i < 120:
    x = (totalRutas[i].index(inicio))
    y = (totalRutas[i].index(final))
    i= i+1
    if(x==0 and y==4 or x==4 and y==0):
        casillas.append(i-1)



#CANTIDAD DE validas
total = len(casillas)
print("\n\tTOTAL DE RUTAS VALIDAS")
print(total)
    

rutValidas =[]
q= 0
c = 0
while q < total:
    z = casillas[c]
    c = c+1
    q = q+1
   # print(z)
    #print(rutas[z])
    rutValidas.append(totalRutas[z])
    
print(rutValidas)





