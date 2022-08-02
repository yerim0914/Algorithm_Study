def solution(x):
    answer = True
    xx = list(str(x))
    sumX = 0
    for i in xx:
        sumX += int(i)
    if x % sumX != 0:
        answer = False
    return answer