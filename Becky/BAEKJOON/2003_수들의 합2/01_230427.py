# 문제: https://www.acmicpc.net/problem/2003
n, m = map(int, input().split())
lst = list(map(int, input().split()))

l, r = 0, 1
cnt = 0

while r<=n and l<=r:
    total = sum(lst[l:r])

    if total < m:
        r += 1
    elif total > m:
        l += 1
    else:
        cnt += 1
        r += 1

print(cnt)