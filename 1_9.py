import math
from triangle import is_valid_triangle, semiperimeter
from math_util import is_positive_real


while True:
    try:
        a = float(input('Введіть довжину сторони A:'))
        b = float(input('Введіть довжину сторони B:'))
        c = float(input('Введіть довжину сторони C:'))

        if not all(map(is_positive_real, [a, b, c])):
            print("Довжина повинна бути дійсним числом більше нуля")
        elif not is_valid_triangle(a, b, c):
            print('задані сторони не утворюють трикутник')
        else:
            break

    except ValueError:
        print("Довжина повинна бути дійсним числом більше нуля")

p = semiperimeter(a, b, c)
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Площа трикутника: %f" % area)
