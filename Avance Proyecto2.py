# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:23:31 2021

@author: iramv
"""
import itertools
def grafo1(inicio,final):
    ciudades=[1,2,3,4,5]
    rutas= itertools.combinations(ciudades,2)
    print(rutas)
    rutas= itertools.permutations(ciudades,5)
    totalRutas=[]
    
    for p in rutas:
        i=0
        costo=0
        print(p)
        x =p.index(inicio)
        y =p.index(final)
        if(x==0 and y==4):
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
            totalRutas.append([costo,p])
        i=i+1   
    totalRutas.reverse()
    totalRutas.sort()
    
    print(f"\n\t====RUTAS QUE VAN DESDE EL PUNTO {inicio} AL PUNTO {final} ====")    
    print(totalRutas,len(totalRutas))
    print("\n\t====CANTIDAD TOTAL DE RUTAS ====")
    print(len(totalRutas))
    
    costomin=totalRutas[0][0]
    print("La ruta con el costo minimo es: ",costomin)
    costomax=totalRutas[len(totalRutas)-1][0]
    print("La ruta con mayor costo es: ",costomax)
    

    
def grafo2(inicio,final):
    ciudades=[1,2,3,4,5]
    rutas= itertools.combinations(ciudades,2)
    print(rutas)
    rutas= itertools.permutations(ciudades,5)
    totalRutas=[]
    
    for p in rutas:
        i=0
        costo=0
        print(p)
        x =p.index(inicio)
        y =p.index(final)
        if(x==0 and y==4):
            for n in range(len(p)-1):
                
                if(p[n]==1 and p[n+1]==2)or(p[n]==2 and p[n+1]==1):    
                    costo=costo + 10
                if(p[n]==1 and p[n+1]==4)or(p[n]==4 and p[n+1]==1):    
                    costo=costo + 25
                if(p[n]==1 and p[n+1]==5)or(p[n]==5 and p[n+1]==1):    
                    costo=costo + 45
                if(p[n]==2 and p[n+1]==3)or(p[n]==3 and p[n+1]==2):    
                    costo=costo + 20
                if(p[n]==2 and p[n+1]==4)or(p[n]==4 and p[n+1]==2):    
                    costo=costo + 25
                if(p[n]==3 and p[n+1]==4)or(p[n]==4 and p[n+1]==3):    
                    costo=costo + 15
                if(p[n]==4 and p[n+1]==5)or(p[n]==5 and p[n+1]==4):    
                    costo=costo + 50
            totalRutas.append([costo,p])
        i=i+1   
    totalRutas.reverse()
    totalRutas.sort()
    
    print(f"\n\t====RUTAS QUE VAN DESDE EL PUNTO {inicio} AL PUNTO {final} ====")    
    print(totalRutas,len(totalRutas))
    print("\n\t====CANTIDAD TOTAL DE RUTAS ====")
    print(len(totalRutas))
    
    costomin=totalRutas[0][0]
    print("La ruta con el costo minimo es: ",costomin)
    costomax=totalRutas[len(totalRutas)-1][0]
    print("La ruta con mayor costo es: ",costomax)

def desplegarMenu(texto,max):
    while (True):
        for elemento in texto:
            print (elemento)
        
        opcion = int(input())            
        if (opcion >0 and opcion <= max):
            return opcion


def main():
    textoMenu=("\n---GRAFOS---","1)Grafo 1","2)Grafo 2","3)Salir","\nSeleccione un a opcion:")
    opcion =1
    while (opcion != 3):
        opcion = desplegarMenu(textoMenu,len(textoMenu)-2)
        if(opcion==1):
            print("+++´GRAFO NÚMERO 1+++ ")
            print("\n\t====BUSCAR POSIBLES RUTAS====")
            inicio = int(input("Ruta Inicial: "))
            final = int(input("Ruta Final: "))
            grafo1(inicio,final)
        elif(opcion == 2):
            print("+++GRAFO NÚMERO 2+++")
            print("\n\t====BUSCAR POSIBLES RUTAS====")
            inicio = int(input("Ruta Inicial: "))
            final = int(input("Ruta Final: "))
            grafo2(inicio,final)
        
        
main()
