def solution(N, stages):
<<<<<<< HEAD
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
=======
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
>>>>>>> 4f6b4a01969ca2c20b3cc6950e047be2d4ac91fe
