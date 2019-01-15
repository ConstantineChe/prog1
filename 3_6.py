from math_util import is_natural_number


def power(x, n):
    return x if n == 1 else power(x, n - 1) * x

while True:
    try:
        x = float(input("Введіть основу: "))
        n = int(input("Введіть ступінь: "))
        if is_natural_number(n):
            break
        else:
            print("Ступінь має бути натуральним числом.")
    except ValueError:
        print("Основа має бути дійсним числом, а ступінь - натуральним.")

print("%f^%f = %f" % (x, n, power(x, n)))
