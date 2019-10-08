def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma


if __name__ == "__main__":
    print(soma_2(2, 3))
    print(soma_3(2, 3, 4))
    print(soma_n(2, 2, 2, 2, 2))

    print('===packing===')
    print(soma_n(1))
    print(soma_n(1, 1, 1))
    print(soma_n(1, 1, 1, 1))

    print('===unpacking===')
    tupla_nums = (1,2,3)
    print(soma_n(*tupla_nums))
    list_nums = [1,2,3]
    print(soma_n(*list_nums))
