def solution(s):
    answer = ''
    answer = sorted(s, key = lambda x : x, reverse=True)
    return ''.join(answer)