%module argv

%{
/* Everything in this block will be copied in the wrapper file. We include the C header file necessary to compile the interface
*/
int main(int argc, char **argv);
%}

%include "typemap.i"

int main(int argc, char **argv);
