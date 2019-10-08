# [ expressão for item in list if condicional ]

dobros_pares = [i * 2 for i in range(10) if i % 2 == 0 ]
print(dobros_pares)

# [ versão normal ]
dobros_pares2 = []
for i in range(10):
    if i % 2 == 0:
        dobros_pares2.append(i * 2)
print(dobros_pares2)