%module(directors="1") callback
%{  
    #include "callback.hpp"
%}
%include stdint.i
/* turn on director wrapping Callback */
%feature("director") Callback;
%include "callback.hpp"
