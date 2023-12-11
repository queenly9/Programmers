def solution(price, money, count):
    amount = 0
    all = 0
    for i in range(count+1):
        amount = price*i
        all += amount
    if all <= money:
        return 0
    answer = (all - money)
    return answer