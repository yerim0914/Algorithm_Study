def solution(n):
    answer = 0
    x = 1
    while 1:
        if n % x == 1:
            answer = x
            break
        x += 1
    return answer

solution(10)