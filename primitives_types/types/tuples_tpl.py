tupla = ('ola',)
tupla2 = tuple()
print(tupla2)

print(type(tupla), type(tupla2))

tupla = ('rodrigo', 'ed', 1, 2, 3, 3, 3, 3, 3)
print(tupla)
print(tupla[1])

print(tupla.count(3))
print(tupla.index('rodrigo'))
print(tupla.__add__(('edson', 1)))
