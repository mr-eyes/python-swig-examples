%module example
%include std_vector.i
using namespace std;
%template(vectorInt) std::vector<int>;