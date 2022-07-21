#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:07:54 2022

@author: mint
"""

"""
Problema 17 - Euler Project
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

# Una funcion que transforma un numero entero en texto
def Lector(number) :
    lectura=[]
    dict1 = {'1': 'one' ,
             '2': 'two' ,
             '3': 'three' ,
             '4': 'four' ,
             '5': 'five' ,
             '6': 'six' ,
             '7': 'seven' ,
             '8': 'eight' ,
             '9': 'nine' ,
             '10': 'ten' ,
             '11': 'eleven' ,
             '12': 'twelve' ,
             '13': 'thirteen' ,
             '14': 'fourteen' ,
             '15': 'fifteen' ,
             '16': 'sixteen' ,
             '17': 'seventeen' ,
             '18': 'eighteen' ,
             '19': 'nineteen'
             }
    
    dict2 = {
         '2': 'twenty' ,
         '3': 'thirty' ,
         '4': 'forty' ,
         '5': 'fifty' ,
         '6': 'sixty' ,
         '7': 'seventy' ,
         '8': 'eighty' ,
         '9': 'ninety' ,
         }
    
    N=str(number)
    if type(number)!= int or number<0:
        print("For natural numbers only")
        return
    
    n=dict1.get(N, 0)
    if n==0:
        for i in range(1,len(N)+1):
            temp=N[len(N)-i]
            if temp == '0':
                continue
        
            if i==1 and N[len(N)-2]!='1':
                lectura.append(dict1[temp])
            elif i==2:
                try:
                    lectura.append(dict2[temp])
                except:
                    lectura.append(dict1[N[len(N)-2:]])
            elif i==3 and N[len(N)-2:]=='00':
                    lectura.append(dict1[temp] + ' hundred')
            elif i==3 and N[len(N)-2:]!='00':
                    lectura.append(dict1[temp] + ' hundred and ')
            elif i==4:
                lectura.append(dict1[temp] + ' thousand ')
            elif i==5:
                print("Only for numbers less than 9999")
                return
    else:
        lectura.append(n)

    salida=''
    for i in range(1, len(lectura)+1):
        salida=salida + lectura[len(lectura)-i]
    
    if salida=="":
        salida='zero'
    
    return salida

# Una funcion que cuenta la cantidad de letras en la palabra, sin espacios
def Contador(word):
    i=0
    try:
        temp=word.replace(' ','')
        i=len(temp)
    except:
        print("Error found")
    return i


# Ahora si, el programa que suma las letras usadas en los numeros
try:
    n=int(input("Ingrese el numero maximo : "))
    if n>9999:
        raise TypeError()
    elif n<0:
        raise TypeError()
    
    contador=0
    for i in range(1,n+1):
        temp = Contador(Lector(i))
        contador += temp

    print("La suma de las letras usadas para escribir los numeros del 1 al " + str(n) 
    +" es" , contador)
    
except TypeError:
    print("Solo enteros positivos menores a 9999")
    
except:
    print("Un numero entero, joder!")