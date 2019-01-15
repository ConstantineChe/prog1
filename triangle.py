import math


def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c  > b) and (c + b > a)

def semiperimeter(a, b, c):
    return (a + b + c)/2
