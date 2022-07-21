#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:43:41 2022

@author: mint
"""

"""
Problema 62 - Euler Project
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import numpy as np
from sympy.utilities.iterables import multiset_permutations as perm

"""
ESTA VERSION ES MUY LENTA
#Una funcion que determina si un numero x es un cubo perfecto
def Cubo(x):
    n=len(str(x))
    for i in range(2**(n-1), 4**(n-1)+2):
        temp=i**3
        if temp==x:
            return True
    return False


for i in range(350,400):
    #Elevo el numero al cubo
    n=np.power(i,3)
    #Armo las permutaciones y cuento los cubos perfectos
    p=[]
    contador=0
    for number in perm(str(n)):
        temp=""
        for j in number:
            temp+=j
        permutation=int(temp)
        if Cubo(permutation):
            p.append([permutation,i])
            contador+=1
    if contador==5:
        break
    
print(p)
"""



"""
ESTO YA NI ME ACUERDO QUE HACIA
    if p==3:
        print("El cubo del numero " + str(i) +" tiene exactamente 3 perm. que "
              +"son cubos perfectos, y es el menor")
        break
        
        
        
        p.append(number)
    #Concateno cada numero de cada permutacion para volver a hacerlos int
    lista=[] #Esta va a ser la lista con las permutaciones
    for string in p:
        temp=""
        for j in string:
            temp+=j
        lista.append(int(temp))
    
    #Busco si los elementos de la lista son cubos perfectos y los guardo:
    cubes=[]
    for permutation in lista:
        if Cubo(permutation):
            cubes.append(permutation)
"""



"""
TAMBIEN ES MUY LENTO
#Una funcion que toma una lista de cifras como texto y construye el numero:
def Trad(lista):
    temp=''
    for i in lista:
        temp+=i
    return int(temp)


for i in range(200,1000):
    #Elevo el numero al cubo
    n=np.power(i,3)
    
    #Armo la lista de cubos perfectos, en el rango necesario:
    Max=Trad(max(perm(str(n))))
    Min=Trad(min(perm(str(n))))
    largo1=len(str(Max))
    largo2=len(str(Min))
    cubos=[k**3 for k in range(i, 4**(largo1-1)+2)]
    
    #Me fijo si las permutaciones estan en la lista:
    contador=0
    for j in perm(str(n)):
        if Trad(j) in cubos:
            contador+=1
            print(i, "   ", Trad(j), "   ", contador)
    if contador>=5:
        break
"""



"""
TODAVIA MAS LENTO Y CON PROBLEMAS
#Una funcion que toma una lista de cifras como texto y construye el numero:
def Trad(lista):
    temp=''
    for i in lista:
        temp+=i
    return int(temp)

#Una funcion que factoriza el numero
def Factors(number):
    I = 2
    factors=[]
    #Un loop que arma la factorizacion del numero
    while I>0:
        while number%I==0:
            C=number//I
            factors.append(I)
            if C==1:
                number=C
                break
            else:
                number=C
        if number==1:
            break
        else:
            I+=1
            continue
    return factors

#Si el numero es un cubo perfecto, cada factor distinto aparece 3n veces en la
#factorizacion.
#Una funcion que determina eso:
def EsCubo(number):
    factors=Factors(number)
    different=set(factors)
    for n in different:
        if factors.count(n)%3!=0:
            return False
    return True

#Empecemos a probar permutaciones de cubos:
for i in range(301,400):
    #Elevo el numero al cubo
    n=np.power(i,3)
    #Armo las permutaciones y cuento los cubos perfectos
    contador=0
    for j in perm(str(n)):
        number=Trad(j)
        if EsCubo(number):
            contador+=1
            print(i, "   ", number, "   ", contador)
    if contador>=3:
        break
"""



"""
ESTE ES MAS SIMPLE Y FUNCIONA MEJOR PERO NO ES SUFICIENTE
#Una funcion que toma una lista de cifras como texto y construye el numero:
def Trad(lista):
    temp=''
    for i in lista:
        temp+=i
    return int(temp)
    
def EsCubo1(number):
    n=number**(1/3)
    if (int(n)+1)**3==number:
        return True
    else:
        return False
    
cubos=[]
for i in range(1000,10000):
    #Elevo el numero al cubo
    n=np.power(i,3)
    if i in cubos:
        continue
    #Armo las permutaciones, cuento los cubos perfectos y guardo sus raices
    contador=1
    permutations=[i for i in perm(str(n)) if i[0]>=str(n)[0]]
    for j in permutations:
        number=Trad(j)
        if EsCubo1(number) and number>n:
            contador+=1
            print(i, "   ", number, "   ", contador)
            cubos.append(int(number**(1/3))+1)
    
    if contador>=5:
        break
"""

#Una funcion que determina si dos numeros son permutaciones entre si.
def PermCheck(number1, number2):
    N1=str(number1)
    N2=str(number2)
    temp=''
    
    if len(N1)!=len(N2):
        return False
    else:
        for i in range(len(N1)):
            temp+="@"
            if N1[i] in N2:
                N2=N2.replace(N1[i], '@',1)
    
    if temp==N2:
        return True
    else:
        return False

i=100
contador=1
cubos=[]

#Armo una lista de cubos y me fijo si encuentro permutaciones
while i>0:
    resultado=[]
    N=i**3
    cubos.append(N)
    for n in cubos:
        if PermCheck(N, n):
            resultado.append(n)
    #Freno cuando encuentro 5 permutaciones
    if len(resultado)==5:
        break
    i+=1
    
#FUNCIONAAAAA
