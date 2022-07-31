def solution(nums):
    answer = 0
    n = int(len(nums) / 2)
    collect = {nums[0]}
    for i in range(0, len(nums)):
        collect.add(nums[i])
    if len(collect) > n:
        answer = n
    else:
        answer = len(collect)
    print(answer)
    return answer

solution([3,3,3,2,2,4])