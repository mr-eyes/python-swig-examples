#include <iostream>
#include <string>
#include "example.hpp"


using namespace std;


void fact(uint64_t x){
    cout << "it Worked :"<< x << endl;
}

void tr_str(string x){
    cout << "Str: " << x << endl;
}

// int fact(int n){
//     if (n < 0){
//         return 0;
//     }
//     else if(n == 0){
//         return 1;
//     }
//     else if (n > 0){
//         return n * fact(n - 1);
//     }
// }