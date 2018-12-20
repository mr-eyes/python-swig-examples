#include <iostream>
#include "include/main.hpp"

using namespace std;

int main(int argc, char **argv){

    cerr << argc - 1 << endl;
    for (int i = 1; i < argc; ++i)
    {
        cout << argv[i] << ", ";
    }
    cerr << endl;
}