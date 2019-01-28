import swigMap as sm

MAP = sm.testMap()
mp = MAP.returnMap()

it = mp.begin()
while(it != mp.end()):
    print it.next()
    

