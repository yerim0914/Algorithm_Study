def solution(scoville, K):
    answer = 0
    scoville = list(scoville)
    while min(scoville) < K:
        scoville.sort()
        scoville.insert(0, scoville.pop(0) + scoville.pop(0)*2)
        answer += 1
    return answer

print(solution([1,2,3,9,10,12], 7))