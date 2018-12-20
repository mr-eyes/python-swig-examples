#include "example.hpp"


int fact(int n){
    if (n < 0){
        return 0;
    }
    else if(n == 0){
        return 1;
    }
    else if (n > 0){
        return n * fact(n - 1);
    }
}