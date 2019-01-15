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


def median(a, b, c):
    return math.sqrt((2 * (b ** 2)) + (2 * (c ** 2)) - (a ** 2))/2

def bisector(a, b, c):
    p = semiperimeter(a, b, c)
    return 2 * math.sqrt(a * b * p * (p - c) ) / (a + b)

def height(a, b, c):
    p = semiperimeter(a, b, c)
    return math.sqrt(p * (p - a) * (p - b) * (p - c) ) * 2 / a

vertices = {'A': (a, b, c),
            'B': (b, c, a),
            'C': (c, b, a)}

for vertex,sides in vertices.items():
    print("Медіана на сторону %s: %f" % (vertex, median(*sides)))
    print("Бісектриса на сторону %s: %f" % (vertex, bisector(*sides)))
    print("Висота на сторону %s: %f" % (vertex, height(*sides)))
