import math
from math_util import is_positive_real


while True:
    try:
        r = float(input('Введіть радіус основи циліндра:'))
        h = float(input('Введіть висоту циліндра: '))
        if not all(map(is_positive_real, [h, r])):
            print("Довжина повинна бути дійсним числом більше нуля")
        else:
            break

    except ValueError:
        print("Довжина повинна бути дійсним числом більше нуля")

v = math.pi * (r ** 2) * h / 3

print("Об'єм конуса: %f" % v)
