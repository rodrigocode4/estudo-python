a = {1, 2, 3}
print(type(a))

print(a)
name = set('roooooddrriiigo')
print(name)

print('r' in name, 2 not in name, 'g' not in name)

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))

print(c1.intersection(c2))

c1.update(c2)
print(c1)
print(c2)

print(c1 >= c2)
print(c2 <= c1)

print({1, 2, 3} - {2})

c1 - c2
print(c1)

c1 -= {2}
print(c1)