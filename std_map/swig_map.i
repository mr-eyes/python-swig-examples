%module swigMap
%{  
    #include "stdMap.hpp"
%}

%include stdint.i
%include std_map.i
%include std_string.i
%include std_vector.i

%template(intVec) std::vector<int>;
%template(Mapsi) std::map<std::string, std::vector<int>>;

class testMap
{
  public:
    testMap(){};
    std::map<std::string, std::vector<int>> returnMap();
};
