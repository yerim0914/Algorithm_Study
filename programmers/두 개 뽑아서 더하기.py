def solution(numbers):
    answer = []
    lst = []
    idx = 1
    left = 0
    while left < len(numbers):
        for i in range(idx, len(numbers)):
            lst.append(numbers[left] + numbers[i])
        left += 1
        idx += 1 
    lst.sort()
    for i in lst:
        if i not in answer:
            answer.append(i)
    return answer