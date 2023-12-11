def solution(a, b):
    sum = 0
    for i in range(len(a)):
        mul = a[i]*b[i]
        sum += mul
    return sum