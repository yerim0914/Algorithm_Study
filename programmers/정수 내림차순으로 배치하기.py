def solution(n):
    result = ''
    answer = list(str(n))
    answer.sort(reverse=True)
    for i in range(0, len(answer)):
        result += answer[i]
    return int(result)

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))