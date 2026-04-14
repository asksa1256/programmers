def solution(s):
    mid = int(len(s)/2)
    if len(s) % 2 == 0:
        return s[mid-1] + s[mid]
    else:
        return s[mid]