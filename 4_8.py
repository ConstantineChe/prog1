l1 = []
l2 = []
n = 1
for l in [l1, l2]:
    N = int(input("Кількість елементів списку %d:  " % n))

    for i in range(N):
        x = float(input("Задайте %d-й елемент списку: " % (i)))
        l.append(x)
    print(l)
    n += 1

common = []

if len(l1) > len(l2):
    base = l2
    search = l1
else:
    base = l1
    search = l2

for item in base:
    if item in search:
        common.append(item)

print("Спільні елементи:", common)
