%module(directors="1") callback
%{  
    #include "callback.hpp"
%}

%include stdint.i

/* turn on director wrapping Callback */
%feature("director") Callback;
%inline %{
    class Callback{
    public:
        enum fn {ADD, SUB, DIV};
        virtual int handle(int x) = 0;
        virtual ~Callback() {}
        static int add(int x){
            return x + 10;
        }
        static int sub(int x){
            return x - 10;
        }
        static int div(int x){
            return x / 10;
        }
    };
%}

%{
    static Callback *handler_ptr = NULL;
    static int handler_helper(int a) {
        // Make the call up to the target language when handler_ptr
        // is an instance of a target language director class
        return handler_ptr->handle(a);
    }

%}
%inline %{
    void tr_str_wrapper(int a, Callback *handler) {
        handler_ptr = handler;
        tr_str(a, &handler_helper);
        handler = NULL;
    }
    void tr_str_wrapper(int a, Callback::fn f) {
        printf("TEST");
        Callback *ptr = 0;
        switch(f){
            case Callback::fn::ADD:
                tr_str(a, Callback::add);
                break;
            case Callback::fn::SUB:
                tr_str(a, Callback::sub);
                break;
            case Callback::fn::DIV:
                tr_str(a, Callback::div);
                break;
            default:
                break;
        }
        
    }
%}
%include "callback.hpp"
