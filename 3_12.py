n = int(input('Введіть кількітсть членів послідовності: '))

xs = []

def idx(xs, x):
    try:
        return xs.index(x) + 1
    except ValueError:
        return 0

while n > 0:
    xs.append(float(input("Введіть %i член послідовності: " % (len(xs) + 1))))
    n = n - 1


print("Максимальний член послідовності: %f" % (max(xs)))
