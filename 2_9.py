import math

while True:
    try:
        x = float(input("Введіть координату x: "))
        y = float(input("Введіть координату y: "))
        break
    except ValueError:
        print("Вводіть тільки дійсні числа")

def distance_from_origin(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def is_in_area(x, y):
    if x > 0 and y > 0: return False
    if distance_from_origin(x, y) < 2: return False
    if abs(x) > 2 or abs(y) > 2: return False
    return True

if is_in_area(x, y):
    print("Точка (%f, %f) належить до заданої області" % (x, y))
else:
    print("Точка (%f, %f) не належить до заданої області" % (x, y))
