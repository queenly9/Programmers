def solution(x, n):
    answer = []
    num = x
    answer.append(x)
    for i in range(1, n):
        num += x
        answer.append(num)
    return answer