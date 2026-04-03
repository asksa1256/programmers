def solution(num):
    return num + sum([i for i in range(1, (num // 2)+1) if num % i == 0])
# num / 2: 2로 나눈 값을 float로 반환 
# num // 2: 2로 나눈 값을 정수로 반환 