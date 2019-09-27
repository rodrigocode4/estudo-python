from random import randint

num_info = -1
num_secret = randint(0, 9)

while num_info != num_secret:
    num_info = int(input('Informe o número: '))

print(f'O número {num_secret} foi encontrado!')