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

a = int(input('Введіть член послідовності номер якого ви хочете знайти: '))

print("Номер члена послідовносі %f - %i" % (a, idx(xs, a)))
