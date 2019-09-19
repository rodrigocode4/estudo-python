# AND
print('===============AND==================')
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True and True and False and True)

# OR
print('===============OR==================')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(False or False or True or False)

# XOR
print('===============XOR==================')
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Unário de negação (not)
print('================not=================')
print(not True)
print(not False)

# (False, True)[condition]
print('================ternary=================')
esta_chovendo = True
print('Hoje estou com as roupas ' + ('secas!', 'molhadas!')[esta_chovendo])
esta_chovendo = False
print('Hoje estou com as roupas ' + ('molhadas!' if esta_chovendo else 'secas!'))

print('================+++=================')
lista = [1, 2, 3, 'Amos', 'Harari']
print('Amos' in lista)
print(3 not in lista)

x = 3
y = 3

print(x is y)
print(y is not x)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)