print(type(4))

print(int.__add__(1,2))
print(1 + 2)

print(dir(int))

print((-2).__abs__())

from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(3))

getcontext().prec = 3
print(Decimal(1) / Decimal(3))