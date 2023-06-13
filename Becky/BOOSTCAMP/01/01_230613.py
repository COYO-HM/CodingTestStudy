# 1. function
def solution(arr):
    answer = []
    dic = {}
    arr.sort()

    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1

    for i, v in dic.items():
        if v > 1:
            answer.append(v)

    if len(answer) == 0:
        answer = [-1]
    return answer

# solution([1, 2, 3, 3, 3, 3, 4, 4])
# solution([3, 2, 4, 4, 2, 5, 2, 5, 5])
# solution([3, 5, 7, 9, 1])