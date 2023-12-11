def solution(numbers):
    num = 0
    for i in range(1, 10):
        if i in numbers:
            pass
        elif i not in numbers:
            num += i
    return num