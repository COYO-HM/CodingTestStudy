# https://www.acmicpc.net/problem/1138
# 14:35-15:00
N = int(input())
people = list(map(int, input().split()))
ans = [-1] * N

for i in range(N):
    taller = people[i]
    j = 0

    while taller > 0 or ans[j] != -1:
        if ans[j] == -1:
            taller -= 1
        j += 1
    ans[j] = i + 1

print(*ans)
