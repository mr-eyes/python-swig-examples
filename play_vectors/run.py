import example

x = example.vectorInt()
x.push_back(1)
x.push_back(2)
x.push_back(3)

z = x.begin()
while(z != x.end()):
    print next(z)

