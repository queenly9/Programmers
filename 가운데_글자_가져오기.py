def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        snum = (len(s)//2)-1
        inum = snum+2
        answer = s[snum:inum]
    elif len(s) % 2 != 0:
        onum = (len(s)-(len(s)//2))-1
        answer = s[onum]
    return answer