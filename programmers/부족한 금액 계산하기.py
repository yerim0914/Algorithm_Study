def solution(price, money, count):
    answer = -1
    sumP = 0
    for i in range(1, count+1):
        sumP += price * i
    if sumP < money:
        answer = 0
    else :
        answer = sumP - money
    return answer