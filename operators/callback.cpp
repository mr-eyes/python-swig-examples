#include "callback.hpp"

int callback(int x){
    return x * x;
}

void tr_str(int x, Callback *obj){
    std::cout << "tr_STR" << std::endl;
    std::cout << obj->run(x) << std::endl;
}

void printtest()
{
    std::cout << "Hello World" << std::endl;
}
// int main()

// {

//     std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;

//     tr_str(10 , [](int x){
//         return x;
//     });

//     tr_str(100, callback);

//     std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;

// }


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
callbackc callbackc::operator =(const callbackc &c) const
{
    return *this;
}
callbackc callbackc::operator +(const callbackc &c) const
{
    callbackc m_turn = callbackc(x + c.x);
    m_turn.y += c.y;
    return m_turn;
}