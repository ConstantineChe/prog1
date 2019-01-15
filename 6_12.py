bills = [1, 2, 5, 10, 20, 50, 100]

wallet = {}

for v in bills:
    n = int(input("Введіть кількість банкнот номіналом %d \n" % v))
    if n > 0:
        wallet[v] = n

total = 0

for bill, n in wallet.items():
    total += bill * n

print("Гаманець: ", wallet)
print("Сума: %d" % total)
