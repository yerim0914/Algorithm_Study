def solution(n, m):
    answer = []
    i = max(n, m)
    j = min(n, m)
    rig = 0
    lef = 0
    while 1:
        if i % m == 0 and i % n == 0:
            rig = i
            break
        i += 1
    lef = n * m / rig
    return [lef, rig]