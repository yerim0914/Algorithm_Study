def solution(N, stages):
    temp = {}
    saram = len(stages)
    for i in range(1, N + 1):
        if saram != 0:
            f = stages.count(i)
            temp[i] = f / (saram)
            saram -= f
        else:
            temp[i] = 0
    answer = sorted(temp, key=lambda x: temp[x], reverse=True)
    return answer