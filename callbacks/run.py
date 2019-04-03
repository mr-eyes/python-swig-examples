import callback as cb

class PyCallback(cb.Callback):

    def __init__(self):
        cb.Callback.__init__(self)

    def run(self, x):
        return x + 100

callback = PyCallback()
callback.callback(10)
del callback

cb.printtest()

# def ss(x):
#     return x

# cb.tr_str(1, ss)
ss = cb.callbackc(10)
ss.printrt()
ss.next()
ss.next()
ss.printrt()
