#include "example.hpp"
#include <vector>
#include <iostream>

using namespace std;


vector<int>* r_v(){

    int arr[] = { 10, 20, 30 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
  
    vector<int>* vect = new vector<int> (arr, arr + n);

    return vect;
    
}


void print_v(vector<int>* v){
    
    for(int i=0; i < v->size(); i++){
        std::cout << v->at(i) << endl;
    }

}

// int main(){
    
    
    
// }