import math

def solution(n):
    root = int(math.sqrt(n))
    if root * root == n:
        # root.is_integer() 사용 불가능. root에 사용된 int()에 is_integer()가 없음. => root * root == n으로 대체
        return (root+1) ** 2
    else:
        return -1