def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = list(new_id)
    for i in new_id:
        if i.islower() == True or i == '-' or i == '_' or i == '.':
            answer += i
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    answer = answer.strip('.')
    if len(answer) == 0:
        answer = 'a'
    if len(answer) > 15:
        answer[0:15]
    answer = answer.strip('.')
    while len(answer) <= 2:
        answer += answer[-1]
    
solution('...!@BaT#*..y.abcdefghijklm')