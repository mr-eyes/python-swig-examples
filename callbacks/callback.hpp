#include <iostream>

class Callback;

void tr_str(int x, Callback *obj);

void printtest();

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

class Callback{
    public:
        virtual int run(int x){return 0;}
        void callback(int x){
            tr_str(x, this);
            delete this;
        }
};