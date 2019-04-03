import callback as cb

class PyCallback(cb.Callback):

    def __init__(self, x):
        cb.Callback.__init__(self)
        self.callback(x)
        del self
        
    def run(self, x):
        return x + 100

PyCallback(10)

cb.printtest()

# def ss(x):
#     return x

# cb.tr_str(1, ss)
ss = cb.callbackc(10)
print 'ss before increment'
ss.printrt()
ss.next()
ss.next()
print 'ss after 2 increment'
ss.printrt()
print 'dd = ss'
dd = ss
dd.printrt()
print 'kk ='
kk = cb.callbackc(5)
kk.printrt()
print 'll = kk + dd'
ll = kk + dd
ll.printrt()