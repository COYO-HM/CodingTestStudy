# 문제: https://www.acmicpc.net/problem/18429
# 변수 초기화에 신경 쓸 것
def permutation(lst, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(lst)):
        perm = lst[i]
        for rest in permutation(lst[:i] + lst[i+1:], n-1):
            result.append([perm] + rest)

    return result
# ========================================================
n, k = map(int, input().split())
kit = list(map(int, input().split()))

kits = permutation(kit, n)

cnt = 0
for w in kits:
    weight = 500
    for i in w:
        weight += i - k

        if weight < 500:
            break
    else:
        cnt += 1
print(cnt)