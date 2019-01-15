from math_util import is_natural_number

def memoize(f):
    m = {}
    def memoized(x):
        if x not in m:
            m[x] = f(x)
        return m[x]
    return memoized

@memoize
def P(k):
    if k < 4:
        return 1
    else:
        # В задачі формула не коректна.
        return P(k - 2) + P(k - 3)

while True:
    n = input('Введіть натуральне n: ')
    try:
        n = int(n)
        if is_natural_number(float(n)):
            break
        else: raise ValueError
    except ValueError:
        print("%s не є натуральним числом" % n)

print("A: %i = %i" % (P(n), P(n - 1) + P(n - 5)))
print("B: %i = %i" % (P(n), 2 * P(n - 2) - P(n - 7)))
print("C: %i = %i" % (P(n), P(n - 2) + P(n - 4) + P(n - 8)))
print("D: %i = %i" % (P(n), 4 * P(n - 5) + P(n - 14)))
