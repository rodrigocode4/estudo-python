person = {
    'nome': 'Rodrigo',
    'idade': 23,
    'cursos': ['JS', 'Python']
}
print(type(person))
print(person.__len__())
print(person['cursos'])
print(person.keys())
print(person.values())
print(person.items())
#print(dir(dict))

person['idade'] = 24
print(person)

person['cursos'].append('Typescript')
print(person)
print(person.get('cursos')[1])

person.pop('nome')
print(person)

person.update({'first_name': 'Rodrigo', 'last_name': 'Olivaira'})
print(person)

print(person.get('aa'))

print(person)

print(person.setdefault('first_name', 'Edson'))