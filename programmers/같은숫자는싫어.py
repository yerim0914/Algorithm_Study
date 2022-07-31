def solution(arr):
    answer = []
    stack = []
    stack.append(-1)
    for i in range(0, len(arr)):
        if(stack[len(stack)-1] == arr[i]):
            stack.pop()
        else :
            answer.append(arr[i])
        stack.append(arr[i])
    print(answer)
    return answer

solution([1,1,3,3,0,1,1])