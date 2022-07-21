#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:48:02 2022

@author: mint
"""

"""
Problema 50 - Euler Project
The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime
below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

#Una funcion que determina si un numero es primo o no
def EsPrimo(number):
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
    #Miramos la lista de factores
    if len(factors)>1:
        return False
    else:
        return True

i=2
primos=[2]
N=int(input("Inserte maximo: "))
#Armo una lista de primos consecutivos que no sumen (mucho) mas de N
while i>0:
    i+=1
    if sum(primos)>N*2:
        break
    contador=0
    for j in primos:
        if i%j==0:
            break
        else:
            contador+=1
    if contador==len(primos):
        primos.append(i)

#Busco la mayor suma de primos consec. que sea primo
lista=[0]
j=0

while max(lista)<N:
    suma=0
    i=1
    while suma<N:
        suma=sum(primos[j:j+i])
        i+=1
        if EsPrimo(suma):
            lista.append(suma)
    j+=1

final=lista[:len(lista)-2]
print("El numero es:", max(final))