def fatorial(n: int) -> int:
    if n <= 0 or n == 1: 
        return 1
    return n * fatorial(n - 1)

if __name__ == '__main__':
    print(f'10! == {fatorial(10)}')
    print(fatorial(0))
    print(fatorial(-2))
    print(fatorial(2))
    print(fatorial(3))
from calendar import mdays, month_name