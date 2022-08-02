def solution(arr, divisor):
    answer = []
    for i in range(0, len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        return [-1]
    return sorted(answer)