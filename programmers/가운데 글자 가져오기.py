def solution(s):
    answer = ''
    lenS = len(s)
    if lenS % 2 == 0:
        answer = s[int(lenS/2)-1 : int(lenS/2)+1]
    else :
        answer = s[int(lenS/2)]
    return answer