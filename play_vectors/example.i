%module example
%{  
    #include "example.hpp"
%}

%include "std_vector.i"

using namespace std;

%template(vectorInt) vector<int>;


%include "example.hpp"
