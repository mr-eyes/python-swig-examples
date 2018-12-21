%module argv

%{
/* Everything in this block will be copied in the wrapper file. We include the C header file necessary to compile the interface
*/
#include "include/main.hpp"
%}

%include "include/main.hpp"

/*This to select the function we want to wrap, we can use %include "include/main.hpp"*/

int main(int argc, char **argv);