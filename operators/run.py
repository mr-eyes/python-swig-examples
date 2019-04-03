import operators as ops

ss = ops.Operators(10)
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
kk = ops.Operators(5)
kk.printrt()
print 'll = kk + dd'
ll = kk + dd
ll.printrt()