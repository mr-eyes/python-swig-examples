%module example
%{  
    #include "example.hpp"
%}


%include std_vector.i

%import stdint.i            /*This mainly used for converting python int to C++ uint64_t*/
%include std_string.i       /*And this for converting python str to C++ std::string*/
using std::string;
using namespace std;
/*START The following is to convert std::vector to python list*/


%template(IntVector) vector<int>;

/*END*/

%include "example.hpp"

