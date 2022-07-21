// Suma de pares de FIbonacci - Problema 2

#include <iostream>

int main(){
    using namespace std;
    
    int fibo1=0;
    int fibo2=1;
    int fiboN=0;
    int suma=0;
    
    while (fiboN<4000000) {
        fiboN = fibo1 + fibo2;
        fibo1 = fibo2;
        fibo2 = fiboN;
        
        if (fiboN<4000000 && fiboN%2==0) {
            suma = suma + fiboN;
        }

    }
    
    cout << "La suma de los numeros de Fibonacci pares menores a cuatro millones es " << suma << endl;
    return 0;
}
