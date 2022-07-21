// Primer numero de Fibonacci con 1000 digitos - Problema 25

#include <iostream>

int main(){
    using namespace std;
    
    long N=1;
    int i=1;
    
    while (i<20){
    
        for (int j=1; j<=20; j++){
            if (N%j==0){
            continue;
            }
            else {
                N++;
                i++;
                j=1;
            }
        }
    }
    cout << " El numero es " << N << endl;
    return 0;
}
