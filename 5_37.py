import re
import math

s = input("Введіть квадратне рівняння використовуючі символи x, +, -, *, = \n")

left, right = s.split('=')

coefs = [0, 0, 0]

terms_left = []
terms_right = []
term = ''

for ch in left:
    if ch not in "+-":
        term += ch
    else:
        terms_left.append(term)
        term = ch
terms_left.append(term)

term = ''
for ch in right:
    if ch not in "+-":
        term += ch
    else:
        terms_right.append(term)
        term = ch
terms_right.append(term)


for t in terms_left:
    match = re.sub(r'[^\d]', '', t)
    if match == '':
        coef = 1
    else:
        coef = float(match)
    if '-' in t:
        coef = (-1) * coef
    coefs[t.count('x')] += coef

for t in terms_right:
    match = re.sub(r'[^\d]', '', t)
    if match == '':
        coef = 1
    else:
        coef = float(match)
    if '-' not in t:
        coef = (-1) * coef
    coefs[t.count('x')] += coef



print(coefs)

c,b,a = coefs

D = (b ** 2) - (4 * a * c)

x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)

print("x1 = %f, x2 = %f" % (x1, x2))
