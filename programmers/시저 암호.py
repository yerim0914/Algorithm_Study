def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        if s[i].isspace():
            answer += ' '
        elif s[i].islower():
            imsi = s[i].upper()
            if (ord(imsi) + n) >= 90:   
                answer += chr(ord(imsi)+n-25+31)
            else:
                answer += chr(ord(imsi)+n+32)
                 
        else:
            if (ord(s[i]) + n) >= 90:   
                answer += chr(ord(s[i])+n-25)
            else:
                answer += chr(ord(s[i])+n)
    print(answer)     
    return answer
solution("A", 25)