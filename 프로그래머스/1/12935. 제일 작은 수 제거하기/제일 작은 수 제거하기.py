def solution(arr):
    if len(arr) <= 1: return [-1]
    
    arr_copy = arr[:]   # 원본 배열 보호
    arr_copy.remove(min(arr))
    return arr_copy