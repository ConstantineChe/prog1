n = int(input("Введіть порядок матриці n="))

A = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input("Введіть {}{} елемент матріці".format(i + 1,j + 1))))
    A.append(row)

m = int(input("Введіть розмірніість вектора m="))

v = []

for i in range(m):
    v.append(float(input("Введіть {} елемент вектору".format(i+1))))

for i in range(n):
    for j in range(n):
        if A[i][j] in v:
            A[i][j] = 0


for row in A:
    print(row)
