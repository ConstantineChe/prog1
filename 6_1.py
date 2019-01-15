n = int(input("Введіть кількість членів послідовності 1"))


seq1 = []

for i in range(n):
    seq1.append(float(input("Введіть {} член послідовності".format(i+1))))

print(seq1)

m = int(input("Введіть кількість членів послідовності 2"))

seq2 = []
for i in range(m):
    seq2.append(float(input("Введіть {} член послідовності".format(i+1))))

print(seq2)

common = list(set(seq1).intersection(set(seq2)))
common.sort()

print("Спільні члени у порядку зростання: ", common)
