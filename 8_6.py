def memoize(f):
    m = {}
    def memoized(*x):
        if x not in m:
            m[x] = f(*x)
        return m[x]
    return memoized

@memoize
def xn(x, n, k):
        if k == 0:
            return (x / n)
        else:
            return ((((n - 1) * xn(x, n, k - 1)) + (x / (xn(x, n, k - 1) ** (n - 1)))) / n)


def nthroot(x, n, epsilon):
    x1 = xn(x, n, 1)
    x2 = xn(x, n, 2)
    k = 2
    while abs(x1 - x2) > epsilon:
        k += 1
        x1 = x2
        x2 = xn(x, n, k)
    return x2


epsilon = 0.00001

def f(a):
    return (nthroot(a, 3, epsilon) - nthroot(((a ** 2) + 1), 6, epsilon)) / (1 + nthroot((3 + a), 7, epsilon))

def test(a):
    return (a**(1/3) - (a**2 + 1)**(1/6))/(1 + (3 + a)**(1/7))

while True:
    a = float(input('Введіть a>0: '))
    if a > 0:
        break

print("Значеня виразу: %f, test: %f" % (f(a), test(a)))
