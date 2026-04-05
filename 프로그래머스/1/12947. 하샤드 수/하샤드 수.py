def solution(x):
    arr = []
    for i in str(x):
        arr.append(int(i)%10)
    return x % sum(arr) == 0