#include "callback.hpp"

uint64_t callback(uint64_t x){
    return x * x;
}

void tr_str(uint64_t x, uint64_t f(uint64_t)){
    std::cout << f(x) << std::endl;
}
int main()

{

    std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;
    tr_str(10, callback);
    return 0;

}