def solution(n):
    answer = 0
    for i in range(0, n):
        if i*i == n:
            answer = (i+1)**2
            break
        elif i**2 > n:
            answer = -1
            break
        elif n == 1:
            answer = 4
    return answer
