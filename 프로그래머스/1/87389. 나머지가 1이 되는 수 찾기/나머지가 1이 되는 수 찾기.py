def solution(n):
    # 일단 for문 안에서 2부터 1씩 증가
    # 증가할 때마다 n과 나눠보고,
    # 나머지가 1이면 min에 값 할당
    # 이전 min값보다 작은지 체크할 필요가 있나?
    for i in range(2, n):
        if (n % i == 1):
            return i
        else:
            continue