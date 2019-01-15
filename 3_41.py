import math
from math_util import is_natural_number

while True:
    n = input('Введіть натуральне n: ')
    try:
        n = int(n)
        if is_natural_number(float(n)):
            break
        else: raise ValueError
    except ValueError:
        print("%s не є натуральним числом" % n)

s =  0

for i in range(n):
    x = i + 2
    s = s + ((-1) ** x) * (x - 1)/x


print("Сума послідовносі %i членів послідовносі дорівнює %f" % (n, s))
