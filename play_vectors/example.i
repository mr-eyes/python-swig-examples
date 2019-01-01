%module example


%include "std_vector.i"

using namespace std;

%template(vectorInt) vector<int>;
