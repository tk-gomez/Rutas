# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:32:33 2021

@author: ANGY
"""
import itertools

ciudades=[1,2,3,4,5]
rutas= itertools.permutations(ciudades,5)
arrrutas=[]
for i in rutas:
    for n in range(len(i)-1):
        if(i[n]==1 and i[n+1]==2)or(i[n]==2 and i[n+1]==1):    
            arrrutas.append(i)
            print()
            print(i)
            print("Posicion de la casila en la que se encuentra la union o ruta\
                  entre las dos ciudades:",n)
            print("De la ruta")
    
print(arrrutas,len(arrrutas))

