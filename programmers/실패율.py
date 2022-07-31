def solution(N, stages):
    answer = []
    temp = {}
    saram = len(stages)
    for i in range(1, N + 1):
        f = stages.count(i)
        
        temp[i] = f / (saram)
        saram -= f
    temp = sorted(temp, key=lambda x: temp[x], reverse=True)
    print(temp)
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])