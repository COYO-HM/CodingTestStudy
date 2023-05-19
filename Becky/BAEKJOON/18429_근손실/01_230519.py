# 문제: https://www.acmicpc.net/problem/18429

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
weight = 500

kits = permutation(kit, n)

cnt = 0
for w in kits:
    for i in range(len(w)):
        weight += w[i] - k

        if weight < 500:
            break
    else:
        cnt += 1
print(cnt)