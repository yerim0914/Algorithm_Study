def solution(sizes):
    x = 0
    y = 0
    minList = []
    maxList = []
    for size in sizes:
        minList.append(min(size))
        maxList.append(max(size))
    y = max(minList)
    x = max(maxList)
    return x * y