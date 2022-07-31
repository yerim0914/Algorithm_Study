def solution(priorities, location):
    answer = 0
    dic = {}
    for i in range(0, len(priorities)):
        if priorities[i-1] > priorities[i]:
            dic[i] = priorities[i]

    answer = dic[location]
    return answer
solution([1, 1, 9, 1, 1, 1], 0)