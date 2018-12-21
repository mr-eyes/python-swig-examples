import ctypes

class argv:
    def __init__(self):
        self.argv = ctypes.cdll.LoadLibrary('./_argv.so')

    def call_main(self, py_list):
        LP_c_char = ctypes.POINTER(ctypes.c_char) # equivalent to char **argv
        #LP_LP_c_char = ctypes.POINTER(LP_c_char)
        argc = len(py_list)
        _argv = (LP_c_char * (argc + 1))()
        
        for i, arg in enumerate(py_list):
            enc_arg = arg.encode('utf-8')
            _argv[i] = ctypes.create_string_buffer(enc_arg)
        
        self.argv.main(argc, _argv)