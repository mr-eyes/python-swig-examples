#include "callback.hpp"

int callback(int x){
    return x * x;
}

void tr_str(int x, int (*fn)(int)){
    std::cout << fn(x) << std::endl;
}

int printtest()

{

    std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;
    tr_str(10, [](int x){
        return x;
    });

    tr_str(100, callback);
    return 0;

}


callbackc::callbackc(int n)
{
    x = n;
}

callbackc::~callbackc()
{
}

void callbackc::printrt() const
{
    std::cout << x << " ... y " << y << std::endl;
}
void callbackc:: operator ++()
{
    x++;
    y++;
}
void callbackc::next() 
{
    this->operator++();
}