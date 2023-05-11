# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:00:11 2023

@author: danie

"""
#Importar todo
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm

casilla=0

    
#Lanza una moneda si cae 1 entonces avanzara 1, sino avanzara 2
def moneda():
    lanza=1
    x=random.random()
    if(x<=0.5):
        lanza=2
    return lanza

moneda()

#Juega las serpientes y escaleras y cuenta en cuantos turnos acaba
#print(casilla)

def juega():
    casilla=0 #en que casilla va
    contador=0 #cuanras veces tiro
    while casilla<9: #se detendra cuando valga 9
        avanza=moneda()
        casilla+=avanza
        contador+=1
        #Las serpientes y escaleras son los if's
        if casilla==2:
            casilla=7
        if casilla==3:
            casilla=5
        if casilla==8:
            casilla=4
        if casilla==6:
            casilla=1
    return contador
    
#Promedia el numero de tiros entre las veces que se jugo
def promedia(n):
    prom=[]
    tiros=0
    for i in range(n):
        tiros+=juega()
        prom.append(tiros/(i+1))
    return prom
#Cuantas veces repetimos los lanzamientos
X=promedia(300)

plt.plot(X)  
#Vemos la media
print(np.mean(X), np.std(X))
#Modelamos para repetir el experimento n veces mas
def modelo(n):
    lista=[]
    for i in range(n):
        s = promedia(300)
        lista.append(np.mean(s))
    return lista

Y=modelo(120)
plt.hist(Y)
plt.show()

print(np.mean(Y), np.std(Y))
        
print("Acabamos....")
    
    
