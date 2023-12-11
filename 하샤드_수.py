def solution(x):
    xlist = list(map(int, str(x)))
    if x % sum (xlist) == 0:
        answer = True
    else:
        answer = False
    return answer
