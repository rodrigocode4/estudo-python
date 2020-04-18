print('Olá')
name = 'rodrigo'
print(name)

def get_fullname(f_name: str = '', l_name: str = '') -> str:
    return f'{f_name} {l_name}'

print(get_fullname('Rodrigo', 'Oliveira'))
print(get_fullname())

def sum(x: int, y: int) -> int:
    return x + y

def sum2(x, y):
    return x + y

print(sum(2,3))
print(sum2(2, 3))