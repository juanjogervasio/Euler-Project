
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Digitos(numero):
    i=0
    while i>=0 :
        if numero//10==0 :
            i+=1
            break
        else :
            temp = numero//10
            numero = temp
            i+=1
            continue
    return i

j=2
fibo1 = 1
fibo2 = 1
while j>0 :
    fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo
    j+=1
    print(j, "     ", fibo)
    
    if Digitos(fibo)==1000:
        break
print("\n")    
print(fibo, " tiene " , Digitos(fibo), " digitos. \n")
print(" Es el termino numero ", j, " de la sucesion.\n")            