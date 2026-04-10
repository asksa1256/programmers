def solution(arr, divisor):
    # result = []
    # for i in range(len(arr)):
    #     if arr[i] % divisor == 0:
    #         result.append(arr[i])
    # result.sort()
    # return result if len(result) > 0 else [-1]
    
    return sorted([x for x in arr if x % divisor == 0]) or [-1]