def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        div = 0
        for j in range(1, i+1):
            if i % j == 0:
                div += 1
        if div % 2 == 0:
            sum += i
        if div % 2 != 0:
            sum -= i
    return sum