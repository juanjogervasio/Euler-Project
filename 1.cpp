// Multiplos de 3 o 5 - Problema 1

#include <iostream>

int main(){
    using namespace std;
    
    int suma=0;
    
    for (int i=1; i<1000; i++){
        
        if (i%3==0 || i%5==0){
            suma = suma + i;
        };

    };
    
    cout << "La suma de los multiplos de 3 y 5 menores a 1000 es " << suma << endl;
    
    return 0;
};
