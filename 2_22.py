import math
from math_util import positive_real

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

while True:
    try:
        x1 = float(input('Введіть х нижньої лівої вершини першого прямокутника: '))
        y1 = float(input('Введіть y нижньої лівої вершини першого прямокутника: '))
        w1 = float(input('Введіть ширину першого прямокутника: '))
        h1 = float(input('Введіть висоту першого прямокутника: '))

        x2 = float(input('Введіть х нижньої лівої вершини другого прямокутника: '))
        y2 = float(input('Введіть y нижньої лівої вершини другого прямокутника: '))
        w2 = float(input('Введіть ширину другого прямокутника: '))
        h2 = float(input('Введіть висоту другого прямокутника: '))

        if not any(map(positive_real, [h1, h2, w1, w2])):
            print("Всі довжини повинні бути дійсними числами більше нуля")
        break
    except ValueError:
        print("Кожна довжина або компонента координати має бути дійсним числом")


bottom_left1 = Point(x1, y1)
bottom_left2 = Point(x2, y2)

top_right1 = Point(x1 + w1, y1 + h1)
top_right2 = Point(x2 + w2, y2 + h2)

bottom_left = Point(min(bottom_left1.x, bottom_left2.x), min(bottom_left1.y, bottom_left2.y))
top_right = Point(max(top_right1.x, top_right2.x), max(top_right1.y, top_right2.y))

print("Координати лівого нижнього кута: %s" % bottom_left.to_string())
print("Координати правого верхнього кута: %s" % top_right.to_string())
