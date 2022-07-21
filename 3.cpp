// Factor primo mas grande - Problema 3

#include <iostream>

long PrimoMax(long X);
int main(){
    using namespace std;
    long N = 600851475143;
    
    cout << "El factor primo mas grande de " << N << " es " << PrimoMax(N) << endl; 
    
    return 0;
}

long PrimoMax(long X) {
    
    long I=2;
    
    while (I>0){
        
        while (X%I==0){
            
            long c=X/I;
            
            if (c==1){
                X=c;               
                break;
            }
            else {
                X=c;
            }
        }
        
        if (X==1){
            return I;
            break;            
        }
        else {
            I+=1;
            continue;            
        }
    }
    return I;
}
