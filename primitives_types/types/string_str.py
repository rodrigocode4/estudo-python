#print(dir(str))

name = 'Rodrigo-Oliveria'
print(name[0])
print(name[-3])
print(name[:7])
print(name[8:])
print(name[-3:])
print(name[:-3])
print(name[6:9])

numbers = '1234567890'
print(numbers[::])
print(numbers[::2])
print(numbers[::3])
print(numbers[1::2])
print(numbers[0::2])
print(numbers[::-1]) # reverse string

print('Felipe D\'Avila' == "Felipe D'Avila")

print('Com aspars duplas (") envolto de aspas simples')
print("Com aspas simples (') envolto de aspas duplas")

text = """  Este 
texto
    possui """ + ''' multiplas
linhas !!!'''
print(text)

frase = 'Python é uma linguagem lindamente fácil'

print('lindamente' in frase)
print('py' in frase.lower())
print(frase.upper())
print(frase.split(' '))
print(len(frase))
print(str.__len__(frase))

nome, idade, altura = 'Rodrigo', 23, 1.7423

print('Nome: %s, Idade: %d, Altura: %.2f' % (nome, idade, altura))
print('Nome: {0}, Idade: {1}, Altura: {2}'.format(nome, idade, format(altura, '.2f')))
print(f'Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}')