# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:32:33 2021

@author: ANGY
"""
import itertools

ciudades=[1,2,3,4,5]
rutas= itertools.combinations(ciudades,2)
print(rutas)
rutas= itertools.permutations(ciudades,5)
arrrutas=[]
for i in rutas:
    costo=0
    for n in range(len(i)-1):
        if(i[n]==1 and i[n+1]==2)or(i[n]==2 and i[n+1]==1):    
            costo=costo + 10
        if(i[n]==1 and i[n+1]==3)or(i[n]==3 and i[n+1]==1):    
            costo=costo + 55
        if(i[n]==1 and i[n+1]==4)or(i[n]==4 and i[n+1]==1):    
            costo=costo + 25
        if(i[n]==1 and i[n+1]==5)or(i[n]==5 and i[n+1]==1):    
            costo=costo + 45
        if(i[n]==2 and i[n+1]==3)or(i[n]==3 and i[n+1]==2):    
            costo=costo + 20
        if(i[n]==2 and i[n+1]==4)or(i[n]==4 and i[n+1]==2):    
            costo=costo + 25
        if(i[n]==2 and i[n+1]==5)or(i[n]==5 and i[n+1]==2):    
            costo=costo + 40
        if(i[n]==3 and i[n+1]==4)or(i[n]==4 and i[n+1]==3):    
            costo=costo + 15
        if(i[n]==3 and i[n+1]==5)or(i[n]==5 and i[n+1]==3):    
            costo=costo + 30
        if(i[n]==4 and i[n+1]==5)or(i[n]==5 and i[n+1]==4):    
            costo=costo + 50
        
    arrrutas.append([i,costo])        
    
print(arrrutas,len(arrrutas))


