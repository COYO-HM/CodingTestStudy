# https://www.acmicpc.net/problem/1138
# 11:58-12:27
N = int(input())
peoples = list(map(int, input().split()))
que = [-1 for _ in range(N)]

for i in range(N):
    taller = peoples[i]
    j = 0

    while taller > 0 or que[j] != -1:
        if que[j] == -1:
            taller -= 1
        j += 1
    que[j] = i + 1

print(*que)
