def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        answer += a[i] * b[i]
    print(answer)
    return answer


solution([1,2,3,4], [-3,-1,0,2])