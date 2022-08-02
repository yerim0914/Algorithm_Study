def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i+1):
            if j == i:
                answer += 1
            if i % j == 0:
                break
    return answer

solution(10)