# ( expressão for item in list if condicional )

generator = (i ** 2 for i in range(10) if i % 2 == 0)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) Error: StopIteration