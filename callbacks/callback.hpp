#include <iostream>

void tr_str(int x, int (*fn)(int));

//  class Callback{
//     public:
//         virtual int handle(int x) = 0;
//         virtual ~Callback() {}
//         static const int add(int x) const{
//             return x + 10;
//         }
//         static const int sub(int x){
//             return x - 10;
//         }
//         static const int div(int x){
//             return x / 10;
//         }
//     };
