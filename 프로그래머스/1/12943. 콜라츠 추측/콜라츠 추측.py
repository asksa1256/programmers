def solution(num):
    if num == 1: return 0

    cnt = 0
    div = num
    
    while div > 1:
        if div % 2 == 0:
            div = div / 2
            cnt += 1
        else:
            div = div * 3 + 1
            cnt += 1
    
    if cnt > 500: 
        return -1
    else:
        return cnt
            