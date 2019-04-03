import callback as cb

# PyCallback class is defined and derived from C++ class BinaryOp
class PyCallback(cb.Callback):

    # Define Python class 'constructor'
    def __init__(self):
        # Call C++ base class constructor
        cb.Callback.__init__(self)

    # Override C++ method: virtual int handle(int a) = 0;
    def handle(self, a):
        # Return the product
        return a + 5

handler = PyCallback()

# Overriden function
cb.tr_str_wrapper(10, handler)

# Custom defined functions
handler.handle = lambda x: x * 5
cb.tr_str_wrapper(10, handler)

# Pre defined functions
cb.tr_str_wrapper(10, handler.ADD)