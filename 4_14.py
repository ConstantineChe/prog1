from operator import add

class Polynomial:

    def __init__(self, coefs):
        self.coefs = coefs
        self.degree = len(coefs)

    def __add__(self, other):
        if self.degree > other.degree:
            coefs1 = self.coefs
            coefs2 = ([0] * (self.degree - other.degree)) + other.coefs
        else:
            coefs1 = other.coefs
            coefs2 = ([0] * (other.degree - self.degree)) + self.coefs
        return Polynomial(list(map(add, coefs1, coefs2)))


    def __mul__(self, other):
        result_coefs = [0] * (self.degree + other.degree - 1)
        for i, c1 in enumerate(self.coefs):
            for j, c2 in enumerate(other.coefs):
                result_coefs[i + j] += c1 * c2
        return Polynomial(result_coefs)



    def __str__(self):
        p = []
        n = len(self.coefs) - 1
        for coef in self.coefs:
            if coef == 0:
                pass
            elif n == 0:
                p.append(str(coef))
            elif n == 1:
                p.append("{}*x".format(coef))
            else:
                p.append("{}*x^{}".format(coef, n))
            n -= 1
        return " + ".join(p)



coefs1 = []
coefs2 = []
n = 1
for l in [coefs1, coefs2]:
    N = int(input("Введіть ступіть многочлена %d:  " % n))

    for i in range(1, N + 2)[::-1]:
        x = float(input("Задайте коефіцієнт x^%d: " % (i - 1)))
        l.append(x)
    n += 1

p1 = Polynomial(coefs1)
p2 = Polynomial(coefs2)

print("Перший многочлен: %s" % p1.__str__())
print("Другий многочлен: %s" % p2.__str__())
print("Сума цих многочленів: %s" % (p1 + p2).__str__())
print("Добуток цих многочленів: %s" % (p1 * p2).__str__())
