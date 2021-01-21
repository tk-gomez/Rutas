# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:23:31 2021

@author: iramv
"""
import itertools

ciudades=[1,2,3,4,5]
rutas= itertools.combinations(ciudades,2)
print(rutas)
rutas= itertools.permutations(ciudades,5)


totalRutas=[]
for p in rutas:
    costo=0
    n = 0
    for n in range(len(p)-1):
        if(p[n]==1 and p[n+1]==2)or(p[n]==2 and p[n+1]==1):    
            costo=costo + 10
        if(p[n]==1 and p[n+1]==3)or(p[n]==3 and p[n+1]==1):    
            costo=costo + 55
        if(p[n]==1 and p[n+1]==4)or(p[n]==4 and p[n+1]==1):    
            costo=costo + 25
        if(p[n]==1 and p[n+1]==5)or(p[n]==5 and p[n+1]==1):    
            costo=costo + 45
        if(p[n]==2 and p[n+1]==3)or(p[n]==3 and p[n+1]==2):    
            costo=costo + 20
        if(p[n]==2 and p[n+1]==4)or(p[n]==4 and p[n+1]==2):    
            costo=costo + 25
        if(p[n]==2 and p[n+1]==5)or(p[n]==5 and p[n+1]==2):    
            costo=costo + 40
        if(p[n]==3 and p[n+1]==4)or(p[n]==4 and p[n+1]==3):    
            costo=costo + 15
        if(p[n]==3 and p[n+1]==5)or(p[n]==5 and p[n+1]==3):    
            costo=costo + 30
        if(p[n]==4 and p[n+1]==5)or(p[n]==5 and p[n+1]==4):    
            costo=costo + 50
        
    totalRutas.append([p,costo])        
    
print("\n\t====RUTAS EXISTENTES EN EL UNIVERSO ====")    
print(totalRutas,len(totalRutas))
print("\n\t====CANTIDAD TOTAL DE RUTAS ====")
print(len(totalRutas))



print("\n\t")

totalRutas2=[]
tipos= itertools.permutations('12345',5)
for i in tipos:
    print(i)
    totalRutas2.append(i)


print("\n\t====BUSCAR POSIBLES RUTAS====")
inicio = input("Rutaaaaa Inicial: ")
final = input("Rutaaaaa final: ")
i= 0
casillas = []



while i < 120:
    x = (totalRutas2[i].index(inicio))
    y = (totalRutas2[i].index(final))
    i= i+1
    if(x==0 and y==4 or x==4 and y==0):
        casillas.append(i-1)


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
    rutValidas.append(totalRutas[z])
    
print(rutValidas)

costos = []
minimo = costo
for i in range(1,len(costo)):
    if costo[i] < minimo:
        minimo = costo[i]
print("\nEl costo Minimo es: ",minimo)
        


mayor = rutValidas[0]
for i in range(1,len(rutValidas)):
    if rutValidas[i] > mayor:
        mayor = rutValidas[i]

print("\nEl costo Maximo es:",mayor)



