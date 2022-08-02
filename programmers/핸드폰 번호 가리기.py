def solution(phone_number):
    answer = ''
    lenP = len(phone_number)
    for i in range(0, lenP-4):
        answer += '*'
    for j in range(lenP-4, lenP):
        answer += phone_number[j]
    return answer