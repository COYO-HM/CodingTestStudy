def solution(arr):
    nums = set(arr)
    ans = []
    for n in nums:
        cnt = arr.count(n)
        if cnt > 1:
            ans.append(cnt)
    if len(ans) == 0:
        ans.append(-1)
    print(ans)

solution([1, 2, 3, 3, 3, 3, 4, 4])
solution([3, 2, 4, 4, 2, 5, 2, 5, 5])
solution([3, 5, 7, 9, 1])