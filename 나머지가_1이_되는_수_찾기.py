def solution(n):
    answer = 0
    mylist = []
    for i in range(1, n+1):
        if n % i == 1:
            mylist.append(i)
            answer = mylist[0]
    return answer