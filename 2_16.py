import math

def f(x):
    if x <= 0:
        return 0
    elif 0 < x < 1:
        return x
    elif 1 <= x <= 2:
        return 2 - x
    elif x > 2:
        return 0

def g(x):
    if x < -1:
        return 1
    elif x == - 1:
        return 2
    elif -1 < x < 0:
        return x + 1
    elif 0 <= x < 1:
        return -x + 1
    elif x == 1:
        return 2
    elif x > 1:
        return 1

while True:
    try:
        x = float(input("Введіть x:"))
        break
    except ValueError:
        print("Введіть дійсне число")

print("f(%f) = %f" % (x, f(x)))
print("g(%f) = %f" % (x, g(x)))
