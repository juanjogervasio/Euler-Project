// Primer numero de Fibonacci con 1000 digitos - Problema 25

#include <iostream>

int Nro_Digitos(unsigned long X);
int main(){
    using namespace std;
    
    unsigned long fibo1=1;
    unsigned long fibo2=1;
    unsigned long fiboN=0;
    long i=2;
    
    while (i>0) {               // Este loop calcula los fibonacci y cuenta los pasos con i
        fiboN = fibo1 + fibo2;
        fibo1 = fibo2;
        fibo2 = fiboN;
        i++;
        cout << i << "   " << fiboN << endl; 
        
        if (Nro_Digitos(fiboN)==10) {        // Voy a usar una funcion que calcula la cantidad de digitos de un entero.
            break;                            // Freno el loop cuando encuentro el fibonacci con 10 digitos.
        }  
    }
    cout << "El numero " << fiboN << ", que es el termino " << i << " de Fibonacci, es el primero con " << Nro_Digitos(fiboN) << " digitos." << endl;
    return 0;
}

int Nro_Digitos(unsigned long X){
    
    int contador=0;
    long temp;
    
    while (contador >= 0){
        if (X/10==0){
            contador++;
            break;
        }
        else {
            temp=X/10;
            X=temp;
            contador++;
            continue;
        }
    }
    return contador;    
}
