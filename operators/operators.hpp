#include <iostream>

class Operators
{
private:
   int x = 10;
public:
    int y = 5;
    Operators(int n): x(n) {};
    void printrt() const;
    void operator ++();
    Operators operator =(const Operators &c) const;
    Operators operator +(const Operators &c) const;
    void next();
};
