from math import sqrt
import itertools


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень
    """
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return

    root = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


print(message)
calc(25.5)