from math import sqrt
def solution(n):
    answer = 0
    sq = sqrt(n)
    if int(sq) == sq:
        answer = (sq + 1) * (sq + 1)
    else :
        answer = -1
    return int(answer)
solution(121)