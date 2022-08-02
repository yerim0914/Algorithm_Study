def solution(arr):
    arr = list(arr)
    minValue = min(arr)
    if len(arr) == 1:
        return [-1]
    for i in range(0, len(arr)):
        if minValue == arr[i]:
            arr.pop(i)
            break
    return arr