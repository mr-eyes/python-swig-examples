#include <iostream>

int callback(int);

void tr_str(int x, int (*fn)(int));
int printtest();
class callbackc
{
private:
   int x = 10;
public:
    int y = 5;
    callbackc(int);
    ~callbackc();
    void printrt() const;
    void operator ++();
    void next();
};

