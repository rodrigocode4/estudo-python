lista = []
print(type(lista), lista)
print(type(list()), list())

lista.append(1)
lista.append(23)
print(lista)

lista.append('Rodrigo')
lista.append([3, 4])
print(lista)

lista.insert(2, True)
print(lista)

lista.remove(23)
print(lista)

lista.reverse()
print(lista)

list_names = ['Ana', 'Paulo', 'Lia', 'Rui', 'Maria']
print(list_names[:2])
print(list_names[1:4])
del list_names[1]
print(list_names)

for names in range(2,len(list_names)):
    print(names)