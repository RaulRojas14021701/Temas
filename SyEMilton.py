# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:35:02 2023

@author: danie
"""

#Serpientes y escaleras original (Milton Bradley)

#Importar todo
import numpy as np
import random
import matplotlib.pyplot as plt

#La tirada de un dado o un dial
def dado():
    lanza=random.randint(1, 6)
    return lanza

def juego():
    casilla=0 #Inicia en la casilla cero
    contador=0 #Contaremos la tiradas que tardamos en acabar el juego
    while casilla<100:#El juego se acaba cuando lleguemos a la casilla 100
        avanza=dado()
        casilla+=avanza
        contador+=1
        #Las serpientes y escaleras son los if's}
        if casilla==1:
            casilla=38
        if casilla==4:
            casilla=14
        if casilla==9:
            casilla=31
        if casilla==21:
            casilla=42
        if casilla==28:
            casilla=84
        if casilla==36:
            casilla=44
        if casilla==51:
            casilla=67
        if casilla==71:
            casilla=91
        if casilla==80:
            casilla=100 #Son 9 escaleras
        if casilla==98:
            casilla=78
        if casilla==95:
            casilla=75
        if casilla==93:
            casilla=73
        if casilla==87:
            casilla=24
        if casilla==64:
            casilla=60
        if casilla==62:
            casilla=19
        if casilla==56:
            casilla=53
        if casilla==49:
            casilla=11
        if casilla==47:
            casilla=26
        if casilla==16:
            casilla=6 #Son 10 toboganes
    return contador
    
#Promediamos los lanzamientos que se hicieron
def promedia(n):
    prom=[]
    tiros=0
    for i in range(n):
        tiros+=juego()
        prom.append(tiros/(i+1))
    return prom

#Las veces que realizamos el experimento
X=promedia(500)

plt.plot(X)  
#Vemos la media
print(np.mean(X), np.std(X))

#Modelamos para repetir el experimento n veces mas
def modelo(n):
    lista=[]
    for i in range(n):
        s = promedia(500)
        lista.append(np.mean(s))
    return lista
#Realizamos varias veces el modelo
Y=modelo(120)
plt.hist(Y)
plt.show()

print(np.mean(Y), np.std(Y))
        