def solution(n):
    nlist = list(map(int, str(n)))
    nlist.sort(reverse=True)
    num = "".join((map(str, nlist)))
    return int(num)