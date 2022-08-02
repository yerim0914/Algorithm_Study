def solution(n):
    answer = []
    n = list(str(n))
    for i in range(0, len(n)):
        answer.append(int(n[len(n)-i-1]))
    return answer