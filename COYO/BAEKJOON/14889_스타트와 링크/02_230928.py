import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
ans = int(1e9)
player = list(range(n))
team = combinations(player, n // 2)

graph = [list(map(int, input().split())) for _ in range(n)]

def calcPoint(arr):
    arr.sort()
    cnt = 0
    for i in range(n // 2 - 1):
        for j in range(i + 1, n // 2):
            cnt += graph[arr[i]][arr[j]] + graph[arr[j]][arr[i]]
    return cnt

for t in team:
    a = calcPoint(list(t))
    b = calcPoint(list(set(player) - set(t)))
    # print(list(t), list(set(player) - set(t)), abs(a - b))
    ans = min(abs(a - b), ans)

print(ans)