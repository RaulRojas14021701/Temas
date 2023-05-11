# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Generadores congrunciales
#semilla x>0
import random 
x=2
i=1
print("Visto en clase")
#formula x_i=(a*x_{i-1}+c)mod(m), 0<a<m, 0<c<m, 0<x_0<m
#Hecho en clase
while (i<11):
    x=(5*x+11)%7
    imp=x/7
    print(imp)
    i+=1

#Otros datos
y=1
j=1
print("Nuevos datos")
while (j<20):
    y=(5*y+1)%16
    imp2=y/16
    print(imp2)
    j+=1
    
    
    print("Metodo de las 12 uniformes")
    k=0
    u=[]
    datos=[]
    for k in range(12):
        u.append(random.random())
        print(u[k])
        
    suma=sum(u)
    datos.append(suma)
       # print(datos)
    