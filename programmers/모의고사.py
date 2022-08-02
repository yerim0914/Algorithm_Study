def solution(answers):
    answer = []
    count = [0,0,0]
    one = [1, 2, 3, 4, 5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    i = 0
    print(6%5)
    while i < len(answers):
        # print(i % len(one))
        if answers[i] == one[i % len(one)]:
            count[0] += 1
        if answers[i] == two[i % len(two)]:
            count[1] += 1
        if answers[i] == three[i % len(three)]:
            count[2] += 1
        i += 1
    maxValue = max(count)
    for i in count:
        if i >= maxValue:
            answer.append(i)
    return answer

solution([1,2,3,4,5,1,2,3,4,5,1])