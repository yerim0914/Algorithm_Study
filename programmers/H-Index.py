def solution(citations):
    answer = []
    citiations = sorted(citations)
    index = 0
    for i in range(1, len(citiations)+1):
        while(i > citiations[index]):
            if index == len(citations) - 1:
                break
            index += 1 
        if citiations[i-1] != 0 and i <= len(citiations) - index:
            answer.append(i)
        # if i <= citiations[index]:
        #     if i <= len(citiations) - index:
        #         answer.append(i)
        # else :
        #     index += 1
    if len(answer) == 0:
        answer = 0
    else:
        answer = max(answer)
    return answer

print(solution([0, 1, 3, 5, 6]))
print(solution([10, 10, 10, 10, 10]))
print(solution([1,4]))
print(solution([0, 0, 0, 0, 0]))
