def solution(s):
    answer = ''
    s = list(s)
    j = 0
    for i in range(0, len(s)):
        if s[i].isspace():
            j = 0
            answer += ' '
        else: 
            if j % 2 == 0 : # 짝수
                answer += s[i].upper()
            else :
                answer += s[i].lower()
            j += 1
    return answer

solution("try hello world")