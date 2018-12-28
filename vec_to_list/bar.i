%module bar 
%{ 
#define SWIG_FILE_WITH_INIT 
#include "bar.h" 
#include "foo.h" 
%} 

%ignore bar::bar(); 
%ignore foo::foo(); 

%include "std_vector.i"; 
namespace std { 
    %template(vector_foo) vector<int>; 
} 

%include "bar.h"; 
%include "foo.h"; 
