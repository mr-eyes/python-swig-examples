%module callback
%{
#include "callback.hpp"
%}
using namespace std;

%import stdint.i 

uint64_t callback(uint64_t);
void tr_str(uint64_t x, uint64_t fn(uint64_t));

void printtt();