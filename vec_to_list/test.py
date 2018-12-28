from bar import bar, foo

a = foo(1, 2, 3)
b = foo(2, 3, 4)

vecs = [a, b]

c = bar(vecs)

d = c.get_vectors()

for vec in d:
   print vec.mag()
