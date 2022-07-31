def solution(n):
    nlist = list(str(n))
    # nlist = list(map(int, list(str(n))))
    answer = 0
    for i in range(0, len(nlist)):
        answer += int(nlist[i])
    print(answer)
    return answer
solution(123)