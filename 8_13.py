def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return (1 / power(x, abs(n)))
    else:
        return x * power(x, n - 1)

while True:
    try:
        x = float(input("Введіть основу: "))
        n = int(input("Введіть ступінь: "))
        break
    except ValueError:
        print("Основа має бути дійсним числом, а ступінь - цілим.")

print("%f^%f = %f" % (x, n, power(x, n)))
