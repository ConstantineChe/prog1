def b(k):
    if k < 3:
        return 1
    else:
        return b(k - 1) + a(k - 1)

def a(k):
    if k == 1:
        return 0
    elif k == 2:
        return 1
    else:
        return (a(k - 1) / k) + a(k - 2) * b(k)

def sum(n):
    return ((2 ** n) / (a(n) + b(n)))

while True:
    n = input('Введіть натуральне n: ')
    try:
        n = int(n)
        if is_natural_number(float(n)):
            break
        else: raise ValueError
    except ValueError:
        print("%s не є натуральним числом" % n)

S = sum(n)

print("S = %f" % S)
