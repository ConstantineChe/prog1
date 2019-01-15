
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def findElement(mtx, trg):
    isFound = False
    for ridx, row in enumerate(mtx):
        for eidx, elm in enumerate(row):
            if elm == trg:
                isFound = True
                print(f'Found at [{ridx}][{eidx}]')
    if not isFound:
        print('Can not find element')

target = int(input('Enter number to find: '))

findElement(matrix, target)