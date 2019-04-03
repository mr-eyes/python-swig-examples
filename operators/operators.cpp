#include "operators.hpp"

void printtest()
{
    std::cout << "Hello World" << std::endl;
}
int main()

{

    std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;

    std::cout<<"\n\nHello World,\nWelcome to my first C ++ program on Ubuntu Linux\n\n"<<std::endl;

}


void Operators::printrt() const
{
    std::cout << "x = " << x << ", y = " << y << std::endl;
}
void Operators:: operator ++()
{
    x++;
    y++;
}
void Operators::next() 
{
    this->operator++();
}
Operators Operators::operator =(const Operators &c) const
{
    return *this;
}
Operators Operators::operator +(const Operators &c) const
{
    Operators m_turn = Operators(x + c.x);
    m_turn.y += c.y;
    return m_turn;
}