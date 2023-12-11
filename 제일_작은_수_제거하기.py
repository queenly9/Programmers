def solution(arr):
    num = min(arr)
    arr.remove(num)
    if len(arr) == 0:
        return [-1]
    return arr