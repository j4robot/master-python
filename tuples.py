tup = 12345, 54321, 'hello!', 'hello!'
print(tup)
print(list(tup))

#sequence unpacking
a, b, c, d = tup
print(a)
print(b)
print(c)

st = set(tup)
print(st)
print(list(st))

a = set('abracadabra')
print(a)