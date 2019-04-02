%module inputModule
%{  
    #include "q.hpp"
%}

%include stdint.i
%include std_string.i
%include std_queue.i
%include std_vector.i

// For passing variables by reference
%apply std::string& INOUT {std::string& seq};
// %apply std::vector<int>& INOUT {std::vector<int>& params};
// %apply std::queue<std::string>& INOUT { std::queue<std::string>& kmers};

%template(strQueue) std::queue<std::string>;
%template(IntVector) std::vector<int>;

%include "q.hpp"