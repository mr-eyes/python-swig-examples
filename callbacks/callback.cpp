#include "callback.hpp"

int callback(int x){
    return x * x;
}

void tr_str(int x, int (*fn)(int)){
    std::cout << "tr_STR" << std::endl;
    std::cout << fn(x) << std::endl;
}

int main()

{

    std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;

    tr_str(10 , [](int x){
        return x;
    });

    tr_str(100, callback);

    std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;

}


