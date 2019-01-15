def GetDigit(c):
    return int(c) if c.isnumeric() else -1

def GetSymbol(d):
    return str(d)

def AddColumn(S, S1, S2):
    for i in reversed(range(len(S1))):
        r = GetDigit(S1[i]) + GetDigit(S2[i]) + GetDigit(S[i])
        S[i+1] = GetSymbol(r % 10)
        if r > 9:
            S[i] = "1"


def Add(a, b):
    if len(a) > len(b):
        b = ('0' * (len(a) - len(b))) + b
    else:
        a = ('0' * (len(b) - len(a))) + a
    result = ['0'] * (len(a) + 1)
    AddColumn(result, a, b)
    if result[0] == '0':
        result.remove('0')
    return ''.join(result)

a = input('Введіть a: ')
b = input('Введіть b: ')

c = Add(a, b)
print(" %s\n+ \n %s\n = %s" % (a, b, Add(a,b)))
