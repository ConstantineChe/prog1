from math_util import is_natural_number

while True:
    n = input('Введіть натуральне число: ')
    try:
        i = int(n)
        if is_natural_number(float(n)):
            break
        else: raise ValueError
    except ValueError:
        print("%s не є натуральним числом" % n)

if n == n[::-1]:
    print("%s - паліндром." % n)
else:
    print("%s - не паліндром." % n)
